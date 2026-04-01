# ☁️ Bulut Hava Danışmanı (Cloud Weather Advisor)

## Proje Hakkında
Bulut Hava Danışmanı, kullanıcıların istedikleri şehrin güncel hava durumunu görebildikleri ve havanın durumuna göre akıllı giyim veya hazırlık tavsiyeleri alabildikleri modern bir web uygulamasıdır. Proje, Ankara Üniversitesi Bulut Bilişim dersi kapsamında geliştirilmiştir ve AWS EC2 sunucusu üzerinde çalışan bir Flask backend'i ile AWS S3 üzerinde barındırılan estetik, modern bir frontend arayüzünden oluşmaktadır.

## ✨ Gelişmiş Özellikler
- 🏙️ **Anlık Hava Durumu:** Şehir ismine göre OpenWeatherMap API kullanılarak gerçek zamanlı hava durumu verisi çekilir.
- 💡 **Akıllı Tavsiye Sistemi:** Hava sıcaklığına ve yağış durumuna göre anlık giyim (örn. "Hava soğuk, kalın giyinmelisin! 🧥") tavsiyeleri sunar.
- 🎨 **Modern ve Premium Arayüz:** - Gökyüzü hissiyatı veren akıcı **Gradient** arka plan tasarımı.
  - Derinlik hissi veren kaliteli **Glassmorphism** (Buzlu cam) kart yapısı.

## 🛠️ Kullanılan Teknolojiler
### Frontend (AWS S3)
- HTML5, CSS3, Vanilla JavaScript (Fetch API)
- **Tasarım Dili:** Glassmorphism, CSS Animations
- **Barındırma:** AWS S3 Bucket (Static Website Hosting)

### Backend (AWS EC2)
- Python 3 & **Flask** (Web Framework)
- **Flask-CORS** (Cross-Origin Resource Sharing yönetimi)
- **Requests** (Dış API çağrıları için)
- **Barındırma:** AWS EC2 (Ubuntu) üzerinde `nohup` ile 7/24 arkaplan servisi.

### API ve Bulut Altyapısı
- **Hava Durumu API'si:** OpenWeatherMap API
- **Güvenlik:** EC2 Security Groups üzerinden Custom TCP 5000 portu erişimi.

---

## 🚀 Proje Mimarisi ve Çalışma Mantığı

1. **Frontend Erişimi:** Kullanıcı, AWS S3 Endpoint linki üzerinden arayüze erişir.
2. **API İsteği:** Kullanıcı bir şehir arattığında, S3'teki JavaScript kodları AWS EC2 sunucusunun IP adresine (Port 5000) bir HTTP GET isteği atar.
3. **Dış Veri Çekimi:** EC2 üzerindeki Flask uygulaması bu isteği alır ve OpenWeatherMap API'sine bağlanarak canlı veriyi çeker.
4. **Veri İşleme ve Yanıt:** Flask, gelen ham veriyi işler, akıllı tavsiye algoritmasını çalıştırır ve sonucu tekrar S3'teki Frontend'e göndererek ekranda gösterilmesini sağlar.

---
**Geliştirici:** Yağmur İNAN - Ankara Üniversitesi Bilgisayar Mühendisliği