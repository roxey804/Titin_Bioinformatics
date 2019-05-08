# Bioinformatics
Analysis of titin amino acid sequences using python

Titin is a giant muscle protein, the largest protein in the human body! (over 4 MDa in size). Amongst many others it comtains 132 fibronectin type 3 (Fn-3) domains, many of which have very similar amino acid sequences.

The 20 essential amino acids can be described in a one letter code:

G		Glycine		Gly									P		Proline		Pro
A		Alanine		Ala									V		Valine		Val
L		Leucine		Leu									I		Isoleucine		Ile
M		Methionine		Met						  C		Cysteine		Cys
F		Phenylalanine		Phe						Y		Tyrosine		Tyr
W		Tryptophan		Trp							H		Histidine		His
K		Lysine		Lys									R		Arginine		Arg
Q		Glutamine		Gln								N		Asparagine		Asn
E		Glutamic Acid		Glu						D		Aspartic Acid		Asp
S		Serine		Ser									T		Threonine		Thr


There are 2 files in this project:

bioinformatics.py containing the code 
fn3alignment.txt a text file containing a multiple sequence alignment (amino acid alignment) of all titin's 132 Fn-3 domains

The various functions in the python file can be run independently to perform a number of functions:

get_domains returns all the 132 Fn-3 domains

get_all_res(x) returns the amino acid (residue) at position (x) for each domain

countres looks asks the user for which position they are interested in and should return a counter which counts the numbers of amino acids by single leter code in that particular position. 

EXAMPLE: run countres() function and input 4

PROBLEM: how can I get countres to then run the percentagecalculator on the amino acid most often found in the inputted position? It seems to work for some positions but for others it selects one that only occurs e.g 4 times rather than the one that occurs more often?
