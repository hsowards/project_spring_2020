susie_output <- susieR::susie_rss(z = sumstats_clean$Z_fixed, #p vector of z scores
                                  R = R, #LD matrix
                                  L = causals, #number of causals
                                  check_z = F, #saving computation since we check PSD earlier
                                  estimate_residual_variance = T,
                                  estimate_prior_variance = F, 
                                  max_iter = 100000) 