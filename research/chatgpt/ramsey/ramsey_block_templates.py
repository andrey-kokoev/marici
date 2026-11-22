"""Identify compact reusable spanning certificates inside the largest tight blocks: remove edges preserving the independence budget, then explicitly match each resulting graph against template representatives. Counts describe the deterministic chosen certificates, not all alternatives."""
from ramsey_inverse_five_motifs import D,json,graph,bits,Counter,combinations

def iso(G,H):
    if len(G)!=len(H):return None
    def rec(p,avail):
        if len(p)==len(G):return p.copy()
        ds={i:[j for j in avail if G[i].bit_count()==H[j].bit_count() and all((G[i]>>a&1)==(H[j]>>b&1) for a,b in p.items())] for i in range(len(G)) if i not in p};i=min(ds,key=lambda i:len(ds[i]));
        for j in ds[i]:
            p[i]=j;r=rec(p,avail-{j});del p[i]
            if r is not None:return r
    return rec({},set(range(len(G))))
if __name__=='__main__':
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();z=json.loads((D/'ramsey_odd_block_cover.json').read_text());reps=[];out=[]
    for i,rs in z.items():
        H=graph(ls[int(i)-1]);
        for r in rs:
            for s in r['supports']:
                vs=list(bits(s['blocks'][0]));a=s['profile'][0][1];n=len(vs);G=[sum(1<<j for j,w in enumerate(vs) if H[v]>>w&1) for v in vs];T=list(combinations(range(n),a+1));
                for x,y in combinations(range(n),2):
                    if not G[x]>>y&1:continue
                    G[x]^=1<<y;G[y]^=1<<x
                    if any(all(not G[u]>>v&1 for u,v in combinations(t,2)) for t in T):G[x]^=1<<y;G[y]^=1<<x
                for k,h in enumerate(reps):
                    p=iso(G,h)
                    if p is not None:break
                else:k=len(reps);reps.append(G);p={j:j for j in range(n)}
                out.append(dict(record=i,R=r['R'],S=s['S'],template=k,embedding=[vs[j] for j in sorted(p,key=p.get)]))
    print([(len(g),sum(x.bit_count() for x in g)//2,sum(r['template']==k for r in out)) for k,g in enumerate(reps)]);(D/'ramsey_block_templates.json').write_text(json.dumps(dict(templates=reps,uses=out))+'\n')
