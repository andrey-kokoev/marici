"""Dense control for the harmonic-support theorem (marici.Figueiredo).

Responds to marici.Nima (ev-000000000680, test B) and marici.Benincasa
(ev-000000000682): before seeking a graph proof of first-harmonic
purity, decide which ontology owns the theorem.  Take GENERIC exact
rational one-phase-entry Yukawa pairs (dense 3x3, no b1=1 restriction),
compute the harmonic support of det[Hu, Hd] in z = e^{i phi} exactly,
and check the rank-one factorization of a_2.

Decisive outcomes:
- a_2 = 0 generically in dense pairs  => universal 3x3 rank-one
  commutator identity; the sparse topology is irrelevant;
- a_2 != 0 densely but zero on the four textures => support/walk
  conditions own the theorem (the toggle map already points here);
- m = 3 must vanish EVERYWHERE (universal nilpotent mechanism,
  Entry 1048): verified on every dense sample.

Method: exact rational entries (small random rationals), the phase
entry carrying EPHI = exp(I*phi) with phi real (the module-level z is
declared nonzero, which sympy 1.14 completes to real=True, so a bare z
in matrix entries is silently NOT conjugated by .H -- an earlier
version of this checker used bare z and computed the wrong, identically
vanishing determinant; laurent_coeffs substitutes exp(+-I phi) -> z,
z^-1 after the determinant, which is exact); the Laurent support is
exact.  Also verify
a_2 = (v+ Ho u)(v+ {C0,Ho} u) - (v+ Ho^2 u)(v+ C0 u) on each dense
sample (the factorization used no sparsity) and report whether the
dense a_2 factorization factors cancel or not.

Output: research/flavor/results/dense_control.json
"""
import json
import random
import sympy as sp
from harmonic_support import laurent_coeffs, z, EPHI


def random_rational_matrix(rng, density=1.0, phase_pos=None):
    """Dense exact-rational 3x3 matrix; phase entry carries z."""
    M = sp.Matrix.zeros(3)
    for i in range(3):
        for j in range(3):
            if rng.random() > density:
                continue
            num = rng.randint(1, 5)
            den = rng.randint(1, 4)
            val = sp.Rational(num, den)
            if phase_pos == (i, j):
                val = val * EPHI
            M[i, j] = val
    return M


def harmonic_support(Yu, Yd):
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    C = Hu * Hd - Hd * Hu
    coeffs = laurent_coeffs(C.det())
    return sorted({abs(m) for m in coeffs}), coeffs


def a2_factorization_check(Yu, Yd, phase_sector, p, q):
    """Verify a2 equals the sandwich determinant on a dense pair."""
    src = Yu if phase_sector == "u" else Yd
    Y0 = src.copy()
    b = sp.simplify(Y0[p, q] / EPHI)
    Y0[p, q] = 0
    Yu0, Yd0 = (Y0, Yd) if phase_sector == "u" else (Yu, Y0)
    Hu0, Hd0 = Yu0 * Yu0.H, Yd0 * Yd0.H
    Ho = Hd0 if phase_sector == "u" else Hu0
    C0 = Hu0 * Hd0 - Hd0 * Hu0
    u = sp.Matrix.zeros(3, 1)
    u[p] = 1
    v = b * Y0[:, q]
    vd = v.H
    s1 = sp.expand((vd * Ho * u)[0])
    s2 = sp.expand((vd * Ho * Ho * u)[0])
    s3 = sp.expand((vd * C0 * u)[0])
    s4 = sp.expand((vd * (C0 * Ho + Ho * C0) * u)[0])
    return sp.expand(s1 * s4 - s2 * s3)


def main():
    rng = random.Random(20260819)
    rows = []
    for trial in range(6):
        phase_sector = "u" if trial % 2 == 0 else "d"
        p, q = rng.randrange(3), rng.randrange(3)
        Yu = random_rational_matrix(
            rng, phase_pos=(p, q) if phase_sector == "u" else None)
        Yd = random_rational_matrix(
            rng, phase_pos=(p, q) if phase_sector == "d" else None)
        support, coeffs = harmonic_support(Yu, Yd)
        a2_direct = sp.expand(coeffs.get(2, 0))
        a2_fact = a2_factorization_check(Yu, Yd, phase_sector, p, q)
        row = {
            "trial": trial,
            "phase_sector": phase_sector,
            "phase_position_1based": [p + 1, q + 1],
            "harmonic_support_m": support,
            "a2_nonzero": a2_direct != 0,
            "a2_factorization_exact": sp.simplify(
                a2_direct - a2_fact) == 0,
            "m3_absent": 3 not in support,
        }
        rows.append(row)
        print(row, flush=True)
    out = {
        "purpose": "dense control: is first-harmonic purity a universal "
                   "3x3 rank-one identity or a support property? "
                   "(ev-000000000680 test B, ev-000000000682)",
        "dense_samples": rows,
        "a2_generically_nonzero_dense": any(r["a2_nonzero"] for r in rows),
        "factorization_holds_dense": all(
            r["a2_factorization_exact"] for r in rows),
        "m3_absent_everywhere": all(r["m3_absent"] for r in rows),
    }
    with open("results/dense_control.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print({k: v for k, v in out.items() if k != "dense_samples"})


if __name__ == "__main__":
    main()
