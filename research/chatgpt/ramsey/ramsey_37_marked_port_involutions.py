"""Catalogue test of the necessary and sufficient symmetry condition for *representing* a graph with one marked tetrahedral port, not a target-free constructor. Enumerate involutions by assigning fixed vertices or unordered transpositions; preserve adjacency to every previously assigned vertex. Degree and neighbor-degree signatures are isomorphism invariants."""
from pathlib import Path
from collections import Counter
from itertools import combinations,permutations
import json
H=Path(__file__).parent
X=[('c',i) for i in range(4)]+[('p',*t) for t in permutations(range(4),2)]+[('e',*t) for t in combinations(range(4),2)]
g=(0,1,3,2)
def reflect(x):
    a=[g[i] for i in x[1:]];return (x[0],*(sorted(a) if x[0]=='e' else a))
r=[X.index(reflect(x)) for x in X];fix=sum(i==j for i,j in enumerate(r));assert fix==6

def search(N):
    deg=list(map(len,N));sig=[(deg[i],tuple(sorted(deg[j] for j in nb))) for i,nb in enumerate(N)];out=[]
    def visit(left,p,f):
        if not left:
            if f==fix:out.append([p[i] for i in range(22)])
            return
        if f>fix or f+len(left)<fix:return
        opts=None
        for i in left:
            ys=[j for j in left if sig[i]==sig[j] and (j!=i or f<fix) and all(((a in N[i])==(b in N[j])) for a,b in p.items())];
            if not ys:return
            if opts is None or len(ys)<len(opts):x,opts=i,ys
        for y in opts:visit(left-{x,y},p|{x:y,y:x},f+(x==y))
    visit(set(range(22)),{},0);return out
rows=[]
for idx,line in enumerate((H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines(),1):
    assert ord(line[0])-63==22;bits=''.join(format(ord(ch)-63,'06b') for ch in line[1:]);N=[set() for _ in range(22)];k=0
    for j in range(22):
        for i in range(j):
            if bits[k]=='1':N[i].add(j);N[j].add(i)
            k+=1
    sol=search(N)
    for p in sol:assert all(p[p[i]]==i and {p[j] for j in N[i]}==N[p[i]] for i in range(22))
    if sol:rows.append(dict(record=idx,count=len(sol),example=sol[0]))
print('records',idx,'matching',len(rows),'counts',Counter(x['count'] for x in rows),'first',rows[:1]);(H/'ramsey_37_marked_port_involutions.json').write_text(json.dumps(rows,indent=2)+'\n')
