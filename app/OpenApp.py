#coding=utf-8
'''
Created on 2018年5月24日

@author: 赵永健    
appium 打开APP并登陆

'''
# -*- coding: UTF-8 -*-
from appium import webdriver
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,\
    expected_conditions
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

class OpenApp(object):
    dr=None
    
    def open(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': '*',
                        'noReset':True,
                        'resetKeyboard':True,
                        "unicodeKeyboard":True,
                        'app':'D:\\SmartHomev6.2.9.apk',
                        'appPackage': 'cc.wulian.smarthomev6',
                        'appActivity': 'cc.wulian.smarthomev6.main.welcome.SplashActivity',
#                         'appPackage': 'com.wandoujia.phoenix2',
#                         'appActivity': 'com.wandoujia.jupiter.activity.HomeActivity',
                        'automationName':'Uiautomator2'
                        
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         driver.capabilities.setCapability("noReset", True);

        self.dr=driver
        print("打开app成功")
        sleep(5)
    
    def getDr(self):
        dr=self.dr
        return dr
    
    def after(self):
        self.dr.quit()
        print('退出成功')


    def login(self):

        # self.dr.find_element_by_id('cc.wulian.smarthomev6:id/btn_skip').click() #跳过
        # self.dr.find_element_by_id("cc.wulian.smarthomev6:id/btn_negative").click()  #升级取消按钮
        self.dr.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        self.dr.find_element_by_id('cc.wulian.smarthomev6:id/item_account_login').click()
#         context = self.dr.find_element_by_id('cc.wulian.smarthomev6:id/username').get_attribute('text')
#         self.edittextclear(context)
        sleep(2)
        self.dr.find_element_by_id('cc.wulian.smarthomev6:id/username').send_keys('15951644332')
        self.dr.find_element_by_id('cc.wulian.smarthomev6:id/password').send_keys('123456abc')
        self.dr.find_element_by_id('cc.wulian.smarthomev6:id/login').click()
#         toast_loc = ("xpath", ".//*[contains(@text,'再按一次退出')]")
#         t = WebDriverWait(self.dr, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
#         t = WebDriverWait(self.dr,10,0.1).until(expected_conditions.presence_of_element_located((toast_loc)))
#         print t

        
        
        
        
#     判断toast是否存在    
    def findToast(self,message):
        message = '//*[@text=\'{}\']'.format(message)
        try:
            element = WebDriverWait(self.dr,10,0.1).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            return True
        except:
            return False
            
#         
o=OpenApp()
o.open()
o.login()
print(o.findToast("用户密码错误"))
o.after()


    
    
       
       
    
        