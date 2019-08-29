#coding=utf-8
'''
Created on 2018年6月15日

@author: 赵永健，改写loginProc,优化写法
'''
from process.commonProc import commonProc
from public import excel
from process.loginProc import loginProc
from model.loginModel import loginModel
from time import sleep
import random

lm=loginModel()

class CploginProc(object): 
     
    def baseProc(self,driver,list=[]): 
        for i in list:
            self.switch(driver, i) 
    
    def switch(self,driver,num):
        if num==0:# 版本更新取消按钮
            commonProc().initApp(driver)
        elif num==1:#点击我的
            driver.find_element_by_xpath(excel.xpathCon("mine")).click() 
        elif num==2:#判断是否登录，登录就退出
            text=commonProc().getText(driver,excel.idCon("item_account_login_name"))
            loginProc().loginNot(driver,text)
        elif num==3:#点击用户名，进入登录页
            driver.find_element_by_id(excel.idCon("item_account_login")).click()
            driver.wait_activity(excel.activityCon("SigninActivity"),3)
        elif num==4:
            driver.find_element_by_id(excel.idCon("username")).send_keys(lm.userName)
        elif num==5:
            driver.find_element_by_id(excel.idCon("password")).send_keys(lm.password)
        elif num==6:
            driver.find_element_by_id(excel.idCon("login")).click()
        elif num==7:#登录之后进入首页
            sleep(3)
            commonProc().waitForPageById(driver, excel.idCon("fixed_bottom_navigation_container"), lm.msg)
        elif num==8:#判断登录按钮禁用
            if driver.find_element_by_id(excel.idCon("login")).is_enabled():
                commonProc().messageShow(lm.msg)
        elif num==9:#toast提示
            s=commonProc().findToast(driver,lm.msg)
            print(s)
            if s==False:
                commonProc().messageShow("未弹出"+lm.msg+"的提示框")
        elif num==10:#连续3次输入错误密码
            for i in range(0,10):
                driver.find_element_by_id(excel.idCon("login")).click()
                sleep(2)
                if commonProc().findItem(driver, "找回密码"):
                    break
        elif num==11:#点击取消按钮
            commonProc().clickById(driver, lm.buttonTxt)
        elif num==12:#判断是否进入忘记密码页面
            commonProc().waitActivity(driver, excel.activityCon("ForgotAccountActivity"),lm.msg)   
        #H5页面测试
        elif num==13:#判断是否登录，未登录则登录
            commonProc().loginOrNot(driver)
            
        elif num==14:#点击设备
            commonProc().clickByXpath(driver, excel.xpathCon("device"))
            
        elif num==15:#点击移动插座
            commonProc().clickDevice(driver,lm.deviceName, "//android.widget.ListView[@resource-id='cc.wulian.smarthomev6:id/lv_device']/android.widget.LinearLayout[7]")
        
        elif num==16:#进入设备详情页面
            commonProc().waitActivity(driver,".main.device.DeviceDetailActivity",lm.msg)
            sleep(2)
        elif num==17:#切换到H5页面点击开关，点击更多
            commonProc().switch_h5(driver)
        #         点击打开按钮
            commonProc().clickByXpath(driver, "/html/body/section[1]/div[2]")
        #         打开更多按钮
            commonProc().clickByXpath(driver, "/html/body/header/div/a[3]")
            sleep(2)
        elif num==18:#切换到app页面，点击
            commonProc().switch_app(driver)
            commonProc().clickById(driver, "cc.wulian.smarthomev6:id/item_device_more_rename")
        
        elif num==19:#点击首页
            commonProc().clickByXpath(driver,"//android.widget.LinearLayout[@resource-id='cc.wulian.smarthomev6:id/bottom_navigation_bar_item_container']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]")
        elif num==20:#往下滑动   
            commonProc().swipeDown(driver)
        elif num==21:#点击全部场景 
            commonProc().clickByXpath(driver, "//android.support.v7.widget.RecyclerView[@resource-id='cc.wulian.smarthomev6:id/home_scene_recyclerview']/android.widget.LinearLayout[8]")   
        elif num==22:#点击添加
            commonProc().clickById(driver, "cc.wulian.smarthomev6:id/all_scene_image_add")
            sleep(2)
        elif num==23:#增加场景，输入点击
            commonProc().switch_h5(driver)
#             commonProc().enterTextByXpath(driver,"//*[@id='customScene_input_name']","测试"+random.randint(1,100))
            driver.find_element_by_xpath("//*[@id='customScene_input_name']").send_keys(random.randint(1,10000))
            commonProc().clickByXpath(driver, "/html/body/section[2]/a[1]")
            commonProc().clickByXpath(driver, "//*[@id='customScene_sure']")
    
    
    
    #1、登录成功
    def loginSuccess(self,driver):
        lm.userName="15951644332"
#         print l.userName
        lm.password="123456abcd"
        lm.msg="登录失败！"
        self.baseProc(driver, [0,1,2,3,4,5,6,7])
    
#     2、 账号为空   
    def noneUser(self,driver): 
        lm.userName=""
        lm.password="123456abcd"
        lm.msg="登录按钮未禁用！"
        self.baseProc(driver, [0,1,2,3,4,5,8])
    
#     3、密码为空   
    def nonePass(self,driver):
        lm.userName="15951644332"
        lm.password=""
        lm.msg="登录按钮未禁用！"
        self.baseProc(driver, [0,1,2,3,4,5,8])
        
#      4、错误的账号（手机号）登录
    def wrongUser(self,driver): 
        lm.userName="159516443"
        lm.password="123456abcd"
        lm.msg="账号或密码不正确" 
        self.baseProc(driver, [0,1,2,3,4,5,6,9])
    
    #  5、错误的密码登录
    def wrongPass(self,driver):
        lm.userName="15951644332"
        lm.password="123456a"
        lm.msg="用户密码错误" 
        self.baseProc(driver, [0,1,2,3,4,5,6,9])
    
    #  6、手机号登录，连续3次输错密码，不找回密码            
    def InputAsCancel(self,driver):
        lm.userName="15951644332"
        lm.password="123"
        lm.buttonTxt="cc.wulian.smarthomev6:id/dialog_btn_negative"
        self.baseProc(driver, [0,1,2,3,4,5,10,11])
    
    #    7、手机号登录，连续3次输错密码，找回密码
    def InputAsSure(self,driver):
        lm.userName="15951644332"
        lm.password="123"
        lm.buttonTxt="cc.wulian.smarthomev6:id/dialog_btn_positive"
        lm.msg="未进入忘记密码页面"
        self.baseProc(driver, [0,1,2,3,4,5,10,11,12])
    
#       8、在H5页面点击
    def clickOnH5(self,driver):
        lm.deviceName="移动插座"
        lm.msg="进入设备详情页面失败！"
        self.baseProc(driver, [0,1,13,14,15,16,17,18])
    
    # 9、在H5页面输入
    def enterOnH5(self,driver):
        self.baseProc(driver, [0,1,13,19,20,21,22,23])

        
        
        
    
        
        
        
        
        
        
        
        
                       