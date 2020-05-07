exec(open("source.py").read())

(bim, fam, bed) = read_plink(rsID)

def PLINKtoLD(x, n):
    """
    LD from plink data
  
    Creation of a linkage disequilibrium matrix from a plink genotype matrix
  
    Parameters: 
    x (ndarray): genotype matrix
    n (int): sample size
  
    Returns: 
    ndarray: linkage disequilibrium matrix
    """
    if ndim