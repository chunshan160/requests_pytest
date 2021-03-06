#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py
import os

import pytest
import sys
import shutil

sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
from Base.project_path import log_path



@pytest.fixture(scope="session")
def del_file():
    """
    删除某一目录下的所有文件或文件夹
    """
    if os.path.exists(log_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        shutil.rmtree(log_path)

    # 代替parametrize的一种思路


# def getCaseDataFromExcel(sheet):
#     caseInfoList = DoExcel.getCaseDataFromExcel(test_data_path, sheet)
#     return caseInfoList
#
#
# @pytest.fixture(params=getCaseDataFromExcel("login"))
# def login_case_info(request):
#     case_info=request.param
#     # with allure.step("对当前的case进行参数化替换"):
#         # 对当前的case进行参数化替换
#     case_info = BaseCase().params_replace_current_case_info(case_info)
#     return case_info


if __name__ == '__main__':
    # params_replace_all_case_info()
    pass
