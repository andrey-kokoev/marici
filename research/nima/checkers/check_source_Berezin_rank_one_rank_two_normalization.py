"""Calibrate ordered Grassmann normalization independently at k=1 and k=2."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=(ROOT/'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex').read_text()
assert r'd^4 \phi_1 \dots d^4 \phi_k' in source
prior=json.loads((OUT/'four-mass-Y0-Berezin-component.json').read_text());assert prior['passed']
assert prior['det_Ch_fourth_power_top_fermion_coefficient']==2880
assert all(r['extracted_over_sourced_psi']=='2880' for r in prior['witnesses'])
# Independent n=5, k=1 simplex calibration: one root of C z=0.
z=s.Matrix([[j**d for d in range(4)] for j in range(1,6)])
unknowns=-z[0,:]*z[1:5,:].inv();C=s.Matrix([[1,*unknowns]])
assert C*z==s.zeros(1,4) and all(C[0,i]!=0 for i in range(1,5))
def br(i,j,k,l):return z[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
jz=z[1:5,:].det(method='domain-ge')
raw_r_invariant_component=s.factor(s.prod(C[0,i]**(-1) for i in range(1,5))/jz)
five_bracket_den=s.prod(br(*seq) for seq in ((1,2,3,4),(2,3,4,5),(3,4,5,1),(4,5,1,2),(5,1,2,3)))
five_bracket_eta1_component=br(2,3,4,5)**4/five_bracket_den
intrinsic_sign=s.factor(raw_r_invariant_component/five_bracket_eta1_component)
assert intrinsic_sign in (-1,1)
# The actual exterior top coefficient of (sum_A phi_A eta_A)^4 is +4!.
def multiply(A,B):
 out={}
 for ma,ca in A.items():
  for mb,cb in B.items():
   if ma&mb:continue
   swaps=sum((mb&((1<<i)-1)).bit_count() for i in range(8) if ma>>i&1)
   mask=ma|mb;out[mask]=out.get(mask,0)+(-1 if swaps%2 else 1)*ca*cb
 return {m:c for m,c in out.items() if c}
one={(1<<a)|(1<<(4+a)):1 for a in range(4)}
top={0:1}
for _ in range(4):top=multiply(top,one)
assert top=={(1<<8)-1:24}
rank1_extracted_ratio=24*intrinsic_sign
# No independent per-phi-row normalizing scalar can absorb BOTH 4!
# (one row) and 5!(4!) (two rows), since 2880/24^2=5.
assert s.Rational(2880,24**2)==5
report={'schema':'marici.nima.source-Berezin-rank-one-rank-two-normalization.v1','passed':True,
 'rank_one_raw_source_form_to_five_bracket_component_sign':str(intrinsic_sign),
 'rank_one_ordered_Berezin_top_coefficient':24,
 'rank_one_raw_extracted_to_five_bracket_component_ratio':str(rank1_extracted_ratio),
 'rank_two_ordered_Berezin_top_coefficient':2880,
 'rank_two_raw_extracted_to_starred_psi_ratio_at_two_targets':'2880',
 'extra_nonfactorizing_rank_two_factor':5,
 'scope':'A direct rank-one simplex and independent rank-two full component exhibit a factor-five discrepancy from the square of a single row normalization. This only excludes a normalization explained solely by assigning the same scalar to each d^4phi row; projective delta, invariant volume and source five-bracket orientation may carry additional k-dependent conventions. No claim that the cited primary source is wrong.'}
(OUT/'source-Berezin-rank-one-rank-two-normalization.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'rank_one_component_sign':str(intrinsic_sign),
 'rank_one_raw_ratio':str(rank1_extracted_ratio),'rank_two_vs_two_rows_factor':5},indent=2))
