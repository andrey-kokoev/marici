#!/usr/bin/env python3
"""Check the generator-level tetrahedral-to-channel semidirect comparison."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
def rot_edge(e,s,n):a,b=e;return edge((a+s)%n,(b+s)%n)
rows=[]
for n in (8,12,16,20):
 s=n//4;d=edge(0,2);orbit=[d]
 for _ in range(3):orbit.append(rot_edge(orbit[-1],s,n))
 distinct=len(set(orbit))==4
 # B(e_i)=e_(q^i d). Thus Q B(e_i)=B rho(e_i) by construction.
 intertwines=all(rot_edge(orbit[i],s,n)==orbit[(i+1)%4] for i in range(4))
 rows.append({'n':n,'seed_channel':list(d),'tetra_basis_image':[list(x) for x in orbit],'embedding_rank':len(set(orbit)),'Q_B_equals_B_rho':intertwines,'four_steps_on_distribution_target':'identity','required_helix_target':'suspension'})
checks={'rank_four_embeddings':all(r['embedding_rank']==4 for r in rows),'semidirect_relation_on_generators':all(r['Q_B_equals_B_rho'] for r in rows),'comparison_requires_periodicization_or_shift_lift':True}
out={'schema':'marici.nima.tetra-channel-semidirect-comparison.v1','degrees':[8,12,16,20],'results':rows,'checks':checks,'passed':all(checks.values()),'boundary':'The incidence/rotation skeleton intertwines. The ungraded Fourier target has F^4=I, whereas the universal stable source requires q^4=Sigma; use a periodic stable target or a graded shift lift before claiming a functor from U.'}
p=ROOT/'research/nima/results/tetra-channel-semidirect-comparison.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
