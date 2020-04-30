#!/bin/bash
source config.sh #sourcing the config file so that configs are used in file creation
unzip /data/Brown_lab/vQTL/LD_reference/UKBB/transfer_1599580_files_b3b70061.zip #unzip (decompress into multiple file componenets), this and the next step must be done for plink to run
gunzip UKBB* #gunzip (decompress files)
module load plink #load plink
#running plink to pull $rdID.bim/.fam/.bed files on relevant chr:start-end region
plink --bfile UKBB_LD_bestguess_ref_panel_maf1e3_rsq_point3_HRC_SNPs_only --chr $chr --from-bp $start --to-bp $end --make-bed --out $rsID
mv -r $rsID.* $dir #moving files to indicated project directory
sumstats="MEL_all_RSQ0.5_${chr}_for_TWAS.txt.gz" #initializing filename for sumstats
mv -r /data/Brown_lab/PAINTOR/dataset/GWAS_Meta/$sumstats $dir #moving sumstats to project directory
