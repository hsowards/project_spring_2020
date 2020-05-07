exec(open("source.py").read())

prefix = dir + "/" + rsID
(bim, fam, bed) = read_plink(prefix)

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

ld = PLINKtoLD(bed, n)

def eig_check(ld):
    """
    Check eignenvalues of LD matrix
  
    Check that all eignenvalues of the LD matrix are > -1E-10, meaning the matrix is positive semi-definite
  
    Parameters: 
    ld (ndarray): linkage disequilibrium matrix
  
    Returns: 
    boolean: True if matrix is positive semi-definite, false if not
    """
    eig <- np.linalg.eigvals(ld)
    check <- np.all(np.linalg.eigvals(x) > -1e-10)
    print(check)
    
eig_check(ld)

def write_ld(ld, rsID):
    """
    Write LD matrix
  
    Writes out LD matrix, after checking that it's positive semi-definite, as a comma delimited file named rsid.ld
    
    Parameters: 
    ld (ndarray): linkage disequilibrium matrix
    """
    if eig_check(ld) == True:
        filename = dir + "/" + rsID + ".ld"
        np.savetext(filename, ld, delimeter=",")
    else :
        print("LD matrix is not positive semi-definite")
        
write_ld(ld)