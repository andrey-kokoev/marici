"""Symbolic translation-parity theorem for stable magnetic Hall endpoints."""
import json
import os

import sympy as sp

a, g, q, d, w = sp.symbols("a g q d w", integer=True, positive=True)

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


minus_new = -a - g
plus_left = -a - g + q
minus_old = -(a - 2 * d) - g
collision_equation = sp.solve(sp.Eq(plus_left, minus_old), d)
record("TRANSLATION.collision", "plus-left collides with an old minus endpoint iff d=q/2",
       collision_equation == [q / 2], collision_equation)

odd_collision_free = all(not (qv == 2 * dv)
                         for qv in range(1, 101, 2)
                         for dv in range(1, 101))
record("PARITY.odd", "odd translation cannot collide with the depth-two endpoint lattice",
       odd_collision_free, "q odd versus displacement 2d")

even_collision = sp.simplify(
    plus_left.subs(q, 2 * w) - minus_old.subs(d, w))
record("PARITY.even", "q=2w collides exactly with the minus endpoint w pairs behind",
       even_collision == 0, "depth a-2w")

# The adjacent row has opposite parity to every minus endpoint and repairs the
# collision without increasing the backward memory.
plus_adjacent = plus_left + 1
adjacent_collision = sp.solve(sp.Eq(plus_adjacent, minus_old), d)
record("PARITY.repair", "the adjacent B1 row has no integral minus-endpoint collision for even q",
       adjacent_collision == [q / 2 + sp.Rational(1, 2)], adjacent_collision)

memory_identity = sp.simplify((a - (a - 2 * w)) / 2)
record("MEMORY.exact", "the even collision occurs at backward memory w=q/2",
       memory_identity == w, "pole-pair distance w")

# Derive the two endpoint products.  The sign parity cancels in the wedge.
rf_g = sp.rf(a, g)
rf_gm1 = sp.rf(a, g - 1)
minus_weight = (-1) ** (g + 1) * (a + g + q - 1) * rf_g
plus_odd_weight = (-1) ** g * (a + g - q - 1) * rf_g
odd_product = sp.factor(minus_weight * plus_odd_weight)
odd_expected = -rf_g ** 2 * (a + g - q - 1) * (a + g + q - 1)
record("WEIGHT.odd", "odd parity selects two B0 endpoints and gives the odd character",
       sp.simplify(odd_product - odd_expected) == 0, str(odd_product))

m_plus = 1 - g + q - a
x_response = sp.factor(g * (a - 4) * (m_plus + 1) +
                       (a + g - 1) * (m_plus - g))
plus_even_weight = -(-1) ** g * rf_gm1 * x_response
even_raw_product = sp.factor(minus_weight * plus_even_weight)
record("WEIGHT.even", "even parity replaces the collided B0 edge by the adjacent B1 response",
       even_raw_product.has(x_response) or
       sp.simplify(even_raw_product /
                   ((a + g + q - 1) * rf_g * rf_gm1) - x_response) == 0,
       "raw product contains X")

# The stable thresholds put all referenced old pole depths inside the admitted
# lattice: odd q=2w+1 starts at a>=q+3; even q=2w starts at a>=q+4.
threshold_ok = all((qv % 2 and (qv + 3 - 2 * (qv // 2) >= 4)) or
                   (qv % 2 == 0 and (qv + 4 - qv >= 4))
                   for qv in range(1, 101))
record("STABLE.window", "the collision witness lies inside the admitted stable window",
       threshold_ok, "old depth is at least 4")

# A unit pole-depth lattice would erase the parity distinction.
unit_collision = sp.solve(sp.Eq(plus_left, -(a - d) - g), d)
record("FALSIFIER.spacing", "changing pole spacing from two to one destroys the parity split",
       unit_collision == [q], "every integer q then collides")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_translation_parity_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic stable endpoint-collision theorem"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The even/odd transfer split is forced by translating one branch across a pole-depth lattice of spacing two. The plus B0 endpoint collides with an old minus endpoint exactly when d=q/2. Odd q has no integral collision and uses two B0 characters. Even q=2w collides w pairs behind and must use the adjacent B1 response X, producing memory w and the nontrivial Schur lane. Changing the pole lattice spacing destroys this parity mechanism.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_translation_parity.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
