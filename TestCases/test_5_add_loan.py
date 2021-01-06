#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/28 15:32
# @Author :春衫
# @File :test_5_add_loan.py
import allure
import pytest

import jmespath
from Base.BaseCase import BaseCase
from Base.GlobalEnvironment import GlobalEnvironment
from tools.do_excel import DoExcel
from tools.http_request import HttpRequest
from tools.project_path import test_data_path


@pytest.mark.run(order=5)
@allure.feature('添加项目接口')
class TestAddLoan(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_data_path, "addLoan")

    @allure.story("测试添加项目接口")
    @pytest.mark.parametrize("case_info", caseInfoList)
    def test_add_loan(self, case_info):
        with allure.step("对当前的case进行参数化替换"):
            # 对当前的case进行参数化替换
            case_info = self.params_replace_current_case_info(case_info)

        with allure.step("发起请求"):
            res=HttpRequest().http_request(case_info)

        # 断言
        with allure.step("响应结果断言"):
            self.assert_expected(case_info, res)

        memberId = jmespath.search("data.member_id", res.json())
        if memberId != None:
            loan_id = jmespath.search("data.id", res.json())
            # 2、保存到环境变量中
            GlobalEnvironment().put("loan_id", loan_id)
