#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/4/13 16:33
#@Author :春衫
#@File :get_data.py

from tools import project_path
import pandas as pd

class GetData:
    Cookie = None#存储cookie  初始值为None
    loan_id = None
    #iloc 替换ix   第一行不算 从第二行开始 第一格为[0,0]
    NoRegTel=int(pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[0,0])

    normal_tel=int(pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[1,0])
    admin_tel=int(pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[2,0])
    loan_member_id = int(pd.read_excel(project_path.test_case_path, sheet_name='init').iloc[3, 0])
    memberId=int(pd.read_excel(project_path.test_case_path, sheet_name='init').iloc[4, 0])


if __name__ == '__main__':
    print(getattr(GetData,'NoRegTel'))
    # setattr(GetCookie, 'Cookie', "小黄")  # 可以直接把类里面的属性值做修改
    # print(hasattr(GetCookie, "Cookie"))  # 判断是否有这个属性值  布尔值  has
    # print(getattr(GetCookie, "Cookie"))  # attribute 属性  获取这个值  get
    # delattr(GetCookie, "Cookie")  # 删除这个属性值  del
    # print(hasattr(GetCookie, "Cookie"))  # 判断是否有属性值