from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pickle, time
from ppadb.client import Client as adbclient
import random
import pyperclip
client = adbclient(host="127.0.0.1", port=5037)
devices = client.devices()
indexDevice = int(input("Index devices: "))
if len(list(devices)) != 0:
    devices = devices[indexDevice]
    print("Đã kết nối với thiết bị:", devices.serial)
else:
    print("Không tìm thấy thiết bị nào")
userGolike = 'tranducdat24'
passGolike = 'az0777541112'

mobile_emulation = {
    "deviceName" : "SamSung S23"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=600,812") 
chrome_options.add_argument(f'--user-agent={mobile_emulation["deviceName"]}')
chrome_options.add_argument('--executable_path=/chromedriver.exe')
chrome_options.add_argument('--disable-images')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
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
time.sleep(15)
driver.get('https://app.golike.net/jobs/tiktok')
wait = WebDriverWait(driver, 20)
b = True
wait5s = WebDriverWait(driver, 5)
while True:
    try:
        wait1 = WebDriverWait(driver, 10)
        time.sleep(random.uniform(1.5647, 3.15456))
        try:
            element_getjob = wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.card-job-detail.mt-3.bg-gradient-tiktok")))
            element_getjob.click()
            # time.sleep(10)
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            try:
                wait5s = WebDriverWait(driver, 5)
                confirm_alert = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                confirm_alert.click()
                continue
            except (NoSuchElementException, TimeoutException):
                continue
        if b:
            try:
                daHieu = wait.until(EC.presence_of_element_located((By.ID, "agree")))
                time.sleep(2)
                daHieu.click()
                time.sleep(2)
                agree = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
                # time.sleep(2)
                agree.click()
                b =False
            except (TimeoutException, ElementClickInterceptedException):
                pass
        def skipJob():
            print("bao loi 1")
            try:
                baoLoi = wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".row.mt-3")))
                baoLoi.click()
                # time.sleep(2)
                # driver.execute_script("window.scrollTo(0, 1500)")
                time.sleep(random.uniform(3.1254, 5.64562))
                sendRequest = wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.form-control.mt-3")))
                sendRequest.send_keys(Keys.END)
                time.sleep(1)
                sendRequest.click()     
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, TimeoutException):
                current_window = driver.current_window_handle
                try:
                    baoLoi = wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-12.px-0")))
                    time.sleep(1)
                    baoLoi[1].click()
                    # time.sleep(random.uniform(3.1254, 5.64562))
                    print("bao loi 2.1")                            
                    sendRequest = wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.form-control.mt-3")))
                    sendRequest.send_keys(Keys.END)
                    time.sleep(1)
                    sendRequest.click()  
                except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException, TimeoutException):
                    time.sleep(2)
                    if len(driver.window_handles) > 1:
                        print("close tab")
                        driver.switch_to.window(driver.window_handles[-1])
                        driver.close()
                        driver.switch_to.window(current_window)
                    baoLoi = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-12.px-0")))
                    time.sleep(1)
                    baoLoi[2].click()
                    print("bao loi 2.2")
                    sendRequest = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.form-control.mt-3")))
                    # time.sleep(random.uniform(1))
                    sendRequest.send_keys(Keys.END)
                    time.sleep(1)
                    sendRequest.click() 
            # time.sleep(3) 
        try:
            # time.sleep(random.uniform(1.25864, 4.564248))
            element = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ml-1.d400.font-weight-bold'))).text
            typeJob = element
            soLuongConLai = wait5s.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/span/span'))).text
            print(typeJob)
            if str(typeJob).strip() == "TĂNG LƯỢT COMMENT":
                time.sleep(2)
                element = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.font-bold.font-18.b200')))
                element.click()
                time.sleep(1)
                noiDungCMT = pyperclip.paste()
                idJob = wait5s.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div/div[2]/b')))
                idJob = idJob.text
                print(noiDungCMT)
                w = (str(idJob)).strip()
                open("CM.txt", "a").write(w)
                open("CM.txt", "a", encoding="utf-8").write(noiDungCMT.strip())
                getLink = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.bg-button-1.px-0.btn-block")))
                current_window = driver.current_window_handle
                getLink.click()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(1)
                driver.close()
                driver.switch_to.window(current_window)
                hoanThanh = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".col-12.px-0.mt-3"))) 
                # time.sleep(random.uniform(5.4552, 10.6745))
                time.sleep(random.uniform(4.7552, 5.6745))
                hoanThanh.click()
                continue
            elif (str(typeJob).strip() != 'TĂNG LƯỢT THEO DÕI' and str(typeJob).strip() != 'TĂNG LIKE CHO BÀI VIẾT') or int(soLuongConLai) < 8:
                try:
                    time.sleep(2)
                    element = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.font-bold.font-18.b200')))
                    element.click()
                except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
                    pass
                # time.sleep(1)
                skipJob()
                continue
            getLink = wait5s.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.bg-button-1.px-0.btn-block")))
            current_window = driver.current_window_handle
            linkJob = getLink.get_attribute("href")
            # time.sleep(random.uniform(2.2345, 5.6453))
            getLink.click()
            print(linkJob)
            devices.shell(f'am start -a android.intent.action.VIEW -d "{linkJob}"')
            time.sleep(random.uniform(2.5254, 3.254))
            if str(typeJob).strip() == 'TĂNG LƯỢT THEO DÕI':
                devices.shell('input tap 439 782')
            else:
                devices.shell('input tap 999 1034')
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            try:
                wait3 = WebDriverWait(driver, 40)
                confirm_alert = wait3.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                confirm_alert.click()
                continue
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                continue
        driver.switch_to.window(driver.window_handles[-1])
        # devices.shell(f'am start -a android.intent.action.VIEW -d "{linkJob}"')
        # time.sleep(random.uniform(3.4514, 8.12546))
        # devices.shell('input tap 164 376')
        # time.sleep(random.uniform(2.456, 6.234))
        if len(driver.window_handles) > 1:
            driver.close()
        driver.switch_to.window(current_window)
        hoanThanh = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".col-12.px-0.mt-3"))) 
        # time.sleep(random.uniform(5.4552, 10.6745))
        time.sleep(random.uniform(4.8552, 5.6745))
        hoanThanh.click()
        def checkNoiDungThongBao():
            wait0 = WebDriverWait(driver, 10)
            content = wait0.until(EC.presence_of_element_located((By.ID, 'swal2-content')))
            print(content.text)
            contentDoneRp = removeNumber(str(content.text)).strip() 
            confirm_alert = wait0.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
            # time.sleep(random.uniform(2.34514, 4.6452))
            confirm_alert.click()
            if contentDoneRp == 'Báo cáo thành công,số TIỀN làm được sẽ được cộng sau ÍT PHÚT ! Số jobs đã làm trong ngày':
                return True
            else:
                return False
        def removeNumber(s):
            kq = ""
            for i in range(len(s)):
                n = 0
                try:
                    n = int(s[i])
                except ValueError:
                    kq += s[i]
            return kq
        try:
            content = wait.until(EC.presence_of_element_located((By.ID, 'swal2-content')))
            ct = str(content.text)
            listE = ['Hệ thống kiểm tra bạn chưa thực hiện thao tác follow !', 
                    'Yêu cầu đã bị xóa,hoặc bạn đã quá hạn làm việc !', 
                    'Yêu cầu đã bị xóa,hoặc bạn đã quá hạn làm việc !',
                    ]
            def checkNoiDungThongBao():
                content = wait0.until(EC.presence_of_element_located((By.ID, 'swal2-content')))
                print(content.text)
                contentDoneRp = removeNumber(str(content.text)).strip() 
                confirm_alert = wait0.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                # time.sleep(random.uniform(2.34514, 4.6452))
                confirm_alert.click()
                if contentDoneRp == 'Báo cáo thành công,số TIỀN làm được sẽ được cộng sau ÍT PHÚT ! Số jobs đã làm trong ngày':
                    return True
                else:
                    return False
            d = ct
            ct = removeNumber(ct)
            if ct.strip() == 'Báo cáo thành công,số TIỀN làm được sẽ được cộng sau ÍT PHÚT ! Số jobs đã làm trong ngày':
                print("\033[32m"+d)
                print('ok') 
            if ct.strip() != 'Báo cáo thành công,số TIỀN làm được sẽ được cộng sau ÍT PHÚT ! Số jobs đã làm trong ngày':
                print("\033[31m"+d)
                confirm_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                confirm_alert.click()
                soLanHoanThanh = 0
                done = False
                for i in range(2):
                    wait0 = WebDriverWait(driver, 10)                
                    try:
                        hoanThanh = wait0.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".col-12.px-0.mt-3"))) 
                        hoanThanh.click()
                        content = wait0.until(EC.presence_of_element_located((By.ID, 'swal2-content')))
                        print(content.text)
                        contentDontrRp = removeNumber(str(content.text)).strip() 
                        confirm_alert = wait0.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                        # time.sleep(random.uniform(2.34514, 4.6452))
                        confirm_alert.click()
                        if contentDontrRp.strip() == 'Báo cáo thành công,số TIỀN làm được sẽ được cộng sau ÍT PHÚT ! Số jobs đã làm trong ngày':
                            print('hoan thanh')
                            done = True
                            break
                        else:
                            done = False
                    except (NoSuchElementException, ElementClickInterceptedException, TimeoutException):
                        pass
                # skip
                if done == False:
                    try:
                        confirm_alert = wait0.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                        confirm_alert.click()
                    except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException, TimeoutException):
                        pass
                    try:
                        skipJob() 
                    except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException, TimeoutException):
                        try:
                            wait3 = WebDriverWait(driver, 3)
                            confirm_alert = wait3.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                            confirm_alert.click()
                        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                            continue
            else:
                confirm_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")))
                confirm_alert.click()
        except (NoSuchElementException, ElementClickInterceptedException, TimeoutException):
            # Bo qua captcha
            print('Captcha')
            # driver.refresh()
            hoanThanh = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".col-12.px-0.mt-3"))) 
            # time.sleep(random.uniform(5.4552, 10.6745))
            time.sleep(random.uniform(2.7552, 5.6745))
            hoanThanh.click()
            time.sleep(2)
            if checkNoiDungThongBao() == False:
                skipJob()  

            try:
                confirm_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm.swal2-styled"))) 
                confirm_alert.click()
            except (TimeoutException, NoSuchElementException):
                pass
    except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException, TimeoutException, StaleElementReferenceException):
        time.sleep(3)
        pass
    time.sleep(random.uniform(5.4562, 15.23452))