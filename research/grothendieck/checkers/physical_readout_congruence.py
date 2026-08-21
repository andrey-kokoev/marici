"""Exact finite controls for the universal physical-readout congruence."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUTS = {
    "three_level_audit": ROOT / "research/grothendieck/results/phase-i-three-level-reconciliation-audit.json",
    "flavor": ROOT / "research/nima/results/phase-i-flavor-lens-readout-abelianization.json",
    "scattering": ROOT / "research/nima/results/phase-i-m2-ward-d4-factorization.json",
    "cosmology": ROOT / "research/benincasa/results/five-site-kummer-betti-pairing.json",
    "string_gate": ROOT / "research/nima/phase-i-string-readout-abelianization-gate.md",
    "string_d5": ROOT / "research/nima/results/phase-i-string-disk-readout-d5.json",
    "string_all_arity": ROOT / "research/nima/results/string-disk-readout-dihedral-all-arity.json",
    "radiative_memory_d3": ROOT / "research/nima/results/radiative-memory-d3-commutator.json",
    "radiative_memory_d3_invariants": ROOT / "research/nima/results/radiative-memory-d3-invariants.json",
}
OUT = ROOT / "research/grothendieck/results/physical-readout-congruence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in INPUTS.values():
    assert path.is_file(), path

source = {
    name: (
        json.loads(path.read_text(encoding="utf-8"))
        if path.suffix == ".json"
        else path.read_text(encoding="utf-8")
    )
    for name, path in INPUTS.items()
}

assert source["three_level_audit"]["verdict"]["grothendieck_full_carrier_closure_preserved"] is True
assert source["three_level_audit"]["verdict"]["conditional_pi0_verdict_corrected"] is True
assert source["flavor"]["coefficient_lens"]["factors_through_S3_abelianization"] is False
assert source["flavor"]["physical_readout"]["all_exact_weak_basis_invariants_preserved"] is True
assert source["scattering"]["representation"]["factors_through_D4_ab"] is True
assert source["cosmology"]["result"] == (
    "The coefficient-Betti pairing is strictly invariant under simultaneous deck transport."
)
assert "no existing artifact constructs the global physical readout" in source["string_gate"]
assert source["string_d5"]["passed"] is True
assert source["string_d5"]["all_commutators_killed"] is True
assert source["string_d5"]["factors_through_abelianization"] == "D5_ab = C2"
assert source["string_all_arity"]["passed"] is True
assert source["string_all_arity"]["audited_arities"] == list(range(3, 17))
assert all(row["all_commutators_killed"] for row in source["string_all_arity"]["audits"])
assert source["radiative_memory_d3"]["passed"] is True
assert source["radiative_memory_d3"]["directional_plane_rank"] == 2
assert source["radiative_memory_d3"]["commutator_detected"] is True
assert source["radiative_memory_d3"]["reflection_matrix"] == [[1, 0], [1, -1]]
assert source["radiative_memory_d3_invariants"]["passed"] is True
assert source["radiative_memory_d3_invariants"]["invariant_ring"] == "Q[a,b]^D3 = Q[q2,q3]"
assert source["radiative_memory_d3_invariants"]["bounded_orbits_separated"] is True

Permutation = tuple[int, ...]


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(value: Permutation) -> Permutation:
    result = [0] * len(value)
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def closure(identity: Permutation, generators: tuple[Permutation, ...]) -> set[Permutation]:
    group = {identity}
    changed = True
    while changed:
        changed = False
        for left in tuple(group):
            for right in generators + tuple(group):
                product = compose(left, right)
                if product not in group:
                    group.add(product)
                    changed = True
    return group


def commutator_subgroup(group: set[Permutation], identity: Permutation) -> set[Permutation]:
    commutators = tuple(
        compose(compose(compose(left, right), inverse(left)), inverse(right))
        for left, right in itertools.product(group, repeat=2)
    )
    return closure(identity, commutators)


# Flavor control: the S3 coefficient presentation sees its commutator A3,
# while a symmetric physical readout is invariant under the whole group.
s3_identity = (0, 1, 2)
s3_cycle = (1, 2, 0)
s3_swap = (1, 0, 2)
s3 = closure(s3_identity, (s3_cycle, s3_swap))
s3_commutator = commutator_subgroup(s3, s3_identity)
assert len(s3) == 6
assert len(s3_commutator) == 3
assert s3_cycle in s3_commutator

coefficient_vector = (1, 2, 4)


def permute(vector: tuple[int, ...], permutation: Permutation) -> tuple[int, ...]:
    result = [0] * len(vector)
    for source_index, target_index in enumerate(permutation):
        result[target_index] = vector[source_index]
    return tuple(result)


def physical_invariant(vector: tuple[int, ...]) -> tuple[int, int]:
    return sum(vector), sum(value * value for value in vector)


assert permute(coefficient_vector, s3_cycle) != coefficient_vector
assert all(
    physical_invariant(permute(coefficient_vector, value))
    == physical_invariant(coefficient_vector)
    for value in s3
)

# Scattering control: the D4 orientation line kills the commutator, whereas
# the standard rank-two D4 representation detects the same half-turn. This
# is the minimal hostile counterexample showing why a rank-one pass cannot
# authorize universal abelianization.
d4_identity = (0, 1, 2, 3)
d4_rotation = (1, 2, 3, 0)
d4_reflection = (0, 3, 2, 1)
d4 = closure(d4_identity, (d4_rotation, d4_reflection))
d4_commutator = commutator_subgroup(d4, d4_identity)
d4_half_turn = compose(d4_rotation, d4_rotation)
assert len(d4) == 8
assert d4_commutator == {d4_identity, d4_half_turn}


def orientation_character(value: Permutation) -> int:
    oriented_edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    image_edge = (value[0], value[1])
    return 1 if image_edge in oriented_edges else -1


assert all(orientation_character(value) == 1 for value in d4_commutator)

# Standard square representation: r^2 acts as -I and is observable.
rank_two_probe = (1, 0)
half_turn_matrix = ((-1, 0), (0, -1))
rank_two_image = (
    half_turn_matrix[0][0] * rank_two_probe[0] + half_turn_matrix[0][1] * rank_two_probe[1],
    half_turn_matrix[1][0] * rank_two_probe[0] + half_turn_matrix[1][1] * rank_two_probe[1],
)
assert rank_two_image != rank_two_probe

# Cosmology control: exact simultaneous translation invariance of the
# coefficient-Betti delta pairing for G=(C2)^5. The commutator test is
# vacuous because this source group is already abelian.
deck_group = tuple(range(32))
deck_pairing_checks = 0
for shift, left, right in itertools.product(deck_group, repeat=3):
    before = int(left == right)
    after = int((left ^ shift) == (right ^ shift))
    assert before == after
    deck_pairing_checks += 1

# Conditional pi_0 descent control. Every additive congruence on the free
# rank-one commutative monoid is automatically stable under the multiplication
# classified by additive endomorphisms, because multiplication by a fixed
# element is repeated addition.
congruence_checks = 0
cutoff = 12
for modulus in range(2, 8):
    for left, left_prime, right, right_prime in itertools.product(range(cutoff + 1), repeat=4):
        if left % modulus == left_prime % modulus and right % modulus == right_prime % modulus:
            assert (left + right) % modulus == (left_prime + right_prime) % modulus
            assert (left * right) % modulus == (left_prime * right_prime) % modulus
            congruence_checks += 1

out = {
    "schema": "marici.grothendieck.physical_readout_congruence.v1",
    "status": "conditional_universal_theorem_with_exact_falsifier",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in INPUTS.values()
    },
    "universal_construction": {
        "prerequisite": "a nonempty family of typed physical-observable representations",
        "observable_kernel": "K_obs = intersection_i ker(rho_i) on typed physical-observable representations",
        "invisible_commutator_kernel": "K_phys = [G,G] intersection K_obs",
        "quotient": "G_phys = G/K_phys",
        "universal_property": (
            "Every group quotient that kills all and only the jointly invisible "
            "commutators factors uniquely through G_phys"
        ),
        "abelian_exactly_when": "[G,G] is contained in K_obs",
        "untyped_when": "no global physical-observable representation rho_i is constructed",
    },
    "distinct_invariant_quotient": {
        "object": "Spec A[V]^G",
        "universal_property": "universal among G-invariant affine maps out of V",
        "question": "which invariant scalar records distinguish physical orbits",
        "is_group_abelianization": False,
        "determined_by_representation_kernel_quotient": False,
        "d3_control_ring": source["radiative_memory_d3_invariants"]["invariant_ring"],
        "d3_bounded_orbits_separated": source["radiative_memory_d3_invariants"]["bounded_orbits_separated"],
    },
    "pi0_descent": {
        "isotropy_only_quotient": "pi_0 is unchanged, so its conditional semiring descends identically",
        "object_congruence_criterion": "the readout equivalence must be an additive monoid congruence",
        "rank_one_theorem": (
            "on the free commutative monoid generated by U, every additive "
            "congruence is automatically stable under endomorphism multiplication"
        ),
        "finite_modular_controls": congruence_checks,
        "carrier_tensor_assumed": False,
    },
    "sector_controls": {
        "flavor": {
            "source_group": "S3",
            "commutator_order": len(s3_commutator),
            "coefficient_probe_detects_commutator": True,
            "physical_symmetric_readout_is_invariant": True,
        },
        "cosmology": {
            "source_group": "(C2)^5",
            "already_abelian": True,
            "simultaneous_pairing_checks": deck_pairing_checks,
            "status": "positive pairing architecture; vacuous commutator test",
        },
        "scattering": {
            "source_group": "D4",
            "commutator_order": len(d4_commutator),
            "orientation_line_kills_commutator": True,
            "rank_two_standard_probe_detects_half_turn": True,
            "status": "rank-one source test passes but is non-hostile",
        },
        "string_five_point": {
            "physical_scalar_assembly_exists": True,
            "source_group": "D5",
            "commutator_order": 5,
            "commutator_kernel_explicitly_computed": True,
            "factors_through": "D5_ab = C2",
            "status": "positive physical-readout quotient",
        },
        "string_disk_all_arity": {
            "character": "chi_n(r)=1, chi_n(s)=(-1)^n",
            "exact_control_arities": list(range(3, 17)),
            "all_commutators_killed": True,
            "odd_abelianization": "C2",
            "even_abelianization": "C2 x C2",
        },
        "string_six_point_exceptional_module": {
            "coefficient_module_rank": 8,
            "coefficient_covariance": "reflection-covariant with trivial cyclic holonomy",
            "global_source_cycle": None,
            "global_pairing": None,
            "commutator_descent_status": "untyped",
            "missing_datum": "N_shift tensor Gamma_source -> C with both variances transported",
        },
        "radiative_memory": {
            "physical_readout": "three direction-labelled samples of Delta C_zz = D_z^2 N",
            "source_group": "D3 celestial-direction symmetry",
            "decomposition": "trivial scalar line plus rank-two directional difference plane",
            "commutator_subgroup": "C3 generated by r",
            "commutator_detected_on_directional_plane": True,
            "factors_through_abelianization": False,
            "invariant_ring": "Q[a,b]^D3 = Q[q2,q3]",
            "invariant_generators": ["q2=a^2-a*b+b^2", "q3=a*b*(a-b)"],
            "invariant_scalarization_is_group_abelianization": False,
            "bounded_orbits_separated_by_invariants": True,
            "status": "first source-established higher-rank physical commutator detector",
        },
    },
    "deliberate_failure": {
        "naive_claim": "every higher-dimensional D4 observable factors through D4_ab",
        "claim_holds": False,
        "witness": "the standard rank-two square representation detects the commutator half-turn r^2",
    },
    "verdict": {
        "universal_physical_readout_congruence_defined": True,
        "automatic_abelianization": False,
        "conditional_pi0_semiring_descends_under_additive_congruence": True,
        "carrier_level_tensor_reopened": False,
        "string_disk_readout_all_arity_abelianization_derived": True,
        "six_point_exceptional_module_descent_proved": False,
        "universal_physical_abelian_shadow_falsified": True,
        "invariant_scalarization_is_not_group_abelianization": True,
        "arithmetic_invariant_record_algebra_remains_conditional": True,
        "phase_ii_authorized": False,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
