"""Time each stage of the S43 H_d eigensystem at phi=-pi/8."""
import time
import sympy as sp
from harmonic_support import build, eps, EPHI
from wp4_triangle_lo import (charpoly_invariants, eigen_lams, eigvec, trunc,
                             lead)

I = sp.I
t0 = time.time()


def log(msg):
    print(f"[+{time.time() - t0:7.1f}s] {msg}", flush=True)


Yu, Yd = build("S43")
Yu = Yu.subs(EPHI, sp.exp(-I * sp.pi / 8))
Yd = Yd.subs(EPHI, sp.exp(-I * sp.pi / 8))
Hd = sp.expand(Yd * Yd.H)
log("H_d built")

t1, t2, t3 = charpoly_invariants(Hd)
log(f"charpoly invariants done (sizes: {len(sp.Add.make_args(t1))},"
    f" {len(sp.Add.make_args(t2))}, {len(sp.Add.make_args(t3))})")

for n in (6, 8, 10):
    tl = time.time()
    lams = eigen_lams(t1, t2, t3, n)
    log(f"eigen_lams n={n} done in {time.time() - tl:.1f}s; leads "
        f"{[lead(l)[0] for l in lams]}")

for n in (8, 10):
    for i, lam in enumerate(lams):
        tv = time.time()
        v = eigvec(Hd, lam, n)
        log(f"eigvec[{i}] n={n} done in {time.time() - tv:.1f}s")
