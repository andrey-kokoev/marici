"""One-shot odd bridge cut certificate on seven-step residuals, without a catalogue of matchings or iterative leaf-pair elimination."""
from ramsey_strip_prefix_geometry import N,result,labels,rep,r
from collections import Counter

def component(root,g,skip=None):
 seen={root};q=[root]
 for v in q:
    for w in g[v]-seen:
        if (v,w)==skip or (w,v)==skip:continue
        seen.add(w);q.append(w)
 return seen

def certificate(rem):
 G={v:N[v]&rem for v in rem};forced=set();forbid=set()
 for x in rem:
    for y in G[x]:
        if x>=y:continue
        c=component(x,G,(x,y))
        if y not in c:(forced if len(c)%2 else forbid).add((x,y))
 occ={x for e in forced for x in e};H={x:{y for y in G[x]-occ if tuple(sorted((x,y))) not in forbid} for x in rem-occ};todo=set(H);parts=[]
 while todo:
    cc=component(next(iter(todo)),H);todo-=cc;parts.append((len(cc),sum(len(H[x]) for x in cc)//2,max(len(H[x]) for x in cc)))
 assert len(occ)==2*len(forced)
 if len(H)==12:
    cyc=set(H)
    while leaves:=(set(x for x in cyc if len(H[x]&cyc)<2)):cyc-=leaves
    roots=sorted(x for x in cyc if H[x]-cyc);rims=[]
    if roots:
        x=roots[0];prev=None
        for k in range(len(cyc)):
            if x in roots:rims.append(k)
            y=next(iter((H[x]&cyc)-{prev}));prev,x=x,y
    tails=tuple(sorted(len(component(y,{v:H[v]-cyc for v in H if v not in cyc})) for x in roots for y in H[x]-cyc));return len(forced),len(cyc),tuple(rims),tails
 return len(forced),tuple(sorted(parts))
for (layers,status,eligible),words in result.items():
 if not eligible:continue
 certs=Counter()
 for word in words:
    names=word.split();p=[0 if names[0]=='A' else 14]
    for name in names:p.append(min(y for y in N[p[-1]] if labels.get(rep(y))==name))
    for alt in (0,1):
        obs=[(v,w) if i%2==alt else (r[v],r[w]) for i,(v,w) in enumerate(zip(p,p[1:]))];rem=set(range(30))-{v for e in obs for v in e};certs[certificate(rem)]+=1
 print('certificate',words[0],certs)
