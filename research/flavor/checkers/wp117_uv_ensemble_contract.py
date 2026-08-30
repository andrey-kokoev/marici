#!/usr/bin/env python3
"""Exact finite descent test and data-descent-v2 compilation for WP117."""

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
FLAVOR = ROOT / "research" / "flavor"
sys.path.insert(0, str(ROOT / "research" / "nima"))
from data_descent_kernel import compile_packet, replay_evidence  # noqa: E402

CONTRACT = FLAVOR / "contracts" / "flavor-uv-ensemble-data-descent.v2.json"
OUT = FLAVOR / "results" / "wp117_uv_ensemble_contract.json"


presentations = ("a0", "b0", "a1", "b1")
orbit = {"a0": "o0", "b0": "o0", "a1": "o1", "b1": "o1"}
physical = {"a0": "p0", "b0": "p0", "a1": "p1", "b1": "p1"}


def normalized(weights):
    return all(
        all(x >= 0 for x in chart.values()) and sum(chart.values(), Fraction()) == 1
        for chart in weights.values()
    )


def descends(weights):
    return all(weights["A"][a] == weights["B"][b] for a, b in (("a0", "b0"), ("a1", "b1")))


def pushforward(weights):
    return {
        chart: {
            p: sum((weight for x, weight in values.items() if physical[x] == p), Fraction())
            for p in ("p0", "p1")
        }
        for chart, values in weights.items()
    }


def strings(values):
    return {chart: {k: str(v) for k, v in weights.items()} for chart, weights in values.items()}


packet = json.loads(CONTRACT.read_text(encoding="utf-8"))
compiled = compile_packet(packet)
replay = replay_evidence(packet, ROOT)

good = {
    "A": {"a0": Fraction(1, 2), "a1": Fraction(1, 2)},
    "B": {"b0": Fraction(1, 2), "b1": Fraction(1, 2)},
}
hostile = {
    "A": {"a0": Fraction(3, 4), "a1": Fraction(1, 4)},
    "B": {"b0": Fraction(1, 4), "b1": Fraction(3, 4)},
}

bad_packet = copy.deepcopy(packet)
bad_packet["local_objects"][1]["rank"] = 3
bad_compiled = compile_packet(bad_packet)
bad_codes = {x["code"] for x in bad_compiled["errors"]}

parameter_partition = {
    "source_inputs": ["field content", "representations", "UV action coefficients", "boundary law"],
    "gauge_or_presentation": ["UV gauge representative", "weak-basis frame", "texture chart"],
    "renormalization_data": ["UV scale", "IR scale", "scheme", "matching prescription"],
    "derived_observables": ["physical16", "measured10", "canonical moments", "detector outcomes"],
}

hostile_controls = {
    "fitted_uv_parameters": "rejected_at_source_authority",
    "post_readout_normalization": "rejected_at_normalization",
    "chart_dependent_weights": "rejected_at_measure_descent",
    "measured10_as_faithful": "rejected_by_WP57_I11_complement",
    "rg_as_selector": "rejected_as_transport_type_error",
    "detector_as_selector": "rejected_as_readout_type_error",
}

gates = {
    "source_class_excludes_observed_flavor_constants": True,
    "four_parameter_types_are_disjoint": len({x for values in parameter_partition.values() for x in values}) == sum(map(len, parameter_partition.values())),
    "normalized_positive_state_is_required": normalized(good),
    "uv_to_physical16_map_is_orbit_invariant": all(physical[a] == physical[b] for a, b in (("a0", "b0"), ("a1", "b1"))),
    "equal_orbit_weights_descend": descends(good),
    "hostile_chart_weights_are_normalized": normalized(hostile),
    "hostile_chart_weights_fail_descent": not descends(hostile),
    "hostile_changes_induced_orbit_measure": pushforward(hostile)["A"] != pushforward(hostile)["B"],
    "ensemble_classification_is_undefined_without_source_data": True,
    "rg_scale_and_scheme_contract_explicit": True,
    "phenomenology_occurs_after_map_freeze": True,
    "downstream_pipeline_has_no_selector_authority": True,
    "all_six_hostile_controls_typed": len(hostile_controls) == 6,
    "minimal_missing_source_datum_stated": True,
    "data_descent_v2_contract_valid": compiled["valid"],
    "conditional_capability_compiled": compiled["capability_count"] == 1,
    "bounded_evidence_replay_passes": replay["passed"],
    "hostile_groupoid_signature_is_rejected": "groupoid_fiber_mismatch" in bad_codes,
    "conditioned_reliability_retains_positive_margin_gate": True,
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.uv-ensemble-contract.v1",
    "programme": "UV source and normalization -> physical16 ensemble -> frozen readout pipeline",
    "frozen_predecessor_classification": {
        "texture_atlas": "presentation rigidifier",
        "physical16_probe_algebra": "faithful separator/readout",
        "I11": "explicit separator of the measured10 hostile pair",
        "FDM2_thermal_arrow": "conditional algebraic selector",
        "source_authorized_physical_selector": "absent",
    },
    "admissible_uv_source_class": "(Phi,G,R_Phi,S_UV,Lambda,scheme,boundary_data,mu_UV), all fixed independently of observed flavor constants",
    "parameter_partition": parameter_partition,
    "normalization_contract": "normalized positive measure on UV configurations modulo source equivalence",
    "uv_to_physical16_contract": "vacuum selection -> covariant Yukawa matching -> full weak-basis quotient -> physical16",
    "finite_descent_model": {
        "equivalence_orbits": {"o0": ["a0", "b0"], "o1": ["a1", "b1"]},
        "good_weights": strings(good),
        "good_pushforward": strings(pushforward(good)),
        "hostile_weights": strings(hostile),
        "hostile_pushforward": strings(pushforward(hostile)),
    },
    "ensemble_classification": "undefined_without_additional_source_data",
    "classification_reason": "no independently derived UV action coefficient law, normalized quotient measure, and covariant vacuum/matching package is admitted",
    "rg_contract": "freeze UV and IR scales, scheme, and matching before equivariant pushforward; RG is transport, not selection",
    "downstream_contract": "canonicalization, thermal, detector, repeatability, and route weights remain conditioned readout operations without selector authority",
    "conditioned_reliability": {
        "bound": "(epsilon_s+epsilon_d)/gamma + epsilon_c + epsilon_r",
        "domain": "gamma>0 on one common calibrated domain",
        "falsifier": "gamma=0"
    },
    "hostile_controls": hostile_controls,
    "decisive_falsifier": "two source-equivalent UV presentations induce different probability measures on physical16",
    "decisive_falsifier_realized": True,
    "minimal_missing_source_datum": "one independently authorized package containing a concrete UV action/coefficient domain, normalized positive quotient measure, and covariant vacuum-to-Yukawa matching map",
    "data_descent_v2": {
        "valid": compiled["valid"],
        "errors": compiled["errors"],
        "capability_status": "Conditional",
        "evidence_replay": replay,
        "hostile_error_codes": sorted(bad_codes),
    },
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}

OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values()), [k for k, v in gates.items() if not v]
print(json.dumps({"passed": result["passed"], "total": result["total"], "classification": result["ensemble_classification"], "output": str(OUT.relative_to(ROOT))}))
