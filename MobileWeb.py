from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, pickle, random
from colorama import Fore, Back, Style, init
mobile_emulation = {
    "deviceName" : "SamSung S23"
}
idFB = str(input(Fore.RED + "Nhập id FB: ")) #100049257640475
userGolike = str(input(Fore.RED + "Nhập user GL: "))
passGolike = str(input(Fore.RED + "Nhập Passwords: "))
# t1, t2 = int(input("Nhập thời gian delay khi thực hiện like: "))
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobile_emulation", mobile_emulation)
chrome_options.add_argument("--window-size=600,812")  # Kích thước cửa sổ tương ứng với dien thoai
chrome_options.add_argument(f"--user-agent={mobile_emulation['deviceName']}")  # Thiết lập User-Agent tương ứng

driver = webdriver.Chrome(options=chrome_options)
cookies = pickle.load(open("cookieFB_MA.txt", "rb"))
# cookies = [{'domain': '.facebook.com', 'expirationDate': 1726301213.007736, 'hostOnly': False, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': 'G-zVZKIGWUUUECx9O1Zsq9YQ'}, {'domain': '.facebook.com', 'expirationDate': 1699520690.66833, 'hostOnly': False, 'httpOnly': True, 'name': 'fr', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': '0MNbYVJzSdffCyH57.AWWzkYbdlyARfi0jY_PvGw__xZA.Bk1fj1.0D.AAA.0.0.Bk1fmy.AWW1bY1IVjY'}, {'domain': '.www.facebook.com', 'expirationDate': 1726304626, 'hostOnly': False, 'httpOnly': False, 'name': 'm_ls', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': '%7B%22c%22%3A%7B%221%22%3A%22HCwAABaevSQWyOfYEhMFForfqtK8wC0A%22%2C%222%22%3A%22GSwVQBxMAAAWABbasK_NDBYAABV-HEwAABYAFtSwr80MFgAAFigA%22%2C%2295%22%3A%22HCwAABbGCRbIr835CBMFForfqtK8wC0A%22%7D%2C%22d%22%3A%2255f56bc8-4924-42cc-94c6-6260221d8507%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22a84xtu%22%7D'}, {'domain': '.facebook.com', 'expirationDate': 1723280687.906273, 'hostOnly': False, 'httpOnly': True, 'name': 'xs', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': '29%3AyLQKSdU9bw17mQ%3A2%3A1691744688%3A-1%3A6266'}, {'domain': '.facebook.com', 'expirationDate': 1723280687.906266, 'hostOnly': False, 'httpOnly': False, 'name': 'c_user', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': '100049257640475'}, {'domain': '.facebook.com', 'hostOnly': False, 'httpOnly': False, 'name': 'presence', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': True, 'storeId': None, 'value': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1691744757945%2C%22v%22%3A1%7D'}, {'domain': '.facebook.com', 'expirationDate': 1692349493, 'hostOnly': False, 'httpOnly': False, 'name': 'dpr', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': '1.25'}, {'domain': '.facebook.com', 'expirationDate': 1726304689.906204, 'hostOnly': False, 'httpOnly': True, 'name': 'sb', 'path': '/', 'sameSite': 'None', 'secure': True, 'session': False, 'storeId': None, 'value': 'G-zVZChwo6X5chf3cNJbP-L_'}, {'domain': '.facebook.com', 'expirationDate': 1692349493, 'hostOnly': False, 'httpOnly': False, 'name': 'wd', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'session': False, 'storeId': None, 'value': '1536x707'}]

driver.get("https://facebook.com")
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(5)
driver.get("https://app.golike.net")
time.sleep(3)
element = driver.find_element(By.CLASS_NAME, "form-control")
element.click()
# user = "dat5112004"
# for i in user:
element.send_keys(userGolike)
    # time.sleep(0.5)
time.sleep(5)
try:
    element = driver.find_element(By.XPATH, "//form//div[2]")
    element.click()
    passw = element.find_element(By.TAG_NAME, "input")
    passw.click()
    passw.send_keys(passGolike)
    time.sleep(5)
except NoSuchElementException:
    print("Khong tim thay phan tu")
element = driver.find_element(By.CSS_SELECTOR, ".text-center.my-4")
element.click()
while True:
    if input("Enter 'c': ") == 'c':
        break
time.sleep(4)
driver.get("https://app.golike.net/jobs/facebook?load_job=true")
wait = WebDriverWait(driver, 40) # Chờ phần tử xuất hiện, chờ tối đa 30s
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.mt-2.select-account")))
element.click()
time.sleep(1)
listAccounts = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span//div")))
print(f"Có {len(listAccounts)} FB được thêm vào tài khoản GL")
if listAccounts:
    for i in range(len(listAccounts)): 
        time.sleep(2)
        accountFB = listAccounts[i].get_attribute('id')
        print(accountFB)
        if str(accountFB) == idFB:
            listAccounts[i].click()
            time.sleep(1)
            break
        
def linkMbasic(linkJob):
    kq = "https://mbasic"
    copyI = 0
    for i in range(len(linkJob)):
        if linkJob[i] == '.':
            copyI = i
            break
    for i in range(copyI, len(linkJob)):
        kq+=linkJob[i]
    print("mBasic link: ", kq)
    return kq
soLanChoLoad = 0
while True:
    time.sleep(2)
    
    if soLanChoLoad >= 5:
        print("refresh")
        driver.refresh()
        time.sleep(3)
        soLanChoLoad = 0
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.mb-2.hand")))
        # if element:
        element = element[0]
        element.click()
        time.sleep(2)
        tabJobdetail = driver.current_window_handle
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
        try:
            confirm_alert = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
            confirm_alert.click()
        except NoSuchElementException:
            print("ko cf")
            soLanChoLoad += 1
            time.sleep(10)
            continue    
        time.sleep(10)
        continue
    time.sleep(2)
    element = driver.find_element(By.CSS_SELECTOR, ".font-18.font-bold.b200.block-text")
    jobType = element.text
    print(jobType)
    
    def dinhDangLink(link):
        kq = 'https://www'
        R = False
        if link[8] != 'w' or link[8] != 'f':
            for i in range(8, len(link)):
                if link[i] == '.':
                    R = True
                    
                if R:
                    kq += link[i]
        print(kq)
        return kq
    def work(jobType):
        d = False
        time.sleep(7)
        tabHienTai = driver.current_window_handle
        try:
            element = driver.find_element(By.XPATH, "//div[@class='card card-job-detail']//div[@class='p-3']//div//a[1]")
            linkJob = element.get_attribute("href")
            tabHienTai = driver.current_window_handle
            element.click()
            # tabHienTai = driver.current_window_handle
            print(linkJob)
            linkJob = dinhDangLink(linkJob)
            driver.switch_to.window(driver.window_handles[-1])
            # driver.get(linkJob)
            time.sleep(random.randint(20, 40))
            listLikeTypes = ["TĂNG LIKE CHO BÀI VIẾT",'TĂNG THƯƠNG THƯƠNG CHO BÀI VIẾT', "TĂNG WOW CHO BÀI VIẾT", 'TĂNG LOVE CHO BÀI VIẾT']
            if jobType in listLikeTypes:
                print(1)
                driver.get(linkMbasic(linkJob)) 
                time.sleep(5)
                element = driver.find_element(By.XPATH, "//*[contains(text(), 'Bày tỏ cảm xúc')]") 
                element.click()
                time.sleep(2)
                if jobType == "TĂNG LIKE CHO BÀI VIẾT":
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Thích')]")
                    element.click()
                    time.sleep(5)
                    print(Style.BRIGHT + Fore.GREEN + "Like thành công" + Style.RESET_ALL)
                    d = True
                elif jobType == 'TĂNG THƯƠNG THƯƠNG CHO BÀI VIẾT':
                    time.sleep(2)
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Thương thương')]")
                    element.click()
                    time.sleep(5)
                    print(Style.BRIGHT + Fore.GREEN + "Thả Thương thương thành công" + Style.RESET_ALL)
                    d = True
                elif jobType == 'TĂNG LOVE CHO BÀI VIẾT':
                    time.sleep(2)
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Yêu thích')]")
                    element.click()
                    time.sleep(5)
                    print(Style.BRIGHT + Fore.GREEN + "Thả Love thành công" + Style.RESET_ALL)
                    d = True
                elif jobType == 'TĂNG WOW CHO BÀI VIẾT':
                    time.sleep(2)
                    element = driver.find_element(By.XPATH, "//*[contains(text(), 'Wow')]")
                    element.click()
                    time.sleep(5)
                    print(Style.BRIGHT + Fore.GREEN + "Thả Wow thành công" + Style.RESET_ALL)
                    d = True
            else:  
                print(2)
                element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.x1qhmfi1.x1r1pt67")))
                if element:
                    for i in range(len(list(element))):
                        # t = element[i].get_attribute("aria-label")
                        b = element[i].find_element(By.CSS_SELECTOR, ".x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft")
                        t = b.text
                        if t:
                            print(t)
                            if t == "Đã thích":
                                d = True
                            elif t == "Thích": #or t == "Theo dõi":
                                print(2)
                                driver.execute_script("window.scrollTo(0, 300)")
                                time.sleep(1)
                                print(t)
                                element[i].click()
                                time.sleep(3)
                                print(Style.BRIGHT + Fore.GREEN + "Like thành công"  + Style.RESET_ALL)
                                d = True
                                break
            if d == False:
                print(3)
                try:
                    follow = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3")))
                    # tf = follow.get_attribute("aria-label")       x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3
                    # print(tf)
                    for i in range(len(list(follow))):
                        tf = follow[i].get_attribute("aria-label")
                        
                        if str(tf) == "Theo dõi" or str(tf) == "Thêm bạn bè" or str(tf) == "Thích":
                            print(tf)
                            follow[i].click()
                            print(Style.BRIGHT + Fore.GREEN + "Theo dõi thành công" + Style.RESET_ALL)
                            break
                except (NoSuchElementException, ElementClickInterceptedException):
                    pass
            time.sleep(3)
            driver.close()
            driver.switch_to.window(tabHienTai)

        except NoSuchElementException:
            print("No Such Element")
            driver.close()
            # driver.switch_to.window(tabHienTai)
        # time.sleep(10)
        # driver.switch_to.window(tabJobdetail)
        time.sleep(2)
        hoanThanh = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.card-job-detail.hand")))
        if hoanThanh:
            hoanThanh[0].click()
            element = wait.until(EC.presence_of_element_located((By.ID, "swal2-content")))
            dontReports = element.text
            print(Back.WHITE + Fore.GREEN + dontReports+ Style.RESET_ALL)
        # if jobType == "TĂNG LƯỢT THEO DÕI":
        #     element = driver.find_element(By.CSS_SELECTOR, ".card.card-job-detail")
        #     element.click()
    work(jobType)
    
    time.sleep(10)
    try:
        confirm_alert = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
        confirm_alert.click()
        time.sleep(5)
    except (NoSuchElementException, ElementClickInterceptedException):
        while True:
            if str(input("Giải Captcha! Nhập 'c' để tiếp tục: ")) == 'c':
                try:
                    confirm_alert = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
                    confirm_alert.click()
                    break
                except NoSuchElementException:
                    break
driver.quit()