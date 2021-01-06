#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 22:55
# @Author :春衫
# @File :project_path.py
import datetime
import os

"""专门来读取路径的值"""
# 当前目录的顶级路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例的路径
test_case_path = os.path.join(project_path, 'TestCases')

# 测试数据的路径
test_data_path = os.path.join(project_path, 'TestData', 'api_testcases_futureloan_v4.xlsx')

# 测试报告的路径
test_report_path = os.path.join(project_path, 'TestResult', 'html_report', 'test_api.html')

# 用例配置文件的路径
case_config_path = os.path.join(project_path, 'Conf', 'case_config.yaml')

# 数据库配置文件的路径
db_config_path = os.path.join(project_path, 'Conf', 'db_config.yaml')

##日志配置文件的路径
logs_config_path = os.path.join(project_path, "Conf", "logs_config.yaml")

# 日志输出文件的路径
log_path = os.path.join(project_path, 'TestResult', 'log')

# 上传图片文件地址
image_path = os.path.join(project_path, "Source", "picture.jpg")

# allure_report报告保存地址
allure_report = os.path.join(project_path, "TestResult", "Allure", "report")

# allure_result保存地址
allure_result = os.path.join(project_path, "TestResult", "Allure", "result")

js = os.path.join(project_path, "Source", "des2.js")

TestCases = os.path.join(project_path, "TestCases")
