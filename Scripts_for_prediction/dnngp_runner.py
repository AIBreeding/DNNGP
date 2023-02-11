import time
import config_dnngp, dnngp

if __name__ == '__main__':
    start_model = time.time()
    opt = config_dnngp.get_options()
    SNP = opt.SNP
    cal = opt.cal
    output = opt.output
    model=opt.Model
    dnngp.prepare()
    dnngp.main(SNP, cal,model,output)
    end_model = time.time()
    print('cnn1D Running time: %s Seconds' % (end_model - start_model))