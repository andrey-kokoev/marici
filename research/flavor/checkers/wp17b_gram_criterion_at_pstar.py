#!/usr/bin/env python3
"""WP17b: certified orbit-3 exclusion at the exact physical point p*.

WP10 derived a closed symbolic criterion (mpmath-verified convexity and
minimum) for a Hermitian Gram matrix H = (diag A,B,C; off-diagonal
squared magnitudes p=|H01|^2, q=|H02|^2, r=|H12|^2) to admit a
zero-diagonal square root Y=[[0,a,b],[c,0,d],[e,f,0]], H = Y Y^dagger:

    realizable  iff  A B > p  and
    C (A B - p) >= r A + q B + 2 sqrt(p q r).

WP10 applied it to the 3-sigma experimental box (all 128 corners
excluded).  WP17's exact inverse solve (wp17_orbit3_exclusion.py) found
zero preimages of p* empirically.  This checker closes the loop: it
evaluates the SAME closed criterion at the exact point p* itself, for
both sector halves of orbit 3.

Half A (84,238): Yu anti-diagonal monomial => Uu is a permutation =>
the down Gram matrix in flavor basis is H = V D_d V^dagger; the
criterion is applied under all 6 row labelings (mass-to-row
assignments of the monomial permutation).

Half B (238,84): Yd monomial => H = V^dagger D_u V, same criterion.

V and the singular values are taken from the WP16a seed (global-best
WP15b fit, member (281,395), chi2 = 3.3628), rebuilt exactly from its
stored parameters.  All-criterion evaluations in mpmath at 60 digits.

Outputs: research/flavor/results/wp17b_gram_criterion_at_pstar.json
"""
import itertools
import json
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7

mp.mp.dps = 60

SEED_MEMBER = (281, 395)
SEED_LOG_MAGS = [-5.641984537468731, -8.055423452738562,
                 -11.852731054867656, -0.03355678352884273,
                 -8.141879941809702, -7.28226346827134,
                 -9.634136874199553, -4.122962332118776,
                 -6.375964291207225]
SEED_PHI = 1.5754637056806353


def criterion_gap(H):
    """Per-labeling (f_min - C, relative gap).  Positive => excluded."""
    rows = []
    for pi in itertools.permutations(range(3)):
        i, j, k = pi
        A = mp.re(H[i, i]); B = mp.re(H[j, j]); C = mp.re(H[k, k])
        p = abs(H[i, j])**2; q = abs(H[i, k])**2; r = abs(H[j, k])**2
        if A * B <= p:
            rows.append({"row_permutation": list(pi),
                         "AB_minus_p": mp.nstr(A*B - p, 6),
                         "excluded_by": "AB<=p (no positive solution)",
                         "relative_gap": None})
            continue
        f_min = (r*A + q*B + 2*mp.sqrt(p*q*r)) / (A*B - p)
        gap = f_min - C
        rows.append({"row_permutation": list(pi),
                     "f_min_minus_C": mp.nstr(gap, 12),
                     "relative_gap": mp.nstr(gap / C, 12),
                     "criterion_satisfied": bool(gap <= 0)})
    return rows


def to_mp(M):
    return mp.matrix([[mp.mpc(complex(M[i, j])) for j in range(3)]
                      for i in range(3)])


def main():
    mu, md = SEED_MEMBER
    phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
    theta = np.array(SEED_LOG_MAGS + [SEED_PHI])
    Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot, theta)
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    V = to_mp(Uu.conj().T @ Ud)
    Du = mp.diag([mp.mpf(float(x)) for x in su2])
    Dd = mp.diag([mp.mpf(float(x)) for x in sd2])

    halves = {
        "up84_down238": ("V Dd V^dagger", V * Dd * V.transpose_conj()),
        "up238_down84": ("V^dagger Du V", V.transpose_conj() * Du * V),
    }
    report = {}
    for label, (construction, H) in halves.items():
        rows = criterion_gap(H)
        satisfied = [r for r in rows if r.get("criterion_satisfied")]
        gaps = [mp.mpf(r["relative_gap"]) for r in rows
                if r["relative_gap"] is not None]
        report[label] = {
            "construction": construction,
            "labelings": rows,
            "any_labeling_realizable": bool(satisfied),
            "min_relative_gap": mp.nstr(min(gaps), 12) if gaps else None,
        }
        print(f"{label} ({construction}): realizable labelings = "
              f"{len(satisfied)}/6, min relative gap = "
              f"{report[label]['min_relative_gap']}", flush=True)

    excluded = all(not v["any_labeling_realizable"]
                   for v in report.values())
    out = {
        "schema": "marici.flavor.orbit3_criterion_at_pstar.v1",
        "purpose": "certified orbit-3 exclusion at the exact WP16a "
                   "physical point p* via the WP10 closed Gram criterion",
        "seed": {"member": list(SEED_MEMBER), "phi": SEED_PHI,
                 "log_mags": SEED_LOG_MAGS},
        "criterion": ("H realizable as zero-diagonal Y Y^dagger iff "
                      "A B > p and C(AB-p) >= rA+qB+2 sqrt(pqr); "
                      "symbolic convexity/minimum proof in "
                      "checkers/wp10_orbit3_gram_criterion.py"),
        "mp_dps": mp.mp.dps,
        "halves": report,
        "conclusion": ("EXCLUDED at p*: no row labeling of either sector "
                       "half satisfies the realizability criterion"
                       if excluded else
                       "NOT excluded: some labeling satisfies the "
                       "criterion — empirical LM result contradicted"),
    }
    dest = "results/wp17b_gram_criterion_at_pstar.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(out["conclusion"])
    print("->", dest)


if __name__ == "__main__":
    main()
