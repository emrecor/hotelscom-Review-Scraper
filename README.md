<div align="center">
  <a href="#-hotelscom-yorum-kazıyıcı-scraper">Türkçe</a> • <a href="#-hotelscom-review-scraper">English</a>
</div>

---

# 🏨 Hotels.com Yorum Kazıyıcı (Scraper)

Bu Python betiği, [Hotels.com](https://tr.hotels.com/) üzerindeki belirli bir otel sayfasından müşteri yorumlarını, puanlarını ve tarihlerini çekmek için Selenium kütüphanesini kullanır. Çekilen verileri yapılandırılmış bir CSV dosyasına kaydeder.

## 🚀 Özellikler

-   Belirtilen otel URL'sindeki tüm yorumları çeker.
-   "Diğer yorumlar" düğmesine basarak dinamik olarak yüklenen içerikleri alır.
-   Güvenilirlik için Selenium'un `WebDriverWait` özelliğini kullanır.
-   Yorum metni, puan (10 üzerinden), yıl, ay ve gün bilgilerini ayrı sütunlarda bir CSV dosyasına kaydeder.

## 🔧 Kurulum

Bu betiği çalıştırmak için Python 3.x sürümünün kurulu olması gerekmektedir.

1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git)
    cd PROJE_ADINIZ
    ```

2.  **Sanal bir ortam oluşturup aktif edin (Önerilir):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♀️ Kullanım

1.  `scraper.py` dosyasını bir metin düzenleyici veya IDE ile açın.
2.  `main()` fonksiyonu içindeki `otel_url` değişkenini, yorumlarını çekmek istediğiniz otelin Hotels.com URL'si ile değiştirin.

    ```python
    def main():
        # Yorumlarını çekmek istediğiniz otelin URL'sini buraya yapıştırın
        otel_url = "[https://tr.hotels.com/ho690580/](https://tr.hotels.com/ho690580/)..." 
        
        # ... geri kalan kod ...
    ```

3.  Betigi terminalden çalıştırın:
    ```bash
    python scraper.py
    ```

## 📊 Çıktı

Betik çalışmasını tamamladığında, proje klasörünüzde `Otel_Adi(hotels).csv` adında bir dosya oluşturulacaktır.

**Örnek CSV Çıktısı:**

| Yorum                                 | Puan | Yil  | Ay | Gun |
| ------------------------------------- | ---- | ---- | -- | --- |
| "Oda temiz ve konforluydu."           | 9    | 2025 | 10 | 25  |
| "Kahvaltı daha çeşitli olabilirdi..." | 7    | 2025 | 10 | 22  |


## ⚠️ Sorumluluk Reddi

Bu araç, eğitim ve kişisel kullanım amaçlıdır. Web sitelerinden veri çekerken ilgili sitenin kullanım koşullarına uymak kullanıcının sorumluluğundadır. Lütfen sorumlu bir şekilde kullanın.

---
---

<div align="center">
  <a href="#-hotelscom-yorum-kazıyıcı-scraper">Türkçe</a> • <a href="#-hotelscom-review-scraper">English</a>
</div>

# 🏨 Hotels.com Review Scraper

This Python script uses the Selenium library to scrape customer reviews, ratings, and dates from a specific hotel page on [Hotels.com](https://www.hotels.com/). It saves the extracted data into a structured CSV file.

## 🚀 Features

-   Scrapes all reviews from a given hotel URL.
-   Handles dynamically loaded content by clicking the "Load more reviews" button.
-   Uses Selenium's `WebDriverWait` for improved reliability.
-   Saves review text, rating (out of 10), year, month, and day into separate columns in a CSV file.

## 🔧 Installation

Python 3.x must be installed to run this script.

1.  **Clone the project:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git](https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git)
    cd YOUR_PROJECT_NAME
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♀️ Usage

1.  Open the `scraper.py` file in a text editor or IDE.
2.  In the `main()` function, replace the `otel_url` variable with the Hotels.com URL of the hotel you want to scrape.

    ```python
    def main():
        # Paste the URL of the hotel you want to scrape here
        otel_url = "[https://www.hotels.com/ho690580/](https://www.hotels.com/ho690580/)..." 
        
        # ... rest of the code ...
    ```

3.  Run the script from your terminal:
    ```bash
    python scraper.py
    ```

## 📊 Output

When the script finishes, it will create a file named `Hotel_Name(hotels).csv` in your project folder.

**Sample CSV Output:**

| Review                                  | Rating | Year | Month | Day |
| --------------------------------------- | ------ | ---- | ----- | --- |
| "The room was clean and comfortable."   | 9      | 2025 | 10    | 25  |
| "The breakfast could be more diverse..."| 7      | 2025 | 10    | 22  |


## ⚠️ Disclaimer

This tool is for educational and personal use only. It is the user's responsibility to comply with the terms of service of the website being scraped. Please use it responsibly.