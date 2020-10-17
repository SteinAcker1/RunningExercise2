# -*- coding: utf-8 -*-
"""
@author: Meghana Balasubramanian
Script for running exercise-2, Part-1:
    This script aims to calculate the alignment scores for given alignments 
    and also provides an option to produce a rough alignment score for 
    non-aligned sequences.
    transition= a<->g or c<->t -1
    transversion= a<->c,t or c<->g,a

Changes to be made:
    -commenting; initial guide for usage;
    -use sys.argv
    -replace scoring loops with function
    -remove sequences.append() and sequence_ID.append()

Note:The score.fna file provided in the example makes use of only 2 sequences.
     The following script makes use of an example sequence. 


"""
import sys
import re
import itertools
# fasta= sys.argv[0]
fasta='score.fna'
with open(fasta) as seq, open("output.txt", "w") as output:
    seq_lines=seq.read() #print(seq_lines) #the sequence is in one line
    seq_lines=seq_lines.replace('\n','')
    seq_list= re.split('(>.*?\d)', seq_lines)
    sequence_ID = seq_list[1::2] #list of seq id's
    sequences= seq_list[2::2] #you have the sequences in the list
    
    #just an example for when there are 3 sequences
    sequence_ID.append(">id3")
    sequences.append("ATCTGGATCG---TCGA-CGTTAGGGG--------CGTA")
    

    for seq1, seq2 in itertools.combinations(sequences,2): #compares all elements in the list with each other only once
        score_value=0
        index1= sequences.index(seq1) #print(sequence_ID[index1])
        index2= sequences.index(seq2) #print(sequence_ID[index2])

        if len(seq1)==len(seq2): #if length is same, perform the comparison
            for n in range(0,len(seq1)-1): #make this into a function
                if seq1[n]== seq2[n] != '-':
                    # print('match')
                    score_value+= 1
                elif seq1[n]=='-' or seq2[n] == '-':                #gap
                    # print('gap')
                    score_value+= -1
                elif seq1[n] in ['A','T'] and seq2[n] in ['G','C']: #transition
                    # print('transition')
                    score_value+= -1
                elif seq1[n] in ['G','C'] and seq2[n] in ['A','T']: #transition
                    # print('transition')
                    score_value+= -1
                else:                                               #transversion
                    # print("transversion")
                    score_value+= -2
            output.write("{}-{}: Score={}".format(sequence_ID[index1], sequence_ID[index2], score_value))
        elif len(seq1)<len(seq2): #add gaps to the shorter one
            seq1= seq1+ '-'*(len(seq2)-(len(seq1)))
            for n in range(0,len(seq1)-1): #make this into a function
                if seq1[n]== seq2[n] != '-':
                    # print('match')
                    score_value+= 1
                elif seq1[n]=='-' or seq2[n] == '-':                #gap
                    # print('gap')
                    score_value+= -1
                elif seq1[n] in ['A','T'] and seq2[n] in ['G','C']: #transition
                    # print('transition')
                    score_value+= -1
                elif seq1[n] in ['G','C'] and seq2[n] in ['A','T']: #transition
                    # print('transition')
                    score_value+= -1
                else:                                               #transversion
                    # print("transversion")
                    score_value+= -2
            output.write("{}-{}: Score={}".format(sequence_ID[index1], sequence_ID[index2], score_value))

        elif len(seq1)>len(seq2):
            seq2= seq2+ '-'*(len(seq1)-(len(seq2)))
            for n in range(0,len(seq1)-1): #make this into a function
                if seq1[n]== seq2[n] != '-':
                    # print('match')
                    score_value+= 1
                elif seq1[n]=='-' or seq2[n] == '-':                #gap
                    # print('gap')
                    score_value+= -1
                elif seq1[n] in ['A','T'] and seq2[n] in ['G','C']: #transition
                    # print('transition')
                    score_value+= -1
                elif seq1[n] in ['G','C'] and seq2[n] in ['A','T']: #transition
                    # print('transition')
                    score_value+= -1
                else:                                               #transversion
                    # print("transversion")
                    score_value+= -2
            output.write("{}-{}: Score={}".format(sequence_ID[index1], sequence_ID[index2], score_value))

        
        
        
        
        
        
        
        
        
        
        
        
        
        