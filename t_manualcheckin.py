# encoding=utf-8
"""this module is used to do manual check in by teacher"""
import time
from reminder import Reminder
from t_base_checkin import BaseCheckin
from manage_checkindata import ResultManager


class TeacherManualCheckIn(BaseCheckin):
    """some methods to do manual check"""

    # 对教师手工考勤类的初始化
    def __init__(self):
        self.manager = ResultManager()

    def choose_stu_num(self, course_list):
        """
        to choose check in student
        :param course_list:
        :return:
        """
        list = enumerate(course_list)
        for index, item in list:
            if index > 0:
                print index, ":", item['StuID']
        try:
            choose_num = int(raw_input("请选择希望修改学生的学号："))
            list = enumerate(course_list)
            for index, item in list:
                if index == choose_num:
                    return item
        except ValueError:
            print "所选择的值错误"
            self.choose_num(course_list)

    def check_result_choose(self):
        """
        to choose the check in result
        :return:
        """
        print "1.出勤  2.缺勤  3.迟到  4.早退  5.请假已确认"
        choose_num = int(raw_input("请选择希望修改学生的学号："))
        if choose_num == 1:
            return '出勤'
        elif choose_num == 2:
            return '缺勤'
        elif choose_num == 3:
            return '迟到'
        elif choose_num == 4:
            return '早退'
        elif choose_num == 5:
            return '请假已确认'

    # 教师进行手工考勤修改
    def manual_checkin_alter(self, teacher_id, course_list):
        """
        teacher can alter the result for student
        teacher can choose num to do this action
        """
        course_id = self.teacher_choose_course(course_list)
        file_name = self.get_detailname(teacher_id, course_id)
        data = self.read_file(file_name)
        stu_line = self.choose_stu_num(data)
        bufferdata = []
        for line in data:
            if line['StuID'] == stu_line['StuID']:
                line['checkinResult'] = self.check_result_choose()
                print Reminder.AlterSuccessfully
            else:
                pass
            bufferdata.append(line)
        self.write_file(bufferdata, file_name)
        self.manager.update_sum(teacher_id, course_id)

    # 教师进行手工考勤增加
    def manual_checkin_add(self, teacher_id, course_list):
        """
        add detail file data
        :param teacher_id:
        :param course_list:
        :return:
        """
        course_id = self.teacher_choose_course(course_list)
        filename = 'OutData/seq.csv'
        data = self.read_file(filename)
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
        seq_num = ''
        for line in data:
            if line['TeacherID'] == teacher_id:
                seq_num = line['SeqID']
            else:
                pass
        if seq_num == '':
            seq_num = 1
        else:
            seq_num = str(int(seq_num) + 1)
        message_list = [{'TeacherID': teacher_id, 'CourseID': course_id, 'SeqID': seq_num, \
                         'StartTime': nowtime}]
        if seq_num == 1:
            self.write_file(message_list, filename)
        else:
            self.write_file(message_list, filename, way='a+')
        if message_list:
            seq_num = int(seq_num)
            self.manual_checkin_add_detile(teacher_id, seq_num, course_id, nowtime)


    def manual_checkin_add_detile(self, teacher_id, seq_num, course_id, nowtime):
        """
        :param teacher_id:
        :param seq_num:
        :param course_id:
        :param nowtime:
        :return:
        """
        teacher_class = self.get_classlist(course_id)
        file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                    str(seq_num) + '_' + 'checkinDetail.csv'
        stufile = 'InData/studentInfo.csv'
        stu = []
        data = self.read_file(stufile)
        for line in data:  # 由教师ID和课程ID得到班级列表，将班级中的所有学生全部写入列表，默认出勤。
            if line['ClassID'] in teacher_class:
                message = {'StuID': line['StuID'], 'checkTime': nowtime, 'ProofPath': '无', \
                           'checkinType': 'man', 'IsSuss': 'True', 'checkinResult': '出勤'}
                stu.append(message)
        self.write_file(stu, file_name)

        print Reminder.AddSuccessfully
        self.creat_sum(teacher_id, course_id, seq_num)
        self.manager.update_sum(teacher_id, course_id)

    def cform(self, teacher_id, course_list):
        """
        :param teacher_id:
        :param course_list:
        :return:
        """
        print "****************欢迎进入手工考勤菜单***************"
        print "*******1.教师进行手工修改****2.教师进行手工增加******"
        print "*******0.退出****************"
        op_num = raw_input("请输入您想要的操作：")
        count = 0
        while count == 0:
            count = 1
            if op_num == '1':  # 教师手工考勤修改
                self.manual_checkin_alter(teacher_id, course_list)

            elif op_num == '2':  # 教师手工考勤增加
                self.manual_checkin_add(teacher_id, course_list)

            elif op_num == '0':
                break

            else:
                flagchar = raw_input(Reminder.SystemInError)
                if flagchar:
                    return 0

    def manual_form_control(self, teacherwechat_id):
        """
        :param teacherwechat_id:
        :return:
        """
        count = 0
        teacher_id = self.get_teacherid(teacherwechat_id)
        courselist = self.get_courselist(teacher_id)
        self.cform(teacher_id, courselist)
        while count == 0:
            print "----------------------------"
            operator = raw_input("您是否在手工考勤界面继续操作?y/n：")
            if operator == 'y':
                self.cform(teacher_id, courselist)
            elif operator == 'n':
                return
            else:
                operator = raw_input("您的输入有误，请重新输入: (y/n)")


# 教师所能进行的手工考勤
if __name__ == "__main__":
    pass
