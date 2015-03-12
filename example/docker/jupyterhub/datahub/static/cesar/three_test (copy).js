		var camera, scene, projector, renderer;
		
		var objects = {};
		var lastPosition = {};
		
		var containerWidth, containerHeight;
		var containerLeft = $("#threejs-container").offset().left;
		var containerTop = $("#threejs-container").offset().top;
		
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

// 			controls = new THREE.TrackballControls(camera, renderer.domElement);
// 			controls.rotateSpeed = 0.5;
// 			controls.minDistance = 500;
// 			controls.maxDistance = 6000;
// 			controls.addEventListener('change', render);

 			window.addEventListener('resize', onWindowResize, false);

 			$("#threejs-container").on('contextmenu', function() {return false;});
 			
			var people = [
			    {name: "Jill", age: 30},
			    {name: "Bob", age: 32},
			    {name: "George", age: 29},
			    {name: "Sally", age: 31}
			];
			
			tabulate(people, ["name", "age"]);
		}
		
		
		function tabulate(data, columns) {			
			//var table = d3.selectAll(".element").data([0]).enter().append("table").attr("class", "element");
			//var div = d3.selectAll(".element").data([0]).enter().append("div").attr("class", "element");
			d = document.createElement("div");
			d.id = "element"; // TODO: Turn this into unique table ID
			d.className = "ui-widget-content";
			
			//div = d3.select(d);
			//div = d3.selectAll("div.element");
			div = d3.select(d);
			
			var table = div.append("table");
			var thead = table.append("thead");
			var tbody = table.append("tbody");

		    // append the header row
		    thead.append("tr")
		        .selectAll("th")
		        .data(columns)
		        .enter()
		        .append("th")
		            .text(function(column) { return column; });

		    // create a row for each object in the data
		    var rows = tbody.selectAll("tr")
		        .data(data)
		        .enter()
		        .append("tr");

		    // create a cell in each row for each column
		    var cells = rows.selectAll("td")
		        .data(function(row) {
		            return columns.map(function(column) {
		                return {column: column, value: row[column]};
		            });
		        })
		        .enter()
		        .append("td")
		            .text(function(d) { return d.value; });
		    
		    div.each(objectify);
		    
		    /*
			alert('div is ' + div.className);
			alert('div0 is ' + div[0].className);
			alert('div00 is ' + div[0][0].className);

			
		    object = new THREE.CSS3DObject(div[0][0]);//'[0][0]);
		    //object.rotation.x = -20;
		    scene.add(object);
		    
			
			//div.on('mousemove', onTableMove);	
			//$(document).on('mousedown', onTableDown);
			*/
			
			d.style.padding = "0.5em";
			
			//$(d).on('mousedown', onMouseDown);
			//$(d).on('mouseup', onMouseUp);
			$(d).on('mousemove', onMouseMove);		
			$(d).on('mousewheel', onTableResize);
			
			$(function() {
				$(d).resizable();
			});
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
			    if (typeof lastPosition.x != "undefined") {
			        var deltaX = lastPosition.x - event.clientX,
			            deltaY = lastPosition.y - event.clientY;

			        objects[this.id].position.x -= deltaX;
			        objects[this.id].position.y += deltaY;
			    } 
				lastPosition.x = event.clientX;
				lastPosition.y = event.clientY;
			}
		}

		function onMouseDown(event) {
			if (event.which === 3 && this.id in objects) {
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
