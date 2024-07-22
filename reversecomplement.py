def rc(dna):
    complement = {'A':'T','T':'A','C':'G','G':'C'}

    comp_str = ''.join(complement[base] for base in dna)

    re_comp_str = comp_str[::-1]

    return re_comp_str


def rdff(fp):
    with open(fp, 'r') as file:

        dna_seq = ''.join(line.strip() for line in file)

    return dna_seq


ifp = 'z.txt'

dna_seq = rdff(ifp)

re_comp_str = rc(dna_seq)

print(re_comp_str)
