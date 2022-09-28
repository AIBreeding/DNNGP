#-*- coding: utf-8 -*-
import os,time,config_dnngp
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import regularizers
from tensorflow.keras.layers import *
from keras.callbacks import EarlyStopping
from scipy.stats.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tfdeterminism import patch

SEED=123
def prepare():
    #SEED=123
    patch()

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3,4,5,6,7,8,9,10,11,12"
    os.environ['PYTHONHASHSEED'] = str(SEED)
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.7
    session = tf.Session(config=config)
    config.gpu_options.allow_growth = True
    np.random.seed(SEED)
    tf.compat.v1.set_random_seed(SEED)

def readData(SNP, pheno):
    Gene = pd.read_pickle(SNP)
    phe = pd.read_csv(pheno, header=0, sep="\t")
    print(Gene.shape)
    print(phe.shape)
    X1_train, X1_test, Y_train, Y_test = train_test_split(Gene, phe, test_size=0.1, random_state=SEED)
    mms = StandardScaler()
    Y_train_mms = mms.fit_transform(Y_train)
    X_train = np.expand_dims(X1_train, axis=2)
    print(X_train.shape)
    X_test = np.expand_dims(X1_test, axis=2)
    print(X_test.shape)
    n = X_train.shape[1]
    return X1_train, X1_test, X_train, X_test, Y_train, Y_test, Y_train_mms, n

def dnngp_model(X_train, X_test, Y_train, Y_test, Y_train_mms, n, epoch, patience, batch_size, lr, dropout1, dropout2):
    mms = StandardScaler()
    cnn1D = Sequential()
    cnn1D.add(Conv1D(64, 4, padding='same', activation='relu', input_shape=(n, 1),
                     kernel_initializer='TruncatedNormal',
                     kernel_regularizer=regularizers.l2(0.01),
                     bias_regularizer=regularizers.l2(0.1)
                     ))
    cnn1D.add(Dropout(dropout1))
    cnn1D.add(BatchNormalization())
    cnn1D.add(Conv1D(64, 4, padding='same', activation='relu',
                     kernel_initializer='TruncatedNormal',
                     kernel_regularizer=regularizers.l2(0.001),
                     bias_regularizer=regularizers.l2(0.00001)
                     ))
    cnn1D.add(Dropout(dropout2))
    cnn1D.add(BatchNormalization())
    cnn1D.add(Conv1D(64, 4, padding='same', activation='relu',
                     kernel_initializer='TruncatedNormal',
                     kernel_regularizer=regularizers.l2(0.001),
                     bias_regularizer=regularizers.l2(0.0001)
                     ))
    cnn1D.add(BatchNormalization())
    cnn1D.add(Flatten())
    cnn1D.add(Dense(3))
    cnn1D.add(Dropout(0.3))
    cnn1D.add(Dense(1))
    cnn1D.compile(
        loss='mean_squared_error',
        optimizer=keras.optimizers.Adam(lr=lr),
        metrics=(['mae', 'mse'])
    )
    print('\n', cnn1D.summary())
    early_stopping = EarlyStopping(monitor='mean_squared_error', patience=patience, verbose=2)

    reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.1, patience=patience, verbose=2, mode='auto',
                                                  min_delta=0.0001, cooldown=0, min_lr=0.00001)
    history = cnn1D.fit(X_train, Y_train_mms, batch_size=batch_size, epochs=epoch,
                        callbacks=[reduce_lr],
                        validation_data=(X_test, Y_test), shuffle=True, verbose=2)
    pred = cnn1D.predict(X_test)
    print(pred)
    pred = np.squeeze(pred)
    Y_test = mms.fit_transform(Y_test)
    Y_test = np.squeeze(Y_test)
    corr = pearsonr(pred, Y_test)
    return corr

def dnngp(SNP, pheno, epoch, patience, batch_size, lr, dropout1, dropout2):
    X1_train, X1_test, X_train, X_test, Y_train, Y_test, Y_train_mms, n = readData(SNP, pheno)
    corr = dnngp_model(X_train, X_test, Y_train, Y_test, Y_train_mms, n, epoch, patience, batch_size, lr, dropout1, dropout2)
    print("\nCorr obs vs pred =", corr)

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

 
    prepare()
    dnngp(SNP, pheno)
    end_model = time.time()
    print('cnn1D Running time: %s Seconds' % (end_model - start_model))
