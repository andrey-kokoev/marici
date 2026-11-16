"""Standard-library verification of signed pair-conservation obstruction and
six obstructions to nonnegative pair potentials for the complete 33-edge R(3,6;16) catalogue.
Requires r36_16.g6.gz, ramsey_pair_conservation_certificates.json and
ramsey_r37_full_catalogue_audit.py in the same directory.
No scipy/numpy or optimization invoked.
"""
import json
from pathlib import Path
from itertools import combinations
from ramsey_r37_full_catalogue_audit import data_rows,decode_graph6,indep_sets,triangle_free,EXPECTED_SHA

ROOT=Path(__file__).resolve().parent
source=ROOT/'r36_16.g6.gz'
rows=data_rows(source)
certs=json.loads((ROOT/'ramsey_pair_conservation_certificates.json').read_text())
assert certs['dataset_sha256']==EXPECTED_SHA
assert len(certs['records'])==39
record_by_row={r['graph6']:r for r in certs['records']}
assert len(record_by_row)==39

n_relevant=0
for idx,row in enumerate(rows,1):
 H=decode_graph6(row)
 assert triangle_free(H)
 if sum(a.bit_count() for a in H)!=66:continue
 n_relevant+=1
 assert not indep_sets(H,6),('independent six',idx)
 F=indep_sets(H,5)
 r=record_by_row.pop(row.decode('ascii'))
 assert r['source_index']==idx
 pmap={tuple(map(int,k.split(','))):c for k,c in r['signed_pair_coefficients'].items()}
 pairs=[(u,v) for u,v in combinations(range(16),2) if not(H[u]>>v&1)]
 assert len(pairs)==87
 assert set(pmap).issubset(pairs)
 assert all(isinstance(c,int) for c in pmap.values())
 # The nonnegative weight on I is the sum of its 10 signed pair potentials.
 weights=[]
 for I in F:
  weight=sum(pmap.get((u,v),0) for u,v in pairs if I>>u&1 and I>>v&1)
  weights.append(weight)
 assert min(weights)>=0,(idx,'negative five-set weight')
 minimum=min(sum(weights[i] for i,I in enumerate(F) if (I&T)==0) for T in F)
 total=sum(weights)
 assert minimum==r['min_coverage']
 assert total==r['total_weight']
 assert min(weights)==r['min_five_weight']
 assert minimum>0 and total<6*minimum
 assert 6*minimum-total==r['exact_margin']
print('PASS',n_relevant,'signed pair certificates; all five-set weights nonnegative; strict six-port gap')
assert n_relevant==39 and not record_by_row

# For each of six identified graphs, verify a primal-independent exact dual
# guaranteeing no NONNEGATIVE pair coefficients can achieve mass below six.
nonnegative_duals=certs['nonnegative_pair_duality_obstructions']
assert len(nonnegative_duals)==6
assert sorted(r['source_index'] for r in nonnegative_duals)==[412,927,972,973,1253,1813]
rows_by_index={i:row for i,row in enumerate(rows,1)}
for r in nonnegative_duals:
 H=decode_graph6(rows_by_index[r['source_index']])
 F=indep_sets(H,5)
 dual={int(k):int(v) for k,v in r['dual_weights'].items()}
 den=r['denominator']
 assert den>0 and set(dual).issubset(F)
 assert all(v>=0 for v in dual.values())
 assert sum(dual.values())==r['numerator'] and r['numerator']>6*den
 for u,v in combinations(range(16),2):
  if H[u]>>v&1:continue
  containing=[I for I in F if I>>u&1 and I>>v&1]
  total_containing=len(containing)
  # B[T,e]=#{I independent5: e⊆I, T∩I=empty}
  # Verify sum_T dual[T] B[T,e] <= den*#{I:e⊆I}.
  dual_sum=sum(dual.get(T,0)*sum((I&T)==0 for I in containing) for T in F)
  assert dual_sum<=den*total_containing,(r['source_index'],u,v,dual_sum,den*total_containing)
print('PASS',len(nonnegative_duals),'independent dual certificates: nonnegative pair potentials cannot give mass <6')

# An exact dual proves that *even signed* vertex-additive potentials cannot
# achieve the six-port threshold on graph 1253. This establishes genuine
# pair-order necessity in this additive incidence hierarchy.
one=json.loads((ROOT/'ramsey_vertex_affine_dual_1253.json').read_text())
assert one['source_index']==1253
H=decode_graph6(rows_by_index[1253]);F=indep_sets(H,5)
assert one['graph6']==rows_by_index[1253].decode()
la={int(k):int(v) for k,v in one['lambda_coverage'].items()}
et={int(k):int(v) for k,v in one['eta_nonnegative'].items()}
den=one['denominator']
assert den>0 and set(la).issubset(F) and set(et).issubset(F)
assert all(v>=0 for v in la.values()) and all(v>=0 for v in et.values())
assert sum(la.values())==one['lambda_numerator'] and sum(la.values())>6*den
for v in range(16):
  # B[T,v] = #{I∈F: I avoids T and contains v}
  term_coverage=sum(la.get(T,0)*sum((I&T)==0 and (I>>v&1) for I in F) for T in F)
  term_positive=sum(et.get(I,0) for I in F if (I>>v&1))
  total_presence=sum(bool(I>>v&1) for I in F)
  assert term_coverage+term_positive==den*total_presence,(v,term_coverage,term_positive,den*total_presence)
print('PASS signed vertex-additive lower bound: mass >= %d/%d >6 on graph 1253' % (one['lambda_numerator'],den))
