from flask import Flask, request, jsonify
app = Flask(__name__)
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

    print(name, programType, imageSrc,castInfo)
    return jsonify("added succesfully")

if __name__ == "__main__":
    app.run(port = 3000)
