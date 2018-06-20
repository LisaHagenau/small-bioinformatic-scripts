# parse fasta file into dictionary, removing linebreaks in the sequence (common occurence)
# uses inherent property of dictionary: only unique keys allowed! Duplicate names simply lead to updated values
# this keeps the last non-unique sequence and deletes duplicate names

def parseFasta(file):
    with open(file) as fasta:
        fastalist = []
        for line in fasta:
            if line.startswith(">"):
                fastalist.append("\n"+line)
            else:
                fastalist.append("" + line.strip())
    fastalist = ''.join(fastalist)[1:].split('\n')
    seq = dict(zip(fastalist[::2], fastalist[1::2]))
    return(seq)

with open("fasta_out.fa", "w") as out:
    result = parseFasta("fasta_in.fa")
    for name, seq in result.items():
        out.write(name+"\n"+seq+"\n")
