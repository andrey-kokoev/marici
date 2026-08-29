import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp1025=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
lo=sp.Rational(wp1025["reconstructed_r_outer_bracket"]["lower"])
hi=sp.Rational(wp1025["reconstructed_r_outer_bracket"]["upper"])

# Common-source candidate: N equal orthogonal mass contributions of norm f
# give M^2=N f^2 and hence r=f/M=1/sqrt(N).
compatible=[N for N in range(1,1001) if 1/sp.sqrt(N)>lo and 1/sp.sqrt(N)<hi]
assert compatible==[17]
assert 1/sp.sqrt(16)>hi
assert 1/sp.sqrt(18)<lo

r=sp.symbols("r",positive=True)
P=(12878670000*r**8+16583280000*r**7+10789212400*r**6+
   4331604000*r**5+1454241747*r**4+398819200*r**3+
   90718200*r**2+10800000*r+1687500)
J2=sp.factor(400*r**6/(3*P))
r17=1/sp.sqrt(17)
J2_17=sp.factor(J2.subs(r,r17))
Js2=[abs(sp.Rational(str(row["J"])))**2 for row in ensemble["records"]]
below=len([j for j in Js2 if j<J2_17])
above=len([j for j in Js2 if j>J2_17])
equal=len([j for j in Js2 if j==J2_17])
assert (below,above,equal)==(18,1192,0)
assert min(Js2)<J2_17<max(Js2)

# Deliberate-failure tests: neighbouring integer multiplicities miss the
# complete reconstructed interval on opposite sides.
assert not (lo<1/sp.sqrt(16)<hi)
assert not (lo<1/sp.sqrt(18)<hi)

result={
 "schema":"marici.flavor.wp1028.v1","status":"PASS",
 "question":"Can a common-source integer mass norm replace the free threshold normalization?",
 "admitted_candidate_domain":"positive integer N equal orthogonal mass contributions with M^2=N f^2",
 "faithful_threshold_coordinate":"r=f/M=1/sqrt(N)",
 "compatible_integer_multiplicities":[17],
 "selected_candidate_ratio":"1/sqrt(17)",
 "exact_predicted_J_squared":str(J2_17),
 "predicted_abs_J_float":float(sp.sqrt(J2_17)),
 "ensemble_partition":{"below_prediction":below,"above_prediction":above,"equal_prediction":equal},
 "neighbour_falsifiers":{"N=16":"above reconstructed interval","N=18":"below reconstructed interval"},
 "classification":"discrete common-source interface family with a unique data-compatible member; conditional selector if and only if source theory independently derives N=17",
 "smallest_exact_falsifier":"the adjacent multiplicities 16 and 18 miss the fitted interval on opposite sides",
 "instrument":"requires spectroscopy or a source-count observable proving seventeen equal orthogonal mass contributions; CKM alone cannot authorize N",
 "claim_boundary":"does not derive N=17, equal contribution norms, radiative stability, or a physical messenger realization",
 "disposition":"progressive candidate, not yet an admitted source selector"
}
(ROOT/"results"/"wp1028_integer_mass_norm_window.json").write_text(
 json.dumps(result,indent=2)+"\n")
print("WP1028 PASS: unique N=17, |J|",float(sp.sqrt(J2_17)),below,above,equal)
