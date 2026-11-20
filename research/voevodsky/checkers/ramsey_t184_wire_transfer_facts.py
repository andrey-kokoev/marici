"""Fine-edge contact readout. One native oriented edge, two coupled barycentric changes. Test global exclusions plus site/strict existential witnessing with the proposed ordering and with all orderings. Never choose an orientation per wire."""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';d=json.loads((D/'esd7_explicit_analytical_census.json').read_text());V={v['id']:v['barycentric'] for v in d['vertices']};E={frozenset(e['vertices']):e for e in d['edges']};T=d['tetrahedra'];c=next(t for t in T if t['id']=='T184');C=set(c['vertices']);ws=sorted(C,key=lambda v:V[v].index(1));neighbors=[next(t for t in T if t!=c and C-{w}<=set(t['vertices'])) for w in ws];rows=[]
for i,j in combinations(range(4),2):
    a,b=neighbors[i],neighbors[j];e=E[frozenset(a['vertices'])&frozenset(b['vertices'])];assert set(a['edges'])&set(b['edges'])=={e['id']};x,y=e['vertices'];delta=[s-r for r,s in zip(V[x],V[y])];assert sorted(delta)==[-1,0,0,1];rows.append(dict(ij=(i,j),edge=e['id'],ends=[x,y],delta=delta,mask=e['transfer_mask']))
claims=('no R-','no B+','some R+','some B-');fixed={};all_maps={}
for strict in (False,True):
    hist=Counter()
    for order in permutations(claims):
        legal=[]
        for mask in range(64):
            used=[r for i,r in enumerate(rows) if mask>>i&1];
            if any(r['delta'][0]<0 or r['delta'][1]>0 for r in used):continue
            sets=[[r['delta'][k]==s for r in used if order.index(name) in r['ij']] for name,k,s in [('some R+',0,1),('some B-',1,-1)]]
            if all(any(v) and (not strict or all(v)) for v in sets):legal.append([r['edge'] for r in used])
        m=max(map(len,legal),default=0);hist[m]+=1
        if order==claims:fixed[strict]=[s for s in legal if len(s)==m]
    all_maps[strict]=dict(hist)
out=dict(axes=['R','B','N1','N2'],proposed_binding=claims,contacts=rows,fixed_maximal_by_count=fixed,all_binding_max_count=all_maps);print(fixed,all_maps);(D/'ramsey_t184_wire_transfer_facts.json').write_text(json.dumps(out,indent=2)+'\n')
