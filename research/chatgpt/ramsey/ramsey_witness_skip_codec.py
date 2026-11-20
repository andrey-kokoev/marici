"""Lossless triangle-free codec. Omit a zero if earlier positive bits force it."""
import csv
from pathlib import Path
from itertools import combinations


def stream(n, order, source=None, payload=None):
    rows=[0]*n;out=[];skips=0;it=iter(payload or ())
    for i,j in order:
        if rows[i]&rows[j]:
            bit=0;skips+=1
            if source is not None:assert source[i][j]==0
        else:
            bit=source[i][j] if source is not None else next(it);out.append(bit)
        if bit:rows[i]|=1<<j;rows[j]|=1<<i
    assert next(it,None) is None
    return rows,out,skips

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:
        header,*data=csv.reader(f)
    M=[list(map(int,r[1:])) for r in data];n=len(M);target=[sum(b<<j for j,b in enumerate(r)) for r in M];labels=list(map(int,header[1:]));pairs=list(combinations(range(n),2))
    for name,order in [('balanced rows',pairs),('balanced address arrival',sorted(pairs,key=lambda t:(t[1],t[0]))),('original label rows',sorted(pairs,key=lambda t:sorted(labels[i] for i in t)))]:
        _,bits,k=stream(n,order,M);rec,_,_=stream(n,order,payload=bits);assert rec==target
        print(name,'emitted',len(bits),'inferred',k)
