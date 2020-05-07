import numpy as np

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
        
