
# -*- coding: UTF-8 -*-

'''
打开uc app
'''
from time import sleep

from appium import webdriver


class openUc(object):

    dr=None
    def open(self):
        desired_cap={
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': '*',
            'noReset': True,
            'resetKeyboard': True,
            "unicodeKeyboard": True,
            'app': 'D:\\UCBrowser.apk',
            'appPackage': 'com.UCMobile',
            'appActivity': 'com.uc.browser.InnerUCMobile',
            'automationName': 'Uiautomator2'
        }
        driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
        self.dr=driver
        print("打开成功")
        sleep(5)

    def getDr(self):
        return self.dr

    def after(self):
        self.dr.quit()
        print('退出成功')
        self.dr=None


o=openUc()
o.open()
print(o.getDr())
o.after()