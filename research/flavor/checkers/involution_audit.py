"""Involution audit: which weak-basis invariants are fixed by phi -> pi-phi?

Responds to marici.Nima's scope correction (epistemic event
ev-000000000680): det[Hu,Hd] = 2iF sin(phi) establishes first-harmonic
dependence only for the CP-odd numerator.  The full physical invariant
map could still distinguish the two chart points phi and pi-phi through
CP-even invariants carrying cos(m phi).

For each of the four worked textures of arXiv:2607.27315v1 with the
placed phase generalized to z = e^{i phi}, compute EXACTLY (symbolic
Laurent polynomials in z):

  power sums   p_u_k = tr(Hu^k),  p_d_k = tr(Hd^k),  k = 1,2,3
  mixed        m11 = tr(Hu Hd), m21 = tr(Hu^2 Hd),
               m12 = tr(Hu Hd^2), m22 = tr(Hu^2 Hd^2)
  control      det[Hu, Hd]  (known: a_1 (z - z^{-1}))

and apply the involution sigma: z -> -z^{-1}  (phi -> pi - phi).
Report per invariant: fixed / changes (and the exact Laurent support).

The two-point fiber {phi, pi-phi} of Entries 1047/1048 is then asserted
only for the largest invariant submap actually fixed by sigma.

All arithmetic exact (sympy symbolic).  No floating point.

Output: research/flavor/results/involution_audit.json
"""
import json
import sympy as sp
from harmonic_support import build, laurent_coeffs, z

TEXTURES = ("S38", "S43", "S48", "S53")


def laurent(expr):
    """Laurent support + coefficient dict of a scalar expr in z."""
    return laurent_coeffs(expr)


def under_sigma(coeffs):
    """Apply z -> -z^-1 to a Laurent dict {m: coeff} and compare."""
    transformed = {}
    for m, c in coeffs.items():
        # z^m -> (-1)^m z^{-m}; coefficients are z-free real polynomials
        transformed.setdefault(-m, 0)
        transformed[-m] = sp.expand(transformed[-m] + (-1)**m * c)
    return {m: sp.expand(c) for m, c in transformed.items() if c != 0}


def coeffs_equal(c1, c2):
    keys = set(c1) | set(c2)
    return all(sp.simplify(c1.get(m, 0) - c2.get(m, 0)) == 0 for m in keys)


def analyze(name):
    Yu, Yd = build(name)
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    Hu2, Hd2 = Hu * Hu, Hd * Hd
    invariants = {
        "p_u_1": sp.trace(Hu), "p_u_2": sp.trace(Hu2),
        "p_u_3": sp.trace(Hu2 * Hu),
        "p_d_1": sp.trace(Hd), "p_d_2": sp.trace(Hd2),
        "p_d_3": sp.trace(Hd2 * Hd),
        "m11": sp.trace(Hu * Hd), "m21": sp.trace(Hu2 * Hd),
        "m12": sp.trace(Hu * Hd2), "m22": sp.trace(Hu2 * Hd2),
        "det_comm": (Hu * Hd - Hd * Hu).det(),
    }
    out = {}
    for key, expr in invariants.items():
        c = laurent(sp.expand(expr))
        cs = under_sigma(c)
        out[key] = {
            "laurent_support": sorted(c.keys()),
            "fixed_by_sigma": coeffs_equal(c, cs),
        }
        print(name, key, "support", sorted(c.keys()),
              "fixed:", out[key]["fixed_by_sigma"], flush=True)
    return out


def main():
    out = {"purpose": "exact phi -> pi-phi involution audit on a "
                      "ten-invariant set plus det-commutator control "
                      "(Nima's scope correction, ev-000000000680)",
           "textures": {}}
    for name in TEXTURES:
        out["textures"][name] = analyze(name)
    # summary: which invariants are fixed in ALL four charts
    allfixed = [k for k in next(iter(out["textures"].values()))
                if all(out["textures"][t][k]["fixed_by_sigma"]
                       for t in TEXTURES)]
    out["invariants_fixed_in_all_four_charts"] = allfixed
    with open("results/involution_audit.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("fixed in all four:", allfixed)


if __name__ == "__main__":
    main()
