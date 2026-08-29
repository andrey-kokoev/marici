import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
lo=sp.Rational(wp["reconstructed_r_outer_bracket"]["lower"])
hi=sp.Rational(wp["reconstructed_r_outer_bracket"]["upper"])
hlo=sp.factor(1/(17*hi**2)); hhi=sp.factor(1/(17*lo**2))
pi_lo=sp.Rational(103993,33102); pi_hi=sp.Rational(104348,33215)
assert pi_lo < sp.pi < pi_hi
h=lambda C,k: sp.Rational(12*C,1367*k)*sp.pi**2
low=lambda C,k: sp.Rational(12*C,1367*k)*pi_lo**2
high=lambda C,k: sp.Rational(12*C,1367*k)*pi_hi**2

assert high(22,2)<hlo
assert low(23,2)>hlo and high(23,2)<hhi
assert low(24,2)>hhi
assert sp.factor(h(23,2))==138*sp.pi**2/1367

result={"schema":"marici.flavor.wp1036.v1","status":"PASS",
 "question":"Does the nonprimitive integer WP802 family contain an arithmetic pole-compatible packet?",
 "compatible_packet":{"k":2,"N_C":40,"N_F":222,"C":23,"h":"138*pi^2/1367","h_decimal":str(sp.N(h(23,2),18))},
 "adjacent_falsifiers":{"C=22":"below","C=24":"above"},
 "compatible_h_interval":{"lower":str(hlo),"upper":str(hhi)},
 "contextual_partition":"at fixed k=2, C<=22 is below, C=23 compatible, and C>=24 above",
 "smallest_exact_falsifier":"the same k=2 source permits adjacent integer coefficients C=22 and C=24 unless a representation theorem selects C=23",
 "classification":"arithmetic capacity point and presentation rigidifier only; not a source selector",
 "instrument":"not established; thresholds and physical16 calibration remain downstream",
 "remaining_gate":"derive k=2 and C=23 from one anomaly-complete representation and a typed pole operator, independently of the fitted interval",
 "claim_boundary":"proves existence and uniqueness only within the k=2 positive-integer coefficient slice; no authority for choosing that slice",
 "disposition":"progressive capacity: a compatible integer lift exists, but selection authority is absent"}
(ROOT/"results"/"wp1036_nonprimitive_integer_lift_capacity.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1036 PASS:",h(23,2),sp.N(h(23,2),18))
