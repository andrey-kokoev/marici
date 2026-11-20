"""Compare the literal marked block at entry (not just the entry vertex) with the exit block. No half-step, path transport, or endpoint symmetry used to identify a member."""
from itertools import combinations
E=list(combinations(range(1,5),2));P=list(combinations(range(6),2));T=[m for m in combinations(P,3) if len(set(sum(m,())))==6];rows=('BRNN','BNRN');B=1;Q=4
edge=lambda a,b:E.index(tuple(sorted((a,b))))
def blocks(i):
 w=rows[i];u=1+w.index('R');mark={edge(B,Q),edge(u,Q)};dst={edge(B,u),E.index(tuple(j for j,c in enumerate(w,1) if c=='N'))};return mark,dst
for i in (0,1):
 m,_=blocks(i);s={edge(B,2),edge(B,3)};entry,=[j for j,t in enumerate(T,15) if tuple(sorted(s)) in t and tuple(sorted(m)) in t]
 for j in (0,1):
    _,d=blocks(j);a=m&d;assert len(a)==(i!=j);out=d-a
    if a:
        x,=a;y,=out;assert Q in E[x] and B in E[y] and edge(B,1+rows[j].index('R'))==y
    print('entry',entry,'exit',P.index(tuple(sorted(d))),'shared mark',[E[v] for v in a],'exit remainder',[E[v] for v in sorted(out)])
