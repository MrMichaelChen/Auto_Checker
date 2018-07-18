# # encoding:utf-8
# import random
# import unittest
# from ImportDate import importdata
from __init__ import readini
from t_antocheckin import TeacherAutoCheckIn
from s_autocheckin import StuCheckIn
from operate_file import OperateData
from t_randomcheckin import TeacherRandomCheckIn
# from S_RandomCheckin import sturandomcheckin
# from T_ManualCheckin import teacherManualCheckIn
# from S_Delay import stuDelay
#
#
# class Test(unittest.TestCase):
#     ##初始化工作
#     def setUp(self):
#         self.test1 = importdata()
#         self.test2 = readini()
#         self.test3 = teacherAutoCheckIn()
#         self.test4 = stuCheckIn()
#         self.test5 = teacherRandomCheckIn()
#         self.test6 = sturandomcheckin()
#         self.test7 = teacherManualCheckIn()
#         self.test8 = stuDelay()
#     # 退出清理工作
#     def tearDown(self):
#         pass
#
#     # 具体的测试用例，一定要以test开头
#     def test_Is(self):
#         self.assertIS(abs(-1), 1)
#
#     # def testsub(self):
#     #      self.assertEqual(self.test2.readIni(), 1, 'test sub fail')
#
#
# if __name__ == '__main__':
#     unittest.main()

import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.t = TeacherAutoCheckIn()
        self.t1 = StuCheckIn()
        self.t2 = TeacherRandomCheckIn()

    # 测试查找教师ID
    def test_Get_teacherID(self):
        self.assertEqual(self.t.get_teacherid('wonka80'), '2004633')
        self.assertEqual(self.t.get_teacherid('ailin_66'), '2004366')
        self.assertEqual(self.t.get_teacherid('Tp_rt55'), '2004355')

    # 测试查找课程列表
    def test_Get_courseList(self):
        self.assertEqual(self.t.get_courselist('2004633'), ['51610189'])
        self.assertEqual(self.t.get_courselist('2004366'), ['51610166'])
        self.assertEqual(self.t.get_courselist('2004355'), ['51610055'])

    # 测试查找班级列表
    def test_Get_classList(self):
        self.assertIn(self.t.get_classlist('2004633', '51610189'),
                      [['\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1401', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1402', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1404', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1405']])
        self.assertIn(self.t.get_classlist('2004366', '51610166'),
                      [['计算机科学与技术1401']])
        self.assertIn(self.t.get_classlist('2004355', '51610055'),
                      [['\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1401', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1402', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1404', \
                        '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1405']])

    # 测试教师进入队列
    def test_Enter_List(self):
        self.assertTrue(self.t.enter_list('2004633', '51610189'))
        self.assertTrue(self.t.enter_list('2004366', '51610166'))
        print "班级信息冲突教师进入队列"
        # self.assertTrue(self.t.enter_list('2004355', '51610055'))

    # 测试学生信息
    def test_Get_SData(self):
        a = OperateData()
        data = a.read_file('InData/studentInfo.csv')
        studataList = []
        for line in data:
            stu = []
            stu.append(line['WeChatID'])
            stu.append(line['StuID'])
            stu.append(line['ClassID'])
            studataList.append(stu)
        for line in studataList:
            self.assertEqual(self.t1.get_student_info(line[0]), [line[1], line[2]])

        readini.List = [['2004633', '51610189', ['软件工程1401',
                                                 '软件工程1402',
                                                 '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403',
                                                 '\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe7\xa7\x91\xe5\xad\xa6\xe4\xb8\x8e\xe6\x8a\x80\xe6\x9c\xaf1401'],
                         '2016-06-09 14:00:21']]

        for line in studataList:
            if line[2] == '软件工程1401':
                self.t1.stu_auto_checkin(line[0], '1')
                print "考勤成功"

    # 测试详细表名称是否正确
    def test_Get_detailname(self):
        readini.List = [['2004633', '51610189', ['软件工程1401',
                                                 '软件工程1402',
                                                 '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403',
                                                 '\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe7\xa7\x91\xe5\xad\xa6\xe4\xb8\x8e\xe6\x8a\x80\xe6\x9c\xaf1401'],
                         '2016-06-09 14:00:2查找banji1']]

        print self.t2.get_detailname('wfsf_135')
        self.assertEqual(self.t2.get_trdetailname('wfsf_135', '51610189'),
                         'OutData/2004633_51610189_3_checkinDetail.csv')


if __name__ == '__main__':
    unittest.main()
