import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp = json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
G, qs, qp, y2 = sp.symbols("G qs qp y2", positive=True)
x, z, xi = sp.symbols("x z xi", real=True)
VD = G*(qs*x+qp*z-xi)**2/2
hD = sp.factor(2*sp.diff(sp.diff(VD,x),z))
hF = y2
assert hD == 2*G*qs*qp
lo = sp.Rational(wp["reconstructed_r_outer_bracket"]["lower"])
hi = sp.Rational(wp["reconstructed_r_outer_bracket"]["upper"])
hlo = sp.factor(1/(17*hi**2))
hhi = sp.factor(1/(17*lo**2))
r = lambda h: 1/sp.sqrt(17*h)
assert hlo < 1 < hhi
assert lo < r(1) < hi and r(2) < lo
dD = sp.factor(sp.diff(r(hD),G))
dF = sp.factor(sp.diff(r(hF),y2))
assert dD != 0 and dF != 0
result = {
 "schema":"marici.flavor.wp1032.v1","status":"PASS",
 "question":"Do minimal D-term or F-term protected completions fix the WP1031 single-pole normalization?",
 "admitted_state_domain":"one spectator pole over N=17 equal condensates, with either one Abelian moment-map square or N identical auxiliary/Yukawa squares",
 "D_term":{"potential":str(VD),"effective_h":str(hD),"ratio":str(r(hD)),"continuous_response":str(dD)},
 "F_term":{"effective_h":str(hF),"ratio":str(r(hF)),"continuous_response":str(dF)},
 "N17_data_compatible_h_interval":{"lower":str(hlo),"upper":str(hhi)},
 "contextual_partition":"fixed charge and Clebsch data partition constructors by discrete representation, but each class retains a continuous G or |y|^2 fiber",
 "smallest_exact_falsifier":"at fixed N=17 and fixed charges/Clebsches, h=1 lies inside the fitted interval while h=2 gives r=1/sqrt(34) below it",
 "classification":"protected relative rigidifier, not absolute selector",
 "instrument":"pole mass and condensate scale measure h; they do not derive or decompose its normalization",
 "remaining_gate":"a source-derived normalization theorem fixing 2G qs qp=1 or |y|^2=1, plus a typed nondecoupling realization",
 "claim_boundary":"closes minimal one-moment-map and identical-auxiliary-square completions; not genuinely quantized topological couplings or separately proved gauge-Yukawa fixed points",
 "disposition":"negative: protection locks relations but preserves one continuous normalization fiber"}
out=ROOT/"results"/"wp1032_protected_single_pole_normalization_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print("WP1032 PASS:",hD,hF,hlo,hhi)
