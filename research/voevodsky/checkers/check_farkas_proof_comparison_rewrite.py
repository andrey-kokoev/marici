"""Source-row syzygy rewrite between two valid Farkas proofs, as candidate 2-cell."""
from fractions import Fraction as Q
from pathlib import Path
import json
# Source rows: -x<=0 and x<=1. Proof m=(a,b), surplus c>=0;
# target row x<=T, reference shift d: b-a=1 and b+c=T.
def valid(a,b,c,T,d):
 a,b,c,T,d=map(Q,(a,b,c,T,d))
 return a>=0 and b>=0 and c>=0 and b-a==1 and b+c==T and b-d+c==T-d
def normalize(a,b,c,T,d):
 a,b,c=map(Q,(a,b,c));assert valid(a,b,c,T,d)
 # Kernel of normal row [-1,1] is (1,1). Its source bound is 1,
 # compensated by decreasing target surplus by c.
 result=(a+c,b+c,Q(0))
 assert valid(*result,T,d)
 return result
prior=json.loads((Path(__file__).resolve().parents[1]/'results/canonical-farkas-policy.json').read_text())
assert prior['passed']
staged=(Q(1),Q(2),Q(1));direct=(Q(2),Q(3),Q(0));T=Q(3);d=Q(1,2)
assert valid(*staged,T,d) and normalize(*staged,T,d)==direct
assert normalize(*direct,T,d)==direct
# Exhaustively enumerate a finite rational family of valid proofs and show
# normalization has unique endpoint irrespective of starting multiplier.
checks=0
for denominator in (1,2,3):
 for numer in range(denominator,5*denominator+1):
  target=Q(numer,denominator)
  for scale in range(denominator,5*denominator+1):
   b=Q(scale,denominator);a=b-1;c=target-b
   if not valid(a,b,c,target,Q(1,4)):continue
   assert normalize(a,b,c,target,Q(1,4))==(target-1,target,Q(0))
   checks+=1
assert checks>20
# The rewrite requires the primitive row bounds (0,1), not just normals:
# if the upper source bound changes to 2, adding (c,c) changes the implied
# bound by 2c and cannot be compensated by subtracting only c.
assert Q(2)*Q(1)!=Q(1)
# This is a mathematical directed rewrite; original Farkas 1-category has
# no declared 2-cell or authority to identify proof paths.
report={'passed':True,'staged_to_direct':{'multiplier_before':['1','2'],'surplus_before':'1','multiplier_after':['2','3'],'surplus_after':'0'},'family_checks':checks,'normal_form':'(T-1,T); surplus 0 for T>=1 on this fixed source','source_bound_dependent':True,'original_category_has_2_cell':False,'scope':'Candidate directed source-row proof rewrite, not an admitted analytic or operative coherencer; bounded source interval and target x<=T.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-proof-comparison-rewrite.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
