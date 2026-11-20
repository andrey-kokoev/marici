"""Test the direct-edge convention on ALL literal-pole simple reflected strips. Compute terminal forms by all square shortcuts, closure changes, and lift endpoint (sheet) after each change."""
from ramsey_strip_prism_proof import labels,rep,r,E
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
records=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());data={tuple(labels[rep(i)] for i in z['path'][1:-1]):z for z in records if (z['path'][0],z['path'][-1])==(0,29)};assert len(data)==24

def shortcuts(w):
 for i in range(len(w)-3):
    if tuple(sorted((w[i],w[i+3]))) in E:
        v=w[:i+1]+w[i+3:];assert v in data;yield i,v
@lru_cache(None)
def normal(w):return frozenset(v for _,q in shortcuts(w) for v in normal(q)) or frozenset([w])
h=Counter();terminal=Counter();classes=Counter();counter=None
for w,z in data.items():
 for i,v in shortcuts(w):
    short=data[v];a=z['path'][1:-1];b=short['path'][1:-1];assert a[:i+1]==b[:i+1] and tuple(r[x] for x in a[i+3:])==tuple(b[i+1:]);h[len(w),z['closes'],short['closes']]+=1
    if z['closes']!=short['closes']:counter=(w,v,z['closes'],short['closes'])
 f=normal(w);assert len(f)==1;classes[next(iter(f))]+=1
 if not list(shortcuts(w)):terminal[len(w),z['closes']]+=1
from ramsey_strip_witness_orbits import orbits,fill,edges
@lru_cache(None)
def types(w):
 p=data[w]['path'];c=p+[r[x] for x in p[-2:0:-1]];return frozenset(orbits[frozenset((i,j-15) for i,j in extra|{edges(c[k],c[(k+1)%len(c)]) for k in range(alt,len(c),2)})] for extra in fill(set(range(30))-set(c)) for alt in (0,1))
print('witness types long/short',Counter((len(w),tuple(sorted(types(w))),tuple(sorted(types(v)))) for w in data for _,v in shortcuts(w)))
print('shortcuts by original length, original/short closure',h,'terminal lengths',terminal,'class sizes',sorted(classes.values()),'example closure change',counter)
