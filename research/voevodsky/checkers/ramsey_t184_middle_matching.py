"""Middle layers only: all fine edges, bijective edge selections, and incidence-reversing involutions between the two layers. No imposed matching or coordinate order."""
import json
from itertools import permutations
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';d=json.loads((D/'esd7_explicit_analytical_census.json').read_text());rad=json.loads((D/'ramsey_t184_two_connection_layers.json').read_text())['radial'];E={frozenset(e['vertices']) for e in d['edges']};coord={v['id']:tuple(v['barycentric']) for v in d['vertices']};ids={x:v for v,x in coord.items()};rho=lambda v:ids[coord[v][-1:]+coord[v][:-1]];out=[];matches=[]
for r in rad:
    a,b=r['shortest_path_layers'][1:3];M=[[int(frozenset((v,w)) in E) for w in b] for v in a];P=list(permutations(range(4)));p,=[p for p in P if all(M[i][p[i]] for i in range(4))];m=dict(zip(a,(b[j] for j in p)));matches.append(m)
    # Using matched column names, test exact equality to subset inclusion on two bits.
    lab=next(h for h in P if all(bool(M[i][p[j]])==(h[i]&h[j]==h[i]) for i in range(4) for j in range(4)))
    reversals=[h for h in P if all(M[i][h[j]]==M[j][h[i]] for i in range(4) for j in range(4))];assert len(reversals)==2 and p not in reversals
    out.append(dict(exit=r['exit'],rows=a,cols=b,matrix=M,matching=m,subset_labels_on_matched_pairs=lab,layer_swap_maps=[dict(zip(a,(b[j] for j in h))) for h in reversals]))
assert all({rho(v):rho(w) for v,w in m.items()}==matches[(i+1)%4] for i,m in enumerate(matches));(D/'ramsey_t184_middle_matching.json').write_text(json.dumps(out,indent=2)+'\n');print('4 unique rotation-compatible matchings; each middle relation is the two-bit subset order with two layer-reversing involutions')
