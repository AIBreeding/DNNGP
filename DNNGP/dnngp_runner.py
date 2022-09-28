import time
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
    SNP = opt.SNP
    pheno = opt.pheno

    dnngp.prepare()
    dnngp.dnngp(SNP, pheno, epoch, patience, batch_size, lr, dropout1, dropout2)
    end_model = time.time()
    print('cnn1D Running time: %s Seconds' % (end_model - start_model))

