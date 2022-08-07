from flask import Flask , request , jsonify
from flask_pymongo import PyMongo
from bson.json_util import Dumps
app = Flask(__name__)
app.secret_key = "secret" #manage the authenticaion the mongodb
app.config["MONGO_URI"] = "mongodb+srv://rianarun:Tech5278@cluster0.go11c.mongodb.net/NetFlixFlask"
mongo = PyMongo(app)
@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/addPrograms", methods=["POST"])
def addPrograms():
    _json = request.json
    name = _json["name"]    
    programType = _json["programType"]
    programId = int(_json["programId"])
    ImageSrc = _json["imageSrc"]
    trailerLink = _json("trailerLink")
    videoLink = _json("videoLink")
    uaRating = _json("uaRating")
    description =_json("description")
    castInfo = _json("castInfo")
    creatorInfo = _json("creatorInfo")
    yearOfMaking = _json("yearOfMaking")
    genre = _json("genre")
    seasonsNo = _json("seasonNo")
    return jsonify("Added Successfully")
    print("name,programType")
    dataInsert = mongo.db.netflixlist.insert_one({
        "name" :name,
        "programType" : programType,
        "programId" : programId,
        "ImageSrc" : ImageSrc,
        "trailerLink" : trailerLink, 
        "videoLink" : videoLink,
        "uaRating" : uaRating,
        "description": description,
        "castInfo" :castInfo,
        "creatorInfo" :creatorInfo,
        "yearOfMaking" : yearOfMaking, 
        "genre" : genre
        "seasonsNo":seasonsNo,  
    })
    
    
    @app.route("/getMovieDetails" , methods=["GET"])
    def getDetails():
        allDetail=mongo.db.netflixlist.find()
        resp=dumps(allDetail)
        return resp
    
    @app.route("/getMovieId/<int:id>" , methods=["GET"])
    def getMovieId(id):
        allDetail=mongo.db.netflixlist.find_one({"programId":id})
        resp=dumps(allDetail)
        return resp
            
            

if __name__ == "__main__":
        app.run(port = 3000)