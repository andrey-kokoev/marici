"""Toggle map for the second harmonic of det[Hu, Hd] (marici.Figueiredo).

Question left open by harmonic_support.py (ledger 1048): the four worked
textures of arXiv:2607.27315v1 all carry ONLY the first harmonic sin(phi) in
det[Yu Yu^dag, Yd Yd^dag].  Is first-harmonic purity forced by the connected
b1 = 1 topology, or is it a finer graph property?

Probe: add ONE extra real positive edge x at each zero position of the
texture (a "tenth edge", taking the graph to b1 = 2), recompute det C
EXACTLY as a Laurent polynomial in z = e^{i phi} with all magnitudes
symbolic, and record whether the second-harmonic coefficient a_2 stays
identically zero or becomes a nonzero polynomial.

Because a_2 is a polynomial in (eps, magnitudes, x), the eps power assigned
to the added edge does not affect identical vanishing; we use plain x.

Textures probed: S38 (phase in the up sector) and S43 (phase in the down
sector).  Baseline (no tenth edge) must reproduce support {1}.

All arithmetic exact (sympy symbolic).  No floating point.

Output: research/flavor/results/m2_toggle_map.json
"""
import json
import sympy as sp
from harmonic_support import build, laurent_coeffs, eps

x = sp.symbols("x", positive=True, real=True)


def a2_status(Yu, Yd):
    """Return (support, a2_is_zero) for det[Yu Yu^dag, Yd Yd^dag]."""
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    C = Hu * Hd - Hd * Hu
    coeffs = laurent_coeffs(C.det())
    a2 = sp.simplify(coeffs.get(2, 0))
    support = sorted({abs(m) for m in coeffs})
    return support, a2 == 0, str(sp.expand(coeffs.get(2, 0)))


def toggle(name):
    Yu0, Yd0 = build(name)
    base_support, base_a2_zero, _ = a2_status(Yu0, Yd0)
    rows = []
    for sec, Y0 in (("u", Yu0), ("d", Yd0)):
        zeros = [(i, j) for i in range(3) for j in range(3) if Y0[i, j] == 0]
        for (i, j) in zeros:
            Yu, Yd = Yu0.copy(), Yd0.copy()
            (Yu if sec == "u" else Yd)[i, j] = x
            support, a2_zero, a2_poly = a2_status(Yu, Yd)
            rows.append({"added_edge": [sec, i + 1, j + 1],
                         "harmonic_support_m": support,
                         "a2_identically_zero": a2_zero,
                         "a2_polynomial": None if a2_zero else a2_poly})
            print(name, sec, i + 1, j + 1,
                  "support", support, "a2_zero", a2_zero, flush=True)
    return {"baseline_support_m": base_support,
            "baseline_a2_zero": base_a2_zero,
            "toggles": rows}


def main():
    out = {"purpose": "second-harmonic toggle map: does a tenth edge create "
                      "an m=2 harmonic in det[Hu,Hd]?  Exact symbolic probe.",
           "note": "a_2 polynomial in (eps, magnitudes, x); identical "
                   "vanishing is independent of the eps power of x.",
           "textures": {}}
    for name in ("S38", "S43"):
        out["textures"][name] = toggle(name)
    with open("results/m2_toggle_map.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    for name, r in out["textures"].items():
        broken = [t["added_edge"] for t in r["toggles"]
                  if not t["a2_identically_zero"]]
        print(name, "baseline support", r["baseline_support_m"],
              "| a2 broken by adding:", broken)


if __name__ == "__main__":
    main()
