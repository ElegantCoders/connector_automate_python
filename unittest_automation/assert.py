import unittest  # 测试框架
import conf  # conf配置文件
import datetime  # 这个是获取时间的包
import json
import csv  # 处理csv文件的包
from tools.open_excel import ConversionDictAndList  # 从open_excel文件中导入ConversionDictAndList类
from request_start.get_post_req import PostGetDeleteReq  # 从get_post_req文件中导入PostGetDeleteReq类


def error_write(error, assert_err, res_text):
    try:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间  进行格式化输出（转换为字符串形式）   赋值
        file = conf.Error_File_Path  # 文件路径   在conf文件中配置
        csv_list = [error, assert_err, res_text, time]  # 把传递进的参数添加进列表
        with open(file, 'a+', newline='', encoding='utf-8') as f:  # 打开文件  设置为向后追加模式   写入数据编码方式为中文utf-8
            w = csv.writer(f)  # 生成csv文件句柄   可以理解为转换成csv方式文件的操作
            w.writerow(csv_list)  # 把 csv_list 列表写入文件
    except Exception as err:
        print(err)


class Assert(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.daliebiao = ConversionDictAndList().list_and_dict()  # 得到Execl中的大列表  所有处理过的数据
        self.post_get_delete_req = PostGetDeleteReq()  # 实例化PostGetDeleteReq类

    '''
    post断言验证方法
    '''

    def test_post_token_par_urldict(self):  # 有token   有参数   url有{ }
        for every_list in self.daliebiao:  # 遍历大列表  得到所有小列表  每一个小列表代表一条数据
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} != every_list[2] and "{" in every_list[0]:  # 有参数  url有{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_token_par_urldict(every_list)  # 获取到请求返回的内容
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))

            except AssertionError as assert_err:  # 捕获断言异常
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)  # 写入error文件
                # print(assert_err)

    def test_post_token_par_urlnotdict(self):  # 有token   有参数   url无{ }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} != every_list[2] and "{" not in every_list[0]:  # 有参数  url无{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_token_par_urlnotdict(every_list)  # 获取到请求返回的内容
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))

            except AssertionError as assert_err:  # 捕获断言异常
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)  # 写入error文件
                # print(assert_err)

    def test_post_token__not_par_urldict(self):  # 有token   无参数    url有{ }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} == every_list[2] and "{" in every_list[0]:  # 无参数  url有{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_token__not_par_urldict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_post_token__not_par_urlnotdict(self):  # 有token   无参数    url无{ }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} == every_list[2] and "{" not in every_list[0]:  # 无参数  url无{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_token__not_par_urlnotdict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_post_not_token_header_par(self):  # 无token   有请求头   有参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
                        if {'': ''} != every_list[2]:  # 有参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_not_token_header_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_post_not_token_not_header_par(self):  # 无token   无请求头   有参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] == '':  # 请求头  无token  且请求头为空
                        if {'': ''} != every_list[2]:  # 有参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_not_token_not_header_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_post_not_token_header_not_par(self):  # 无token   有请求头   无参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "post":  # 得到所有  post请求  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
                        if {'': ''} == every_list[2]:  # 无参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.post_not_token_header_not_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    '''
    get断言验证方法
    '''

    def test_get_token_par_urldict(self):  # 有token   有参数   url有 { }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} != every_list[2] and "{" in every_list[0]:  # 有参数  url有{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_token_par_urldict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_token_par_urlnotdict(self):  # 有token   有参数   url无 { }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} != every_list[2] and "{" not in every_list[0]:  # 有参数  url无{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_token_par_urlnotdict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_token__not_par_urldict(self):  # 有token   无参数   url有 { }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} == every_list[2] and "{" in every_list[0]:  # 无参数  url有{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_token_not_par_urldict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_token__not_par_urlnotdict(self):  # 有token   无参数   url无 { }
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
                        if {'': ''} == every_list[2] and "{" not in every_list[0]:  # 无参数  url无{ }
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_token_not_par_urlnotdict(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_not_token_header_par(self):  # 无token   有请求头   有参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
                        if {'': ''} != every_list[2]:  # 有参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_not_token_header_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_not_token_not_header_par(self):  # 无token   无请求头   有参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get请求  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] == '':  # 请求头  无token  且请求头为空
                        if {'': ''} != every_list[2]:  # 有参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_not_token_not_header_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    def test_get_not_token_header_not_par(self):  # 无token   有请求头   无参数
        for every_list in self.daliebiao:
            try:
                # print(every_list)
                if every_list[1] == "get":  # 得到所有  get  列表
                    if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
                        if {'': ''} == every_list[2]:  # 无参数
                            # print(every_list)
                            self.res_text = self.post_get_delete_req.get_not_token_header_not_par(every_list)
                            dic_t = json.loads(self.res_text)  # 转换为python字典类型
                            code = dic_t['code']  # 通过键取值
                            self.assertEqual(every_list[3], str(code))
            except AssertionError as assert_err:
                error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
                error_write(error, assert_err, self.res_text)
                # print(assert_err)

    # '''
    # delete断言验证方法
    # '''
    #
    # def test_delete_token_par(self):  # 有token   有参数
    #     for every_list in self.daliebiao:
    #         try:
    #             # print(every_list)
    #             if every_list[1] == "delete":  # 得到所有  delete请求  列表
    #                 if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
    #                     if {'': ''} != every_list[2]:  # 有参数
    #                         # print(every_list)
    #                         self.res_text = self.post_get_delete_req.delete_token_par(every_list)
    #                         dic_t = json.loads(self.res_text)  # 转换为python字典类型
    #                         code = dic_t['code']  # 通过键取值
    #                         self.assertEqual(every_list[3], str(code))
    #         except AssertionError as assert_err:
    #             error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
    #             error_write(error, assert_err, self.res_text)
    #             print(assert_err)
    #
    # def test_delete_token__not_par(self):  # 有token   无参数
    #     for every_list in self.daliebiao:
    #         try:
    #             # print(every_list)
    #             if every_list[1] == "delete":  # 得到所有  delete请求  列表
    #                 if "X-AUTH-TOKEN" in every_list[4]:  # 请求头  有token
    #                     if {'': ''} == every_list[2]:  # 无参数
    #                         # print(every_list)
    #                         self.res_text = self.post_get_delete_req.delete_token_not_par(every_list)
    #                         dic_t = json.loads(self.res_text)  # 转换为python字典类型
    #                         code = dic_t['code']  # 通过键取值
    #                         self.assertEqual(every_list[3], str(code))
    #         except AssertionError as assert_err:
    #             error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
    #             error_write(error, assert_err, self.res_text)
    #             print(assert_err)
    #
    # def test_delete_not_token_header_par(self):  # 无token   有请求头   有参数
    #     for every_list in self.daliebiao:
    #         try:
    #             # print(every_list)
    #             if every_list[1] == "delete":  # 得到所有  delete请求  列表
    #                 if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
    #                     if {'': ''} != every_list[2]:  # 有参数
    #                         # print(every_list)
    #                         self.res_text = self.post_get_delete_req.delete_not_token_header_par(every_list)
    #                         dic_t = json.loads(self.res_text)  # 转换为python字典类型
    #                         code = dic_t['code']  # 通过键取值
    #                         self.assertEqual(every_list[3], str(code))
    #         except AssertionError as assert_err:
    #             error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
    #             error_write(error, assert_err, self.res_text)
    #             print(assert_err)
    #
    # def test_delete_not_token_not_header_par(self):  # 无token   无请求头   有参数
    #     for every_list in self.daliebiao:
    #         try:
    #             # print(every_list)
    #             if every_list[1] == "delete":  # 得到所有  delete请求  列表
    #                 if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] == '':  # 请求头  无token  且请求头为空
    #                     if {'': ''} != every_list[2]:  # 有参数
    #                         # print(every_list)
    #                         self.res_text = self.post_get_delete_req.delete_not_token_not_header_par(every_list)
    #                         dic_t = json.loads(self.res_text)  # 转换为python字典类型
    #                         code = dic_t['code']  # 通过键取值
    #                         self.assertEqual(every_list[3], str(code))
    #         except AssertionError as assert_err:
    #             error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
    #             error_write(error, assert_err, self.res_text)
    #             print(assert_err)
    #
    # def test_delete_not_token_header_not_par(self):  # 无token   有请求头   无参数
    #     for every_list in self.daliebiao:
    #         try:
    #             # print(every_list)
    #             if every_list[1] == "delete":  # 得到所有  delete请求  列表
    #                 if "X-AUTH-TOKEN" not in every_list[4] and every_list[4] != '':  # 请求头  无token  且请求头不为空
    #                     if {'': ''} == every_list[2]:  # 无参数
    #                         # print(every_list)
    #                         self.res_text = self.post_get_delete_req.delete_not_token_header_not_par(every_list)
    #                         dic_t = json.loads(self.res_text)  # 转换为python字典类型
    #                         code = dic_t['code']  # 通过键取值
    #                         self.assertEqual(every_list[3], str(code))
    #         except AssertionError as assert_err:
    #             error = "这个url有错误:" + every_list[0] + "   参数文件中code错误码：" + every_list[3]
    #             error_write(error, assert_err, self.res_text)
    #             print(assert_err)


if __name__ == '__main__':
    unittest.main()
