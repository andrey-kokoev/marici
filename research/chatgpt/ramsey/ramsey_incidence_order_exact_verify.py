"""Pure Python verification of exact incidence-order hierarchy (r=0,1,2).
Requires the uploaded r36_16.g6.gz and two JSON certificate files.
No numerical optimizer, sympy or numpy used.
"""
from pathlib import Path
import json
from itertools import combinations
from ramsey_r37_full_catalogue_audit import data_rows,decode_graph6,indep_sets,EXPECTED_SHA
ROOT=Path(__file__).resolve().parent
input_data=json.loads((ROOT/'ramsey_incidence_order_exact_certificates.json').read_text())
pair_data=json.loads((ROOT/'ramsey_pair_conservation_certificates.json').read_text())
assert input_data['dataset_sha256']==pair_data['dataset_sha256']==EXPECTED_SHA
rows=data_rows(ROOT/'r36_16.g6.gz')
uniform={r['source_index']:r for r in input_data['uniform_failures']}
vertex_yes={r['source_index']:r for r in input_data['vertex_success']}
vertex_no={r['source_index']:r for r in input_data['vertex_impossible']}
pairs={r['source_index']:r for r in pair_data['records']}
assert len(uniform)==39 and len(vertex_yes)==19 and len(vertex_no)==20 and len(pairs)==39
assert set(vertex_yes).isdisjoint(vertex_no)
assert set(vertex_yes)|set(vertex_no)==set(uniform)==set(pairs)
for idx,row in enumerate(rows,1):
 H=decode_graph6(row)
 if sum(v.bit_count() for v in H)!=66:continue
 F=indep_sets(H,5); fset=set(F)
 u=uniform[idx]
 assert len(F)==u['fives']
 degrees=[sum((I&T)==0 for I in F) for T in F]
 assert min(degrees)==u['min_disjoint_degree']
 assert len(F)>=6*min(degrees),('uniform positive would succeed',idx)
 if idx in vertex_yes:
  rec=vertex_yes[idx]
  assert row.decode()==rec['graph6']
  assert len(rec['coefficients'])==16
  assert all(type(x)==int for x in rec['coefficients'])
  weights={I:sum(rec['coefficients'][v] for v in range(16) if I>>v&1) for I in F}
  assert min(weights.values())>=0
  cover=min(sum(w for I,w in weights.items() if (I&T)==0) for T in F)
  total=sum(weights.values())
  assert cover==rec['min_coverage'] and total==rec['total_weight']
  assert cover>0 and 6*cover-total==rec['gap']>0
 else:
  rec=vertex_no[idx]
  assert row.decode()==rec['graph6']
  lam={int(k):v for k,v in rec['lambda_coverage'].items()}
  eta={int(k):v for k,v in rec['eta_nonnegative'].items()}
  assert set(lam)<=fset and set(eta)<=fset
  assert all(type(x)==int and x>=0 for x in list(lam.values())+list(eta.values()))
  den=rec['denominator'];num=rec['lambda_numerator']
  assert den>0 and num==sum(lam.values())>=6*den
  for v in range(16):
   lhs=sum(y*sum((I&T)==0 and (I>>v&1) for I in F) for T,y in lam.items())
   lhs+=sum(y for I,y in eta.items() if I>>v&1)
   rhs=den*sum(I>>v&1 for I in F)
   assert lhs==rhs,(idx,v,lhs,rhs)
 # All r=2 certificates are checked independently of the r=1 duals.
 p=pairs[idx]
 assert row.decode()==p['graph6']
 c={tuple(map(int,k.split(','))):v for k,v in p['signed_pair_coefficients'].items()}
 nE=[(a,b) for a,b in combinations(range(16),2) if not(H[a]>>b&1)]
 assert set(c)<=set(nE)
 weights={I:sum(c.get((a,b),0) for a,b in nE if (I>>a&1) and (I>>b&1)) for I in F}
 assert min(weights.values())>=0
 cover=min(sum(w for I,w in weights.items() if (I&T)==0) for T in F)
 total=sum(weights.values())
 assert cover>0 and 6*cover-total==p['exact_margin']>0
print('PASS: 39 uniform impossibilities, 19 exact vertex certificates, 20 exact vertex impossibility duals, 39 signed pair certificates.')
