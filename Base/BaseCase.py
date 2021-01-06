#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/27 17:05
# @Author :春衫
# @File :BaseCase.py

import decimal
import random
import re
import jmespath

from Base.GlobalEnvironment import GlobalEnvironment
from tools.do_sql import DoMysql


class BaseCase:

    def params_replace_all_case_info(self, caseInfoList):
        """

        Parameters
        ----------
        caseInfoList：当前测试类中的所有测试用例数据

        Returns：参数化替换之后的用例数据
        -------

        """
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        for caseInfo in caseInfoList:
            # 如果数据是为空的，没有必要去进行参数化的处理
            if caseInfo['request_header'] != None:
                requestHeader = self.regex_replace(caseInfo['request_header'])
                caseInfo['request_header'] = eval(requestHeader)

            if caseInfo['url'] != None:
                url = self.regex_replace(caseInfo['url'])
                caseInfo['url'] = url

            if caseInfo['input_params'] != None:
                inputParams = self.regex_replace(caseInfo['input_params'])
                caseInfo['input_params'] = eval(inputParams)

            if caseInfo['expected'] != None:
                expected = self.regex_replace(caseInfo['expected'])
                caseInfo['expected'] = eval(expected)

            if caseInfo['check_SQL'] != None:
                expected = self.regex_replace(caseInfo['check_SQL'])
                caseInfo['check_SQL'] = eval(expected)

        return caseInfoList

    def params_replace_current_case_info(self, caseInfo):
        """

        Parameters
        ----------
        caseInfo：当前测试类中的某个用例

        Returns：参数化替换之后的用例数据
        -------

        """
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        # 如果数据是为空的，没有必要去进行参数化的处理
        if caseInfo['request_header'] != None:
            requestHeader = self.regex_replace(caseInfo['request_header'])
            caseInfo['request_header'] = eval(requestHeader)

        if caseInfo['url'] != None:
            url = self.regex_replace(caseInfo['url'])
            caseInfo['url'] = url

        if caseInfo['input_params'] != None:
            inputParams = self.regex_replace(caseInfo['input_params'])
            caseInfo['input_params'] = eval(inputParams)

        if caseInfo['expected'] != None:
            expected = self.regex_replace(caseInfo['expected'])
            caseInfo['expected'] = eval(expected)

        if caseInfo['check_SQL'] != None:
            expected = self.regex_replace(caseInfo['check_SQL'])
            caseInfo['check_SQL'] = eval(expected)

        return caseInfo

    def regex_replace(self, sourceStr):
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        while re.search('{{(.*?)}}', str(sourceStr)):
            key = re.search('{{(.*?)}}', str(sourceStr)).group(0)
            value = re.search('{{(.*?)}}', str(sourceStr)).group(1)
            new_value = str(GlobalEnvironment().get(value))
            sourceStr = str(sourceStr).replace(key, new_value)

        return sourceStr

    # def get_phone(self):
    #     #缺陷，会留出很多空白没有注册的手机号
    #     phonePrefix = [133, 134]
    #     choice_num = random.choice(phonePrefix)
    #     sql = f"SELECT mobile_phone FROM `futureloan`.`member` WHERE `mobile_phone` LIKE '{choice_num}%' ORDER BY `mobile_phone` DESC LIMIT 1;"
    #     res = DoMysql().do_mysql(sql)
    #     mobile_phone = eval(res[0][0])
    #     return mobile_phone

    def get_random_phone(self):
        # 随机生成一个手机号码
        # 定义手机的号段
        phone_prefix_list = ["133", "137", "189"]
        while True:
            phone_prefix = random.choice(phone_prefix_list)
            choice_num = str(random.randint(0, 99999999)).zfill(8)
            phone = phone_prefix + choice_num
            sql = f"select count(*) from member where mobile_phone={phone};"
            res = DoMysql("tuple").query_one(sql)
            if res[0] == 0:
                return eval(phone)

    def assert_expected(self, caseInfo, res):
        # 用例公共的断言方法，断言期望值和实际值
        expected = caseInfo['expected']
        for i in expected.keys():
            result = jmespath.search(i, res.json())
            assert expected[i] == result, "期望值断言失败:{}".format(i)

    def assert_SQL(self, caseInfo):
        check_SQL_data = caseInfo['check_SQL']
        if check_SQL_data != None:
            for sql in check_SQL_data.keys():
                actual = DoMysql("tuple").query_one_value(sql)

                if isinstance(actual, decimal.Decimal):
                    expected = decimal.Decimal(str(check_SQL_data[sql]))
                else:
                    expected = check_SQL_data[sql]
                assert expected == actual, "数据库断言失败:{}".format(sql)


if __name__ == '__main__':
    a = {'caseId': 1, 'interface': 'login', 'title': '正常登录-管理员',
         'requestHeader': '{"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}', 'method': 'POST',
         'url': '/member/login', 'inputParams': '{\n  "mobile_phone": "{{mobile_phone1}}",\n  "pwd": "{{pwd1}}"\n}',
         'expected': '{\n    "code": 0,\n    "msg": "OK",\n    "data.mobile_phone": "{{mobile_phone1}}"\n}',
         'checkSQL': None, 'sheet_name': 'login'}
    res = BaseCase().params_replace_current_case_info(a)
    print(res)
