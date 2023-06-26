from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, random, pickle

fullwindow = Options()
fullwindow.add_argument("--start-maximized")
driver = webdriver.Chrome(options=fullwindow)
driver.get("https://tiktok.com")
# with open("mycookie.pkl", "rb") as file:
#     cookie = pickle.load(file)
# print(cookie)
cookie = pickle.load(open("cookieTikTok.pkl", "rb"))
# for i in cookie:
#     print(i)
#     print("\n")
time.sleep(5)
for i in cookie:
    driver.add_cookie(i)
driver.get("https://tiktok.com")
time.sleep(5)
# driver.get("https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=vi")
# # driver.implicitly_wait(20)
# time.sleep(5)
# element = driver.find_element(By.CLASS_NAME, "g-c-Hf")
# element.click()
# time.sleep(10)
# driver.get("https://tiktok.com/")

# element = driver.find_element(By.ID, "header-login-button")
# time.sleep(3)
# element.click()
# time.sleep(5)
# element = driver.find_element(By.CLASS_NAME, "tiktok-t5chka-ALink epl6mg0").get_attribute("href")
# driver.get(element)
# time.sleep(3)
# element = driver.find_element(By.CLASS_NAME, "ep888o80 tiktok-1mgli76-ALink-StyledLink epl6mg0")
# element.click()
# time.sleep(3)
# element = driver.find_element(By.NAME, "username")
# element.click()
# element.send_keys("datt97792@gmail.com")
# time.sleep(3)
# element = driver.find_element(By.CSS_SELECTOR, ".tiktok-wv3bkt-InputContainer.etcs7ny1")
# element.click()
# element.send_keys("Az0777541112@")
# element = driver.find_element(By.CSS_SELECTOR, ".e1w6iovg0.tiktok-9c63gx-Button-StyledButton.ehk74z00")
# element.click()
driver.get("https://traodoisub.com/")
time.sleep(5)
element = driver.find_element(By.ID, "username")
element.click()
element.send_keys("tranducdat24")
time.sleep(3)
element = driver.find_element("id", "password")
element.click()
element.send_keys("az0777541112")
time.sleep(5)
element = driver.find_element("id", "loginclick")
element.click()
time.sleep(8)
driver.get("https://traodoisub.com/ex/tiktok_like/")
# time.sleep(3)


demJob = 0
while True:
    
    time.sleep(5)
    # lưu tab hiện tại
    cuaSoHienTai = driver.current_window_handle
    try:
        element = driver.find_element(By.CLASS_NAME, "col-2")
        time.sleep(3)
        element.click()
    except NoSuchElementException:
        time.sleep(15)
        element = driver.find_element(By.ID, "reload")
        element.click()
        time.sleep(3)
        element = driver.find_element(By.CLASS_NAME, "col-2")
        element.click()
    time.sleep(random.randint(8, 13))
    # Lấy tất cả các tab
    tatCaCuaSo = driver.window_handles
    # Chuyen drivet đến tab cuối cùng
    driver.switch_to.window(driver.window_handles[-1])
    try:
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tiktok-1npmxy5-DivActionItemContainer.er2ywmz0"))) #driver.find_element(By.CSS_SELECTOR, )
        soTym = driver.find_element(By.CSS_SELECTOR, ".tiktok-cpjh4r-StrongText.edu4zum2")
        TymBanDau = soTym.get_attribute("textContent")
        like = TymBanDau
        element = driver.find_element(By.CSS_SELECTOR, ".tiktok-1eor4vt-SpanIconWrapper.edu4zum1")
        element.click()
        element = driver.find_element(By.CSS_SELECTOR, ".tiktok-q1bwae-DivPlayIconContainer.e1ya9dnw8")
        element.click()
        time.sleep(5)
        while like == TymBanDau:
            soTym = driver.find_element(By.CSS_SELECTOR, ".tiktok-cpjh4r-StrongText.edu4zum2")
            TymHienTai = soTym.get_attribute("textContent")
            if TymHienTai == TymBanDau:
                element = driver.find_element(By.CSS_SELECTOR, ".tiktok-1eor4vt-SpanIconWrapper.edu4zum1")
                element.click()
            # element.click()
            time.sleep(5)
            soTym = driver.find_element(By.CSS_SELECTOR, ".tiktok-cpjh4r-StrongText.edu4zum2")
            like2 = soTym.get_attribute("textContent")
            like = like2
    except NoSuchElementException:
        print("Khong")
        driver.close()
        continue
    time.sleep(3)
    # time.sleep(5)
    # # element = driver.find_element(By.ID, "xgwrapper-4-7241551947981966597")
    # # element.click()
    # # element.click()
    time.sleep(3)
    # linkWebHienTai = driver.current_url
    # driver.get(linkWebHienTai)
    driver.close()
    driver.switch_to.window(cuaSoHienTai)
    time.sleep(10)
    driver.refresh()
    if demJob == 20:
        element = driver.find_element(By.ID, "nhanall")
        time.sleep(3)
        driver.quit()