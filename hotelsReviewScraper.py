# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:45:58 2025

@author: emrec
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # ← BU SATIR ÇOK ÖNEMLİ
import time
import pandas as pd
from datetime import datetime
import locale
import dateparser
# Örnek otel URL'si
otel_url = "https://tr.hotels.com/ho2507601408/panagia-premier-trabzon-trabzon-turkiye/?chkin=2025-05-23&chkout=2025-05-24&x_pwa=1&rfrr=HSR&pwa_ts=1747579670469&referrerUrl=aHR0cHM6Ly90ci5ob3RlbHMuY29tL0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&rm1=a2&regionId=3597&destination=Trabzon%2C+Trabzon%2C+T%C3%BCrkiye&destType=MARKET&neighborhoodId=553248635975851811&selected=78331294&latLong=41.002688%2C39.716754&sort=RECOMMENDED&top_dp=2819&top_cur=TRY&userIntent=&selectedRoomType=322833529&selectedRatePlan=399962721&expediaPropertyId=78331294&searchId=5b0d78b1-a151-4cb8-badc-dd42fe153429"

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get(otel_url)

# Sayfa yüklenmesini bekle
time.sleep(5)


element = driver.find_element(By.CSS_SELECTOR, "button[data-stid='reviews-link']")
ActionChains(driver).move_to_element(element).perform()
time.sleep(1)
element.click()
time.sleep(3)
while True:
    try:
        element1 = driver.find_element(By.XPATH, "//button[normalize-space()='Diğer yorumlar']")
        ActionChains(driver).move_to_element(element1).perform()
        time.sleep(1)
        element1.click()
        time.sleep(5)  # Yeni yorumların yüklenmesi için bekle
    except Exception as e:
        break

try:
    comment_elements = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='description']")
    comments = [c.text.strip() for c in comment_elements if c.text.strip()]
    rating_elements = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='ratingValue']")
    ratings = [r.text.strip().split('/')[0] for r in rating_elements if r.text.strip()]
    date_elements = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='datePublished']")
    dates = [d.text.strip() for d in date_elements if d.text.strip()]
    
except:
    comments = []
    rating = []
    dates = []

for i, comment in enumerate(comments, 1):
    print(f" {i}. {comment}")

# Tarayıcıyı kapat
driver.quit()
min_len = min(len(comments), len(ratings), len(dates))
data = []

for i in range(min_len):
    try:
        date_obj = dateparser.parse(dates[i], languages=['tr'])
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        data.append({
            "Text": comments[i],
            "Rating": ratings[i],
            "Year": year,
            "Month": month,
            "Day": day
        })
    except Exception as e:
        print(f"❌ Tarih ayrıştırma hatası: {dates[i]} → {e}")

# DataFrame'e çevir ve CSV olarak kaydet
df = pd.DataFrame(data)
df.to_csv("otel_yorumlari.csv", index=False, encoding="utf-8-sig")
print("📁 Veriler 'otel_yorumlari.csv' dosyasına kaydedildi.")