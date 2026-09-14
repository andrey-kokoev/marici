#!/usr/bin/env python3
"""Exact finite interval-Gram checks supporting the cutoffwise L2 bound."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/common_radial_history_has_a_cutoffwise_half_line_L2_bound_20260911.md'
SOURCE=ROOT/'research/nima/a-spanning-forest-cycle-port-is-the-minimal-finite-observer-completing-common-radial-history.md'
RANK=ROOT/'research/nima/the-diagonal-shell-wronskian-family-is-infinite-rank-and-cannot-factor-through-the-scalar-wall-incidence-plane.md'
RESULT=ROOT/'research/voevodsky/results/common_radial_history_half_line_L2_bound.json'
# Oriented interval relation [0,1]+[1,2]-[0,2]=0 almost everywhere.
intervals=[(s.Rational(0),s.Rational(1)),(s.Rational(1),s.Rational(2)),(s.Rational(0),s.Rational(2))]
def overlap(x,y): return s.Max(0,s.Min(x[1],y[1])-s.Max(x[0],y[0]))
G=s.Matrix([[overlap(x,y) for y in intervals] for x in intervals]); c=s.Matrix([1,1,-1])
lengths=[b-a for a,b in intervals]; support=max(b for _,b in intervals)-min(a for a,_ in intervals); total=sum(lengths)
source_text=SOURCE.read_text(); rank_text=RANK.read_text()
checks={
 'Gram_exact':G==s.Matrix([[1,0,1],[0,1,1],[1,1,2]]),
 'Gram_positive_semidefinite':all(v>=0 for v in G.eigenvals()),
 'cycle_witness_in_kernel':G*c==s.zeros(3,1) and c!=s.zeros(3,1),
 'cycle_indicator_norm_zero':(c.T*G*c)[0]==0,
 'trace_equals_total_edge_length':s.trace(G)==total==4,
 'largest_eigenvalue_bounded_by_trace':max(G.eigenvals())<=s.trace(G),
 'support_diameter_exact':support==2,
 'cutoff_constant_combinatorial_factor':s.sqrt(support*total)==2*s.sqrt(2),
 'history_source_formula_present':'B_Dc(t)' in source_text and 'J_Dc' in source_text,
 'source_cycle_kernel_present':'ker B_D=Z_1(G_D)' in source_text,
 'Gaussian_tail_recorded':'double-exponential decay rates' in rank_text and 'exp' in rank_text,
 'packet_discloses_cutoff_dependence':'No cutoff-uniform bound' in PACKET.read_text(),
}
# Hostile omission of overlap changes the norm and is detected.
Gbad=s.diag(1,1,2)
checks['overlap_free_hostile_rejected']=(c.T*Gbad*c)[0]!=0
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.common-radial-history-half-line-L2-bound-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'source_history':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'source_decay':hashlib.sha256(RANK.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'fixture':{'intervals':[[str(a),str(b)] for a,b in intervals],'Gram':[[str(x) for x in row] for row in G.tolist()],'support_diameter':str(support),'total_edge_length':str(total),'bound_factor_without_Phi_norms':str(s.sqrt(support*total))},'disposition':{'constructed':'cutoffwise bounded map into half-line L2 conditional on recorded Phi L2 and Linfinity decay','retained_kernel':'cycle space requires spanning-forest port','remaining':'uniform cutoff growth and compatible cycle-port transitions'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'Gram_rank':G.rank(),'cycle_kernel_dimension':3-G.rank()}))
raise SystemExit(0 if result['passed'] else 1)
