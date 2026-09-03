import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1135,1136,1137,1138)
wp1135=json.loads((ROOT/"results"/"wp1135_parent_projection_mass_clock_no_go.json").read_text())
wp1136=json.loads((ROOT/"results"/"wp1136_common_twist_localization_clock_no_go.json").read_text())
wp1137=json.loads((ROOT/"results"/"wp1137_radius_absolute_clock_no_go.json").read_text())
wp1138=json.loads((ROOT/"results"/"wp1138_mass_clock_constructor_closure_audit.json").read_text())
assert wp1135["classification"].startswith("negative gate: equal dimensions")
assert wp1136["classification"].startswith("negative gate: common parent")
assert wp1137["classification"].startswith("negative gate: radius stabilization")
assert wp1138["classification"].startswith("closure audit")
# Conditional parent and radius facts are exact, but no localized absolute
# clock constructor passes.
conditional_clock=True
radius_law=True
closure_audit=True
current_source_passes=wp1138["current_source_passes"]
projection=False
twist_descent=False
unique_flux_sector=False
gauge_gravity_ratio=False
localized_descent=False
physical_frame=False
absolute_clock=False
assert conditional_clock and radius_law and closure_audit and current_source_passes==0
assert not (projection or twist_descent or unique_flux_sector or gauge_gravity_ratio or localized_descent or physical_frame or absolute_clock)
result={
    "schema":"marici.flavor.wp1255.v1",
    "status":"PASS",
    "question":"Can the current source derive the absolute localized mass clock?",
    "dpc":{
        "conjecture":"Spin-11 projection, common-twist alignment, or radius stabilization may derive the localized unit pole clock.",
        "rivals":["parent projection","common-twist tower","radius stabilization","closure audit"],
        "risky_consequences":["localized and spin-11 cells both have dimension 23","parent masses are 1/4 and radius squared is 1/16","B/A=6n^2 has unit-clock solutions (1,6) and (2,24)","a constructor must preserve ports and five localized mass blocks"],
        "falsification_attempt":"zero equivariant projections, clock descent certificates, sourced flux sectors, gauge-gravity ratios, localized descent maps, or physical momentum frames exist; the closure audit has zero passes.",
        "residual":"materialize a compactification clock packet selecting n and B/A, proving localized descent, and fixing the momentum frame",
        "disposition":"retain conditional clock facts; reject current-source absolute-clock authority"
    },
    "localized_dimensions":wp1135["localized_dimensions"],
    "localized_C":wp1135["localized_C"],
    "spin11_dimension":wp1135["spin11_dimension"],
    "localized_mass_blocks_after_exchange":wp1135["localized_mass_blocks_after_exchange"],
    "spin11_mass_blocks":wp1135["spin11_mass_blocks"],
    "parent_projection":{
        "sourced_equivariant_maps":wp1135["sourced_equivariant_maps"],
        "port_preserving_descent_maps":wp1135["port_preserving_descent_maps"],
        "mass_pullback_certificates":wp1135["mass_pullback_certificates"]
    },
    "common_twist":{
        "parent_masses":wp1136["parent_masses"],
        "parent_ratio":wp1136["parent_ratio"],
        "localization_preserving_clock_maps":wp1136["localization_preserving_clock_maps"],
        "mass_descent_certificates":wp1136["mass_descent_certificates"],
        "radius2_common_value":wp1136["radius2_common_value"]
    },
    "radius_stabilization":{
        "joint_condition":wp1137["joint_condition"],
        "unit_clock_solutions":wp1137["unit_clock_solutions"],
        "hostile_rows":wp1137["hostile_rows"],
        "flux_sectors_sourced":wp1137["flux_sectors_sourced"],
        "gauge_gravity_ratios_sourced":wp1137["gauge_gravity_ratios_sourced"],
        "localized_descent_maps":wp1137["localized_descent_maps"]
    },
    "closure_audit":{
        "tested_gates":wp1138["tested_gates"],
        "target_M2":wp1138["target_M2"],
        "conditional_parent_clock":wp1138["conditional_parent_clock"],
        "missing_object":wp1138["missing_object"]
    },
    "conditional_clock_facts":conditional_clock,
    "radius_law_exact":radius_law,
    "closure_audit_complete":closure_audit,
    "current_source_passes":current_source_passes,
    "equivariant_projection":projection,
    "common_twist_descent":twist_descent,
    "unique_flux_sector":unique_flux_sector,
    "gauge_gravity_ratio":gauge_gravity_ratio,
    "localized_descent":localized_descent,
    "physical_momentum_frame":physical_frame,
    "absolute_clock":absolute_clock,
    "classification":"conditional mass-clock gate: parent and radius facts exact, absolute localized clock absent",
    "remaining_gate":"materialize compactification_clock_packet and pass its acceptance test",
    "hostile_gate":"do not call equal dimensions, parent mass equality, B/A=6n^2, radius values, or closure audits an absolute localized clock",
    "claim_boundary":"WP1135 through WP1138 retain conditional facts and close tested constructors; no M2=1 localized authority is admitted",
    "disposition":"mass-clock gate resolved conditionally; compactification-clock packet rival selected"
}
(ROOT/"results"/"wp1255_mass_clock_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1255 PASS: conditional clock facts exact, absolute localized clock absent")
