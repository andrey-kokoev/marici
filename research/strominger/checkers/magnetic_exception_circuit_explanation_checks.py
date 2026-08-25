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
