# coding=utf-8

import re
# import sys
# sys.path.append("..")
from base_import import BaseImport
from importcsv.checker.course_check import CourseCheckMixin


class ImportCourseInfo(BaseImport, CourseCheckMixin):
    course_id_len = 8
    teacher_id_len=7
    columns = ['CourseID', 'CourseName', 'TeacherID', 'ClassNums']
    keys = ["CourseID", "TeacherID", "ClassNums"]

    def __init__(self):
        self.validator_re={"CourseID":'^[\d]{' + str(self.__class__.course_id_len) + '}$', \
                           "CourseName":'^[\x80-\xff]{6,18}$', \
                           "TeacherID":'^[\d]{' +str(self.__class__.teacher_id_len) + '}$', \
                           "ClassNums":'[\x80-\xff]+\d{4}$'\
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
            # 现行提取courseprogress文件所需要的数据
            progress_data=new_data
            # 拆分班级区间,取出所需列
            mid_data = self.split_table(new_data)
            # 去除完全重复的数据（在去除日期属性后会出现重复的情况）
            mid_data = self.course_repeat_dup(mid_data)
            # 去除与内部文件的重复数据
            end_data = self.remove_repeat(mid_data, original_data)
            # 逻辑检查  # 因为调用的相对路径变化，在本进程中测试时需要添加一层路径"../"
            student_data = self.read_file('InData/studentInfo.csv')
            teacher_data = self.read_file('InData/teacherInfo.csv')
            self.logic_check(student_data, teacher_data, end_data, wrong_log)

            if wrong_log:
                print '课程信息有误！\n' + str(wrong_log)
                return
            else:
                self.write_file(progress_data,_filename,'wb')
#                self.write_file(end_data, 'InData/courseInfo.csv', 'wb')
                print '课程信息**导入成功**'
        else:
            print 'filename error'



    # 拆分班级区间
    def split_table(self, course_data):
        new_data = []
        for line in course_data:
            major = line['ClassNums']
            info = major.split(',')
            for inf in info:
                class_info = re.findall(r'\d+', inf)
                class_interval = len(class_info)
                if class_interval == 0:
                    continue
                else:
                    begin = int(class_info[0])
                    end = int(class_info[-1])

                major_info = re.findall('[^-0-9]+', inf)
                class_name = major_info[0]

                for i in range(begin, end + 1):
                    # ['CourseID', 'CourseName', 'TeacherID', 'ClassNums']
                    dict_line ={}
                    dict_line['CourseID'] = line['CourseID']
                    dict_line['CourseName'] = line['CourseName']
                    dict_line['TeacherID'] = line['TeacherID']
                    dict_line['ClassNums'] = class_name + str(i)
                    new_data.append(dict_line)

        return new_data


if __name__ == '__main__':
    # # 待导入课程信息文件
    new_file = '../../external/courseProgress.csv'
    # # 目标文件
    orig_file = '../../InData/courseProgress.csv'
    # # 目标文件
    info_file ='../../InData/courseInfo.csv'
    # # 实例化
    CourseInfo = ImportCourseInfo()
    # # 调用方法
    CourseInfo.classfile_import(new_file, orig_file, 'InData/courseInfo.csv')
