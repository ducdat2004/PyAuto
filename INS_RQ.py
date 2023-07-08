import requests, time, pickle, random
from selenium import webdriver
from selenium.webdriver.common.by import By
tokenTDS = "TDS0nIwEjclZXZzJiOiIXZ2V2ciwiI0IDdhR2Y1RmbhJHdiojIyV2c1Jye"
cauHinh = requests.get("https://traodoisub.com/api/?fields=instagram_run&id=ducdat05112004&access_token="+tokenTDS)
time.sleep(5)
driver = webdriver.Chrome()
driver.get("https://instagram.com")
cookies = pickle.load(open("CookieIns_ducdat05112004.pkl", "rb"))
time.sleep(5)
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
while True:
    thoi_gian_hien_tai = time.localtime()  # Lấy thông tin về thời gian hiện tại
    thoi_gian_format = time.strftime("%H:%M:%S", thoi_gian_hien_tai)  # Định dạng lại thời gian
    layNhiemVu = requests.get("https://traodoisub.com/api/?fields=instagram_like&access_token="+tokenTDS).json()
    if 'data' in layNhiemVu:
        listData = layNhiemVu['data']
        if len(list(listData)) == 0:
            print("Không có Job")
            time.sleep(8)
            continue
    else:
        time.sleep(7)
        continue  
    time.sleep(2)
    print(listData)
    for i in listData:
        idJob = i["id"]
        linkJob = i["link"]
        print("\033[95m", linkJob)
        print("\033[95m", idJob)
        driver.get(linkJob)
        time.sleep(5)
        driver.implicitly_wait(10)
        time.sleep(random.randint(10, 25))
        clickTim = driver.find_element(By.CLASS_NAME, "xp7jhwk")
        clickTim.click()    
        time.sleep(3)
        guiNV = requests.get("https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id="+str(idJob)+"&access_token="+tokenTDS)
        print("\033[92m", guiNV.json())
        time.sleep(5)
