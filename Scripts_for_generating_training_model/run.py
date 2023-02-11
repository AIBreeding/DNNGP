#-*- coding:utf-8 -*-
#########################
# filename: run.py
#########################

import subprocess

cmds = [
    'python dnngp_runner.py --batch_size 28 --lr 0.001 --epoch 200 --dropout1 0.5 --dropout2 0.3 --Seed 123 --SNP "../Input_files/wheat599_pc95.pkl" --pheno "../Input_files/wheat1.tsv" --output ../Output_files/' 
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