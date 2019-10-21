import requests
from tools.login_token import GainToken  # 从login_token文件中导入GainToken类
from conf import Start_Request_Address


def del_dict(val):  # 替换{ }  为空
    return val.replace('{', '').replace('}', '')


class PostGetDeleteReq(object):
    def __init__(self):
        self.url = Start_Request_Address
        self.gaintoken = GainToken()  # 实例化GainToken类

    def post_token_par_urldict(self, post_list, *args, **kwargs):  # 有token   有参数   url有{ }
        try:
            post_list[0] = del_dict(post_list[0])  # 删除url中 { }   函数中用到的是替换方法 replace
            print(post_list)
            post_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(post_list)  # 调用token_req方法得到token  进行赋值
            res = requests.post(  # 发起post请求
                self.url + post_list[0],  # 拼接url
                json=post_list[2],  # 请求参数
                headers=post_list[4]  # 请求头
            )
            print(res.text)  # 输出到  Terminal（终端控制台）
            return res.text  # 返回响应的文本内容
        except Exception as err:  # 捕捉代码报错
            print(err)

    def post_token_par_urlnotdict(self, post_list, *args, **kwargs):  # 有token   有参数   url无{ }
        try:
            print(post_list)
            post_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(post_list)  # 调用token_req方法得到token  进行赋值
            res = requests.post(self.url + post_list[0], json=post_list[2], headers=post_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def post_token__not_par_urldict(self, post_list, *args, **kwargs):  # 有token   无参数  url有{ }
        try:
            post_list[0] = del_dict(post_list[0])
            print(post_list)
            post_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(post_list)
            res = requests.post(self.url + post_list[0], headers=post_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def post_token__not_par_urlnotdict(self, post_list, *args, **kwargs):  # 有token   无参数  url无{ }
        try:
            print(post_list)
            post_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(post_list)
            res = requests.post(self.url + post_list[0], headers=post_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def post_not_token_header_par(self, post_list, *args, **kwargs):  # 无token   有请求头   有参数
        try:
            print(post_list)
            res = requests.post(self.url + post_list[0], json=post_list[2], headers=post_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def post_not_token_not_header_par(self, post_list, *args, **kwargs):  # 无token   无请求头   有参数
        try:
            print(post_list)
            res = requests.post(self.url + post_list[0], json=post_list[2])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def post_not_token_header_not_par(self, post_list, *args, **kwargs):  # 无token   有请求头   无参数
        try:
            print(post_list)
            res = requests.post(self.url + post_list[0], headers=post_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_token_par_urldict(self, get_list, *args, **kwargs):  # 有token   有参数  url有 { }
        try:
            get_list[0] = del_dict(get_list[0])  # 删除url中 { }  ----》函数中用到的是替换方法 replace
            print(get_list)
            get_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(get_list)
            res = requests.get(self.url + get_list[0], params=get_list[2], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_token_par_urlnotdict(self, get_list, *args, **kwargs):  # 有token   有参数  url无 { }
        try:
            print(get_list)
            get_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(get_list)
            res = requests.get(self.url + get_list[0], params=get_list[2], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_token_not_par_urldict(self, get_list, *args, **kwargs):  # 有token   无参数  url有 { }
        try:
            get_list[0] = del_dict(get_list[0])  # 删除url中 { }  ----》函数中用到的是替换方法 replace
            print(get_list)
            get_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(get_list)
            res = requests.get(self.url + get_list[0], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_token_not_par_urlnotdict(self, get_list, *args, **kwargs):  # 有token   无参数  url有 { }
        try:
            print(get_list)
            get_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(get_list)
            res = requests.get(self.url + get_list[0], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_not_token_header_par(self, get_list, *args, **kwargs):  # 无token   有请求头   有参数
        try:
            print(get_list)
            res = requests.get(self.url + get_list[0], params=get_list[2], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_not_token_not_header_par(self, get_list, *args, **kwargs):  # 无token   无请求头   有参数
        try:
            print(get_list)
            res = requests.get(self.url + get_list[0], params=get_list[2])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    def get_not_token_header_not_par(self, get_list, *args, **kwargs):  # 无token   有请求头   无参数
        try:
            print(get_list)
            res = requests.get(self.url + get_list[0], headers=get_list[4])
            print(res.text)
            return res.text
        except Exception as err:
            print(err)

    # def delete_token_par(self, delete_list, *args, **kwargs):  # 有token   有参数
    #     try:
    #         print(delete_list)
    #         delete_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(delete_list)
    #         res = requests.delete(self.url + delete_list[0], params=delete_list[2], headers=delete_list[4])
    #         print(res.text)
    #         return res.text
    #     except Exception as err:
    #         print(err)
    #
    # def delete_token_not_par(self, delete_list, *args, **kwargs):  # 有token   无参数
    #     try:
    #         print(delete_list)
    #         delete_list[4]['X-AUTH-TOKEN'] = self.gaintoken.token_req(delete_list)
    #         res = requests.delete(self.url + delete_list[0], headers=delete_list[4])
    #         print(res.text)
    #         return res.text
    #     except Exception as err:
    #         print(err)
    #
    # def delete_not_token_header_par(self, delete_list, *args, **kwargs):  # 无token   有请求头   有参数
    #     try:
    #         print(delete_list)
    #         res = requests.delete(self.url + delete_list[0], params=delete_list[2], headers=delete_list[4])
    #         print(res.text)
    #         return res.text
    #     except Exception as err:
    #         print(err)
    #
    # def delete_not_token_not_header_par(self, delete_list, *args, **kwargs):  # 无token   无请求头   有参数
    #     try:
    #         print(delete_list)
    #         res = requests.delete(self.url + delete_list[0], params=delete_list[2])
    #         print(res.text)
    #         return res.text
    #     except Exception as err:
    #         print(err)
    #
    # def delete_not_token_header_not_par(self, delete_list, *args, **kwargs):  # 无token   有请求头   无参数
    #     try:
    #         print(delete_list)
    #         res = requests.delete(self.url + delete_list[0], headers=delete_list[4])
    #         print(res.text)
    #         return res.text
    #     except Exception as err:
    #         print(err)
