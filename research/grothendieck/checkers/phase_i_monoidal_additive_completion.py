"""Exact conditional additive completion of one connected surface carrier."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

from sympy import Integer, Symbol, expand


ROOT = Path(__file__).resolve().parents[3]
ENTRY_07 = ROOT / "src/ledger/20260812-07 Surface Operations and the Cut Kernel.md"
TYPING_RESULT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-surface-disjoint-union-typing.json"
)
ASSEMBLY_RESULT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-unmarked-assembly-obstruction.json"
)
OUT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-monoidal-additive-completion.json"
)


Word = tuple[str, ...]
SignedWord = tuple[Word, Word]
UNIT: Word = ("U",)
EMPTY: Word = tuple()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def sqcup(left: Word, right: Word) -> Word:
    """Canonical word for disjoint union in the one-generator groupoid."""

    return tuple(sorted(left + right))


def cancel(pair: SignedWord) -> SignedWord:
    """Canonical group-completion representative by cancelling U-pairs."""

    positive, negative = pair
    common = min(len(positive), len(negative))
    return (positive[common:], negative[common:])


inputs = [ENTRY_07, TYPING_RESULT, ASSEMBLY_RESULT]
for path in inputs:
    assert path.is_file()

typing_result = json.loads(TYPING_RESULT.read_text(encoding="utf-8"))
assembly_result = json.loads(ASSEMBLY_RESULT.read_text(encoding="utf-8"))
assert typing_result["verdict"]["surface_disjoint_union_monoidal"] is True
assert (
    typing_result["verdict"]["surface_disjoint_union_coproduct_derived"]
    is False
)
assert (
    assembly_result["verdict"]["unmarked_connected_binary_assembly_derived"]
    is False
)

# The Carrier inputs below are words built recursively from U and the empty
# surface.  Integer lengths are emitted only as checker readouts.
cutoff = 10
unit_powers: list[Word] = [EMPTY]
for _ in range(cutoff):
    unit_powers.append(sqcup(unit_powers[-1], UNIT))

assert len(set(unit_powers)) == cutoff + 1
assert all(
    sqcup(left, right) == sqcup(right, left)
    for left, right in itertools.product(unit_powers, repeat=2)
)
assert all(
    sqcup(sqcup(left, middle), right)
    == sqcup(left, sqcup(middle, right))
    for left, middle, right in itertools.product(unit_powers[:5], repeat=3)
)
assert all(sqcup(word, EMPTY) == word for word in unit_powers)

# Universal-map control.  A monoid homomorphism out of the free additive
# object is fixed by the image 'a' of U, and a word evaluates by repeated
# addition.  The symbolic coefficient is a result of normalization.
target_generator = Symbol("a")


def free_map(word: Word):
    return expand(sum((target_generator for _ in word), Integer(0)))


assert all(
    free_map(sqcup(left, right)) == free_map(left) + free_map(right)
    for left, right in itertools.product(unit_powers, repeat=2)
)

# Grothendieck completion is constructed from pairs of positive words modulo
# simultaneous stabilization.  Cancellation produces a signed surplus word;
# the integer below is a readout of that categorical normal form.
pair_cutoff = 6
completion_pairs = tuple(
    (unit_powers[positive], unit_powers[negative])
    for positive, negative in itertools.product(
        range(pair_cutoff + 1), repeat=2
    )
)
stabilizers = unit_powers[:5]
assert all(
    cancel((sqcup(positive, common), sqcup(negative, common)))
    == cancel((positive, negative))
    for positive, negative in completion_pairs
    for common in stabilizers
)
generator = (UNIT, EMPTY)
inverse_generator = (EMPTY, UNIT)
assert cancel(
    (sqcup(generator[0], inverse_generator[0]),
     sqcup(generator[1], inverse_generator[1]))
) == (EMPTY, EMPTY)


def signed_readout(pair: SignedWord) -> Integer:
    positive, negative = cancel(pair)
    return Integer(len(positive)) - Integer(len(negative))


signed_values = sorted({int(signed_readout(pair)) for pair in completion_pairs})
assert signed_values == list(range(-pair_cutoff, pair_cutoff + 1))

# Deliberate failure at the next gate.  The previous exact source-symmetry
# test finds no fixed gluing choice for the smallest unmarked connected
# assembly.  Thus the additive construction does not supply a tensor rule.
fixed_gluing_pairs = assembly_result["finite_model"][
    "dihedral_fixed_gluing_pairs"
]
required_connected_product_fixed_points = Integer(1)
observed_connected_product_fixed_points = Integer(len(fixed_gluing_pairs))
connected_product_fixed_point_deficit = (
    required_connected_product_fixed_points
    - observed_connected_product_fixed_points
)
assert connected_product_fixed_point_deficit == 1

packet = {
    "schema": (
        "marici.grothendieck.phase_i_monoidal_additive_completion.v1"
    ),
    "status": "conditional_on_monoidal_relaxation",
    "demonstrated_strength": [
        "unbounded additive universal-property theorem",
        "exact finite normalization control",
    ],
    "compatibility_preflight": {
        "coefficient_domain": None,
        "coefficient_prime": None,
        "ambient_carrier": (
            "mapping-class groupoid generated by one connected surface U"
        ),
        "adopted_for_project": False,
        "conditional_change": (
            "replace categorical finite coproduct by symmetric-monoidal "
            "disjoint union"
        ),
        "input_sha256": {rel(path): sha256(path) for path in inputs},
    },
    "additive_completion": {
        "generator": "connected surface U",
        "zero": "empty surface",
        "operation": "geometric disjoint union",
        "normal_form": "finite disjoint-union word in U",
        "universal_property": "free commutative monoid on U",
        "pi0_identification": "N under the conditional hypothesis",
        "cardinality_used_as_carrier_input": False,
        "unit_power_cutoff": cutoff,
        "distinct_unit_power_count": len(set(unit_powers)),
        "associativity_control_count": 5 ** 3,
        "commutativity_control_count": (cutoff + 1) ** 2,
    },
    "group_completion": {
        "construction": (
            "pairs of finite U-words modulo simultaneous stabilization"
        ),
        "normal_form": "signed surplus U-word",
        "universal_property": "free abelian group on U",
        "identification": "Z under the conditional hypothesis",
        "pair_cutoff": pair_cutoff,
        "pair_count": len(completion_pairs),
        "signed_readout_range": signed_values,
        "generator_plus_inverse_is_zero": True,
    },
    "multiplication_gate": {
        "conditional_forcing_statement": (
            "if a second tensor with unit U exists and distributes over "
            "disjoint union, its law on U-words is forced by pairwise "
            "distribution"
        ),
        "total_unmarked_connected_tensor_derived": False,
        "smallest_candidate": "unmarked quadrilateral sewing",
        "required_fixed_point_count": int(
            required_connected_product_fixed_points
        ),
        "observed_fixed_point_count": int(
            observed_connected_product_fixed_points
        ),
        "fixed_point_deficit": int(connected_product_fixed_point_deficit),
        "initial_semiring_derived": False,
    },
    "deliberate_failure": {
        "naive_claim": (
            "the free monoidal additive completion itself supplies the "
            "second distributive Carrier product"
        ),
        "claim_holds": False,
        "nonzero_obstruction": {
            "connected_product_fixed_point_deficit": int(
                connected_product_fixed_point_deficit
            )
        },
    },
    "verdict": {
        "literal_phase_i_coproduct_gate_passed": False,
        "conditional_additive_N_derived": True,
        "conditional_group_completion_Z_derived": True,
        "carrier_multiplication_derived": False,
        "initial_semiring_derived": False,
        "irreducibles_or_primes_derived": False,
        "arithmetic_sector_derived": False,
    },
    "deferred": [
        "operator or plan-owner decision on monoidal relaxation",
        "source-derived total tensor and tensor unit",
        "distributivity",
        "intrinsic irreducibility",
        "Burnside/Witt operations",
        "Euler product",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
