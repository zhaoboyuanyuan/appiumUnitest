#coding=utf-8
'''
Created on 2017年3月24日
@author: 赵永健
'''
# 把test_case目录添加到path下，这里用相对路径
import sys


from HTMLTestRunner import HTMLTestRunner

from testcase import *

sys.path.append("\testcase")
import time
import unittest


# 1.添加测试套件
testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(loginTest.loginTest))
# testunit.addTest(unittest.makeSuite(cploginTest.cploginTest))


#获取当前时间，这样便于下面的使用。
now = time.strftime("%Y-%m-%d-%H_%M_%S")
# 定义测试报告存放路径，支持相对路径
filename = "D:\\workspace\\appiumUnitest\\result\\"+"result.html"
fp = open(filename,'wb')
# 定义测试报告
runner = HTMLTestRunner(stream = fp,title=u'智能家居测试报告',description=u'用例执行情况')
runner.run(testunit)
fp.close()
if fp.close()==None:
    print("测试完成")





