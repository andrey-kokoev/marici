"""Transfer clause-square prediction to first 10 catalogue parents, every two-site deletion. Enumerate exact same syntactic motif on projected minimal rows. Test each predicted cut by side distance vs two-cross excursions. Restrict to connected boundaries with all four groups occupied."""
from pathlib import Path
import itertools,json,collections
import networkx as nx
D=Path(__file__).parent;out=collections.Counter();examples={};sites=lambda s:[i for i in range(22) if s>>i&1]
for rec,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[:10],1):
 g=nx.from_graph6_bytes(line);I=[0];H=[sum(1<<j for j in g[i]) for i in range(22)]
 for i,h in enumerate(H):I.extend([s|1<<i for s in I if not s&h]);
 T=[s for s in I if s.bit_count()==6];hits=[sum(1<<i for i,t in enumerate(T) if t>>v&1) for v in range(22)];cov={0:0}
 for s in I[1:]:b=s.bit_length()-1;cov[s]=cov[s^1<<b]|hits[b]
 for u,v in itertools.combinations(range(22),2):
    out['cores']+=1;m=1<<u|1<<v;must=((1<<len(T))-1)&~(hits[u]|hits[v]);B={s for s in I if not s&m and not must&~cov[s]};
    if len(B)<4:continue
    U=0;F=(1<<22)-1
    for s in B:U|=s;F&=s
    R={t&U for t in T if not t&(m|F)};tri=[s for s in R if s.bit_count()==3 and not any(t!=s and t&s==t for t in R)];G=None
    for A,C in itertools.combinations(sorted(tri),2):
     if A&C:continue
     for a,c in itertools.product(sites(A),sites(C)):
      if not H[a]>>c&1:continue
      p,q=sites(A^1<<a);r,t=sites(C^1<<c)
      if not (H[p]>>t&1 and H[q]>>r&1):r,t=t,r
      if not (H[p]>>t&1 and H[q]>>r&1):continue
      groups={s:0 if s>>a&1 else 3 if s>>c&1 else 1 if s>>p&1 else 2 for s in B};
      if len(set(groups.values()))!=4:continue
      if G is None:
       G=nx.Graph();G.add_nodes_from(B);G.add_edges_from((s,s^1<<j) for s in B for j in sites(s) if s^1<<j in B)
      if not nx.is_connected(G):continue
      out['motifs']+=1;full=dict(nx.all_pairs_shortest_path_length(G));valid=[];witness=None
      for bit in (1,2):
       half={s for s in B if groups[s]&bit};cross=[(s,t) for s in half for t in G[s] if t not in half];ok=all(all((full[w][s]<full[w][t])==(w in half) for w in B) for s,t in cross);valid.append(ok)
       if not ok:
        sidewalk=min((nx.shortest_path(G,x,y) for x,y in itertools.combinations(B,2) if bool(groups[x]&bit)==bool(groups[y]&bit) and any(full[x][z]+full[z][y]==full[x][y] for z in B if bool(groups[z]&bit)!=bool(groups[x]&bit))),key=len);x,y=sidewalk[0],sidewalk[-1];z=next(z for z in B if bool(groups[z]&bit)!=bool(groups[x]&bit) and full[x][z]+full[z][y]==full[x][y]);path=nx.shortest_path(G,x,z)[:-1]+nx.shortest_path(G,z,y);witness=dict(bit=bit,path=list(map(sites,path)),classes=[groups[s] for s in path],distance=len(path)-1,side_connected=nx.has_path(G.subgraph([s for s in B if bool(groups[s]&bit)==bool(groups[x]&bit)]),x,y))
      k='valid_'+str(sum(valid));out[k]+=1;examples.setdefault(k,dict(parent=rec,deleted=[u,v],states=len(B),pattern=[a,c,p,q,r,t],valid=valid,witness=witness))
print(out,examples);(D/'ramsey_gate_transfer.json').write_text(json.dumps(dict(counts=out,examples=examples),indent=2)+'\n')
