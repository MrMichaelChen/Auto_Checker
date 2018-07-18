# encoding=utf-8
"""this module is to prepare data for student"""
# This program provide some methods for student to do check-in
from operate_file import OperateData
from __init__ import readini


class SMethod(OperateData):
    """do some methods"""
    def __init__(self):
        pass

    def get_student_info(self, _stu_wechatid):
        """to get student info by student`s wechatid"""
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
        return stu_message_list

    def get_detail_name(self, _stu_wechatid):
        """to get detail file name"""
        tea_id = 0
        cou_id = 0
        seq_id = 0
        stu_info = self.get_student_info(_stu_wechatid)
        count = 0  # 设置查询班级时的控制变量
        for listline in readini.List:  # 在全局队列中找到该行
            for classline in listline[2]:  # 在含有信息的行中找到班级
                if classline == stu_info[1]:
                    count = 1
                    tea_id = listline[0]
                    cou_id = listline[1]
                else:
                    pass
        if count == 0:
            print '没有查询到该班级'
            file_name = ''
            return file_name
        data = self.read_file('OutData/seq.csv')
        count1 = 0  # 设置一个查询seq时的控制变量
        for line in data:
            if (line['TeacherID'] == tea_id) & (line['CourseID'] == cou_id):
                seq_id = line['SeqID']
                count1 = 1
            else:
                pass
        if count1 == 0:
            print '找不到相关信息！'
            # exit(0)
            return

        print '你将进行ID为' + str(tea_id) + ',课程ID为' + str(cou_id) + '的教师的考勤操作'
        file_name = 'OutData/' + str(tea_id) + '_' + str(cou_id) + '_' + \
                   str(seq_id) + '_' + 'checkinDetail.csv'
        return file_name


if __name__ == '__main__':
    pass
