#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2021/1/4 14:37
# @Author :春衫
# @File :test_7_invest.py

import allure
import pytest
from Base.BaseCase import BaseCase
from tools.do_excel import DoExcel
from tools.http_request import HttpRequest
from tools.project_path import test_data_path


@pytest.mark.run(order=7)
@allure.feature('投资接口')
class TestInvest(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_data_path, "invest")

    @allure.story("测试投资接口")
    @pytest.mark.parametrize("case_info", caseInfoList)
    def test_invest(self, case_info):
        with allure.step("对当前的case进行参数化替换"):
            case_info = self.params_replace_current_case_info(case_info)

        with allure.step("发起请求"):
            res = HttpRequest().http_request(case_info)

        # 断言
        with allure.step("响应结果断言"):
            self.assert_expected(case_info, res)
