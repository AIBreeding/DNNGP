# ___DNNGP: Deep neural network for genomic prediction___ <br>
<br>
The Python project 'DNNGP' can be used to implement genome-wide prediction (GP), which can predict the phenotypes of plants and animals based on multi-omics data. The code is written using Python 3.6 and TensorFlow 1.15.
<br><br>

## 📘 Table of Contents

  - [Table of Contents](#📘-Table-of-Contents-)
  - [Change Log](#🔍-Change-Log-)
  - [Installation](#🌟-Installation-)
  - [How to run DNNGP](#🌟-How-to-run-DNNGP-)
  - [Data](#🔍-Data-)
  - [Maintainers](#Maintainers)
  - [Contacts](#👥-Contacts-)
  - [License](#📘-License-)

## 🔍 Change Log

- [Version 1.0](#) -First version released on August, 20th, 2022


## 🌟 Installation

Installation supports Python 3.6. Follow the instructions at https://www.tensorflow.org/install/gpu to set up GPU support for faster model
training. Once GPU is set up, install with
[conda](https://docs.conda.io/projects/conda/en/latest/index.html) by executing
these instructions from the root of the checked-out repository:

```
conda create -n dnngp python=3.6.5
conda activate dnngp
pip install -r requirements.txt
```
Users can also use DNNGP on CPU, and the installation method is the same as above.

## 🌟 How to run DNNGP

To run locally, there are two required input files. One file contains the phenotype of interest, the other file contains the SNP data, genomic expression data or other related omics data with digital coding. 

An example command to train DNNGP to predict the phenotype pheno from the SNP data, genomic expression data or other related omics data with digital coding is the following:
```bash
python dnngp_runner.py \
  --batch_size [num] \
  --epoch [num] \
  --lr [num] \
  --patience [num] \
  --dropout1 [num] \
  --dropout2 [num] \
  --SNP [your omics-data file] \
  --pheno [your phenotype data file]
```
Of particular note is the [`run.py`](./DNNGP/run.py). This script is used to get results in batches by adjusting different hyperparameters and inputs.

## 🔍 Data

- [tomato332](#./DNNGP-master/example-data/tomato332)
- [wheat599](#./DNNGP-master/example-data/wheat599)
- [maize1404](#./DNNGP-master/example-data/maize1404)
- [wheat2000](#./DNNGP-master/example-data/wheat2000)

## Maintainers

[@Kelin Wang](wangkelin_2022@163.com)

[@Huihui Li](lihuihui@caas.cn)

## 👥 Contacts

[Kelin Wang](wangkelin_2022@163.com)（wangkelin_2022@163.com）

[Huihui Li](lihuihui@caas.cn)（lihuihui@caas.cn）


## 📘 License

[DNNGP](LICENSE) © Kelin Wang, Huihui Li