# 📚 Library Management System

Bu proje, kitap ekleme, listeleme ve yönetim işlemlerini terminal ve API tabanlı bir yapı üzerinden gerçekleştiren bir **Library Management System** uygulamasıdır.  

## 🚀 Kurulum

## 1. Reponun klonlanması:

- ``git clone https://github.com/busraatasoy/library-management_project.git``
- ``cd library-management``


## 2. Sanal ortam oluşturun ve gerekli paketleri yükleyin:

- ``python -m venv .venv``

- ``.venv\Scripts\activate   # Windows``

- ``source .venv/bin/activate   # Mac/Linux için``

## 3. Gereksinimleri yükleyin:

- ``pip install -r requirements.txt``

**▶️ Kullanım**
**Aşama 1 ve 2 - Terminal Uygulaması**

`python main.py`

- Menü üzerinden kitap ekleyebilir, silebilir, listeleyebilirsiniz.
- ISBN girildiğinde Open Library API’den bilgiler çekilecektir.

**Aşama 3 - API Sunucusu**
`uvicorn api:app --reload`

- Tarayıcıda http://127.0.0.1:8000/docs adresine giderek interaktif API dokümantasyonunu kullanabilirsiniz.


**🌐 API Dokümantasyonu (Aşama 3)**
| Yöntem | Endpoint      | Açıklama              | Örnek Body                                                               |
| ------ | ------------- | --------------------- | ------------------------------------------------------------------------ |
| GET    | /books        | Tüm kitapları listele | -                                                                        |
| POST   | /books        | Yeni kitap ekle       | `{"isbn": "1234567890", "title": "Book Title", "author": "Author Name"}` |
| DELETE | /books/{isbn} | ISBN ile kitabı sil   | -                                                                        |

**Testler**

**Tüm Testleri Çalıştırma**

`pytest tests/`

- Tüm metod ve API testleri burada çalıştırılabilir.
