#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: dna2aa.py
Author: Stein Acker
Date: 16-10-2020

Description:
    When given a protein FASTA file, this program will calculate the raw 
    abundance of each amino acid in the FASTA file.

List of user-defined functions:
    fasta_to_line(fasta): When given a FASTA file in Python list format, this
    function returns a fully uppercase single-line string containing only the
    sequences.

List of non-standard modules:
    sys: Allows python script to easily interface with bash commands in a
    terminal.

Procedure:
    1. Create a list of single-letter amino acid codes.
    2. Turn all amino acids into a single string.
    3. Iterate through the amino acid list and sum up the counts of these
    amino acids in the sequences.
    4. Subtract the sum of identified amino acids from the sum of total amino
    acids to identify number of 'X' amino acids.
    5. Return a text file containing the raw abundances of each amino acid.

Usage:
    ./amino_count.py fasta.faa output.txt
"""

#%% Setup

import sys
import re
input_file = sys.argv[1]
output_file = sys.argv[2]

#%% Step 1: Create a list of single-letter amino acid codes.

aminoacids = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S',
             'T','V','W','Y']

#%% Step 2: Turn all amino acids into a single string.

def fasta_to_line(fasta):
    #Create an empty string for all amino acids
    all_amino = ''
    for line in fasta:
        #If the current line is not a header...
        if line.startswith('>') == False:
            #Strip it of newlines and add it to all_amino.
            line = line.strip('\n')
            all_amino += line
    #Convert all characters in all_amino to uppercase if they are not already
    #uppercase.
    all_amino = all_amino.upper()
    #Return all_amino as the result of this function.
    return all_amino

#Run this function on the inputted FASTA file.
with open(input_file) as f:
    protein = fasta_to_line(f)

#%% Step 3: Iterate through the amino acid list and sum up the counts of these
#   amino acids in the sequences.

#Create an empty dictionary for amino acid counts
amino_counts = dict()

#Put the sums of amino acid residues in this new dictionary
for amino in aminoacids:
    amino_counts[amino] = len(re.findall(amino, protein))

#%% Step 4: Subtract the sum of identified amino acids from the sum of total amino
#   acids to identify number of 'X' amino acids.

amino_counts['X'] = len(protein) - sum(amino_counts.values())

#%% Step 5: Return a text file containing the raw abundances of each amino acid.

with open(output_file,'w') as o:
    for amino in aminoacids:
        o.write('{0} {1}\n'.format(amino, amino_counts[amino]))
    o.write('X ' + str(amino_counts['X']))
