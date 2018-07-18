# encoding:utf-8
"""this module is to manage checkin result and update sum data"""
from t_base_checkin import BaseCheckin
from __init__ import readini


# 自主考勤的考勤结果计算方法
class ResultManager(BaseCheckin):
    """to manage checkin result"""

    def __init__(self):
        pass

    # 以后的话seq序号应该作为参数传入
    def get_c_detailname(self, teacher_id, course_id):
        """
        to get detail file name
        :param teacher_id:
        :param course_id:
        :return:
        """
        seq_list = self.get_seqnumlist(course_id, teacher_id)
        print seq_list
        if seq_list:
            seq_id = max(seq_list)
            file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                        str(seq_id) + '_' + 'checkinDetail.csv'
            return file_name
        else:
            print "查找考勤次序号错误，可能该教师还未生成考勤记录"

    # 计算迟到时间
    def get_latertime(self, teacher_id, course_id):
        """
        to get the late time
        :param teacher_id:
        :param course_id:
        :return:
        """
        seq_list = self.get_seqnumlist(course_id, teacher_id)
        seq_id = max(seq_list)
        data = self.read_file('OutData/seq.csv')
        for line in data:
            if teacher_id == line['TeacherID']:
                if seq_id == line['SeqID']:
                    return line['StartTime']

    # 2017-06-07 17:02:30.
    def format_time(self, time):
        """
         to format time
        :param time:
        :return:
        """
        gettime = time[11:13] + time[14:16] + time[17:19]
        return gettime

    # 此函数将所有的出勤、迟到、早退的判定方法列举，余下的所有情况皆判定为缺勤
    def judge_result(self, teacher_id, course_id):
        """
         to judge the check in result
        :param teacher_id:
        :param course_id:
        :return:
        """
        filename = self.get_c_detailname(teacher_id, course_id)
        data = self.read_file(filename)
        bufferdata = []
        for line in data:
            if (line['StuID']):
                if (line['IsSuss'] == 'True') & (line['checkinType'] == 'Auto'):
                    # 出勤
                    if (line['checkinResult'] == '缺勤'):
                        line['checkinResult'] = '出勤'
                    # 迟到
                    if (line['checkinResult'] == '出勤') & (int(self.format_time(line['checkTime'])) >
                                                              int(self.format_time(
                                                                  self.get_latertime(teacher_id, course_id)))) + 300:
                        line['checkinResult'] = '迟到'
                # 请假
                if (line['checkinResult'] == '缺勤') & (line['checkinType'] == '请假'):
                    line['checkinResult'] = '请假'

                if (line['IsSuss'] == 'True') & (line['checkinType'] == 'Random'):
                    for line1 in data:
                        if (line1["StuID"] == line["StuID"]):
                            if (line['checkinResult'] == '出勤') & (line1['checkinResult'] == '出勤'):
                                line['checkinResult'] = '出勤'

                            if (line1['checkinResult'] == '出勤') & (line['checkinResult'] == '缺勤'):
                                line['checkinResult'] = '早退'

                            if (line1['checkinResult'] == '迟到') & (line['checkinResult'] == '出勤'):
                                line['checkinResult'] = '迟到'

                            if (line1['checkinResult'] == '迟到') & (line['checkinResult'] == '缺勤'):
                                line['checkinResult'] = '迟到/早退'

            bufferdata.append(line)

        self.write_file(bufferdata, filename)

    # 计算考勤次数
    def get_checktime(self, course_id):
        """
             
        :param course_id:
        :return:
        """
        detailfilelist = self.find_detailfile(course_id)
        count = 0
        for line in detailfilelist:
            if line[17] > count:
                count = line[17]
                if line[18] != "_":
                    count = count + line[18]
        return count

    # 更新sum表
    def update_sum(self, teacher_id, course_id):
        sumfile = self.find_sumfile(course_id)
        sumfile = 'OutData/' + str(sumfile)
        sum_data = self.read_file(sumfile)
        checktime = self.get_checktime(course_id)
        sum_all_data = []
        for line in range(1, int(checktime) + 1):
            file_name = 'OutData/' + str(teacher_id) + '_' + str(course_id) + '_' + \
                        str(line) + '_' + 'checkinDetail.csv'
            detail_data = self.read_file(file_name)
            # 把更新的列表放在第一行遍历
            for line2 in sum_data:

                for line1 in detail_data:

                    if (line1['StuID'] == line2['StuID']):
                        checknum = 'checkin' + str(line)
                        line2.update({checknum: line1['checkinResult']})

                checknum = 'checkin' + str(line)
                if line2[checknum] == '':
                    line2[checknum] = '缺勤'

                if line == int(checktime):
                    sum_all_data.append(line2)
        self.write_file(sum_all_data, sumfile)
        print "更新考勤sum表成功"

    # 计算考勤结果 并将考勤结果导入sum表
    def manage_action(self, teacher_id, course_id):
        self.judge_result(teacher_id, course_id)
        self.update_sum(teacher_id, course_id)


if __name__ == '__main__':
    readini.List = [['2004633', '51610189', ['\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1401',
                                             '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1402',
                                             '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403', ],
                     '2016-06-09 08:00:21']]

    teacher_action = ResultManager()
    teacher_action.manage_action('2004633', '51610189')
    # t=CheckinRule()
    # #t.Judge_result('OutData/2004355_51610055_1_checkinDetail.csv')
    # #t.Get_latertime('2004633','51610189')
    # t.format_time()
