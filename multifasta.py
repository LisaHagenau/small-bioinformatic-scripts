# make multifasta file from seq files 
import os
# create empty lists for the names and sequences
seqname = []
seqs= []

# read each file in dictionary with .seq extension, append the filename to a list with a leading > and the sequence
# without linebreaks to another list
for file in os.listdir('.'):
    if ".seq" in file:
            seqname.append(">"+file)
            with open(file) as f:
                lines = [line.rstrip() for line in f.readlines()]
                seqs.append("".join(lines))

# zips the 2 lists together, alternating between filename and content
# the more simple 'list(zip(a,b))' would create a list of tuples which doesn't work with the write command
# basically, this command unpacks every tuple (pair) in the list created by zip, and replaces it with
# the items it contains > flattening the list
multifasta = [item for pair in zip(seqname, seqs) for item in pair]

# writes the zipped list to a file with fasta extension
with open("fasta.fa", "w") as fa:
    for item in multifasta:
        fa.write("%s\n" % item)

# another possibility would be to just use fa.read() to read out the entire content of the seq file, however, this
# would not get rid of linebreaks, which are annoying to deal with later on