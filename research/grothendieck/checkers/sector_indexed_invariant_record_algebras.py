"""Exact controls for the first sector-indexed invariant-record composition."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
INPUTS = {
    "census": ROOT / "research/nima/results/cross-sector-readout-algebra-types.json",
    "memory_commutator": ROOT / "research/nima/results/radiative-memory-d3-commutator.json",
    "memory_invariants": ROOT / "research/nima/results/radiative-memory-d3-invariants.json",
    "system_typing": ROOT / "research/nima/sector-indexed-readout-algebra-system.md",
    "memory_composition": ROOT / "research/nima/results/radiative-memory-readout-composition.json",
    "cosmology_composition": ROOT / "research/nima/results/cosmology-readout-composition.json",
    "arithmetic_naturality": ROOT / "research/nima/results/readout-arithmetic-naturality.json",
    "prime_to_exponent": ROOT / "research/nima/results/prime-to-exponent-readout-operations.json",
    "deck_selection_variance": ROOT / "research/nima/results/deck-selection-variance.json",
    "finite_deck_transfer": ROOT / "research/nima/results/finite-deck-transfer.json",
}
OUT = ROOT / "research/grothendieck/results/sector-indexed-invariant-record-algebras.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in INPUTS.values():
    assert path.is_file(), path

census = json.loads(INPUTS["census"].read_text(encoding="utf-8"))
commutator = json.loads(INPUTS["memory_commutator"].read_text(encoding="utf-8"))
invariants = json.loads(INPUTS["memory_invariants"].read_text(encoding="utf-8"))
typing = INPUTS["system_typing"].read_text(encoding="utf-8")
memory_composition = json.loads(INPUTS["memory_composition"].read_text(encoding="utf-8"))
cosmology_composition = json.loads(INPUTS["cosmology_composition"].read_text(encoding="utf-8"))
arithmetic_naturality = json.loads(INPUTS["arithmetic_naturality"].read_text(encoding="utf-8"))
prime_to_exponent = json.loads(INPUTS["prime_to_exponent"].read_text(encoding="utf-8"))
deck_selection_variance = json.loads(INPUTS["deck_selection_variance"].read_text(encoding="utf-8"))
finite_deck_transfer = json.loads(INPUTS["finite_deck_transfer"].read_text(encoding="utf-8"))

assert census["passed"] is True
assert census["cross_sector_constructor_maps"] == "none source-derived in the audited packets"
assert census["conditional_arithmetic_naturality"] == "untyped without those maps"
assert commutator["commutator_detected"] is True
assert invariants["invariant_ring"] == "Q[a,b]^D3 = Q[q2,q3]"
assert "sector-indexed system" in typing
assert memory_composition["passed"] is True
assert cosmology_composition["passed"] is True
assert arithmetic_naturality["passed"] is True
assert arithmetic_naturality["common_physical_arithmetic_action"] is False
assert prime_to_exponent["passed"] is True
assert prime_to_exponent["cosmology_C2_power5_survivors"] == "positive odd integers"
assert deck_selection_variance["passed"] is True
assert finite_deck_transfer["passed"] is True
assert finite_deck_transfer["normalization"] == "unnormalized fiber sum; averaging is rejected"

x, y, z, a, b = sp.symbols("x y z a b")
e1 = x + y + z
e2 = x * y + x * z + y * z
e3 = x * y * z
q2 = a**2 - a * b + b**2
q3 = a * b * (a - b)

# Inclusion i: (a,b) |-> (a,-a+b,-b).
inc = {x: a, y: -a + b, z: -b}
i_star = {
    "e1": sp.expand(e1.subs(inc, simultaneous=True)),
    "e2": sp.expand(e2.subs(inc, simultaneous=True)),
    "e3": sp.expand(e3.subs(inc, simultaneous=True)),
}
assert sp.simplify(i_star["e1"]) == 0
assert sp.simplify(i_star["e2"] + q2) == 0
assert sp.simplify(i_star["e3"] - q3) == 0

# Difference projection d subtracts the mean. In plane coordinates a'=x', b'=-z'.
mean = e1 / 3
a_centered = x - mean
b_centered = -(z - mean)
d_q2 = sp.expand(q2.subs({a: a_centered, b: b_centered}, simultaneous=True))
d_q3 = sp.expand(q3.subs({a: a_centered, b: b_centered}, simultaneous=True))
expected_d_q2 = sp.expand(e1**2 / 3 - e2)
expected_d_q3 = sp.expand(e3 - e1 * e2 / 3 + 2 * e1**3 / 27)
assert sp.simplify(d_q2 - expected_d_q2) == 0
assert sp.simplify(d_q3 - expected_d_q3) == 0

# Contravariance for d o i = id_V: i* o d* fixes both invariant generators.
assert sp.simplify(d_q2.subs(inc, simultaneous=True) - q2) == 0
assert sp.simplify(d_q3.subs(inc, simultaneous=True) - q3) == 0

# Equivariance of the centering idempotent against the exact permutation generators.
r3 = sp.Matrix(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
s3 = sp.Matrix(((1, 0, 0), (0, 0, 1), (0, 1, 0)))
identity3 = sp.eye(3)
centering = identity3 - sp.ones(3, 3) / 3
assert centering * centering == centering
assert centering * r3 == r3 * centering
assert centering * s3 == s3 * centering

# The second sourced square: diagonal deck quotient followed by delta_0.
cosmology_composition_checks = 0
cosmology_orbit_fiber_checks = 0
cosmology_deck_checks = 0
for g in range(32):
    for h in range(32):
        difference = g ^ h
        assert int(difference == 0) == int(g == h)
        cosmology_composition_checks += 1
        fiber = {(u, u ^ difference) for u in range(32)}
        orbit = {(g ^ k, h ^ k) for k in range(32)}
        assert fiber == orbit
        cosmology_orbit_fiber_checks += 1
        for k in range(32):
            assert ((g ^ k) ^ (h ^ k)) == difference
            assert int((g ^ k) == (h ^ k)) == int(g == h)
            cosmology_deck_checks += 1
assert cosmology_composition_checks == 1024
assert cosmology_orbit_fiber_checks == 1024
assert cosmology_deck_checks == 32768

result = {
    "schema": "marici.grothendieck.sector_indexed_invariant_record_algebras.v1",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in INPUTS.values()
    },
    "typed_morphism_criterion": {
        "source_constructor_required": True,
        "declared_group_homomorphism_and_equivariance_required": True,
        "observable_subalgebra_pullback_closure_required": True,
        "physical_selection_compatibility_required": True,
        "support_chain_framing_coherence_transport_required": True,
        "arbitrary_algebra_homomorphism_sufficient": False,
    },
    "sector_census": {
        "object_count": 4,
        "memory": census["memory"],
        "strings": census["strings"],
        "cosmology": census["cosmology"],
        "flavor": census["flavor"],
        "admitted_cross_sector_morphism_count": 0,
    },
    "first_admitted_fiberwise_composition": {
        "sector": "radiative memory",
        "permutation_module": "P=Q^3",
        "directional_plane": "V=ker(x+y+z)",
        "constructors": ["F:P->V subtracting the constant mode", "E:V->Spec Q[q2,q3] invariant scalarization"],
        "equivariant": True,
        "F_star": {
            "q2": "e1^2/3-e2",
            "q3": "e3-e1*e2/3+2*e1^3/27",
        },
        "contravariant_composition_verified": True,
        "composition_checks": memory_composition["composition_checks"],
        "permutation_checks": memory_composition["permutation_checks"],
        "constant_mode_translation_checks": memory_composition["constant_mode_translation_checks"],
        "admitted_as_typed_readout_morphism": True,
    },
    "rejected_algebraic_section": {
        "map": "i:V->P zero-mean inclusion",
        "i_star": {key: str(value) for key, value in i_star.items()},
        "split_retraction_identity": "i_star o F_star = id on Q[q2,q3]",
        "algebraically_verified": True,
        "physical_constructor_provenance_supplied": False,
        "admitted_as_typed_readout_morphism": False,
    },
    "second_admitted_fiberwise_composition": {
        "sector": "five-site cosmology",
        "constructors": ["F(g,h)=g xor h diagonal-deck orbit quotient", "E=delta_0 identity primitive idempotent"],
        "composite": "delta_0(g xor h)=delta_(g,h)",
        "composition_checks": cosmology_composition_checks,
        "orbit_fiber_checks": cosmology_orbit_fiber_checks,
        "deck_invariance_checks": cosmology_deck_checks,
        "admitted_as_typed_readout_morphism": True,
    },
    "shared_diagram_shape": {
        "shape": "quotient covariant redundancy, then apply invariant physical selection",
        "sector_count": 2,
        "cross_sector_algebra_map_asserted": False,
    },
    "arithmetic_naturality": {
        "formal_repetition_maps_tested": True,
        "memory_pullback": "q2 -> n^2 q2; q3 -> n^3 q3",
        "memory_graded_naturality": True,
        "cosmology_quotient_naturality": True,
        "cosmology_selection_compatible_indices": arithmetic_naturality["cosmology"]["physical_selection_natural_for_n"],
        "even_index_failure_count_per_index": 992,
        "full_conditional_semiring_action_selection_compatible": False,
        "commutativity_sufficient": False,
        "general_criterion": "[n]^* delta_0 = delta_0 iff gcd(n, exponent(G)) = 1",
        "maximal_common_index_system_for_memory_and_C2_power5": "positive odd multiplicative monoid",
        "closed_under_multiplication": True,
        "closed_under_addition": False,
        "is_semiring": False,
        "adams_frobenius_lambda_structure_claimed": False,
        "missing_resource_for_larger_action": "independently sourced sectorwise physical repetition constructors and selection coherence",
        "status": "exact obstruction with prime-to-exponent multiplicative survivor",
    },
    "deck_map_variance": {
        "pullback_identity": "phi^* delta_0,H = indicator_(ker phi)",
        "pullback_preserves_identity_selection_iff": "phi is injective",
        "homomorphisms_tested": deck_selection_variance["homomorphism_count"],
        "selection_pullback_checks": deck_selection_variance["selection_pullback_checks"],
        "multiplication_maps_natural_for_all_homomorphisms": True,
        "group_level_naturality_implies_selection_naturality": False,
        "noninjective_maps_require_covariant_resource": True,
    },
    "finite_deck_transfer_candidate": {
        "operation": "phi_! f(h) = sum_(g:phi(g)=h) f(g)",
        "selection_identity": "phi_! delta_0,G = delta_0,H",
        "normalization": "unnormalized fiber sum",
        "averaging_preserves_frozen_selection": False,
        "strict_composition": True,
        "frobenius_reciprocity": True,
        "homomorphisms_tested": finite_deck_transfer["homomorphism_count"],
        "frobenius_reciprocity_checks": finite_deck_transfer["frobenius_reciprocity_checks"],
        "composition_checks": finite_deck_transfer["composition_checks"],
        "algebraically_canonical": True,
        "physically_admitted": False,
        "missing_resource": "source-derived deck trace/Gysin map with orientation, support, multiplicity, and chain normalization",
    },
    "verdict": {
        "sector_indexed_category_typed": True,
        "algebraic_split_retraction_verified": True,
        "admitted_nonidentity_fiberwise_compositions_verified": 2,
        "shared_diagram_shape_verified_in_two_sectors": True,
        "cross_sector_system_constructed": False,
        "conditional_arithmetic_naturality_proved": False,
        "automatic_common_semiring_action_falsified": True,
        "prime_to_exponent_multiplicative_survivor_derived": True,
        "pullback_variance_theorem_derived": True,
        "finite_deck_transfer_is_physical_theorem": False,
        "carrier_multiplication_added": False,
        "phase_ii_authorized": False,
        "passed": True,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
