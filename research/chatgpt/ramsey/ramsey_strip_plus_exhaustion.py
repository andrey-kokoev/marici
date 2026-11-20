"""Adaptive plus-first grouping; no closure labels used. Explore all maximizer ties and compare to a single global column order."""
import json
from pathlib import Path
from functools import lru_cache
from itertools import product
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(0,29)]
cols={f'{k}{i}':frozenset(n for n,z in enumerate(rows,1) if i in z['selected'][j]) for j,k in enumerate('FR') for i in range(1,11)};root=tuple(range(1,11));by_size=lambda c:-len(cols[c]);global_order=sorted(cols,key=by_size);print('global',sorted(root,key=lambda n:tuple(n not in cols[c] for c in global_order)))
def choices(group):
    opt=[(len(set(group)&v),k) for k,v in cols.items() if 0<len(set(group)&v)<len(group)]
    return [k for n,k in opt if n==max(t[0] for t in opt)]
def split(g,k):return tuple(n for n in g if n in cols[k]),tuple(n for n in g if n not in cols[k])
def trace(g):
    c=choices(g)
    if c:
        a,b=split(g,c[0]);print(g,c,'->',a,b);trace(a);trace(b)
trace(root)
@lru_cache(None)
def all_orders(g):
    c=choices(g)
    if not c:return {(g,)}
    return {a+b for k in c for x,y in [split(g,k)] for a,b in product(all_orders(x),all_orders(y))}
o=all_orders(root);print('orders',len(o));print('possible leaves',set(x for v in o for x in v));print('possible first groups',set(v[0] for v in o));print('root populations',{k:len(cols[k]) for k in cols});assert len(rows)==10
allrows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());assert all(((8 in z['selected'][0])==(3 in z['selected'][1]))==z['closes'] for z in allrows)
