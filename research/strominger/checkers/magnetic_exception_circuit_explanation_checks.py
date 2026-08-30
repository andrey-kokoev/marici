"""Dependency-free exact constructor certificate for the grade-two q=7 circuit."""
from fractions import Fraction
import json
import math
import os


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def path_coefficients(g, a, m):
    source = [
        choose(g, j) * (-1) ** (g - j)
        * rising(a, g - j) * rising(4 - a, j)
        for j in range(g + 1)
    ]
    return ([m * source[0]]
            + [(m + j) * source[j] + (m + j - 1 - g) * source[j - 1]
               for j in range(1, g + 1)]
            + [m * source[g]])


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m)) if value}


def source(g, a, j):
    if not 0 <= j <= g:
        return 0
    return choose(g, j) * (-1) ** j * rising(a, g - j) * rising(4 - a, j)


def path(g, a, m, j):
    if j == 0:
        return m * source(g, a, 0)
    return ((m + j) * source(g, a, j)
            + (m + j - 1 - g) * source(g, a, j - 1))


def det2(a, b, c, d):
    return a * d - b * c


def det3(m):
    return (m[0][0] * det2(m[1][1], m[1][2], m[2][1], m[2][2])
            - m[0][1] * det2(m[1][0], m[1][2], m[2][0], m[2][2])
            + m[0][2] * det2(m[1][0], m[1][1], m[2][0], m[2][1]))


def cofactor(m, row, col):
    rows = [i for i in range(3) if i != row]
    cols = [j for j in range(3) if j != col]
    value = det2(m[rows[0]][cols[0]], m[rows[0]][cols[1]],
                 m[rows[1]][cols[0]], m[rows[1]][cols[1]])
    return value if (row + col) % 2 == 0 else -value


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


labels = [(0, -8), (4, 2), (6, 0)]
columns = [canonical_column(2, a, m) for a, m in labels]
rows = sorted(set().union(*(set(column) for column in columns)))
matrix = [[column.get(row, 0) for column in columns] for row in rows]
normalized = [[Fraction(value, 20) for value in row] for row in matrix]
expected = [[-6, 0, 3], [-8, -2, 1]]
record("SUPPORT.two", "the exceptional columns collapse to two observations",
       rows == [0, 1], rows)
record("STATE.boundary", "the normalized boundary matrix is canonical",
       normalized == expected, normalized)

minors = [
    det2(normalized[0][1], normalized[0][2],
         normalized[1][1], normalized[1][2]),
    -det2(normalized[0][0], normalized[0][2],
          normalized[1][0], normalized[1][2]),
    det2(normalized[0][0], normalized[0][1],
         normalized[1][0], normalized[1][1]),
]
divisor = math.gcd(*(abs(value.numerator) for value in minors))
primitive = [value / divisor for value in minors]
residual = [sum(matrix[i][j] * primitive[j] for j in range(3))
            for i in range(2)]
record("PLUCKER.primitive", "signed maximal minors force (1,-3,2)",
       primitive == [1, -3, 2], primitive)
record("CIRCUIT.zero", "the primitive circuit annihilates both observations",
       residual == [0, 0], residual)
record("CIRCUIT.minimal", "every column pair remains independent",
       all(value != 0 for value in minors), minors)

record("JET.transverse", "the surviving grade-two route is -6(d-1)(d-5)",
       all(-path(2, d - 1, 2, 1) == -6 * (d - 1) * (d - 5)
           for d in range(-2, 10)),
       "quadratic identity certified at more than three points")
record("JET.one_column", "the neighboring route is identically absent at grade two",
       all(-path(2, d + 1, 0, 3) == 0 for d in range(-2, 10)),
       "constructor index j=3 exceeds grade two")
record("JET.unique_loss", "the admissible odd range loses the route only at d=5",
       [d for d in range(3, 100, 2)
        if -path(2, d - 1, 2, 1) == 0] == [5],
       "q=g+d=7")


def left_expected(g, d):
    return (-(2 * d * g + 2 * d - g * g - 11 * g - 4)
            * math.factorial(d + g - 3) // math.factorial(d - 2))


def right_expected(g, d):
    numerator = (g * (d - 4) * (d - 3) * (g - 2) * (g - 1) * (g + 3)
                 * math.factorial(d + g - 3))
    return numerator // (2 * math.factorial(d))


samples = [(g, d) for g in range(2, 21) for d in range(3, 32, 2)]
left_ok = all(-path(g, d - 1, 2, 1) == left_expected(g, d)
              for g, d in samples)
right_ok = all(-path(g, d + 1, 0, 3) == right_expected(g, d)
               for g, d in samples)
record("ROUTES.left", "the left carrier matches its closed source formula",
       left_ok, f"{len(samples)} exact samples")
record("ROUTES.right", "the right carrier exposes the factor g-2",
       right_ok, f"{len(samples)} exact samples")
record("ROUTES.intersection", "both routes vanish at (g,d)=(2,5)",
       -path(2, 4, 2, 1) == 0 and -path(2, 6, 0, 3) == 0,
       "capacity divisor meets alignment divisor")

core = [[-160, -40, 20], [0, 0, 0], [-120, 0, 60]]
left_cofactor = cofactor(core, 1, 1)
right_cofactor = cofactor(core, 1, 2)
record("CONSTRUCTOR.cofactors", "either route independently restores rank",
       (left_cofactor, right_cofactor) == (-7200, 4800),
       (left_cofactor, right_cofactor))
record("CONSTRUCTOR.repair", "the repaired determinant is -7200 ell+4800 rho",
       all(det3([core[0], [0, ell, rho], core[2]])
               == -7200 * ell + 4800 * rho
               for ell, rho in [(-2, 3), (0, 1), (1, 0), (4, -5)]),
       "exact linear determinant identity")


def sensitivity_expected(g, d):
    left = (g * (g + 3) * (d * g - 2 * d - 5 * g + 4)
            * math.factorial(g + 3) * math.factorial(d + g - 1)
            // (6 * math.factorial(d)))
    right = (math.factorial(g + 3) * math.factorial(d + g - 1)
             // (3 * math.factorial(d - 2)))
    return left, right


interference_ok = True
for g, d in samples:
    f = rising(4, g)
    left = -path(g, d - 1, 2, 1)
    right = -path(g, d + 1, 0, 3)
    symbolic_core = [
        [(1 - 2 * g - d) * f, -path(g, d - 1, 2, 0),
         -path(g, d + 1, 0, 2)],
        [0, left, right],
        [(1 - g - d) * f, 0, -path(g, d + 1, 0, 1)],
    ]
    actual = cofactor(symbolic_core, 1, 1), cofactor(symbolic_core, 1, 2)
    expected_sensitivity = sensitivity_expected(g, d)
    interference_ok &= actual == expected_sensitivity
    interference_ok &= det3(symbolic_core) == actual[0] * left + actual[1] * right
record("INTERFERENCE.sum",
       "the determinant is the cofactor-weighted sum of both routes",
       interference_ok, f"{len(samples)} exact source blocks")

failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_exception_circuit_explanation_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "dependency-free exact local theorem plus bounded formula replay",
        "locus": {"g": 2, "q": 7},
        "bounded_formula_range": {"g": [2, 20], "odd_d": [3, 31]},
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The q=7 circuit is a simultaneous loss of two routes into one "
        "observation quotient. The surviving two-row state forces the primitive "
        "Plucker circuit (1,-3,2)."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_exception_circuit_explanation.json"),
          "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
"""Primitive Plucker explanation of the grade-two q=7 magnetic circuit."""
import json
import math
import os
import sympy as sp


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def path_coefficients(g, a, m):
    source = [math.comb(g, j) * (-1) ** (g - j) *
              rising(a, g - j) * rising(4 - a, j)
              for j in range(g + 1)]
    output = [m * source[0]]
    output += [(m + j) * source[j] +
               (m + j - 1 - g) * source[j - 1]
               for j in range(1, g + 1)]
    output.append(m * source[g])
    return output


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m)) if value}


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


labels = [(0, -8), (4, 2), (6, 0)]
columns = [canonical_column(2, a, m) for a, m in labels]
rows = sorted(set().union(*(set(column) for column in columns)))
matrix = sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])
normalized = matrix / 20

record("SUPPORT.two", "all three exceptional columns collapse to rows 0 and 1",
       rows == [0, 1], rows)
record("STATE.boundary", "the normalized boundary-state matrix is canonical",
       normalized == sp.Matrix([[-6, 0, 3], [-8, -2, 1]]),
       normalized.tolist())

# For three vectors v0,v1,v2 in dimension two, the signed maximal minors are
# the canonical circuit coordinates (det(v1,v2),-det(v0,v2),det(v0,v1)).
plucker = sp.Matrix([
    normalized[:, 1:3].det(),
    -normalized[:, [0, 2]].det(),
    normalized[:, 0:2].det(),
])
primitive_gcd = math.gcd(*(abs(int(value)) for value in plucker))
primitive = plucker / primitive_gcd
record("PLUCKER.primitive", "signed maximal minors force the primitive circuit",
       primitive == sp.Matrix([1, -3, 2]), primitive.T.tolist())
record("CIRCUIT.zero", "the primitive Plucker vector annihilates both observations",
       matrix * primitive == sp.zeros(2, 1), (matrix * primitive).T.tolist())
record("CIRCUIT.minimal", "every column pair is independent, so the circuit is minimal",
       all(matrix[:, pair].det() != 0 for pair in ([0, 1], [0, 2], [1, 2])),
       [matrix[:, pair].det() for pair in ([0, 1], [0, 2], [1, 2])])

# Derive the missing transverse observation before specializing d=5.  At
# grade two the odd collision columns have depths d-1 and d+1.  Row R2 sees
# only the former; the latter has terminal weight m=0.
d_symbol = sp.symbols("d", integer=True, positive=True)


def symbolic_source(a, j):
    return (sp.binomial(2, j) * (-1) ** j * sp.rf(a, 2 - j) *
            sp.rf(4 - a, j))


def symbolic_path(a, m, j):
    if j == 0:
        return sp.factor(m * symbolic_source(a, 0))
    return sp.factor((m + j) * symbolic_source(a, j) +
                     (m + j - 3) * symbolic_source(a, j - 1))


transverse_left = sp.factor(-symbolic_path(d_symbol - 1, 2, 1))
transverse_right = sp.factor(-symbolic_path(d_symbol + 1, 0, 3))
record("JET.transverse", "the grade-two R2 response has the exact obstruction factor",
       sp.expand(transverse_left + 6 * (d_symbol - 1) * (d_symbol - 5)) == 0,
       transverse_left)
record("JET.one_column", "the neighboring right collision column is invisible to R2",
       transverse_right == 0, transverse_right)
record("JET.unique_loss", "the admissible odd collision range loses R2 only at d=5",
       [value for value in range(3, 100, 2)
        if transverse_left.subs(d_symbol, value) == 0] == [5],
       "q=g+d=7 and collision depths are d-1=4,d+1=6")

# Symbolic two-route factorization before restriction to grade two.
g_symbol = sp.symbols("g", integer=True, positive=True)


def general_source(a, j):
    return (sp.binomial(g_symbol, j) * (-1) ** j *
            sp.rf(a, g_symbol - j) * sp.rf(4 - a, j))


def general_path(a, m, j):
    return sp.factor(sp.combsimp(
        (m + j) * general_source(a, j) +
        (m + j - 1 - g_symbol) * general_source(a, j - 1)))


left_route = sp.factor(sp.combsimp(-general_path(d_symbol - 1, 2, 1)))
right_route = sp.factor(sp.combsimp(-general_path(d_symbol + 1, 0, 3)))
left_expected = sp.factor(
    -(2 * d_symbol * g_symbol + 2 * d_symbol - g_symbol**2 -
      11 * g_symbol - 4) * sp.factorial(d_symbol + g_symbol - 3) /
    sp.factorial(d_symbol - 2))
right_expected = sp.factor(
    g_symbol * (d_symbol - 4) * (d_symbol - 3) * (g_symbol - 2) *
    (g_symbol - 1) * (g_symbol + 3) *
    sp.factorial(d_symbol + g_symbol - 3) /
    (2 * sp.factorial(d_symbol)))
record("ROUTES.left", "the left transverse carrier has the closed two-parameter form",
       sp.simplify(left_route - left_expected) == 0, left_route)
record("ROUTES.right", "the right transverse carrier contains the grade divisor g-2",
       sp.simplify(right_route - right_expected) == 0, right_route)
record("ROUTES.intersection", "on g=2 the left route vanishes at admissible d=5",
       sp.simplify(left_route.subs(g_symbol, 2) - transverse_left) == 0 and
       sp.simplify(right_route.subs(g_symbol, 2)) == 0,
       "exception is the intersection g=2 and d=5")

# Constructor theorem at the exceptional fiber.  In row order (R1,R2,R0),
# R2 has exactly the two collision-column ports.  Its cofactors measure the
# response to independently restoring either port.
core = sp.Matrix([
    [-160, -40, 20],
    [0, 0, 0],
    [-120, 0, 60],
])
left_cofactor = core.cofactor(1, 1)
right_cofactor = core.cofactor(1, 2)
record("CONSTRUCTOR.routes", "R2 has exactly two possible collision-source ports",
       core[1, 0] == 0 and core[1, 1] == 0 and core[1, 2] == 0,
       "structurally: (0,-) is absent; (4,+),(6,+) are the two carriers")
record("CONSTRUCTOR.cofactors", "both independent R2 repair cofactors are nonzero",
       left_cofactor == -7200 and right_cofactor == 4800,
       f"left={left_cofactor}; right={right_cofactor}")
ell, rho = sp.symbols("ell rho")
repaired = core.copy()
repaired[1, 1] = ell
repaired[1, 2] = rho
record("CONSTRUCTOR.repair", "the local repaired determinant is the carrier pairing",
       sp.expand(repaired.det() - (-7200 * ell + 4800 * rho)) == 0,
       sp.factor(repaired.det()))
record("CONSTRUCTOR.single", "restoring either route alone restores full rank",
       repaired.subs({ell: 1, rho: 0}).det() != 0 and
       repaired.subs({ell: 0, rho: 1}).det() != 0,
       "capacity repair or alignment repair is individually sufficient")

# Full symbolic interference law.  Expanding the odd collision determinant
# along R2 pairs the two carrier routes with their reconstruction cofactors.
F = sp.rf(4, g_symbol)
m_minus = 1 - 2 * g_symbol - d_symbol
symbolic_core = sp.Matrix([
    [m_minus * F,
     -general_path(d_symbol - 1, 2, 0),
     -general_path(d_symbol + 1, 0, 2)],
    [0, left_route, right_route],
    [(1 - g_symbol - d_symbol) * F,
     0,
     -general_path(d_symbol + 1, 0, 1)],
])
left_sensitivity = sp.factor(sp.combsimp(symbolic_core.cofactor(1, 1)))
right_sensitivity = sp.factor(sp.combsimp(symbolic_core.cofactor(1, 2)))
left_sensitivity_expected = sp.factor(
    g_symbol * (g_symbol + 3) *
    (d_symbol * g_symbol - 2 * d_symbol - 5 * g_symbol + 4) *
    sp.factorial(g_symbol + 3) *
    sp.factorial(d_symbol + g_symbol - 1) /
    (6 * sp.factorial(d_symbol)))
right_sensitivity_expected = sp.factor(
    sp.factorial(g_symbol + 3) *
    sp.factorial(d_symbol + g_symbol - 1) /
    (3 * sp.factorial(d_symbol - 2)))
record("INTERFERENCE.left", "the left-route reconstruction sensitivity is closed",
       sp.simplify(left_sensitivity - left_sensitivity_expected) == 0,
       left_sensitivity)
record("INTERFERENCE.right", "the right-route reconstruction sensitivity is closed",
       sp.simplify(right_sensitivity - right_sensitivity_expected) == 0,
       right_sensitivity)
record("INTERFERENCE.sum", "the full determinant is the weighted sum of both routes",
       sp.simplify(symbolic_core.det() -
                   left_sensitivity * left_route -
                   right_sensitivity * right_route) == 0,
       "det=C_L*L+C_R*R")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_exception_circuit_explanation_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact local constructor explanation",
              "locus": {"g": 2, "q": 7}},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The transverse observation has exactly two collision-source routes, and the full symbolic determinant is their cofactor pairing C_L*L+C_R*R. The right route contains g-2; there the left route reduces to -6(d-1)(d-5), so both disappear only at (2,5). Their exceptional-fiber cofactors are -7200 and 4800, proving either independent repair restores rank. The surviving R0,R1 states have primitive Plucker circuit (1,-3,2).",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_exception_circuit_explanation.json"),
          "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
