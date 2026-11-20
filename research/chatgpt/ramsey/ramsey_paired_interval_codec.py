"""Code ordered pairs of incoming addresses together; do not identify swapped labels."""
from pathlib import Path
import csv
from fractions import Fraction
from ramsey_blind_start_formulas import blue
from ramsey_interval_column_codec import append


def choices(rows):
    ss=blue(rows); six=[s for s in ss if s.bit_count()==6]; five=[s for s in ss if s.bit_count()==5]
    cols=sorted(p for p in ss if all(p&t for t in six));miss={p:sum(1<<i for i,t in enumerate(five) if not p&t) for p in cols}
    return [(p,q,b) for p in cols for q in cols for b in (0,1) if (not(p&q) if b else not(miss[p]&miss[q]))]

def run(M):
    base=0;den=1;rows=[]
    for i in range(0,len(M),2):
        opts=choices(rows);p,q=[sum(M[j][h]<<h for h in range(i)) for j in (i,i+1)];b=M[i+1][i];base=base*len(opts)+opts.index((p,q,b));den*=len(opts);rows=append(append(rows,p),q|(b<<i))
    L=(den-1).bit_length()
    while True:
        a=((base<<L)+den-1)//den
        if (a+1)*den<=((base+1)<<L):break
        L+=1
    v=Fraction(2*a+1,2<<L);out=[]
    while len(out)<len(M):
        opts=choices(out);v*=len(opts);idx=int(v);v-=idx;p,q,b=opts[idx];out=append(append(out,p),q|(b<<len(out)))
    assert rows==out==[sum(b<<j for j,b in enumerate(r)) for r in M];return L

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));base=[list(map(int,row[1:])) for row in data]
    for name,order in [('original',sorted(range(20),key=labels.__getitem__)),('balanced',list(range(20)))]:print(name,run([[base[i][j] for j in order] for i in order]),flush=True)
