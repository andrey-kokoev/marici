"""Lookup audit on fixed scopes: red pair A, disjoint blue (k-2)-set B.
Test all 4 Boolean keys at each of 3 cells twice. Cache complete probe answers.
Count row predicate tests, index postings, index lookups separately.
"""
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
from ramsey_37_pair_rotation_rule import build
from pauli_realization_audit import decode_graph6

def audit(g,k):
    V=range(len(g));A,B=next((a,b) for a in combinations(V,2) if g[a[0]]>>a[1]&1 for b in combinations(sorted(set(V)-set(a)),k-2) if all(not(g[x]>>y&1) for x,y in combinations(b,2)))
    rows={};reads=set()
    for w in sorted(set(V)-set(A)-set(B)):
        a=[g[w]>>x&1 for x in A];b=[g[w]>>x&1 for x in B]
        reads.update(tuple(sorted((w,x))) for x in (*A,*B));rows[w]=(not all(a),all(b),not all(b),not any(a))
    keys=[(0,3),(0,1),(0,2)];stats=[]
    for mode in ('scan','two','three'):
        tables={};posts=tests=lookups=0;cache={}
        for i in range({'scan':0,'two':2,'three':3}[mode]):
            t=defaultdict(list);x,y=keys[i]
            for w,r in rows.items():t[r[x],r[y]].append(w);posts+=1
            tables[i]=t
        for _ in range(2):
            for i,(x,y) in enumerate(keys):
                for u,v in product((False,True),repeat=2):
                    j,s=(1,not v) if i==2 and mode!='three' else (i,v)
                    if (j,u,s) not in cache:
                        if j in tables:out=tables[j].get((u,s),[]);lookups+=1
                        else:
                            p,q=keys[j];out=[w for w,r in rows.items() if (r[p],r[q])==(u,s)];tests+=len(rows)
                        cache[j,u,s]=out
                    assert cache[j,u,s]==[w for w,r in rows.items() if (r[x],r[y])==(u,v)]
        stats.append((mode,posts,tests,lookups))
    print(k,A,B,len(rows),len(reads),stats)

if __name__=='__main__':
    p=Path(__file__).parent/'pauli-realization-catalogues/r36_17.g6';audit(decode_graph6(p.read_text().splitlines()[0]),6);audit(build(),7)
