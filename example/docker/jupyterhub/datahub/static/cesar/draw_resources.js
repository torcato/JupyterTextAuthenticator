var camera, scene, projector, renderer;
var objects = {};

var containerWidth, containerHeight;
var containerLeft = $("#threejs-container").offset().left;
var containerTop = $("#threejs-container").offset().top;
// variable for the timer, waiting time, between getting resources
var resourceInterval = 1000;

google.load("visualization", "1", {packages:["corechart", "table", "gauge"]});
google.setOnLoadCallback(drawCharts);


//data structure with functions to visualize the data
var draw_functions  = {

    table : function(){
        $(this.id).empty();
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.Table(this); 
        visualization.draw(t);
    },

    columnChart : function(){ 
        $(this.id).empty();
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.ColumnChart(this); 
        visualization.draw(t);
    },
    barChart : function(){ 
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.BarChart(this); 
        visualization.draw(t);
    },    
    pieChart : function(){ 
        $(this.id).empty();
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.PieChart(this); 
        visualization.draw(t);
    },
    scatterChart : function(){ 
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.ScatterChart(this); 
        visualization.draw(t);
    },
    gauge : function (){
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.Gauge(this); 
        visualization.draw(t);
    },
    areaChart : function (){ 
        var t = google.visualization.arrayToDataTable(this.raw_resource.data); 
        var visualization = new google.visualization.AreaChart(this); 
        visualization.draw(t);
    }
}

function getResource(id){
    var resource = {}
    jQuery.ajax({
         type: "GET",
         url: "resources/"+id + ".json",
         async : false,
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
            resource = data;
         },
         
         error: function (jqXHR, status) {           
              // error handler
         }
    })
    return resource;
}


init();
render();
animate();

function init() {
	containerWidth = $("#threejs-container").width();
	containerHeight = $("#threejs-container").height();

	camera = new THREE.PerspectiveCamera(40, containerWidth / containerHeight, 1, 10000);
	camera.position.z = 3000;

	scene = new THREE.Scene();

	projector = new THREE.Projector();
	
	renderer = new THREE.CSS3DRenderer();
	renderer.setSize(containerWidth, containerHeight);
	renderer.domElement.style.position = 'absolute';
	document.getElementById('threejs-container').appendChild(
			renderer.domElement);
			
	window.addEventListener('resize', onWindowResize, false);

	$("#threejs-container").on('contextmenu', function() {return false;});
	
}


function createView(res) {
    
	d = document.createElement("div");
	d.id = res.id; // TODO: Turn this into unique table ID
	d.className = "ui-widget-content";
	
	d.style.padding = "0.5em";
	div = d3.select(d);
    div.each(objectify);
    
	$(d).on('mousemove', onMouseMove);
	$(d).on('mousewheel', onTableResize);
	$(d).on('mousedown', onMouseDown);
	$(function() {
		$(d).resizable();
	});
	
    decorateDiv(d,res);
    d.drawResource();
}

function decorateDiv(d, res){
    d.raw_resource = res;
    if (res.render in draw_functions){
        d.drawResource = draw_functions[res.render];
    }
    else{
        d.drawResource = draw_functions['table'];
    }
}

function drawCharts() {
    var resources = getResource("resources");
    for(var i = 0 ; i < resources.length; i ++){
        res = getResource(resources[i] );
        res.id = resources[i];
        createView(res);
    }
    //will run only once
    setInterval(updateResources, resourceInterval);
}

function areArraysEqual(a1, a2) {
    //TODO find a better way of doing this
    return a1.toString() ==a2.toString();
}

function removeResource(id){
    console.log('removing ', id)
    // maybe is not needed to remove the div
    var element = document.getElementById(id);
    element.parentNode.removeChild(element);
    scene.remove(objects[id]);
    delete objects[id];
}

function updateResources(){
    var resources = getResource("resources");
    for(var i = 0 ; i < resources.length; i ++){
        jQuery.ajax({
             type: "GET",
             url: "resources/"+resources[i]+ ".json",
             async : false,
             data: {},
             contentType: "application/json; charset=utf-8",
             dataType: "json",
             success: function (res,  status, jqXHR){
                if (res.id in objects){
                    d = objects[res.id].element;
                    // redraws only if the resource changed
                    if( areArraysEqual(d.raw_resource.data, res.data)==false 
                                || d.raw_resource.render != res.render){
                        console.log('updating div with resource', d);
                        decorateDiv(d,res);
                        d.drawResource();
                    }
                }
                else {
                    console.log('adding new object')
                    // add new objects
                    createView(res);
                }
            },
             error: function (jqXHR, status) {
                console.log("error getting resource list", jqXHR, status)
                removeResource(resources[i]);
             }
        });
    }
    //remove non existing objects
    for(id in objects){
        //console.log(obj);
        if ($.inArray( id, resources) < 0){
            removeResource(id);
        }
    }
}


function onTableResize(event) {
	if (event.originalEvent.wheelDelta > 0) {
		var factor = .1;
	} else {
		var factor = -.1;
	}
	
	objects[this.id].scale.x += factor;
	objects[this.id].scale.y += factor;
}

function objectify(d) {
	var object = new THREE.CSS3DObject(this);
    object.position.x = 0;
    object.position.y = 0;
    object.position.z = 2300;

	scene.add(object);
	
	objects[this.id] = object;
}

function onMouseMove(event) {
    // TODO: Trap movement in the div or document to track fast mouse movements 
    if (event.which === 3 && this.id in objects) {
        var obj = objects[this.id];

        var lastPosition = obj.lastPosition;
        var deltaX = lastPosition.x - event.clientX,
            deltaY = lastPosition.y - event.clientY;
            
        obj.position.x -= deltaX;
        obj.position.y += deltaY;

        lastMoveObj = obj;
        obj.lastPosition ={
            x : event.clientX,
            y : event.clientY
        };
    }
}

var lastObj;
function onMouseDown(event) {
	if (event.which === 3 && this.id in objects) {
	    // remembers here what was the position when the mouse was clicked 
	    var obj = objects[this.id];
	    console.log(obj);
        obj.lastPosition ={
            x : event.clientX,
            y : event.clientY
        };
        
        // does this to put the current object in front of all the others
        if (obj != lastObj & (typeof lastObj != "undefined")){
            obj.position.z = 2300;
            lastObj.position.z = 2299;
            
        }
        lastObj = obj;
	}
}

function onMouseUp(event) {
	if (event.which === 3) {
	}
}

function onWindowResize() {
	containerWidth = $("#threejs-container").width();
	containerHeight = $("#threejs-container").height();
	
	camera.aspect = containerWidth / containerHeight;
	camera.updateProjectionMatrix();

	renderer.setSize(containerWidth, containerHeight);
	render();
}

function animate() {
	requestAnimationFrame(animate);
	render();
}

function render() {
	renderer.render(scene, camera);
}
