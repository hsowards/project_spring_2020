#!/bin/bash
source scripts/config.sh #sourcing the config file so that configs are used in file creation
dap-g -d_z `$rsID`_dapg_sumstats.csv -d_ld `$rsID`_dapg.ld