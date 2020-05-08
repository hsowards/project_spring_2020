library(tidyverse)
source("scripts/config.sh") #load in configs

x <- read_csv(paste0(dir, "/", rsid, "_susie.ld"))
sumstats <- read_csv(paste0(dir, "/", rsid, "_susie_sumstats.csv"))

crediblesets <- function(causals){
  susie_output <- susieR::susie_rss(z = sumstats$Z_fixed, #p vector of z scores
                                   R = x, #LD matrix
                                   L = causals, #number of causals
                                   check_z = F, #saving computation since we check PSD earlier
                                   estimate_residual_variance = T,
                                   estimate_prior_variance = F, 
                                   max_iter = 100000) #iterations based on CAVIAR
  cs <- map_df(susie_output$sets$cs, ~as.data.frame(.x), .id="susie_set")
  if (nrow(sumstats_clean) == nrow(ld_info)) {
    cs <- ld_info %>% 
      select(pos) %>% 
      rowid_to_column("row") %>% 
      inner_join(cs, by = c("row" = ".x"))
    crediblesets <- as.data.frame(susie_output$pip) %>% 
      rowid_to_column("row") %>% 
      inner_join(cs, by = "row") %>% 
      inner_join(ld_info, by = "pos") %>% 
      select(susie_set, row, `susie_output$pip`, pos, chr, id, ref, alt)
    colnames(crediblesets) <- paste(colnames(crediblesets), causals, sep = "_")
    print(crediblesets)
  }
  else{
    cs <- ld_info %>% 
      filter(pos > start & pos < end) %>% 
      select(pos) %>% 
      rowid_to_column("row") %>% 
      inner_join(cs, by = c("row" = ".x"))
    crediblesets <- as.data.frame(susie_output$pip) %>% 
      rowid_to_column("row") %>% 
      inner_join(cs, by = c("row")) %>% 
      inner_join(ld_info, by = "pos") %>% 
      select(susie_set, row, `susie_output$pip`, pos, chr, id, ref, alt) 
    colnames(crediblesets) <- paste(colnames(crediblesets), causals, sep = "_")
    print(crediblesets)
  }
}

crediblesets(causals)