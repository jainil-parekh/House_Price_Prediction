from flask import Flask, request, jsonify
import util
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/get_location_names')   
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '+')

    return response
    

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['BHK'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    # Log the received data
    app.logger.info(f"Received data - Sqft: {total_sqft}, Location: {location}, BHK: {bhk}, Bath: {bath}")

    return response


if __name__ == '__main__':  
    print("Starting flask server for home price prediction")
    app.run()  