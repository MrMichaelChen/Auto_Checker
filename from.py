# #encoding:utf-8
# import time
# from __init__ import readini
# from T_AntoCheckin import teacherAutoCheckIn
# from S_AutoCheckin import stuCheckIn
# from T_RandomCheckin import teacherRandomCheckIn
# from S_Delay import stuDelay
#
#
# # #下课时间情况下，第一教师进入队列，正常开启考勤，第二位教师也进入队列，且第二
# # # 位教师和第一位教师班级信息没有冲突，正常开启考勤。这时第三位教师进入队列，
# # # 第三位教师和第一位教师的班级信息存在冲突。
# # tea=teacherAutoCheckIn()
# # time.sleep(5)
# #
# # tc = 'wonka80'
# # co = '51610189'
# # tea.Start_CheckIn(tc, co)
# #
# # time.sleep(15)
# #
# # tc1 = 'ailin_66'
# # co1 = '51610166'
# # tea.Start_CheckIn(tc1,co1)
# #
# # time.sleep(15)
# #
# # tc2 = 'Tp_rt55'
# # co2 = '51610055'
# # tea.Start_CheckIn(tc2,co2)
#
#
# # #上课情况下，第一位教师进入队列考勤，这时第二位教师尝试进入队列，第二位教师与第一位教师的班级信息存在冲突。
# # tea=teacherAutoCheckIn()
# # time.sleep(5)
# #
# # tc = 'wonka80'
# # co = '51610189'
# # tea.Start_CheckIn(tc, co)
# #
# # time.sleep(15)
# #
# # tc2 = 'Tp_rt55'
# # co2 = '51610055'
# # tea.Start_CheckIn(tc2,co2)
#
# # #上课情况下，第一位教师进入队列，其学生进行考勤，然后第二位教师进入队列
# # # ，其学生进行考勤，第一位教师时间计时器结束之后，时间窗口计算差值为第二位教师计时。
# # tea=teacherAutoCheckIn()
# # time.sleep(5)
# #
# # tc = 'wonka80'
# # co = '51610189'
# # tea.Start_CheckIn(tc, co)
# #
# # stu=stuCheckIn()
# # stu.Stu_Auto_CheckIn('wfsf_135', 1)
# #
# # time.sleep(10)
# #
# # tc1 = 'ailin_66'
# # co1 = '51610166'
# # tea.Start_CheckIn(tc1,co1)
# #
# # stu.Stu_Auto_CheckIn('wfsf_85', 1)
#
# #上课情况下，教师进入队列，提出上一节次的教师。
# readini.List = [['2004633', '51610189', ['\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1401',
#                                              '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1402',
#                                              '\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xb7\xa5\xe7\xa8\x8b1403',
#                                              '\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe7\xa7\x91\xe5\xad\xa6\xe4\xb8\x8e\xe6\x8a\x80\xe6\x9c\xaf1401'],
#                      '2016-06-09 15:20:21']]
#
# tea=teacherAutoCheckIn()
# time.sleep(15)
#
# tc2 = 'Tp_rt55'
# co2 = '51610055'
# tea.Start_CheckIn(tc2,co2)
