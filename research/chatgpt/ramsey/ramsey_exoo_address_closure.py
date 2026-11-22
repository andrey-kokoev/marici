"""Blind address-only closure. The loader discards all exterior links, sorts the exterior by signature, and gives the inference routine no parent or target-centre ID. Exact triangle and ten-set units via common red neighbours / common nonred 8-cliques. Failed-literal closure tests both hypothetical colours. Preserve open links, not just totals."""
from exoo39_symbolic_relations import edges
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

def chart(root):
    E=edges();A=sorted(v for v in range(39) if tuple(sorted((root,v))) in E);X=sorted((sum(1<<k for k,a in enumerate(A) if tuple(sorted((v,a))) in E),v) for v in range(39) if v not in [root,*A]);return A,X

def solve(sig,na):
    n=1+na+len(sig);P=list(combinations(range(1+na,n),2));red=[0]*n;blue=[0]*n
    def mark(g,i,j):g[i]|=1<<j;g[j]|=1<<i
    for i,j in combinations(range(n),2):
        if i>na:continue
        val=(j<=na if not i else j>na and sig[j-na-1]>>(i-1)&1);mark(red if val else blue,i,j)
    def clique(g,m,k):
        if k==0:return True
        while m.bit_count()>=k:
            b=m&-m;m^=b
            if clique(g,m&g[b.bit_length()-1],k-1):return True
        return False
    def unit(r,b):
        while True:
            change=False
            for i,j in P:
                if (r[i]|b[i])>>j&1:continue
                minus=r[i]&r[j];plus=clique(b,b[i]&b[j],8)
                if minus and plus:return False
                if minus or plus:mark(b if minus else r,i,j);change=True
            if not change:return True
    def branch(r,b,i,j,one):
        rr=r.copy();bb=b.copy()
        if (b if one else r)[i]>>j&1:return None
        if (r[i]&r[j] if one else clique(b,b[i]&b[j],8)):return None
        mark(rr if one else bb,i,j);return (rr,bb) if unit(rr,bb) else None
    opened=lambda:[(i,j) for i,j in P if not (red[i]|blue[i])>>j&1];snap=[]
    def save(tag):snap.append(dict(stage=tag,red=sum(bool(red[i]>>j&1) for i,j in P),open=[[i-na-1,j-na-1] for i,j in opened()]))
    save('input');assert unit(red,blue);save('unit');
    while True:
        forced=[]
        for i,j in opened():
            for one in (False,True):
                if branch(red,blue,i,j,one) is None:forced.append((i,j,not one));break
        if not forced:break
        for i,j,one in forced:mark(red if one else blue,i,j)
        assert unit(red,blue);save('failed_literal')
    return snap
if __name__=='__main__':
    controls=[]
    for root in range(39):
        A,X=chart(root);degrees=[1+sum(mask>>i&1 for mask,_ in X) for i in range(len(A))];mask=sum(1<<i for i,d in enumerate(degrees) if d<9);hits=[v for m,v in X if m==mask];controls.append(dict(root=root,anchors=A,degrees=degrees,deficient_address=hits,qualifies=len(A)==9 and degrees.count(8)==2 and degrees.count(9)==7 and len(hits)==1))
    assert [t['root'] for t in controls if t['qualifies']]==[22];A,X=chart(22);s=solve([v for v,_ in X],len(A));possible={tuple(sorted((X[i][1],X[j][1]))) for i,j in s[-1]['open']};print([(r['stage'],r['red'],len(r['open'])) for r in s],sum(35 not in e for e in possible));Path(__file__).with_suffix('.json').write_text(json.dumps(dict(anchors=A,addresses=X,stages=s,root_controls=controls))+'\n')
