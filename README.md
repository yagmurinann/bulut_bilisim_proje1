# Bulut Bilişim Projesi 1: Bulut Hava Danışmanı 🌤️

## Proje Hakkında
Bulut Hava Danışmanı, kullanıcıların istedikleri şehrin güncel hava durumunu görebildikleri ve havanın durumuna göre akıllı giyim veya hazırlık tavsiyeleri alabildikleri modern bir web uygulamasıdır. Proje, Bulut Bilişim dersi kapsamında geliştirilmiştir ve AWS EC2 sunucusu üzerinde çalışan bir Flask backend'i ile estetik, modern bir frontend arayüzünden oluşmaktadır.

## Gelişmiş Özellikler
- 🏙️ **Anlık Hava Durumu:** Şehir ismine göre OpenWeatherMap API kullanılarak gerçek zamanlı hava durumu verisi çekilir.
- 💡 **Akıllı Tavsiye Sistemi:** Hava sıcaklığına ve yağış durumuna göre anlık giyim (örn. "Hava soğuk, kalın giyinmelisin! 🧥" veya "Şemsiyeni unutma! ☂️") tavsiyeleri sunar.
- 🎨 **Modern ve Premium Arayüz:** 
  - Göz yormayan, dinamik ve akıcı **Mesh Gradient** (hareketli renkli arka plan) tasarımı.
  - Derinlik hissi veren kaliteli **Glassmorphism** (Buzlu cam) kart yapısı.
  - Yumuşak animasyon geçişleri ve **Phosphor Icons** ile profesyonel/minimalist görünüm.
  - "Enter" tuşu ile hızlı arama desteği (Kullanıcı Dostu UX).
  - Sıcaklığa göre rengi değişen (soğukta mavi, sıcakta kırmızımtırak) dinamik derece göstergesi.

## Teknolojiler
### Frontend
- HTML5, CSS3, Vanilla JavaScript
- **Fontlar:** Google Fonts (Outfit)
- **İkonlar:** Phosphor Icons
- **Tasarım Dili:** Modern Dark Mode, Glassmorphism, CSS Animations

### Backend
- Python 3
- **Flask** (Web Framework)
- **Flask-CORS** (Cross-Origin Resource Sharing hatalarını önlemek için)
- **Requests** (Dış API çağrıları için)

### API ve Bulut Altyapısı
- **Hava Durumu API'si:** OpenWeatherMap API
- **Sunucu Altyapısı (Cloud):** AWS EC2 Instance (Uygulama arka ucu bu sunucuda `5000` portundan hizmet vermektedir).

---

## Kurulum ve Çalıştırma

### 1. Gereksinimler
Sistemin lokalde (veya kendi sunucunuzda) çalışması için Python 3'ün yüklü olması gerekir. Ardından gerekli kütüphaneleri kurun:
```bash
pip install flask flask-cors requests
```

### 2. Backend'i Çalıştırma (`app.py`)
Proje kök dizininde bir terminal açıp aşağıdaki komutu çalıştırarak Flask sunucusunu başlatın:
```bash
python app.py
```
Sunucu, varsayılan olarak `http://0.0.0.0:5000` adresinde çalışmaya başlayacaktır. 
*(Not: AWS EC2 gibi uzak bir sunucu kullanıyorsanız, Security Groups (Güvenlik Grupları) içerisinden `5000` portuna dışarıdan erişim izni vermeyi unutmayın.)*

### 3. Frontend'i Çalıştırma (`index.html`)
- `frontend` klasörü içindeki `index.html` dosyasını herhangi bir web tarayıcısıyla açarak (çift tıklayarak) kullanabilirsiniz. 
- Arayüz, arka planda API isteklerini `app.py` üzerinde çalışan bulut sunucuya (örneğin EC2 Public IP'nize) gönderir. 
  - **Önemli Not:** Eğer EC2 sunucunuzu yeniden başlatırsanız (ve IP adresi değişirse), `index.html` içerisindeki `fetch` fonksiyonunda bulunan IP adresini yeni IP ile güncellemeniz gerekir.

---
**Geliştirici:** Yağmur İNAN
# Bulut Bilişim Projesi 1

Bu repo, çift katmanlı (Backend + Frontend) web uygulaması projesini içermektedir.

## Geliştirme Günlüğü
* **Adım 1:** GitHub reposu oluşturuldu, lokal bilgisayara çekildi (clone) ve README dosyası eklendi.