# coding=utf-8
from importcsv.fileimport.import_student import ImportStudentInfo
from importcsv.fileimport.import_teacher import ImportTeacherInfo
from importcsv.fileimport.import_course import ImportCourseInfo


class ImportCsvData(object):  # 导入文件信息
    '''this class is to start import data'''

    def __init__(self):
        self.teacher_info = ImportTeacherInfo()
        self.course_info = ImportCourseInfo()
        self.student_info = ImportStudentInfo()

    def start_import_data(self):
        '''this function is starting to import data'''
        # 待导入教师信息文件
        new_file = 'external/teacherInfo.csv'
        # 目标文件
        orig_file = 'InData/teacherInfo.csv'
        # 调用方法
        self.teacher_info.file_import(new_file, orig_file)

        # 待导入学生信息文件
        new_file = 'external/studentInfo.csv'
        # # 目标文件
        orig_file = 'InData/studentInfo.csv'
        # 调用方法
        self.student_info.file_import(new_file, orig_file)

        # # 待导入课程信息文件
        new_file = 'external/courseProgress.csv'
        # # 目标文件
        orig_file = 'InData/courseProgress.csv'
        # 调用方法
        self.course_info.file_import(new_file, orig_file)
