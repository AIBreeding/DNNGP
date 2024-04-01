# ___DNNGP: Deep neural network for genomic prediction___ <br>
<br>
The Python project 'DNNGP' can be used to implement genome-wide prediction (GP), which can predict the phenotypes of plants and animals based on multi-omics data. The code is written using Python 3.9 and TensorFlow 2.6.0.
<br><br>

More information could be found in the [user manual](DNNGP-usermanual.pdf).

Tips:
Deep learning models perform better with larger sample sizes.

### Change log

2024.03:
 1. Update the software to version 3.1 for both Windows and Linux.
 2. Optimize the naming of output files for model training. The current file name concatenates the `input phenotype file name`, the `original output file name` and the `part parameter value`. This change prevents the issue of overlapping phenotypic characters and fold number collisions with files.
 3. Optimize the complex parameter adjustment process.

### It is suggested tuning parameters as follows:

    batchsize: Set this to the largest value your hardware can support, typically increasing powers of 2.

    lr: Set this to 1, or any value you think is appropriate based on your understanding of deep learning. The learning rate is partially auto-adjusted by the internal algorithm.

    epoch: Set a maximum value and allow “earlystopping” to decide the optimal stopping point.

    dropout1；This parameter should be experimentally determined, with recommended trials ranging from 0.1 to 0.9.

    dropout2: Similarly, this needs empirical evaluation, usually between 0.1 and 0.9.

    patience: A value between 10 and 100 is generally acceptable. It doesn't take much adjustment.

    earlystopping: Set this value to 5-10 times the value of patience. Increase this multiplier if the iterations end too quickly.

The information above is consistent with our user manual. For more details, please refer to the user manual.




## 👥 Contacts

[Huihui Li](lihuihui@caas.cn)（lihuihui@caas.cn）

