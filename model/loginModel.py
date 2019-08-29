#coding=utf-8
'''
Created on 2018年6月15日
@author: 赵永健，model类，get，set自定义数据
'''

class loginModel(object):
    
    @property
    def userName(self):
        return self._userName
    
    @userName.setter
    def userName(self,userName):  
        self._userName=userName 
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):  
        self._password=password   
    
    @property
    def msg(self):
        return self._msg
    
    @msg.setter
    def msg(self,msg):  
        self._msg=msg  
        
    @property    
    def buttonTxt(self):  
        return self._buttonTxt  
    
    @buttonTxt.setter    
    def buttonTxt(self,buttonTxt):  
        self._buttonTxt=buttonTxt  
        
    @property   
    def deviceName(self): 
        return self._deviceName
    
    @deviceName.setter  
    def deviceName(self,deviceName):  
        self._deviceName=deviceName





          
# if __name__ == '__main__':
#     l=loginModel()
#     l.userName="123"
#     print loginModel()._userName