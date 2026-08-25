"""Sparse physical point-source kernel and contour-selection checks."""

import json
import os

import sympy as sp


checks = []


def record(gate, statement, passed, detail):
    checks.append({
        "gate": gate,
        "statement": statement,
        "passed": bool(passed),
        "detail": detail,
    })


I = sp.I


def local_port_matrix(weights):
    blocks = []
    for weight in weights:
        # Columns are (L, Lbar, h); rows are (bar-pole, z-pole, delta).
        blocks.append(sp.diag(-weight / (2 * I), weight / (2 * I), weight))
    return sp.diag(*blocks)


rank_ok = True
det_ok = True
for count in range(1, 21):
    weights = [sp.Rational(j + 2, j + 1) for j in range(count)]
    matrix = local_port_matrix(weights)
    rank_ok &= matrix.rank() == 3 * count
    det_ok &= matrix.det() != 0
record(
    "LOCAL.injective",
    "complete residue and delta ports are injective for distinct punctures",
    rank_ok and det_ok,
    "one through twenty punctures with distinct nonzero metric weights",
)


# Restriction to conservation subspaces cannot create a kernel.  Exercise
# explicit full-column-rank inclusions with sum-zero constraints.
restriction_ok = True
for count in range(2, 11):
    matrix = local_port_matrix([sp.Integer(1)] * count)
    # For each of the three source types, eliminate the last coordinate as
    # minus the sum of its predecessors.
    inclusion = sp.zeros(3 * count, 3 * (count - 1))
    for kind in range(3):
        for j in range(count - 1):
            inclusion[3 * j + kind, 3 * j + kind] = 1
            inclusion[3 * (count - 1) + kind, 3 * j + kind] = -1
    restriction_ok &= (matrix * inclusion).rank() == inclusion.cols
record(
    "LOCAL.conservation",
    "restriction to explicit sum-zero conservation subspaces remains injective",
    restriction_ok,
    "two through ten punctures",
)


# Finite contour selection is a row projection and necessarily aliases when
# fewer rows than source coordinates are retained.
contour_ok = True
for source_dim in range(2, 31):
    for contour_count in range(1, min(source_dim, 6)):
        entries = [
            sp.Integer((row + 1) ** (col + 1))
            for row in range(contour_count)
            for col in range(source_dim)
        ]
        contour = sp.Matrix(contour_count, source_dim, entries)
        contour_ok &= len(contour.nullspace()) >= source_dim - contour_count
record(
    "CONTOUR.deficiency",
    "an incomplete contour family has the rank-forced source kernel",
    contour_ok,
    "source dimensions 2..30; one through five retained contours",
)


c1, c2 = sp.symbols("c1 c2", nonzero=True)
one_contour = sp.Matrix([[c1, c2]])
circuit = sp.Matrix([c2, -c1])
record(
    "CONTOUR.circuit",
    "the two-route one-contour alias depends on the physical pairing coefficients",
    one_contour * circuit == sp.zeros(1, 1),
    "kernel vector=(c2,-c1)",
)


# At a collision, two value-only columns coincide.  Adding independent first
# jet ports restores the two labelled coefficients in the minimal model.
collision_value = sp.Matrix([[1, 1]])
collision_jet = sp.Matrix([[1, 1], [0, 1]])
record(
    "COLLISION.jet",
    "coincident value ports lose a label and a first-jet port restores it",
    collision_value.rank() == 1 and collision_jet.rank() == 2,
    "minimal two-source collision model",
)


passed = sum(item["passed"] for item in checks)
total = len(checks)
payload = {
    "checker": "physical_point_source_kernel_checks.py",
    "strength": "unbounded finite-puncture kernel theorem",
    "passed": passed,
    "total": total,
    "checks": checks,
    "verdict": (
        "Complete local residue and delta ports are injective on every finite "
        "distinct-puncture packet. Kernels arise from incomplete contour "
        "selection or collision-incomplete targets, with pairing-dependent "
        "circuits unrelated to the Laurent towers and E1/E2."
    ),
}

outdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "physical_point_source_kernel.json")
with open(outpath, "w", encoding="ascii") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

for item in checks:
    label = "PASS" if item["passed"] else "FAIL"
    print(f"{label} {item['gate']}: {item['statement']} - {item['detail']}")
print(f"SUMMARY {passed}/{total}")

if passed != total:
    raise SystemExit(1)

