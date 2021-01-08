

//vars 

let bodyBackGround = document.querySelector('body');

document.body.style.backgroundImage = "url('/static/Img/gettyimages-1096832854-2048x2048.jpeg')"; 

//function



function backGround ()
{
    let weightclass = document.getElementById('weight');
    let options = weightclass.value;
   
    // if(options == "WelterWeight")
    // {

    // }
    switch(options)
    {
     case "Heavyweight": 
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-884616004-2048x2048.jpeg')"; 
        break;

     case "LightHeavyweight": 
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1204970529-2048x2048.jpeg')"; 
        break;
     case "MiddleWeight":
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1096832854-2048x2048.jpeg')"; 
        break;
        case "WelterWeight": 
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1194027049-2048x2048.jpeg')"; 
        break;

     case "Lightweight":
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1046970976-2048x2048.jpeg')"; 
        break;
     case "featherWeight": 
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-884616004-2048x2048.jpeg')"; 
        break;
     case "BantamWeight":
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-884616004-2048x2048.jpeg')"; 
        break;

     case "flyWeight": 
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1046970976-2048x2048.jpeg')"; 
        break;
     case "strawWeight":
        document.body.style.backgroundImage = "url('/static/Img/gettyimages-1046971010-2048x2048.jpeg')"; 
        break;

     
    
    

    }



}


//event 
let weightclass = document.getElementById('weight');
weightclass.onchange = backGround;
