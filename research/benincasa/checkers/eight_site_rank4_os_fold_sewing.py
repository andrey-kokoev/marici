"""Sew the C8 excess Leray current to the local fold coefficient through OS.

The rank-three excess basis contracts the labelled seven-torus to degree four.
This checker reduces that exact four-form modulo the occurrence's complete
Orlik--Solomon ideal and combines the result with the independently computed
odd source-face coefficient.  It keeps all 288 labels and the two attachment
components separate.
"""

import collections
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
LERAY = ROOT / "results" / "eight-site-rank4-excess-leray-complex.json"
ATTACHMENT = ROOT / "results" / "eight-site-rank4-circuit-attachment-graph.json"
PAIRING = ROOT / "results" / "eight-site-rank4-face-fold-pairing.json"
TARGET = ROOT / "results" / "eight-site-rank4-os-fold-sewing.json"
GROUND_SIZE = 7


def wedge(left: tuple[int, ...], right: tuple[int, ...]):
    if set(left) & set(right):
        return None
    inversions = sum(1 for a in left for b in right if a > b)
    return tuple(sorted(left + right)), -1 if inversions % 2 else 1


def circuit_boundary(circuit: tuple[int, ...]):
    return [(circuit[:i] + circuit[i + 1 :], -1 if i % 2 else 1) for i in range(len(circuit))]


def ideal_matrix(circuits: list[tuple[int, ...]], degree: int) -> sp.Matrix:
    basis = list(itertools.combinations(range(GROUND_SIZE), degree))
    row = {monomial: index for index, monomial in enumerate(basis)}
    columns = []
    for circuit in circuits:
        extra_degree = degree - (len(circuit) - 1)
        if extra_degree < 0:
            continue
        for multiplier in itertools.combinations(range(GROUND_SIZE), extra_degree):
            column = [0] * len(basis)
            for monomial, boundary_sign in circuit_boundary(circuit):
                product = wedge(multiplier, monomial)
                if product is not None:
                    output, wedge_sign = product
                    column[row[output]] += boundary_sign * wedge_sign
            columns.append(column)
    return sp.Matrix(len(basis), len(columns), lambda i, j: columns[j][i]) if columns else sp.zeros(len(basis), 0)


def contracted_top_form(excess_basis: sp.Matrix) -> sp.Matrix:
    """Compute i_k3 i_k2 i_k1(e0 wedge ... wedge e6)."""
    degree_four_basis = list(itertools.combinations(range(GROUND_SIZE), 4))
    coefficients = []
    for complement in degree_four_basis:
        removed = tuple(index for index in range(GROUND_SIZE) if index not in complement)
        permutation = removed + complement
        inversions = sum(1 for i in range(7) for j in range(i + 1, 7) if permutation[i] > permutation[j])
        coefficients.append((-1 if inversions % 2 else 1) * excess_basis[:, removed].det())
    return sp.Matrix(coefficients)


def main() -> None:
    source = json.loads(SOURCE.read_text())
    leray = json.loads(LERAY.read_text())
    attachment = json.loads(ATTACHMENT.read_text())
    pairing = json.loads(PAIRING.read_text())
    leray_by_occurrence = {item["occurrence_id"]: item for item in leray["occurrences"]}
    local_by_key = {item["source_orbit_key"]: item for item in pairing["families"]}
    component_by_occurrence = {
        occurrence_id: component
        for component, packet in enumerate(attachment["components"])
        for occurrence_id in packet["occurrence_ids"]
    }

    audits = []
    status_counts = collections.Counter()
    component_counts = collections.Counter()
    orientation_counts = collections.Counter()
    reference_contracteds = {}
    cyclic_projective_transport = collections.Counter()
    for occurrence in source["occurrences"]:
        excess_basis = sp.Matrix(leray_by_occurrence[occurrence["occurrence_id"]]["labelled_circuit_basis"])
        contracted = contracted_top_form(excess_basis)
        circuits = [
            tuple(index for index, coefficient in enumerate(circuit["coefficients"]) if coefficient)
            for circuit in occurrence["labelled_circuits"]
        ]
        ideal = ideal_matrix(circuits, 4)
        ideal_rank = ideal.rank()
        augmented_rank = ideal.row_join(contracted).rank()
        os_nonzero = augmented_rank == ideal_rank + 1
        reference = reference_contracteds.setdefault(occurrence["source_orbit_key"], contracted)
        transport_matrix = ideal.row_join(reference)
        projective_transport_typed = transport_matrix.row_join(contracted).rank() == transport_matrix.rank()
        assert projective_transport_typed
        transport_solution, transport_parameters = transport_matrix.gauss_jordan_solve(contracted)
        transport_solution = transport_solution.subs({parameter: 0 for parameter in transport_parameters})
        transport_scalar = sp.factor(transport_solution[-1])
        assert transport_scalar != 0
        cyclic_projective_transport[str(transport_scalar)] += 1
        local_nonzero = bool(local_by_key[occurrence["source_orbit_key"]]["local_pairing_nonzero"])
        sewn_nonzero = local_nonzero and os_nonzero
        status = "activated_in_os_degree_four" if sewn_nonzero else (
            "source_fold_coefficient_killed_by_os" if local_nonzero else "zero_source_fold_coefficient"
        )
        component = component_by_occurrence[occurrence["occurrence_id"]]
        orientation = leray_by_occurrence[occurrence["occurrence_id"]]["transverse_minor_determinant"]
        status_counts[status] += 1
        component_counts[(component, status)] += 1
        if sewn_nonzero:
            orientation_counts[orientation] += 1
        audits.append({
            "occurrence_id": occurrence["occurrence_id"],
            "source_orbit_key": occurrence["source_orbit_key"],
            "cyclic_shift": occurrence["cyclic_shift"],
            "attachment_component": component,
            "transverse_orientation": orientation,
            "contracted_degree_four_vector": [str(value) for value in contracted],
            "os_degree_four_ideal_rank": ideal_rank,
            "os_augmented_rank": augmented_rank,
            "contracted_class_nonzero_in_os": os_nonzero,
            "cyclic_projective_transport_scalar_from_shift_zero": str(transport_scalar),
            "local_source_fold_coefficient_nonzero": local_nonzero,
            "sewn_pairing_nonzero": sewn_nonzero,
            "status": status,
        })

    checks = {
        "occurrence_count": len(audits),
        "all_contracted_classes_nonzero_in_os": all(item["contracted_class_nonzero_in_os"] for item in audits),
        "status_counts": dict(sorted(status_counts.items())),
        "component_status_counts": {
            f"component_{component}:{status}": count
            for (component, status), count in sorted(component_counts.items())
        },
        "activated_orientation_counts": {str(key): value for key, value in sorted(orientation_counts.items())},
        "cyclic_support_is_closed": all(
            len({item["sewn_pairing_nonzero"] for item in audits if item["source_orbit_key"] == key}) == 1
            for key in local_by_key
        ),
        "all_cyclic_transports_preserve_the_projective_os_line": all(
            item["cyclic_projective_transport_scalar_from_shift_zero"] != "0" for item in audits
        ),
        "cyclic_projective_transport_scalar_distribution": dict(sorted(cyclic_projective_transport.items())),
    }
    assert checks["occurrence_count"] == 288
    assert checks["cyclic_support_is_closed"]

    packet = {
        "schema": "marici.eight_site_rank4_os_fold_sewing.v1",
        "typing": {
            "source_map": "rank-three excess contraction Lambda^7 -> Lambda^4",
            "sewing_map": "labelled degree-four projection to the complete occurrence OS quotient",
            "coefficient_map": "odd source-face derivative into the rank-one A1 fold line",
            "physical_scope": "algebraic Betti/de Rham sewing; absolute Bunch--Davies chain support tested separately",
        },
        "checks": checks,
        "occurrences": audits,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
