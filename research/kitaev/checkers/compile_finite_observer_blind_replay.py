#!/usr/bin/env python3
"""Exact blind replay of five finite observer/constructor benchmarks."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/kitaev/contracts/finite-observer-blind-replay.v1.json"
OUT = ROOT / "research/kitaev/results/finite-observer-blind-replay.json"


def gf2_rank(rows: list[int], width: int) -> int:
    work = list(rows)
    rank = 0
    for col in range(width):
        pivot = next((i for i in range(rank, len(work)) if (work[i] >> col) & 1), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(len(work)):
            if i != rank and ((work[i] >> col) & 1):
                work[i] ^= work[rank]
        rank += 1
    return rank


def minimum_subsets(items, predicate):
    items = list(items)
    lower_failures = []
    for size in range(len(items) + 1):
        passing = []
        for choice in itertools.combinations(items, size):
            if predicate(choice):
                passing.append(choice)
            else:
                lower_failures.append(choice)
        if passing:
            return size, passing, lower_failures
    return None, [], lower_failures


def powerset(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from itertools.combinations(items, size)


def matroid_rank_audit(items, rank_function):
    items = tuple(items)
    ranks = {frozenset(s): rank_function(s) for s in powerset(items)}
    normalized = ranks[frozenset()] == 0
    cardinality_bounded = all(0 <= rank <= len(s) for s, rank in ranks.items())
    monotone = all(ranks[a] <= ranks[b] for a in ranks for b in ranks if a <= b)
    submodular = all(
        ranks[a] + ranks[b] >= ranks[a | b] + ranks[a & b]
        for a in ranks for b in ranks
    )
    return {
        "normalized": normalized,
        "cardinality_bounded": cardinality_bounded,
        "monotone": monotone,
        "submodular": submodular,
        "is_matroid_rank": normalized and cardinality_bounded and monotone and submodular,
    }


def torus_incidence(L: int):
    vertex = lambda x, y: (x % L) * L + (y % L)
    horizontal = lambda x, y: (x % L) * L + (y % L)
    vertical = lambda x, y: L * L + (x % L) * L + (y % L)
    stars = []
    for x in range(L):
        for y in range(L):
            stars.append(
                (1 << horizontal(x, y))
                | (1 << horizontal(x - 1, y))
                | (1 << vertical(x, y))
                | (1 << vertical(x, y - 1))
            )
    faces = []
    for x in range(L):
        for y in range(L):
            faces.append(
                (1 << horizontal(x, y))
                | (1 << vertical(x + 1, y))
                | (1 << horizontal(x, y + 1))
                | (1 << vertical(x, y))
            )
    return stars, faces, horizontal, vertical


def run_toric(spec):
    L = spec["lattice_size"]
    stars, faces, h, v = torus_incidence(L)
    n_edges = 2 * L * L
    width = 2 * n_edges
    syndrome_rows = [star << n_edges for star in stars] + list(faces)
    stabilizer_generators = list(stars) + [face << n_edges for face in faces]
    stabilizer_rank = gf2_rank(stabilizer_generators, width)
    target_rank = width - stabilizer_rank

    z_h = sum(1 << h(x, 0) for x in range(L))
    z_v = sum(1 << v(0, y) for y in range(L))
    x_dual_v = sum(1 << h(0, y) for y in range(L))
    x_dual_h = sum(1 << v(x, 0) for x in range(L))
    candidates = {
        "z_horizontal_commutator": z_h,
        "z_vertical_commutator": z_v,
        "x_dual_vertical_commutator": x_dual_v << n_edges,
        "x_dual_horizontal_commutator": x_dual_h << n_edges,
    }
    base_rank = gf2_rank(syndrome_rows, width)

    def probe_rank(choice):
        return gf2_rank(syndrome_rows + [candidates[name] for name in choice], width) - base_rank

    def separates(choice):
        rows = syndrome_rows + [candidates[name] for name in choice]
        return gf2_rank(rows, width) == target_rank

    minimum, passing, lower = minimum_subsets(candidates, separates)
    witness = list(passing[0])
    maximum_lower_rank = max(
        gf2_rank(syndrome_rows + [candidates[name] for name in choice], width)
        for choice in lower if len(choice) < minimum
    )
    return {
        "mode": spec["mode"],
        "source_dimension": width,
        "stabilizer_rank": stabilizer_rank,
        "base_observer_rank": base_rank,
        "base_kernel_dimension": width - base_rank,
        "legal_kernel_dimension": stabilizer_rank,
        "candidate_count": len(candidates),
        "minimum_augmentation": minimum,
        "witness": witness,
        "full_rank": gf2_rank(syndrome_rows + [candidates[n] for n in witness], width),
        "target_rank": target_rank,
        "maximum_rank_with_fewer_probes": maximum_lower_rank,
        "first_missing_rank": target_rank - maximum_lower_rank,
        "all_smaller_subsets_fail": all(not separates(x) for x in lower if len(x) < minimum),
        "first_defect_without_augmentation": "observer_kernel",
        "closure_geometry": {
            "kind": "representable_probe_matroid",
            "rank": probe_rank(tuple(candidates)),
            "axioms": matroid_rank_audit(candidates, probe_rank),
        },
    }


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def run_flux_algebra(spec):
    degree = spec["permutation_degree"]
    group = list(itertools.permutations(range(degree)))
    target_dimension = len(group) ** 2

    def closure_dimension(selected):
        resolved = {
            h for g in selected for h in group if cycle_type(h) == cycle_type(g)
        }
        atoms = [(g,) for g in group if g in resolved]
        complement = tuple(g for g in group if g not in resolved)
        if complement:
            atoms.append(complement)
        atom_sets = {frozenset(atom) for atom in atoms}
        closed = all(
            frozenset(conjugate(x, g) for g in atom) in atom_sets
            for atom in atoms for x in group
        )
        assert closed
        return len(atoms) * len(group)

    candidates = [g for g in group if g != tuple(range(degree))]
    minimum, passing, lower = minimum_subsets(
        candidates, lambda choice: closure_dimension(choice) == target_dimension
    )
    witness = passing[0]
    one_port_max = max(closure_dimension([g]) for g in candidates)
    maximum_lower_dimension = max(
        closure_dimension(choice) for choice in lower if len(choice) < minimum
    )
    return {
        "mode": spec["mode"],
        "group_order": len(group),
        "target_algebra_dimension": target_dimension,
        "gauge_only_dimension": closure_dimension([]),
        "candidate_count": len(candidates),
        "maximum_one_candidate_dimension": one_port_max,
        "maximum_dimension_with_fewer_ports": maximum_lower_dimension,
        "first_missing_dimension": target_dimension - maximum_lower_dimension,
        "minimum_augmentation": minimum,
        "witness": [list(g) for g in witness],
        "witness_cycle_types": [list(cycle_type(g)) for g in witness],
        "full_dimension": closure_dimension(witness),
        "all_smaller_subsets_fail": all(
            closure_dimension(x) != target_dimension for x in lower if len(x) < minimum
        ),
        "first_defect_without_augmentation": "action_algebra_deficit",
        "physical_executability_certified": False,
        "closure_geometry": {
            "kind": "partition_matroid_on_nontrivial_conjugacy_types",
            "ground_parallel_classes": {
                str(list(kind)): sum(cycle_type(g) == kind for g in candidates)
                for kind in sorted({cycle_type(g) for g in candidates})
            },
            "rank": len({cycle_type(g) for g in candidates}),
            "algebra_dimension_is_a_weight_on_flats_not_matroid_rank": True,
        },
    }


def rational_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [x / pivot_value for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def rational_inverse(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        value = a[col][col]
        a[col] = [x / value for x in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[col])]
    return [row[n:] for row in a]


def run_boolean_zeta(spec):
    n = spec["label_count"]
    subsets = list(range(1 << n))
    zeta = [[int((s & t) == t) for s in subsets] for t in subsets]
    rank = rational_rank(zeta)
    inv = rational_inverse(zeta)
    mobius_law = all(
        inv[s][t] == (Fraction((-1) ** ((t ^ s).bit_count())) if (t & s) == s else 0)
        for s in subsets for t in subsets
    )
    return {
        "mode": spec["mode"],
        "route_count": len(subsets),
        "observation_count": len(subsets),
        "zeta_rank": rank,
        "kernel_dimension": len(subsets) - rank,
        "reconstruction": "mobius_inverse_derived",
        "derived_inverse_matches_boolean_mobius_law": mobius_law,
        "minimum_observation_rank": len(subsets),
        "rank_after_deleting_one_observation": rational_rank(zeta[:-1]),
        "first_defect_after_deleting_any_independent_row": "observer_kernel",
        "closure_geometry": {
            "kind": "free_representable_matroid",
            "rank": len(subsets),
            "ground_size": len(subsets),
        },
    }


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def run_repetition(spec):
    maximum = spec["maximum_copies"]
    t = spec["fault_weight"]
    rows = []
    detection_minimum = None
    correction_minimum = None
    for n in range(1, maximum + 1):
        code = {bit: (bit,) * n for bit in (0, 1)}
        corruptions = {
            bit: {
                tuple(v ^ int(i in positions) for i, v in enumerate(code[bit]))
                for weight in range(t + 1)
                for positions in itertools.combinations(range(n), weight)
            }
            for bit in (0, 1)
        }
        detects = all(
            word == code[bit] or word not in set(code.values())
            for bit in (0, 1) for word in corruptions[bit]
        )
        corrects = corruptions[0].isdisjoint(corruptions[1])
        rows.append({"copies": n, "detects": detects, "corrects": corrects})
        if detects and detection_minimum is None:
            detection_minimum = n
        if corrects and correction_minimum is None:
            correction_minimum = n
    return {
        "mode": spec["mode"],
        "fault_weight": t,
        "search": rows,
        "minimum_copies_for_detection": detection_minimum,
        "minimum_copies_for_correction": correction_minimum,
        "lower_detection_sizes_fail": all(not r["detects"] for r in rows if r["copies"] < detection_minimum),
        "lower_correction_sizes_fail": all(not r["corrects"] for r in rows if r["copies"] < correction_minimum),
        "common_mode_flip_invisible": True,
        "quantum_actuator_repair_inferred": False,
        "closure_geometry": {
            "kind": "hamming_code_geometry",
            "fixed_ground_set_probe_matroid": False,
            "reason": "changing replica count changes the carrier and fault balls",
        },
    }


def frac(x):
    return Fraction(x)


def mat_vec(matrix, vector):
    return [sum((frac(a) * b for a, b in zip(row, vector)), Fraction(0)) for row in matrix]


def dot(row, vector):
    return sum((frac(a) * b for a, b in zip(row, vector)), Fraction(0))


def run_sequential(spec):
    source = [frac(x) for x in spec["source_vector"]]
    effect = [frac(x) for x in spec["terminal_effect"]]
    candidates = spec["candidate_projectors"]

    def amplitude(sequence):
        state = source
        for name in sequence:
            state = mat_vec(candidates[name], state)
        return dot(effect, state)

    direct = amplitude(())
    names = list(candidates)
    passing = []
    lower = []
    minimum = None
    for size in range(spec["maximum_insertions"] + 1):
        candidates_at_size = list(itertools.product(names, repeat=size))
        passing = [sequence for sequence in candidates_at_size if amplitude(sequence) != 0]
        lower.extend(sequence for sequence in candidates_at_size if amplitude(sequence) == 0)
        if passing:
            minimum = size
            break
    witness = passing[0]
    amp = amplitude(witness)
    single_step_intensities = {
        name: str(amplitude((name,)) ** 2) for name in names
    }
    return {
        "mode": spec["mode"],
        "direct_amplitude": str(direct),
        "direct_intensity": str(direct * direct),
        "minimum_insertions": minimum,
        "witness": list(witness),
        "witness_amplitude": str(amp),
        "witness_intensity": str(amp * amp),
        "minimum_witness_count": len(passing),
        "single_step_intensities": single_step_intensities,
        "all_smaller_subsets_fail": all(amplitude(x) == 0 for x in lower if len(x) < minimum),
        "constructor_closure_changes_effective_observation": True,
        "simple_parallel_gramian_addition_used": False,
        "closure_geometry": {
            "kind": "ordered_constructor_word_semigroup",
            "fixed_ground_set_probe_matroid": False,
            "reason": "sequential products depend on word order and may repeat generators",
        },
    }


RUNNERS = {
    "toric_gf2": run_toric,
    "finite_group_flux_algebra": run_flux_algebra,
    "boolean_zeta": run_boolean_zeta,
    "repetition_fault": run_repetition,
    "sequential_rational_instrument": run_sequential,
}


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    results = {}
    for spec in contract["benchmarks"]:
        results[spec["id"]] = RUNNERS[spec["mode"]](spec)

    gates = {
        "five_primitive_packets_loaded": len(results) == 5,
        "toric_minimum_derived": results["toric_phase_free_pauli_quotient"]["all_smaller_subsets_fail"],
        "ds3_minimum_derived": results["ds3_flux_resolved_endpoint_algebra"]["all_smaller_subsets_fail"],
        "boolean_routes_reconstructed": results["boolean_deletion_route_reconstruction"]["kernel_dimension"] == 0,
        "replica_minima_derived": results["classical_replica_single_flip"]["lower_detection_sizes_fail"] and results["classical_replica_single_flip"]["lower_correction_sizes_fail"],
        "sequential_visibility_derived": results["crossed_polarizer_visibility"]["all_smaller_subsets_fail"],
        "physical_authority_not_inferred": not results["ds3_flux_resolved_endpoint_algebra"]["physical_executability_certified"],
        "closure_geometries_typed": (
            results["toric_phase_free_pauli_quotient"]["closure_geometry"]["axioms"]["is_matroid_rank"]
            and results["ds3_flux_resolved_endpoint_algebra"]["closure_geometry"]["rank"] == 2
            and results["boolean_deletion_route_reconstruction"]["closure_geometry"]["kind"] == "free_representable_matroid"
            and not results["classical_replica_single_flip"]["closure_geometry"]["fixed_ground_set_probe_matroid"]
            and not results["crossed_polarizer_visibility"]["closure_geometry"]["fixed_ground_set_probe_matroid"]
        ),
    }
    packet = {
        "schema": "marici.kitaev.finite-observer-blind-replay-result.v1",
        "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        "benchmarks": results,
        "aggregate_gates": gates,
        "passed": all(gates.values()),
        "claim_boundary": "Finite exact re-derivation from primitive declared packets; no infinite completion, source-authority discovery, or physical implementation theorem.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    raise SystemExit(0 if packet["passed"] else 1)


if __name__ == "__main__":
    main()
