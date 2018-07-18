# encoding:utf-8
"""this module is to do random check in for student"""

import time
import random
from s_prepare_data import SMethod
from reminder import Reminder


class StuRandomCheckin(SMethod):
    """one method for student"""
    def __init__(self):
        pass

    def stu_random_checkin(self, _stuwechatid, input_stream):
        """main method"""
        data = self.read_file(self.get_detail_name(_stuwechatid))
        count = 0
        databuffer = []
        for line in data:
            if (line['StuID'] == self.get_student_info(_stuwechatid)[0]) & \
                    (line['checkinType'] == 'Random'):
                is_succ = bool(random.randrange(0, 2))
                checkin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                line = {'StuID': line['StuID'], 'checkTime': checkin_time, 'ProofPath': input_stream,
                        'checkinType': 'Random',
                        'IsSuss': is_succ, 'checkinResult': '出勤'}
                print Reminder.StuRandomSuccessfully
                count = 1
            databuffer.append(line)
        if count == 0:
            print Reminder.StuRandomError
        self.write_file(databuffer, self.get_detail_name(_stuwechatid))


if __name__ == '__main__':
    pass
