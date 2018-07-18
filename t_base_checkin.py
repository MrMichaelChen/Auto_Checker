# encoding:utf-8
"""this module is provide methods for teacher"""

import csv
import time
import os
from reminder import Reminder
from operate_file import OperateData

class BaseCheckin(OperateData):
    """some methods here
       operate files
       cure data
    """

    def __init__(self):
        pass

    # althrough TeacherWechatID  get teacherID
    def get_teacherid(self, teacher_wechatid):
        filename = 'InData/teacherInfo.csv'
        check_teacher = 0  # 对查询教师时的判断量
        teadata = self.read_file(filename)
        teacher_id = 0
        for readline in teadata:
            if readline["WeChatID"] == teacher_wechatid:
                teacher_id = readline["TeacherID"]
                check_teacher = 0
                break
            else:
                check_teacher = 1  # 没有查询到教师工号
        if check_teacher == 1:
            # print '无法在教师的信息表里查询到该教师的信息'
            return False
            # exit(0)
        return teacher_id

    def get_classlist(self, course_id):
        filename = 'InData/courseInfo.csv'
        teacher_class = []
        data = self.read_file(filename)
        for line in data:
            if line['CourseID'] == course_id and not line['ClassNums'] in teacher_class:
                teacher_class.append(line['ClassNums'])
            else:
                pass

        return teacher_class

    def get_courselist(self, teacher_id):
        filename = 'InData/courseInfo.csv'
        data = self.read_file(filename)
        course_list = []
        for line in data:
            if line['TeacherID'] == teacher_id:
                if not line['CourseID'] in course_list:
                    course_list.append(line['CourseID'])
            else:
                pass
        return course_list

    def get_detailname(self, teacher_id, course_id):
        seq_list = self.get_seqnumlist(course_id, teacher_id)
        seq_id = raw_input(Reminder.InputAlterSeqTime)
        while not seq_id in seq_list:
            seq_id = raw_input(Reminder.SystemInError)
            if seq_id == -1:
                return 0

        file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                    str(seq_id) + '_' + 'checkinDetail.csv'
        return file_name

    def get_seqnumlist(self, course_id, teacher_id):
        if course_id == -1:
            return 0

        with open('OutData/seq.csv', 'r') as filename:
            reader2 = csv.reader(filename)
            seq_list = []
            for line in reader2:
                if (line[0] == teacher_id) & (line[1] == course_id):
                    if not line[2] in seq_list:
                        seq_list.append(line[2])
                else:
                    pass
        print seq_list
        return seq_list

    def choose_num(self, course_list):
        """use this function to choose"""
        try:
            choose_num = int(raw_input(Reminder.ChooseCourseId))
            list = enumerate(course_list)
            for index, item in list:
                if index == choose_num:
                    return item
        except ValueError:
            print "所选择的值错误"
            self.choose_num(course_list)

    def teacher_choose_course(self, course_list):
        list = enumerate(course_list)
        for index, item in list:
            print index, ':', item
        course_id = 0
        count = 0
        item = self.choose_num(course_list)
        if item:
            course_id = item
            count = 1
        else:
            print "请重新输入"
        while count == 0:
            item = self.choose_num(course_list)
            if item:
                course_id = item
                count = 1
            else:
                print "输入错误，请重新输入"
        if count == 1:
            return course_id
        else:
            print "选择课程错误，即将返回"
            return

    def get_nowtime(self):
        """get now time in a right format"""
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
        stime0 = nowtime.split(" ")
        stime1 = stime0[1].split(':')
        stime = stime1[0] + stime1[1] + stime1[2]
        return stime

    def judge_sec(self, start_time):
        """if a teacher want to enter the list and the same class teacher is already existed
           judge the sec info to refuse one
        """
        if Reminder.FirstS < start_time < Reminder.FirstE:
            return 1
        if Reminder.SecondS < start_time < Reminder.SecondE:
            return 2
        if Reminder.ThirdS < start_time < Reminder.ThirdE:
            return 3
        if Reminder.ForthS < start_time < Reminder.ForthE:
            return 4
        if Reminder.EveS < start_time < Reminder.EveE:
            return 5

    def create_seq(self, teacher_id, course_id):
        """when a teacher enter the list successfully the system need to do this
           create a new seq recording
        """
        with open('OutData/seq.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(csvfile)
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
            seq_id = ''
            for line in reader:
                if line[0] == teacher_id:
                    seq_id = line[2]
                else:
                    pass
            if seq_id == '':
                seq_id = 1
            else:
                seq_id = str(int(seq_id) + 1)
            message_list = [teacher_id, course_id, seq_id, nowtime]
            writer.writerow(message_list)
            if seq_id:
                self.creat_detail(teacher_id, course_id, seq_id)

    def creat_detail(self, teacher_id, course_id, seq_id):
        """
        when a teacher enter the list successfully the system need to do this
        create a new detail file
        """
        file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                    str(seq_id) + '_' + 'checkinDetail.csv'
        stu = []
        message = {'StuID': None, 'checkTime': None, 'ProofPath': None, 'checkinType': None,
                   'IsSuss': None, 'checkinResult': None}
        stu.append(message)
        self.write_file(stu, file_name)

    # 此时将学生ID全部加入
    def creat_sum(self, teacher_id, course_id, seq_id):
        filename = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + "sum.csv"
        if os.path.exists(filename) != True:
            sumdata = []
            data1 = self.read_file('InData/courseInfo.csv')
            classlist = []
            for line in data1:
                if (line['TeacherID'] == teacher_id) & (line['CourseID'] == course_id):
                    classlist.append(line['ClassNums'])
            filename1 = 'InData/studentInfo.csv'
            data = self.read_file(filename1)
            for line1 in data:
                if line1['ClassID'] in classlist:
                    string = {'StuID': line1["StuID"]}
                    for num in range(1, seq_id + 1):
                        butter = 'checkin' + str(num)
                        checktime = {butter: None}
                        string.update(checktime)
                    sumdata.append(string)
            self.write_file(sumdata, filename)
        else:
            sumallinfo = []
            suminfo = self.read_file(filename)
            for line in suminfo:
                message = {'checkin' + str(seq_id + 1): None}
                line.update(message)
                sumallinfo.append(line)
            self.write_file(sumallinfo, filename)
        print "sum表初始化成功"

    def find_detailfile(self, course_id):
        filelist = []
        info = 'OutData/'
        listfile = os.listdir(info)
        for line in listfile:
            if str(course_id) in line:
                if 'checkinDetail' in line:
                    filelist.append(line)
        return filelist

    def find_sumfile(self, course_id):
        info = 'OutData/'
        listfile = os.listdir(info)
        count = 0
        for line in listfile:
            if str(course_id) in line:
                if 'sum' in line:
                    print line
                    count = 1
                    return line

        if count == 0:
            print Reminder.FindSumfileError
            return False

    def get_student_id(self, _stu_wechatid):
        stu_message_list = []  # 对由学生的微信号的到的学生信息列表初始化
        filename = 'InData/studentInfo.csv'
        data = self.read_file(filename)
        count = 0  # 设置一个查询学生时的控制变量
        for readline in data:
            if readline['WeChatID'] == _stu_wechatid:
                count = 1
                stu_id = readline['StuID']  # 记录学生的ID
                class_id = readline['ClassID']  # 将所在班级的ID记录
                stu_message_list = [stu_id, class_id]
            else:
                pass
        if count == 0:
            # print '没有该学生的记录！'
            # exit(0)
            return
        return stu_message_list[0]
