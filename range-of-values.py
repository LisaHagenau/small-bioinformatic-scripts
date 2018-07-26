# find the range of values in column 3 for unique values in column 1 and the most common value in column 2

import csv

# open both files and store sequences from file1 as list
stream = open("file1.txt")
seqlist = list(stream)
seqlist = [element.strip() for element in seqlist]

stream = open("file2.txt")
reader = csv.reader(stream, delimiter="\t")

for seq in seqlist:
    # create array from column 2 and 3
    array = ([line[1:] for line in reader if seq == line[0]])
    # find and count most common element from column 2
    common = [element[0] for element in array]
    mostCommon = max(common, key=common.count)
    commonCount = common.count(mostCommon)
    # find range of values for most common element
    values = [element[1] for element in array if element[0] == mostCommon]
    # print out results
    print(seq, "\t", mostCommon, "\t", min(values), "-", max(values), "\t", commonCount)
    stream.seek(0)
