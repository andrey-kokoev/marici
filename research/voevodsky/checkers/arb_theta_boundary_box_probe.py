"""Arb box integration of the positive Riemann theta kernel.

Both the omitted theta-series tail and the integration tail are enclosed by
explicit positive majorants for derivative orders 0, 1, and 2.
"""
import json, sys
from pathlib import Path

vendored = Path(__file__).parents[2] / "benincasa" / ".tmp_flint"
sys.path.insert(0, str(vendored))
from flint import acb, arb, ctx

ctx.dps = 50
pi = arb.pi()
N = 5
U = arb(3)


def psi(v):
    total = acb(0)
    for n in range(1, N + 1):
        nn = arb(n * n)
        total += (
            4 * pi * pi * nn * nn * (9 * v).exp()
            - 6 * pi * nn * (5 * v).exp()
        ) * (-pi * nn * (4 * v).exp()).exp()
    return total


def moment_tail(U0, rate, k):
    if k == 0:
        return 1 / rate
    if k == 1:
        return U0 / rate + 1 / (rate * rate)
    return U0 * U0 / rate + 2 * U0 / (rate * rate) + 2 / (rate * rate * rate)


def derivative_tail(k):
    # v > U for the retained n <= N terms.
    E = (4 * U).exp()
    v_tail = arb(0)
    for n in range(1, N + 1):
        nn = arb(n * n)
        rate = 4 * pi * nn * E - arb("9.5")
        coeff = 4 * pi * pi * nn * nn * (arb("9.5") * U - pi * nn * E).exp()
        v_tail += coeff * moment_tail(U, rate, k)

    # All v >= 0 for omitted n > N. Sum a finite majorant and then a
    # geometric remainder. The denominator rate only improves with n.
    def n_term(n):
        nn = arb(n * n)
        rate = 4 * pi * nn - arb("9.5")
        coeff = 4 * pi * pi * nn * nn * (-pi * nn).exp()
        return coeff * moment_tail(arb(0), rate, k)

    M = 40
    n_tail = sum((n_term(n) for n in range(N + 1, M + 1)), arb(0))
    first = n_term(M + 1)
    q = (arb(M + 2) / arb(M + 1)) ** 4 * (-pi * arb(2 * (M + 1) + 1)).exp()
    n_tail += first / (1 - q)
    return v_tail + n_tail


def add_positive_error(value, error):
    # Enclose value + [0,error]. arb(0,1) is the unit-radius zero ball.
    return value + error / 2 + (error / 2) * arb(0, 1)


def certify_box(mid, rad):
    x = arb(float(mid), float(rad))
    vals = []
    tails = []
    for k in range(3):
        def integrand(v, _analytic, k=k):
            base = psi(v)
            if k == 0:
                return base * (x * v).cosh()
            if k == 1:
                return base * v * (x * v).sinh()
            return base * v * v * (x * v).cosh()
        prefix = acb.integral(integrand, arb(0), U, abs_tol=arb("1e-35"), eval_limit=100000).real
        tail = derivative_tail(k)
        vals.append(add_positive_error(prefix, tail))
        tails.append(tail)
    X, X1, X2 = vals
    m = X1 / X
    m1 = X2 / X - m * m
    G = (1 + 4 * x * x) * m - x * (1 - 4 * x * x) * m1
    return x, vals, tails, G

boxes = [
    *[(str(0.0525 + 0.005 * j), "0.0025") for j in range(20)],
    ("0.1625", "0.0125"),
    ("0.1875", "0.0125"),
    ("0.2125", "0.0125"),
    ("0.2375", "0.0125"),
    ("0.2625", "0.0125"),
    ("0.2875", "0.0125"),
    ("0.35", "0.05"),
    ("0.45", "0.05"),
]
records=[]
for mid,rad in boxes:
    x,vals,tails,G=certify_box(mid,rad)
    records.append({"x":str(x),"x_lower":str(x.lower()),"x_upper":str(x.upper()),"Xi":str(vals[0]),"Xi1":str(vals[1]),"Xi2":str(vals[2]),"tail_bounds":[str(t) for t in tails],"G":str(G),"G_lower":str(G.lower()),"G_upper":str(G.upper()),"positive":G.lower()>0})
out={"n_terms":N,"u_cutoff":str(U),"boxes":records,"tails_attached":True,"all_listed_boxes_certified_positive":all(r["positive"] for r in records),"interval_certified":True}
if __name__=='__main__':
    path=Path(__file__).parents[1]/'results'/'arb-theta-boundary-box-probe.json';path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
