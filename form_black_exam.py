# encoding:utf-8
"""this module is create a form"""
import sys
from import_date import ImportCsvData
from __init__ import readini
from t_antocheckin import TeacherAutoCheckIn
from s_autocheckin import StuCheckIn
from t_randomcheckin import TeacherRandomCheckIn
from s_randomcheckin import StuRandomCheckin
from t_manualcheckin import TeacherManualCheckIn
from s_delay import StuDelay
from t_delay import TDelay
from t_printsum import TeacherPrintSum
from s_printsum import StudentPrintSum


class ParentForm(object):
    """this class is to show a form for user"""
    def __init__(self):

        self.read = readini()  # 读取配置文件
        self.t_auto_checkin = TeacherAutoCheckIn()  # 教师开始签到
        self.t_random_checkin = TeacherRandomCheckIn()  # 教师随机抽点
        self.t_manual_checkin = TeacherManualCheckIn()  # 教师手工签到
        self.s_checkin = StuCheckIn()  # 学生自动签到
        self.s_delay = StuDelay()  # 学生迟到类
        self.s_randomcheckin = StuRandomCheckin()
        self.import_data = ImportCsvData()
        self.t_delay = TDelay()
        self.t_print_sum = TeacherPrintSum()
        self.s_print_sum = StudentPrintSum()

    def main_form(self):
        wechat_id = raw_input("请输入您的微信号：")
        if self.t_auto_checkin.get_teacherid(wechat_id) != False:

            print "****************欢迎进入模拟控制菜单******************"
            print "*******1.教师开始考勤********2.教师手工考勤************"
            print "*******3.教师抽点考勤********4.教师确认请假************"
            print "*******5.教师查看考勤结果*****0.退出*******************"
            op_num = raw_input("请输入您想要的操作：")
            main_count = 0
            while main_count == 0:
                main_count = 1
                if op_num == '1':  # 教师开启考勤
                    teacher_wechat_id = wechat_id
                    self.t_auto_checkin.start_checkin(teacher_wechat_id)

                elif op_num == '2':  # 教师进行手工考勤操作
                    teacher_wechat_id = wechat_id
                    self.t_manual_checkin.manual_form_control(teacher_wechat_id)

                elif op_num == '3':  # 教师开启抽点考勤
                    teacher_wechat_id = wechat_id
                    self.t_random_checkin.random_checkin(teacher_wechat_id)
                    print "抽点结束！"

                elif op_num == '4':  # 教师确认请假
                    teacher_wechat_id = wechat_id
                    self.t_delay.leave_checkin(teacher_wechat_id)

                elif op_num == '5':  # 教师查看信息
                    teacher_wechat_id = wechat_id
                    self.t_print_sum.print_form_control(teacher_wechat_id)

                elif op_num == '0':  # 退出系统
                    sys.exit(0)

                else:
                    main_count = 0
                    op_num = raw_input("您的输入有误！请重新输入:")

        elif self.s_checkin.get_student_info(wechat_id):
            print "****************欢迎进入模拟控制菜单******************"
            print "*******1.学生进行考勤********2.学生抽点考勤************"
            print "*******3.学生进行请假********4.学生查看考勤信息*********"
            print "*******0.退出***************************************"

            op_num = raw_input("请输入您想要的操作：")
            s_count = 0
            while s_count == 0:
                s_count = 1
                if op_num == '1':
                    stu_wechat_id = wechat_id
                    input_stream = raw_input("请输入您的考勤证据：")
                    self.s_checkin.stu_auto_checkin(stu_wechat_id, input_stream)

                elif op_num == '2':
                    stu_wechat_id = wechat_id
                    input_stream = raw_input("请输入您的考勤证据：")
                    self.s_randomcheckin.stu_random_checkin(stu_wechat_id, input_stream)

                elif op_num == '3':  # 学生进行请假操作
                    stu_wechat_id = wechat_id
                    input_stream = raw_input("请输入您的请假证据：")
                    self.s_delay.stu_leave(stu_wechat_id, input_stream)

                elif op_num == '4':
                    stu_wechat_id = wechat_id
                    self.s_print_sum.form_control(stu_wechat_id)

                elif op_num == '0':  # 退出系统
                    sys.exit(0)

                else:
                    s_count = 0
                    op_num = raw_input("您的输入有误！请重新输入:")

        elif wechat_id == '000000':
            print "****************欢迎进入模拟控制菜单******************"
            print "*******1.导入文件信息********0.退出******************"
            op_num = raw_input("请输入您想要的操作：")
            g_count = 0
            while g_count == 0:
                g_count = 1
                if op_num == '1':
                    self.import_data.start_import_data()
                elif op_num == '0':  # 退出系统
                    sys.exit(0)
                else:
                    g_count = 0
                    op_num = raw_input("您的输入有误！请重新输入:")

        else:
            print"您不是本系统已经认定的成员"


if __name__ == "__main__":

    first_test = ParentForm()
    first_count = 0
    first_test.main_form()
    while first_count == 0:
        print "-------------------------------"
        first_operator = raw_input("您是否在主菜单继续操作?y/n：")
        # print readini.List
        if first_operator == 'y':
            first_test.main_form()
        elif first_operator == 'n':
            sys.exit(0)
        else:
            first_operator = raw_input("您的输入有误，请重新输入: (y/n)")
