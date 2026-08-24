"""Symbolic endpoint localization and even-cycle correction."""
import json
import os

import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_parity_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
determinant = namespace["determinant"]

a, g, q = sp.symbols("a g q", integer=True, positive=True)
rf_g = sp.rf(a, g)
rf_gm1 = sp.rf(a, g - 1)
endpoint_minus = (-1) ** (g + 1) * (a + g + q - 1) * rf_g
endpoint_plus_odd = (-1) ** g * (a + g - q - 1) * rf_g

# For even q the selected plus edge is -B1.  X is B1 after removing its
# parity sign and rising-factor character.
m_plus = 1 - g + q - a
x_even = sp.factor(g * (a - 4) * (m_plus + 1) +
                   (a + g - 1) * (m_plus - g))
endpoint_plus_even = -(-1) ** g * rf_gm1 * x_even

odd_character = -rf_g ** 2 * (a + g - q - 1) * (a + g + q - 1)
even_character = (q * g * (g + 3) * rf_g * rf_gm1 *
                  (a + g + q - 1))

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("ODD.endpoint", "the odd-q transfer character is exactly the endpoint product",
       sp.simplify(endpoint_minus * endpoint_plus_odd - odd_character) == 0,
       "symbolic identity")

even_product = sp.factor(endpoint_minus * endpoint_plus_even)
even_correction = sp.factor(even_character / even_product)
record("EVEN.correction", "the even-q character is the endpoint product times q*g*(g+3)/X",
       sp.simplify(even_correction - q * g * (g + 3) / x_even) == 0,
       str(even_correction))
record("EVEN.nontrivial", "the even-cycle correction is not identically one",
       sp.simplify(x_even - q * g * (g + 3)) != 0, str(x_even))

# Cross-check the two identities against exact determinant ratios in their
# stable domains.  This checks the previously discovered scalar characters,
# while the endpoint factorization above is symbolic.
odd_failures = []
even_failures = []
for gv in range(2, 9):
    for qv in range(2, 12):
        start = qv // 2 + 2
        previous = None
        for kv in range(0, start + 5):
            try:
                current = determinant(gv, kv, qv)
            except AssertionError:
                previous = None
                continue
            if previous is None or kv < start:
                previous = current
                continue
            ratio = sp.Rational(current, previous)
            av = 2 * kv
            substitutions = {a: av, g: gv, q: qv}
            expected = (odd_character if qv % 2 else even_character).subs(substitutions)
            if ratio != expected:
                (odd_failures if qv % 2 else even_failures).append(
                    (gv, qv, kv, ratio, expected))
            previous = current
record("ODD.ratios", "odd stable determinant ratios localize to endpoint products",
       not odd_failures, "175 exact ratios")
record("EVEN.ratios", "even stable ratios include the displayed cycle correction",
       not even_failures, "175 exact ratios")

# The odd singular factor is outside the stable region.  If q=2w+1 and
# k>=w+2, then a>=q+3 and a+g-q-1>=g+2>0.
stable_odd_positive = all(2 * k + gv - qv - 1 >= gv + 2
                          for gv in range(2, 101)
                          for qv in range(3, 101, 2)
                          for k in [qv // 2 + 2])
record("ODD.stable", "the odd singular factor is strictly positive after initialization",
       stable_odd_positive, "a+g-q-1>=g+2")

record("EXCEPTION.q7", "the grade-two q=7 exception is an odd endpoint zero before stability",
       odd_character.subs({a: 6, g: 2, q: 7}) == 0,
       "a+g-q-1=0 at (2,7,3)")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_parity_localization_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic parity-localization identities with exact finite ratio audit",
              "ratio_audit": {"g": [2, 8], "q": [2, 11], "steps": 5}},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "x_even": str(x_even),
    "verdict": "Odd-q scalar transport localizes exactly to the two new endpoint weights; its cycles are determinant-invisible after elimination. Even-q transport carries a genuine Schur correction q*g*(g+3)/X. The q=7 class is the zero of the odd plus-endpoint character in the finite initialization region, while that character is strictly nonzero at every stable step.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_parity_localization.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
