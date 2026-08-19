"""WP5 exact audit: perfect matchings, determinant reality, gauge moves.

Source: arXiv:2607.27315v1.  All arithmetic exact (sympy symbolic).

For each of the four worked textures (S38, S43, S48, S53), in the paper's
standard gauge (all non-loop entries real positive, the phase on its
designated loop edge):

  1. enumerate perfect matchings per sector and verify their signed sum
     equals the determinant (already in nine_link_exact_checks; reused);
  2. locate the phase edge relative to every matching;
  3. compute arg det(Yu Yd) exactly as e^{2 i arg} = det/det-bar.

Additionally:

  4. GAUGE MOVE for Example I: the placed phase edge Yu_12 belongs to the
     unique up-sector matching, so det Yu is imaginary as placed.  Apply
     the exact diagonal rephasing that relocates the loop phase onto
     Yu_22 (a loop edge in NO matching) and verify: non-loop entries real,
     loop phase preserved at pi/2, and det Yu, det Yd both real.
  5. GROUPOID TRANSPORT: the S3^3 permutation of Example I used in
     nine_link_exact_checks preserves matching membership of the phase
     edge exactly (real sign factors only).

Output: research/flavor/results/wp5_matching_reality.json
"""
import json
import sympy as sp
from nine_link_exact_checks import (build_textures, perfect_matchings, sym,
                                    eps, I)

PHI = sp.pi / 2


def matching_report(name, Yu, Yd, phase_edge):
    out = {"sectors": {}}
    for sec, Y in (("u", Yu), ("d", Yd)):
        ms = perfect_matchings(Y)
        out["sectors"][sec] = {
            "n_matchings": len(ms),
            "sum_equals_det": sp.simplify(
                sum(m["term"] for m in ms) - Y.det()) == 0}
    pe = phase_edge
    in_any = False
    for sec, Y in (("u", Yu), ("d", Yd)):
        for m in perfect_matchings(Y):
            for i in range(3):
                if (sec, i + 1, m["permutation"][i]) == pe:
                    in_any = True
    out["phase_edge_in_any_matching"] = in_any
    det = sp.expand(Yu.det() * Yd.det())
    out["detYuYd_over_conjugate"] = str(sp.simplify(det / sp.conjugate(det)))
    return out


def gauge_move_example_I():
    """Relocate the loop phase Yu_12 -> Yu_22 by an exact rephasing."""
    T = build_textures()["example_I_S38"]
    Yu, Yd = T["Yu"], T["Yd"]
    # D_u = diag(1, e^{i pi/2}, 1): Yu -> Yu D_u^dagger sends
    # Yu_12 -> Yu_12 e^{-i pi/2} (real) and Yu_22 -> -i Yu_22 (phase).
    Du = sp.diag(1, sp.exp(I * PHI), 1)
    Yu2 = Yu * Du.conjugate().T
    detu, detd = sp.expand(Yu2.det()), sp.expand(Yd.det())
    # reality audit: ratio expr/conj(expr) == 1 means real
    def is_real(e):
        return sp.simplify(e / sp.conjugate(e)) == 1
    # loop monomial after the move: Yu_12 conj(Yu_22) Yd_22 conj(Yd_12)
    M = sp.expand(Yu2[0, 1] * sp.conjugate(Yu2[1, 1])
                  * Yd[1, 1] * sp.conjugate(Yd[0, 1]))
    rr = sp.expand_complex((M / sp.conjugate(M)).rewrite(sp.exp))
    return {
        "phase_edge_after": ["u", 2, 2],
        "Yu12_real_after": is_real(sp.expand(Yu2[0, 1])),
        "Yu22_arg_after": "pi/2 (carries -i)",
        "det_Yu_real_after": is_real(detu),
        "det_Yd_real_after": is_real(detd),
        "detYuYd_real_after": is_real(sp.expand(detu * detd)),
        "loop_phase_preserved": sp.simplify(rr + 1) == 0,  # e^{2 i arg} = -1
    }


def permutation_membership():
    """S3^3 image of Example I: phase-edge matching membership preserved."""
    T = build_textures()["example_I_S38"]
    Yu, Yd = T["Yu"], T["Yd"]
    P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Qu = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    Qd = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    YuP, YdP = P * Yu * Qu, P * Yd * Qd
    # locate the transported phase edge mechanically: find the entry of YuP
    # equal to the original phase entry Yu_12 (no hand-computed index maps)
    phase_entry = sp.expand(Yu[0, 1])
    locs = [(i + 1, j + 1) for i in range(3) for j in range(3)
            if sp.simplify(sp.expand(YuP[i, j]) - phase_entry) == 0]
    assert len(locs) == 1, f"phase entry not uniquely transported: {locs}"
    pe2 = ("u", locs[0][0], locs[0][1])

    def edge_in_any(Y, sec, edge):
        return any((sec, i + 1, m["permutation"][i]) == edge
                   for m in perfect_matchings(Y) for i in range(3))

    before = edge_in_any(Yu, "u", T["phase_edge"])
    after = edge_in_any(YuP, "u", pe2)
    return {"transported_phase_edge": list(pe2),
            "membership_before": before,
            "membership_after": after,
            "membership_preserved": before == after}


def main():
    textures = build_textures()
    out = {"textures": {}}
    for name, T in textures.items():
        out["textures"][name] = matching_report(
            name, T["Yu"], T["Yd"], T["phase_edge"])
        out["textures"][name]["placed_phase"] = str(T["placed_phase"])
    out["gauge_move_example_I"] = gauge_move_example_I()
    out["permutation_membership"] = permutation_membership()
    out["source_census_note"] = (
        "App. V: 5 of the 99 fixed-phase textures do NOT allow the phase "
        "to avoid all determinant matchings; matching-reality is not even "
        "chart-universal.")
    with open("results/wp5_matching_reality.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
