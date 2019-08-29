#coding=utf-8
'''
Created on 2018年6月15日
@author: Administrator
'''


class switch(object):
    
    def meth1(self):
      print "你好"  
      
    def meth2(self):
        print "我刚"
        
    def meth3(self):
        print "uu"
        
    def numbers_to_strings(self,argument):
        switcher = {
            0:"www",
            1:"aaa",
            2:"sss"
        }
        return switcher.get(argument)
#         return switcher.get(0)
    
    def swt(self,num):
        if num==0:
            self.meth1()
        elif num==1:
            self.meth2()
        elif num==2:
            self.meth3()
       
    def xun(self,list=[]):
        for i in list:
            self.swt(i)    
    
    

if __name__ == '__main__':
       a=switch()
       a.xun([2,1,0])