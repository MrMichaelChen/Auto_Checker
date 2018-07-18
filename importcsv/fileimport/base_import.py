# coding=utf-8

import csv
from abc import ABCMeta, abstractmethod


class BaseImport(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def file_import(self, file_name, _filename):
        pass

    #向系统文件内导入无误外部数据
    def write_file(self, data, filename, way='wb'):
        """
        将数据写入文件
        :param data:
        :param filename:
        :param FIEDLS:
        :param way:
        :return:
        """
        try:
            with open(filename, way) as csv_file:
                FIEDLS = data[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=FIEDLS)
                writer.writerow(dict(zip(FIEDLS, FIEDLS)))  # 写表头
                for line in data:
                    writer.writerow(line)  # 写数据
                csv_file.close()

        except IOError:
            print "File open error : " + filename + "\nplease check the filename"
            exit(-1)

    # 从外部文件读取数据
    def read_file(self, filename, way='rb'):
        """read file information to listList
        :param filename: filename
        :param way: 文件打开方式默认为'rb'
        :return: 文件数据列表
        """
        try:
            with open(filename, way) as csv_file:
                reader = csv.DictReader(csv_file)
                data = []
                for info in reader:
                    data.append(info)

                csv_file.close()
                return data
        except IOError:
            print "File open error : " + filename + "\nplease check the filename"
            exit(-1)
