import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pickle, time, random
tokenTraoDoiSub = "TDS0nIwEjclZXZzJiOiIXZ2V2ciwiI0IDdhR2Y1RmbhJHdiojIyV2c1Jye"
idFB = "100085319979852"
a, b = map(int, input("Thời gian random khi thực hiện like: ").split())
typee = str(input("like, follow: "))
cauHinh = requests.get("https://traodoisub.com/api/?fields=run&id="+idFB+"&access_token="+tokenTraoDoiSub)
if cauHinh.status_code == 200:
    print("\033[92mCấu hình thành công")
    data = cauHinh.json()['data']
    idFBCauHinh = data['id']
    print("\033[92m", idFBCauHinh)
driver = webdriver.Chrome()
driver.get("https://facebook.com")
# Login Facebook bằng cookies
cookies = pickle.load(open("CookieFB_MyAnh.pkl", "rb")) # Đọc files cookies
for cookie in cookies:
    driver.add_cookie(cookie) # add cookie vào driver

driver.refresh() 
time.sleep(5)


while True:
    layNhiemVu = requests.get("https://traodoisub.com/api/?fields="+typee+"&access_token="+tokenTraoDoiSub).json()
    
    print(layNhiemVu)
    if len(layNhiemVu) == 0:
        time.sleep(5)
        continue
    else:
        for i in list(layNhiemVu):
            idJob = i['id']
            linkJob = 'https://facebook.com/'+str(idJob)
            driver.get(linkJob)

            time.sleep(random.randint(a, b))
            
        
            # Tìm nút like
            nutLike = driver.find_element(By.CSS_SELECTOR, ".x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x193iq5w.xeuugli.x1r8uery.x1iyjqo2.xs83m0k.xg83lxy.x1h0ha7o.x10b6aqq.x1yrsyyn")
            # Click vào nút like x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xg83lxy x1h0ha7o x10b6aqq x1yrsyyn
            nutLike.click()
            
            time.sleep(5)
            nhanXu = requests.get("https://traodoisub.com/api/coin/?type=LIKE&id="+str(idJob)+"&access_token="+tokenTraoDoiSub)
            print("\033[92m", nhanXu.json())
            time.sleep(5)