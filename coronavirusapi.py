from flask import Flask

import json

app = Flask(__name__)
data = json.load(open('worldwide.json'))


@app.route('/')
def all():
    return data, 200


@app.route('/<country>')
def country(country):
    value = data.get(country)
    if value is None:
        return {"Error": "There is no such country.", "Value": country}, 404
    else:
        return value, 200


if __name__ == "__main__":
    app.run(debug=True)
