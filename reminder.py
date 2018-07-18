# encoding:utf-8

class Reminder(object):
    # 手工考勤中的提示信息
    NotFindInfo = '无法在教师的信息表里查询到该教师的信息'
    SystemInError = '输入有误！请重新输入：或者输入-1返回'
    ChooseCourseId = '请输入您选择的课程号'
    ChooseCourseIdError = '输入有误！请重新输入：'
    InputAlterSeqTime = '请输入您所需要的次序号'
    InputAlterStuID = '输入你想要修改的学生学号'
    InputCheckInResult = '输入该学生的考勤结果：'
    AlterSuccessfully = '您已成功修改该学生的考勤结果'
    AddSuccessfully = '您已成功增加一次考勤记录，并默认所有学生出勤'
    NotFindSumFrom = "文件不存在（可能是还未生成一次考勤记录！）！请查看您的输入！"
    FindSumfileError = '未找到对应sum表'
    StuRandomError = '对不起！当前教师没有开启抽点！'
    StuRandomSuccessfully = '您已完成了正确的抽点考勤操作'

    # 节次的考勤限定时间
    FirstSsec = '080000'
    FirstEsec = '101000'
    SecondSsec = '101000'
    SecondEsec = '121000'
    ThirdSsec = '140000'
    ThirdEsec = '161000'
    ForthSsec = '161000'
    ForthEsec = '181000'
    EveSsec = '190000'
    EveEsec = '211000'

    # 上课时间
    FirstS = '080000'
    FirstE = '101000'
    SecondS = '101000'
    SecondE = '121000'
    ThirdS = '140000'
    ThirdE = '161000'
    ForthS = '161000'
    ForthE = '181000'
    EveS = '190000'
    EveE = '211000'


    def __init__(self):
        pass
