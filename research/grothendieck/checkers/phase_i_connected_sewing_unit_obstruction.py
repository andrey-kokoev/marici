"""Exact arity obstruction to a Carrier unit for edge sewing."""

from __future__ import annotations

import contextlib
import hashlib
import importlib
import io
import json
import sys
from pathlib import Path

from sympy import Eq, Symbol, solve


ROOT = Path(__file__).resolve().parents[3]
VOEVODSKY = ROOT / "research/voevodsky"
ENTRY_27 = (
    ROOT
    / "src/ledger/20260813-27 Regional Core-Filtered Scalar-QTDS Theorem.md"
)
ENTRY_436 = (
    ROOT
    / "src/ledger/20260817-436 The Physical Derived Pullback Is One "
    "Primitive Integral Line.md"
)
ENTRY_628 = (
    ROOT
    / "src/ledger/20260817-628 The First Eight-Point Cut Boundary Is Forced.md"
)
ENTRY_537 = (
    ROOT
    / "src/ledger/20260818-537 The Eight-Point Framed Physical Line Is Rigid.md"
)
ENTRY_540 = (
    ROOT
    / "src/ledger/20260818-540 The Framed Decagon Cut Gluing Space Is "
    "Contractible.md"
)
ENTRY_541 = (
    ROOT
    / "src/ledger/20260818-541 The Dodecagon Passes the First Four-Cut "
    "Induction Gate.md"
)
ENTRY_542 = (
    ROOT
    / "src/ledger/20260818-542 Even-Arity Framed Cut Descent Follows by "
    "Quadrangulation Induction.md"
)
SOURCE_CHECKERS = [
    VOEVODSKY / "check_n8_framed_physical_line_rigidity.py",
    VOEVODSKY / "check_n10_framed_cut_gluing_rigidity.py",
    VOEVODSKY / "check_n12_physical_cut_induction_gate.py",
    VOEVODSKY / "check_general_even_cut_induction.py",
]
OUT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-connected-sewing-unit-obstruction.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def boundary_pushout_cardinality(left: int, right: int) -> int:
    """Cardinality of two tagged boundaries glued along one two-endpoint edge."""

    elements = [*(('L', i) for i in range(left)), *(('R', i) for i in range(right))]
    parent = {element: element for element in elements}

    def find(element: tuple[str, int]) -> tuple[str, int]:
        while parent[element] != element:
            parent[element] = parent[parent[element]]
            element = parent[element]
        return element

    def union(first: tuple[str, int], second: tuple[str, int]) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root != second_root:
            parent[second_root] = first_root

    union(("L", 0), ("R", 0))
    union(("L", 1), ("R", 1))
    return len({find(element) for element in elements})


ledger_inputs = [
    ENTRY_27,
    ENTRY_436,
    ENTRY_628,
    ENTRY_537,
    ENTRY_540,
    ENTRY_541,
    ENTRY_542,
]
inputs = ledger_inputs + SOURCE_CHECKERS
for path in inputs:
    assert path.is_file()

# Re-run the exact positive controls.  Their output is suppressed so this
# checker emits one machine-readable JSON object.
sys.path.insert(0, str(VOEVODSKY))
source_checker_controls: dict[str, bool] = {}
for checker_path in SOURCE_CHECKERS:
    module = importlib.import_module(checker_path.stem)
    with contextlib.redirect_stdout(io.StringIO()):
        module.main()
    source_checker_controls[rel(checker_path)] = True

# These profiles occur in the exact n=8, n=10, and n=12 Cut audits.  The
# pushout computation uses tagged boundary sites and identifies only the two
# endpoints of the sewn edge.
profiles = (
    (4, 4, 6, "first connected quadrilateral sewing"),
    (6, 4, 8, "six-by-four octagon boundary"),
    (4, 8, 10, "four-by-eight decagon Cut"),
    (6, 6, 10, "six-by-six decagon Cut"),
    (4, 10, 12, "four-by-ten dodecagon Cut"),
    (6, 8, 12, "six-by-eight dodecagon Cut"),
)
profile_results = []
for left, right, expected, source in profiles:
    observed = boundary_pushout_cardinality(left, right)
    assert observed == expected
    profile_results.append(
        {
            "left_arity": left,
            "right_arity": right,
            "expected_output_arity": expected,
            "observed_output_arity": observed,
            "source_profile": source,
        }
    )

# Solve the unit law for the sewing arity operation.  A unit must consist only
# of the two endpoints of the interface edge.  The admitted stable even
# polygon family begins at arity four.
arity = Symbol("n", integer=True, positive=True)
unit_arity = Symbol("e", integer=True, positive=True)
unit_solutions = solve(Eq(arity + unit_arity - 2, arity), unit_arity)
assert unit_solutions == [2]
admitted_minimum_arity = 4
required_unit_arity = int(unit_solutions[0])
interface_only_unit_admitted = required_unit_arity >= admitted_minimum_arity
assert interface_only_unit_admitted is False

four_point_residuals = {
    str(test_arity): boundary_pushout_cardinality(test_arity, 4) - test_arity
    for test_arity in (4, 6, 8, 10, 12, 14)
}
assert set(four_point_residuals.values()) == {2}

# Removing the two interface endpoints exposes the intrinsic additive law.
assert all(
    expected - 2 == (left - 2) + (right - 2)
    for left, right, expected, _ in profiles
)

# Deliberate failure: the primitive +1 in the four-point coefficient line is
# not an object-level unit for connected edge sewing.
naive_four_point_carrier_unit_claim = all(
    residual == 0 for residual in four_point_residuals.values()
)
assert naive_four_point_carrier_unit_claim is False

packet = {
    "schema": (
        "marici.grothendieck.phase_i_connected_sewing_unit_obstruction.v1"
    ),
    "demonstrated_strength": [
        "unbounded boundary-pushout theorem",
        "exact all-even framed positive control",
    ],
    "compatibility_preflight": {
        "coefficient_domain": None,
        "coefficient_prime": None,
        "ambient_carrier": "stable even marked polygons",
        "interface": "one boundary edge with two endpoints",
        "source_operation": "connected edge sewing / Cut factorization",
        "filtration_stage": "Carrier arity before framed coefficient readout",
        "input_sha256": {rel(path): sha256(path) for path in inputs},
    },
    "positive_coefficient_control": {
        "source_checker_reruns": source_checker_controls,
        "framed_cut_descent_scope": "cellular fs/Kato sector",
        "verified_statement": (
            "primitive four-point coefficient lines external-product "
            "coherently on every even-arity Cut stratum"
        ),
        "carrier_unit_claimed_by_control": False,
    },
    "boundary_pushout": {
        "operation": "B_left pushout_over_interface_edge B_right",
        "interface_endpoint_count": 2,
        "arity_law": "left + right - 2",
        "profiles": profile_results,
        "excess_arity": "arity - 2",
        "excess_law": (
            "excess(output) = excess(left) + excess(right)"
        ),
    },
    "unit_test": {
        "unit_equation": "n + e - 2 = n",
        "unique_unit_arity_solution": required_unit_arity,
        "admitted_stable_minimum_arity": admitted_minimum_arity,
        "interface_only_unit_admitted": interface_only_unit_admitted,
        "four_point_candidate_residuals": four_point_residuals,
        "four_point_is_carrier_unit": naive_four_point_carrier_unit_claim,
    },
    "type_separation": {
        "coefficient_primitive_unit": (
            "chosen +1 generator in an oriented rank-one framed line"
        ),
        "carrier_tensor_unit": (
            "object E with natural isomorphisms X sew E isomorphic to X"
        ),
        "observed_external_product_target": (
            "a higher-arity Cut boundary, not the original Carrier object"
        ),
        "types_coincide": False,
    },
    "deliberate_failure": {
        "naive_claim": (
            "the primitive four-point coefficient unit is the unit object "
            "for connected Carrier sewing"
        ),
        "claim_holds": naive_four_point_carrier_unit_claim,
        "required_arity_residual": 0,
        "observed_arity_residual": 2,
        "nonzero_obstruction": {"four_point_unit_arity_residual": 2},
    },
    "verdict": {
        "framed_coefficient_unit_verified": True,
        "framed_external_product_coherent_all_even_arities": True,
        "four_point_carrier_tensor_unit": False,
        "interface_only_two_point_unit_admitted": False,
        "connected_sewing_unital_on_admitted_carriers": False,
        "connected_sewing_is_intrinsic_multiplication": False,
        "initial_semiring_derived": False,
        "arithmetic_sector_derived": False,
    },
    "scope_boundary": {
        "adjoining_unstable_two_point_object_contradicted": False,
        "different_carrier_tensor_contradicted": False,
        "coefficient_external_product_contradicted": False,
        "precise_missing_datum": (
            "an admitted Carrier unit object and total source-equivariant "
            "product distinct from the framed coefficient-line unit"
        ),
    },
    "deferred": [
        "admission and geometry of an interface-only object",
        "different total Carrier tensor",
        "distributivity over geometric disjoint union",
        "initial semiring multiplication",
        "intrinsic irreducibility and primes",
        "Burnside/Witt operations",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
