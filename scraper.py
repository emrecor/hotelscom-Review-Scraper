# -*- coding: utf-8 -*-

import pandas as pd
import dateparser
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# --- Sabitler (Değişirse buradan güncelleyin) ---
# Web sitesi yapısı değişirse, bu seçicilerin güncellenmesi gerekebilir.
SELECTORS = {
    "reviews_link": "button[data-stid='reviews-link']",
    "load_more_button": "//button[normalize-space()='Diğer yorumlar']",
    "comment_description": "span[itemprop='description']",
    "rating_value": "span[itemprop='ratingValue']",
    "date_published": "span[itemprop='datePublished']",
    "hotel_name": "h1.uitk-heading-3",
}


# --- Fonksiyonlar ---

def setup_driver():
    """
    Selenium WebDriver'ı kurar ve döndürür.
    ChromeDriverManager kullanarak uyumlu sürücüyü otomatik olarak indirir.
    """
    print("WebDriver hazırlanıyor...")
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Tarayıcıyı göstermeden çalıştırmak için
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Elementlerin yüklenmesi için genel bir bekleme süresi
    return driver


def click_reviews_section(driver):
    """
    Yorumlar bölümüne gider ve tıklar.
    """
    try:
        print("Yorumlar bölümü butonu aranıyor...")
        reviews_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["reviews_link"]))
        )
        # Bazen buton başka bir elementin altında kalabilir, bu yüzden JS ile tıklamak daha garantidir.
        driver.execute_script("arguments[0].scrollIntoView(true);", reviews_button)
        time.sleep(1)  # Scroll sonrası sayfanın oturmasını bekle
        driver.execute_script("arguments[0].click();", reviews_button)
        print("Yorumlar bölümüne tıklandı.")
        # Yorumların yüklenmesi için kısa bir bekleme
        time.sleep(5)
    except TimeoutException:
        print("Hata: Yorumlar linki bulunamadı veya tıklanamadı.")
        raise


def load_all_reviews(driver):
    """
    'Diğer yorumlar' butonuna, buton artık görünmeyene kadar tıklar.
    """
    print("Tüm yorumlar yükleniyor...")
    while True:
        try:
            # Butonun tıklanabilir olmasını bekle
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, SELECTORS["load_more_button"]))
            )
            # Butona scroll yap ve tıkla
            driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
            time.sleep(1)  # Scroll sonrası bekleme
            load_more_button.click()
            print("'Diğer yorumlar' butonuna tıklandı.")
            time.sleep(2)  # Yeni yorumların yüklenmesi için bekle
        except TimeoutException:
            print("Tüm yorumlar yüklendi ('Diğer yorumlar' butonu bulunamadı).")
            break  # Döngüden çık
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")
            break


def scrape_review_data(driver):
    """
    Yüklü tüm yorumları, puanları ve tarihleri sayfadan kazır.
    """
    print("Yorum verileri çekiliyor...")
    try:
        comments = [c.text.strip() for c in driver.find_elements(By.CSS_SELECTOR, SELECTORS["comment_description"]) if
                    c.text.strip()]
        ratings = [r.text.strip().split('/')[0] for r in
                   driver.find_elements(By.CSS_SELECTOR, SELECTORS["rating_value"])]
        dates = [d.text.strip() for d in driver.find_elements(By.CSS_SELECTOR, SELECTORS["date_published"])]
        hotel_name = driver.find_element(By.CSS_SELECTOR, SELECTORS["hotel_name"]).text.strip()

        print(f"Toplam {len(comments)} yorum, {len(ratings)} puan, {len(dates)} tarih bulundu.")
        return comments, ratings, dates, hotel_name
    except NoSuchElementException as e:
        print(f"Hata: Veri çekilirken bir element bulunamadı -> {e}")
        return [], [], [], "Bilinmeyen_Otel"


def process_and_save_data(comments, ratings, dates, hotel_name):
    """
    Çekilen ham veriyi işler ve bir CSV dosyasına kaydeder.
    """
    if not all([comments, ratings, dates]):
        print("Kaydedilecek veri bulunamadı. İşlem sonlandırılıyor.")
        return

    print("Veriler işleniyor ve CSV dosyası oluşturuluyor...")
    min_len = min(len(comments), len(ratings), len(dates))
    data = []

    for i in range(min_len):
        try:
            date_obj = dateparser.parse(dates[i], languages=['tr'])
            data.append({
                "Yorum": comments[i],
                "Puan": ratings[i],
                "Yil": date_obj.year,
                "Ay": date_obj.month,
                "Gun": date_obj.day
            })
        except Exception as e:
            print(f"Tarih ayrıştırma hatası: {dates[i]} -> {e}")

    df = pd.DataFrame(data)

    # Dosya adı için otel adını temizle
    safe_filename = re.sub(r'[^\w\s-]', '', hotel_name).strip().replace(" ", "_")
    output_filename = f"{safe_filename}(hotels).csv"

    df.to_csv(output_filename, index=False, encoding="utf-8-sig")
    print(f"Başarılı! Veriler '{output_filename}' dosyasına kaydedildi.")


def main():
    """
    Ana program akışını yönetir.
    """
    otel_url = "https://tr.hotels.com/ho690580/grand-mardin-i-hotel-mersin-turkiye/?chkin=2025-06-03&chkout=2025-06-04&x_pwa=1&rfrr=HSR&pwa_ts=1747936214516&referrerUrl=aHR0cHM6Ly90ci5ob3RlbHMuY29tL0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&rm1=a2&regionId=4525&destination=Mersin%2C+Mersin+%C4%B0li%2C+T%C3%BCrkiye&destType=MARKET&neighborhoodId=553248635290262208&latLong=36.81211%2C34.641487&sort=RECOMMENDED&top_dp=1999&top_cur=TRY&userIntent=&selectedRoomType=201951803&selectedRatePlan=209931326&expediaPropertyId=18284083&searchId=aae43b41-b236-4488-9e56-a24739868128"

    driver = setup_driver()
    try:
        driver.get(otel_url)
        click_reviews_section(driver)
        load_all_reviews(driver)
        comments, ratings, dates, hotel_name = scrape_review_data(driver)
        process_and_save_data(comments, ratings, dates, hotel_name)
    except Exception as e:
        print(f"Program çalışırken ana bir hata oluştu: {e}")
    finally:
        print("WebDriver kapatılıyor.")
        driver.quit()


if __name__ == "__main__":
    main()