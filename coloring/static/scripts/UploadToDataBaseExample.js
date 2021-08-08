function login(username, password) {
    console.log("456")
    var settings = {
        "url": "http://localhost:8000/login?username=" + username + "&" + "password=" + password,
        "method": "GET",
        "timeout": 0,
        "Access-Control-Allow-Origin":"*",
        headers: {
            "charset":"UTF-8",
            "Access-Control-Allow-Origin":'http://localhost:8080',
            "Access-Control-Allow-Credentials":"true",
          }
      };
      
      $.ajax(settings).done(function (response) {
        //WRITE YOUR CODE HERE
        console.log(response);
      });
}

function uploadText(LastPart_Language, Genre, Name_Of_Writters, Story_Content, Story_Summary) {
    var Name_Of_Writters_Str = ""
    for (const v of Name_Of_Writters) {
        Name_Of_Writters_Str += String(v) + "."
    }
    Name_Of_Writters_Str = Name_Of_Writters_Str.substring(0, Name_Of_Writters_Str.length - 1)
    var settings = {
        "url": "http://localhost:8000/coloring/uploadText",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
          "LastPart_Language": LastPart_Language,
          "Genre": Genre,
          "Name_Of_Writters": Name_Of_Writters_Str,
          "Story_Content": Story_Content,
          "Story_Summary": Story_Summary
        }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}

function getText(filename) {
    var settings = {
        "url": "http://localhost:8000/getText?filename=" + filename,
        "method": "GET",
        "timeout": 0,
      };
      
    //   {
    //     "result": 0,
    //     "msg": "Get Success",
    //     "text": "\"cross the firewall and go to the world\""
    //   }
      $.ajax(settings).done(function (response) {
        //WRITE YOUR CODE HERE
        console.log(response);
      });
}