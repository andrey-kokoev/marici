"""Recover circular interval orders from graph6 adjacency only. No input coordinates, multiplier, edge distances or two quartet templates in extraction."""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parents[1]/'results';G='bsaCCA?O?O_aC??`c@O@b?RcHQ?DcA@H?PC_@QO@@Q?DA@MP?RgKADoH?aR?KCbOC_JE?xO@AALC@AJPG?__V?_K@ROO_A@dOG@?_'
def extract(N):
    U=set(range(len(N)));best={};size=-1
    for t in combinations(U,4):
        if any(b in N[a] for a,b in combinations(t,2)):continue
        c=U.difference(t,*[N[i] for i in t]);k=len(c)
        if k>size:best.clear();size=k
        if k==size:best[frozenset(t)]=c
    triples=defaultdict(list);adj={q:set() for q in best}
    for q in best:
        for t in combinations(sorted(q),3):triples[t].append(q)
    for qs in triples.values():
        for a,b in combinations(qs,2):adj[a].add(b);adj[b].add(a)
    deg=max(map(len,adj.values()));S={q for q in best if len(adj[q])==deg};left=set(S);out=[]
    while left:
        q=min(left,key=lambda z:sorted(z));walk=[];prev=None
        while q in left:
            left.remove(q);walk.append(q);nb=adj[q]&S;assert len(nb)==2;prev,q=q,min(nb-{prev},key=lambda z:sorted(z))
        assert q==walk[0] and len(walk)==len(N);order=[]
        for i,q in enumerate(walk):
            v,=best[q]-best[walk[(i+1)%len(walk)]];order.append(v)
        assert set(order)==U
        for i,q in enumerate(walk):
            window={order[(i+j)%len(N)] for j in range(size)};assert window==best[q] and all(len(N[v]&window)==4 for v in window)
        ds=[j for j in range(1,len(N)//2+1) if order[j] in N[order[0]]];assert all((order[j] in N[order[i]])==(min(j-i,len(N)+i-j) in ds) for i,j in combinations(range(len(N)),2));out.append(dict(order=order,distances=ds))
    return dict(max_core=size,quartets=len(best),max_exchange_degree=deg,orders=out)
def main():
    n=ord(G[0])-63;bits=''.join(f'{ord(c)-63:06b}' for c in G[1:]);N=[set() for _ in range(n)]
    for j in range(n):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
    out=extract(N);cycles=[r['order'] for r in out['orders']];oriented={tuple((c+c)[i:i+n]) for order in cycles for c in (order,order[::-1]) for i in range(n)};assert len(oriented)==210 and all(r['distances']==[4,6,7,9] for r in out['orders']);out.update(oriented_with_origin=len(oriented),catalogue='https://users.cecs.anu.edu.au/~bdm/data/r39_35.g6',checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(D/'ramsey_39_extract_window_orders.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
