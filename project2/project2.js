$(".dropdown-item").on("click", function(){

if ($(this).text()=='History') {
    console.log(this)
    $(".h1-title").text("History");
    $("pre").text("COVID-19 is the disease caused by the new coronavirus that emerged in China in December 2019.\n\nThe symptoms include cough, fever, shortness of breath, muscle aches, sore throat, unexplained loss of taste or smell, diarrhea and headache.It can be severe, and some cases have caused death.\n\nThis coronavirus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).");}

if ($(this).text()=='Symptoms') {
    console.log(this)
    $(".h1-title").text("Identify Symptoms");
    $("pre").text("The COVID-19 virus affects different people in different ways. It is a respiratory disease and most infected people will develop mild to moderate symptoms and recover without requiring special treatment.\n\nPeople who have underlying medical conditions and those over 60 years old have a higher risk of developing severe disease and death.\n\nThe common symptoms are: fever, tiredness and dry cough.\n\nThere are other symptoms that might appear and are: shortness of breath, aches and pains, sore throat very few people will report diarrhoea, nausea or a runny nose.");}

if ($(this).text()=='Evolution') {
    console.log(this)
    $(".h1-title").text("COVID-19 Evolution");
    $("pre").text("1234567890qwertyuisdfghjcvbnm");}
})


$(".navbar-li-default-link").on("click", function(){

    if ($(this).text()=='Data Analytics Bootcamp') {
        console.log(this)
        $(".h1-title").text("Introduction");
        $("pre").text("This website was created by students of the Data Analytics Bootcamp 2019-2020 with the objective of showing the effects of COVID-19.");}
    
    })