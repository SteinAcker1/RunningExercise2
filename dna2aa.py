#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: dna2aa.py
Author: Stein Acker
Date: 15-10-2020

Description:
    When given a DNA multi-FASTA file, this script will translate the DNA 
    sequences into RNA sequences and then translate the generated RNA
    sequences into amino acid sequences, which will be printed into a new 
    multi-FASTA file. Stop codons are represented with '*' in the amino acid 
    sequence.
    
    This application can handle the input of any DNA FASTA file; the letters
    can be uppercase or lowercase. If the application comes across a codon that
    it does not recognize (for instance, CNC or AXG) then it will return an 
    error.

List of user-defined functions:
    convert_DNA_to_RNA(fasta): converts a DNA FASTA file into an RNA FASTA in
    Python list format
    collate_FASTA(fastalist): eliminates newlines from sequences in FASTA files
    in Python list format
    convert_RNA_to_protein(newFasta): converts an RNA FASTA in Python list 
    format to a protein FASTA in Python list format

List of non-standard modules:
    sys: Allows python script to easily interface with bash commands in a
    terminal.

Procedure:
    1. Create a dictionary using RNA codons as keys and amino acid single-letter
    codes as values.
    2. Convert all Ts to Us in the DNA sequence of interest to create RNA.
    3. Put the individual RNA sequences together into single-line FASTAs.
    4. Turn each RNA sequence into a list of codons and translate to protein
    by using the dictionary.
    5. Put all the pieces together and generate a protein FASTA file.

Usage:
    ./dna2aa.py sequences.fna output.faa
"""
#%% Setup

import sys

fasta = sys.argv[1]
output = sys.argv[2]


#%% Step 1: Create dictionary with RNA codons as keys and amino acid single-letter 
#   codes as values
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

#%% Step 2: Convert all Ts to Us in the DNA sequence of interest to generate RNA.

def convert_DNA_to_RNA(fasta):
    rnaFasta = []
    with open(fasta) as f:
        for line in f:
            #Eliminate all newlines from file
            line = line.strip('\n')
            #If the line is not a header, make the whole line uppercase and replace T with U
            if line.startswith('>') == False:
                line = line.upper()
                line = line.replace('T','U')
            rnaFasta.append(line)
        #An error is returned if the first line does not start with >, as would be
        #expected of a FASTA file
        if rnaFasta[0].startswith('>') == False:
            print('A valid FASTA file is required')
            sys.exit()
    return rnaFasta

#%% Step 3: Put the individual RNA sequences together into single-line FASTAs.

def collate_FASTA(fastalist):
    if 'collate' in locals():
        del collate
    newFasta = []
    for line in fastalist:
        #If the line is not a header and there is no collated line yet, equate "collate" with the line
        if line.startswith('>') == False and 'collate' not in locals():
            collate = line
        #If the line is not a header and there is a collated line, then add the line to "collate"
        elif line.startswith('>') == False and 'collate' in locals():
            collate += line
        #If the line is a header and the "collate" variable exists, then append the completed collated line and append the header right under.
        #Then, delete the "collate" variable to prepare for the next loop.
        elif line.startswith('>') == True and 'collate' in locals():
            newFasta.append(collate)
            newFasta.append(line)
            del collate
        #Otherwise (and this only applies to the first header in the file), just append the line
        else:
            newFasta.append(line)
    #After all this is done, append the last collated line to complete the FASTA
    if 'collate' in locals(): newFasta.append(collate)
    return newFasta

#%% Step 4: Turn each RNA sequence into a list of codons and translate to protein
#   by using the dictionary.

def convert_RNA_to_protein(newFasta):
    proteinFasta = []
    for line in newFasta:
        #If the line is not a header, then break it up into codons and translate into protein
        if line.startswith('>') == False:
            line = ','.join([line[i:i+3] for i in range(0, len(line),3)])
            line = line.split(',')
            protein = ''
            for codon in line:
                #If the codon is 3 bases long and in the Translator dictionary, then convert it to an amino acid
                if len(codon) == 3:
                    try:
                        protein += Translator[codon]
                    #If not, return an error
                    except KeyError:
                        print("Please ensure your input FASTA file contains only the nucleotides ACTG or ACUG and try again")
                        sys.exit()
            proteinFasta.append(protein)
        #If the line is just a header, add it to the proteinFasta without modification
        else:
            proteinFasta.append(line)
    return proteinFasta

#%% Step 5: Put all the pieces together and generate a protein FASTA file.

RNA = convert_DNA_to_RNA(fasta)
RNA_single = collate_FASTA(RNA)
Protein = convert_RNA_to_protein(RNA_single)

with open(output,'w') as o:
    for line in Protein:
        o.write(line + '\n')