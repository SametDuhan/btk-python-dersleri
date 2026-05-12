import time
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://github.com"

# siteye giriş
driver.get(url)
driver.maximize_window()
# driver.set_window_size(800, 600)
# driver.minimize_window()

time.sleep(2)

#sayfa bilgilerini alma
print(f"Title: {driver.title}")
print(f"Current URL: {driver.current_url}")
print(f"Page Source Length: {len(driver.page_source)}")

# sayfa yönlendirme
target_user = "sadikturan____"
driver.get(f"{url}/{target_user}")

# doğrulama
if target_user in driver.title.lower():
    print(f"{target_user} profili başarıyla açıldı.")
    driver.save_screenshot(f"github_screenshot_{target_user}.png")
else:
    print(f"{target_user} profili açılamadı.")

driver.back()  # geri git
print("Geri gidildi.", driver.current_url)
time.sleep(2)

target_user = "sadikturan"
driver.get(f"{url}/{target_user}")

time.sleep(2)
driver.refresh()  # sayfayı yenile
print("Sayfa yenilendi.", driver.current_url)


time.sleep(2)


driver.quit()