import pyautogui

def location_IMG(scr):
    image_path = str(scr)
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    return location
scr = "hoanthanh.png"
# if location_IMG(scr):
#     x, y, w, h = location_IMG(scr)
#     print(x, y)
# else:
#     print("Không tìm thấy ảnh")
pyautogui.scroll(-200)