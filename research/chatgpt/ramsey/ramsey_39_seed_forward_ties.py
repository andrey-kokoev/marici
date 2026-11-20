"""Host-free forward search from the published 27-vertex induced seed."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
seed='ZsaCC@?CGP??@BGD?KWCxCh?AH@Ac@`?hGA[GCIAYGGmH??B_OpU__?Ci@?G'
bits=''.join(f'{ord(c)-63:06b}' for c in seed[1:]);I=[0]
for j in range(27):
    p=sum(1<<i for i in range(j) if bits[j*(j-1)//2+i]=='1');assert p in I
    I += [s|1<<j for s in I if not p&s]
# Once the initial legal borders are known, extend each with both signs and
# filter precisely the new forbidden sets through the last vertex.
def run(n,opts,sevens):
    if not opts:return Counter({n:1}),Fraction(n==35)
    nexts=[]
    for p in opts:
        miss=[s for s in sevens if not s&p];child=[];score=0
        for q in opts:
            plus=not(p&q);minus=all(s&q for s in miss)
            if plus:child.append(q|1<<n)
            if minus:child.append(q)
            score+=bool(plus or minus)
        nexts.append((score,p,child))
    best=max(s for s,_,_ in nexts);out=Counter();prob=0;num=0
    for score,p,child in nexts:
        if score!=best:continue
        # Track old independent sets of sizes 0..7 to update size seven.
        fam=levels[n];levels[n+1]=[fam[0]]+[fam[k]+[s|1<<n for s in fam[k-1] if not s&p] for k in range(1,8)]
        h,f=run(n+1,child,levels[n+1][7]);out.update(h);prob+=f;num+=1
    return out,prob/num
if __name__=='__main__':
    assert max(s.bit_count() for s in I)<=8
    levels={27:[[s for s in I if s.bit_count()==k] for k in range(8)]};eight=[s for s in I if s.bit_count()==8];opts=[p for p in I if all(p&s for s in eight)]
    print(run(27,opts,levels[27][7]))
