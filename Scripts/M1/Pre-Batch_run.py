#-*- coding:utf-8 -*-
#########################
# filename: run.py
#########################

import subprocess

cmds = [
    'python Pre_runner.py --Model ".../Output_files/training.model.h5" --SNP ".../Input_files/wheat599_pc95.pkl" --output .../Output_files/'
]

for cmd in cmds:
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE
    )
    str=p.stdout.read()
    try:
        print(str.decode('utf-8'))
    except Exception:
        print(str.decode('gbk'))