#-*- coding:utf-8 -*-
#########################
# filename: run.py
#########################

import subprocess,sys
sys.path.append("..")

cmds = [
    'python dnngp_runner.py --batch_size 28 --patience 5 --lr 0.001 --dropout2 0.3 --seed 123 --epoch 5 --cv 5 --part 1 --earlystopping 10 --snp ".../Input_files/wheat599_pc95.pkl" --pheno ".../Input_files/wheat1.tsv" --output .../Output_files/'
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