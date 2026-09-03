"""Exact Fourier-multiplier admissibility check for the preconditioned spline."""
from fractions import Fraction as F
import json
from pathlib import Path

# For x=cos(theta), 2 cos(2 theta)-10 cos(theta)+33/4.
# Coefficients in ascending powers of x.
baseline=[F(25,4),F(-10),F(4)]
square=[F(25,4),F(-10),F(4)]  # (2x-5/2)^2
assert baseline==square
# Vertex 5/4 lies outside [-1,1]; polynomial decreases there, so minimum is at x=1.
minimum=sum(baseline)
assert minimum==F(1,4)>0

# Deliberate rival: central coefficient 6 gives 4x^2-10x+4 and is negative at x=1.
rival=[F(4),F(-10),F(4)]
rival_at_one=sum(rival)
assert rival_at_one==F(-2)<0

# Symmetry- and sum-preserving perturbation eps*(1,0,-2,0,1).
eps=F(3,10**6)
# Multiplier is baseline + 4 eps (x^2-1). Its vertex is right of 1 for eps<1/4,
# so it decreases on [-1,1] and retains the exact minimum 1/4 at x=1.
assert F(5,4*(1+eps))>1
perturbed_minimum=minimum
assert perturbed_minimum==F(1,4)>0

# The Laurent multiplier is (z+z^-1-5/2)^2: it has double pole-killing zeros at z=2,1/2.
def laurent(z,c): return c[0]*z*z+c[1]*z+c[2]+c[3]/z+c[4]/(z*z)
def laurent_derivative(z,c): return 2*c[0]*z+c[1]-c[3]/(z*z)-2*c[4]/(z**3)
base_coeff=[F(1),F(-5),F(33,4),F(-5),F(1)]
assert laurent(F(2),base_coeff)==0 and laurent_derivative(F(2),base_coeff)==0
perturbed=[base_coeff[i]+eps*[F(1),F(0),F(-2),F(0),F(1)][i] for i in range(5)]
assert laurent(F(2),perturbed)==F(9,4)*eps>0

# Exact rank-two solve in symmetric coordinates (u,v,w,v,u).
u=F(7,3);v=-5*u;w=F(33,4)*u
assert F(15,4)*u+F(3,4)*v==0  # P'(2)=0
assert F(17,4)*u+F(5,2)*v+w==0  # P(2)=0
assert v/u==-5 and w/u==F(33,4)

out={
    "schema":"marici.preconditioned-spline-admissibility.v1",
    "multiplier_factor":"(2 cos(theta)-5/2)^2",
    "unit_circle_minimum":"1/4",
    "base_fourier_factor":"nonnegative sinc^8 factor",
    "baseline_fourier_nonnegative":True,
    "deliberate_rival_central_coefficient":"6",
    "deliberate_rival_value_at_theta_0":"-2",
    "deliberate_rival_fourier_nonnegative":False,
    "admissible_sign_reversal_epsilon":"3/1000000",
    "admissible_sign_reversal_multiplier_minimum":"1/4",
    "baseline_pole_multiplier_at_2":"0 (double zero)",
    "perturbed_pole_multiplier_at_2":"27/4000000",
    "pole_annihilating_symmetric_ray":"u*(1,-5,33/4,-5,1)",
    "ray_gram_sign":"sign(u) times positive baseline",
    "scope":"source-independent analytic admissibility; not source normalization or Weil-criterion authority"
}
path=Path('research/nima/results/preconditioned_spline_admissibility.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
