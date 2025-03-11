#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary untuk menyimpan jumlah kemunculan kata
word_count = defaultdict(int)

# Baca input dari standar input
for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_count[word] += int(count)

# Output hasil
for word, count in word_count.items():
    print(f"{word}\t{count}")
