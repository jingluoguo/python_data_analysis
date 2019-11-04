#coding:utf-8
import re
import linecache
# Date£º2019.10.11
# author£ºjingluo
file_name = '702ge.fasta'
Creat_file_DP = 'a.txt'
Creat_file_OP = 'b.txt'
f = open(file_name,'rb')
num_get = 8
check_D = 'DP'
check_O = 'OP'
def create__file(file_name_1, msg_1, file_name_2, msg_2, num_line):
    if file_name_1 != '':
        f_1 = open(file_name_1, "a")
        f_1.write('>'+num_line+'\n'+msg_1)
        f_1.close()
    if file_name_2 != '':
        f_2 = open(file_name_2, "a")
        f_2.write(msg_2 + '\n')
        f_2.close()
def create_DP_OP(DPS, DPE, OPS, OPE, str_list,line_nume):
    List = sorted(list(map(int,DPS+DPE+OPS+OPE)))
    Flag = True
    if DPS[0] > OPS[0]:
        Flag = False
    for num,i in enumerate(List,start=1):
        if num < len(List):
            if i+1 == List[num]:
                if Flag:
                    Flag = False
                    if ((i - List[num-2] +1) >= num_get) and ((List[num+1] - List[num] +1) >= num_get):
                        create__file(Creat_file_DP, str_list[i-num_get:i], Creat_file_DP, str_list[i:i+num_get], str(line_nume))
                    # elif ((i - List[num-2] +1) >= num_get):
                    #     create__file(Creat_file_DP, str_list[i-num_get:i], '', '',str(line_nume))
                    # elif ((List[num+1] - List[num] +1) >= num_get):
                    #     create__file('', '', Creat_file_DP, str_list[i:i+num_get],str(line_nume))
                else:
                    Flag = True
                    if ((i - List[num-2] +1) >= num_get) and ((List[num+1] - List[num] +1) >= num_get):
                        create__file(Creat_file_OP, str_list[i-num_get:i], Creat_file_OP, str_list[i:i+num_get],str(line_nume))
                    # elif ((i - List[num-2] +1) >= num_get):
                    #     create__file(Creat_file_OP, str_list[i-num_get:i], '', '', str(line_nume))
                    # elif ((List[num+1] - List[num] +1) >= num_get):
                    #     create__file('', '', Creat_file_OP, str_list[i:i+num_get], str(line_nume))
def handle_fasta():
    line_nume = 0
    with open(file_name,'r') as f:
        for num,line in enumerate(f):
            line = line.strip('\n')
            if re.match('^>', line) is not None:
                line_nume =  line_nume + 1
                if check_D and check_O in line:
                    str = linecache.getline(file_name, num + 2)
                    DPS = re.findall('DPS(\d+)+', line)
                    DPE = re.findall('DPE(\d+)+', line)
                    OPS = re.findall('OPS(\d+)+', line)
                    OPE = re.findall('OPE(\d+)+', line)
                    create_DP_OP(DPS, DPE, OPS, OPE, str, line_nume)
if __name__ == '__main__':
    num_get = int(input('input num_get'))
    handle_fasta()