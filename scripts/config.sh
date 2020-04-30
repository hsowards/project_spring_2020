#set each of these variables to reflect your region of interest
chr= #chr
start= #starting bp
end= #ending bp
rsID= #rsID for filenames
dir= #your project directory

echo "The configured region is on chr $chr, starting at position $start, and ending at position $end. $rsID.bed/.fam/.bim and MEL_all_RSQ0.5_${chr}_for_TWAS.txt.gz are now available in $dir."