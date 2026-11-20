"""Count normalized XOR label lifts via characteristic polynomial of forbidden four-column relations. Enumerate subsets only for these small examples."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
from pathlib import Path
import json

def obstructions(A,m,r):
    n=1<<m;free=[p for p in range(n) if p and p&(p-1)];D=len(free);B=set()
    for i,j in combinations(range(r),2):
        if len({(A[i*n+a]>>(j*n+a))&1 for a in range(n)})!=1 or any(((A[i*n+a]>>(j*n+b))^(A[i*n+b]>>(j*n+a)))&1 for a,b in combinations(range(n),2)):
            return D,None # Neither defect can be remedied by extra XOR bits.
    for t in combinations(range(n),4):
        a,b,c,d=t
        if a^b^c^d:continue
        def sig(a,b):return tuple(A[i*n+a]>>(j*n+b)&1 for i,j in combinations_with_replacement(range(r),2))
        if any(sig(*u)!=sig(*sorted(set(t)-set(u))) for u in combinations(t,2)):B.add(sum(1<<i for i,x in enumerate(free) if x in t))
    return D,B

def polynomial(A,m,r):
    D,B=obstructions(A,m,r)
    if B is None:return [0]*(D+1)
    coeff=Counter()
    def rec(bs,i,sign):
        if i==len(vec):coeff[D-len(bs)]+=sign;return
        rec(bs,i+1,sign);w=vec[i];nb=bs.copy()
        while w and w.bit_length() in nb:w^=nb[w.bit_length()]
        if w:nb[w.bit_length()]=w
        rec(nb,i+1,-sign)
    vec=sorted(B);rec({},0,1);return [coeff[i] for i in range(D+1)]
if __name__=='__main__':
    for f in ['4bit_25','5bit_26','6bit_26','6bit_27_from_catalogue']:
        rows=json.loads(Path(__file__).with_name('ramsey_38_cell_'+f+'.json').read_text())['rows'];c=polynomial(rows,3,3);print(f,'coefficients ascending',c,'counts at q=1,2,4,8',[sum(v*q**i for i,v in enumerate(c)) for q in (1,2,4,8)])
