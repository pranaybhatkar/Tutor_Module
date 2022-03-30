	window.onload = function() {
	const url = 'http://localhost:8000/'

	// fetch("http://127.0.0.1:8000/CS_IT_Count").then((Response) => {
	//             return Response.json()
	//         }).then((data) => {
	//             console.log(data);
	//         })

	 fetch('http://localhost:8000/Tech_Stack_Certifications_Known_By_Students', 
	        {
	        	method: "GET", 
	            // mode: 'cors',
	            headers: {
	                'Content-Type': 'application/json',
	       		
	            }
	        }
	    ).then(function(response) {
	        return response.json()
	    }).then(function(response) {
	    	let labels = []; 
	    response.subject_count.map((data) => {
	    	let single_labels = {};
	    	single_labels.label = data[0];
	    	single_labels.y = data[1];
	    	labels.push(single_labels);
	    	 
	    }); 
	    console.log(labels)
	    var options = {
		title: {
			text: "Tech-Stack and Number of students:"
		},
		data: [{
				type: "pie",
				startAngle: 45,
				showInLegend: "true",
				legendText: "{label}",
				indexLabel: "{label} ({y})",
				yValueFormatString:"#,##0.#"%"",
				dataPoints: labels
		}]
	};
	$("#chartContainer").CanvasJSChart(options);


	    }).catch((err) => {
	        console.log(err)
	        })

	 fetch('http://localhost:8000/Shortlisting_the_subjects', 
	        {
	        	method: "GET", 
	            // mode: 'cors',
	            headers: {
	                'Content-Type': 'application/json',
	       		
	            }
	        }
	    ).then(function(response) {
	        return response.json()
	    }).then(function(response) {
	    	let labels = []; 
	    response.shortlist.map((data) => {
	    	let single_labels = {};
	    	single_labels.label = data[0];
	    	single_labels.y = data[1];
	    	labels.push(single_labels);
	    	 
	    }); 
	    console.log(labels)
	    var options = {
		title: {
			text: "Shortlisted Subjects:"
		},
		data: [{
				type: "pie",
				startAngle: 45,
				showInLegend: "true",
				legendText: "{label}",
				indexLabel: "{label} ({y})",
				yValueFormatString:"#,##0.#"%"",
				dataPoints: labels
		}]
	};
	$("#chartContainer_1").CanvasJSChart(options);


	    }).catch((err) => {
	        console.log(err)
	        })
	    

	 fetch('http://localhost:8000/Weightage_per_Subject', 
	        {
	        	method: "GET", 
	            // mode: 'cors',
	            headers: {
	                'Content-Type': 'application/json',
	       		
	            }
	        }
	    ).then(function(response) {
	        return response.json()
	    }).then(function(response) {
	    	console.log(response.weightage)
	    	let row = '<tr><th>Subjects</th><th>Weightage</th></tr>'
	    	response.weightage.map((data) => {
	    		row += `<tr><td>${data[0]}</td><td>${data[1]}</td></tr>`
	    		console.log(row);
	    	
	    	})	
	    	    document.getElementById('table').innerHTML = row
	    	    // element.innerHTML(row)

	    }).catch((err) => {
	        console.log(err);
	        }) 

	fetch('http://localhost:8000/Time_Period_per_Subject', 
	        {
	        	method: "GET", 
	            // mode: 'cors',
	            headers: {
	                'Content-Type': 'application/json',
	       		
	            }
	        }
	    ).then(function(response) {
	        return response.json()
	    }).then(function(response) {
	    	console.log(response.Time)
	    	let row = '<tr><th>Subjects</th><th>Time alloted</th></tr>'
	    	response.Time.map((data) => {
	    		row += `<tr><td>${data[0]}</td><td>${data[1]}</td></tr>`
	    		console.log(row);
	    	
	    	})	
	    	    document.getElementById('table_1').innerHTML = row
	    	    // element.innerHTML(row)

	    }).catch((err) => {
	        console.log(err);
	        }) 

	}

