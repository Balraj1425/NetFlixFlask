from bson.json_util import dumps
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret"
# app.config["MONGO_URI"] = "mongodb+srv://balraj:yXcJhuzMOTrYB9rp@cluster0.ewdz4tn.mongodb.net/NetflixFlask?retryWrites=true&w=majority"
app.config["MONGO_URI"] = "mongodb://localhost:27017/localdb"
mongo = PyMongo(app)


@app.route("/hello")
def hello():
    return jsonify("hello World")


@app.route("/addProgram", methods=["POST"])
def addProgram():
    _json = request.json
    name = _json["name"]
    programType = _json["programType"]
    programId = int(_json["programId"])
    imageSrc = _json["imageSrc"]
    trailerLink = _json["trailerLink"]
    videoLink = _json["videoLink"]
    uaRating = _json["uaRating"]
    description = _json["description"]
    castInfo = _json["castInfo"]
    creatorInfo = _json["creatorInfo"]
    yearOfMaking = int(_json["yearOfMaking"])
    genre = _json["genre"]
    noOfSeasons = _json["noOfSeasons"]

    dataInsert = mongo.db.netflixlist.insert_one({
        "name": name,
        "programType": programType,
        "programId": programId,
        "imageSrc": imageSrc,
        "trailerLink": trailerLink,
        "videoLink": videoLink,
        "uaRating": uaRating,
        "description": description,
        "castInfo": castInfo,
        "creatorInfo": creatorInfo,
        "yearOfMaking": yearOfMaking,
        "genre": genre,
        "noOfSeasons": noOfSeasons
    })

    print(name, programType, imageSrc, castInfo)
    return jsonify("added succesfully")


@app.route("/getMovielist", methods=["GET"])
def allDetails():
    allDetail = mongo.db.netflixlist.find()
    resp = dumps(allDetail)
    return resp


@app.route("/getMovieId/<int:id>", methods=["POST"])
def getMovieId(id):
    allDetail = mongo.db.netflixlist.find_one({"programId": id})
    resp = dumps(allDetail)
    return resp


@app.route("/deleteMovieId/<int:id>", methods=["POST"])
def deleteMovieId(id):
    deleteDeletemovie = mongo.db.netflixlist.delete_one({"programId": id})
    return "Message delete"


@app.route("/updateMovie/<int:id>", methods=["PUT"])
def updateMovie(id):
    _json = request.json
    updateone = mongo.db.netflixlist.update_one(
        {"programId": id}, {'$set': _json})

    print(_json)
    return ("data updated")


@app.route("/updateallMovie/<id>", methods=["PUT"])
def updateallMovie(id):
    _json = request.json
    updateone = mongo.db.netflixlist.update_many(
        {"castInfo": id}, {'$set': _json})

    print(_json)
    return ("data updated")


@app.route("/addContact/", methods=["POST"])
def addContact():
    _json = request.json
    fname = _json["fname"]
    lname = _json["lname"]
    email = _json["email"]
    gender = _json["gender"]
    age = int(_json["age"])

    dataInsertContact = mongo.db.userDetails.insert_one({
        "fname": fname,
        "lname": lname,
        "email": email,
        "gender": gender,
        "age": age
    })

    print(fname, lname, gender, age)
    return jsonify("contact added succesfully")


@app.route("/getalluserlist", methods=["GET"])
def allContactDetails():
    allContactDetails = mongo.db.userDetails.find()
    resp = dumps(allContactDetails)
    return resp


@app.route("/userRegister/", methods=["POST"])
def userRegister():
    _json = request.json
    uname = _json["fname"]
    uemail = _json["email"]
    password = _json["password"]

    dataInsertContact = mongo.db.userRegister.insert_one({
        "fname": uname,
        "email": uemail,
        "password": password
    })

    return jsonify("contact added succesfully")


@app.route("/login", methods=["POST"])
def login():
    _json = request.json
    useremail = _json["useremail"]
    password = _json["password"]

    email_found = mongo.db.userRegister.find_one({"email": useremail})

    if email_found:
        email_val = email_found['email']
        passwrd_val = email_found['password']
        if password == passwrd_val:
            return "login success"
        else:
            return "failed"

    else:
        return "email not found"


if __name__ == "__main__":
    app.run(port=3000, debug=True)
