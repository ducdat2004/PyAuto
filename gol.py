import pyautogui
import time, random

def location_IMG(scr):
    image_path = str(scr)
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    return location
while True:
    time.sleep(3)
    # pyautogui.displayMousePosition()
    pyautogui.click(1026, 539)
    while True:
        time.sleep(5)
        if location_IMG('follow_job.png'):
            break
        
    
    if location_IMG('get_job.png'):
        if location_IMG('follow_job.png'):
            x, y, w, h = location_IMG('get_job.png')
            pyautogui.click(x, y)
        else:
            #confirm alert
            # pyautogui.click(953, 724)
            time.sleep(1)
            x, y, w, h = location_IMG('baoloi.png')
            pyautogui.click(x, y)
            time.sleep(1)
            pyautogui.scroll(-200)
            time.sleep(1)
            x, y, w, h = location_IMG('send_report.png')
            pyautogui.click(x, y)
            continue
    time.sleep(5)


    if location_IMG('follow.png'):
        x, y, w, h = location_IMG('follow.png')
        time.sleep(random.randint(5, 10))
        pyautogui.click(x + 20, y + 20)
        time.sleep(8)
        pyautogui.hotkey('ctrl', '1')
        time.sleep(2)
        x, y, w, h = location_IMG('hoanthanh.png')
        pyautogui.click(x, y)
        time.sleep(15)
        pyautogui.click(953, 724)
    else:
        print("Không tìm thấy ảnh")
        pyautogui.hotkey('ctrl', '1')
        time.sleep(1)
        x, y, w, h = location_IMG('baoloi.png')
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.scroll(-200)
        time.sleep(1)
        x, y, w, h = location_IMG('send_report.png')
        pyautogui.click(x, y)
        time.sleep(15)
        #confirm alert
        pyautogui.click(953, 724)