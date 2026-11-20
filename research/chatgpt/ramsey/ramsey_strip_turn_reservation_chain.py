"""Read a step-eight reservation directly from previously visited positions. No transported ID table, Hall subset enumeration, or matching search. p[0] is the fixed pole; normalize alternation by reflecting p for parity 1."""
from ramsey_strip_prefix_geometry import rows,N,r,rep,labels
from collections import Counter

def reservation(p):
    names=[labels[rep(x)] for x in p[1:]];k=next(i for i,w in enumerate(names[1:],2) if len(w)==1)
    if k==4:anchors=(p[4],r[p[4]]);extensions=[p[0]]
    elif k==5 and names[2][0]==names[6][0]:anchors=(p[2],r[p[4]]);extensions=[p[6]]
    elif k==5:anchors=(r[p[2]],p[4]);extensions=[]
    elif k==6:anchors=(p[6],r[p[6]]);extensions=[p[0],p[4]]
    else:raise ValueError(k)
    occupied={x for i,(a,b) in enumerate(zip(p,p[1:])) for x in ((a,b) if i%2==0 else (r[a],r[b]))};chain=[];a,b=anchors
    for ext in [*extensions,None]:
        leaf,=N[a]&N[b];assert a in occupied and b in occupied and leaf not in occupied
        mate,=N[leaf]-occupied;chain.append((leaf,mate));occupied.update((leaf,mate));a,b=mate,ext
    current=r[p[-1]];assert chain[-1][1] in N[current];next_mate,=N[current]-occupied;return chain,r[next_mate]
seen={};patterns=Counter()
for row in rows:
    p=tuple(row['path'][:8]);
    for parity in (0,1):
        q=tuple(r[x] for x in p) if parity else p;chain,v=reservation(q);v=r[v] if parity else v;assert (v==row['path'][8])==row['closes'];seen[q]=len(chain)
assert len(seen)==64 and Counter(seen.values())=={1:16,2:32,3:16};print('Verified direct chains by length:',Counter(seen.values()))
