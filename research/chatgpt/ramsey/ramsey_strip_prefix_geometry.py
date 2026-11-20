"""Generate seven-step prefixes without any finish test. Classify in folded coordinates and by residual leaf peeling. Compare only afterwards with prefixes of the 40 routes. Show certificates by forced layers."""
from ramsey_strip_prism_proof import labels,rep,r,P,T
from collections import Counter,defaultdict
from pathlib import Path
import json
N=[set() for _ in range(30)]
for i,d in enumerate(P):
 for j,m in enumerate(T,15):
    if d in m:N[i].add(j);N[j].add(i)
# With a fixed starting pole, all turns of length 7 in the moving prism, modulo first reflection.
rows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());seen={tuple(z['path'][:8]) for z in rows};result=defaultdict(list)
def peel(rem):
 rest=set(rem);sizes=[]
 while rest:
    if any(not N[x]&rest for x in rest):return tuple(sizes),'isolated'
    edges={tuple(sorted((x,next(iter(N[x]&rest))))) for x in rest if len(N[x]&rest)==1};ends={x for edge in edges for x in edge};
    if not ends:
            assert len(rest)==8 and all(len(N[x]&rest)==2 for x in rest)
            return tuple(sizes),'8-cycle (two matchings)'
    if len(ends)!=2*len(edges):return tuple(sizes),'collision'
    sizes.append(len(edges));rest-=ends
 return tuple(sizes),'unique'
def walk(p,used):
 if len(p)==8:
    edges=[(v,w) if i%2==0 else (r[v],r[w]) for i,(v,w) in enumerate(zip(p,p[1:]))];rem=set(range(30))-{v for e in edges for v in e};s,z=peel(rem);word=' '.join(labels[rep(v)] for v in p[1:]);in_census=tuple(p) in seen;w=word.split();early_drift=len(w[3])==1 and len(w[6])!=1;assert (not early_drift)==(z=='unique')==in_census;result[s,z,in_census].append(word);return
 for y in N[p[-1]]-used:
    if y==r[y] or (len(p)==1 and y>r[y]):continue
    walk(p+[y],used|{y,r[y]})
for start in (0,14):walk([start],{start})
for k,ws in result.items():print(k,len(ws),ws[0]);print('' if len(ws)>10 else ws)
