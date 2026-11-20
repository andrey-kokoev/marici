"""Find all incidence automorphisms commuting with the literal row swap and exchanging the chosen poles, without input turn labels or closure data. Compare the induced turn transport and full path reversal separately."""
from ramsey_literal_poles import adj,p,q,r,rep,labels,cases
from collections import Counter
V=range(30);solutions=[]
def search(m):
    if len(m)==30:
        assert all({m[w] for w in adj[v]}==adj[m[v]] and m[r[v]]==r[m[v]] for v in V);solutions.append(dict(m));return
    def opts(v):return [x for x in V if x not in m.values() and (v<15)!=(x<15) and (v==r[v])==(x==r[x]) and (r[v] not in m or m[r[v]]==r[x]) and all((w in adj[v])==(y in adj[x]) for w,y in m.items())]
    opts_,v=min(((opts(v),v) for v in V if v not in m),key=lambda t:len(t[0]));
    for x in opts_:search(dict(m)|{v:x})
search({p:q,q:p});summary=Counter();bycase=Counter()
for f in solutions:
    h={name:labels[rep(f[v])] for v,name in labels.items()}
    invol=all(f[f[v]]==v for v in V);assert h['A']=='B' and h['B']=='A';assert all(h[x+k][0]==y for x,y in zip('abcd','badc') for k in '01');summary[invol,h['a0']]+=1
    for route,_,__,turns,closed in cases:
        if [h[v] for v in route]==route[::-1]:bycase[tuple(route)]+=1;assert closed
print('pole exchanges by involution and image of a0:',summary);print('folded routes exactly reversed:',bycase)
