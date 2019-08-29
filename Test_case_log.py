#coding=utf-8
'''
Created on 2017年3月23日
@author: Administrator
'''
#-*coding=utf-8*-
import os
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
caselist = os.listdir('D:\\workspace\\appiumUnitest\\testcase')
for a in caselist:
    s = a[-2:] #选取后缀名为 py 的文件
    if s =='py':         #此处执行 dos 命令并将结果保存到 log.tx
        os.system('python D:\\workspace\\appiumUnitest\\testcase\\%s 1>>log.txt 2>&1'%a)
        print("测试完成")