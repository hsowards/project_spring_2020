def test_PLINKtoLD():
    assert bed.shape[0] == n or bed.shape[1] == n, "One of the dimensions of the bed file should be n"
    
def test1_PLINKtoLD():
    assert dtype(ld) == "ndarray", "The LD matrix should be an ndarray"
    
def test_eig_check():
    assert dtype(eig) == "array", "The eigenvalues should be in an array"

