# encoding=utf-8
"""this module is to delay for student"""
import time
import random
from s_prepare_data import SMethod

class StuDelay(SMethod):
    """对学生请假类的初始化"""
    def __init__(self):
        pass


    def stu_leave(self, _stuwechatid, _inputstream):
        """学生进行请假"""
        stu_id = self.get_student_info(_stuwechatid)[0]
        file_name = self.get_detail_name(_stuwechatid)
        checkin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        proof_path = _inputstream
        checkin_type = '请假'
        is_succ = bool(random.randrange(0, 2))
        checkin_result = '缺勤'
        bufferdata = []
        if file_name == '':
            print '打开详细表失败，或许是考勤窗口已经关闭'
            return
        else:

            line = {'StuID': stu_id, 'checkTime': checkin_time, 'ProofPath': proof_path, \
                    'checkinType': checkin_type,
                    'IsSuss': is_succ, 'checkinResult': checkin_result}
            bufferdata.append(line)

        self.write_file(bufferdata, file_name, way="a+")
        print '你已进行了正常的请假操作'
