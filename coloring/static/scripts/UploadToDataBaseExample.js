function newStory(LastPart_Language, Genre, Name_Of_Writters, Story_Content, Story_Summary,cb) {
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
          "Story_Summary": Story_Summary,
          "Finished": "0"
        }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        return cb();
      });
}

function replaceStory(token, last_Part_Language, genre, newWriter, storyContent, StorySummary, finished,cb) {
    var Name_Of_Writters_Str = ""
            for (const v of newWriter) {
                Name_Of_Writters_Str += String(v) + "."
            }
            Name_Of_Writters_Str = Name_Of_Writters_Str.substring(0, Name_Of_Writters_Str.length - 1)
    var settings = {
        "url": "http://localhost:8000/coloring/replaceText",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
          "LastPart_Language": last_Part_Language,
          "Genre": genre,
          "Name_Of_Writters": Name_Of_Writters_Str,
          "Story_Content": storyContent,
          "Story_Summary": StorySummary,
          "Finished": finished,
          "Article_ID": token
        }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        return cb()
      });
}

function getToken(genre, language, cb) {
    var settings = {
        "url": "http://localhost:8000/coloring/getTokenByInfo?Language=" + language + "&Genre=" + genre,
        "method": "GET",
        "timeout": 0,
      };
      $.ajax(settings).done(function (response) {
        if (response.result == 0) {
            //RETURN A LIST OF ID, U NEED TO RANDOM CHOOSE ONE
            return cb(response.id)
        } else return cb(-1)
      });
}


function getTokenRandom(cb) {
  var settings = {
      "url": "http://localhost:8000/coloring/getTokenGallery",
      "method": "GET",
      "timeout": 0,
    };
    $.ajax(settings).done(function (response) {
      if (response.result == 0) {
          //RETURN A LIST OF ID, U NEED TO RANDOM CHOOSE ONE
          return cb(response.id)
      } else return cb(-1)
    });
}

function getStory(token,cb) {
    var settings = {
        "url": "http://localhost:8000/coloring/getText?id=" + token,
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        if (response.result == 0) {
            return cb(response.Story)
        } else return cb(-1)
      });
}

function getSummary(token,cb) {
    var settings = {
        "url": "http://localhost:8000/coloring/getText?id=" + token,
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        if (response.result == 0) {
            return cb(response.Summary)
        } else return cb(-1)
      });
}

function getWriters(token,cb) {
    var settings = {
        "url": "http://localhost:8000/coloring/getText?id=" + token,
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        if (response.result == 0) {
            return cb(response.Writters)
        } else return cb(-1)
      });
}

function getAll() {
    var settings = {
        "url": "http://localhost:8000/coloring/getAll",
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}
function addLanguage(language_name) {
    var settings = {
        "url": "http://localhost:8000/coloring/addLanguage",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
          "language_name": language_name
        }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}
function getLanguage() {
    var settings = {
        "url": "http://localhost:8000/coloring/getLanguage",
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}
