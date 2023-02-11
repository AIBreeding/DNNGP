# -*- coding: utf-8 -*-
import argparse
import os

def output_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def get_options(
        parser=argparse.ArgumentParser()
):  
    parser.add_argument('--batch_size',
                        type=int,
                        default=64,
                        help='Input batch size, default=64')
    parser.add_argument('--epoch',
                        type=int,
                        default=100,
                        help='Number of epochs to train for, default=100')
    parser.add_argument('--lr',
                        type=float,
                        default=0.1,
                        help='Select the learning rate, default=0.1')
    parser.add_argument('--patience',
                        type=int,
                        default=25,
                        help='If do not see model performance improvement in patience epoch, reduce the learning rate, default=25')
    parser.add_argument('--dropout1',
                        type=float,
                        default=0.5,
                        help='Dropout rate for the first layer, default=0.5')
    parser.add_argument('--dropout2',
                        type=float,
                        default=0.5,
                        help='Dropout rate for the second layer, default=0.5')
    parser.add_argument('--SNP',
                        type=str,
                        default="cubicf1_pc95.pkl",
                        help='Gene file')
    parser.add_argument('--pheno',
                        type=str,
                        default="DTT.txt",
                        help='Pheno file')
    parser.add_argument('--Seed',
                        type=int,
                        default=123,
                        help='Random seed, default=123')
    parser.add_argument('--output',
                        type=output_path,
                        help="Specify the path of outputs")
    opt = parser.parse_args()
    if opt.output: 
        print(f'batch_size: {opt.batch_size}')
        print(f'epochs (niters) : {opt.epoch}')
        print(f'learning rate : {opt.lr}')
        print(f'patience : {opt.patience}')
        print(f'dropout1 : {opt.dropout1}')
        print(f'dropout2 : {opt.dropout2}')
        print(f'SNP : {opt.SNP}')
        print(f'pheno : {opt.pheno}')
        print(f'output : {opt.output}')
        print(f'Random seed : {opt.Seed}')
    return opt
