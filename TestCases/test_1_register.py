#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:46
# @Author :春衫
# @File :test_1_register.py

import allure
import pytest
import jmespath

from Base.RelyData import RelyData
from Base.BaseCase import BaseCase
from tools.do_excel import DoExcel
from Base.project_path import test_data_path
from tools.http_request import HttpRequest

@pytest.mark.run(order=1)
@allure.feature('注册接口')
class TestRegister(BaseCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_data_path, "register")

    @allure.story("注册新账号")
    @pytest.mark.parametrize("caseInfo", caseInfoList)  # 替代ddt
    def test_register(self, caseInfo):
        with allure.step("读数据库获取没有注册过的手机号码"):
            # 读数据库获取没有注册过的手机号码
            if caseInfo["case_id"] == 1:
                mobile_phone = self.get_random_phone()
                setattr(RelyData, "mobile_phone1", mobile_phone)
            elif caseInfo["case_id"] == 2:
                mobile_phone = self.get_random_phone()
                setattr(RelyData, "mobile_phone2", mobile_phone)
            elif caseInfo["case_id"] == 3:
                mobile_phone = self.get_random_phone()
                setattr(RelyData, "mobile_phone3", mobile_phone)

        with allure.step("对当前的case进行参数化替换"):
            # 对当前的case进行参数化替换
            case_info = self.params_replace_current_case_info(caseInfo)

        with allure.step("发起请求"):
            res=HttpRequest().http_request(case_info)

        with allure.step("响应结果断言"):
            # 1、响应结果断言
            self.assert_expected(case_info, res)
        with allure.step("数据库断言"):
            # 2、数据库断言
            self.assert_SQL(case_info)

        memberId = jmespath.search("data.id", res.json())
        if memberId != None:
            with allure.step("保存手机号、用户id、密码到环境变量里"):
                mobile_phone = jmespath.search("data.mobile_phone", res.json())
                # 3、注册成功的密码--从用例数据里面
                pwd = case_info['input_params']['pwd']
                if case_info["case_id"] == 1:
                    setattr(RelyData, "mobile_phone1", mobile_phone)
                    setattr(RelyData, "member_id1", memberId)
                    setattr(RelyData, "pwd1", pwd)

                elif case_info["case_id"] == 2:
                    # 2、保存到环境变量中
                    setattr(RelyData, "mobile_phone2", mobile_phone)
                    setattr(RelyData, "member_id2", memberId)
                    setattr(RelyData, "pwd2", pwd)

                elif case_info["case_id"] == 3:
                    # 2、保存到环境变量中
                    setattr(RelyData, "mobile_phone3", mobile_phone)
                    setattr(RelyData, "member_id3", memberId)
                    setattr(RelyData, "pwd3", pwd)



if __name__ == '__main__':
    pytest.main(["-s"])
