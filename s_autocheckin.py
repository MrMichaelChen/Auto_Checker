# encoding=utf-8

# This program show the student's operations
import time
import random
from s_prepare_data import SMethod


class StuCheckIn(SMethod):
    # 对学生正常考勤类进行初始化
    def __init__(self):
        pass

    # 学生进行正常的自主考勤
    def stu_auto_checkin(self, _stuWechatID, _inputStream):
        stu_id = self.get_student_info(_stuWechatID)[0]
        file_name = self.get_detail_name(_stuWechatID)
        checkin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        proof_path = _inputStream
        checkin_type = 'Auto'
        is_succ = bool(random.randrange(0, 2))
        checkin_result = '缺勤'

        if file_name == '':
            print '打开详细表失败，或许是考勤窗口已经关闭'
            return
        else:

            bufferdata = []
            data = self.read_file(file_name)
            for line in data:
                if line['StuID']:
                    if (line['StuID'] == stu_id) & (line['IsSuss'] == 'True'):
                        print "已经有您的成功认定记录"
                        return

            line = {'StuID': stu_id, 'checkTime': checkin_time, 'ProofPath': proof_path, \
                    'checkinType': checkin_type,
                    'IsSuss': is_succ, 'checkinResult': checkin_result}
            bufferdata.append(line)

        self.write_file(bufferdata, file_name, way='a+')
        print '你已进行了正常考勤的操作'

if __name__ == '__main__':
    pass
