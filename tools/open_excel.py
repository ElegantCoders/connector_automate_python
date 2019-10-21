import xlrd  # 操作execl需要的包   要提前进行安装
import json  # 处理json和python类型转换所用的包
import conf  # 导入配置文件  配置路径在这个文件

#反倒是科技范德萨
class OpenExcel(object):
    def __init__(self):
        excel_file = conf.Excel_File_Path  # 得到execl文件的路径
        self.data = xlrd.open_workbook(excel_file)  # 读取到这个文件

    def open_sheet1(self):  # 操作Excel表
        sheet = self.data.sheet_by_name('Sheet1')  # 获取到名为 Sheet1 的表
        nrows = sheet.nrows  # 获取有效行数
        row_list = []  # 定义一个空列表
        for i in range(1, nrows):  # 遍历有效的行数  得到列表中每一行数据的对象
            row = sheet.row_values(i)  # 得到列表中的每一行数据
            row_list.append(row)  # 把得到的数据添加进已经定义的row_list中
        return row_list  # 把这个大列表进行返回

    def transform_dict(self):  # 修改参数和值为字典格式，return 大列表
        test_list = []  # 定义一个空列表
        for every_lists in self.open_sheet1():  # 调用open_sheet1方法  得到大列表  然后进行遍历得到小列表
            # print(every_lists)
            every_lists[4] = str(int(every_lists[4]))  # 通过列表索引取值的方式 获取到错误码  对错误码类型的进行转换  单精度转成整数（int）类型再转成字符串（str）类型

            if every_lists[5] != '':  # 请求头  不为空
                every_lists[5] = json.loads(every_lists[5])  # 转字典

            if every_lists[6] != '':  # 判断 账号不为空
                every_lists[6] = str(int(every_lists[6]))  # 然后获取到账号   对账号类型进行转换

            if not isinstance(every_lists[7], str):  # 判断 密码不是字符串（str）类型执行下边代码  这个判断是为了解决execl中密码为纯数字且有小数点的情况
                result_int = str(every_lists[7]).split('.')[
                    0]  # 把密码转换成字符串以小数点进行切割  得到一个列表  取这个列表中的索引为0的值（列表中第一个值）  也就是小数点前面的值
                result_flt = str(every_lists[7]).split('.')[1]  # 这个是小数点后边的值

                if float('0.' + result_flt) == 0:  # 拼接'0.'小数点后边的值  然后转成单精度（float）类型  跟0进行判等
                    every_lists[7] = result_int  # 条件成立后  把小数点前的值（result_int）赋给密码
                else:
                    every_lists[7] = str(every_lists[7])  # 不等于0时  把获取的密码类型直接转成字符串  然后赋值给密码

            for index, value in enumerate(every_lists):  # 遍历小列表，得到索引和值
                if index == 2:  # 索引为2时  以中文逗号切割返回的是一个列表
                    self.k = value.split('，')
                if index == 3:  # 索引为3时 同样返回的是列表
                    # print(every_lists)
                    self.v = value.split('，')

            dicts = dict(zip(self.k, self.v))  # 把两个列表中的值压缩成字典
            del every_lists[2:4]  # 删除小列表原位置字符串
            every_lists.insert(2, dicts)  # 根据索引把压缩好的字典添加进小列表的原位置
            test_list.append(every_lists)  # 把处理好的小列表添加进空列表（test_list）
        return test_list  # 进行返回


class ConversionDictAndList(object):
    def __init__(self):
        self.oetf = OpenExcel().transform_dict()  # 实例化OpenExcel类中的transform_dict方法  得到返回的结果（test_list这个大列表）

    def list_and_dict(self):
        for every_lists in self.oetf:  # 遍历这个大列表 得到小列表
            # print(every_lists)
            for key, value in every_lists[2].items():  # 调用items方法  获取到这个字典的键和值    every_lists[2]这个是字典
                if "[" in value and "]" in value:  # 如果字典的值中有 [ ]   这时value类型为字符串
                    conversion_list = json.loads(value)  # 把字符串转换为python列表类型
                    every_lists[2][key] = conversion_list  # 通过键进行对值进行赋值
                    # print(every_lists[2])
                if "{" in value and "}" in value:  # 这个同上边一样   有 { } 时   进行转换
                    conversion_list = json.loads(value)
                    every_lists[2][key] = conversion_list
            # print(every_lists)
        return self.oetf  # 把整个大列表返回

# print(ConversionDictAndList().list_and_dict())
