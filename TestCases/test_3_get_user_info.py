#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/23 11:20
# @Author :春衫
# @File :test_3_get_user_info.py

import pytest
import allure

from Base.BaseCase import BaseCase
from tools.do_excel import DoExcel
from tools.http_request import HttpRequest
from tools.project_path import test_case_path


@pytest.mark.run(order=3)
@allure.feature('获取用户信息接口')
class TestGetUserInfo(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "getUserInfo")

    @allure.story("测试获取用户信息接口")
    @pytest.mark.parametrize("case_info", caseInfoList)
    def test_get_user_info(self, case_info):
        with allure.step("对当前的case进行参数化替换"):
            # 对当前的case进行参数化替换
            case_info = self.params_replace_current_case_info(case_info)

        with allure.step("发起请求"):
            res=HttpRequest().http_request(case_info)

        # 断言
        with allure.step("响应结果断言"):
            self.assert_expected(case_info, res)
