#coding=utf-8
'''
Created on 2018年6月11日

@author: 赵永健 ，登录测试
'''
import unittest
from app.OpenApp import OpenApp
from process.loginProc import loginProc
from process.CploginProc import CploginProc

login=CploginProc()
class loginTest(unittest.TestCase):
    
    def setUp(self):
        self.ina=OpenApp()
        self.ina.open()
        self.driver=self.ina.getDr()
        self.verificationErrors = [] # 错误信息打印到这个列表
        self.accept_next_alert = True # 是否继续接受下个警告
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        
    #1、登录成功
    def testLoginSuccess(self):
        u"""登录测试用例"""
#         loginProc().loginSuccess(self.driver)
        login.loginSuccess(self.driver)
# #
    #     2、 账号为空
    def testNoneuser(self):
        login.noneUser(self.driver)

    #     3、密码为空
    def testNonePass(self):
        login.nonePass(self.driver)

#     #      4、错误的账号（手机号）登录
#     def testWrongUser(self):
#         login.wrongUser(self.driver)
#
#     #  5、错误的密码登录
#     def testWrongPass(self):
#         login.wrongPass(self.driver)
#
# #      6、手机号登录，连续3次输错密码，不找回密码
#     def testInputAsCancel(self):
#         login.InputAsCancel(self.driver)
# #         loginProc().InputAsCancel(self.driver)
# #
#     #  7、手机号登录，连续3次输错密码，找回密码
#     def testInputAsSure(self):
#         login.InputAsSure(self.driver)
# #
# #    8、在H5页面点击
#     def testclickOnH5(self):
#         login.clickOnH5(self.driver)
#
# # 9、在H5页面输入
#     def testEnterOnH5(self):
#         login.enterOnH5(self.driver)


if __name__ == "__main__":
    unittest.main()