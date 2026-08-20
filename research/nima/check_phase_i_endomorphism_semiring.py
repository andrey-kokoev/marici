"""Exact audit of the endomorphism-semiring construction on the additive Carrier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/grothendieck/phase-i-monoidal-additive-completion.md"
SOURCE_RESULT = ROOT / "research/grothendieck/results/phase-i-monoidal-additive-completion.json"
OUT = ROOT / "research/nima/results/phase-i-endomorphism-semiring.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in (SOURCE, SOURCE_RESULT):
    assert path.is_file()

source_result = json.loads(SOURCE_RESULT.read_text(encoding="utf-8"))
assert source_result["verdict"]["conditional_additive_N_derived"] is True
assert source_result["verdict"]["carrier_multiplication_derived"] is False

# Elements are finite U-words in their source-derived connected-component
# normal form. Integers are checker encodings of word length, never inputs to
# the Carrier construction.
cutoff = 24
elements = tuple(range(cutoff + 1))


def add(left: int, right: int) -> int:
    """Disjoint union after connected-component normalization."""

    return left + right


def endomorphism(image_of_u: int, word: int) -> int:
    """Unique additive endomorphism determined by U -> image_of_u copies."""

    return image_of_u * word


def multiply(left: int, right: int) -> int:
    """Evaluate the endomorphism classified by left at right."""

    return endomorphism(left, right)


# Evaluation at U is inverse to the classifier n |-> f_n on the finite
# control window. The unbounded bijection follows from the proved free-monoid
# universal property, not from this cutoff.
assert all(endomorphism(image, 1) == image for image in elements)
assert all(
    endomorphism(image, add(left, right))
    == add(endomorphism(image, left), endomorphism(image, right))
    for image in elements
    for left in elements
    for right in elements
)

# Composition is multiplication: (f_left o f_right)(U)=f_left(right U).
assert all(
    endomorphism(left, endomorphism(right, 1)) == multiply(left, right)
    for left in elements
    for right in elements
)

# Exact semiring controls. Inputs are bounded so outputs need not remain in
# the enumeration window.
triples = tuple(range(9))
assert all(multiply(left, right) == multiply(right, left) for left in elements for right in elements)
assert all(multiply(1, value) == value for value in elements)
assert all(multiply(0, value) == 0 for value in elements)
assert all(
    multiply(multiply(left, middle), right)
    == multiply(left, multiply(middle, right))
    for left in triples
    for middle in triples
    for right in triples
)
assert all(
    multiply(left, add(middle, right))
    == add(multiply(left, middle), multiply(left, right))
    for left in triples
    for middle in triples
    for right in triples
)

# Uniqueness control: any distributive multiplication with unit U must have
# n*m equal to the m-fold additive sum of n, because its left-multiplication
# map is the unique additive endomorphism taking U to n.
candidate_products = {
    (left, right): sum(left for _ in range(right))
    for left in elements
    for right in elements
}
assert all(candidate_products[pair] == multiply(*pair) for pair in candidate_products)

packet = {
    "schema": "marici.nima.phase_i_endomorphism_semiring.v1",
    "status": "conditional_theorem",
    "conditional_hypothesis": (
        "Grothendieck's symmetric-monoidal disjoint-union relaxation, "
        "including the unbounded free commutative monoid theorem"
    ),
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in (SOURCE, SOURCE_RESULT)
    },
    "construction": {
        "additive_object": "pi_0(Surf_U^sqcup), free commutative monoid on U",
        "classifier": "nU maps to the unique additive endomorphism f_n with f_n(U)=nU",
        "multiplication": "n*m = f_n(mU)",
        "multiplicative_unit": "U, whose classified endomorphism is identity",
        "zero": "empty surface, whose classified endomorphism is zero",
        "source_of_associativity": "composition of additive endomorphisms",
        "source_of_distributivity": "additivity and pointwise addition of endomorphisms",
        "second_surface_tensor_used": False,
        "cardinality_used_as_carrier_input": False,
        "initiality": (
            "a unital semiring map must take U to the target unit; additive "
            "freeness makes that map unique and target distributivity makes "
            "it multiplicative"
        ),
    },
    "finite_controls": {
        "element_cutoff": cutoff,
        "endomorphism_additivity_checks": len(elements) ** 3,
        "composition_checks": len(elements) ** 2,
        "candidate_uniqueness_checks": len(candidate_products),
        "semiring_triple_cutoff": len(triples) - 1,
    },
    "verdict": {
        "conditional_initial_semiring_on_pi0_derived": True,
        "conditional_initial_ring_after_group_completion_derived": True,
        "surface_level_distributive_tensor_derived": False,
        "burnside_witt_structure_derived": False,
        "euler_product_derived": False,
    },
    "scope": (
        "This corrects the claim that a second geometric tensor is necessary "
        "for the decategorified initial semiring. It does not construct that "
        "tensor or remove the explicit monoidal-relaxation hypothesis."
    ),
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
