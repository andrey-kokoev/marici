import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp1025 = json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
lo = sp.Rational(wp1025["reconstructed_r_outer_bracket"]["lower"])
hi = sp.Rational(wp1025["reconstructed_r_outer_bracket"]["upper"])

# Values derived upstream without using WP1025.  Their source packets select
# ratios in their own typed domains; none declares a covariant map to f/M.
candidates = {
 "WP309 reciprocal fixed point": sp.Integer(1),
 "WP312 exchange-symmetric vacuum": sp.Integer(1),
 "WP316 unit-flux lower reciprocal branch": sp.sqrt(2)-1,
 "WP132 Higgs-flavon amplitude ratio": 1/sp.sqrt(2),
 "WP760 minimal tadpole T=3": sp.Integer(2),
 "WP760 minimal tadpole T=4": sp.Integer(3),
}
declared_f_over_M_interfaces = {name: False for name in candidates}
identity_hits = {
 name: bool(value > lo and value < hi) for name,value in candidates.items()
}
assert not any(declared_f_over_M_interfaces.values())
assert not any(identity_hits.values())

# Deliberate authority obstruction: a free positive scale maps every nonzero
# source ratio to any target in the fitted interval.  Therefore numerical
# compatibility after scaling does not define the missing interface.
target = (lo+hi)/2
scales = {name: sp.simplify(target/value) for name,value in candidates.items()}
assert all(sp.simplify(scale*value-target)==0
           for (name,value),scale in zip(candidates.items(),scales.values()))
assert len(set(map(str,scales.values()))) > 1

result={
 "schema":"marici.flavor.wp1027.v1","status":"PASS",
 "question":"Does any previously source-derived flavor ratio already select the WP1025 threshold coordinate r=f/M?",
 "admitted_source_ratio_family":{k:str(v) for k,v in candidates.items()},
 "faithful_target_coordinate":"WP90 threshold ratio r=f/M on the WP1025 branch",
 "target_interval":{"lower":str(lo),"upper":str(hi)},
 "declared_source_to_threshold_interfaces":0,
 "identity_interface_hits":sum(identity_hits.values()),
 "contextual_partition":"six upstream selector presentations in five exact value classes; zero typed arrows into f/M",
 "classification":"source selectors exist, but the source-to-threshold interface family is empty; numerical rescaling would be a rigidifier, not selection",
 "smallest_exact_falsifier":"WP309 and WP312 both select 1, yet no admitted operation identifies either ratio with f/M",
 "deliberate_failure":"a freely chosen positive scale maps every candidate exactly to the interval midpoint",
 "instrument":"none of the source-ratio instruments is calibrated as an f/M measurement; CKM only supplies the downstream inverse readout",
 "claim_boundary":"inventory is bounded to the explicitly listed admitted selectors and tests only their declared or identity interfaces",
 "disposition":"negative but locates the missing arrow: construct a source-covariant dimensionless interface into f/M before comparing values"
}
(ROOT/"results"/"wp1027_source_ratio_interface_inventory.json").write_text(
 json.dumps(result,indent=2)+"\n")
print("WP1027 PASS: candidates",len(candidates),"typed interfaces 0 identity hits 0")
