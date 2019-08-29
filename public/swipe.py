#coding=utf-8
'''
Created on 2017年3月22日

@author: 赵永健，滑动
'''
# from app.OpenApp import OpenApp


class swipe(object):
#     ina = OpenApp()
#     ina.open()
#     driver=ina.getDr()
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
            
    def swipeLeft(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.8)    #获取起始x坐标，根据实际调整相乘参数
        x2 = int(w_size[0] * 0.05)   #获取终点x坐标，根据实际调整相乘参数
        y1 = int(w_size[1] * 0.5)    #获取y坐标，根据实际调整相乘参数
        driver.swipe(x1,y1,x2,y1,200)
        
    def swipeRight(self,driver):
        w_size = self.getSize(driver)
        x1 = int(w_size[0] * 0.05)    #获取起始x坐标，根据实际调整相乘参数
        x2 = int(w_size[0] * 0.8)   #获取终点x坐标，根据实际调整相乘参数
        y1 = int(w_size[1] * 0.5)    #获取y坐标，根据实际调整相乘参数
        driver.swipe(x1,y1,x2,y1,200)
     
     