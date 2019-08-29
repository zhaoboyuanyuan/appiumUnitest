#coding=utf-8
'''
Created on 2018年6月12日

@author: 赵永健，公共方法类
'''
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,\
    expected_conditions
from appium.webdriver.mobilecommand import MobileCommand
from pickle import classmap



class commonProc(object):
    #点击ID控件
    def clickById(self,driver,id):
        driver.find_element_by_id(id).click()
        
#     点击xpath的控件
    def clickByXpath(self,driver,xpath):
        driver.find_element_by_xpath(xpath).click()
    
#     根据ID输入内容
    def enterTextById(self,driver,id,content):
        con=content.decode("utf-8")
        driver.find_element_by_id(id).send_keys(con)
    
#     根据xpath输入内容    
    def enterTextByXpath(self,driver,xpath,content):
        con=content.decode("utf-8")
        driver.find_element_by_xpath(xpath).send_keys(con)
        
      
    def getSize(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)
               
    #向上滑动，x轴不变，y轴从大变小（实验结果），t一般设置为200
    def swipeUp(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.5)    #获取x坐标，根据实际调整相乘参数     
        y1 = int(w_size[1] * 0.8)    #获取起始y坐标，根据实际调整相乘参数       
        y2 = int(w_size[1] * 0.2)    #获取终点y坐标，根据实际调整相乘参数
        driver.swipe(x1, y1, x1, y2,200)
        
    #向下滑动，x轴不变，y轴从小变大    
    def swipeDown(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.5)    #获取x坐标，根据实际调整相乘参数     
        y1 = int(w_size[1] * 0.2)    #获取起始y坐标，根据实际调整相乘参数       
        y2 = int(w_size[1] * 0.8)    #获取终点y坐标，根据实际调整相乘参数
        driver.swipe(x1, y1, x1, y2,200)
        
#      向右滑动       
    def swipeLeft(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.8)    #获取起始x坐标，根据实际调整相乘参数
        x2 = int(w_size[0] * 0.05)   #获取终点x坐标，根据实际调整相乘参数
        y1 = int(w_size[1] * 0.5)    #获取y坐标，根据实际调整相乘参数
        driver.swipe(x1,y1,x2,y1,200)
        
#       向左滑动  
    def swipeRight(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.05)    #获取起始x坐标，根据实际调整相乘参数
        x2 = int(w_size[0] * 0.8)   #获取终点x坐标，根据实际调整相乘参数
        y1 = int(w_size[1] * 0.5)    #获取y坐标，根据实际调整相乘参数
        driver.swipe(x1,y1,x2,y1,200)
    
#     判断是否是包涵这个ID的页面 
    def waitForPageById(self,driver,id,msg):  
        try:
            driver.find_element_by_id(id)
        except:
            raise NameError(msg) 
        
#     获取控件的text
    def getText(self,driver,id):
        return driver.find_element_by_id(id).text

# 判断页面元素是否存在
    def isElement(self,driver,identifyBy,c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        flag=None
        try:
            if identifyBy == "id":
                #self.driver.implicitly_wait(60)
                driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                #self.driver.implicitly_wait(60)
                driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                driver.find_element_by_css_selector(c)
            flag = True
        except:
            flag = False
        finally:
            return flag
        
 # 判断页面上text是否存在   
    def findItem(self,driver,text):
        text=text.decode("utf-8")
        source = driver.page_source
        if text in source:
            return True
        else:
            return False
            
#     版本更新点击取消按钮
    def updateButton(self,driver):
#         if self.isElement(By.ID, ):
#             self.clickById(driver,("cc.wulian.smarthomev6:id/btn_negative")
#         result=self.findItem(driver,"取消")
        result=self.isElement(driver,By.ID,"cc.wulian.smarthomev6:id/btn_negative")
        if result:
           driver.find_element_by_id("cc.wulian.smarthomev6:id/btn_negative").click()           

    def initApp(self,driver):
        #判断是否有升级toast
        self.updateButton(driver)
        #判断是否跳过按钮
        skip = self.isElement(driver,By.ID,"cc.wulian.smarthomev6:id/btn_skip")
        if skip:
            driver.find_element_by_id("cc.wulian.smarthomev6:id/btn_skip").click()



        #     抛异常message
    def messageShow(self,msg):    
        raise NameError(msg)


    #     判断toast是否存在    
    def findToast(self,driver,message):
        message = '//*[@text=\'{}\']'.format(message)
        try:
            element = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            return True
        except:
            return False
        
#     等待activity
    def waitActivity(self,driver,activityName,msg):
        s=driver.wait_activity(activityName,3)
        print(s)
        if s==False:
            self.messageShow(msg)
            
#     判断是否登录
    def loginOrNot(self,driver):
        sleep(2)
        text=self.getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        txt=text.encode("utf-8")
        if cmp(txt, "登录/注册")==0:
            driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
            driver.wait_activity(".main.login.SigninActivity",3)
            driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644332")
            driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456abcd")
            driver.find_element_by_id("cc.wulian.smarthomev6:id/login").click()
            self.waitForPageById(driver, "cc.wulian.smarthomev6:id/fixed_bottom_navigation_container", "登录失败！")

#     切换至H5页面
    def switch_h5(self,driver):
        print driver.contexts
#     print driver.current_context 
#     print driver.page_source   打印H5源码
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_cc.wulian.smarthomev6"})

#   切换至原生
    def switch_app(self,driver):
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})  

#     设备列表页面点击设备
    def clickDevice(self,driver,deviceName,xpath): 
        for i in range(0,10):
            self.swipeUp(driver)
            if self.findItem(driver,deviceName):
                break
        driver.find_element_by_xpath(xpath).click()
                