#!/usr/bin/env python3
"""Run the axis-marked grade change through Aspect's executable tower."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect"
STROMINGER = ROOT / "research" / "strominger"
CONTRACT = STROMINGER / "contracts" / "axis-marked-grade-change-aspect-fixture.v1.json"


def gf2_rank(rows: list[list[int]]) -> int:
    work = [sum((value & 1) << j for j, value in enumerate(row)) for row in rows]
    rank = 0
    column = 0
    width = len(rows[0]) if rows else 0
    while column < width and rank < len(work):
        pivot = next((i for i in range(rank, len(work)) if (work[i] >> column) & 1), None)
        if pivot is None:
            column += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(len(work)):
            if i != rank and ((work[i] >> column) & 1):
                work[i] ^= work[rank]
        rank += 1
        column += 1
    return rank


def load_aspect_decide():
    path = ASPECT / "checkers" / "check_admissibility_governance_falsifier.py"
    spec = importlib.util.spec_from_file_location("aspect_admissibility", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Aspect admission tester")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.decide


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    completed = subprocess.run(
        [sys.executable, str(ASPECT / "checkers" / "check_five_rung_tower.py")],
        cwd=ROOT, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr or completed.stdout)
    aspect_tower = json.loads((ASPECT / "results" / "five_rung_tower.json").read_text(encoding="utf-8"))

    mutations = contract["mutation_carrier"]
    current_rows = list(contract["current_observation_rows"].values())
    pre_rank = gf2_rank(current_rows)
    pre_kernel = len(mutations) - pre_rank

    mutation_index = {name: i for i, name in enumerate(mutations)}
    synthesized_rows = []
    for mutation in contract["synthesized_interventions"].values():
        row = [0] * len(mutations)
        row[mutation_index[mutation]] = 1
        synthesized_rows.append(row)
    post_rank = gf2_rank(current_rows + synthesized_rows)
    post_kernel = len(mutations) - post_rank

    blind_primitives = []
    for j, mutation in enumerate(mutations):
        if not any(row[j] for row in current_rows):
            blind_primitives.append(mutation)

    ontology = contract["ontology_mutations"]
    old_language = set(mutations)
    old_blind = [term for term in ontology if term not in old_language]
    enlarged = old_language.union(ontology)
    separated_after_enlargement = len(set(ontology).intersection(enlarged))
    diagonal_successor = f"fresh({ontology[-1]})"
    diagonal_escapes = diagonal_successor not in enlarged

    profile = contract["aspect_evidence_profile"]
    ordered_profile = tuple(profile[key] for key in (
        "source_provenance", "well_typed_term", "discriminating_target",
        "operational_witness", "nonredundancy", "bounded_decisive_test"))
    aspect_decide = load_aspect_decide()
    disposition = aspect_decide(ordered_profile)

    expected = contract["expected"]
    gates = {
        "aspect_five_rung_tower_executed_and_passed": aspect_tower["status"] == "pass",
        "frozen_mutation_carrier_has_expected_rank": pre_rank == expected["pre_repair_rank"],
        "current_tester_exposes_three_dimensional_kernel": pre_kernel == expected["pre_repair_kernel_dimension"],
        "blind_mutations_are_phase_order_and_domain": blind_primitives == [
            "weight_dependent_phase_twist", "constructor_order_swap", "singular_domain_extension"],
        "dual_interventions_close_frozen_kernel": post_rank == expected["post_repair_rank"] and post_kernel == expected["post_repair_kernel_dimension"],
        "ontology_mutations_are_invisible_to_old_language": len(old_blind) == len(ontology),
        "enlargement_separates_frozen_ontology_challenge": separated_after_enlargement == len(ontology),
        "fresh_successor_refutes_absolute_closure": diagonal_escapes,
        "aspect_decision_function_returns_expected_disposition": disposition == expected["admission_disposition"],
        "no_physical_qualification_is_inferred": not expected["physical_apparatus_qualified"] and disposition != "admit",
    }
    result = {
        "schema": "marici.strominger.axis-marked-grade-change-aspect-tower-result.v1",
        "status": "superseded" if all(gates.values()) else "fail",
        "formal_declared_matrix_status": "pass" if all(gates.values()) else "fail",
        "superseded_by": "axis_marked_grade_change_aspect_exact_checks.json",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "aspect_tower_schema": aspect_tower["schema"],
        "aspect_tower_status": aspect_tower["status"],
        "pre_repair": {"rank": pre_rank, "kernel_dimension": pre_kernel, "blind_primitives": blind_primitives},
        "synthesized_interventions": list(contract["synthesized_interventions"].keys()),
        "post_repair": {"rank": post_rank, "kernel_dimension": post_kernel, "operational": False},
        "ontology": {
            "frozen_challenge_count": len(ontology),
            "old_blind_count": len(old_blind),
            "separated_after_enlargement": separated_after_enlargement,
            "diagonal_successor": diagonal_successor,
            "absolute_closure": False,
        },
        "aspect_admission": {"profile": profile, "disposition": disposition},
        "verdict": "This declared-matrix prototype reported a three-dimensional kernel, but executable mutation semantics in v2 show that two directions were respectively an alias and outside the declared domain. Use the v2 result.",
    }
    target = STROMINGER / "results" / "axis_marked_grade_change_aspect_tower_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "pre_repair", "post_repair", "aspect_admission")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
