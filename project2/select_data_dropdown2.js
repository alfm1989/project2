const url = "http://127.0.0.1:5000/project2/data/status";

/* function init() {
    data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 2, 4, 8, 16] }];
  
    Plotly.newPlot("plot", data);
} */


var Confirmed=[];
var Death=[];
var Recovered=[];
var Identifier=[];
var x= [];
var y= [];



/* var layout = {
    xaxis: {
      showgrid: true,
      zeroline: true,
      showline: true,
      mirror: 'ticks',
      gridcolor: '#bdbdbd',
      gridwidth: 2,
      zerolinecolor: '#969696',
      zerolinewidth: 4,
      linecolor: '#636363',
      linewidth: 6
    },
    yaxis: {
      showgrid: true,
      zeroline: true,
      showline: true,
      mirror: 'ticks',
      gridcolor: '#bdbdbd',
      gridwidth: 2,
      zerolinecolor: '#969696',
      zerolinewidth: 4,
      linecolor: '#636363',
      linewidth: 6
    }
}; */

d3.selectAll("#selDataset").on("change", updatePlotly1);
// d3.selectAll("#selDataset2").on("change", updatePlotly2);

// Fetch the JSON data and console log it
d3.json(url).then(function(data){
    
    //console.log(data);
    

    for (i=3;i<data.length;i++){
        var v_id=data[i].identifier;
        var v_conf=data[i].confirmed;
        var v_dea=data[i].death;
        var v_recov=data[i].recovered;
        
        Identifier.push(v_id)
        Confirmed.push(parseInt(v_conf))
        Death.push(parseInt(v_dea))
        Recovered.push(parseInt(v_recov))
        
    }
   
    for (i=0;i<Identifier.length-1;i++){
        var v_id=Confirmed[i];
        var v_conf=i+1;
        
        x.push(v_id)
        y.push(v_conf)
    }

    var data=[{x:Identifier,
      y:Confirmed}];

    Plotly.newPlot("plot", data);
    //Plotly.newPlot("plot", "y", [Confirmed]);

});

console.log(Identifier)
console.log(Confirmed)
console.log(Death)
console.log(Recovered)
console.log(x)
console.log(y)


//init();

 
function updatePlotly1() {
//     // Use D3 to select the dropdown menu
  
    var dropdownMenu = d3.select("#selDataset");
     // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
  
//     // Initialize x and y arrays
   var x = [];
   var y = [];
  

  
   /* for (i=0;i<Identifier.length;i++){
     var v_id=Confirmed[i];
     var v_conf=i+1;
       
     x.push(v_id)
     y.push(v_conf)
        
   } */
  
   console.log(dataset)
   if (dataset === 'dataset1') {
    var data=[{x:Identifier,
      y:Confirmed}]; 
      Plotly.newPlot("plot", data);  
    }
  

  
   if (dataset === 'dataset2') {
    var data=[{x:Identifier,
      y:Recovered}];
      Plotly.newPlot("plot", data);
   }

   if (dataset === 'dataset3') {
    var data=[{x:Identifier,
      y:Death}];
      Plotly.newPlot("plot", data);
   } 

  

    //Plotly.newPlot("plot", data);
   //Plotly.newPlot("plot", "y", [y]);
};