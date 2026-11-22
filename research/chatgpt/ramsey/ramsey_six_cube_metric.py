"""Natural hypercube net: fixed (3,7) duad chart; do not preselect a pair of rows. Exhaust legal wirings, compute occupied raw-cube metric and shortest transitions. Test one omission per partition, invariance under the entire address S6. Check nearest-neighbor components and bipartiteness; do not infer unrestricted minimal embedding dimension."""
from ramsey_six_label_readout import E,X,sol,z3,W,m,mate,P,T,D,json
from itertools import combinations,permutations
from collections import Counter,deque
ws=[]
while sol.check()==z3.sat:
    md=sol.model();w=sum(1<<i for i,x in enumerate(X) if z3.is_true(md.eval(x)));ws.append(w);sol.add(z3.Or(*[z3.Not(x) if w>>i&1 else x for i,x in enumerate(X)]))
assert sol.check()==z3.unsat and len(ws)==288;ws.sort();U=set(ws);blocks=[[E.index(tuple(sorted((P.index(a),P.index(b))))) for a,b in combinations(t,2)] for t in T];assert sorted(sum(blocks,[]))==list(range(45));profile=Counter(tuple(sorted(Counter(sum(w>>i&1 for i in block) for block in blocks).items())) for w in ws);h=Counter((w^v).bit_count() for w,v in combinations(ws,2));least=min(h);adj={w:{v for v in ws if (w^v).bit_count()==least} for w in ws};left=set(ws);components=[]
while left:
    s=min(left);par={s:0};q=deque([s]);bip=True
    while q:
        x=q.popleft()
        for v in adj[x]:
            if v not in par:par[v]=1-par[x];q.append(v)
            elif par[v]==par[x]:bip=False
    left-=par.keys();components.append((len(par),bip))
orbits=[];left=set(ws);maps=[]
for p in permutations(range(6)):
    g=[P.index(tuple(sorted(p[j] for j in d))) for d in P];maps.append([E.index(tuple(sorted((g[i],g[j])))) for i,j in E])
while left:
    s=min(left);o={sum((s>>i&1)<<j for i,j in enumerate(g)) for g in maps};assert o<=U;orbits.append(len(o));left-=o
cols=[sum((w>>i&1)<<j for j,w in enumerate(ws)) for i in range(45)];n=(1<<len(ws))-1;r=dict(wirings=len(ws),block_profiles=str(profile),red_weights=dict(Counter(w.bit_count() for w in ws)),column_counts=dict(Counter(x.bit_count() for x in cols)),distinct_splits=len({min(x,n^x) for x in cols}),source_orbits=orbits,distance_hist=dict(sorted(h.items())),min_degrees=dict(Counter(map(len,adj.values()))),min_components=components,selected_row_distance=(W(m)^W(mate)).bit_count());x,y=max(combinations(ws,2),key=lambda ab:len(adj[ab[0]]&adj[ab[1]]));shared=sorted(adj[x]&adj[y]);r['max_common_min_neighbors']=len(shared);r['common_neighbor_witness']=[x,y,shared];print(r);(D/'ramsey_six_cube_metric.json').write_text(json.dumps(r,indent=2)+'\n')
