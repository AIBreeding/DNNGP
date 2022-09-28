# -*- coding: utf-8 -*-
import argparse


def get_options(
        parser=argparse.ArgumentParser()
):  
    parser.add_argument('--batch_size',
                        type=int,
                        default=64,
                        help='input batch size, default=64')
    parser.add_argument('--epoch',
                        type=int,
                        default=100,
                        help='number of epochs to train for, default=100')
    parser.add_argument('--lr',
                        type=float,
                        default=0.1,
                        help='select the learning rate, default=0.1')
    parser.add_argument('--patience',
                        type=int,
                        default=25,
                        help='如果在patience个epoch中看不到模型性能提升，则减少学习率, default=25')
    parser.add_argument('--dropout1',
                        type=float,
                        default=0.5,
                        help='dropout rate for the first layer, default=0.5')
    parser.add_argument('--dropout2',
                        type=float,
                        default=0.5,
                        help='dropout rate for the second layer, default=0.5')
    parser.add_argument('--SNP',
                        type=str,
                        default="cubicf1_pc95.pkl",
                        help='snp file')
    parser.add_argument('--pheno',
                        type=str,
                        default="DTT.txt",
                        help='pheno file')
    # parser.add_argument('--seed', type=int, default=123, help="random seed")
    # parser.add_argument('--cuda', action='store_true', default=True, help='enables cuda')
    # parser.add_argument('--checkpoint_path',type=str,default='',
    #                     help='Path to load a previous trained model if not empty (default empty)')
    parser.add_argument('--output',
                        action='store_true',
                        default=True,
                        help="shows output")
    opt = parser.parse_args()
    if opt.output: 
        # print(f'num_workers: {opt.workers}')
        print(f'batch_size: {opt.batch_size}')
        print(f'epochs (niters) : {opt.epoch}')
        print(f'learning rate : {opt.lr}')
        print(f'patience : {opt.patience}')
        print(f'dropout1 : {opt.dropout1}')
        print(f'dropout2 : {opt.dropout2}')
        print(f'SNP : {opt.SNP}')
        print(f'pheno : {opt.pheno}')
        # print(f'manual_seed: {opt.seed}')
        # print(f'cuda enable: {opt.cuda}')
        # print(f'checkpoint_path: {opt.checkpoint_path}')
    return opt
