#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:37:30 2020

@author: steinacker
"""
import sys
# Step 1: Create dictionary with mRNA codons as keys and amino acid 1-letter 
# codes as values

Translator = {
    'AAA':'K',
    'AAU':'N',
    'AUA':'I',
    'UAA':'*',
    'AAC':'N',
    'ACA':'T',
    'CAA':'Q',
    'AAG':'K',
    'AGA':'R',
    'GAA':'E',
    'UUU':'F',
    'UUA':'L',
    'UAU':'Y',
    'AUU':'I',
    'UUC':'F',
    'UCU':'S',
    'CUU':'L',
    'UUG':'L',
    'UGU':'C',
    'GUU':'V',
    'CCC':'P',
    'CCA':'P',
    'CAC':'H',
    'ACC':'T',
    'CCU':'P',
    'CUC':'L',
    'UCC':'S',
    'CCG':'P',
    'CGC':'R',
    'GCC':'A',
    'GGG':'G',
    'GGA':'G',
    'GAG':'E',
    'AGG':'R',
    'GGC':'G',
    'GCG':'A',
    'CGG':'R',
    'GGU':'G',
    'GUG':'V',
    'UGG':'W',
    'ACG':'T',
    'ACU':'T',
    'CAG':'Q',
    'CAU':'H',
    'AUG':'M',
    'AUC':'I',
    'UAG':'*',
    'UAC':'Y',
    'CUG':'L',
    'CUA':'L',
    'UCG':'S',
    'UCA':'S',
    'GUC':'V',
    'GUA':'V',
    'UGC':'C',
    'UGA':'*',
    'CGU':'R',
    'CGA':'R',
    'GCU':'A',
    'GCA':'A',
    'AGU':'S',
    'AGC':'S',
    'GAU':'D',
    'GAC':'D'
    }


# Step 2: Convert all Ts to Us in the DNA sequence of interest
rnaFasta = []
newFasta = []

fasta = sys.argv[1]
output = sys.argv[2]
if 'a' in locals():
    del a
with open(fasta) as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith('>') == False:
            line = line.upper()
            line = line.replace('T','U')
        rnaFasta.append(line)

for line in rnaFasta:
    if line.startswith('>') == False and 'a' not in locals():
        a = line
    elif line.startswith('>') == False and 'a' in locals():
        a = a + line
    elif line.startswith('>') == True and 'a' in locals():
        newFasta.append(a)
        newFasta.append(line)
        del a
    else:
        newFasta.append(line)

proteinFasta = []

for line in newFasta:
    if line.startswith('>') == False:
        line = ','.join([line[i:i+3] for i in range(0, len(line),3)])
        line = line.split(',')
        protein = ''
        for codon in line:
            if len(codon) == 3 and codon in Translator.keys():
                protein += Translator[codon]
            elif len(codon) == 3:
                protein += 'X'
        proteinFasta.append(protein)
    else:
        proteinFasta.append(line)
        
with open(output,'w') as o:
    for line in proteinFasta:
        o.write(line + '\n')

# Step 3: Strip off all unnecessary newlines from FASTA

# Step 4: Convert each sequence to a list with codons as units

# Step 5: Create new list

# Step 6: Use the dictionary to convert each 