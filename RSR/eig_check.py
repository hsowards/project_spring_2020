import numpy as np

def eig_check(ld):
    """
    Check eignenvalues of LD matrix
  
    Check that all eignenvalues of the LD matrix are > -1E-10, meaning the matrix is positive semi-definite
  
    Parameters: 
    ld (ndarray): linkage disequilibrium matrix
  
    Returns: 
    boolean: True if matrix is positive semi-definite, false if not
    """
    eig = np.linalg.eigvals(ld) #taking the eigenvalues of the ld matrix
    check = np.all(np.linalg.eigvals(x) > -1e-10) #checking that the values are all above -1e-10
    print(check) #prints boolean