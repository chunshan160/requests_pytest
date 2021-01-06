#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:15
# @Author :春衫
# @File :test_2_login.py

import pytest
import jmespath
import allure

from tools.do_excel import DoExcel
from tools.http_request import HttpRequest
from tools.project_path import test_data_path
from Base.BaseCase import BaseCase
from Base.GlobalEnvironment import GlobalEnvironment

@pytest.mark.run(order=2)
@allure.feature('登录接口')
class TestLogin(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_data_path, "login")

    @allure.story("测试登录接口")
    @pytest.mark.parametrize("case_info", caseInfoList)
    def test_login(self, case_info):
        with allure.step("对当前的case进行参数化替换"):
            # 对当前的case进行参数化替换
            case_info = self.params_replace_current_case_info(case_info)

        with allure.step("发起请求"):
            res=HttpRequest().http_request(case_info)

        # 断言
        with allure.step("响应结果断言"):
            self.assert_expected(case_info, res)

        member_id = jmespath.search("data.id", res.json())
        if member_id != None:
            with allure.step("保存token到环境变量里"):
                token = jmespath.search("data.token_info.token", res.json())
                if case_info["case_id"] == 1:
                    # 2、保存到环境变量中
                    GlobalEnvironment().put("token1", token)

                elif case_info["case_id"] == 2:
                    # 2、保存到环境变量中
                    GlobalEnvironment().put("token2", token)

                elif case_info["case_id"] == 3:
                    # 2、保存到环境变量中
                    GlobalEnvironment().put("token3", token)



if __name__ == '__main__':
    pytest.main()
