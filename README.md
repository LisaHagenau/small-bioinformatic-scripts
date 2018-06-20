# A collection of small scripts dealing with problems of a bioinformatic nature
These scripts are inspired by questions/programming challenges on online forums, e.g. biostars and r/bioinformatics. 

## multifasta.py
Creates a fasta file from files containing sequencing data (e.g. .seq files), using the filename as fasta header. Copy the script to the folder containing the sequencing files and run it. If your files have a different extension, change the file extension in line 10. Inspired by a question on r/bioinformatics. 

## questionsmark.py
This is apparently the hardest "easy" programming challenge on coderbyte.com. It checks if there are exactly 3 question marks between every pair of numbers that add up to 10. If that is the case, the output is true, otherwise, the output prints false. 

## select_columns.py
This was a question asked on the biostars forum: https://www.biostars.org/p/319990/. It finds the range of numbers in the 3rd column for unique entries in the 1st column for the most common value in the 2nd column. 

## del_duplicate_names.py
From another biostars question: https://www.biostars.org/p/321641/. The script removes duplicate names (and the respective sequence) from a fasta file, but the sequences for duplicate names are unique. Requires fasta file as input and outputs fasta file as result. 

