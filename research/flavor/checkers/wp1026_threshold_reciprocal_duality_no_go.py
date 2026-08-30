import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
WP1025 = json.loads((ROOT / "results" / "wp1025_threshold_cube_inverse_readout.json").read_text())
r, kappa = sp.symbols("r kappa", positive=True)
V = (r - kappa**2 / r) ** 2
dV = sp.factor(sp.diff(V, r))
d2V = sp.factor(sp.diff(V, r, 2))
positive_stationary = [x for x in sp.solve(dV, r) if x.is_positive]
assert positive_stationary == [kappa]
assert sp.simplify(d2V.subs(r, kappa)) == 8
assert sp.diff(positive_stationary[0], kappa) == 1
assert positive_stationary[0].subs(kappa, 1) == 1
assert 1 > sp.Rational(1, 4)
quarter = sp.Rational(1, 4)
assert positive_stationary[0].subs(kappa, quarter) == quarter
outer = WP1025["reconstructed_r_outer_bracket"]
outer_lo = sp.Rational(outer["lower"])
outer_hi = sp.Rational(outer["upper"])
assert 0 < outer_lo < outer_hi < quarter
P = (12878670000*r**8 + 16583280000*r**7 + 10789212400*r**6
     + 4331604000*r**5 + 1454241747*r**4 + 398819200*r**3
     + 90718200*r**2 + 10800000*r + 1687500)
J2 = sp.factor(400*r**6/(3*P))
quarter_J2 = sp.factor(J2.subs(r, quarter))
assert quarter_J2 == sp.Rational(WP1025["endpoint_J_squared"])
# Deliberate nonzero obstruction: the fitted edge is not the quarter fixed point.
assert outer_hi != quarter
result = {
 "schema":"marici.flavor.wp1026.v1","status":"PASS",
 "question":"Can reciprocal duality independently select the reconstructed WP1025 threshold ratio?",
 "admitted_state_domain":"positive threshold ratios r=f/M, with WP1025 EFT branch 0<r<=1/4",
 "candidate_source_operation":"generalized reciprocal involution r -> kappa^2/r",
 "stationary_locus":"r=kappa","stationary_hessian":"8",
 "normalization_response_rank":1,"canonical_fixed_point":"1",
 "quarter_normalized_fixed_point":"1/4",
 "fitted_outer_r_bracket":{"lower":str(outer_lo),"upper":str(outer_hi)},
 "quarter_J_squared":str(quarter_J2),
 "ensemble_sheets_rejected_by_quarter_prediction":WP1025["ensemble_sheets_tested"],
 "classification":"canonical duality is incompatible; quarter duality is a normalization rigidifier with a false numerical prediction, not a source selector",
 "smallest_exact_falsifier":"the fitted upper inverse bracket is strictly below 1/4",
 "instrument":"CKM/Jarlskog readout falsifies the quarter prediction conditionally on the WP90 threshold map; no executable reciprocal source operation is admitted",
 "claim_boundary":"closes reciprocal-duality selection on r and the rescaled q=4r proposal; it does not close independently derived non-duality source equations",
 "disposition":"negative but useful"
}
out=ROOT/"results"/"wp1026_threshold_reciprocal_duality_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print("WP1026 PASS: r=1 outside branch; r=1/4 above fitted",float(outer_hi))
