"""Exact discovery and held-out test of the transverse-response recurrence."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def transverse_response(g):
    q, k = 2 * g + 8, g // 2 + 4
    columns = component(g, k, q)
    rows = [3 if row == 1 else row for row in hall_rows(columns)]
    endpoint_columns = [0, len(columns) - 1]
    interior_columns = [index for index in range(len(columns))
                        if index not in endpoint_columns]
    endpoint_rows = [rows.index(0), rows.index(3)]
    interior_rows = [index for index in range(len(rows))
                     if index not in endpoint_rows]
    A = sp.Matrix([[columns[j].get(rows[i], 0) for j in interior_columns]
                   for i in interior_rows])
    B = sp.Matrix([[columns[j].get(rows[i], 0) for j in endpoint_columns]
                   for i in interior_rows])
    C = sp.Matrix([[columns[j].get(rows[i], 0) for j in interior_columns]
                   for i in endpoint_rows])
    E = sp.Matrix([[columns[j].get(rows[i], 0) for j in endpoint_columns]
                   for i in endpoint_rows])
    return sp.factor((E - C * A.inv() * B)[1, 1])


def multiplier(g):
    return sp.Rational(
        4 * g * (g + 3) * (g + 4) * (2 * g + 1) * (2 * g + 3) *
        (g * g - g - 26),
        (g - 2) * (g + 6) * (g + 7) * (g * g - 5 * g - 20))


values = {g: transverse_response(g) for g in range(2, 48, 2)}
ratios = {g: sp.factor(values[g] / values[g - 2]) for g in range(4, 48, 2)}

checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("BASE.tau", "the initial transverse response is tau_2=320/3",
       values[2] == sp.Rational(320, 3), values[2])
record("RATIO.fit", "the factored recurrence matches all discovery grades 4..40",
       all(ratios[g] == multiplier(g) for g in range(4, 42, 2)),
       "19 exact ratios")
record("RATIO.heldout", "the recurrence predicts held-out grades 42,44,46",
       all(ratios[g] == multiplier(g) for g in (42, 44, 46)),
       [(g, ratios[g]) for g in (42, 44, 46)])

# Both exceptional quadratics have discriminant 105, not a square.  Hence
# neither numerator nor denominator can vanish at an integral grade.
record("FACTOR.integral", "the two quadratic factors have nonsquare discriminant 105",
       not sp.ntheory.primetest.is_square(105), "discriminant=105")
record("FACTOR.domain", "the proposed multiplier has no zero or pole at even g>=4",
       all(multiplier(g) != 0 for g in range(4, 1002, 2)),
       "factor proof cross-checked through g=1000")
record("SIGN.law", "tau is positive at g=2,4 and negative for every tested g>=6",
       values[2] > 0 and values[4] > 0 and
       all(values[g] < 0 for g in range(6, 48, 2)), "g=2..46")

wrong = sp.Rational(
    4 * 42 * 45 * 46 * 85 * 87 * (42 * 42 - 42 - 24),
    40 * 48 * 49 * (42 * 42 - 5 * 42 - 20))
record("FALSIFIER.quadratic", "changing -26 to -24 leaves a held-out residual",
       ratios[42] - wrong != 0, sp.factor(ratios[42] - wrong))

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_transverse_recurrence_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact recurrence discovery with held-out tests",
              "g": "even 2..46", "fit": "4..40", "held_out": [42, 44, 46]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "values": {str(g): str(value) for g, value in values.items()},
    "ratios": {str(g): str(value) for g, value in ratios.items()},
    "proposed_multiplier": "4*g*(g+3)*(g+4)*(2*g+1)*(2*g+3)*(g^2-g-26)/((g-2)*(g+6)*(g+7)*(g^2-5*g-20))",
    "verdict": "The transverse response satisfies the displayed hypergeometric ratio at 19 discovery grades and three held-out grades through g=46. The multiplier has no zero or pole at any even integer g>=4 because both exceptional quadratics have nonsquare discriminant 105. This is strong exact discovery evidence and a conditional all-grade nonvanishing proof, but the recurrence itself still requires symbolic Schur-elimination derivation."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_transverse_recurrence.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
