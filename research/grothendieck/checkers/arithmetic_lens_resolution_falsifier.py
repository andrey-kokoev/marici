"""Falsify an untyped Carrier-intrinsic torsion readout on an exact diagram."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[3]
PARITY_PATH = (
    ROOT
    / "research/benincasa/results/"
    "rank12-e6-parity-occurrence-composition.json"
)
COUSIN_PATH = (
    ROOT
    / "research/benincasa/results/"
    "rank12-e6-integral-cousin-comparison.json"
)
OUT = (
    ROOT
    / "research/grothendieck/results/"
    "arithmetic-lens-resolution-falsifier.json"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def smith_nonzero(matrix: Matrix) -> list[int]:
    diagonal = smith_normal_form(matrix, domain=ZZ)
    invariants: list[int] = []
    for index in range(min(diagonal.rows, diagonal.cols)):
        value = abs(int(diagonal[index, index]))
        if value:
            invariants.append(value)
    return invariants


def vector(matrix: Matrix) -> list[int]:
    assert matrix.cols == 1
    return [int(matrix[index, 0]) for index in range(matrix.rows)]


parity = load_json(PARITY_PATH)
cousin = load_json(COUSIN_PATH)

assert parity["schema"] == (
    "marici.benincasa.rank12_e6_parity_occurrence_composition.v1"
)
assert cousin["schema"] == (
    "marici.benincasa.rank12_e6_integral_cousin_comparison.v1"
)

occurrence_order = [
    "12|23",
    "12|31",
    "23|31",
    "23|12",
    "31|12",
    "31|23",
]
assert parity["occurrence_order"] == occurrence_order

forgetting = Matrix(parity["occurrence_forgetting_matrix"])
sheet_parity = Matrix(parity["sheet_parity_matrix"])
composite = Matrix(parity["composite_matrix"])
assert forgetting.shape == (3, 6)
assert sheet_parity.shape == (6, 6)
assert composite == forgetting * sheet_parity

resolved = Matrix(cousin["occurrence_resolved_betti_boundary"])
forgotten = Matrix(cousin["occurrence_forgotten_boundary"])
quarter_enlarged = Matrix(cousin["quarter_enlarged_e6_boundary"])
primitive_forgotten_target = Matrix([1, 1, 1])

assert resolved.shape == (6, 1)
assert forgotten.shape == (3, 1)
assert quarter_enlarged.shape == (6, 1)
assert forgetting * resolved == forgotten
assert quarter_enlarged == 4 * resolved

resolved_smith = smith_nonzero(resolved)
forgotten_smith = smith_nonzero(forgotten)
quarter_smith = smith_nonzero(quarter_enlarged)
assert resolved_smith == [1]
assert forgotten_smith == [2]
assert quarter_smith == [4]

# Deliberate failure of the naive claim that the torsion readout is intrinsic
# to the unresolved Carrier and survives forgetting/normalization unchanged.
naive_torsion_invariance = (
    resolved_smith == forgotten_smith == quarter_smith
)
torsion_order_residual = Matrix(
    [forgotten_smith[0] - resolved_smith[0],
     quarter_smith[0] - resolved_smith[0]]
)
assert naive_torsion_invariance is False
assert torsion_order_residual != Matrix.zeros(2, 1)

# The typed forgetting map commutes with the boundary, but it sends the
# resolved primitive generator to twice the primitive target generator.
primitive_forgetting_residual = (
    forgetting * resolved - primitive_forgotten_target
)
assert primitive_forgetting_residual == Matrix([1, 1, 1])
assert primitive_forgetting_residual != Matrix.zeros(3, 1)

source_invariant = Matrix(parity["invariant_source_generator"])
target_invariant = Matrix(parity["invariant_target_generator"])
assert composite * source_invariant == -4 * target_invariant

packet = {
    "schema": (
        "marici.grothendieck."
        "arithmetic_lens_resolution_falsifier.v1"
    ),
    "demonstrated_strength": [
        "source-typed morphism",
        "physical/readout",
    ],
    "compatibility_preflight": {
        "coefficient_domain": "Z",
        "coefficient_prime": None,
        "ambient_complex_degree": "0_to_1",
        "source_column_convention": "one primitive degree-zero generator",
        "resolved_target_row_count": 6,
        "resolved_target_row_order": occurrence_order,
        "forgotten_target_row_count": 3,
        "forgotten_target_row_order": ["12", "23", "31"],
        "filtration_stage": (
            "first-Rees e6 coefficient comparison against primitive Betti"
        ),
        "pole_depths": "not_applicable",
        "input_schemas": [parity["schema"], cousin["schema"]],
        "input_sha256": {
            str(PARITY_PATH.relative_to(ROOT)).replace("\\", "/"): sha256(
                PARITY_PATH
            ),
            str(COUSIN_PATH.relative_to(ROOT)).replace("\\", "/"): sha256(
                COUSIN_PATH
            ),
        },
    },
    "maps": {
        "occurrence_forgetting_shape": list(forgetting.shape),
        "sheet_parity_shape": list(sheet_parity.shape),
        "typed_composite_verified": True,
        "invariant_line_map": -4,
    },
    "smith_invariants": {
        "occurrence_resolved_primitive_betti": resolved_smith,
        "occurrence_forgotten": forgotten_smith,
        "quarter_enlarged_coefficient_lens": quarter_smith,
    },
    "cokernel_torsion": {
        "occurrence_resolved_primitive_betti": "trivial",
        "occurrence_forgotten": "Z/2",
        "quarter_enlarged_coefficient_lens": "Z/4",
    },
    "deliberate_failure": {
        "naive_claim": (
            "cokernel torsion is Carrier-intrinsic and invariant under "
            "occurrence forgetting and coefficient-lattice normalization"
        ),
        "claim_holds": naive_torsion_invariance,
        "torsion_order_residual": vector(torsion_order_residual),
        "primitive_forgetting_residual": vector(
            primitive_forgetting_residual
        ),
        "predicted_nonzero_obstruction_exhibited": True,
    },
    "verdict": {
        "untyped_carrier_intrinsic_torsion_readout_falsified": True,
        "typed_weak_carrier_calculus_falsified": False,
        "arithmetic_derived": False,
        "new_carrier_datum": False,
    },
    "not_proved": [
        "Carrier-only semiring",
        "identification with N or Z",
        "Spec(Z)",
        "prime recovery",
        "Frobenius",
        "Euler product",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
