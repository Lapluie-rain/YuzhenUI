import time


def save_screenShot(driver):
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    pic_path = "../screenshot/"+now+'_screen.png'
    driver.save_screenshot(pic_path)