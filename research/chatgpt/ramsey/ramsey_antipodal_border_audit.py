"""Exact symmetric vs antipodal product predictor comparison, unordered pairs only."""
import csv
from pathlib import Path
from itertools import combinations
from collections import Counter


def main():
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:
        h,*rows=csv.reader(f)
    n=len(rows); pairs=list(combinations(range(n),2));labels=list(map(int,h[1:]))
    pos=[sum(1<<j for j in range(n) if row[j+1]=='1') for row in rows]
    baseline=sum(bool(pos[i]>>j&1) for i,j in pairs)
    best={};ties=Counter();full=(1<<n)-1;cut=0;sep=0
    for t in range(1<<(n-1)):
        if t:
            bit=(t&-t)<<1;i=bit.bit_length()-1;delta=pos[i].bit_count()-2*(pos[i]&cut).bit_count();sep+=(-delta if cut&bit else delta);cut^=bit
        k=min(cut.bit_count(),n-cut.bit_count());loss=baseline+k*(n-k)-2*sep
        if k not in best or loss<best[k]:best[k]=loss;ties[k]=1
        elif loss==best[k]:ties[k]+=1
    print('cut size, best loss, ties:',[(k,best[k],ties[k]) for k in sorted(best)])
    assert baseline==best[0] and min(best.values())==baseline

if __name__=='__main__':main()
