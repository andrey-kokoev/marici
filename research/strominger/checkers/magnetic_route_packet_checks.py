"""Exact route-packet separation of loss and destructive interference."""
import json
import os
import sympy as sp


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Abstract one-source models for the two fibers of
# ker(sigma*T): ker(T) and im(T) intersect ker(sigma).
sigma = sp.Matrix([[1, 1]])
loss_transport = sp.Matrix([[0], [0]])
interference_transport = sp.Matrix([[3], [-3]])
visible_transport = sp.Matrix([[1], [0]])
record("EXACT.loss", "route loss lies in ker(T)",
       loss_transport.rank() == 0 and (sigma * loss_transport).rank() == 0,
       "source maps to the zero route packet")
record("EXACT.interference", "interference is nonzero transport into ker(sigma)",
       interference_transport.rank() == 1 and
       sigma * interference_transport == sp.zeros(1, 1),
       "source maps to the nonzero anti-diagonal packet")
record("EXACT.visible", "a route packet outside ker(sigma) remains observable",
       (sigma * visible_transport).rank() == 1,
       "nonzero packet and nonzero composed readout")


def routes(grade, excess):
    g = sp.Rational(grade)
    d = sp.Rational(excess)
    left = -(2 * d * g + 2 * d - g**2 - 11 * g - 4) * sp.rf(d - 1, g - 1)
    right = (g * (d - 4) * (d - 3) * (g - 2) * (g - 1) * (g + 3) *
             sp.rf(d + 1, g - 3) / 2)
    c_left = (g * (g + 3) * (d * g - 2 * d - 5 * g + 4) *
              sp.factorial(g + 3) * sp.rf(d + 1, g - 1) / 6)
    c_right = sp.factorial(g + 3) * sp.rf(d - 1, g + 1) / 3
    return tuple(sp.factor(value) for value in (left, right, c_left, c_right))


# The admissible magnetic exception is genuine route loss.
left_25, right_25, _, _ = routes(2, 5)
record("MAGNETIC.loss", "the integral exceptional fiber loses both carriers",
       left_25 == 0 and right_25 == 0, "(g,d)=(2,5)")

# The complexified/rational obstruction also contains genuine interference.
# P(6,d) has rational roots 17/3 and 37/3; choose the first.
left, right, c_left, c_right = routes(6, sp.Rational(17, 3))
amplitude_left = sp.factor(c_left * left)
amplitude_right = sp.factor(c_right * right)
record("MAGNETIC.routes_live", "the rational obstruction point has two live routes",
       left != 0 and right != 0 and amplitude_left != 0 and amplitude_right != 0,
       f"L={left}; R={right}")
record("MAGNETIC.interference", "the two nonzero route amplitudes cancel exactly",
       amplitude_left + amplitude_right == 0,
       f"A={amplitude_left}; B={amplitude_right}")

# Arithmetic protection of the admitted depth lattice.
d_symbol = sp.symbols("d")
P6 = sp.factor(
    d_symbol**2 * 6**2 + d_symbol**2 * 6 - 6 * d_symbol**2 -
    d_symbol * 6**3 - 12 * d_symbol * 6**2 - 5 * d_symbol * 6 +
    30 * d_symbol + 5 * 6**3 + 39 * 6**2 + 12 * 6 - 40)
record("ARITHMETIC.factor", "the first higher-grade interference fiber factors over Q",
       sp.expand(P6 - 4 * (3 * d_symbol - 17) *
                 (3 * d_symbol - 37)) == 0,
       P6)
record("ARITHMETIC.off_lattice", "both grade-six balance points miss integer depth",
       sp.solve(sp.Eq(P6, 0), d_symbol) ==
       [sp.Rational(17, 3), sp.Rational(37, 3)],
       "roots=17/3,37/3")

# Cubic-cover preflight: the local residual zero is not a three-column kernel
# of the full fractional path matrix.
def full_column(grade, a, m):
    source = [sp.binomial(grade, j) * (-1) ** (grade - j) *
              sp.rf(a, grade - j) * sp.rf(4 - a, j)
              for j in range(grade + 1)]
    path = [m * source[0]]
    path += [(m + j) * source[j] +
             (m + j - 1 - grade) * source[j - 1]
             for j in range(1, grade + 1)]
    path.append(m * source[grade])
    delta = 1 - grade - (a + m)
    shift = -a - grade if delta > 0 else -a - grade + abs(delta)
    sign = 1 if delta > 0 else -1
    return {sp.simplify(shift + j): sp.factor(sign * value)
            for j, value in enumerate(path) if value != 0}


grade = 6
excess = sp.Rational(17, 3)
labels = [(0, 1 - 2 * grade - excess),
          (excess - 1, 2), (excess + 1, 0)]
columns = [full_column(grade, a, m) for a, m in labels]
full_rows = sorted(set().union(*(set(column) for column in columns)),
                   key=lambda value: float(value))
full_matrix = sp.Matrix([[column.get(row, 0) for column in columns]
                         for row in full_rows])
record("COVER.no_three_kernel", "the rational residual zero is not a full three-column kernel",
       full_matrix.rank() == 3 and not full_matrix.nullspace(),
       f"rows={len(full_rows)}; rank={full_matrix.rank()}")

lifted_exponents = [(sp.simplify(4 - 3 * a), sp.simplify(3 * m))
                    for a, m in labels]
record("COVER.exponents", "the cubic spin-two pullback has integral Laurent exponents",
       lifted_exponents == [(4, -50), (-10, 6), (-16, 0)],
       lifted_exponents)
w, wb = sp.symbols("w wb")
metric = 18 * w**2 * wb**2 / (1 + w**3 * wb**3)**2
connection = sp.factor(sp.diff(sp.log(metric), w))
connection_expected = 2 / w - 6 * w**2 * wb**3 / (1 + w**3 * wb**3)
record("COVER.connection", "the cubic pullback changes the connection and is ramified",
       sp.simplify(connection - connection_expected) == 0,
       connection_expected)

# Deck-equivariance is the descent type.  For w -> omega*w and
# wb -> omega^-1*wb, w^p wb^r has character p-r mod 3.  A pulled-back C_zz
# component has the fixed Jacobian character 4 mod 3 = 1.
deck_characters = [int((p - r) % 3) for p, r in lifted_exponents]
record("COVER.deck_split", "the three proposed sources split across deck characters",
       deck_characters == [0, 2, 2], deck_characters)
record("COVER.no_descent", "none belongs to the descended spin-two character sector",
       all(character != 1 for character in deck_characters),
       "essential pullback image has character 1 mod 3")
record("COVER.no_coherent_sum", "the proposed three-term circuit is not deck-homogeneous",
       len(set(deck_characters)) > 1,
       "a descended linear relation cannot mix characters 0 and 2")

# Include the two covariant w indices of C_ww.  The intrinsic deck charge of
# w^p wb^r (dw)^n (dwb)^m is p-r+n-m mod 3.  Descent means charge zero.
tensor_charges = [int((p - r + 2) % 3) for p, r in lifted_exponents]
record("CHARGE.tensor", "the intrinsic spin-two deck charges are (2,1,1)",
       tensor_charges == [2, 1, 1], tensor_charges)

# Modular constructor proof: D_w lowers p by one and adds one w index;
# D_wb lowers r by one and adds one wb index.  Both preserve total charge.
p, r, n, m = sp.symbols("p r n m", integer=True)
charge = p - r + n - m
charge_dw = (p - 1) - r + (n + 1) - m
charge_dwb = p - (r - 1) + n - (m + 1)
record("CHARGE.derivatives", "both covariant derivative constructors preserve deck charge",
       sp.expand(charge_dw - charge) == 0 and
       sp.expand(charge_dwb - charge) == 0,
       "exponent loss is exactly balanced by the added tensor index")
record("CHARGE.reflection", "reflection reverses deck charge",
       sp.expand((r - p + m - n) + charge) == 0,
       "paired route sectors are conjugate, not silently identified")

# To align the first candidate charge 2 with the other charge-1 sources, an
# adapter must itself carry charge 2 (for example multiplication by w^2).
record("CHARGE.adapter", "the minimal character-changing repair must carry nonzero charge",
       (tensor_charges[0] + 2) % 3 == tensor_charges[1] and
       (2 - 0) % 3 == 2,
       "charge-2 adapter, e.g. w^2, aligns the sectors but breaks descent")

# The analytic continuation also moves source labels; d is a discrete type,
# not a coefficient of a fixed matrix module.  Audit the depth cosets before
# and after the cubic pullback.  If A=-p is the cover pole-depth label, the
# essential image of original even a has A=3a-4 congruent to 2 mod 6 and
# barred exponent divisible by 3.
fractional_depths = [label[0] for label in labels]
fractional_cosets = [sp.Mod(depth, 2) for depth in fractional_depths]
cover_pole_depths = [-p_value for p_value, _ in lifted_exponents]
cover_depth_cosets = [int(value % 6) for value in cover_pole_depths]
cover_bar_cosets = [int(value % 3) for _, value in lifted_exponents]
record("TYPE.moving_columns", "analytic continuation moves columns between depth cosets",
       fractional_cosets == [0, sp.Rational(2, 3), sp.Rational(2, 3)],
       fractional_cosets)
record("TYPE.cover_cosets", "the cubic candidates occupy two cover-depth congruence classes",
       cover_pole_depths == [-4, 10, 16] and
       cover_depth_cosets == [2, 4, 4],
       f"depths={cover_pole_depths}; mod6={cover_depth_cosets}")
record("TYPE.essential_image", "no candidate satisfies both essential-image congruences",
       all(not (depth_class == 2 and bar_class == 0)
           for depth_class, bar_class in zip(cover_depth_cosets, cover_bar_cosets)),
       f"required (A mod6,r mod3)=(2,0); actual={list(zip(cover_depth_cosets,cover_bar_cosets))}")

# Arbitrary cyclic-cover theorem.  For z=w^N, a spin-two monomial has total
# deck charge N*(2-a-m) mod N.  Reflected q branches differ by 2*N*q, so a
# cover can align them only if 2*q is integral.
def cover_charge(degree, a, m):
    return sp.Mod(degree * (2 - a - m), degree)


cover_failures = []
for excess_value in (sp.Rational(17, 3), sp.Rational(37, 3)):
    q_value = 6 + excess_value
    source_labels = [(0, 1 - 12 - excess_value),
                     (excess_value - 1, 2),
                     (excess_value + 1, 0)]
    for degree in range(3, 61, 3):
        charges = [cover_charge(degree, a, m) for a, m in source_labels]
        if charges[0] == charges[1] or charges[1] != charges[2]:
            cover_failures.append((q_value, degree, charges))
record("COVER.all_degrees", "no cyclic cover clearing thirds aligns the reflected branches",
       not cover_failures, f"N=3,6,...,60; failures={cover_failures[:1]}")

q_symbol, degree_symbol, grade_symbol = sp.symbols(
    "q N grade", integer=True, positive=True)
minus_sum = 1 - grade_symbol - q_symbol
plus_sum = 1 - grade_symbol + q_symbol
charge_difference = sp.expand(
    degree_symbol * (2 - minus_sum) - degree_symbol * (2 - plus_sum))
record("COVER.criterion", "the reflected deck-charge difference is exactly 2*N*q",
       charge_difference == 2 * degree_symbol * q_symbol,
       "alignment modulo N requires 2q integral")
record("COVER.thirds", "both rational interference components violate the cover criterion",
       all(not (2 * q_value).is_integer
           for q_value in (sp.Rational(35, 3), sp.Rational(55, 3))),
       "q=35/3,55/3; neither has integral 2q")

# Join the discriminant classification with the cover criterion.  For integer
# grade, a rational quadratic root requires the integer discriminant to be a
# square.  The companion Diophantine theorem proves the only higher-grade
# square occurs at g=6; this exact audit extends through g=500.
def obstruction(grade_value, depth_value):
    return (depth_value**2 * grade_value**2 +
            depth_value**2 * grade_value - 6 * depth_value**2 -
            depth_value * grade_value**3 -
            12 * depth_value * grade_value**2 -
            5 * depth_value * grade_value + 30 * depth_value +
            5 * grade_value**3 + 39 * grade_value**2 +
            12 * grade_value - 40)


rational_zeroes = [(2, sp.Rational(5))]
for grade_value in range(3, 501):
    polynomial = sp.Poly(obstruction(grade_value, d_symbol), d_symbol)
    for root in sp.solve(polynomial.as_expr(), d_symbol):
        if root.is_Rational and root >= 3:
            rational_zeroes.append((grade_value, root))
record("COVER.rational_class", "the rational residual zeros are exactly the three known points",
       rational_zeroes == [(2, sp.Rational(5)),
                           (6, sp.Rational(17, 3)),
                           (6, sp.Rational(37, 3))],
       rational_zeroes)
compatible_zeroes = [
    (grade_value, depth_value)
    for grade_value, depth_value in rational_zeroes
    if (2 * (grade_value + depth_value)).is_integer
]
record("COVER.descent_class", "only the original route-loss zero passes cyclic descent typing",
       compatible_zeroes == [(2, sp.Rational(5))], compatible_zeroes)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_route_packet_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact local residual route-packet witnesses",
              "exclusion": "does not construct a fractional full magnetic kernel"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The intermediate local route packet separates loss from interference. The analytically continued residual coordinate cancels at grade-six rational depths, but this does not lift to a three-column full kernel. On the cubic cover the candidate spin-two Laurent components have deck characters (0,2,2), whereas descended base tensors have character 1; the proposed circuit is not deck-homogeneous. Thus representability on the cover does not supply a descended constructible state.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_route_packet.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
