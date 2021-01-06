#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/28 13:29
# @Author :春衫
# @File :test_4_recharge.py

import pytest
import requests
import allure

from Base.BaseCase import BaseCase
from tools.do_excel import DoExcel
from tools.http_request import HttpRequest
from tools.project_path import test_case_path


@pytest.mark.run(order=4)
@allure.feature('充值接口')
class TestRecharge(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "recharge")

    @allure.story("测试充值接口")
    @pytest.mark.parametrize("case_info", caseInfoList)
    def test_recharge(self, case_info):
        with allure.step("对当前的case进行参数化替换"):
            # 对当前的case进行参数化替换
            case_info = self.params_replace_current_case_info(case_info)

        with allure.step("发起请求"):
            res=HttpRequest().http_request(case_info)

        # 断言
        with allure.step("响应结果断言"):
            self.assert_expected(case_info, res)
        with allure.step("数据库断言"):
            self.assert_SQL(case_info)
