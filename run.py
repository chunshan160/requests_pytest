#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:59
# @Author :春衫
# @File :run.py
import os
import pytest

from Base.project_path import allure_report, allure_result
pytest.main(
    ["-v", "-s", "--alluredir", allure_result, "--clean-alluredir"])

# 生成测试报告
os.system(f"allure generate {allure_result} -o {allure_report} --clean")
#pytest -v -s --alluredir D:\Pycharm_workspace\Hobay\Requests_Pytest\TestResult\Allure\results --clean-alluredir
#allure generate D:\Pycharm_workspace\Hobay\Requests_Pytest\TestResult\Allure\results -o D:\Pycharm_workspace\Hobay\Requests_Pytest\TestResult\Allure\html --clean
