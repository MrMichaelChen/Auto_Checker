# encoding:utf-8
"""this module is to create a print form for student """
from t_base_checkin import BaseCheckin
from reminder import Reminder


class StudentPrintSum(BaseCheckin):
    """some print method"""

    def __init__(self):
        pass

    def to_get_teacherid(self, stu_id):
        """to get teacher id by student id"""
        usedata = []
        data = self.read_file('InData/studentInfo.csv')
        count = 0
        classname = ' '
        for line in data:
            if line['StuID'] == stu_id:
                classname = line['ClassID']
        data = self.read_file('InData/courseInfo.csv')

        courselist = []

        for line in data:
            if line['ClassNums'] == classname:
                if line['CourseID'] not in courselist:
                    courselist.append(line['CourseID'])

        list = enumerate(courselist)

        course_id = ''

        for index, item in list:
            print index, ':', item
        choose_num = int(raw_input(Reminder.ChooseCourseId))
        for index, item in list:
            if index == choose_num:
                course_id = item
                count = 1

        while course_id == '':
            print Reminder.ChooseCourseIdError
            choose_num = int(raw_input(Reminder.ChooseCourseId))
            for index, item in list:
                if index == choose_num:
                    course_id = item
                    count = 1

        if count == 0:
            print "未找到学生所选课程ID"
            return False

        teacher_id = 0
        data = self.read_file('InData/courseInfo.csv')
        for line in data:
            if line['CourseID'] == course_id:
                teacher_id = line['TeacherID']
        usedata.append(teacher_id)
        usedata.append(course_id)

        return usedata

    def to_get_all_sum(self, course_id):
        """get sum data"""
        sumfilename = self.find_sumfile(course_id)
        sumdata = self.read_file("OutData/" + sumfilename)
        return sumdata

    def to_print_all_sum(self, sum_data, stu_id):
        """print all"""
        for line in sum_data:
            if line['StuID'] == stu_id:
                print line

    def to_print_oneseq_sum(self, sumdata, stu_id):
        """print only one time seq in the sum"""
        print sumdata[0].keys()
        seq = input("请选择您所希望查看的考勤次序号(1、2、3.....)")
        checknum = 'checkin' + str(seq)
        for line in sumdata:
            if line['StuID'] == stu_id:
                print line['StuID'] + line[checknum]

    def printfrom(self, sumdata, stu_id):
        """the form for teacher"""
        print "****************欢迎进入教师查看菜单******************"
        print "*******1.考勤汇总信息全部输出*****2.查看自己某次考勤信息******"
        print "*******0.退出**************************************"
        op_num = raw_input("请输入您想要的操作：")
        count = 0
        while count == 0:
            count = 1
            if op_num == '1':  # 教师手工考勤修改
                self.to_print_all_sum(sumdata, stu_id)

            elif op_num == '2':  # 教师手工考勤增加
                self.to_print_oneseq_sum(sumdata, stu_id)

            elif op_num == '0':
                break

            else:
                flagchar = raw_input(Reminder.SystemInError)
                if flagchar:
                    return 0

    def form_control(self, stu_wechatid):
        """to control teacher form"""
        stu_id = self.get_student_id(stu_wechatid)
        data = self.to_get_teacherid(stu_id)
        course_id = data[1]
        sumdata = self.to_get_all_sum(course_id)
        count = 0
        self.printfrom(sumdata, stu_id)
        while count == 0:
            print "----------------------------"
            operator = raw_input("您是否在学生查看考勤结果界面继续操作?y/n：")
            if operator == 'y':
                self.printfrom(sumdata, stu_id)
            elif operator == 'n':
                return
            else:
                operator = raw_input("您的输入有误，请重新输入: (y/n)")


if __name__ == "__main__":
    pass
