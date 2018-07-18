# encoding=utf-8
"""this module is to do random check in by teacher"""

import random
import time
from t_base_checkin import BaseCheckin
from __init__ import readini

class TeacherRandomCheckIn(BaseCheckin):
    """some methods for teacher to do random check in"""

    def __init__(self):
        pass

    def get_trdetailname(self, teacher_id, course_id):
        """
        this function is only to get detail file name
        when a teacher want to start
        random check in
        """
        seq_list = self.get_seqnumlist(course_id, teacher_id)
        if seq_list:
            seq_id = max(seq_list)
        else:
            seq_id = 1
        course_id = course_id[0]
        file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                    str(seq_id) + '_' + 'checkinDetail.csv'
        return file_name

    # 教师开始抽点
    def random_checkin(self, teacher_wechat_id):
        """
         when a teacher want to start random check in
        :param teacher_wechat_id:
        :return:
        """
        teacher_id = self.get_teacherid(teacher_wechat_id)
        course_list = []
        course_list.append(self.get_courselist(teacher_id))
        course_id = self.teacher_choose_course(course_list)
        stu_array = []  # 置空该班级下的学生列表
        count = 0
        class_list = []
        for line in readini.List:
            if line[0] == teacher_id:
                class_list = line[2]  # 获得班级列表
                count = 1
            else:
                pass
        if count == 0:
            print '当前队列里没有此教师，无法开始抽点！'
            # exit(0)
            return

        data = self.read_file('InData/studentInfo.csv')
        for line in data:  # 遍历class列表查看是否是该班级内的学生，是就追加微信号
            if line["ClassID"] in class_list:
                stu_array.append(line["StuID"])

        num = int(raw_input("请输入您抽取的人数：（教师）"))
        stu_array2 = random.sample(stu_array, num)  # 实现抽取学生！
        print "需要进行考勤的学生的学号如下："
        print stu_array2
        file_name = self.get_trdetailname(teacher_id, course_id)  # 得到学生需要进行考勤的详细文件名
        stu = []
        checkin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for line in stu_array2:
            message = {'StuID': line, 'checkTime': checkin_time, 'ProofPath': '无', \
                       'checkinType': 'Random', 'IsSuss': '未知', 'checkinResult': '缺勤'}
            stu.append(message)
        self.write_file(stu, file_name, 'a+')


# 此时含有教师开启抽点和学生进行抽点的函数
if __name__ == "__main__":
    pass
