#coding=utf-8
'''
Created on 2018年6月11日

@author: 赵永健，登录APP
'''
from appium import webdriver

from app.OpenApp import OpenApp
from time import sleep
from public.swipe import swipe
from process.commonProc import commonProc
from selenium.webdriver.common.by import By
from appium.webdriver.mobilecommand import MobileCommand
from public import excel
from wheel.signatures import assertTrue
from _random import Random


class loginProc(object):



    def loginNot(self,driver,text):
        txt=text.encode("utf-8")
        if cmp(txt, "登录/注册")!=0:
            commonProc().swipeUp(driver)
            driver.find_element_by_id("cc.wulian.smarthomev6:id/item_setting").click()
            driver.wait_activity(".main.mine.setting.SettingActivity", 3)
            driver.find_element_by_id("cc.wulian.smarthomev6:id/item_setting_logout").click()
            sleep(2)
            commonProc().swipeDown(driver)


#    1、 成功登录
    def loginSuccess(self,driver):
#         driver.find_element_by_id(excel.idCon("btn_negative")).click()
        commonProc().updateButton(driver)
        
        driver.find_element_by_xpath(excel.xpathCon("mine")).click()
        text=commonProc().getText(driver,excel.idCon("item_account_login_name"))
        self.loginNot(driver,text)
        driver.find_element_by_id(excel.idCon("item_account_login")).click()
        driver.wait_activity(excel.activityCon("SigninActivity"),3)
        driver.find_element_by_id(excel.idCon("username")).send_keys("15951644332")
        driver.find_element_by_id(excel.idCon("password")).send_keys("123456abcd")
        driver.find_element_by_id(excel.idCon("login")).click()
        commonProc().waitForPageById(driver, excel.idCon("fixed_bottom_navigation_container"), "登录失败！")
        print "登陆成功啦"
        
#    2、 账号为空   
    def noneUser(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456abcd")
        if driver.find_element_by_id("cc.wulian.smarthomev6:id/login").is_enabled():
            commonProc().messageShow("登录按钮未禁用！")
            
#     3、密码为空   
    def nonePass(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644332")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("")
        if driver.find_element_by_id("cc.wulian.smarthomev6:id/login").is_enabled():
            commonProc().messageShow("登录按钮未禁用！")
    
#     4、错误的账号（手机号）登录
    def wrongUser(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456abcd")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/login").click()
        s=commonProc().findToast(driver,"账号或密码不正确")
        print(s)
        if s==False:
            commonProc().messageShow("未弹出账号或密码不正确的提示框")
            
    #  5、错误的密码登录
    def wrongPass(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644332")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456ab")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/login").click()
        s=commonProc().findToast(driver,"用户密码错误")
        print(s)
        if s==False:
            commonProc().messageShow("未弹出用户密码错误的提示框")    
                
#     6、手机号登录，连续3次输错密码，不找回密码            
    def InputAsCancel(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644332")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456ab")
        for i in range(0,10):
            driver.find_element_by_id("cc.wulian.smarthomev6:id/login").click()
            if commonProc().findItem(driver, "找回密码"):
                break
        commonProc().clickById(driver, "cc.wulian.smarthomev6:id/dialog_btn_negative")
    
    #     7、手机号登录，连续3次输错密码，找回密码            
    def InputAsSure(self,driver):
        commonProc().updateButton(driver)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()
        text=commonProc().getText(driver,"cc.wulian.smarthomev6:id/item_account_login_name")
        self.loginNot(driver,text)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/item_account_login").click()
        driver.wait_activity(".main.login.SigninActivity",3)
        driver.find_element_by_id("cc.wulian.smarthomev6:id/username").send_keys("15951644332")
        driver.find_element_by_id("cc.wulian.smarthomev6:id/password").send_keys("123456ab")
        for i in range(0,10):
            driver.find_element_by_id("cc.wulian.smarthomev6:id/login").click()
            if commonProc().findItem(driver, "找回密码"):
                break
        commonProc().clickById(driver, "cc.wulian.smarthomev6:id/dialog_btn_positive")
        commonProc().waitActivity(driver, ".main.account.ForgotAccountActivity","未进入忘记密码页面")       
    
#     8、在H5页面点击
    def clickOnH5(self,driver):
        commonProc().updateButton(driver) 
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()  
        commonProc().loginOrNot(driver)
        commonProc().clickByXpath(driver, "//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]")
#         for i in range(0,10):
#             commonProc().swipeUp(driver)
#             if commonProc().findItem(driver, "移动插座"):
#                 break
        
#         commonProc().clickByXpath(driver, "//android.widget.ListView[@resource-id='cc.wulian.smarthomev6:id/lv_device']/android.widget.LinearLayout[7]")
        commonProc().clickDevice(driver,"移动插座", "//android.widget.ListView[@resource-id='cc.wulian.smarthomev6:id/lv_device']/android.widget.LinearLayout[7]")
        commonProc().waitActivity(driver,".main.device.DeviceDetailActivity","进入设备详情页面失败！")
#         print driver.contexts 
#         driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name":"WEBVIEW_cc.wulian.smarthomev6"})  
#         print driver.current_context 
#         print driver.page_source  
        sleep(2)
        commonProc().switch_h5(driver)
        #         点击打开按钮
        commonProc().clickByXpath(driver, "/html/body/section[1]/div[2]")
        #         打开更多按钮
        commonProc().clickByXpath(driver, "/html/body/header/div/a[3]")
#         driver.find_element_by_xpath("/html/body/section[1]/div[2]").click()
        sleep(2)
#         打开更多按钮
#         driver.find_element_by_xpath("/html/body/header/div/a[3]").click()
#         sleep(2)
        commonProc().switch_app(driver)
        commonProc().clickById(driver, "cc.wulian.smarthomev6:id/item_device_more_rename")
#         commonProc().enterTextById(driver,"cc.wulian.smarthomev6:id/et_user_info","移动")
#         commonProc().clickById(driver, "cc.wulian.smarthomev6:id/dialog_btn_positive")

# 9、在H5页面输入
    def enterOnH5(self,driver):
        commonProc().updateButton(driver) 
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]").click()  
        commonProc().loginOrNot(driver)
        commonProc().clickByXpath(driver,"//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]")
        commonProc().swipeDown(driver)
        commonProc().clickByXpath(driver, "//android.support.v7.widget.RecyclerView[@resource-id='cc.wulian.smarthomev6:id/home_scene_recyclerview']/android.widget.LinearLayout[4]")
        commonProc().clickById(driver, "cc.wulian.smarthomev6:id/all_scene_image_add")
        sleep(2)
        commonProc().switch_h5(driver)
        commonProc().enterTextByXpath(driver,"//*[@id='customScene_input_name']","小博")
        commonProc().clickByXpath(driver, "/html/body/section[2]/a[1]")
        commonProc().clickByXpath(driver, "//*[@id='customScene_sure']")
        
    

                
            
    
        
        
        
        