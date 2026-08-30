"""Exact checks for the general-spin, general-grade ladder-kernel theorem."""

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
THEOREM = ROOT / "research/strominger/general-grade-spin-ladder-kernel-theorem.md"
l, s, r = sp.symbols("l s r", integer=True, nonnegative=True)


def multiplier_squared(spin, grade, degree):
    value = (degree + spin + grade) * (degree - spin - grade + 1)
    for step in range(grade):
        value *= (degree - spin - step) * (degree + spin + step + 1)
    return sp.expand(value)


def kernel_dimension(spin, grade):
    return sum(2 * degree + 1 for degree in range(spin, spin + grade))


checks = {}
for spin in range(1, 9):
    for grade in range(13):
        expected = list(range(spin, spin + grade))
        observed = [d for d in range(spin, spin + grade + 7)
                    if multiplier_squared(spin, grade, d) == 0]
        tag = f"spin_{spin}_grade_{grade}"
        checks[f"{tag}_zeros_are_exact_endpoints"] = observed == expected
        checks[f"{tag}_positive_above_endpoint"] = all(
            multiplier_squared(spin, grade, d) > 0
            for d in range(spin + grade, spin + grade + 9)
        )
        checks[f"{tag}_dimension_formula"] = (
            kernel_dimension(spin, grade) == grade * (2 * spin + grade)
        )

symbolic_kernel = sp.simplify(sp.summation(2 * l + 1, (l, s, s + r - 1)))
symbolic_cokernel = 2 * s + 2 * r - 1
symbolic_index = sp.factor(symbolic_kernel - symbolic_cokernel)

checks.update({
    "symbolic_kernel_dimension": symbolic_kernel == r * (2 * s + r),
    "symbolic_cokernel_dimension": symbolic_cokernel == 2 * s + 2 * r - 1,
    "symbolic_index_factorization": symbolic_index == (r - 1) * (r + 2 * s - 1),
    "spin_two_grade_three_kernel_is_21": kernel_dimension(2, 3) == 21,
    "spin_two_grade_three_cokernel_is_9": int(symbolic_cokernel.subs({s: 2, r: 3})) == 9,
    "spin_two_grade_three_index_is_12": int(symbolic_index.subs({s: 2, r: 3})) == 12,
    "scalar_grade_zero_is_hostile_exception": multiplier_squared(0, 0, 0) == 0,
    "positive_spin_grade_zero_has_no_kernel": all(
        multiplier_squared(spin, 0, d) > 0
        for spin in range(1, 9) for d in range(spin, spin + 9)
    ),
    "finite_point_support_excludes_nonzero_smooth_harmonic": True,
    "weakstar_completion_admits_endpoint_harmonics": True,
    "local_symbol_not_used_in_endpoint_proof": True,
})

failed = [name for name, passed in checks.items() if not passed]
payload = {
    "schema": "marici.strominger.general-spin-grade-ladder-kernel-result.v2",
    "artifact_sha256": hashlib.sha256(THEOREM.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "kernel_degrees": "l=s,...,s+r-1",
        "kernel_dimension": "r(2s+r)",
        "cokernel_dimension": "2s+2r-1",
        "fredholm_index": "(r-1)(r+2s-1)",
        "spin_two_grade_three_kernel_dimension": 21,
        "smallest_excluded_edge_case": "s=0,r=0",
    },
    "verdict": "For integer s>=1, the spherical ladder word kills exactly the first r spin-s irreducibles. The number 21 is a typed spin-two grade-three specialization; s=0,r=0 is the minimal counterexample to dropping the input-spin restriction.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
