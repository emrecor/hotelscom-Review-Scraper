# Hotels.com Yorum Kazıyıcı (Scraper)

Bu Python betiği, [Hotels.com](https://tr.hotels.com/) üzerindeki belirli bir otel sayfasından müşteri yorumlarını, puanlarını ve tarihlerini çekmek için Selenium kütüphanesini kullanır. Çekilen verileri yapılandırılmış bir CSV dosyasına kaydeder.

## 🚀 Özellikler

- Belirtilen otel URL'sindeki tüm yorumları çeker.
- "Diğer yorumlar" düğmesine basarak dinamik olarak yüklenen içerikleri alır.
- Güvenilirlik için Selenium'un `WebDriverWait` özelliğini kullanır.
- Yorum metni, puan (10 üzerinden), yıl, ay ve gün bilgilerini ayrı sütunlarda bir CSV dosyasına kaydeder.

## 🔧 Kurulum

Bu betiği çalıştırmak için Python 3.x sürümünün kurulu olması gerekmektedir.

1.  **Projeyi klonlayın veya indirin:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git)
    cd PROJE_ADINIZ
    ```

2.  **Sanal bir ortam (virtual environment) oluşturup aktif edin (Önerilir):**
    ```bash
    # Proje klasörünün içindeyken bu komutu çalıştırın
    python -m venv venv
    
    # Windows için:
    venv\Scripts\activate
    
    # macOS/Linux için:
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