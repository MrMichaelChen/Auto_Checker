# -*- coding: utf-8 -*-
# 该模块为对导入文件进行相关的文件检查
import csv
import re


class BaseCheckMixin(object):

    def check_column_data(self, new_data, log_buffer):
        """列的格式检查
        :param new_data: 教师数据列表
        :param log_buffer: 错误日志
        :return: null
        """
        chk = BaseCheckMixin()
        for line in new_data:
            line_num = str(new_data.index(line) + 2)
            for column_name in self.validator_re:
                chk.column_format_check(line[column_name], self.validator_re[column_name], log_buffer, line_num)

    def column_format_check(self, column, re_str, log_buffer, line_num):
        if re.findall(re_str, column):
            pass
        else:
            log_buffer.update({column + ' wrong in line NO.' + line_num : ' Format Error'})

    def filename_check(self,filename):
        """check the file name whether is xx.csv file
        :param new_filename: file name
        :return: bool
        """
        print filename
        if re.findall('.+\.csv$', filename):
            return True
        else:
            return False

    # 外部文件与内部文件的查重,并更新内部文件
    def remove_repeat(self, new_data, old_data):
        keys = self.__class__.keys
        for old_line in old_data:
            flog = True
            for new_line in new_data:
                num = 0
                for key in keys:
                    if old_line[key] == new_line[key]:
                        num += 1
                if num == len(keys):
                    flog = False
                    break
            if flog:
                new_data.append(old_line)
            else:
                pass
        return new_data
        # return sorted(new_data, key=lambda n: n[keys[0]])  # 按学号排序

    # 自身的查重
    def dup_key_check(self, new_data, log_buffer):
        """id重复检查
        :param new_data: 待检查的数据列表
        :param log_buffer: 错误日志
        :param subscript: id所处的位置
        :return: null
        """
        keys = self.__class__.keys
        all_id = []
        for line in new_data:
            all_id.append(line[keys[0]])

        for newline in new_data:
            times_of_repeat = all_id.count(newline[keys[0]])
            if times_of_repeat > 1:
                log_buffer.update({'Id ' + newline[keys[0]] +
                                   ' repeat ': 'The id repeat ' + str(times_of_repeat) + ' times'})
            else:
                pass

        return

if __name__ == '__main__':
    data1 = [
        {'TeacherID': '2004344', 'TeacherName': '韩', 'WeChatID': 'wonka80'},
        {'TeacherID': '2004345', 'TeacherName': '志', 'WeChatID': 'wonka80'}
    ]

    data2 = [
        {'TeacherID': '2004344', 'TeacherName': '韩', 'WeChatID': 'wonka80'},
        {'TeacherID': '2004345', 'TeacherName': '志', 'WeChatID': 'wonka80'}
    ]

    demo = BaseCheckMixin()
    wrong_buffer = {}
    print demo.remove_repeat(data1, data2)
    demo.id_format_check('1234567', wrong_buffer, '1')
    print wrong_buffer