from selenium import webdriver
from common.readExcel import ExcelData  # 从readExcel.py中导入ExcelData方法
from common.screenShot import save_screenShot   # 从screenShot.py中导入save_screenShot方法
from time import sleep
import logging


class Login(object):
    """
    封装公用方法-登录
    """

    def __init__(self):
        self.a = ExcelData("登录")
        self.login_name = "19542820141"
        self.login_password = "yuzhen123"
        self.base_url = "https://crm.mgm-iot.com:8667/#/login"
        self.driver = webdriver.Chrome()
        self.log = logging.getLogger()

    def login(self):
        self.log.info("==========登录模块==========")
        self.driver.maximize_window()
        self.driver.get(self.base_url)

        user = self.driver.find_element_by_name(self.a.get_data("user"))
        user.clear()
        sleep(0.5)
        user.send_keys(self.login_name)
        self.log.info("输入的账户为：{}".format(self.login_name))

        psw = self.driver.find_element_by_name(self.a.get_data("psw"))
        psw.clear()
        sleep(0.5)
        psw.send_keys(self.login_password)
        self.log.info("输入的密码为：{}".format(self.login_password))

        self.driver.find_element_by_css_selector(self.a.get_data("submit")).click()
        sleep(2)
        if self.driver.current_url == self.a.get_data("current_url"):
            print("登录成功！")
            self.log.info("==========登陆成功！！！==========")
            sleep(1)
        else:
            print("登录失败！")
            self.log.info("==========登录失败！！！请分析原因...==========")
            save_screenshot(self.driver)

    def login_out(self):
        sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    Login().login()
    Login().login_out()
