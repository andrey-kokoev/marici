"""Test original R(3,7) output condition on every short-cycle filling, not just Hall feasibility. No completion is selected by this test."""
from itertools import combinations
from ramsey_strip_unbiased_three_constraints import selected,allms,ms
from ramsey_strip_matching_restart import P,T

def check(m):
 removed={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in m}
 red={(0,1+i) for i in range(6)}|{(1+i,7+j) for j,d in enumerate(P) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if set(P[i]).isdisjoint(P[j]) and (i,j) not in removed}
 nbr=[0]*22
 for i,j in red:nbr[i]|=1<<j;nbr[j]|=1<<i
 triangles=sum(bool(nbr[a]>>b&1 and nbr[b]>>c&1 and nbr[a]>>c&1) for a,b,c in combinations(range(22),3))
 def independent(mask,k):
    if not k:return 1
    if mask.bit_count()<k:return 0
    ans=0
    while mask:
        bit=mask&-mask;mask^=bit;i=bit.bit_length()-1;ans+=independent(mask&~nbr[i],k-1)
    return ans
 return len(red),triangles,independent((1<<22)-1,7)
for a,b in selected:
 result=[check(allms[i]) for i in (a,b)];print('accumulated target',set(ms)=={allms[a],allms[b]},'(red edges, red triangles, blue sevens)',result);assert result==[(66,0,0)]*2
