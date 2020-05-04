from flask import Flask,jsonify

import json

app=Flask(__name__)
@app.route('/')
def allpokemon():
    with open('worldwide.json') as infile:
        data=json.load(infile)
        return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)