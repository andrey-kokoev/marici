"""Catalogue-assisted obstruction at order 36, independent of circle symmetry.
Optional argument: path to decompressed r38_27.g6. Otherwise fetch McKay catalogue.
"""
from collections import Counter
from pathlib import Path
from urllib.request import urlopen
from gzip import decompress
import sys

def audit(raw):
    counts=Counter()
    for s in raw.splitlines():
        assert len(s)==60 and s[0]==90 and all(63<=b<=126 for b in s[1:]);assert (s[-1]-63)&7==0
        counts[sum((b-63).bit_count() for b in s[1:])]+=1
    assert sum(counts.values())==477142
    # Necessarily 8-regular, by R(3,8)=28 and alpha <= 8. Positive neighbors
    # of a vertex form an independent 8-set, leaving 27 negative neighbors.
    cross=8*(8-1);required=(27*8-cross)//2
    print('graphs:',sum(counts.values()),'minimum edges:',min(counts),'attaining minimum:',counts[min(counts)],'required:',required)
    assert min(counts)>required
if __name__=='__main__':
    audit(Path(sys.argv[1]).read_bytes() if len(sys.argv)>1 else decompress(urlopen('https://users.cecs.anu.edu.au/~bdm/data/r38_27.g6.gz',timeout=30).read()))
