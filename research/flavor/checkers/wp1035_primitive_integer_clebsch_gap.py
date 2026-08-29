import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
lo=sp.Rational(wp["reconstructed_r_outer_bracket"]["lower"])
hi=sp.Rational(wp["reconstructed_r_outer_bracket"]["upper"])
hlo=sp.factor(1/(17*hi**2))
hhi=sp.factor(1/(17*lo**2))
y2=12*sp.pi**2/1367
C=sp.symbols("C",integer=True,positive=True)

pi_lo=sp.Rational(333,106)
pi_hi=sp.Rational(22,7)
assert pi_lo < sp.pi < pi_hi
h11_upper=sp.factor(11*sp.Rational(12,1367)*pi_hi**2)
h12_lower=sp.factor(12*sp.Rational(12,1367)*pi_lo**2)
assert h11_upper < hlo
assert h12_lower > hhi

# Monotonicity in positive integer C makes 11 and 12 the adjacent exact
# falsifiers; no positive integer lies between them.
assert sp.diff(C*y2,C)>0

result={"schema":"marici.flavor.wp1035.v1","status":"PASS",
 "question":"Can an integer Clebsch or multiplicity C repair the primitive WP802-to-pole interface h=C y^2?",
 "domain":"primitive epsilon=1/20 packet (N_C,N_F)=(20,111), C a positive integer",
 "map":"h=C*12*pi^2/1367",
 "adjacent_falsifiers":{"C=11_upper":str(h11_upper),"C=12_lower":str(h12_lower)},
 "compatible_h_interval":{"lower":str(hlo),"upper":str(hhi)},
 "contextual_partition":"C<=11 lies below the compatible class; C>=12 lies above; the compatible integer class is empty",
 "smallest_exact_falsifier":"the adjacent integers C=11 and C=12 straddle the entire fitted h interval using rational pi bounds",
 "classification":"integer rigidifier with empty admissible readout; not a selector",
 "instrument":"not reached because the source prediction is excluded before thresholds",
 "remaining_gate":"a non-integer coefficient would be continuous normalization unless independently fixed by a source theorem; nonprimitive k>1 requires a separately derived multiplicity law",
 "claim_boundary":"primitive k=1 WP802 packet with a single positive integer coefficient; does not exclude source-derived algebraic Clebsches or nonprimitive packets",
 "disposition":"negative: ordinary integer multiplicity cannot bridge the controlled fixed point to the N=17 pole"}
(ROOT/"results"/"wp1035_primitive_integer_clebsch_gap.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1035 PASS:",h11_upper,hlo,hhi,h12_lower)
