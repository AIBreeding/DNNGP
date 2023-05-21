#-*- coding:utf-8 -*-

import time,sys
sys.path.append("..")
import config_dnngp, dnngp

if __name__ == '__main__': 
    start_model = time.time()
    opt = config_dnngp.get_options()
    batch_size = opt.batch_size
    lr = opt.lr
    epoch = opt.epoch
    patience = opt.patience
    dropout1 = opt.dropout1
    dropout2 = opt.dropout2
    SNP = opt.snp
    pheno = opt.pheno
    output = opt.output
    SEED = opt.seed
    CV = opt.cv
    part = opt.part
    NMearlystopping = opt.earlystopping
    dnngp.prepare() 
    dnngp.main(SNP, pheno, batch_size, lr, epoch, patience, dropout1, dropout2, output, SEED, CV, part, NMearlystopping)
    end_model = time.time()
    print('Running time: %s Seconds' % (end_model - start_model))