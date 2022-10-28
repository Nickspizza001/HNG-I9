from flask import Flask


app = Flask(__name__)

stringUsername = "Damibod"
Boolean = True
Integer = 21
stringBio = "Ready to learn"

json_response ={
    "slackUsername": stringUsername,
    "backend": Boolean,
    "age": Integer,
    "bio": stringBio
}

@app.route("/hng", methods=['GET'])
def hng():
    return json_response



if __name__ == "__main__":
    app.run(debug=True)