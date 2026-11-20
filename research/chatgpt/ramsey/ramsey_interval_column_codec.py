"""Exact arithmetic coding of adaptive, equiprobable column choices. No width table."""
from fractions import Fraction
from pathlib import Path
import csv
from ramsey_row_rank_codec import legal


def append(rows,col):return [r|((col>>j&1)<<len(rows)) for j,r in enumerate(rows)]+[col]

def encode(M):
    base=0;den=1;rows=[]
    for i,row in enumerate(M):
        col=sum(row[j]<<j for j in range(i));opts=legal(rows)
        base=base*len(opts)+opts.index(col);den*=len(opts);rows=append(rows,col)
    # Smallest binary prefix whose entire interval lies in the final interval.
    length=(den-1).bit_length()
    while True:
        unit=1<<length;a=(base*unit+den-1)//den
        if (a+1)*den<=(base+1)*unit:return a,length
        length+=1

def decode(bits,length,n):
    rows=[];v=Fraction(2*bits+1,2<<length)
    for _ in range(n):
        opts=legal(rows);v*=len(opts);rank=int(v);rows=append(rows,opts[rank]);v-=rank
    return rows

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));base=[list(map(int,row[1:])) for row in data]
    for name,order in [('original',sorted(range(20),key=labels.__getitem__)),('balanced',list(range(20)))]:
        M=[[base[i][j] for j in order] for i in order];a,L=encode(M)
        assert decode(a,L,len(M))==[sum(v<<j for j,v in enumerate(row)) for row in M]
        print(name,L,'bits')
