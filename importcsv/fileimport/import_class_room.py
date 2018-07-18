# coding=utf-8

from base_import import BaseImport
from importcsv.checker.base_check import BaseCheckMixin


class ImportClassRoomInfo(BaseImport, BaseCheckMixin):
    pass

if __name__ == '__main__':

    # 待导入教室信息文件
    new_file = '../../external/classRoomInfo.csv'
    # 目标文件
    orig_file = '../../internal/classRoomInfo.csv'
    # 实例化
    roomInfo = ImportClassRoomInfo()
    # 调用方法
    roomInfo.file_import(new_file, orig_file)