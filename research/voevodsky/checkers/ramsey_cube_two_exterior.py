"""Extend the one-port Ramsey equivalence test. Core 1..8; v=9, w=10,z=11. Both edges from v to new ports fixed blue. Ordered supports; wz tested both ways."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results'
def run(edges):
    A=[0]*11
    for i,j in edges:A[i-1]|=1<<(j-1);A[j-1]|=1<<(i-1)
    I=[m for m in range(256) if all(not(m>>i&1 and m&A[i]) for i in range(8))];corners=list(product((1,2),(4,5),(7,8)));rows=[]
    # Max independent size on every induced core subset.
    alpha=[max(s.bit_count() for s in I if s&~m==0) for m in range(256)]
    events=list(product(I,I));g6=list(combinations(range(11),6));testm=[sum(1<<i for i in c) for c in g6];
    for red in (False,True):
        signatures=[]
        for corner in corners:
            S=sum(1<<(v-1) for v in corner);sig=set()
            for idx,(T,U) in enumerate(events):
                ok=(not red or not(T&U)) and all(alpha[255&~m]<4 for m in (S|T,S|U)) and (red or (alpha[255&~(T|U)]<4 and alpha[255&~(S|T|U)]<3));
                if ok:sig.add(idx)
            signatures.append(sig)
        groups={};
        for i,s in enumerate(signatures):groups.setdefault(frozenset(s),[]).append(corners[i]);
        old=[0,1,3,7];dist=[]
        for i,j in combinations(old,2):
            diff=signatures[i]^signatures[j];
            if diff:
                idx=min(diff,key=lambda q:(sum(m.bit_count() for m in events[q]),q));T,U=events[idx];yes,no=(i,j) if idx in signatures[i] else (j,i);receipt=[]
                for h in (yes,no):
                    B=A.copy()
                    for v,m in enumerate([sum(1<<(x-1) for x in corners[h]),T,U],8):
                        B[v]=m
                        for t in range(8):
                            if m>>t&1:B[t]|=1<<v
                    if red:B[9]|=1<<10;B[10]|=1<<9
                    blue=next(([x+1 for x in c] for c,m in zip(g6,testm) if all(not(B[x]&m) for x in c)),None);tri=any(B[x]&B[y] for x,y in combinations(range(11),2) if B[x]>>y&1);assert (not tri and blue is None)==(h==yes);receipt.append(blue)
                dist.append(dict(yes=corners[yes],no=corners[no],T=T,U=U,blue=receipt[1]))
        rows.append(dict(wz='red' if red else 'blue',groups=[dict(corners=g,count=len(s)) for s,g in groups.items()],distinctions=dist));
    return rows
if __name__=='__main__':
    edges=[(i,i+1) for i in range(1,8)];result={k:run(e) for k,e in [('path',edges),('chord',edges+[(3,6)])]};(D/'ramsey_cube_two_exterior.json').write_text(json.dumps(result,indent=1));
    for k,rows in result.items():
        for r in rows:print(k,r['wz'],len(r['groups']),[(len(g['corners']),g['count']) for g in r['groups']],r['distinctions'][:1])
