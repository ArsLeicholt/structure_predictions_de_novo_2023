def count_amino_acids(fasta_file):
    with open(fasta_file, 'r') as f:
        header = ""
        count = 0
        for line in f:
            if line.startswith(">"):
                if header:
                    print(f"{header}: {count} amino acids")
                header = line.strip()[1:]
                count = 0
            else:
                count += len(line.strip())
        print(f"{header}: {count} amino acids")

fasta_file = "path/to/fasta.fa"
count_amino_acids(fasta_file)
