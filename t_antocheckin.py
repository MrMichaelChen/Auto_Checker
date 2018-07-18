# encoding=utf-8
"""this module is to start student auto check"""
import re
import time
from t_base_checkin import BaseCheckin
from timewindows import Timer
from __init__ import readini
from manage_checkindata import ResultManager


# This program is show the teacher's operations
# This program is show teacher to start the checkIn

class TeacherAutoCheckIn(BaseCheckin):
    """teacher auto check in methods"""

    def __init__(self):
        self.timer = Timer()  # 建立一个Timer计时器的实例
        self.manager = ResultManager()

    def to_first_judge(self, teacher_id, course_id):
        """first to judging weather the teacher have classes to check or not """
        class_list = []
        data = self.read_file('InData/courseInfo.csv')
        count = 0  # 设置下边追加班级时的控制变量
        for cline in data:
            if (cline['CourseID'] == str(course_id)) & (cline['TeacherID'] == str(teacher_id)):
                count = 1
                class_list.append(cline['ClassNums'])
            else:
                pass
        if count == 0:
            print '没有上课的班级！'
            return
        return class_list

    def get_stime(self, now_time):
        """get now time in a format"""
        stime0 = now_time.split(" ")
        stime1 = stime0[1].split(':')
        stime = stime1[0] + stime1[1]
        return stime

    def get_bagintime(self, b_time):
        """get begin time in a format"""
        begin_time = b_time
        begin_time_array = re.split('[- :]', begin_time)
        begintime = begin_time_array[3] + begin_time_array[4] + begin_time_array[5]
        return begintime

    def enter_list(self, teacher_id, course_id):
        """to judging weather the teacher can enter the list or not"""
        class_list = self.to_first_judge(teacher_id, course_id)  # 设置上课的班级列表
        if class_list == []:
            return False
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
        messagelist = [teacher_id, course_id, class_list, nowtime]
        if readini.List:  # 列表非空要进行判断！
            for line in readini.List:
                if line[0] != teacher_id:
                    if set(class_list) & set(line[2]):
                        print "班级已存在"
                        stime = self.get_stime(nowtime)
                        read = readini()
                        s = read.readIni()  # 从readIni中得到课程的开始时间和结束时间
                        begintime = self.get_bagintime(line[3])
                        # 首先，若是下课时间则可以提出上一位教师
                        if (s[0] < stime < s[1]) | (s[2] < stime < s[3]) | (s[4] < stime < s[5]) | \
                                (s[6] < stime < s[7]):
                            # self.s.manage_action(line[0], line[1])
                            self.append_judge(readini.List, messagelist)
                            print "此时为下课时间，踢出相同班级的教师成功，成功进入队列！"
                            return True
                        # 若为上课时间、则比较节次信息
                        elif self.judge_sec(begintime) < self.judge_sec(stime):
                            # self.s.manage_action(line[0], line[1])
                            self.append_judge(readini.List, messagelist)
                            print "此时为上课时间，提出上一节次的教师成功！"
                            return True
                        else:
                            print "当前班级正在考勤、您无法开启！"
                            return False
                    else:
                        readini.List.append(messagelist)
                        return True
                else:
                    print "教师已经在队列之内"
                    return False
        else:
            self.append_message(messagelist)
            return True

    def append_message(self, _messagelist):
        """append message when the teacher is allowed to enter the list"""
        readini.List.append(_messagelist)
        print "进入队列成功"
        self.timer.start_checktime()

    def append_judge(self, _list, _messagelist):
        """to judge a right way to append message when a teacher push another one"""
        line = readini.List[0]
        self.manager.manage_action(line[0], line[1])
        readini.List.remove(line)
        if readini.List:
            readini.List.append(_messagelist)
            self.timer.stop_checkin()
        else:
            readini.List.append(_messagelist)
            self.timer.start_checktime()

    # 教师开始考勤
    def start_checkin(self, teacher_wechatid):
        """when a teacher want to start auto check in"""
        teacher_id = self.get_teacherid(teacher_wechatid)
        course_list = self.get_courselist(teacher_id)
        course_id = self.teacher_choose_course(course_list)

        if self.get_seqnumlist(course_id, teacher_id) != []:
            seq_id = max(self.get_seqnumlist(course_id, teacher_id))
        else:
            seq_id = 1
        # if (self.Course_judge_time(TeacherID,CourseID) != False):
        if self.enter_list(teacher_id, course_id) != False:
            self.create_seq(teacher_id, course_id)
            self.creat_sum(teacher_id, course_id, int(seq_id))
            print "创建自助考勤考勤文件成功"
        else:
            print "开启考勤失败"


if __name__ == "__main__":
    pass
