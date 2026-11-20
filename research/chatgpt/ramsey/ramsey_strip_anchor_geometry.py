"""Find the anchor pair by walking from the two candidate partners in the network of two-option claimants. No switch time, shape class, endpoint, or subset search in the predictor. Check against the earlier four-case certificate only afterwards."""
from collections import Counter,defaultdict,deque
from ramsey_strip_prefix_geometry import N,r,rows

def anchors(p):
 used={v for i,(x,y) in enumerate(zip(p,p[1:])) for v in ((x,y) if i%2==0 else (r[x],r[y]))};current=r[p[-1]];opts=N[current]-used;adj=defaultdict(set);pin=defaultdict(set)
 assert len(opts)==2
 for x in set(range(30))-used-{current}:
    if (x<15)!=(current<15):continue
    ns=N[x]-used
    if len(ns)==1:pin[next(iter(ns))].add(x)
    if len(ns)==2:
        a,b=ns;adj[a].add(b);adj[b].add(a)
 hits=[]
 for start in opts:
    q=deque([start]);dist={start:0}
    while q:
        v=q.popleft();hits.extend((start,x,dist[v]) for x in pin[v]);
        for w in adj[v]-dist.keys():dist[w]=dist[v]+1;q.append(w)
 assert len(hits)==1
 blocked,leaf,d=hits[0];chosen,=opts-{blocked};pair=N[leaf]&used;assert len(pair)==2;return pair,leaf,d+1,r[chosen]
if __name__=='__main__':
 from ramsey_strip_turn_reservation_chain import reservation
 seen={};outcomes=Counter()
 for z in rows:
    for alt in (0,1):
        p=tuple(r[v] if alt else v for v in z['path'][:8]);pair,leaf,n,y=anchors(p);chain,v=reservation(p);assert leaf==chain[0][0] and v==y and len(chain)==n;assert ((r[y] if alt else y)==z['path'][8])==z['closes'];seen[p]=n;outcomes[alt,z['closes']]+=1
 print('distinct oriented prefixes by certificate length:',Counter(seen.values()),'; outcomes:',outcomes)
