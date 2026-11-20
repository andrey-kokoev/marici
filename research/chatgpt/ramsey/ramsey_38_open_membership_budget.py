"""Anchor the specified initial columns; choose the remaining ordered triples from all remaining addresses,
including old border addresses. Compare exactly the same completions with and without early budget checks."""
from itertools import permutations,combinations,combinations_with_replacement
from collections import Counter
from pathlib import Path
from time import perf_counter
import json
from ramsey_38_online_budget_layout import bydepth,sep,verify_decoder

def audit(A,anchor_count):
    clock=perf_counter();e=lambda u,v:A[u]>>v&1;n=len(A);rows=range(3);rp=list(combinations(rows,2));half=list(combinations_with_replacement(rows,2));anchors=[(i,i+8,i+16) for i in range(anchor_count)]
    def diagonal(t):return tuple(e(t[i],t[j]) for i,j in rp)
    def sig(t,u):
        if set(t)&set(u) or any(e(t[i],u[j])!=e(u[i],t[j]) for i,j in rp):return -1
        return sum(e(t[i],u[j])<<b for b,(i,j) in enumerate(half))
    pattern=diagonal(anchors[0]);assert all(diagonal(x)==pattern for x in anchors);available=set(range(n))-set(sum(anchors,()));cols=anchors+[t for t in permutations(sorted(available),3) if diagonal(t)==pattern and all(sig(a,t)>=0 for a in anchors)]
    N=len(cols);S=[[sig(t,u) for u in cols] for t in cols];neighbors=[{j for j,x in enumerate(s) if x>=0} for s in S]; setup=perf_counter()-clock
    def update(m,t,v):
        for i,j,k,b in bydepth[len(t)]:
            x,y,z=t[i],t[j],t[k]
            if S[x][y]!=S[z][v] or S[x][z]!=S[y][v] or S[x][v]!=S[y][z]:m|=b
        return m
    def run(early,look=False):
        clock=perf_counter();nodes=Counter();hits=set();cuts=Counter();reasons=Counter();updates=0
        def dfs(t,p,m,prepared=None):
            nonlocal updates
            nodes[len(t)]+=1
            if len(t)==8:
                h=sep.build(m,2)
                if h is not None:
                    order=tuple(cols[u][i] for i in rows for u in t);hits.add(order);verify_decoder([sum(e(x,y)<<j for j,y in enumerate(order)) for x in order],h)
                return
            for v in (p if prepared is None else prepared):
                if prepared is None:q=update(m,t,v);updates+=1
                else:q=prepared[v]
                depth=len(t)+1
                if early and depth<8 and sep.build(q,2) is None:cuts[depth]+=1;continue
                after=p&neighbors[v];tt=t+(v,)
                if look and depth<8:
                    if not after:reasons[depth,'structural']+=1;continue
                    viable={}
                    for w in after:
                        z=update(q,tt,w);updates+=1
                        if sep.build(z,2) is not None:viable[w]=z
                    if not viable:reasons[depth,'joint budget']+=1;continue
                    # Filter next choices, but keep the full pool for later positions.
                    dfs(tt,after,q,viable)
                else:dfs(tt,after,q)
        t=tuple(range(anchor_count));mask=0
        for i,v in enumerate(t):mask=update(mask,t[:i],v)
        dfs(t,set(range(anchor_count,N)),mask);return nodes,hits,cuts,perf_counter()-clock,reasons,updates
    a=run(False);b=run(True);assert a[1]==b[1];members={tuple(tuple(sorted(order[8*i:8*i+8])) for i in rows) for order in a[1]};print(n,'anchors',anchor_count,'eligible new triples',N-anchor_count,'shared setup seconds',round(setup,3),'accepted',len(b[1]),'distinct accepted row memberships',len(members));
    c=run(True,True);assert a[1]==c[1]
    for tag,r in [('off',a),('on',b),('pair',c)]:print(tag,'nodes',sorted(r[0].items()),'early rejections',sorted(r[2].items()),'unsupported choices',sorted(r[4].items()),'mask updates',r[5],'seconds',round(r[3],4))
if __name__=='__main__':
    for k in (4,3,2):
        for f in ('5bit_26','6bit_27_from_catalogue'):audit(json.loads(Path(__file__).with_name('ramsey_38_cell_'+f+'.json').read_text())['rows'],k)
