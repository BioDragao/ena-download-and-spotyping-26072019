import os
import shutil

# # TODO create pairs of genomes based on same first name

# all_files = [f for f in os.listdir() if  os.path.isfile(f)]

# def has_fastq_in_name(string):
#     if (string.find("fastq") == -1):
#         #print("NO")
#         return 0
#     else:
#         #print("YES")
#         return 1

# all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))

genome_pairs = [

                ]


def run_spotyping(a_pair):

    genome_1 = a_pair[0]

    genome_2 = a_pair[1]

    output = (a_pair[0].split(".")[0]).split("_")[0] + "_spo.out"

    # NOTE the usage of spotyping command
    # python2.7 SpoTyping.py ./118_cat_R1.fastq ./118_cat_R2.fastq

    cmd =  "vagrant ssh -c \"cd /vagrant/mozambique_genomes/maf_endgame/lab/ && " + \
           "python2.7 SpoTyping.py " + \
            genome_1 + \
            " " + \
            genome_2 + \
            " -o " + \
            output + \
            "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")


for a_pair in genome_pairs:
    run_spotyping(a_pair)

print("DONE")
