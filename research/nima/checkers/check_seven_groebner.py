"""Capped binomial Buchberger completion, lex x0 > ... > x41."""
import json
from pathlib import Path
from itertools import combinations
p=json.loads(Path('research/nima/results/seven_point_fibers.json').read_text());assert p['status']=='passed'
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
def mon(a,b):return tuple(int(i==a)+int(i==b) for i in range(42))
G=[]
for edge in sorted(set().union(*T)):
    inside=set(range(edge[0],edge[1]+1));cells={}
    for k,t in enumerate(T):
        if edge in t:
            a=frozenset(e for e in t-{edge} if set(e)<=inside);cells[a,(t-{edge})-a]=k
    ls=sorted({a for a,b in cells},key=repr);rs=sorted({b for a,b in cells},key=repr)
    for a,b in combinations(ls,2):
        for c,d in combinations(rs,2):
            g=tuple(sorted((mon(cells[a,c],cells[b,d]),mon(cells[a,d],cells[b,c])),reverse=True))
            if g not in G:G.append(g)
assert len(G)==63
steps=0
class Cap(Exception):pass
def nf(m):
    global steps
    while True:
        for a,b in G:
            if all(x>=y for x,y in zip(m,a)):
                m=tuple(x-y+z for x,y,z in zip(m,a,b));steps+=1
                if steps>200000:raise Cap()
                break
        else:return m
pairs=list(combinations(range(len(G)),2));cursor=0;complete=False
try:
    while cursor<len(pairs):
        if cursor>=50000 or len(G)>=300:raise Cap()
        i,j=pairs[cursor];cursor+=1;a,b=G[i];c,d=G[j]
        if not any(x and y for x,y in zip(a,c)):continue
        l=tuple(max(x,y) for x,y in zip(a,c))
        left=nf(tuple(x-y+z for x,y,z in zip(l,a,b)))
        right=nf(tuple(x-y+z for x,y,z in zip(l,c,d)))
        if left!=right:
            k=len(G);G.append(tuple(sorted((left,right),reverse=True)));pairs.extend((i,k) for i in range(k))
    complete=True
except Cap:pass
minimal=[a for i,(a,b) in enumerate(G) if not any(j!=i and c!=a and all(x>=y for x,y in zip(a,c)) for j,(c,d) in enumerate(G))]
result={'status':'complete' if complete else 'capped','order':'lex x0 > ... > x41','basis_size':len(G),'pairs_processed':cursor,'pairs_total':len(pairs),'reduction_steps':steps,'squarefree_minimal_initial':all(max(a)<=1 for a in minimal),'max_degree':max(sum(a) for a,b in G),'basis':G,'caps':{'basis':300,'pairs':50000,'reductions':200000},'scope':'Completion establishes a Groebner basis only if status is complete; binomial monic reductions are integral.'}
Path('research/nima/results/seven_groebner.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='basis'}))
