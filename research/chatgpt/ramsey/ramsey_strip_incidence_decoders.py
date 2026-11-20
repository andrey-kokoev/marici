"""Derive candidate Boolean readers from incidence labels alone. Assume oriented distance signature and its reversed reading, with complementarity on matched unused pairs. No target count. Include held-out negative control: arbitrary unused-pair candidates in same bridge coordinates. Input aggregate routes only, not reference 7+3 rules until comparison."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
H=Path(__file__).parent;load=lambda f:json.loads((H/f).read_text());rows=load('ramsey_strip_closure_control.json');D=list(combinations(range(6),2));M=[m for m in combinations(D,3) if len(set(sum(m,())))==6];N=[set() for _ in range(30)]
for i,d in enumerate(D):
 for j,m in enumerate(M,15):
    if d in m:N[i].add(j);N[j].add(i)
X=list(combinations(range(4),2));g=(0,2,1,3);e=[X.index(tuple(sorted(g[k] for k in x))) for x in X];tr=lambda d:tuple(sorted(e[i] for i in d));r=[D.index(tr(d)) for d in D]+[15+M.index(tuple(sorted(map(tr,m)))) for m in M];orbits=[i for i in range(30) if i<r[i]];dist=[]
for i in range(30):
 q=[i];d={i:0}
 for x in q:
    for y in N[x]-d.keys():q.append(y);d[y]=d[x]+1
 dist.append(d)
obs=set();full=set();paths=[]
for row in rows:
 p=row['path'];bs=row['bridge'][0];s=lambda x:tuple(dist[i][x] for i in bs);occupied=set(p)|{r[x] for x in p};u,v=[x for x in orbits if x not in occupied];adj=lambda x,y:bool(N[x]&{y,r[y]});obs.add((s(u),s(v),adj(u,v)));assert adj(u,v)==row['closes'];paths.append((row['closes'],[s(i) for i in p[1:11]]))
 for x in orbits:
    for y in orbits:
        if x<15<=y:full.add((s(x),s(y),adj(x,y)))
F=sorted({x for u,v,_ in full for x in (u,v)});assert set(x[::-1] for x in F)==set(F)
fits=[];fullfits=0
for k in range(len(F)+1):
 for cs in combinations(F,k):
    c=set(cs);match=lambda u,v:((u in c)!=(v in c)) and ((u[::-1] in c)!=(v[::-1] in c))
    if all(match(u,v)==ok for u,v,ok in full):fullfits+=1
    if not all(match(u,v)==ok for u,v,ok in obs):continue
    hist=Counter(sum(x in c for x in p) for ok,p in paths if ok);fits.append(dict(rule=cs,size=k,closed_counts=dict(hist)))
prev={tuple(sorted(map(tuple,rule))) for rule in load('ramsey_strip_bridge_profiles.json')['whole']['examples']};minimal=min(z['size'] for z in fits);sparse={z['rule'] for z in fits if z['size']==minimal};print('features, observed relation types, fits, sparse size, sparse count, old/sparse intersection, universal fits',len(F),len(obs),len(fits),minimal,len(sparse),len(prev&sparse),fullfits);print(Counter(x['size'] for x in fits));print([z for z in fits if z['size']==minimal]);print('ambiguous full signatures',sum((u,v,False) in full for u,v,b in full if b));(H/'ramsey_strip_incidence_decoders.json').write_text(json.dumps(dict(observed=sorted(obs),fits=fits,fullfits=fullfits),indent=2)+'\n')
