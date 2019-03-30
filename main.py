from flask import Flask, request, make_response, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

lat = 0
lon = 0


@app.route('/get', methods=['GET'])
def get():
    payload = {
        'lat': lat,
        'lon': lon
    }

    return make_response(jsonify(payload)), 200


@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    global lat
    lat = data['lat']
    global lon
    lon = data['lon']

    return make_response(jsonify({'message': 'Saved'})), 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)