import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_order_four_interpolated_hurwitz_minors.py')));ad,hm=g['ad'],g['hurwitz_minor'];A=[F(1),F(4),F(1)];Q=[F(3),F(2),F(1)];out=ad(A,Q,-1)
def stable(p):return p[-1]>0 and all(hm(p,k)>0 for k in range(1,len(p)))
checks={'A_stable':stable(A),'Q_stable':stable(Q),'output_2x_minus2':out==[F(-2),F(2)],'output_unstable':not stable(out)};r={'schema':'marici.strominger.rh_D_condensation_generic_stability_counterexample.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Generic stability preservation is exactly refuted; D-specific cross-input structure is required.','output':'2x-2','checks':checks};(base/'results'/'rh_D_condensation_generic_stability_counterexample.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
