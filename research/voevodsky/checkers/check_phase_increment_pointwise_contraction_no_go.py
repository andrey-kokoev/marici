"""Exact hostile fixture for pointwise contraction of the two phase increments."""
from fractions import Fraction
import json
from pathlib import Path
# Normalize x=1 and choose u=pi, v=0, represented by exact phase data.
u2=Fraction(1); v2=Fraction(0)  # common factor pi^2 omitted
# Both phase increments have |1-exp(i*pi)|^2=4.
r_minus_sq=Fraction(1,2)*(u2-v2)*4
r_plus_sq=Fraction(1,2)*(u2+v2)*4
residual=r_minus_sq+r_plus_sq
bulk=2*(u2+v2)
out={'fixture':'xu=pi, xv=0','common_pi_squared_factor_omitted':True,'r_minus_squared':str(r_minus_sq),'r_plus_squared':str(r_plus_sq),'residual_squared':str(residual),'pointwise_bulk_squared':str(bulk),'residual_over_bulk':str(residual/bulk),'pointwise_contraction':residual<=bulk,'conclusion':'No fiberwise multiplier, projection, or pointwise partial isometry can realize the desired contraction. Any successful sewing must be nonlocal in the two-copy source coordinates.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'phase-increment-pointwise-contraction-no-go.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
