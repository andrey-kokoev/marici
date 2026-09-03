"""Exact-prefix plus positive-tail contact feasibility scout.

At one high-precision-validated t slice, retain prime-power terms n <= P
exactly and relax only the remaining positive measure by its M0,M2,M4 Gram
constraints. This measures how much arithmetic source structure is needed to
collapse the generic moment residue.
"""

import json
import math
from pathlib import Path

import numpy as np
from scipy.special import digamma, roots_hermite

T = 0.275
XI = np.linspace(0.0, 25.0, 2501)
NMAX = 2_000_000
PREFIXES = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 16384]
HERMITE_ORDER = 256
NUMERICAL_SLACK = 2e-13


def prime_power_terms(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    ns, vm = [], []
    for p in np.flatnonzero(sieve):
        n = int(p)
        lp = math.log(n)
        while n <= limit:
            ns.append(n)
            vm.append(lp)
            if n > limit // int(p):
                break
            n *= int(p)
    order = np.argsort(ns)
    return np.asarray(ns, float)[order], np.asarray(vm)[order]


def endpoint(t, x):
    phase = t*x
    pref = np.exp(t/4-t*x*x)
    co, si = np.cos(phase), np.sin(phase)
    return (
        pref*co,
        pref*(-2*t*x*co-t*si),
        pref*((4*t*t*x*x-2*t-t*t)*co+4*t*t*x*si),
    )


ns, vm = prime_power_terms(NMAX)
logs = np.log(ns)
weights_prime = vm/np.sqrt(ns)*np.exp(-(logs*logs)/(4*T))
c = 1/(2*math.sqrt(math.pi*T))

hn, hw = roots_hermite(HERMITE_ORDER)
u = XI[:, None] + hn[None, :]/math.sqrt(T)
q = np.real(digamma(.25+.5j*u))
g0 = -math.log(math.pi)/(4*math.sqrt(math.pi*T)) + q@hw/(4*math.pi*math.sqrt(T))
g1 = (q*hn)@hw/(2*math.pi)
g2 = math.sqrt(T)*(q*(2*hn*hn-1))@hw/(2*math.pi)
e0, e1, e2 = endpoint(T, XI)
a0, a1, a2 = e0+g0, e1+g1, e2+g2

rows = []
for prefix in PREFIXES:
    exact = ns <= prefix
    tail = ~exact
    loge, we = logs[exact], weights_prime[exact]
    logt, wt = logs[tail], weights_prime[tail]
    rpre = np.zeros_like(XI)
    ipre = np.zeros_like(XI)
    r2pre = np.zeros_like(XI)
    if len(we):
        for start in range(0, len(XI), 100):
            stop = min(start+100, len(XI))
            phases = XI[start:stop, None]*loge[None, :]
            rpre[start:stop] = np.cos(phases)@we
            ipre[start:stop] = np.sin(phases)@(we*loge)
            r2pre[start:stop] = np.cos(phases)@(we*loge*loge)
    m0 = float(np.sum(wt))
    m2 = float(np.sum(wt*logt**2))
    m4 = float(np.sum(wt*logt**4))
    rr = a0/c-rpre
    ii = -a1/c-ipre
    ellipse = rr*rr/(m0*m0) + ii*ii/(m0*m2)
    ellipse_excluded = ellipse > 1+NUMERICAL_SLACK
    center = (m2/m0)*rr
    variance = np.maximum(0, (m4-m2*m2/m0)*(m0-rr*rr/m0))
    upper_r2 = center+np.sqrt(variance)
    lower_r2 = -a2/c-r2pre
    curvature_excluded = lower_r2 > upper_r2+NUMERICAL_SLACK
    survives = ~(ellipse_excluded | curvature_excluded)
    sx = XI[survives]
    # Connected survivor runs, useful for testing corridor localization.
    runs = []
    if len(sx):
        indices = np.flatnonzero(survives)
        split = np.where(np.diff(indices)>1)[0]+1
        for run in np.split(indices, split):
            runs.append([float(XI[run[0]]), float(XI[run[-1]])])
    rows.append({
        "prefix_n": prefix,
        "exact_term_count": int(np.sum(exact)),
        "tail_M0": m0,
        "tail_M2": m2,
        "tail_M4": m4,
        "survivor_fraction": float(np.mean(survives)),
        "survivor_count": int(np.sum(survives)),
        "survivor_runs": runs,
        "ellipse_excluded_fraction": float(np.mean(ellipse_excluded)),
        "curvature_additional_fraction": float(np.mean(curvature_excluded & ~ellipse_excluded)),
    })

result = {
    "schema": "marici.exact-prefix-tail-contact-scout.v1",
    "certified": False,
    "t": T,
    "xi_range": [0.0,25.0],
    "xi_step": float(XI[1]-XI[0]),
    "nmax": NMAX,
    "hermite_order": HERMITE_ORDER,
    "numerical_slack": NUMERICAL_SLACK,
    "rows": rows,
    "limitations": [
        "floating-point and grid scout, not interval certification",
        "prime powers above nmax omitted",
        "tail relaxed to three scalar moments",
        "Gauss-Hermite quadrature not enclosed",
    ],
}
out = Path(__file__).parents[1]/"results"/"exact-prefix-tail-contact-scout.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps([{k:r[k] for k in ("prefix_n","survivor_fraction","survivor_runs")} for r in rows],indent=2))
