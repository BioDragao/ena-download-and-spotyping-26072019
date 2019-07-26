import os
import shutil

genome_pairs = [ 
['ERR150046_1.fastq', 'ERR150046_2.fastq'],
['ERR016863_1.fastq', 'ERR016863_2.fastq'],
['ERR841793_1.fastq', 'ERR841793_2.fastq'],
['ERR150047_1.fastq', 'ERR150047_2.fastq'],
['ERR031484_2.fastq', 'ERR031484_1.fastq'],
['ERR016868_2.fastq', 'ERR016868_1.fastq'],
['SRR650227_2.fastq', 'SRR650227_1.fastq'],
['SRR650219_1.fastq', 'SRR650219_2.fastq'],
['SRR1657059_2.fastq', 'SRR1657059_1.fastq'],
['ERR125625_2.fastq', 'ERR125625_1.fastq'],
['ERR016867_2.fastq', 'ERR016867_1.fastq'],
['SRR1792179_2.fastq', 'SRR1792179_1.fastq'],
['SRR1792144_1.fastq', 'SRR1792144_2.fastq'],
['SRR1792076_1.fastq', 'SRR1792076_2.fastq'],
['ERR841874_1.fastq', 'ERR841874_2.fastq'],
['ERR841815_2.fastq', 'ERR841815_1.fastq'],
['ERR125598_2.fastq', 'ERR125598_1.fastq'],
['ERR970412_1.fastq', 'ERR970412_2.fastq'],
['ERR125603_2.fastq', 'ERR125603_1.fastq'],
['SRR1239337_2.fastq', 'SRR1239337_1.fastq'],
['ERR125605_2.fastq', 'ERR125605_1.fastq'],
['SRR1792114_1.fastq', 'SRR1792114_2.fastq'],
['SRR1791979_2.fastq', 'SRR1791979_1.fastq'],
['ERR564262_2.fastq', 'ERR564262_1.fastq'],
['ERR125613_1.fastq', 'ERR125613_2.fastq'],
['ERR125621_2.fastq', 'ERR125621_1.fastq'],
['ERR181435_1.fastq', 'ERR181435_2.fastq'],
['ERR016865_2.fastq', 'ERR016865_1.fastq'],
['ERR125618_2.fastq', 'ERR125618_1.fastq'],
['SRR1792429_2.fastq', 'SRR1792429_1.fastq'],
['SRR1657065_1.fastq', 'SRR1657065_2.fastq'],
['ERR125626_2.fastq', 'ERR125626_1.fastq'],
['SRR5382721_2.fastq', 'SRR5382721_1.fastq'],
['ERR015582_2.fastq', 'ERR015582_1.fastq'],
['ERR125627_2.fastq', 'ERR125627_1.fastq'],
['ERR841904_2.fastq', 'ERR841904_1.fastq'],
['ERR564260_1.fastq', 'ERR564260_2.fastq'],
['SRR650221_1.fastq', 'SRR650221_2.fastq'],
['SRR1792338_1.fastq', 'SRR1792338_2.fastq'],
['ERR032133_1.fastq', 'ERR032133_2.fastq'],
['ERR564261_1.fastq', 'ERR564261_2.fastq'],
['SRR1657070_1.fastq', 'SRR1657070_2.fastq'],
['SRR1239339_1.fastq', 'SRR1239339_2.fastq'],
['SRR1657068_2.fastq', 'SRR1657068_1.fastq'],
['ERR016866_1.fastq', 'ERR016866_2.fastq'],
['ERR032132_2.fastq', 'ERR032132_1.fastq'],
['ERR125612_1.fastq', 'ERR125612_2.fastq'],
['SRR1239338_1.fastq', 'SRR1239338_2.fastq'],
['SRR1657061_1.fastq', 'SRR1657061_2.fastq'],
['ERR841877_2.fastq', 'ERR841877_1.fastq']
]


def run_spotyping(a_pair):

    genome_1 = a_pair[0]

    genome_2 = a_pair[1]

    output = (a_pair[0].split(".")[0]).split("_")[0] + "_spo.out"

    # NOTE the usage of spotyping command
    # python2.7 SpoTyping.py ./118_cat_R1.fastq ./118_cat_R2.fastq

    cmd =  "vagrant ssh -c \"cd /vagrant/ena-downloads/ena-genomes-download-26082019/2_genomes/ && " + \
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
