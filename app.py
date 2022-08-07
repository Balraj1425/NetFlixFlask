from flask import Flask , request , jsonify
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/addPrograms", methods=["POST"])
def addPrograms():
    _json = request.json
    name = _json["name"]    
    programType = _json["programType"]
    programId = _json(programId)
    ImageSrc = _json("imageSrc")
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

if __name__ == "__main__":
        app.run(port = 3000)