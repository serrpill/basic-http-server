# Basic HTTP Server (Python + Docker)

Bu proje, Python dili kullanılarak sıfırdan geliştirilen basit bir HTTP web sunucusudur.  
Framework kullanılmadan, sadece temel `socket` programlama tekniği ile gerçekleştirilmiştir.  
Sunucu, statik dosyaları sunabilmekte ve basit JSON API endpoint'leri ile iletişim kurabilmektedir.  
Uygulama Docker ile containerize edilmiştir.

---

## 🚀 Özellikler

- 📡 TCP socket üzerinden `GET` isteklerini işleme
- 📁 `/static` dizininden `.html`, `.css`, `.js` dosyaları sunma
- 🧾 `/api/hello` endpoint’inden JSON veri döndürme
- 🔤 MIME type (Content-Type) desteği
- 🔁 Çoklu bağlantı desteği (`threading`)
- 📨 `POST` isteğini `/api/echo` üzerinden karşılama
- ⚠️ 404 hata sayfası
- 📋 Konsol loglama

---

## 📦 Kurulum ve Kullanım

### 🔧 Gereksinimler

- Python 3.x
- Docker

### 🐍 Python ile Manuel Çalıştırma

```bash
python server.py
```

Tarayıcıda test:
- [http://localhost:8080](http://localhost:8080)
- [http://localhost:8080/static/index.html](http://localhost:8080/static/index.html)
- [http://localhost:8080/api/hello](http://localhost:8080/api/hello)

### 🐳 Docker ile Çalıştırma

```bash
docker build -t my-http-server .
docker run -d -p 8080:8080 my-http-server
```

### `POST` Testi (curl)

```bash
curl -X POST -d "Merhaba, ben Serpil!" http://localhost:8080/api/echo
```

---

## 🗂️ Proje Yapısı

```
basic-http-server/
├── server.py
├── Dockerfile
├── .dockerignore
├── static/
│   └── index.html
├── README.md
├── LICENSE (opsiyonel)
├── CONTRIBUTING.md (opsiyonel)
├── CODE_OF_CONDUCT.md (opsiyonel)
└── NOTICE.md (opsiyonel)
```

---

## 👩‍💻 Geliştirici

**Serpil Çobanlar**  
2024-2025 Bahar Dönemi  
Açık Kaynak Kodlu Yazılımlar

---

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakınız.
