/*  var myMap = L.map("map", {
  center: [40, -15],  zoom: 2
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap); */

/* var pane1 = myMap.createPane('markers1');
var pane2 = myMap.createPane('markers2'); */



var myMap = L.map("map", {
  center: [40, -15],
  zoom: 2
});

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: 'pk.eyJ1IjoiYWRyaWxmbSIsImEiOiJjazkza2RxOXUwMzZrM2VudWRzaWhtYm80In0.y0pAR7Md3lRKHCnJHhYkkw'
}).addTo(myMap);

function markerSize(cases) {
  return cases;
}

d3.selectAll("#selDataset").on("change", updatePlotly1);
var url1='';
function updatePlotly1() {
  //     // Use D3 to select the dropdown menu
    
      var dropdownMenu = d3.select("#selDataset");
       // Assign the value of the dropdown menu option to a variable
      var dataset = dropdownMenu.property("value");
    
  //     // Initialize x and y arrays
    
     console.log(dataset)
     if (dataset === 'dataset1') {
      url1 = "http://127.0.0.1:5000/project2/data/confirmed";
      
 
      }
    
     if (dataset === 'dataset2') {
      url1 = "http://127.0.0.1:5000/project2/data/recovered";
      
  
     }
  
     if (dataset === 'dataset3') {
      url1 = "http://127.0.0.1:5000/project2/data/death";
        
     } 
  
     d3.json(url1).then(function(data) {  
      for (var i = 0; i < data.length; i++) {
        L.circle([data[i].Lat, data[i].Long], {
          fillOpacity: 0.75,
          color: "red",
          fillColor: "red",
          // Setting our circle's radius equal to the output of our markerSize function
          // This will make our marker's size proportionate to its population
          radius: markerSize(data[i].April_22)
        }).bindPopup("<h1>" + data[i].pais + "</h1> <hr> <h3>Total confirmed cases: " + data[i].April_22 + "</h3>").addTo(myMap);
      }
    })
 };

// Fetch the JSON data and console log it

 