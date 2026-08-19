"""Mechanism classification for the a_2 cancellation (marici.Figueiredo).

Follow-up to a2_factorization.py (which verifies, on all 22 rows,
    a_2 = (v+ Ho u)(v+ {C0,Ho} u) - (v+ Ho^2 u)(v+ C0 u)  exactly).

Three exact mechanism probes:

1. TELESCOPING THEOREM (exact, generic): for H_diag = diag(d0,d1,d2)
   and ANY Hermitian M,
       [H_diag, M]_ij  = (d_i - d_j) M_ij,
       {[H_diag,M], M}_ij = (d_i - d_j) (M^2)_ij,
   so the key identity  M_kp {C0,M}_kp = (M^2)_kp C0_kp  holds
   IDENTICALLY for every (k,p).  Verified symbolically with generic
   symbols.

2. GENERICITY SPLIT per texture: does the baseline identity
   a_2 = 0 survive replacing one sector's H by a generic real
   symmetric matrix?  Records which sector(s) carry the mechanism.
   (S38: survives generic Hd => one-sided, up-sector property.
    S43: fails both swaps => joint two-sector property.)

3. STRIPPED PHASE-SECTOR DIAGONALITY table for the four textures and
   the S48-style SANDWICH OBSTRUCTION check (v+ Ho u = v+ Ho^2 u = 0
   identically => a_2 = 0 trivially).

Output: research/flavor/results/a2_mechanisms.json
"""
import json
import sympy as sp
from harmonic_support import build, eps
from a2_factorization import split_phase, PHASE_POS


def telescoping_theorem():
    d = sp.symbols("d0:3", real=True)
    H = sp.diag(*d)
    m = sp.symbols("m0:9")
    M = sp.Matrix([[m[0], m[1], m[2]],
                   [m[3], m[4], m[5]],
                   [m[6], m[7], m[8]]])
    C = H * M - M * H
    AC = C * M + M * C
    M2 = M * M
    ok_comm = all(sp.simplify(C[i, j] - (d[i] - d[j]) * M[i, j]) == 0
                  for i in range(3) for j in range(3))
    ok_anti = all(sp.simplify(AC[i, j] - (d[i] - d[j]) * M2[i, j]) == 0
                  for i in range(3) for j in range(3))
    # hence M_kp AC_kp - M2_kp C_kp = 0 for all k,p
    ok_key = all(sp.simplify(M[k, p] * AC[k, p] - M2[k, p] * C[k, p]) == 0
                 for k in range(3) for p in range(3))
    return {"commutator_scaling_exact": ok_comm,
            "anticommutator_telescoping_exact": ok_anti,
            "key_identity_exact": ok_key}


def sandwich_a2_mats(Hu0, Hd0, sec, p, q, v):
    u = sp.Matrix.zeros(3, 1)
    u[p] = 1
    Ho = Hd0 if sec == "u" else Hu0
    C0 = Hu0 * Hd0 - Hd0 * Hu0
    vd = v.H
    s1 = sp.expand((vd * Ho * u)[0])
    s2 = sp.expand((vd * Ho * Ho * u)[0])
    s3 = sp.expand((vd * C0 * u)[0])
    s4 = sp.expand((vd * (C0 * Ho + Ho * C0) * u)[0])
    return sp.expand(s1 * s4 - s2 * s3), (s1, s2, s3, s4)


def texture_report(name):
    Yu, Yd = build(name)
    sec, pos = PHASE_POS[name]
    stripped, p, q, b = split_phase(Yu if sec == "u" else Yd, pos)
    Yu0 = stripped if sec == "u" else Yu
    Yd0 = stripped if sec == "d" else Yd
    Hu0, Hd0 = Yu0 * Yu0.H, Yd0 * Yd0.H
    v = b * stripped[:, q]
    Hs = stripped * stripped.H
    offdiag_zero = all(sp.simplify(Hs[i, j]) == 0
                       for i in range(3) for j in range(3) if i < j)
    a2_base, (s1, s2, s3, s4) = sandwich_a2_mats(Hu0, Hd0, sec, p, q, v)
    g = sp.symbols("g0:6", real=True)
    G = sp.Matrix([[g[0], g[3], g[4]],
                   [g[3], g[1], g[5]],
                   [g[4], g[5], g[2]]])
    # replace the NON-phase sector H (Ho) vs the stripped phase-sector H
    # one at a time with a generic real symmetric matrix
    if sec == "u":
        a2_genHo = sandwich_a2_mats(Hu0, G, sec, p, q, v)[0]
        a2_genHs = sandwich_a2_mats(G, Hd0, sec, p, q, v)[0]
    else:
        a2_genHo = sandwich_a2_mats(G, Hd0, sec, p, q, v)[0]
        a2_genHs = sandwich_a2_mats(Hu0, G, sec, p, q, v)[0]
    return {
        "phase_sector": sec,
        "phase_position_1based": [p + 1, q + 1],
        "baseline_a2_zero": sp.simplify(a2_base) == 0,
        "stripped_phase_sector_H_diagonal": offdiag_zero,
        "vHo_u_zero": sp.simplify(s1) == 0,
        "vHo2_u_zero": sp.simplify(s2) == 0,
        "vC0_u_zero": sp.simplify(s3) == 0,
        "vC0Ho_HoC0_u_zero": sp.simplify(s4) == 0,
        "survives_generic_nonphase_sector": sp.simplify(a2_genHo) == 0,
        "survives_generic_phase_sector": sp.simplify(a2_genHs) == 0,
    }


def main():
    out = {"telescoping_theorem": telescoping_theorem(),
           "textures": {}}
    print("telescoping:", out["telescoping_theorem"], flush=True)
    for name in ("S38", "S43", "S48", "S53"):
        out["textures"][name] = texture_report(name)
        print(name, out["textures"][name], flush=True)
    with open("results/a2_mechanisms.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
