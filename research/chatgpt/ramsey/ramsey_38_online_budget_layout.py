"""Controlled on/off benchmark: fixed row memberships, free permutations in each row.
Normalize first-row order under affine relabeling of F2^3 (extra bits arbitrary).
Report every layout accepted, not merely the first. Check every acceptance on all pairs.
"""
import json
from pathlib import Path
from itertools import combinations, combinations_with_replacement, permutations
from functools import lru_cache
from time import perf_counter
from ramsey_budgeted_separator import Separator,verify_decoder

free=(3,5,6,7);ps=[q for q in combinations(range(8),4) if q[0]^q[1]^q[2]^q[3]==0];vec=lambda q:sum(1<<i for i,p in enumerate(free) if p in q)
sep=Separator(4,map(vec,ps));bydepth=[[(a,b,c,1<<sep.ds.index(vec((a,b,c,d)))) for a,b,c,d in ps if d==j] for j in range(8)]

def run(A,online):
    start=perf_counter();edge=lambda i,j:A[i]>>j&1
    cols=[(x,y,z) for x in range(8) for y in range(8,16) for z in range(16,24)];diag=[tuple(edge(t[i],t[j]) for i,j in combinations(range(3),2)) for t in cols];sig={};byfirst=[[] for _ in range(8)]
    for i,t in enumerate(cols):
        byfirst[t[0]].append(i)
        for j,s in enumerate(cols[:i]):
            if diag[i]!=diag[j] or any(t[k]==s[k] for k in range(3)) or any(edge(t[k],s[l])!=edge(s[k],t[l]) for k,l in combinations(range(3),2)):continue
            sig[i,j]=sig[j,i]=sum(edge(t[k],s[l])<<b for b,(k,l) in enumerate(combinations_with_replacement(range(3),2)))
    nodes=leaves=early=accepted=0; path=[]
    def dfs(m,unused):
        nonlocal nodes,leaves,early,accepted
        nodes+=1;j=len(path)
        if j==8:
            leaves+=1;h=sep.build(m,2)
            if h is not None:
                order=[cols[v][i] for i in range(3) for v in path];new=[sum(edge(x,y)<<k for k,y in enumerate(order)) for x in order];verify_decoder(new,h);accepted+=1
            return
        # Inputs 0,1,2 are affinely independent; first vertex outside their plane is at 4.
        xs=[min(unused)] if j in (0,1,2,4) else sorted(unused)
        for x in xs:
            for v in byfirst[x]:
                if any((v,w) not in sig for w in path):continue
                mask=m
                for a,b,c,bit in bydepth[j]:
                    p,q,r=path[a],path[b],path[c]
                    if sig[p,q]!=sig[r,v] or sig[p,r]!=sig[q,v] or sig[p,v]!=sig[q,r]:mask|=bit
                if online and j<7 and sep.build(mask,2) is None:early+=1;continue
                path.append(v);dfs(mask,unused-{x});path.pop()
    dfs(0,set(range(8)));return nodes,leaves,early,accepted,round(perf_counter()-start,3)
if __name__=='__main__':
    for f in ('5bit_26','6bit_27_from_catalogue'):
        A=json.loads(Path(__file__).with_name('ramsey_38_cell_'+f+'.json').read_text())['rows'];a=run(A,False);b=run(A,True);assert a[3]==b[3];print(f,'nodes/full layouts/early prunes/accepted/seconds: off',a,'on',b,flush=True)
