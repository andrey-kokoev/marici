"""Conditional common-law gates, not construction of a native particle law.

All controls use exact Q matrices. Linear-system consistency checks existence
only: a fitted solution is never returned as a source-derived primitive law.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "research/strominger/inputs/carrier-circuit-common-law-v1.json"
PACKET = ROOT / "research/strominger/carrier-circuit-common-law-conjecture.md"
MODEL = ROOT / "research/strominger/scc-models/carrier-circuit-common-law-v1.json"
BASE_PATH = ROOT / "research/strominger/checkers/check_carrier_particle_circuits.py"
COMPILER = ROOT / "research/aspect/scc/categorical_compiler.py"
OUT = ROOT / "research/strominger/results/carrier-circuit-common-law"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load("common_law_matrix_base", BASE_PATH)
compiler = load("common_law_scc", COMPILER)
mm, rank = base.mm, base.rank
I = [[Q(1), Q(0)], [Q(0), Q(1)]]
X = [[Q(0), Q(1)], [Q(1), Q(0)]]


def matrix(a):
    if len(a) != 2 or any(len(row) != 2 for row in a):
        raise ValueError("control stratum is 2x2")
    return [[Q(x) for x in row] for row in a]


def subtract(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def inverse(t):
    t = matrix(t)
    d = t[0][0] * t[1][1] - t[0][1] * t[1][0]
    if not d:
        raise ValueError("faithful source continuation missing; no pseudoinverse substitution")
    return [[t[1][1] / d, -t[0][1] / d], [-t[1][0] / d, t[0][0] / d]]


def flat(a):
    return [x for row in a for x in row]


def characteristic(a):
    return [Q(1), -a[0][0] - a[1][1], a[0][0] * a[1][1] - a[0][1] * a[1][0]]


def gates(p, n, e, t):
    b = mm(inverse(t), e)
    r = rank(b)
    image = rank([rb + rp for rb, rp in zip(b, p)]) - r
    kernel = rank(b + n) - r
    p_out = mm(mm(t, p), inverse(t))
    residual = subtract(mm(e, n), mm(p_out, e))
    return {"decoded_B": b, "rank_B": r, "image_obstruction": image,
            "kernel_obstruction": kernel, "intertwiner_residual": residual,
            "intertwiner_rank": rank(residual), "P_at_output": p_out,
            "compatible": image == kernel == rank(residual) == 0}


def linear_map(b):
    """Independent operator A -> (BA,AB), row-major coordinates."""
    columns = []
    for i, j in product(range(2), repeat=2):
        unit = [[Q(k == i and l == j) for l in range(2)] for k in range(2)]
        columns.append(flat(mm(b, unit)) + flat(mm(unit, b)))
    return base.transpose(columns)


def from_primitives(spec):
    a, b, t = [matrix(spec[k]) for k in ("A", "B", "T")]
    return a, b, t, mm(b, a), mm(a, b), mm(t, b)


def transport(p, n, e, t, c, m, out):
    return (mm(mm(c, p), inverse(c)), mm(mm(m, n), inverse(m)),
            mm(mm(out, e), inverse(m)), mm(mm(out, t), inverse(c)))


def digest(a):
    return sha256(json.dumps(a, sort_keys=True, default=str).encode()).hexdigest()


def run(report):
    checks = report["checks"]

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    f = json.loads(FIXTURE.read_text())
    old = json.loads(base.FIXTURE.read_text())
    check("windows_preserve_operator_corrected_source", f["source_windows"] == old["windows"])
    check("explicit_Q_two_role_control_stratum", f["field"] == "Q" and f["role_dimensions"] == {"C": 2, "M": 2, "C_out": 2})
    a, b, t, p, n, e = from_primitives(f["positive"])
    positive = gates(p, n, e, t)
    check("one_frozen_primitive_law_generates_all_three_windows", positive["compatible"] and positive["decoded_B"] == b)
    check("nonzero_spectra_match_as_conditional_consequence", characteristic(p) == characteristic(n))
    check("shared_B_intertwines_N_and_P", mm(b, n) == mm(p, b))
    check("shared_A_intertwines_P_and_N", mm(n, a) == mm(a, p))
    check("electron_intertwiner_requires_output_continuation_transport", mm(e, n) == mm(positive["P_at_output"], e) and positive["P_at_output"] != p)
    check("common_law_does_not_require_equal_electron_and_loop_ranks", rank(e) == 2 and rank(p) == rank(n) == 1)
    check("all_role_frames_transport_the_complete_gate", gates(*transport(p, n, e, t, X, X, I))["compatible"])

    cases = {}
    for name in ("spectral_spoof", "intertwiner_spoof"):
        spec = f[name]
        pp, nn, ee, tt = [matrix(spec[k]) for k in ("P", "N", "E", "T")]
        cases[name] = {"P": pp, "N": nn, "E": ee, "T": tt, **gates(pp, nn, ee, tt)}
        check(name + "_passes_spectrum_comparison", characteristic(pp) == characteristic(nn))
        check(name + "_fails_complete_common_law_gate", not cases[name]["compatible"])
    spoof = cases["spectral_spoof"]
    check("spectrum_spoof_has_exact_rank_two_intertwiner_obstruction", spoof["intertwiner_rank"] == 2 and spoof["intertwiner_residual"] == [[0, -1], [1, 0]])
    check("intertwiner_alone_misses_image_and_kernel_obstructions", cases["intertwiner_spoof"]["intertwiner_rank"] == 0 and cases["intertwiner_spoof"]["image_obstruction"] == cases["intertwiner_spoof"]["kernel_obstruction"] == 1)
    late_fit = gates(spoof["P"], spoof["N"], spoof["E"], X)
    check("posthoc_T_only_change_can_fake_a_pass", late_fit["compatible"])
    transported_spoof = gates(*transport(spoof["P"], spoof["N"], spoof["E"], spoof["T"], X, I, I))
    check("honest_complete_frame_transport_cannot_repair_the_spoof", not transported_spoof["compatible"] and transported_spoof["intertwiner_rank"] == 2)
    try:
        inverse([[1, 0], [0, 0]])
    except ValueError as error:
        check("singular_continuation_blocks_inverse_stratum", True)
        report["continuation_refusal"] = str(error)
    else:
        check("singular_continuation_blocks_inverse_stratum", False)

    aa, bb, tt, pp, nn, ee = from_primitives(f["singular_positive"])
    delta = matrix(f["singular_positive"]["invisible_A_change"])
    alternative_a = add(aa, delta)
    check("singular_B_still_admits_shared_law", gates(pp, nn, ee, tt)["compatible"])
    check("three_windows_do_not_uniquely_determine_primitive_A", alternative_a != aa and mm(bb, alternative_a) == pp and mm(alternative_a, bb) == nn)
    check("invisible_A_change_is_not_a_zero_operator", rank(delta) == 1 and base.mv(delta, [0, 1]) == [0, 1])
    check("ambiguity_dimension_matches_two_sided_linear_map", 4 - rank(linear_map(bb)) == (2 - rank(bb)) ** 2 == 1)

    binary = [matrix([list(v[:2]), list(v[2:])]) for v in product((0, 1), repeat=4)]
    count, accepted, strata = 0, 0, {}
    for b_case in binary:
        system = linear_map(b_case)
        system_rank = rank(system)
        rb = rank(b_case)
        check("A_ambiguity_dimension_rank_stratum_" + str(count // 256), 4 - system_rank == (2 - rb) ** 2)
        for p_case in binary:
            for n_case in binary:
                target = flat(p_case) + flat(n_case)
                solvable = rank([row + [value] for row, value in zip(system, target)]) == system_rank
                gate = gates(p_case, n_case, b_case, I)
                if gate["compatible"] != solvable:
                    report["census_counterexample"] = {"B": b_case, "P": p_case, "N": n_case, "gate": gate, "linear_system_solvable": solvable}
                    check("all_4096_gates_match_independent_linear_consistency", False)
                count += 1
                accepted += solvable
                strata[rb] = strata.get(rb, 0) + 1
    check("all_4096_gates_match_independent_linear_consistency", count == 4096)
    report["census"] = {"cases": count, "compatible": accepted, "incompatible": count - accepted,
                         "cases_by_rank_B": strata, "zero_gate_solver_disagreements": True,
                         "scope": "all 2x2 zero/one B,P,N; exact Q solution existence, not source construction"}
    lhs, rhs = mm(e, n), mm(positive["P_at_output"], e)
    arrows = [{"id": side, "source": "M", "target": "C_out", "map_token": digest(value),
               "evaluated_map": value, "factorization": words}
              for side, value, words in (("EN", lhs, ["N", "E"]), ("PoutE", rhs, ["E", "TPT_inverse"]))]
    diagram = {"id": "carrier-circuit-common-law-conditional", "objects": [{"id": "M"}, {"id": "C_out"}],
               "arrows": arrows, "cells": [{"id": "electron_intertwiner", "routes": [["EN"], ["PoutE"]]}],
               "obstructions": [], "claims": [{"id": "native_common_law", "requires": ["source_context_transports", "source_primitive_constructor", "held_out_occurrence_checks"]}],
               "available_witnesses": ["conditional_algebraic_gate", "finite_control_census"],
               "scope": "computed conditional control only; native claim remains missing source witnesses"}
    compiled = compiler.compile_diagram(diagram)
    check("conditional_SCC_intertwiner_cell_passes", compiled["passed"])
    check("passing_conditional_cell_does_not_promote_native_conjecture", compiled["inverse_design"]["native_common_law"]["status"] == "missing_witnesses")
    bad = deepcopy(diagram)
    for arrow, value in zip(bad["arrows"], (mm(spoof["E"], spoof["N"]), mm(spoof["P_at_output"], spoof["E"]))):
        arrow["evaluated_map"], arrow["map_token"] = value, digest(value)
    bad_compiled = compiler.compile_diagram(bad)
    check("SCC_spectral_spoof_cell_fails", not bad_compiled["passed"])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "conditional-diagram.json").write_text(json.dumps(diagram, indent=2, default=str) + "\n")
    (OUT / "spectral-spoof-diagram.json").write_text(json.dumps(bad, indent=2, default=str) + "\n")
    report["positive"] = {"A": a, "B": b, "T": t, "P": p, "N": n, "E": e, **positive}
    report["spoofs"] = cases
    report["forbidden_posthoc_T_repair"] = {"changed_T": X, "gate": late_fit, "honestly_transported_gate": transported_spoof}
    report["primitive_ambiguity"] = {"A": aa, "alternative_A": alternative_a, "B": bb, "P": pp, "N": nn, "E": ee, "T": tt, "nonzero_invisible_change": delta}
    report["conditional_compilation"] = compiled
    report["spoof_compilation"] = bad_compiled
    report["scientific_disposition"] = "Common-law conjecture OPEN: conditional criterion and falsifiers verified; no native primitive law or context transports supplied."


def main():
    paths = [FIXTURE, PACKET, MODEL, BASE_PATH, base.FIXTURE, COMPILER, Path(__file__).resolve()]
    report = {"schema": "marici.strominger.carrier-circuit-common-law.verification.v1", "recorded_at": datetime.now(timezone.utc).isoformat(), "checks": {},
              "source_sha256": {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report["status"] = "pass"
    except Exception as error:
        report["status"], report["error"] = "fail", repr(error)
        raise
    finally:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "verification.json").write_text(json.dumps(report, indent=2, default=str) + "\n")
        print(json.dumps({"status": report["status"], "check_groups": len(report["checks"]), "receipt": str((OUT / "verification.json").relative_to(ROOT)).replace("\\", "/")}))


if __name__ == "__main__":
    main()
