import requests
import time
import subprocess
import random
from ppadb.client import Client 
# client = Client(host='127.0.0.1', port=5037)
# devices = client.devices()
# devices = devices[0]
# Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE2OTMxOTQ3NDQsImV4cCI6MTcyNDczMDc0NCwibmJmIjoxNjkzMTk0NzQ0LCJqdGkiOiJkUHNpMUdOVURKaFQ5OU9CIiwic3ViIjo5NjkzNSwicHJ2IjoiYjkxMjc5OTc4ZjExYWE3YmM1NjcwNDg3ZmZmMDFlMjI4MjUzZmU0OCJ9.dc08tt3MF01U1Etp_9hh-PLaZEg_DE7EiDszoO1CKdo
# delay = int(input("Nhập thời gian delay: "))
headers = {
    #dat5112004"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE2OTMyMjk1OTYsImV4cCI6MTcyNDc2NTU5NiwibmJmIjoxNjkzMjI5NTk2LCJqdGkiOiI1M0hLaTJ0aGc4cWVNNGxlIiwic3ViIjo5NjkzNSwicHJ2IjoiYjkxMjc5OTc4ZjExYWE3YmM1NjcwNDg3ZmZmMDFlMjI4MjUzZmU0OCJ9.eATOftpA9x-5n_g9N7NfQh7ia2Qg2WG8ylcuxQ-Q3Ms",
    #tranducdat24
    #"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE2OTMzMDI0NzksImV4cCI6MTcyNDgzODQ3OSwibmJmIjoxNjkzMzAyNDc5LCJqdGkiOiJLZGRuYTdEeEpaRU9MdTk1Iiwic3ViIjoyMDY3NTY5LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.1Uem6uF3h3mAzj8KD61NvlDUJIEkgn_REq5K9co9AJQ"
    "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE2OTM0NjY4MDMsImV4cCI6MTcyNTAwMjgwMywibmJmIjoxNjkzNDY2ODAzLCJqdGkiOiJxdDNtdzZHWmZGOWRMY0JVIiwic3ViIjo5NjkzNSwicHJ2IjoiYjkxMjc5OTc4ZjExYWE3YmM1NjcwNDg3ZmZmMDFlMjI4MjUzZmU0OCJ9.rrJsrOpq3TgunlfgGNsoVrBFKUKej8msl6FrL3mpJb0",
    "Content-Type" : "application/json;charset=utf-8",
    'authority': 'gateway.golike.net',
    'method': 'GET',
    'path': '/api/tiktok-account',
    'scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://app.golike.net',
    'Referer': 'https://app.golike.net/',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'T': 'VFZSWk5VMTZSVFJOVkdONlRXYzlQUT09' 
}
user_info = requests.get('https://gateway.golike.net/api/users/me', headers=headers)
print("Name Golike:", user_info.json()["data"]["name"])
print("User name Golike:", user_info.json()["data"]["username"])
print("Số dư:", str(user_info.json()["data"]["coin"])+"đ")
tt = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
# print(tt.json())
stt = 1
for i in tt.json()["data"]:
    nameTT = i["nickname"]
    idTT = i["unique_username"]
    id_userTT = i["id"]
    soJobDaLam = i["counter_jobs_follow_today"]
    print(f"Nick Tiktok thứ [{stt}] --> ID: {idTT}, Name: {nameTT}")
    print("Số Job đã làm hôm nay:", soJobDaLam)
    stt += 1
params = {
    'account_id': id_userTT,
    'data': 'null'
}
while True:
    try:
    # Lấy job
        getJ = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', headers=headers, params=params)
        # print(getJ.json())
    except (requests.exceptions.Timeout, requests.exceptions.RequestException):
        print("Nhận NV thất bại, thử lại sau 10s")
        time.sleep(10)
        continue
    if getJ.json()["success"]:
        idJob = getJ.json()["data"]["id"]
        linkJob = getJ.json()["data"]["link"]
        typeJob = getJ.json()["data"]["type"]
        object_id = getJ.json()["data"]["object_id"]
        # devices.shell("am start -a android.intent.action.VIEW -d {}".format(linkJob))
        print(f"Link Job: {linkJob} | Type: {typeJob} | ID: {idJob}")
        # subprocess.call("am start -a android.intent.action.VIEW -d {}".format(linkJob), shell = True)
        time.sleep(random.randint(5, 10))
        params = {
            'account_id' : id_userTT,
            'ads_id': idJob,
            'async': 'true',
            'data': 'null'
        }
        time.sleep(4)
        try:
            d = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, params=params)
            print(d.json()) 
            if d.json()['success'] == False:
                print("\033[31mRedHoàn thành thất bại")
                time.sleep(1)
            else:
                print("Nhận tiền thành công | +"+d.json()["prices"])
                continue
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            print("\033[31mRedRequests lỗi")
        try:
            print("\033[33mĐang thử hoàn thành lại")
            d = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, params=params)
            if d.json()["success"]:
                print("\033[32mHoàn thành lại thành công +"+d.json()["prices"])
                continue
            else:
                print("Hoàn thành lại thất bại")
                time.sleep(3)
        except requests.exceptions.Timeout:
            print("Yêu cầu hoàn thành quá thời gian")
            continue
        except requests.exceptions.RequestException:
            print("Lỗi không xác định")
            continue
        print("Đang bỏ qua Job")
        params1 = {
            'description' : "Tôi không muốn làm Job này",
            'error_type' : '0',
            'fb_id': id_userTT,
            'provider': "tiktok",
            'type': "ads",
            'users_advertising_id' : idJob
        }
        try:
            # Bỏ qua job
            send = requests.post("https://gateway.golike.net/api/report/send", headers=headers, params=params1)
            print(send.json())
            params2 = {
                'account_id': id_userTT,
                'ads_id': idJob,
                'object_id': object_id,
                'type': typeJob
            }
            skipJob = requests.post("https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs", headers=headers, params=params2)
            # print(skipJob.json())
            if skipJob.json()["success"]:
                print("Skip thành công")
            else:
                print("Skip thất bại")
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            print("requests skip lỗi")
            time.sleep(5)
            continue
        
        # time.sleep(5)
    else:
        print("Lấy job thất bại, lấy lại sau 10s")
        time.sleep(10)