from __future__ import annotations

import argparse
import json
from collections import deque
from fractions import Fraction
from pathlib import Path


def fraction(value):
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def vector(values):
    return tuple(fraction(value) for value in values)


def matrix(rows):
    return tuple(vector(row) for row in rows)


def validate_contract(config):
    if not isinstance(config.get("state_basis"), list) or not config["state_basis"]:
        raise ValueError("state_basis must be a nonempty list")
    width = len(config["state_basis"])

    def require_vector(values, locus):
        if not isinstance(values, list) or len(values) != width:
            raise ValueError(f"{locus} must have exactly {width} coordinates")
        vector(values)

    def require_matrix(rows, locus):
        if not isinstance(rows, list) or len(rows) != width:
            raise ValueError(f"{locus} must have exactly {width} rows")
        for index, row in enumerate(rows):
            require_vector(row, f"{locus} row {index}")

    for index, item in enumerate(config.get("effects", [])):
        require_vector(item.get("vector"), f"effects[{index}].vector")
    for index, item in enumerate(config.get("constructors", [])):
        require_matrix(item.get("matrix"), f"constructors[{index}].matrix")
    for index, item in enumerate(config.get("rival_differences", [])):
        require_vector(item.get("vector"), f"rival_differences[{index}].vector")
    for index, item in enumerate(config.get("candidates", [])):
        kind = item.get("kind")
        if kind == "effect":
            require_vector(item.get("vector"), f"candidates[{index}].vector")
        elif kind == "constructor":
            require_matrix(item.get("matrix"), f"candidates[{index}].matrix")
        else:
            raise ValueError(f"candidates[{index}].kind must be effect or constructor")


def row_times_matrix(row, operator):
    return tuple(
        sum(row[index] * operator[index][column] for index in range(len(row)))
        for column in range(len(row))
    )


def pairing(effect, state_difference):
    return sum(left * right for left, right in zip(effect, state_difference))


def rref(rows, width):
    work = [list(row) for row in rows if any(row)]
    pivot_columns = []
    pivot_row = 0
    for column in range(width):
        found = next(
            (index for index in range(pivot_row, len(work)) if work[index][column] != 0),
            None,
        )
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for index in range(len(work)):
            if index == pivot_row:
                continue
            scale = work[index][column]
            if scale:
                work[index] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(work[index], work[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return tuple(tuple(row) for row in work), tuple(pivot_columns)


def rank(rows, width):
    return len(rref(rows, width)[1])


def nullspace(rows, width):
    reduced, pivots = rref(rows, width)
    free_columns = [column for column in range(width) if column not in pivots]
    basis = []
    for free in free_columns:
        item = [Fraction(0) for _ in range(width)]
        item[free] = Fraction(1)
        for row_index, pivot in enumerate(pivots):
            item[pivot] = -reduced[row_index][free]
        basis.append(tuple(item))
    return tuple(basis)


def serialize_fraction(value):
    return str(value)


def serialize_vector(values):
    return [serialize_fraction(value) for value in values]


def sign(value):
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def magnitude_class(value):
    absolute = abs(value)
    if absolute == 0:
        return "zero"
    if absolute < 1:
        return "subunit"
    if absolute == 1:
        return "unit"
    return "superunit"


def close_effect_module(config):
    width = len(config["state_basis"])
    admitted = [
        item
        for item in config.get("constructors", [])
        if item.get("source_authorized", True)
        and item.get("executable", True)
        and item.get("admitted", True)
    ]
    operators = [(item["name"], matrix(item["matrix"])) for item in admitted]
    basis = []
    provenance = []
    queue = deque()

    def add_if_independent(row, path):
        if not any(row):
            return False
        if rank(basis + [row], width) == rank(basis, width):
            return False
        basis.append(row)
        provenance.append(path)
        queue.append((row, path))
        return True

    for item in config.get("effects", []):
        if item.get("source_authorized", True) and item.get("admitted", True):
            add_if_independent(vector(item["vector"]), item["name"])

    while queue:
        row, path = queue.popleft()
        for name, operator in operators:
            add_if_independent(row_times_matrix(row, operator), f"{path} -> {name}")

    return tuple(basis), tuple(provenance)


def candidate_effects(candidate, current_basis):
    if candidate["kind"] == "effect":
        return ((vector(candidate["vector"]), candidate["name"]),)
    if candidate["kind"] == "constructor":
        operator = matrix(candidate["matrix"])
        return tuple(
            (row_times_matrix(effect, operator), f"{path} -> {candidate['name']}")
            for effect, path in current_basis
        )
    raise ValueError(f"unsupported candidate kind: {candidate['kind']}")


def compile_contract(config):
    validate_contract(config)
    width = len(config["state_basis"])
    effect_basis, provenance = close_effect_module(config)
    current_basis = tuple(zip(effect_basis, provenance))
    current_rank = rank(effect_basis, width)
    kernel = nullspace(effect_basis, width)
    rivals = [
        (item["name"], vector(item["vector"]))
        for item in config.get("rival_differences", [])
    ]
    requirements = config.get("candidate_requirements", {})
    required_locus = requirements.get("authority_locus")
    candidate_reports = []

    for candidate in config.get("candidates", []):
        generated = candidate_effects(candidate, current_basis)
        generated_reports = []
        transverse = False
        distinguishes_any = False
        for effect, path in generated:
            outside_span = rank(effect_basis + (effect,), width) > current_rank
            responses = []
            for rival_name, difference in rivals:
                value = pairing(effect, difference)
                responses.append(
                    {
                        "rival_difference": rival_name,
                        "pairing": serialize_fraction(value),
                        "sign": sign(value),
                        "magnitude_class": magnitude_class(value),
                    }
                )
                distinguishes_any = distinguishes_any or value != 0
            transverse = transverse or outside_span
            generated_reports.append(
                {
                    "path": path,
                    "effect": serialize_vector(effect),
                    "outside_existing_effect_span": outside_span,
                    "responses": responses,
                }
            )

        gates = {
            "source_authorized": bool(candidate.get("source_authorized", False)),
            "executable": bool(candidate.get("executable", False)),
            "perturbation": bool(candidate.get("perturbation", False)),
            "calibrated": bool(candidate.get("calibrated", False)),
            "completion_stable": bool(candidate.get("completion_stable", False)),
            "authority_locus_matches": required_locus is None
            or candidate.get("authority_locus") == required_locus,
        }
        required_gate_names = [
            name for name, required in requirements.items() if name != "authority_locus" and required
        ]
        gate_pass = all(gates.get(name, False) for name in required_gate_names)
        eligible = (
            gate_pass
            and gates["authority_locus_matches"]
            and transverse
            and distinguishes_any
        )
        failed_gates = [name for name in required_gate_names if not gates.get(name, False)]
        if not gates["authority_locus_matches"]:
            failed_gates.append("authority_locus_matches")
        candidate_reports.append(
            {
                "name": candidate["name"],
                "kind": candidate["kind"],
                "authority_locus": candidate.get("authority_locus"),
                "gates": gates,
                "failed_gates": failed_gates,
                "algebraically_transverse": transverse,
                "distinguishes_rival": distinguishes_any,
                "eligible_source_authorized_effect": eligible,
                "generated_effects": generated_reports,
                "claim_boundary": candidate.get("claim_boundary"),
            }
        )

    first_transverse = next(
        (item["name"] for item in candidate_reports if item["algebraically_transverse"]),
        None,
    )
    first_eligible = next(
        (item["name"] for item in candidate_reports if item["eligible_source_authorized_effect"]),
        None,
    )
    rival_kernel_membership = {
        name: all(pairing(effect, difference) == 0 for effect in effect_basis)
        for name, difference in rivals
    }
    return {
        "schema": "marici.aspect.clifford-constructor-compiler.v1",
        "status": "pass",
        "model": config["model"],
        "clifford_basis": config["state_basis"],
        "pairing": config.get("pairing", "coordinate scalar pairing"),
        "existing_effect_rank": current_rank,
        "state_dimension": width,
        "behavioral_kernel_dimension": len(kernel),
        "effect_basis": [
            {"effect": serialize_vector(effect), "provenance": path}
            for effect, path in current_basis
        ],
        "behavioral_kernel_basis": [serialize_vector(item) for item in kernel],
        "rival_differences_in_existing_kernel": rival_kernel_membership,
        "candidate_requirements": requirements,
        "candidates": candidate_reports,
        "first_algebraically_transverse_candidate": first_transverse,
        "first_eligible_source_authorized_effect": first_eligible,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    config = json.loads(arguments.contract.read_text(encoding="utf-8"))
    result = compile_contract(config)
    rendered = json.dumps(result, indent=2) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
