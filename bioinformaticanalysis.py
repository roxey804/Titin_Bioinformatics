#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:36:55 2019

@author: Rox
"""

import csv
import collections
import time

seqs = {}  # new dictionary
with open("Fn3alignment.txt", 'r') as readin:
    fn3seqs = readin.read()
    rows = fn3seqs.split('\n')
    for row in rows:
        domain_name, sequence = row.split()  # split by empty spaces
        seqs[domain_name] = sequence


# This function prints out a list of all the Keys which are the domain numbers
def get_domains():
    for key, value in seqs.items():
        print(key.title())


def get_all_res(resnumber):
    '''returns residue at position given by resnumber for all domains'''
    resnames = {}
    for dom, seq in seqs.items():
        resnames[dom] = seq[resnumber]
    return resnames


def countres(position):
    # position=input("input position number: ")
    residuelist = []
    print("you selected position number {}:".format(position))
    for dom, seq in seqs.items():
        residuelist.append(seq[int(position)])
    answer = collections.Counter(residuelist)
    print(answer)
    for key, val in answer.most_common():
        print(val, "out of 132 domains contain ", key, "residues at position", position)
        return percentagecalculator(val, key)


def percentagecalculator(val, key):
    percentage = ((val / 132) * 100)
    percent_2dp = round(percentage, 2)
    print(percent_2dp, "%")
    return conservation(percent_2dp, key)


#    print(mylist2[1])


def conservation(percent_2dp, key):
    conservedlist = []
    if percent_2dp >= 75:
        print("higher than 75% conserved residue")
        conservedlist.append(key)
        print(key)
    else:
        print("less than 75% conserved")


def main():
    for i, thing in enumerate(seqs):
        countres(i)


if __name__ == "__main__":
    main()

