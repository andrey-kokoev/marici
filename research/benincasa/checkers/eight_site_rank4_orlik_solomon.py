"""Degreewise Orlik--Solomon audit for the C8 rank-four wall matroids."""

import collections
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
ATTACHMENTS = ROOT / "results" / "eight-site-rank4-circuit-attachment-graph.json"
TARGET = ROOT / "results" / "eight-site-rank4-orlik-solomon.json"
GROUND_SIZE = 7


def wedge(left: tuple[int, ...], right: tuple[int, ...]):
    if set(left) & set(right):
        return None
    inversions = sum(1 for a in left for b in right if a > b)
    return tuple(sorted(left + right)), -1 if inversions % 2 else 1


def circuit_boundary(circuit: tuple[int, ...]):
    return [
        (circuit[:index] + circuit[index + 1 :], -1 if index % 2 else 1)
        for index in range(len(circuit))
    ]


def ideal_generators(circuits: list[tuple[int, ...]], degree: int):
    basis = list(itertools.combinations(range(GROUND_SIZE), degree))
    row = {monomial: index for index, monomial in enumerate(basis)}
    columns = []
    descriptors = []
    for circuit_index, circuit in enumerate(circuits):
        boundary_degree = len(circuit) - 1
        extra_degree = degree - boundary_degree
        if extra_degree < 0:
            continue
        for multiplier in itertools.combinations(range(GROUND_SIZE), extra_degree):
            column = [0] * len(basis)
            for monomial, boundary_sign in circuit_boundary(circuit):
                product = wedge(multiplier, monomial)
                if product is None:
                    continue
                output, wedge_sign = product
                column[row[output]] += boundary_sign * wedge_sign
            columns.append(column)
            descriptors.append({
                "circuit_index": circuit_index,
                "circuit_support": list(circuit),
                "exterior_multiplier": list(multiplier),
            })
    if not columns:
        return sp.zeros(len(basis), 0), descriptors
    return sp.Matrix(len(basis), len(columns), lambda i, j: columns[j][i]), descriptors


def ideal_matrix(circuits: list[tuple[int, ...]], degree: int) -> sp.Matrix:
    return ideal_generators(circuits, degree)[0]


def normalized_key(occurrence: dict, circuit: dict) -> str:
    pairs = sorted(
        (label, int(coefficient))
        for label, coefficient in zip(occurrence["labels"], circuit["coefficients"])
        if coefficient
    )
    if pairs[0][1] < 0:
        pairs = [(label, -coefficient) for label, coefficient in pairs]
    return "|".join(f"{coefficient:+d}*{label}" for label, coefficient in pairs)


def audit_occurrence(occurrence: dict, private_keys: set[str]) -> dict:
    all_circuits = []
    shared_circuits = []
    private_circuits = []
    private_keys_local = []
    for circuit in occurrence["labelled_circuits"]:
        support = tuple(index for index, value in enumerate(circuit["coefficients"]) if value)
        all_circuits.append(support)
        if normalized_key(occurrence, circuit) in private_keys:
            private_circuits.append(support)
            private_keys_local.append(normalized_key(occurrence, circuit))
        else:
            shared_circuits.append(support)

    degrees = []
    for degree in range(GROUND_SIZE + 1):
        ambient_dimension = sp.binomial(GROUND_SIZE, degree)
        full = ideal_matrix(all_circuits, degree)
        shared = ideal_matrix(shared_circuits, degree)
        full_rank = full.rank()
        shared_rank = shared.rank()
        degrees.append({
            "degree": degree,
            "exterior_dimension": int(ambient_dimension),
            "full_ideal_rank": full_rank,
            "shared_only_ideal_rank": shared_rank,
            "private_rank_increment": full_rank - shared_rank,
            "orlik_solomon_dimension": int(ambient_dimension) - full_rank,
        })
    private_syzygies = []
    shared_degree_four, shared_descriptors = ideal_generators(shared_circuits, 4)
    for private_key, private_circuit in zip(private_keys_local, private_circuits):
        private_column = ideal_matrix([private_circuit], 4)[:, 0]
        solution, parameters = shared_degree_four.gauss_jordan_solve(private_column)
        substitutions = {symbol: 0 for symbol in parameters}
        particular = solution.subs(substitutions)
        terms = []
        for coefficient, descriptor in zip(particular, shared_descriptors):
            if coefficient:
                terms.append({
                    **descriptor,
                    "coefficient": str(coefficient),
                    "circuit_labels": [occurrence["labels"][index] for index in descriptor["circuit_support"]],
                    "multiplier_labels": [occurrence["labels"][index] for index in descriptor["exterior_multiplier"]],
                })
        assert shared_degree_four * particular == private_column
        private_syzygies.append({
            "private_circuit_key": private_key,
            "private_circuit_labels": [occurrence["labels"][index] for index in private_circuit],
            "shared_ideal_terms": terms,
            "verified": True,
        })

    return {
        "occurrence_id": occurrence["occurrence_id"],
        "source_orbit_key": occurrence["source_orbit_key"],
        "circuit_count": len(all_circuits),
        "private_circuit_count": len(private_circuits),
        "private_circuit_supports": [list(circuit) for circuit in private_circuits],
        "private_degree_four_syzygies": private_syzygies,
        "degrees": degrees,
        "orlik_solomon_betti_vector": [item["orlik_solomon_dimension"] for item in degrees],
        "private_rank_increment_vector": [item["private_rank_increment"] for item in degrees],
    }


def main() -> None:
    source = json.loads(SOURCE.read_text())
    attachment = json.loads(ATTACHMENTS.read_text())
    private_keys = set(attachment["private_circuit_keys"])
    representatives = [item for item in source["occurrences"] if item["cyclic_shift"] == 0]
    audits = [audit_occurrence(item, private_keys) for item in representatives]

    betti_distribution = collections.Counter(tuple(item["orlik_solomon_betti_vector"]) for item in audits)
    increment_distribution = collections.Counter(tuple(item["private_rank_increment_vector"]) for item in audits)
    private_audits = [item for item in audits if item["private_circuit_count"]]
    checks = {
        "orbit_representative_count": len(audits),
        "orlik_solomon_betti_distribution": {
            ",".join(map(str, key)): value for key, value in sorted(betti_distribution.items())
        },
        "private_orbit_count": len(private_audits),
        "private_rank_increment_distribution": {
            ",".join(map(str, key)): value for key, value in sorted(increment_distribution.items())
        },
        "every_private_boundary_generated_by_shared_ideal": all(
            all(value == 0 for value in item["private_rank_increment_vector"])
            for item in private_audits
        ),
        "private_syzygy_witness_count_on_orbit_representatives": sum(
            len(item["private_degree_four_syzygies"]) for item in private_audits
        ),
    }
    assert checks["orbit_representative_count"] == 36
    assert checks["private_orbit_count"] == 4
    assert checks["every_private_boundary_generated_by_shared_ideal"]
    assert checks["private_syzygy_witness_count_on_orbit_representatives"] == 4

    output = {
        "schema": "marici.eight_site_rank4_orlik_solomon.v1",
        "scope": {
            "included": "degreewise OS ideal generated by source-labelled minimal circuits",
            "excluded": "Betti realization, physical current, and regulator-to-Salvetti comparison",
        },
        "checks": checks,
        "orbit_representatives": audits,
    }
    TARGET.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
