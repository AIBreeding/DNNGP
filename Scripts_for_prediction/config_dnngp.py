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
    parser.add_argument('--Model',
                        type=str,
                        default="training.model.h5",
                        help='Trained model files')
    parser.add_argument('--SNP',
                        type=str,
                        default="cubicf1_pc95.pkl",
                        help='Gene file to be predicted')
    parser.add_argument('--cal',
                        type=str,
                        default="calibration.csv",
                        help='The file used to calibrate the results')
    parser.add_argument('--output',
                        type=output_path,
                        help="Specify the path of outputs")
    opt = parser.parse_args()
    if opt.output: 
        print(f'Model : {opt.Model}')
        print(f'SNP : {opt.SNP}')
        print(f'Calibration : {opt.cal}')
        print(f'Output : {opt.output}')
    return opt
