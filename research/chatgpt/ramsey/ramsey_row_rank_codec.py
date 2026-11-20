"""Encode a new column by its rank among the legal extensions of the decoded prefix."""
import csv
from pathlib import Path
from ramsey_blind_start_formulas import blue


def legal(rows):
    sets=blue(rows);six=[s for s in sets if s.bit_count()==6]
    return sorted(s for s in sets if all(s&t for t in six))


def process(n, M=None, stream=''):
    rows=[];pos=0;out='';counts=[]
    for i in range(n):
        opts=legal(rows);counts.append(len(opts));width=(len(opts)-1).bit_length()
        if M is not None:
            col=sum(M[i][j]<<j for j in range(i));rank=opts.index(col)
            if width:out+=format(rank,f'0{width}b')
        else:
            rank=int(stream[pos:pos+width] or '0',2);pos+=width;col=opts[rank]
        rows=[r|(((col>>j)&1)<<i) for j,r in enumerate(rows)]+[col]
    if M is None:assert pos==len(stream)
    return rows,out,counts

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));base=[list(map(int,r[1:])) for r in data]
    for name,order in [('original',sorted(range(20),key=labels.__getitem__)),('balanced',list(range(20)))]:
        M=[[base[i][j] for j in order] for i in order];rows,bits,counts=process(20,M);r,_,_=process(20,stream=bits)
        assert r==rows==[sum(b<<j for j,b in enumerate(row)) for row in M]
        print(name,len(bits),'last column options',counts[-1])
