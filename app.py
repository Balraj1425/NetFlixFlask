from bson.json_util import dumps
from flask import Flask,request,jsonify
from flask_pymongo import PyMongo

app=Flask(__name__)

app.secret_key="secret"
app.config["MONGO_URI"]="mongodb+srv://Sahil:RFlAvskVarU0ONWN@cluster0.pabqvip.mongodb.net/NetflixList?retryWrites=true&w=majority"
mongo=PyMongo(app)
@app.route("/hello")
def hello():
    return "hello world"


@app.route("/addProgram", methods=["POST"])
def addProgram():
    
   _json= request.json
   name=_json["name"]
   programtype=_json["programtype"]
   programId=_json["programId"]
   imageSrc=_json["imageSrc"]
   videoLink=_json["videoLink"]
   uaRating=_json["uaRating"]
   description=_json["description"]
   castInfo=_json["castInfo"]
   creatorInfo=_json["creatorInfo"]
   yearOfMaking=_json["yearOfMaking"]
   genre=_json["genre"]
   noOfSeasons=_json["noOfSeasons"]

  
   dataInsert=mongo.db.netflix.insert_one({"name": name, 
	"programType":programtype,
	"programId":programId,
	"imageSrc":imageSrc,
	"videoLink":videoLink,
	"uaRating":uaRating,
	"description":description,
	"castInfo":castInfo,
	"creatorInfo":creatorInfo,
	"yearOfMaking":yearOfMaking, 
	"genre":genre,
	"noOfSeasons":noOfSeasons})
    
   print(programtype)
   return jsonify("added succesfully")
@app.route("/getmovielist", methods=["GET"])
def allDetails():
    alldetails=mongo.db.netflix.find()
    resp=dumps(alldetails)
    return resp
@app.route("/getMovieid/<int:id>", methods=["GET"])
def getMovieId(id):
    alldetails=mongo.db.netflix.find_one({'programId':id})
    resp=dumps(alldetails)
    return resp





app.run(port=3000, debug=True)