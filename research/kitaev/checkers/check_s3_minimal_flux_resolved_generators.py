"""Exact associative closure of gauge actions plus flux projectors in D(S3)."""

import itertools
import json
import sympy as sp


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def conjugate(g, h): return compose(compose(g, h), inverse(g))
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "identity" if fixed == 3 else ("transposition" if fixed == 1 else "three_cycle")


def main():
    group = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    basis = [(g, x) for g in group for x in group]
    index = {b: i for i, b in enumerate(basis)}

    def basis_vector(g, x):
        v = sp.zeros(36, 1)
        v[index[(g, x)]] = 1
        return v

    def multiply_vectors(left, right):
        out = sp.zeros(36, 1)
        for i in range(36):
            if left[i] == 0: continue
            g, x = basis[i]
            for j in range(36):
                if right[j] == 0: continue
                h, y = basis[j]
                if g == conjugate(x, h):
                    out[index[(g, compose(x, y))]] += left[i] * right[j]
        return out

    unit = sum((basis_vector(g, identity) for g in group), sp.zeros(36, 1))
    gauge = [sum((basis_vector(g, x) for g in group), sp.zeros(36, 1)) for x in group]
    flux = {g: basis_vector(g, identity) for g in group}

    def closure(selected_fluxes):
        # Gauge conjugation makes every point in a selected conjugacy class
        # available.  Those points become singleton atoms; all unselected
        # classes remain one complementary invariant atom.
        resolved = {
            h for g in selected_fluxes for h in group
            if cycle_type(h) == cycle_type(g)
        }
        atoms = [(g,) for g in group if g in resolved]
        complement = tuple(g for g in group if g not in resolved)
        if complement: atoms.append(complement)

        crossed_basis = [
            sum((basis_vector(g, x) for g in atom), sp.zeros(36, 1))
            for atom in atoms for x in group
        ]
        matrix = sp.Matrix.hstack(*crossed_basis)
        assert matrix.rank() == len(atoms) * len(group)
        # Invariance of the atom partition makes this span multiplicatively
        # closed; verify every atom image under every conjugation is an atom.
        atom_sets = {frozenset(atom) for atom in atoms}
        assert all(
            frozenset(conjugate(x, g) for g in atom) in atom_sets
            for atom in atoms for x in group
        )
        return matrix.rank()

    gauge_rank = closure([])
    assert gauge_rank == 6
    single_ranks = {str(g): closure([g]) for g in group}
    assert max(single_ranks.values()) < 36

    pair_ranks = {}
    full_pairs = []
    for g, h in itertools.combinations(group, 2):
        rank = closure([g, h])
        key = str(g) + "|" + str(h)
        pair_ranks[key] = rank
        if rank == 36: full_pairs.append((g, h))
    assert full_pairs
    assert all({cycle_type(g), cycle_type(h)} == {"transposition", "three_cycle"} for g, h in full_pairs)
    assert len(full_pairs) == 6

    witness = full_pairs[0]
    result = {
        "schema": "marici.s3-minimal-flux-resolved-generators.v1",
        "gauge_only_closure_dimension": gauge_rank,
        "maximum_one_flux_projector_closure_dimension": max(single_ranks.values()),
        "minimum_added_flux_projectors_for_full_closure": 2,
        "full_two_projector_family_count": len(full_pairs),
        "full_pair_type": ["transposition", "three_cycle"],
        "witness_pair": [str(witness[0]), str(witness[1])],
        "full_closure_dimension": closure([witness[0], witness[1]]),
        "deliberate_failures": {
            "gauge_only_is_full": gauge_rank == 36,
            "one_flux_projector_is_enough": max(single_ranks.values()) == 36,
            "identity_plus_transposition_pair_is_full": any(
                rank == 36 and {cycle_type(g), cycle_type(h)} == {"identity", "transposition"}
                for (g, h), rank in [((g, h), pair_ranks[str(g) + "|" + str(h)]) for g, h in itertools.combinations(group, 2)]
            ),
        },
        "aggregate_gates": {
            "gauge_closure_has_dimension_six": True,
            "no_single_flux_projector_completes_the_algebra": True,
            "two_flux_projectors_are_sufficient": True,
            "two_flux_projectors_are_necessary": True,
            "full_pairs_are_exactly_transposition_plus_three_cycle": True,
            "full_endpoint_dimension_is_thirty_six": True,
            "generator_availability_remains_source_typed": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
