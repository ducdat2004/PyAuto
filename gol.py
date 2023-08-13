import pyautogui
import time, random


def location_IMG(scr):
    image_path = str(scr)
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    return location
def skip():
    pyautogui.click(953, 724)
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

while True:
    time.sleep(5)
    # pyautogui.displayMousePosition()
    if location_IMG("getJob.png"):
        x, y, w, h = location_IMG("getJob.png")

        pyautogui.click(x, y)
        
    soLanCheck = 0
    while True:
        time.sleep(5)
        pyautogui.click(953, 724)
        if location_IMG('follow_job.png') or soLanCheck >= 5:
            break
        soLanCheck += 1
    if soLanCheck >= 5:
        continue
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
            time.sleep(5)
            pyautogui.click(953, 724)
            continue
    time.sleep(5)

    # Follow action
    if location_IMG('follow.png'):
        x, y, w, h = location_IMG('follow.png')
        time.sleep(random.randint(5, 10))
        pyautogui.click(x + 20, y + 20)
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        x, y, w, h = location_IMG('hoanthanh.png')
        pyautogui.click(x, y)
        time.sleep(10)
        if location_IMG('error.png'):
            skip()
            continue
        else:
            pyautogui.click(953, 724)
    else:
        print("Captcha")
        pyautogui.hotkey('ctrl', '1')
        time.sleep(1)
        if location_IMG('baoloi.png'):
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
        else:
            continue
