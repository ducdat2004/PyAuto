from ppadb.client import Client as AdbClient
import requests, time, random
# Tạo đối tượng AdbClient
client = AdbClient(host="127.0.0.1", port=5037)

# Lấy danh sách các thiết bị được kết nối
devices = client.devices()

if len(devices) == 0:
    print("Không có thiết bị nào được kết nối")
else:
    # Lấy danh sách các thiết bị 
    devices = devices[0]
    print("Đã kết nối với thiết bị", devices.serial)
    #truyCapLink = f'am start -a android.intent.action.VIEW -d https://www.tiktok.com/@binanime17/video/7248448717454331141?is_from_webapp=1'
    # devices.shell(truyCapLink) # Mở một đường link bằng shell
    # time.sleep(10)
    # devices.shell(f'input tap 993 1098')
tokenTDS = "TDS0nIwEjclZXZzJiOiIXZ2V2ciwiI0IDdhR2Y1RmbhJHdiojIyV2c1Jye"
idTiktok = "tontu37"
cauHinh = requests.get("https://traodoisub.com/api/?fields=tiktok_run&id="+idTiktok+"&access_token="+tokenTDS) # cấu hình nick TDS và nick Tiktok muốn chạy

time.sleep(3)

kieuJob = "tiktok_like"
print("\033[92mSTART")
countNoDataLike = 0
while True:
    def thoiGianHienTai():
        thoi_gian_hien_tai = time.localtime()  # Lấy thông tin về thời gian hiện tại
        thoi_gian_format = time.strftime("%H:%M:%S", thoi_gian_hien_tai)  # Định dạng lại thời gian
        return(thoi_gian_format)
    layNhiemVu = requests.get("https://traodoisub.com/api/?fields="+kieuJob+"&access_token="+tokenTDS).json() # Lấy nhiệm vụ
    def checkData(layNhiemVu):
        if 'data' in dict(layNhiemVu):
            listData = layNhiemVu['data']
            if len(list(listData)) == 0:
                return False
                # countNoDataLike += 1
                # time.sleep(4)
                # continue
        else:
            return True
    if checkData(layNhiemVu) == False:
        # countNoDataLike += 1
        time.sleep(4)
        continue
    # else:
    #     countNoDataLike = 0
    # # print("")
    # if countNoDataLike > 4:
    #     countNoDataLike = 0
    #     countJobFollow = 0
    #     while countNoDataLike <= 10:
    #         countJobFollow += 1
    #         layNVFL = requests.get("https://traodoisub.com/api/?fields=tiktok_follow&access_token="+tokenTDS).json()
    #         if checkData(layNVFL) == False:
    #             time.sleep(5)
    #             continue
    #         if 'data' in layNVFL:
    #             listDataFL = layNVFL['data']
    #             print("Tìm thấy :", len(listDataFL), "nhiệm vụ Follow")
    #         else:
    #             print("Không có Job Follow")
    #             time.sleep(5)
    #             continue
    #         for l in listDataFL:
    #             idFL = l['id']
    #             linkFL = l['link']
    #             truyCapLinkFL = f'am start -a android.intent.action.VIEW -d {linkFL}'
    #             devices.shell(truyCapLinkFL) # Mở một đường link bằng shell
    #             time.sleep(random.randint(10, 20))
    #             devices.shell(f'input tap 984 975')
    #             time.sleep(3)
    #             try:
    #                 guiNVFL = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+idFL+'&access_token='+tokenTDS)
    #                 soJobFLDaLam = guiNVFL.json()['cache']
    #                 print("\033[94mSố job Follow đã gửi:", soJobFLDaLam)
    #             except requests.exceptions.ConnectionError:
    #                 time.sleep(5)
    #                 continue
    #             if int(soJobFLDaLam) >= 10:
    #                 nhanXu = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token='+tokenTDS).json()
    #                 print(nhanXu)
    #         time.sleep(5)
    # if len(listData) == 0:
    #     time.sleep(10)
    #     continue
    #Làm việc
    # listNV = layNhiemVu['data']
    if 'data' in layNhiemVu:
        listData = layNhiemVu['data']
        print("Tìm thấy :", len(listData))
    else:
        print("Không Có Job")
        time.sleep(3)
        continue
    for i in listData:
        idJob = i['id']
        linkJob = i['link']
        print(idJob, "Time:", thoiGianHienTai())
        print(linkJob, "Time:", thoiGianHienTai())
        truyCapLink = f'am start -a android.intent.action.VIEW -d {linkJob}'
        devices.shell(truyCapLink) # Mở một đường link bằng shell
        time.sleep(3)
        devices.shell(f'input tap 993 1098')
        time.sleep(5)
        try:
            guiNV = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+idJob+'&access_token='+tokenTDS)
            soJobDaLam = guiNV.json()['cache']
            print("\033[94mSố job đã gửi:", soJobDaLam)
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            continue
        time.sleep(5)
        if int(soJobDaLam) >= 10:
            time.sleep(3)
            nhanXu = requests.get('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token='+tokenTDS).json()
            dictNhanXu = nhanXu['data']
            soJobThanhCong = dictNhanXu['job_success']
            xuNhanDuoc = dictNhanXu['msg']
            xuHienTai = dictNhanXu['xu']
            

            print(f"\033[92mSố Job Hoàn Thành: {soJobThanhCong}|Xu nhận được: {xuNhanDuoc}|Xu hiện tại {xuHienTai}\nTime: {thoiGianHienTai()}")
    time.sleep(5)