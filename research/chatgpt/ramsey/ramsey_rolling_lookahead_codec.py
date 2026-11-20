"""Rolling one-column lookahead. Skip dead ends or weight by legal continuations."""
import csv
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from ramsey_paired_interval_codec import choices,append
from ramsey_row_rank_codec import legal


def table(rows,last,weighted):
    if last:return [(p,1) for p in legal(rows)]
    counts=Counter(p for p,q,b in choices(rows));return [(p,w if weighted else 1) for p,w in sorted(counts.items())]

def advance(lo,hi,items,select):
    total=sum(w for p,w in items);start=0
    for p,w in items:
        end=start+w
        if select(p,(hi-lo)*end/total+lo):
            return p,lo+(hi-lo)*start/total,lo+(hi-lo)*end/total
        start=end
    raise ValueError('no choice')

def run(M,weighted):
    rows=[];n=len(M);lo,hi=F(0),F(1)
    for i,r in enumerate(M):
        target=sum(r[j]<<j for j in range(i));p,lo,hi=advance(lo,hi,table(rows,i==n-1,weighted),lambda p,end:p==target);rows=append(rows,p)
    length=0
    while True:
        scale=1<<length;num=-((-lo.numerator*scale)//lo.denominator)
        if F(num+1,scale)<=hi:break
        length+=1
    tag=F(2*num+1,2*scale);decoded=[];lo,hi=F(0),F(1)
    for i in range(n):
        p,lo,hi=advance(lo,hi,table(decoded,i==n-1,weighted),lambda p,end:tag<end);decoded=append(decoded,p)
    assert decoded==rows==[sum(b<<j for j,b in enumerate(r)) for r in M];return length

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));base=[list(map(int,row[1:])) for row in data]
    for name,order in [('original',sorted(range(20),key=labels.__getitem__)),('balanced',list(range(20)))]:
        M=[[base[i][j] for j in order] for i in order];print(name,'prune',run(M,False),'weighted',run(M,True))
