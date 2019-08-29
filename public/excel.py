#coding=utf-8
'''
Created on 2018年6月14日

@author: 赵永健   把excel中的数据读取为字典并使用，用于在Excel中保存控件库
'''
import xlrd
 
excel_path='D:\\code\\ControlLibrary.xlsx'
dict={}

# ID控件
def idCon(text):
    data=xlrd.open_workbook(excel_path)  
    table=data.sheets()[0]  
    rows=table.nrows  
    cols=table.ncols 
   
    for i in range(0,rows):  
        for j in range(cols):
            title = table.cell_value(i,0)  
            value = table.cell_value(i,1)  
            dict[title] = value   
    return  dict[text]    

# xpath控件            
def xpathCon(text):
    data=xlrd.open_workbook(excel_path)  
    table=data.sheets()[1]  
    rows=table.nrows  
    cols=table.ncols 
    for i in range(0,rows):  
        for j in range(cols):
            title = table.cell_value(i,0)  
            value = table.cell_value(i,1)  
            dict[title] = value   
    return  dict[text]    

# activity信息           
def activityCon(text):      
    data=xlrd.open_workbook(excel_path)  
    table=data.sheets()[2]  
    rows=table.nrows  
    cols=table.ncols 
    for i in range(0,rows):  
        for j in range(cols):
            title = table.cell_value(i,0)  
            value = table.cell_value(i,1)  
            dict[title] = value   
    return  dict[text] 
        
            
        

        
    

    
    