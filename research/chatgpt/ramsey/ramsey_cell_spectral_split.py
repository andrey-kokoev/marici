"""Exact Walsh spectrum of the collision Cayley graph; greedy bit split vs polynomial optimum."""
from fractions import Fraction
from pathlib import Path
import json
from ramsey_cell_decoder_polynomial import obstructions,polynomial

def split(D,B):
    active=set(B);trace=[];bounds=[]
    while active:
        eig,h=min((sum(1-2*((h&b).bit_count()%2) for b in active),h) for h in range(1,1<<D))
        bounds.append(1+Fraction(len(active),-eig));active={b for b in active if (h&b).bit_count()%2==0};trace.append((h,len(active)))
    return bounds,trace
if __name__=='__main__':
    for f in ['4bit_25','5bit_26','6bit_26','6bit_27_from_catalogue']:
        A=json.loads(Path(__file__).with_name('ramsey_38_cell_'+f+'.json').read_text())['rows'];D,B=obstructions(A,3,3);c=polynomial(A,3,3);opt=next(k for k in range(D+1) if sum(v*(1<<k)**i for i,v in enumerate(c))>0);bounds,trace=split(D,B);print(f,len(B),'Hoffman',bounds[0],'greedy',trace,'opt',opt)
    # Exhaust all subsets of the 14 possible plane obstructions, not necessarily arising in a legal core.
    from itertools import combinations
    import functools,operator
    free=(3,5,6,7);planes=[sum(1<<i for i,v in enumerate(free) if v in q) for q in combinations(range(8),4) if functools.reduce(operator.xor,q)==0];planes.sort();n=1<<len(planes);cuts=[sum(1<<i for i,b in enumerate(planes) if (h&b).bit_count()%2) for h in range(1,16)];opt=[0]*n;greedy=[0]*n
    for m in range(1,n):
        rem=[m&~u for u in cuts];opt[m]=1+min(opt[r] for r in rem if r!=m);g=min(rem,key=int.bit_count);greedy[m]=1+greedy[g]
    print('first-minimum-eigenvalue tie rule suboptimal:',sum(a>b for a,b in zip(greedy,opt)),'/',n)
