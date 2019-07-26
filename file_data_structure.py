import os 
import json 
import shutil
import re


all_files = [f for f in os.listdir() if  os.path.isfile(f)]

def has_fastq_in_name(string):
    if (string.find("fastq") == -1):
        return 0
    else:
        return 1

all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))

all_fastq_names = []

for a_fastq in all_fastq_files:
    all_fastq_names.append(a_fastq.split(".")[0])

#print(sorted(all_fastq_names))
#print(len(all_fastq_names))

all_genome_names = []

for a_fastq in all_fastq_files:
    all_genome_names.append(a_fastq.split(".")[0].split("_")[0])

all_genome_names = set(all_genome_names)

#regex = re.compile(r(set(all_genome_names))[0])
#print(list(filter(regex.search, all_fastq_names)))


def check_genome(genome_name, a_genome):
    if genome_name == a_genome.split(".")[0].split("_")[0]:
        #print(a_genome)
        return True
    
#for a_genome in all_fastq_files:
    #check_genome('SRR650226', a_genome)
    #check_genome('SRR017356', a_genome)

genome_pairs = []

for a_genome in all_genome_names:
    #print("<< " + a_genome + " >>")
    files_per_genome = list(filter(lambda x: check_genome(a_genome, x), all_fastq_files))
    genome_pairs.append(files_per_genome)


#print(genome_pairs)

total = 0
for a_pair in genome_pairs:
    print(a_pair)
    #print(len(a_pair))
    total += len(a_pair)

#print(total)


