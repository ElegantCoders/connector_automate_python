import requests  # 这个是请求包
from conf import Gain_Token_Address  # 获取token的链接地址


# 调用这个类 的token_req 方法  获取到token
class GainToken(object):
    def __init__(self):
        self.url = Gain_Token_Address

    def token_req(self, every_list):
        try:
            if every_list[5] != '' and every_list[6] != '':  # 判断账号密码不能为空传进来的是个小列表
                headers = {
                    "Content-Type": "application/json"  # 设置登录接口的请求头
                }
                data = {  # 登录接口传参
                    "loginName": every_list[5],  # 账号
                    "pwd": every_list[6],  # 密码
                    "os": 1,
                    "idEntity": 1
                }
                res = requests.post(self.url, headers=headers, json=data)  # 发起请求
                # print(res.json()['body']['token'])
                return res.json()['body']['token']  # 获取响应结果里的token   并进行return
        except Exception as err:
            print(err)
