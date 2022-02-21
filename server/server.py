from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_house_price", methods = ['POST'])
def predict_house_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'price': utils.predict_price(location, sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    utils.load_saved_assets()
    app.run()