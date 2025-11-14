from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

api = "abc95120a700f6e5ba7f995be6120384"
url = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/api")
def name():
    city = request.args.get("city")
    
    if not city:
        return jsonify("error : city not found" )
    
    payload = {
            "q" : city,
            "appid" : api,
            "units" : "metric"
        }

    response = requests.get(url, params = payload)

    result = response.json()
    
    if result.get("cod") != 200:
        return jsonify({f"{city} is not found, recheck the city name"})
    
    temp, wind = result["main"]["temp"], result["wind"]["speed"]
    
    final = {"Weather report for the city" : result["name"], 
                                    "Temp" : temp, 
                                    "wind" : wind
    }
    return jsonify(final)
    
if __name__ == "__main__":
    app.run(debug=True)
    