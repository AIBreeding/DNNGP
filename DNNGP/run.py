#-*- coding:utf-8 -*-
#########################
# filename: run.py
#########################

import subprocess

cmds = [
    'python dnngp_runner.py --batch_size 28 --lr 0.001 --dropout2 0.3 --SNP "../example-data/wheat599/SNP_origin/wheat599_X.pkl" --pheno "../example-data/wheat599/SNP_origin/wheat1.Y"',
    'python dnngp_runner.py --batch_size 21 --lr 0.005 --dropout2 0.3 --SNP "../example-data/wheat599/SNP_origin/wheat599_X.pkl" --pheno "../example-data/wheat599/SNP_origin/wheat2.Y"',
    'python dnngp_runner.py --batch_size 18 --lr 0.01 --dropout2 0.3 --SNP "../example-data/wheat599/SNP_origin/wheat599_X.pkl" --pheno "../example-data/wheat599/SNP_origin/wheat3.Y"',
    'python dnngp_runner.py --batch_size 25 --lr 0.001 --dropout2 0.3 --SNP "../example-data/wheat599/SNP_origin/wheat599_X.pkl" --pheno "../example-data/wheat599/SNP_origin/wheat4.Y"'
]

for cmd in cmds:
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE
    )
    print(p.stdout.read().decode('utf8'))
