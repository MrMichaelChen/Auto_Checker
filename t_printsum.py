# encoding:utf-8
"""this module is create a print form for teacher"""
from t_base_checkin import BaseCheckin

class TeacherPrintSum(BaseCheckin):
    """some methods for teacher"""
    def __init__(self):
        pass

    def to_get_all_sum(self, teacher_wechat_id):
        course_list = self.get_courselist(self.get_teacherid(teacher_wechat_id))
        course_id = self.teacher_choose_course(course_list)
        sumfilename = self.find_sumfile(course_id)
        sumdata = self.read_file("OutData/" + sumfilename)
        return sumdata

    def to_print_all_sum(self, sumdata):
        print sumdata

    def to_print_oneseq_sum(self, sumdata):
        print sumdata[0].keys()
        seq = input("请选择您所希望查看的考勤次序号(1、2、3.....)")
        checknum = 'checkin' + str(seq)
        for line in sumdata:
            print line['StuID'] + line[checknum]

    def to_print_onestu_sum(self, sumdata):
        stuid = input("请输入所查看学生的学号：")
        for line in sumdata:
            if line["StuID"] == str(stuid):
                print line

    def printfrom(self, sumdata):

        print "****************欢迎进入教师查看菜单******************"
        print "*******1.考勤汇总信息全部输出*****2.查看某次考勤信息******"
        print "*******3.查看某位同学的考勤信息***0.退出****************"
        op_num = raw_input("请输入您想要的操作：")
        count = 0
        while count == 0:
            count = 1
            if op_num == '1':  # 教师手工考勤修改
                self.to_print_all_sum(sumdata)

            elif op_num == '2':  # 教师手工考勤增加
                self.to_print_oneseq_sum(sumdata)

            elif op_num == '3':  # 查看考勤sum表
                self.to_print_onestu_sum(sumdata)

            elif op_num == '0':
                break

            else:
                flagchar = raw_input(reminder.SystemInError)
                if flagchar:
                    return 0

    def print_form_control(self, teacher_wechat_id):
        sumdata = self.to_get_all_sum(teacher_wechat_id)
        count = 0
        self.printfrom(sumdata)
        while count == 0:
            print "----------------------------"
            operator = raw_input("您是否在查看考勤结果界面继续操作?y/n：")
            if operator == 'y':
                self.printfrom(sumdata)
            elif operator == 'n':
                return
            else:
                operator = raw_input("您的输入有误，请重新输入: (y/n)")


if __name__ == "__main__":
    pass
