"""Integral Smith law for the global tower-residue augmentation."""
import itertools
import json
import math
import os
import sympy as sp

checks = []


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


def residue(grade, depth):
    return -int(grade * (grade + 1) * sp.catalan(grade + 1) *
                sp.rf(depth, grade - 1))


def extended_gcd(left, right):
    """Return x,y,d with x*left+y*right=d=gcd(|left|,|right|)."""
    def nonnegative(a, b):
        if b == 0:
            return 1, 0, a
        x1, y1, divisor = nonnegative(b, a % b)
        return y1, x1 - (a // b) * y1, divisor

    x, y, divisor = nonnegative(abs(left), abs(right))
    return x * (-1 if left < 0 else 1), y * (-1 if right < 0 else 1), divisor


def smith_kernel_basis(values):
    """Unimodular U with row(values)*U=(gcd,0,...,0)."""
    size = len(values)
    row = sp.Matrix([values])
    transform = sp.eye(size)
    if values[0] < 0:
        transform[0, 0] = -1
    for index in range(1, size):
        current = row * transform
        left = int(current[0, 0])
        right = int(current[0, index])
        x, y, divisor = extended_gcd(left, right)
        block = sp.eye(size)
        block[0, 0] = x
        block[0, index] = -right // divisor
        block[index, 0] = y
        block[index, index] = left // divisor
        transform = transform * block
    return transform, abs(int((row * transform)[0, 0]))


depths = (2, 4, 6, 8, 10, 12)
fail_rank = []
fail_kernel = []
fail_growth = []
fail_basis = []
cases = 0
for grade in range(2, 9):
    for size in range(1, len(depths) + 1):
        for admitted in itertools.combinations(depths, size):
            cases += 1
            values = [residue(grade, depth) for depth in admitted]
            row = sp.Matrix([values])
            divisor = math.gcd(*(abs(value) for value in values))
            if row.rank() != 1 or divisor == 0:
                fail_rank.append((grade, admitted))
            transform, smith_divisor = smith_kernel_basis(values)
            reduced = row * transform
            kernel_basis = transform[:, 1:]
            if (abs(int(transform.det())) != 1 or smith_divisor != divisor or
                    reduced != sp.Matrix([[divisor] + [0] * (len(values) - 1)]) or
                    (len(values) > 1 and row * kernel_basis != sp.zeros(1, len(values) - 1))):
                fail_basis.append((grade, admitted, reduced, transform.det()))
            if len(values) > 1:
                reference = values[0]
                for index, value in enumerate(values[1:], start=1):
                    pair_gcd = math.gcd(abs(reference), abs(value))
                    circuit = sp.zeros(len(values), 1)
                    circuit[0] = value // pair_gcd
                    circuit[index] = -reference // pair_gcd
                    nonzero = [abs(int(entry)) for entry in circuit if entry]
                    if row * circuit != sp.zeros(1, 1) or math.gcd(*nonzero) != 1:
                        fail_kernel.append((grade, admitted, index))
            running = abs(values[0])
            for value in values[1:]:
                updated = math.gcd(running, abs(value))
                if running % updated != 0:
                    fail_growth.append((grade, admitted, running, updated))
                running = updated
            if running != divisor:
                fail_growth.append((grade, admitted, running, divisor))

record("SMITH.rank", "every nonempty augmentation has rational rank one",
       not fail_rank, f"cases={cases}; failures={fail_rank}")
record("SMITH.circuit", "pairwise residue relations have primitive integral coordinates",
       not fail_kernel, fail_kernel)
record("SMITH.growth", "adding depths updates the index only by gcd refinement",
       not fail_growth, fail_growth)
record("SMITH.basis", "Bezout reduction gives a saturated integral kernel basis for every audited row",
       not fail_basis, fail_basis[:1])

# Small explicit witness: grade two depths 2 and 4 have residues -60,-120,
# so the primitive exact relation is 2*D_2-D_4 up to sign.
row = sp.Matrix([[residue(2, 2), residue(2, 4)]])
witness = sp.Matrix([2, -1])
record("WITNESS.g2", "the first cross-depth residue circuit is primitive (2,-1)",
       row * witness == sp.zeros(1, 1))

# Pairwise primitive circuits need not saturate a multi-depth kernel.
row = sp.Matrix([[20, 42, 72]])
pairwise = sp.Matrix([[21, 18], [-10, 0], [0, -5]])
missing = sp.Matrix([-12, 4, 1])
pairwise_minors = []
for selected in itertools.combinations(range(3), 2):
    pairwise_minors.append(abs(int(pairwise[list(selected), :].det())))
record("PAIRWISE.falsifier", "reference-pair circuits can miss the saturated kernel by index five",
       row * pairwise == sp.zeros(1, 2) and row * missing == sp.zeros(1, 1) and
       math.gcd(*pairwise_minors) == 5 and missing[2] % 5 != 0)


def valuation_two(value):
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


# Stable fixed divisor of rising products on the positive even constructor.
failures = []
stable_rows = []
for length in range(1, 21):
    # A degree-length integer-valued polynomial has its fixed divisor detected
    # by any length+1 consecutive constructor inputs; audit a much wider range.
    values = [int(sp.rf(2 * index, length)) for index in range(1, 8 * length + 9)]
    observed = math.gcd(*values)
    expected = math.factorial(length)
    if length % 2 == 1:
        expected *= 2 ** valuation_two(length + 1)
    stable_rows.append((length, observed))
    if observed != expected:
        failures.append((length, observed, expected))
record("STABLE.fixed_divisor", "the even-start rising-product fixed divisor has only the predicted 2-adic correction",
       not failures, failures)

failures = []
for grade in range(2, 21):
    length = grade - 1
    delta = math.factorial(length)
    if grade % 2 == 0:
        delta *= 2 ** valuation_two(grade)
    expected = int(grade * (grade + 1) * sp.catalan(grade + 1)) * delta
    observed = math.gcd(*(abs(residue(grade, depth))
                          for depth in range(2, 16 * grade + 2, 2)))
    if observed != expected:
        failures.append((grade, observed, expected))
record("STABLE.residue", "the stable residue index is Catalan transport times the constructor fixed divisor",
       not failures, failures)

failures = []
for grade in range(2, 21):
    length = grade - 1
    finite_even = math.gcd(*(int(sp.rf(2 * index, length))
                             for index in range(1, grade + 1)))
    wide_even = math.gcd(*(int(sp.rf(2 * index, length))
                           for index in range(1, 20 * grade + 1)))
    all_integer = math.gcd(*(int(sp.rf(index, length))
                             for index in range(1, 20 * grade + 1)))
    ratio = finite_even // all_integer
    expected_ratio = 2 ** valuation_two(grade) if grade % 2 == 0 else 1
    if finite_even != wide_even or all_integer != math.factorial(length) or ratio != expected_ratio:
        failures.append((grade, finite_even, wide_even, all_integer, ratio, expected_ratio))
record("STABLE.constructor", "depths through 2g stabilize the index and isolate the even-constructor 2-adic memory",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_residue_augmentation_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "The positive tower family maps by one weighted residue augmentation. Every nonempty family has rational rank one. Its integral image index is the gcd of the Catalan residue characters; adding depths refines this index by gcd. Sequential Bezout reduction supplies a saturated integral kernel basis. Pairwise circuits remain valid but can span a proper sublattice, with an explicit index-five falsifier at grade three depths 4,6,8.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_residue_augmentation.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
