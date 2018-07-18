# coding=utf-8

# import sys
# sys.path.append("..")
from base_import import BaseImport
from importcsv.checker.base_check import BaseCheckMixin

class ImportStudentInfo(BaseImport, BaseCheckMixin):
    id_len = 12
    columns = ['StuID', 'StuName', 'ClassID', 'WeChatID','FeaturePath']
    keys = ['StuID']

    def __init__(self):
        self.validator_re={"StuID":'^[\d]{' + str(self.__class__.id_len) + '}$', \
                           "StuName":'^[\x80-\xff]{6,18}$', \
                           "WeChatID":'^[a-zA-Z0-9_]+$', \
                           "ClassID":'[\x80-\xff]+\d{4}$'\
                           }

    def file_import(self, file_name, _filename):
        # 检查列的个数和列名以及数据的完整性
        if self.filename_check(file_name) and self.filename_check(_filename):
            # 获取数据
            original_data = self.read_file(_filename)
            new_data = self.read_file(file_name)
            # 检查列的个数和列名以及数据的完整性
            wrong_log = {}
            self.check_column_data(new_data, wrong_log)
            # 添加学生信息路径
            self.add_list(new_data)
            # 去除与内部文件的重复数据
            mid_data = self.remove_repeat(new_data, original_data)

            # 检查内部的重复数据
            self.dup_key_check(mid_data, wrong_log)
            if wrong_log:
                print '学生信息有误！' + str(wrong_log)
                return
            else:
                self.write_file(mid_data, _filename, 'wb')
                print '学生信息**导入成功**'

        else:
            print 'filename error'

    def add_list(self, student_data):
        for line in student_data:
            way = 'D:\Feature\\' + line['WeChatID'] + '_face.bin(jpg)'
            line['FeaturePath'] = way
        return True

    def Get_Student_data(self,filename):
        if self.filename_check(filename):
            # 获取数据 改为字典存储后不能整存整取数据
            data = self.read_file(filename)

        return data



if __name__ == '__main__':
    # 待导入学生信息文件
    new_file = '../../external/studentInfo.csv'
    # # 目标文件
    orig_file = '../../InData/studentInfo.csv'
    # # 实例化
    studentInfo = ImportStudentInfo()
    #
    studentInfo.file_import(new_file, orig_file)