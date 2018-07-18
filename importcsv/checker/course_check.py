# -*- coding: utf-8 -*-
# 该模块为对导入文件进行相关的文件检查
import csv
import re

from base_check import BaseCheckMixin

class CourseCheckMixin(BaseCheckMixin):
    # 自身去重
    def course_repeat_dup(self, teacher_data):
        new_data = []
        for line in teacher_data:
            if line in new_data:
                pass
            else:
                new_data.append(line)
        return new_data

    # 检查是否有无关人员
    def logic_check(self, stu_data, tec_data, course_data, log_buffer):
        all_course_stu_id = []
        all_course_tec_id = []
        for line in course_data:
            all_course_stu_id.append(line['ClassNums'])
            all_course_tec_id.append(line['TeacherID'])

        for line in stu_data:
            if line['ClassID'] in all_course_stu_id:
                pass
            else:
                log_buffer.update({'The ' + line['ClassID'] + ' error ': ' not in course'})

        for line in tec_data:
            if line['TeacherID'] in all_course_tec_id:
                pass
            else:
                log_buffer.update({'The ' + line['TeacherID'] + ' error ': ' not in course'})
        return

