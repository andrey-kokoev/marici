"""Uniform pole law of the V-tower channels (marici.Strominger).

Certifies, symbolically and without witnesses, that EVERY channel of tower
orders 2, 3, and 4 has (1+u)-pole order exactly n-1:

    G_alpha * (1+u)^(n-1)  is (1+u)-free        (upper bound)
    G_alpha * (1+u)^(n-2)  still has a (1+u) pole  (exactness, n >= 2)

Consequence recorded in research/strominger/rung4-foldrule.md section 4:
the (1+u)-pole order is uniform across each rung, so the p-dependence of
the depth-graded fold rule (close iff k >= max(1, p-1)) does NOT come
from pole counting; it must live in the numerator structure H_alpha.

Method: exact rational arithmetic; a factor is a (1+u) pole iff it appears
in the factorization of the cancelled denominator. No witnesses, no floats.

Output: research/strominger/results/vtower_polelaw.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

z, zb, zk, zbk, Ek = sp.symbols("z zb zk zbk Ek")
om = sp.symbols("om", positive=True)
sq2 = sp.sqrt(2)
u = z * zb

c_zk = -sq2 * om * (z - zk) ** 2 / (1 + u)
c_Ek = -sq2 * Ek * om * (z - zk) * (1 + z * zbk) / ((1 + u) * (1 + zk * zbk))
den = -4 * Ek * om ** 2 * (z - zk) * (zb - zbk) / ((1 + u) * (1 + zk * zbk))
cs = [c_zk, c_Ek]

results = []


def record(cid, statement, status, detail=""):
    results.append({"id": cid, "statement": statement,
                    "status": status, "detail": detail})
    print(f"[{status:>4}] {cid}: {statement}" + (f"  ({detail})" if detail else ""),
          flush=True)


def check_true(cid, statement, cond, detail=""):
    record(cid, statement, "pass" if bool(cond) else "FAIL", detail)
    return bool(cond)


def Vop(f):
    return sp.cancel(c_zk * sp.diff(f, zk) + c_Ek * sp.diff(f, Ek))


def tower(nmax):
    A = [{(0, 0): sp.Integer(1)}]
    for n in range(1, nmax + 1):
        cur = {}
        for alpha, coef in A[-1].items():
            vc = Vop(coef)
            if vc != 0:
                cur[alpha] = sp.cancel(cur.get(alpha, 0) + vc)
            for i in range(2):
                na = list(alpha)
                na[i] += 1
                na = tuple(na)
                val = sp.cancel(cur.get(na, 0) + coef * cs[i])
                if val != 0:
                    cur[na] = val
        A.append(cur)
    return A


def has_upole(expr):
    """The cancelled denominator contains the factor (1+u)."""
    _, deno = sp.fraction(sp.cancel(expr))
    return any(sp.cancel(f - (1 + u)) == 0
               for f, _ in sp.factor_list(deno)[1])


print("[....] building the V-tower through order 4...", flush=True)
A = tower(4)

for n in (2, 3, 4):
    Gs = {alpha: sp.cancel(sp.cancel(A[n][alpha] / den) * (zb - zbk))
          for alpha in A[n]}
    upper = {alpha: not has_upole(G * (1 + u) ** (n - 1))
             for alpha, G in Gs.items()}
    lower = {alpha: has_upole(G * (1 + u) ** (n - 2))
             for alpha, G in Gs.items()}
    check_true(f"P{n}.uniform", f"order {n}: every channel G satisfies "
               f"G = H (1+u)^-(n-1) with H (1+u)-free (certified, "
               f"{len(Gs)} channels)",
               all(upper.values()),
               f"free: {sorted(upper)}")
    check_true(f"P{n}.exact", f"order {n}: the pole order is EXACTLY n-1 = "
               f"{n-1} — G (1+u)^(n-2) still has a (1+u) pole in every "
               f"channel (certified)",
               all(lower.values()),
               f"pole at n-2: {sorted(lower)}")

mandatory = [r for r in results if r["status"] == "FAIL"]
n_pass = sum(1 for r in results if r["status"] == "pass")
summary = {
    "total": len(results), "passed": n_pass, "failed": len(mandatory),
    "failed_ids": [r["id"] for r in mandatory],
    "law": "every order-n tower channel has (1+u)-pole order exactly n-1",
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "results", "vtower_polelaw.json")
with open(out, "w") as fh:
    json.dump({"summary": summary, "checks": results}, fh, indent=2)
print(f"\n{n_pass}/{len(results)} checks passed; results -> {out}")
raise SystemExit(0 if not mandatory else 1)
