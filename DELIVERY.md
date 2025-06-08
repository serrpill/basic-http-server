# HTTP Web Sunucusu Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri
- **Ad Soyad**: Serpil [Soyadınızı Yazınız]
- **Öğrenci Numarası**: [Numaranızı Yazınız]

---

## 🔗 GitHub Repo Linki
(GitHub üzerinden paylaşmadıysanız burayı boş bırakabilirsiniz.)  
https://github.com/kullaniciadi/basic-http-server

---

## 📝 Proje Açıklaması

Bu projede Python dili kullanılarak sıfırdan, herhangi bir framework kullanılmadan temel bir HTTP sunucusu geliştirilmiştir.  
Uygulama aşağıdaki temel özellikleri desteklemektedir:

- TCP socket üzerinden `GET` isteklerini işleyebilme  
- `/static` dizininden `.html`, `.css`, `.js` dosyalarını sunma  
- `/api/hello` endpoint'inden JSON yanıt döndürme  
- Doğru `Content-Type` (MIME type) header’ları gönderme  

### 🎯 Ekstra (Bonus) Özellikler
- `POST` isteklerini `/api/echo` endpoint’i ile işleyebilme  
- Basit loglama (her istek terminale yazılıyor)  
- 404 hata sayfası (HTML içerikli özel mesaj)  
- Çoklu bağlantı desteği (`threading` modülü kullanılarak)

---

## 🐳 Docker Container Bilgileri

### 🔗 Docker Hub Image Linki
Docker Hub üzerinde paylaşılmadı. Proje yerel olarak çalıştırılmıştır.

### 🐋 Container Açıklaması
Sunucu uygulaması Dockerfile ile containerize edilmiştir.  
Container, 8080 portu üzerinden dış dünyaya servis sağlamaktadır.

#### Komutlar:

docker build -t my-http-server .  
docker run -d -p 8080:8080 my-http-server

---

## 📂 Açık Kaynak Yapı Dosyaları

| Dosya Adı            | Açıklama                                        |
|----------------------|-------------------------------------------------|
| README.md            | Proje tanıtımı, kurulum yönergeleri             |
| LICENSE              | Lisans metni (varsa)                            |
| CONTRIBUTING.md      | Katkı kuralları (varsa)                         |
| NOTICE.md            | Üçüncü parti lisanslar (varsa)                  |
| CODE_OF_CONDUCT.md   | Topluluk davranış kuralları (varsa)            |
| server.py            | HTTP sunucusu Python kodu                       |
| Dockerfile           | Docker yapılandırma dosyası                     |
| .dockerignore        | Docker build sırasında hariç tutulan dosyalar  |
| static/              | Statik içerik klasörü (index.html vs.)         |
| compose.yaml         | (Kullanılmadı)                                  |

---

## 📝 Ek Notlar

- Python'daki Türkçe karakter hataları `.encode('utf-8')` kullanılarak çözülmüştür.  
- Kodlar test edilmiş ve `curl` ile `POST` istekleri başarıyla yanıtlanmıştır.  
- Framework kullanılmadan tamamen temel `socket` programlama ile gerçekleştirilmiştir.

---

📌 Teslimat, Google Classroom üzerinden `DELIVERY.md` dosyası olarak yapılmıştır.
