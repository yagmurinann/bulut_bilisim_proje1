from flask import Flask, jsonify, request # type: ignore
from flask_cors import CORS # type: ignore
import requests # type: ignore

app = Flask(__name__)
CORS(app)

# Aldığın API Key'i buraya tırnak içine yapıştır
API_KEY = "57b8205c25f16c83e2c9c46779000790"

@app.route('/api/hava', methods=['GET'])
def get_weather():
    city = request.args.get('sehir', 'Ankara') # Varsayılan Ankara
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        
        # Akıllı Tavsiye Sistemi
        tavsiye = ""
        if temp < 10: tavsiye = "Hava soğuk, kalın giyinmelisin! 🧥"
        elif 10 <= temp <= 20: tavsiye = "Hava serin, üzerine bir hırka al. 🧥"
        else: tavsiye = "Hava harika, tişört yeterli! 👕"
        
        if "yağmur" in desc or "rain" in desc:
            tavsiye += " Ayrıca şemsiyeni unutma! ☂️"

        return jsonify({
            "sehir": data['name'],
            "derece": temp,
            "durum": desc.capitalize(),
            "tavsiye": tavsiye
        })
    else:
        return jsonify({"hata": "Şehir bulunamadı!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)