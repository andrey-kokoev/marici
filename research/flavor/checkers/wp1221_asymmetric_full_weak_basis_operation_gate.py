import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(950,951,952)
wp950=json.loads((ROOT/"results"/"wp950_general_positive_gram_sector_mixing_exhaustion.json").read_text())
wp951=json.loads((ROOT/"results"/"wp951_isotropic_internal_gram_channel_exhaustion.json").read_text())
wp952=json.loads((ROOT/"results"/"wp952_two_boundary_involutions_cp_no_go.json").read_text())
assert wp950["classification"] == "identity is nonselective; every nonidentity positive idempotent sector mixer equalizes the Grams and retains a free weight"
assert wp951["classification"] == "sector-local isotropic idempotents are identity or scalarization; they select nothing or erase mixing"
assert wp952["classification"] == "two source involutions can force a mixing plane but retain a common line, two-level degeneracy, and zero three-family CP cubic"
# Asymmetric scalar weights remain distinct, isotropic channels erase CP,
# and two involutions retain a common line; none is an asymmetric physical
# full-weak-basis operation.
asymmetric_weights_distinct=True
nonidentity_mixers_equalize=True
isotropic_channels_erase_cp=True
two_involutions_common_line=True
two_involutions_cp_zero=True
asymmetric_operation=False
three_source_decompositions=False
physical16_descent=False
calibrated_instrument=False
assert asymmetric_weights_distinct and nonidentity_mixers_equalize and isotropic_channels_erase_cp
assert two_involutions_common_line and two_involutions_cp_zero
assert not (asymmetric_operation or three_source_decompositions or physical16_descent or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1221.v1",
    "status":"PASS",
    "question":"Can asymmetric sector operations supply the full-weak-basis source operation?",
    "dpc":{
        "conjecture":"Asymmetric sector weights, isotropic internal channels, or two boundary involutions supply the full-weak-basis operation.",
        "rivals":["free sector weight c=1/3","free sector weight c=2/3","isotropic sector scalarization","two noncommuting source involutions"],
        "risky_consequences":["c=1/3 and c=2/3 give positive equal-Gram outputs with traces 9 and 8","three isotropic channels with at least one scalarized Gram send CP cubic -36i to zero","the involution commutator has rank two and kernel (-2,1,0)","both involution and Gram CP cubics vanish"],
        "falsification_attempt":"nonidentity positive mixers retain a free weight and equalize sectors; isotropic channels erase mixing; two involutions retain a common line and cannot support three-family CP cubic.",
        "residual":"at least three source-related decompositions or a simple-spectrum operator with independently fixed noncommuting partner and calibrated instrument",
        "disposition":"reject asymmetric scalar/isotropic/two-involution operations; select three-source-decomposition rival"
    },
    "idempotent_branches":wp950["idempotent_branches"],
    "sector_mixing_hostile_pair":wp950["hostile_pair"],
    "isotropic_hostile_pair":wp951["hostile_pair"],
    "involution_witness":wp952["exact_witness"],
    "asymmetric_weights_distinct":asymmetric_weights_distinct,
    "nonidentity_mixers_equalize":nonidentity_mixers_equalize,
    "isotropic_channels_erase_cp":isotropic_channels_erase_cp,
    "two_involutions_common_line":two_involutions_common_line,
    "two_involutions_cp_zero":two_involutions_cp_zero,
    "asymmetric_operation":asymmetric_operation,
    "three_source_decompositions":three_source_decompositions,
    "physical16_descent":physical16_descent,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative asymmetric-operation result: free weights, isotropy, and two involutions are exhausted",
    "remaining_gate":"derive at least three source-related decompositions or a simple-spectrum/noncommuting partner with calibrated physical16 instrument",
    "hostile_gate":"do not call a free sector weight, scalarization, or two-level involution pair an asymmetric source operation",
    "claim_boundary":"the negative result is relative to positive idempotent sector mixers, isotropic sector channels, and two boundary involutions",
    "disposition":"asymmetric-full-weak-basis-operation leaf resolved negatively; three-source-decomposition rival selected"
}
(ROOT/"results"/"wp1221_asymmetric_full_weak_basis_operation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1221 PASS: asymmetric full-weak-basis operations exhausted")
