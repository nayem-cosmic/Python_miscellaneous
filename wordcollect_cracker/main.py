#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:46:54 2019

@author: cosmic
"""

import json
from itertools import permutations

# Read dictionary
words_filename = 'words_dictionary.json'
with open(words_filename, 'r') as f:
    words_dict = json.load(f)

# Inputs
print('Crack Word collect!')
letter_lst = input('Enter letters: ')
n = int(input('Cracked word letter count: '))

possible_word_lst_ = list(permutations(letter_lst, n))
possible_word_lst = [''.join(l_lst) for l_lst in possible_word_lst_]

# Find words in dictionary
cracked_word_lst = []
for possible_word in possible_word_lst:
    try:
        if words_dict[possible_word] == 1:
            cracked_word_lst.append(possible_word)
    except:
        pass

print('Here are the words!', cracked_word_lst)
