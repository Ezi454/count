#!/usr/bin/env python3
import sys

# Loop setiap baris pada input
for line in sys.stdin:
    line = line.strip()  # Hilangkan spasi di awal/akhir baris
    words = line.split()  # Pecah baris menjadi kata-kata
    for word in words:
        print(f"{word}\t1")
