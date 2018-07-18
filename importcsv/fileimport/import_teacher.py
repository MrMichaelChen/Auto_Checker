# coding=utf-8

from base_import import BaseImport
from importcsv.checker.base_check import BaseCheckMixin


class ImportTeacherInfo(BaseImport, BaseCheckMixin):
    id_len = 7
    columns = ["TeacherID", "TeacherName", "WeChatID"]
    keys = ["TeacherID"]

    def __init__(self):
        self.validator_re={"TeacherID":'^[\d]{' + str(self.__class__.id_len) + '}$', \
                           "TeacherName":r'^[\x80-\xff]{6,18}$', \
                           "WeChatID":'^[a-zA-Z0-9_]+$'
                           }

    def file_import(self, file_name, _filename):
        # 检查列的个数和列名以及数据的完整性
        if self.filename_check(file_name) and self.filename_check(_filename):
            # 获取数据 改为字典存储后不能整存整取数据
            original_data = self.read_file(_filename)
            new_data = self.read_file(file_name)
            # 检查列的个数和列名以及数据的完整性
            wrong_log = {}
            self.check_column_data(new_data, wrong_log)
            # 去除与内部文件的重复数据
            mid_data = self.remove_repeat(new_data, original_data)
            # 检查内部的重复数据
            self.dup_key_check(mid_data, wrong_log)
            if wrong_log:
                print '教师信息有误！' + str(wrong_log)
                return
            else:
                 self.write_file(mid_data, _filename)
                 print '教师信息**导入成功**'
        else:
            print 'filename error'



if __name__ == '__main__':

    # 待导入教师信息文件
    new_file = '../../external/teacherInfo.csv'
    # 目标文件
    orig_file = '../../InData/teacherInfo.csv'
    # 实例化
    teacherInfo = ImportTeacherInfo()
    # 调用方法
    teacherInfo.file_import(new_file, orig_file)