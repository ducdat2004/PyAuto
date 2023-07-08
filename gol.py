from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from ppadb.client import Client as adbclient
from selenium.common.exceptions import NoSuchElementException
# Khởi tạo trình điều khiển Selenium cho trình duyệt Chrome
client = adbclient(host="127.0.0.1", port=5037)

# Lấy danh sách các thiết bị được kết nối
devices = client.devices()
if len(devices) == 0:
    print("Kết nối không thành công")
else:
    devices = devices[0]
    print("Đã kết nối với thiế bị", devices.serial)
driver = webdriver.Chrome()

# Mở trình duyệt và truy cập URL chứa form
driver.get('https://app.golike.net/login')
u = driver.find_element(By.CLASS_NAME, "form-control")
u.click()
u.send_keys("tranducdat204")
time.sleep(3)
# Tìm div thứ hai trong form bằng XPath
second_div = driver.find_element(By.XPATH, '//form/div[2]')
time.sleep(2)
p = second_div.find_element(By.TAG_NAME, 'input')
p.click()
time.sleep(3)
p.send_keys("az0777541112")
time.sleep(2)
submit = driver.find_element(By.CSS_SELECTOR, ".btn.bg-gradient-1.py-2.border-0.text-light.btn-block")
submit.click()
time.sleep(5)
driver.implicitly_wait(30)
time.sleep(5)
# kt = driver.find_element(By.CSS_SELECTOR, ".col.px-0.hand")
# kt.click()


#kt = driver.find_element(By.XPATH, "//div[@class=row text-center align-items-center justify-content-center]/div[2]") # C1 

# second_div = driver.find_element(By.CSS_SELECTOR, '.row.text-center.align-items-center.justify-content-center > div:nth-child(2)')
# print(second_div.get_attribute('outerHTML'))
# second_div.click()
driver.get("https://app.golike.net/jobs")
time.sleep(3)
# click nào nền tảng làm việc TikTok
tt = driver.find_element(By.CSS_SELECTOR, ".card.shadow-400.h-100.mb-3.hand.bg-gradient-tiktok")
tt.click()
time.sleep(3)
b = 0
def thoiGianHienTai():
    thoi_gian_hien_tai = time.localtime()  # Lấy thông tin về thời gian hiện tại
    thoi_gian_format = time.strftime("%H:%M:%S", thoi_gian_hien_tai)  # Định dạng lại thời gian
    return(thoi_gian_format)
while b <= 15:
    b += 1
    if b % 10 == 0:
        time.sleep(10)
    # Nhận job tiktok
    try:
        nhanJob = driver.find_element(By.CSS_SELECTOR, ".card.card-job-detail.mt-3.bg-gradient-tiktok") 
        nhanJob.click()
    except NoSuchElementException:
        loiFl = driver.find_element(By.ID, "swal2-content").get_attribute('textContent')
        loiFl = loiFl.strip()
        if str(loiFl) == "Hệ thống kiểm tra bạn chưa thực hiện thao tác follow !":
            element =driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
            element.click()
            time.sleep(2)
            element = driver.find_element(By.CSS_SELECTOR, ".col-12.px-0")
            element.click()
            time.sleep(1)
            element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.form-control.mt-3")
            element.click()
            time.sleep(8)
    time.sleep(5)
    # Xử lý alert
    if b == 1:
        daHieu = driver.find_element(By.ID, "agree")
        daHieu.click()
        agree = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        agree.click()
    ###################
    time.sleep(8)
    driver.get("https://app.golike.net/jobs/tiktok/job-detail")
    getLink = driver.find_element(By.CSS_SELECTOR, ".btn.bg-button-1.px-0.btn-block") 

    linkJob = getLink.get_attribute("href")
    getLink.click()
    print(linkJob)
    element = driver.find_element(By.CSS_SELECTOR, ".ml-1.d400.font-weight-bold")
    typee = element.get_attribute("textContent")
    typee = typee.strip()
    if str(typee) == "TĂNG LƯỢT THEO DÕI":
        print("1")
        truyCapLink = f'am start -a android.intent.action.VIEW -d {linkJob}' 
        devices.shell(truyCapLink) # Gửi một đường link đến điện thoại được kết nối
        time.sleep(random.randint(20, 35))
        devices.shell("input tap 543 823") # tap vào một tạo độ trên điện thoại 
        time.sleep(3)
    else:
        print("2")
        truyCapLink = f'am start -a android.intent.action.VIEW -d {linkJob}' 
        devices.shell(truyCapLink) # Gửi một đường link đến điện thoại được kết nối
        time.sleep(25)
        devices.shell("input tap 993 1098") # tap vào một tạo độ trên điện thoại 
        time.sleep(3)
    # second_div.click()
    # time.sleep(2)
    # second_div.send_keys("a")
    # In ra nội dung của div thứ hai
    # print(second_div.get_attribute('outerHTML'))

    #*****
    # element = driver.find_element(By.CLASS_NAME, "row")

    # fistDiv = driver.find_element(By.CSS_SELECTOR, ".row.mt-3 > div:nth-child(1)")
    # print(fistDiv)
    # check = fistDiv.find_element(By.TAG_NAME, "button").get_attribute('text')
    # print(check)
    # if(check == "Báo lỗi"):
    #     secondDiv = driver.find_element(By.CSS_SELECTOR, ".row.mt-3 > div:nth-child(2)")
    #     print(secondDiv)
    #     second_div.click()
    # time.sleep(5)
    tabHienTai = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    time.sleep(2)
    driver.switch_to.window(tabHienTai)
    hoanThnah = driver.find_element(By.CSS_SELECTOR, ".col-12.px-0.mt-3")
    hoanThnah.click()

    time.sleep(10)
    
    element = driver.find_element(By.ID, "swal2-content")
    report = element.get_attribute("textContent")
    print("\033[92m", report, thoiGianHienTai())
    
    element = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
    element.click()
    time.sleep(3)