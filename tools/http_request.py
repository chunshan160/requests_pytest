#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request2.py

import requests
from tools.UserLog import UserLog


class HttpRequest:

    def http_request(self, case_info):
        case_id = case_info['case_id']
        interface = case_info['interface']
        headers = case_info['request_header']
        method = case_info['method']
        body = case_info['input_params']
        url = "http://api.lemonban.com/futureloan" + case_info['url']
        try:
            if method.lower() == 'get':
                res = requests.get(url, json=body, headers=headers)
            elif method.lower() == 'post':
                res = requests.post(url, json=body, headers=headers)
            elif method.lower() == "patch":
                res = requests.patch(url, json=body, headers=headers)
            else:
                res = "请求方式不支持"
            UserLog().debug("请求头：" + str(res.request.headers), interface, case_id)
            UserLog().debug("请求正文：" + str(body), interface, case_id)
            UserLog().debug("响应头：" + str(res.headers), interface, case_id)
            UserLog().debug("响应正文：" + str(res.text), interface, case_id)
            return res
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e


if __name__ == '__main__':
    pass
