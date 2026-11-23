"""Rotate (source, next step, destination) interval test: each transition votes on every target by its distance gradient. Recover unoriented walls, then certify the state-to-wall matrix by Hamming reconstruction."""
from ramsey_gate_closure_radius import B,G,d,code,D,json,itertools
rows={};root=min(B,key=sorted)
for x,z in G.edges:
    side=frozenset(y for y in B if d[z][y]<d[x][y]);assert all(abs(d[z][y]-d[x][y])==1 for y in B);k=frozenset(B)-side if root in side else side;rows.setdefault(k,[]).append((x,z))
err=sum(sum((x in k)!=(y in k) for k in rows)!=d[x][y] for x,y in itertools.combinations(B,2));out=dict(states=len(B),edges=G.number_of_edges(),distinct_edge_votes=len(rows),pair_mismatches=err,wall_sizes=sorted(len(k) for k in rows),bits={})
for bit in (2,1):
    k=frozenset(s for s in B if code(s)&bit);k=frozenset(B)-k if root in k else k;cross=[(x,y) for x,y in G.edges if (x in k)!=(y in k)];out['bits'][bit]=dict(crossings=len(cross),distinct_votes=len({j for j,es in rows.items() if any(e in cross for e in es)}),agreeing_crossings=len(rows.get(k,[])))
print(out);(D/'ramsey_target_gradient.json').write_text(json.dumps(out,indent=2)+'\n')
