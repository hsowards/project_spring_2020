import numpy as np

def PLINKtoLD(x, n):
    """
    LD from plink data
  
    Creation of a linkage disequilibrium matrix from a plink genotype matrix. Checks that SNPs 
  
    Parameters: 
    x (ndarray): genotype matrix
    n (int): sample size
  
    Returns: 
    ndarray: linkage disequilibrium matrix
    """
    if bed.shape[1] == n & bed.shape[0] != n: #this would indicate snps are rows, the dataset needs to be transposed
        x = np.asarray(x)
        x = np.transpose(x) #transpose
    else:
        x = np.asarray(x)
    #setting nas as column mean
    col_mean = np.nanmean(x, axis = 0)
    inds = np.where(np.isnan(x)) 
    x[inds] = np.take(col_mean, inds[1])
    #standardizing the matrix (zscore)
    x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
    #creating the ld matrix
    ld = np.transpose(x) @ (x/n)