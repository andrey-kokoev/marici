"""Enumerate incidence dualities for the literal row-preserving poles (0,29), not (0,26). Test the whole stitch, fixed half, outcomes, isolated guard and last partner simultaneously."""
from ramsey_strip_local_stitch import flips,N,s,t
from ramsey_strip_first_generator import r
from collections import Counter
V=range(30);solutions=[]
def search(m):
    if len(m)==30:
        assert all({m[u] for u in N[v]}==N[m[v]] and m[r[v]]==r[m[v]] for v in V);solutions.append(m);return
    def opts(v):return [x for x in V if x not in m.values() and (v<15)!=(x<15) and (v==r[v])==(x==r[x]) and (r[v] not in m or m[r[v]]==r[x]) and all((w in N[v])==(y in N[x]) for w,y in m.items())]
    os,v=min(((opts(v),v) for v in V if v not in m),key=lambda t:len(t[0]));
    for x in os:search(m|{v:x})
search({s:t,t:s});assert (s,t)==(0,29)
def record(z):
 _,idx,g,b,_,__,iso,h=z;v,=iso;w,=N[v]-{s,t,*h};return h,g,b,v,w
records=list(map(record,flips));early=[i for i,z in enumerate(flips) if z[1][0]==2];late=set(range(8))-set(early);images={i:set() for i in early};summary=Counter()
for f in solutions:
 path=lambda x:tuple(f[v] for v in reversed(x));hits=[]
 for i in early:
    h,g,b,v,w=records[i];target=(path(h),path(g),path(b),f[v],f[w]);
    if target in records:
        j=records.index(target);assert j in late;images[i].add(j);hits.append(j)
 summary[all(f[f[v]]==v for v in V),len(hits)]+=1
print('duality count by (involution, complete stitches mapped)',summary);print('early -> late stitch indices',images);print('example guarded links',[(records[i][-2:],records[j][-2:]) for i in early[:1] for j in sorted(images[i])]);
