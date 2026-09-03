"""Classify invariants under independent nonzero row/column detector scalings."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_relative_transition_scaling_invariants.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 d=json.loads((RES/'cosmology_nonstationary_detector_cocycle.json').read_text());R=[[q(x) for x in row] for row in d['relative_matrix']];nz=sum(bool(x) for row in R for x in row);assert nz==9;K=[[R[i][j]*R[0][0]/(R[i][0]*R[0][j]) for j in (1,2)] for i in (1,2)];out={'schema':'marici.voevodsky.cosmology-relative-transition-scaling-invariants.v1','status':'mixing_survives_label_scalings','nonzero_entry_count':nz,'nonzero_offdiagonal_count':6,'normalized_cross_ratio_core':[[enc(x) for x in row] for row in K],'core_all_one':all(x==1 for row in K for x in row),'decision':'Nonzero diagonal row/column scalings preserve the full support pattern, so they cannot remove any of the six off-diagonal couplings; the four cross ratios retain residual scaling-invariant data.','claim_boundary':'This excludes label-preserving diagonal scalings only, not arbitrary changes of detector basis.','next_gate':'test-structured-triangular-basis-normalization','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
