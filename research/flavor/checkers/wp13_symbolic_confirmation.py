"""WP13 symbolic confirmation: exact (9 magnitude symbols) Laurent support of
det[H_u, H_d] for every (orbit-representative, cycle phase-edge) case
(marici.Figueiredo).

This upgrades the WP13 Fraction-PIT census (wp13_all_topology_census.py) to a
rigorous per-orbit theorem: for each of the 18 S3^3-plus-swap orbit
representatives and each edge of its unique cycle, compute det C = tr C^3/3
with 9 free positive magnitude symbols and z on the phase edge, and record
the exact Laurent support.  Orbit invariance (row/column permutations
conjugate H_u, H_d by permutation matrices and leave det C invariant; u<->d
swap maps case to case) then extends the result to all 6552 viable one-cycle
nine-link supports.

Cross-check: the symbolic class (first_harmonic vs identically_zero) must
match the exact rational census classification case by case.

Output: research/flavor/results/wp13_symbolic_confirmation.json
"""
import json
import sys
import time

import sympy as sp

sys.path.insert(0, "checkers")
from wp13_all_topology_census import (
    slots_of, has_perfect_matching, unique_cycle_edges, canonical_form,
    analyze_case, decode_cycle_edge,
)
from wp12_unoriented_pushforward_census import (
    build_symbolic, dagger, laurent_support,
)


def enumerate_orbit_cases():
    masks = range(512)
    pm = {m: (bin(m).count("1") in (3, 4, 5, 6)) and has_perfect_matching(m)
          for m in masks}
    orbits = {}
    for mu in masks:
        if not pm.get(mu):
            continue
        ku = bin(mu).count("1")
        for md in masks:
            if bin(md).count("1") != 9 - ku or not pm.get(md):
                continue
            cyc = unique_cycle_edges(mu, md)
            if cyc is None:
                continue
            orbits.setdefault(canonical_form(mu, md), (mu, md, cyc))
    cases = []
    for canon, (mu, md, cyc) in sorted(orbits.items()):
        for e in sorted(cyc, key=lambda f: tuple(sorted(f))):
            sector, slot = decode_cycle_edge(e)
            cases.append((mu, md, sector, slot, len(cyc)))
    return cases


def symbolic_class(mu, md, sector, slot):
    Yu, Yd = build_symbolic(mu, md, sector, slot)
    Hu = sp.expand(Yu * dagger(Yu))
    Hd = sp.expand(Yd * dagger(Yd))
    C = sp.expand(Hu * Hd - Hd * Hu)
    detC = sp.expand(sp.trace(C**3) / 3)
    coeffs, antisym = laurent_support(detC)
    support = sorted(coeffs)
    if not coeffs:
        cls = "identically_zero"
    elif support == [-1, 1]:
        cls = "first_harmonic"
    else:
        cls = "higher_harmonic"
    return {"support": support, "cp_antisym": antisym, "class": cls,
            "a1": str(sp.expand(coeffs.get(1, 0))),
            "a2": str(sp.expand(coeffs.get(2, 0))),
            "a3": str(sp.expand(coeffs.get(3, 0)))}


def main():
    t0 = time.time()
    cases = enumerate_orbit_cases()
    print(f"{len(cases)} (orbit, phase-edge) cases", flush=True)
    results = []
    mismatches = []
    class_hist = {}
    for k, (mu, md, sector, slot, clen) in enumerate(cases):
        sym = symbolic_class(mu, md, sector, slot)
        rat = analyze_case(mu, md, sector, slot)
        ok = (sym["class"] == rat["class"]
              and sym["support"] == [p for p in rat["support_a"] if p != 0]
              and sym["cp_antisym"])
        if not ok:
            mismatches.append({"member": [mu, md],
                               "phase_edge": [sector, *slot],
                               "symbolic": sym, "rational": rat})
        class_hist[sym["class"]] = class_hist.get(sym["class"], 0) + 1
        results.append({"member": [mu, md], "phase_edge": [sector, *slot],
                        "cycle_length": clen, "support": sym["support"],
                        "class": sym["class"], "cp_antisym": sym["cp_antisym"],
                        "a2": sym["a2"], "a3": sym["a3"]})
        print(f"[{k+1}/{len(cases)}] ({mu},{md}) {sector}{slot} -> "
              f"{sym['class']} {sym['support']} ({time.time()-t0:.0f}s)",
              flush=True)
    out = {
        "purpose": "WP13 symbolic confirmation: exact Laurent support of "
                   "det[Hu,Hd] with 9 free magnitude symbols for every "
                   "(orbit representative, cycle phase-edge) case; extends "
                   "to all 6552 viable supports by orbit invariance",
        "case_count": len(cases),
        "class_histogram": class_hist,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "no_higher_harmonics": class_hist.get("higher_harmonic", 0) == 0,
        "cases": results,
    }
    with open("results/wp13_symbolic_confirmation.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("class histogram:", class_hist)
    print("mismatches:", len(mismatches))
    print(f"elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
