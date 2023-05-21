import time
import Pre_config_dnngp, Pre_dnngp #导入的设置文件和dnngp.pyx文件

if __name__ == '__main__': #以文件形式而非导入形式运行则下方代码进行。
    start_model = time.time()
    opt = Pre_config_dnngp.get_options()
    SNP = opt.SNP
    output = opt.output
    model=opt.Model
    Pre_dnngp.prepare() #运行dnngp.pyx中的环境函数，进行运行环境的设置。
    Pre_dnngp.main(SNP, model,output) #将参数传入dnngp中。
    end_model = time.time()
    print('Running time: %s Seconds' % (end_model - start_model))