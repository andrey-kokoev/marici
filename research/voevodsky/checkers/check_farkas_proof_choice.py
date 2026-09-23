"""Two valid Farkas certificates for the same target relation have different surplus."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky/results'
prior=json.loads((V/'farkas-surplus-transport.json').read_text());assert prior['passed']
# Source interval 0<=x<=1 at reference 0: A=(-1,1), residual=(0,1).
A=(-Q(1),Q(1));r=(Q(0),Q(1));d=Q(1,4)
# Target x<=2 at reference d has normal 1, residual 2-d.
target_normal=Q(1);target_residual=Q(2)-d
certificates=[]
for M in ((Q(0),Q(1)),(Q(1),Q(2))):
 normal=sum(x*a for x,a in zip(M,A));bound=sum(x*b for x,b in zip(M,r))
 surplus=target_residual-(bound-normal*d)
 assert normal==target_normal and surplus>=0 and all(x>=0 for x in M)
 certificates.append({'multiplier':list(map(str,M)),'surplus':str(surplus)})
assert certificates[0]['surplus']=='1' and certificates[1]['surplus']=='0'
assert certificates[0]!=certificates[1]
# Both proof packets target exactly the same inequality and reference shift;
# proof choice, not presentation difference, is responsible for surplus.
assert target_residual==Q(7,4)
# Any attempted semantic invariant assigning a unique surplus to this
# source/target inclusion is contradicted by these two valid arrows.
report={'passed':True,'same_source_target':'[0,1] included in x<=2 at reference 1/4','target_residual':'7/4','certificates':certificates,'surplus_not_determined_by_inclusion':True,'scope':'One rational nonnegative Farkas inclusion with two proof choices; no claim that all proofs are homotopic or that analytic residues are absent.'}
(V/'farkas-proof-choice.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
