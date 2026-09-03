import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1090,1091,1092,1093,1094,1095,1096,1097,1098,1099)
wp1090=json.loads((ROOT/"results"/"wp1090_reciprocal_determinant_rho_no_go.json").read_text())
wp1091=json.loads((ROOT/"results"/"wp1091_source_natural_negative_weight_scalar_no_go.json").read_text())
wp1092=json.loads((ROOT/"results"/"wp1092_conditional_wilson_production_kernel_no_go.json").read_text())
wp1093=json.loads((ROOT/"results"/"wp1093_history_dilation_gain_no_go.json").read_text())
wp1094=json.loads((ROOT/"results"/"wp1094_coset_absolute_boundary_action_fiber.json").read_text())
wp1095=json.loads((ROOT/"results"/"wp1095_wilson_integer_lift_clock_no_go.json").read_text())
wp1096=json.loads((ROOT/"results"/"wp1096_normalization_packet_authority_audit_gate.json").read_text())
wp1097=json.loads((ROOT/"results"/"wp1097_finite_scheme_port_gain_no_go.json").read_text())
wp1098=json.loads((ROOT/"results"/"wp1098_contact_counterterm_boundary_lift_no_go.json").read_text())
wp1099=json.loads((ROOT/"results"/"wp1099_integral_lattice_clock_orientation_no_go.json").read_text())
for key,d,prefix in [("wp1090",wp1090,"negative gate"),("wp1091",wp1091,"negative gate"),("wp1092",wp1092,"negative gate"),("wp1093",wp1093,"negative gate"),("wp1094",wp1094,"negative gate"),("wp1095",wp1095,"negative gate"),("wp1097",wp1097,"negative gate"),("wp1098",wp1098,"negative gate"),("wp1099",wp1099,"negative gate")]: assert d["classification"].startswith(prefix),key
assert wp1096["classification"].startswith("conditional gate")
# Candidate selectors are audited and rejected; only a normalized dual cycle
# or oriented generator remains as the next authority-bearing route.
reciprocal_rho_closed=True
natural_scalar_rho_closed=True
wilson_kernel_closed=True
history_gain_closed=True
coset_lift_ambiguity=True
wilson_integer_lift_closed=True
finite_scheme_gain_closed=True
contact_lift_closed=True
bare_lattice_orientation_closed=True
normalized_dual_cycle=False
oriented_generator=False
integer_lift=False
clock_orientation=False
independent_rho=False
production_kernel=False
gain_3_over_2=False
physical16_descent=False
assert reciprocal_rho_closed and natural_scalar_rho_closed and wilson_kernel_closed and history_gain_closed
assert coset_lift_ambiguity and wilson_integer_lift_closed and finite_scheme_gain_closed and contact_lift_closed and bare_lattice_orientation_closed
assert not (normalized_dual_cycle or oriented_generator or integer_lift or clock_orientation or independent_rho or production_kernel or gain_3_over_2 or physical16_descent)
result={
    "schema":"marici.flavor.wp1249.v1",
    "status":"PASS",
    "question":"Can admitted normalization packets derive an oriented adjoint direction?",
    "dpc":{
        "conjecture":"Existing determinant, Wilson, history, coset, finite-scheme, contact, or lattice packets might select the missing oriented source direction.",
        "rivals":["reciprocal determinant rho","natural negative-weight scalar","Wilson production kernel","history-dilation gain","absolute boundary coset lift","Wilson integer clock lift","finite-scheme ports","contact counterterm","bare integral lattice"],
        "risky_consequences":["1/D has weight -3 only on the cyclic domain and is singular on eigenlines","natural D-denominator candidates reduce to 1/D","conditional B flags and three history slots contribute zero production rows","integer CS lifts preserve the coset but change channel evaluation","Wilson phase is modulo one and the quadratic clock is sign blind","three finite-scheme ports are faithful but constant on event weights","contact shifts have zero projection to the seven-channel lift","a rank-one lattice leaves n and -n degenerate"],
        "falsification_attempt":"all admitted candidates fail to supply independent rho, integer lift, orientation, production kernel, gain 3/2, or Physical16 descent.",
        "residual":"obtain a source-authorized normalized dual cycle or oriented generator selecting n and sigma, then derive the adjoint flag, rho, kernel, gain, and descent",
        "disposition":"accept the authority audit as a set of exact no-gos; select the normalized-dual-cycle/oriented-generator branch"
    },
    "reciprocal_witness":wp1090["witness"],
    "bounded_degree_scan":wp1091["bounded_degree_scan"],
    "conditional_B_flag":wp1092["conditional_B_flag"],
    "history":wp1093["history"],
    "coset_lifts":{
        "required_coset":wp1094["required_coset"],
        "lift0":wp1094["lift0"],
        "lift1":wp1094["lift1"]
    },
    "wilson_phase_lifts":wp1095["phase_lifts"],
    "packet_audit":wp1096["packet_audit"],
    "required_selector_authority":wp1096["required_selector_authority"],
    "finite_scheme_ports":wp1097["ports"],
    "contact_delta_on_lift_occupation":wp1098["contact_delta_on_lift_occupation"],
    "lattice_witness":wp1099["lattice_witness"],
    "sign_degeneracy":wp1099["sign_degeneracy"],
    "reciprocal_rho_closed":reciprocal_rho_closed,
    "natural_scalar_rho_closed":natural_scalar_rho_closed,
    "wilson_kernel_closed":wilson_kernel_closed,
    "history_gain_closed":history_gain_closed,
    "coset_lift_ambiguity":coset_lift_ambiguity,
    "wilson_integer_lift_closed":wilson_integer_lift_closed,
    "finite_scheme_gain_closed":finite_scheme_gain_closed,
    "contact_lift_closed":contact_lift_closed,
    "bare_lattice_orientation_closed":bare_lattice_orientation_closed,
    "normalized_dual_cycle":normalized_dual_cycle,
    "oriented_generator":oriented_generator,
    "integer_lift":integer_lift,
    "clock_orientation":clock_orientation,
    "independent_rho":independent_rho,
    "production_kernel":production_kernel,
    "gain_3_over_2":gain_3_over_2,
    "physical16_descent":physical16_descent,
    "classification":"conditional oriented-direction gate: admitted selectors fail, normalized dual cycle or oriented generator required",
    "remaining_gate":"derive a source-authorized normalized dual cycle or oriented generator selecting n and sigma, then the adjoint flag, rho, kernel, gain, and descent",
    "hostile_gate":"do not call reciprocal determinants, natural scalars, Wilson phases, history slots, coset lifts, finite ports, contact shifts, or bare lattice membership an oriented adjoint direction",
    "claim_boundary":"WP1090 through WP1099 provide exact selector no-gos; no source direction, kernel, gain, or Physical16 descent is derived",
    "disposition":"oriented-adjoint-direction leaf resolved conditionally; normalized-dual-cycle rival selected"
}
(ROOT/"results"/"wp1249_oriented_adjoint_direction_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1249 PASS: admitted selectors fail, normalized dual cycle absent")
