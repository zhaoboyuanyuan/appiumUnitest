#coding=utf-8
'''
Created on 2018年6月1日

@author: 赵永健，将图片中的字符提取出来
'''
import re
import pytesseract  
from PIL import Image  
  
im = Image.open(r'D:\screenShot\screenshot_20180601_171942.png')  
text=pytesseract.image_to_string(im,lang='chi_sim')
print(text) 
txt="用户".decode('utf-8')
ta=re.match(r'^'+txt+'.*',text)
print ta
if txt==None:
    print False
else: 
    print True

# def searchTxt(message,picturePath):
#     im = Image.open(rpicturePath)  
#     text=pytesseract.image_to_string(im,lang='chi_sim')
#     print(text) 
#     txt=message.decode('utf-8')
#     if txt in text:
#         return True
#     else: 
#         return False

#     


