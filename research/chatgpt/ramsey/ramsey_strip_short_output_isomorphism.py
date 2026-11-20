"""Exact labeled-output isomorphism by backtracking, including distinguished output vertex 0 as a separate test. No graph-library dependency."""
from itertools import combinations
from ramsey_strip_unbiased_three_constraints import selected,allms
from ramsey_strip_matching_restart import P,T

def graph(m):
 removed={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in m};red={(0,1+i) for i in range(6)}|{(1+i,7+j) for j,d in enumerate(P) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if set(P[i]).isdisjoint(P[j]) and (i,j) not in removed};N=[set() for _ in range(22)]
 for i,j in red:N[i].add(j);N[j].add(i)
 return N

def iso(A,B,fixed):
 RA=[[(int(j in A[i]),len(A[i]&A[j])) for j in range(22)] for i in range(22)];RB=[[(int(j in B[i]),len(B[i]&B[j])) for j in range(22)] for i in range(22)];sig=lambda R,i:sorted(R[i]);SA=[sig(RA,i) for i in range(22)];SB=[sig(RB,i) for i in range(22)]
 def search(m):
    if len(m)==22:return m
    used=set(m.values());options=[]
    for i in range(22):
        if i in m:continue
        opts=[j for j in range(22) if j not in used and SA[i]==SB[j] and all(RA[i][a]==RB[j][b] for a,b in m.items())]
        if not opts:return None
        options.append((len(opts),i,opts))
    _,i,opts=min(options)
    for j in opts:
        ans=search(m|{i:j})
        if ans is not None:return ans
    return None
 ans=search(fixed)
 if ans:assert all({ans[j] for j in A[i]}==B[ans[i]] for i in range(22))
 return ans
G=[graph(allms[i]) for pair in selected for i in pair]
for j,B in enumerate(G):
 rooted=iso(G[0],B,{0:0});free=rooted or iso(G[0],B,{})
 print('output',j+1,'rooted iso',rooted is not None,'unrooted iso',free is not None,'root image',None if free is None else free[0])
