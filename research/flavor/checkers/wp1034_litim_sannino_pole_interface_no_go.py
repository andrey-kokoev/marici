import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
lo=sp.Rational(wp["reconstructed_r_outer_bracket"]["lower"])
hi=sp.Rational(wp["reconstructed_r_outer_bracket"]["upper"])
k=sp.symbols("k",integer=True,positive=True)

# epsilon=N_F/N_C-11/2=1/20 forces the primitive integer ray
# (N_C,N_F)=(20k,111k).
Nc=20*k
Nf=111*k
assert sp.simplify(Nf/Nc-sp.Rational(11,2))==sp.Rational(1,20)
alpha_y=sp.Rational(15,1367)
y2=sp.factor(16*sp.pi**2*alpha_y/Nc)
assert y2==12*sp.pi**2/(1367*k)

# Exact rational upper bound pi<22/7 proves the entire integer family misses
# the WP1032 compatible h interval.
y2_upper=sp.Rational(12,1367)/k*sp.Rational(22,7)**2
assert sp.pi < sp.Rational(22,7)
assert y2_upper.subs(k,1) < lo
r=1/sp.sqrt(17*y2)
assert sp.simplify(sp.diff(r,k))>0

result={"schema":"marici.flavor.wp1034.v1","status":"PASS",
 "question":"If WP802's fixed Yukawa is charitably identified with the WP1032 pole coupling, can any exact integer epsilon=1/20 realization fit the required h interval?",
 "granted_interface":"h=y^2 with alpha_y=y^2 N_C/(4 pi)^2",
 "integer_family":{"N_C":"20*k","N_F":"111*k","k_domain":"positive integers"},
 "fixed_coordinate":{"alpha_y":"15/1367","h":"12*pi^2/(1367*k)"},
 "exact_upper_bound":"h < 5808/(66983*k) <= 5808/66983",
 "compatible_h_lower":str(sp.factor(1/(17*hi**2))),
 "contextual_partition":"integer source packets k>=1 form distinct fixed-point realizations, all in one rejected below-threshold class",
 "smallest_exact_falsifier":"the maximal case k=1 already obeys h<5808/66983, below the fitted compatible interval",
 "classification":"neither selector nor rigidifier for the pole; even the unauthorized direct interface predicts the wrong magnitude",
 "instrument":"not reached; the numerical failure precedes threshold matching and physical16 calibration",
 "claim_boundary":"uses the WP802 epsilon=1/20 perturbative packet and the strongest direct h=y^2 identification; does not cover other epsilon or other fixed-point theories",
 "disposition":"negative: the controlled WP802 fixed point cannot normalize the N=17 pole on its exact integer source family"}
(ROOT/"results"/"wp1034_litim_sannino_pole_interface_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1034 PASS:",y2,y2_upper.subs(k,1),lo)
