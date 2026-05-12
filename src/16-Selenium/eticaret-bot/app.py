import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MIN_FIYAT = 100000
MAX_FIYAT = 160000
KONTROL_ARALIGI = 60 * 10  # 10 dakika

options = Options()
# options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration 
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')

def veriyi_kaydet(urun_listesi):
    dosya_adi = "fiyat_takip.csv"
    tarih_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(dosya_adi, "a", encoding="utf-8") as dosya:
        yazici = csv.writer(dosya)

        if dosya.tell() == 0:  # Dosya boşsa başlık ekle
            yazici.writerow(["Tarih/Saat", "Ürün İsmi", "Fiyat", "Link"])

        for urun in urun_listesi:
            yazici.writerow([tarih_saat, urun["isim"], urun["fiyat"], urun["link"]])


driver = webdriver.Chrome(options=options)

try:
    while True:
        try:
            driver.get("https://www.amazon.com.tr")

            arama_kutusu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
            arama_kutusu.send_keys("iphone 17 pro max" + Keys.ENTER)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']")))
            urun_kartlari = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
            print(f"Toplam ürün sayısı: {len(urun_kartlari)}")
            urunler = []

            for kart in urun_kartlari:
                try:
                    urun_ismi = kart.find_element(By.CSS_SELECTOR, "h2 span").text
                    fiyat_metin = kart.find_element(By.CLASS_NAME, "a-price-whole").text
                    sayisal_fiyat = float(fiyat_metin.replace(".", "").replace(",", "."))
                    link = kart.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

                    if "17 pro max" in urun_ismi.lower() and MIN_FIYAT <= sayisal_fiyat <= MAX_FIYAT and "kılıf" not in urun_ismi.lower():
                        urunler.append({"isim": urun_ismi, "fiyat": sayisal_fiyat , "link": link})
                        print(f"Uygun ürün bulundu: {urun_ismi[:40]}... - Fiyat: {sayisal_fiyat} TL")
                except:
                    continue

            if urunler:
                veriyi_kaydet(urunler)
                en_ucuz = min(urunler, key=lambda x: x["fiyat"])
                print(f"En ucuz ürün: {en_ucuz['isim']} - Fiyat: {en_ucuz['fiyat']} TL")
            else:
                print("Ürün bulunamadı.")
        except Exception as e:
            print(f"Hata oluştu: {e}")

        print(f"{KONTROL_ARALIGI // 60} dakika sonra tekrar kontrol edilecek...")
        time.sleep(KONTROL_ARALIGI)

except KeyboardInterrupt:
    print("Program sonlandırıldı.")

finally:
    driver.quit()