var myMap = L.map("map", {
  center: [40, -15],  zoom: 2
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

function markerSize(cases) {
  return cases;
}

const url = "http://127.0.0.1:5000/project2/data/confirmed";
// Fetch the JSON data and console log it
d3.json(url).then(function(data) {  
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
  
  
 