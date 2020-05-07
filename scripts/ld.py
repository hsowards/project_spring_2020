exec(open("source.py").read())
import RSR #package

#reads in data, pulling from config file
prefix = dir + "/" + rsID
(bim, fam, bed) = read_plink(prefix)

#creates LD matrix from bed file
ld = PLINKtoLD(bed, n)
    
#checks that matrix is positive semi definite
eig_check(ld)
        
#writes out LD matrix
write_ld(ld)