from flask import Flask, jsonify
from flask_cors import CORS # YENİ EKLENDİ

app = Flask(__name__)
CORS(app)

# Örnek bir veri tablosu (Şimdilik hafızada tutuyoruz, sonra RDS'ye bağlayacağız)
ogrenciler = [
    {"id": 1, "ad": "Ahmet", "bolum": "Bilgisayar Mühendisliği"},
    {"id": 2, "ad": "Ayşe", "bolum": "Yazılım Mühendisliği"}
]

# RESTful API Endpoint (Uç noktası)
@app.route('/api/ogrenciler', methods=['GET'])
def get_ogrenciler():
    return jsonify(ogrenciler)

@app.route('/', methods=['GET'])
def home():
    return "Bulut Bilişim Backend API'si Çalışıyor! Antigravity devrede 🚀"

if __name__ == '__main__':
    app.run(debug=True, port=5000)