from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret"
app.config["MONGO_URI"] = "mongodb+srv://balraj:yXcJhuzMOTrYB9rp@cluster0.ewdz4tn.mongodb.net/NetflixFlask?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/hello")
def hello():
    return "hello World"

@app.route("/addProgram", methods=["POST"])
def addProgram():
    _json = request.json
    name = _json["name"]
    programType = _json["programType"]
    programId = _json["programId"]
    imageSrc = _json["imageSrc"]
    trailerLink = _json["trailerLink"]
    videoLink = _json["videoLink"]
    uaRating = _json["uaRating"]
    description = _json["description"]
    castInfo = _json["castInfo"]
    creatorInfo = _json["creatorInfo"]
    yearOfMaking = _json["yearOfMaking"]
    genre = _json["genre"]
    noOfSeasons = _json["noOfSeasons"]

    dataInsert = mongo.db.netflixlist.insert_one({
        "name": name, 
        "programType":programType,
        "programId":programId,
        "imageSrc":imageSrc,
        "trailerLink":trailerLink,
        "videoLink":videoLink,
        "uaRating":uaRating,
        "description":description,
        "castInfo":castInfo,
        "creatorInfo":creatorInfo,
        "yearOfMaking":yearOfMaking, 
        "genre":genre,
        "noOfSeasons":noOfSeasons
    })

    print(name, programType, imageSrc,castInfo)
    return jsonify("added succesfully")

if __name__ == "__main__":
    app.run(port = 3000)
