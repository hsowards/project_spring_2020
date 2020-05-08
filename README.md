# Run SuSiE Run!
## Data processing for fine-mapping with summary statistics using SuSiE and DAP-G
### Python Project for BIOF309

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

This package aims to help process GWAS summary statistics and LD reference panel data for analysis on a selected region using the fine-mapping programs SuSiE and DAP-G. These are main goals of this package:
1. Limited to those that have access: Pull GWAS summary statistics and reference panel data 
2. Make a linkage disequilibrium (LD) matrix with the reference panel data (PLINK format)
3. Align and clean the summary stats and LD matrix
4. Fine-map the region using 2 different programs:
    - A program written in R named SuSiE
    - A program written in C++ named DAP-G

To access this repository locally, enter the following code into command line:

```
git clone https://github.com/hsowards/project_spring_2020
```

## 1. Limited to those that have access: Pull GWAS summary statistics and reference panel data
*Important Note: the instructions for this step are specific to data that **is not** publicly accessible* 

1. If you don't have biowulf access, [request it](https://hpc.nih.gov/docs/accounts.html)
2. Request access to data files (ask your PI/supervisor)
3. [Connect to Biowulf](https://hpc.nih.gov/docs/connect.html) 

Once you're connected, edit the file **scripts/config.sh** to match your region of interest. Don't forget to include the path to the project directory so that the files don't pile up in shared folders.

After your config.sh file is set up and saved, run the following script

```
sh scripts/data.sh
```

Check that your files are present, there should be a bim/fam/bed file with the rsID in your config file and a txt file with the chr number

```
source scripts/config.sh
cd $dir
ls $dir
```

## 2. Make a linkage disequilibrium (LD) matrix with the reference panel data
If you haven't yet, edit the file **scripts/config.sh** to match your region of interest and the directory where your data is.

The following functions will:
1. read in plink data, specifically the genotype matrix (X)
2. make sure that SNPs are in columns rather than rows
3. set missing genotypes to the sample mean
4. standardize the genotypes
5. compute the LD using the equation np.transpose(X) @ (X/N)
    - X is the genotype matrix
    - N is the sample size (N individuals included in the LD reference population)
    - @ is numpy's matrix multiplication symbol
6. check that the matrix is positive semi-definite (PSD)
    - Specifically checking that all eigen values are greater than -1E-10, SuSiE's threshold for PSD
7. write out the matrix as rsid.ld

```
python scripts/ld.py
```

## 3. Align and clean the summary statistics and LD matrix
The following functions hope to:
1. read in the summary statistics and new LD matrix
2. pare the datasets down to the region
3. check that ref/alt alleles are aligned between the datasets
2. check that the number of SNPs in the summary stats is the same as the LD matrix
3. if there is a mismatch of SNPs:
    - the bim file will be used to align the summary stats with the LD matrix
    - SNPs that are missing from either file will be removed
4. write out the clean summary stats and LD matrix
    - Files for analysis in SuSiE will be named rsid_susie_sumstats.csv and rsid_susie.ld
    - Files for analysis in DAP-G will be named rsid_dapg_sumstats.csv and rsid_dapg.ld

```
python scripts/processing.py
```

## 4. Fine-map the region with SuSiE
The following script will:
1. read in the summary stats and LD matrix
2. run the fine-mapping algorithm with L number of predicted causals
3. write out the credible sets produced by SuSiE as rsid_susie_L_cs.csv

```
R scripts/SuSiE.R
```

## 4. Fine-map the region with DAP-G

- The DAP-G specific files produced by processing.py will be run in DAP-G using the included script dapg.sh
- DAP-G must be compiled and run in a virtual box running ubuntu, here are the rough steps:
    1. [Download Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    2. download ubuntu desktop [here](https://ubuntu.com/download/desktop)
    2. [Follow this guide](https://brb.nci.nih.gov/seqtools/installUbuntu.html) to set up your virtual machine
    3. You can clone this repository into your virtualbox to access the config.sh and dapg.sh files but to access the data you will have to either:
        - Create a shared file between your home OS and ubuntu OR
        - Upload the data to google docs
    4. Once the data is uploaded, make sure the config.sh file is updated, you can do this from the terminal:
    ```
    nano scripts/config.sh
    ```
    5. run dapg.sh
    ```
    sh scripts/dapg.sh
    ```