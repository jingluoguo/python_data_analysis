#!/usr/bin/env python
# coding:utf-8
# Date：2019.11.4
# author：jingluo
import re
import os
# 全局变量
num_get = 8
arrP = []
arrN = []
point_1 = 0
shell_command = ''# 需要填写shell命令
file_name = 'f_9_svm_train.txt'
Creat_training_file = 'training_file.txt'
Creat_testing_file = 'testing_file.txt'
Creat_result_file = 'result_file.txt'
# 创建文件
def create__file(file_name, msg_1):
    if file_name != '':
        f_1 = open(file_name, "a")
        f_1.write(msg_1)
        f_1.close()
# 文本分类新建
def handle_create__file(point_2, arr):
    for i in range(0, len(arr), round(len(arr) / num_get)):
        if point_1 == point_2:
            create__file(Creat_testing_file, arr[i:i + num_get])
        elif i + round(len(arr) / num_get) < len(arr):
            create__file(Creat_training_file, arr[i:i + num_get])
        elif i + round(len(arr) / num_get) >= len(arr):
            create__file(Creat_training_file, arr[len(arr) - 1])
# 文本筛选
def handle_fasta():
    with open(file_name,'r') as f:
        for num,line in enumerate(f):
            line = line.strip('\n')
            if re.match('^\+', line) is not None:
                arrP.append(line)
            if re.match('^\-', line) is not None:
                arrN.append(line)
        for counter in range(num_get):
            os.remove(Creat_training_file)
            os.remove(Creat_testing_file)
            handle_create__file(counter, arrP)
            handle_create__file(counter, arrN)
            var  = os.popen(shell_command)
            for temp in var.readlines():
                create__file(Creat_result_file,temp)
            point_1 = point_1 + 1
if __name__ == '__main__':
    num_get = int(input('input num_get:'))
    handle_fasta()