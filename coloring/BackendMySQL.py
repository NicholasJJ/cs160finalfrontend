import MySQLdb
import hashlib
import django
import cgi
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_api(request):
    return django.http.JsonResponse({
        "result":0,
        "msg":"执行成功"
    })

@csrf_exempt
def login(request):
    if request.method != 'GET':

        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    username, password = request.GET["username"], request.GET["password"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("select User_Password_Hash from UserInformation where User_Name = %s;", (username,))
    data = cursor.fetchone()
    if not data:
        db.close()
        return django.http.JsonResponse({
        "result":-200,
        "msg":"User Not Exist"
    })
    elif str(data[0]) == str(hashlib.sha512(password.encode('utf-8')).hexdigest()).upper():
        return django.http.JsonResponse({
        "result":0,
        "msg":"Login Success",
        "accessToken": str(hashlib.sha512(username.encode('utf-8')).hexdigest()).upper()
    })
    else:
        db.close()
        return django.http.JsonResponse({
        "result":-300,
        "msg":"Password Error"
    })


@csrf_exempt
def register(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    username, password = request.GET["username"], request.GET["password"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT count( * ) FROM UserInformation WHERE `User_Name` = %s;", (username,))
    data = cursor.fetchone()
    hash = str(hashlib.sha512(password.encode('utf-8')).hexdigest()).upper()
    if data[0] != 0:
        db.close()
        return django.http.JsonResponse({
        "result":-400,
        "msg":"User Already Exists"
    })
    else:
        print(hash)
        sql = "INSERT INTO UserInformation (User_Name, User_Password_Hash) VALUES (%s, %s)"
        val = (username, hash)
        cursor.execute(sql , val)
        db.commit()        
        data = cursor.fetchone()
        db.close()
        return django.http.JsonResponse({
        "result":0,
        "msg":"Login Success",
        "accessToken":str(hashlib.sha512(username.encode('utf-8')).hexdigest()).upper()
    })


@csrf_exempt
# def uploadText(request):
#     if request.method != 'POST':
#         return django.http.JsonResponse({
#         "result":-100,
#         "msg":"Parameter Wrong"
#     })
#     accessToken, fileName, fileContent = request.POST.get('accessToken',0), request.POST.get('fileName',0), request.POST.get('fileContent',0)
#     db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
#     cursor = db.cursor()
#     cursor.execute("SELECT count( * ) FROM Articles WHERE `Aritcle_Name` = %s;", (fileName,))
#     data = cursor.fetchone()
#     if data[0] != 0:
#         db.close()
#         return django.http.JsonResponse({
#         "result":-400,
#         "msg":"File Already Exists"
#     })
#     else:
#         print(hash)
#         sql = "INSERT INTO Articles (Aritcle_Name, Article_Owner, Article_Content) VALUES (%s, %s, %s)"
#         val = (str(fileName), str(accessToken), str(fileContent))
#         cursor.execute(sql , val)
#         db.commit()        
#         data = cursor.fetchone()
#         db.close()
#         return django.http.JsonResponse({
#         "result":0,
#         "msg":"Add Success",
#         "accessToken":accessToken
#     })

# @csrf_exempt
# def getText(request):
#     if request.method != 'GET':
#         return django.http.JsonResponse({
#         "result":-100,
#         "msg":"Parameter Wrong"
#     })
#     filename= request.GET["filename"]
#     db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
#     cursor = db.cursor()
#     cursor.execute("SELECT count( * ) FROM Articles WHERE `Aritcle_Name` = %s;", (filename,))
#     data = cursor.fetchone()
#     if data[0] != 1:
#         db.close()
#         return django.http.JsonResponse({
#         "result":-400,
#         "msg":"File Do Not Exists"
#     })
#     else:
#         print(hash)
#         cursor.execute("select Article_Content from Articles where Aritcle_Name = %s;", (filename,))
#         data = cursor.fetchone()
#         db.close()
#         return django.http.JsonResponse({
#         "result":0,
#         "msg":"Get Success",
#         "text": data[0]
#     })

@csrf_exempt
def uploadText(request):
    if request.method != 'POST':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    LastPart_Language, Genre, Name_Of_Writters= request.POST.get('LastPart_Language',0), request.POST.get('Genre',0), request.POST.get('Name_Of_Writters',0)
    Story_Content, Story_Summary, Finished = request.POST.get('Story_Content', 0), request.POST.get('Story_Summary', 0), request.POST.get('Finished', 0)
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    sql = "INSERT INTO `UserInformation`.`Ariticle_Storage` (`LastPart_Language`, `Genre`,`Name_Of_Writters`,`Story_Content`,`Story_Summary`, `Finished`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (str(LastPart_Language), str(Genre), str(Name_Of_Writters), str(Story_Content), str(Story_Summary), Finished)
    cursor.execute(sql , val)
    db.commit()
    db.close()
    return django.http.JsonResponse({
        "result":0,
        "msg":"Add Success"
    })

@csrf_exempt
def replaceText(request):
    if request.method != 'POST':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    Article_ID = request.POST.get('Article_ID', 0)
    LastPart_Language, Genre, Name_Of_Writters= request.POST.get('LastPart_Language',0), request.POST.get('Genre',0), request.POST.get('Name_Of_Writters',0)
    Story_Content, Story_Summary, Finished= request.POST.get('Story_Content', 0), request.POST.get('Story_Summary', 0), request.POST.get('Finished', 0)
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    print(Article_ID)
    cursor.execute("delete from Ariticle_Storage where Article_ID = %s", (Article_ID,))
    db.commit()
    sql = "REPLACE INTO `UserInformation`.`Ariticle_Storage` (`Article_ID`, `LastPart_Language`, `Genre`,`Name_Of_Writters`,`Story_Content`,`Story_Summary`,`Finished`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Article_ID, str(LastPart_Language), str(Genre), str(Name_Of_Writters), str(Story_Content), str(Story_Summary), Finished)
    cursor.execute(sql , val)
    db.commit()
    db.close()
    return django.http.JsonResponse({
        "result":0,
        "msg":"Add Success"
    })

@csrf_exempt
def getText(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    id= request.GET["id"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT count( * ) FROM Ariticle_Storage WHERE `Article_ID` = %s;", (id,))
    data = cursor.fetchone()
    if data[0] < 1:
        db.close()
        return django.http.JsonResponse({
        "result":-400,
        "msg":"File Do Not Exists"
    })
    else:
        cursor.execute("select * from Ariticle_Storage where Article_ID = %s;", (id,))
        data = cursor.fetchone()
        print(data)
        db.close()
        return django.http.JsonResponse({
        "result":0,
        "msg":"Get Success",
        "Story": data[4],
        "Summary": data[5],
        "Writters": data[3].split(".")
    })


@csrf_exempt
def getTokenByInfo(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    req = "SELECT Article_ID FROM UserInformation.Ariticle_Storage where LastPart_Language = %s and Genre = %s"
    params = (request.GET["Language"], request.GET["Genre"])
    cursor.execute(req, params)
    data = cursor.fetchall()
    if (data == None) :
        return django.http.JsonResponse({
            "result": 404,
            "msg": "No Article Fulfill this requirement",
            "id": -1
        })
    else:
        results = [i[0] for i in data]
        return django.http.JsonResponse({
            "result": 0,
            "msg": "Success",
            "id": results
        })

@csrf_exempt
def getTokenGallery(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    req = "SELECT Article_ID FROM UserInformation.Ariticle_Storage where Finished = 1"
    cursor.execute(req)
    data = cursor.fetchall()
    if (data == None) :
        return django.http.JsonResponse({
            "result": 404,
            "msg": "No Article Fulfill this requirement",
            "id": -1
        })
    else:
        results = [i[0] for i in data]
        return django.http.JsonResponse({
            "result": 0,
            "msg": "Success",
            "id": results
        })

@csrf_exempt
def getAll(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    req = "SELECT * FROM UserInformation.Ariticle_Storage"
    cursor.execute(req)
    data = cursor.fetchall()
    return django.http.JsonResponse({
        "result": 0,
        "msg": "GotCha",
        "id": data
        })