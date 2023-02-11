#When eigenvec or tsv are converted to PKL, the PANDAS version and model version should be the same as DNNGP.
#So, please run the program in a DNNGP environment.
import pandas as pd
########Set path section
inpath=r"C:\Users\91425\Desktop\DNNGP使用说明\dnngp\Test\Input_files\train_data.csv" #Set input path
outpath=r"C:\Users\91425\Desktop\DNNGP使用说明\dnngp\Test\Input_files\train_data.pkl" #Set output path

########Conversion format section
inpath=inpath.replace('\\','/') #Replace '\' with '/' in the input path.
outpath=outpath.replace('\\','/') #Replace '\' with '/' in the output path.
if "eigenvec" in inpath:
    Gene = pd.read_csv(inpath, sep='\t',header=0,index_col=1) #read eigenvec file.
    del Gene['#FID'] #Delete the '#FID' column
    Gene.to_pickle(outpath) #output pkl file
elif "csv" in inpath:
    Gene = pd.read_csv(inpath, sep=',',header=0,index_col=0) #read csv file.
    Gene.to_pickle(outpath) #output pkl file
else:
    Gene = pd.read_csv(inpath, sep='\t',header=0,index_col=0) #read tsv file.
    Gene.to_pickle(outpath) #output pkl file