"""Return without a prescribed tour. Keep FCC moves separate from native comparison sectors."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import factorial
from pathlib import Path
import json
src=Path(__file__).resolve().parents[2]/'strominger'/'results'
f=json.loads((src/'fcc-first-transport.json').read_text());dirs=sorted({tuple(m['sector']) for m in f['directed_moves']});edges={(m['source'],dirs.index(tuple(m['sector']))):m['target'] for m in f['directed_moves']};start=next(v['id'] for v in f['vertices'] if v['barycentric']==[1,2,2,2]);
@lru_cache(None)
def walk(v,mask):
    if mask==0:assert v==start;return 1
    return sum(walk(edges[v,i],mask^(1<<i)) for i in range(12) if mask>>i&1 and (v,i) in edges)
print('FCC start',start,'admissible orders',walk(start,4095),'of',factorial(12),'all return')
d=json.loads((src/'native-path-sector-calculus-v1.json').read_text());qs={(0,0):1,(1,1):-1,(2,2):-1,(3,3):-1}
def mul(a,b):
    s=(1 if a*b>0 else -1);i,j=abs(a)-1,abs(b)-1
    if i==0 or j==0:return s*(1+(i|j))
    if i==j:return -s
    return s*(1 if (i,j) in ((1,2),(2,3),(3,1)) else -1)*(1+(i^j))
def word(w):
    g=1
    for i,s in w:g=mul(g,s*(i+2))
    return g
sectors=d['sectors'];moves=[word(r['left']) for r in sectors];assert all(x==-word(r['right']) and r['phase_bit']==1 for x,r in zip(moves,sectors));assert len(moves)==12
@lru_cache(None)
def products(mask):
    if not mask:return Counter({1:1})
    h=Counter()
    for i,v in enumerate(moves):
        if mask>>i&1:
            for g,c in products(mask^(1<<i)).items():h[mul(g,v)]+=c
    return h
out=products(4095);assert sum(out.values())==factorial(12) and set(out)=={1,-1};print('one left route per sector; ordered products',dict(out),'comparison-loop product',(-1)**12)
forms={tuple(r['normal_form']):r['matrix'] for r in d['normal_form_dictionary']};assert len(forms)==24
assert all(all(Fraction(u)==-Fraction(v) for row,other in zip(M,forms[1-e,i,j,k]) for x,y in zip(row,other) for u,v in zip(x,y)) for (e,i,j,k),M in forms.items());print('native dictionary / central sign:',len(forms)//2,'classes')
