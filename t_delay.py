# encoding:utf-8
"""this module is do the teacher cure delay action"""
from t_base_checkin import BaseCheckin
from manage_checkindata import ResultManager


# 教师进行手工确认请假
class TDelay(BaseCheckin):
    """to provide some methods for teacher"""
    def __init__(self):
        self.manager = ResultManager()

    def leave_checkin(self, teacher_wechat_id):
        """to confirm delay"""
        teacher_id = self.get_teacherid(teacher_wechat_id)
        courselist = self.get_courselist(teacher_id)
        course_id = self.teacher_choose_course(courselist)
        filename = self.get_detailname(teacher_id, course_id)
        stu_array = []  # 请假的学生列表
        reader = self.read_file(filename)
        print '这次考勤请假的未被确认的人员为：'
        for line in reader:
            if line['checkinResult'] == '请假':
                stu_array.append(line)

        if stu_array:
            bufferdata = []
            stu_id = self.choose_num(stu_array)
            count = 0
            while count == 0:
                for line in stu_array:
                    for line1 in reader:
                        if line['StuID'] == line1['StuID'] == stu_id:
                            message = {'checkinResult': '请假已确认'}
                            line1.update(message)
                            stu_array.remove(line)
                            if stu_array == []:
                                count = 1
                        else:
                            pass
                        bufferdata.append(line1)
                print '请假信息已经确认！'

            self.write_file(bufferdata, filename)
            self.manager.update_sum(teacher_id, course_id)
        else:
            print "此次考勤没有请假的学生！"
