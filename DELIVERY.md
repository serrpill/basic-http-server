# 🧾 HTTP Web Sunucusu Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri
- **Ad Soyad**: Serpil Çobanlar  
- **Öğrenci Numarası**: 170422055

---

## 🔗 GitHub Repository Bağlantısı
🔗 https://github.com/serrpill/basic-http-server

---

## 📝 Proje Açıklaması

Bu proje kapsamında Python dili ile sıfırdan, hiçbir framework (Flask, Django, Express, Spring vb.) kullanılmadan temel bir HTTP sunucusu geliştirildi. Uygulama, TCP tabanlı socket programlama ile çalışmakta olup, HTTP protokolü üzerinden gelen temel `GET` ve `POST` isteklerini işleyebilmektedir.

### 🔧 Uygulamanın Temel Özellikleri

- `GET` isteklerini TCP socket üzerinden işleyebilme
- `/static` dizininden `.html`, `.css`, `.js` gibi dosyaların sunumu
- `/api/hello` endpoint’inden JSON veri döndürebilme
- MIME türüne göre doğru `Content-Type` header'ı ayarlayabilme

### 💡 Ekstra (Bonus) Özellikler

- `POST` isteklerini `/api/echo` endpoint’i üzerinden işleyebilme  
- Çoklu istemci desteği için `threading` modülü kullanılarak paralel bağlantı kabulü  
- Her gelen isteğin terminale loglanması  
- 404 Not Found gibi durumlar için özel HTML hata sayfası döndürülmesi  
- Karakter kodlama sorunlarının `utf-8` ile çözülmesi

---

## 🐳 Docker Container Bilgileri

### 🔗 Docker Hub Image Linki

Proje yalnızca yerel geliştirme ortamında test edilmiştir. Docker Hub üzerinde paylaşım yapılmamıştır.

### 🐋 Docker Container Açıklaması

Uygulama, `Dockerfile` kullanılarak container ortamına taşınmıştır.  
Sunucu uygulaması container içinde `/app` klasöründe çalışmaktadır ve 8080 portu üzerinden hizmet vermektedir.

#### Kullanılan Dockerfile Yapılandırması:

- `FROM python:3.10-slim` ile hafif Python ortamı kurulumu  
- `WORKDIR /app` ile çalışma dizini tanımı  
- `COPY` komutlarıyla `server.py` ve `static/` klasörünün container’a dahil edilmesi  
- `EXPOSE 8080` ile dış bağlantıların açılması  
- `CMD ["python", "server.py"]` ile sunucu başlatma komutu

#### Kullanılan Komutlar:

docker build -t my-http-server .,

docker run -d -p 8080:8080 my-http-server

#### Test:
Container çalıştırıldıktan sonra http://localhost:8080 adresi üzerinden erişim sağlanmış, hem GET hem de POST istekleri başarıyla cevaplanmıştır. curl komutu kullanılarak testler gerçekleştirilmiştir.

##### 📁 Proje Dosya Yapısı
Dosya/Klasör	Açıklama
README.md	    Projenin genel tanımı, çalıştırma ve kurulum yönergeleri
LICENSE	MIT     Lisans bildirimi
server.py	    Sunucunun tüm Python kodları
Dockerfile	    Docker container yapılandırma dosyası
.dockerignore	Docker imajına dahil edilmemesi gereken dosyaların listesi
static/	        Statik içerikler (HTML/CSS/JS) klasörü

#### 📝 Ek Açıklamalar
Projede socket programlama temel alınmış, http.server gibi hazır Python modülleri dahi kullanılmamıştır.

Kodlar manuel olarak HTTP mesajları ayrıştıracak şekilde yazılmıştır.

Karakter kodlaması utf-8 olarak sabitlenmiştir.

Proje, Linux tabanlı Docker container içerisinde 8080 portu üzerinden başarıyla servis vermektedir.

Framework kullanımına dair yasaklara tamamen uyulmuştur.

Proje VSCode ve PowerShell ortamlarında geliştirilmiş, test edilmiştir.

#### 📌 Bu dosya, ödev yönergesine uygun olarak DELIVERY.md adıyla Google Classroom üzerinden teslim edilmiştir.
