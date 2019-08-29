#coding=utf-8
'''
Created on 2018年5月29日

@author: 赵永健
'''
from appium import webdriver
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,\
    expected_conditions
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

def open(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': '*',
                        'noReset':True,
                        'appPackage': 'cc.wulian.smarthomev6',
                        'appActivity': 'cc.wulian.smarthomev6.main.welcome.SplashActivity',
#                         'appPackage': 'com.wandoujia.phoenix2',
#                         'appActivity': 'com.wandoujia.jupiter.activity.HomeActivity',
                        'automationName':'Uiautomator2'
#                         'newCommandTimeout':'6000'  
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def panduan(s):
    if s!=None:
        return True
    else:
        return False


def stringEque(s,a):
    if cmp(s, a)==0:
        return True
    else:
        return False
    
        
def findToast(self,message):
        message = '//*[@text=\'{}\']'.format(message)
        try:
            element = WebDriverWait(self.driver,10,0.1).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            return True
        except:
            return False
   
    
# if __name__ == '__main__':
#    d= panduan("")
#     print d
#    a="赵永健"
#    b="赵"
#    print stringEque(a, b)
    
    