"""WP15b: paper-rule equivalence-class reduction of the nine-link
viable-fit ensemble (marici.Figueiredo).

Reproduces the App.-V.a class reduction of arXiv:2607.27315v1 on the
WP7 ensemble (research/flavor/results/wp7_ensemble.json):

  two texture fits T_a, T_b are identified iff there is a permutation
  in S3^Q x S3^{u^c} x S3^{d^c} mapping the support of T_a onto the
  support of T_b such that the absolute values of all nine permuted
  entries match within 5% and |phi| agrees within 0.1 deg.

The paper's numbers (free-phase 10-parameter scan): 2398 viable fits,
156 classes.  The WP7 ensemble is a free-phase multi-start LM sweep of
the same texture space (1592 supports with (3,3) in both matrices,
WP15a) at the same 17-observable chi2 (Tab. S2) and the same 3-sigma
viability cut, but sparser: 24-30 members per orbit x 24 starts.
The class count is the density-robust comparison target; the raw fit
count is scan-density dependent (the paper itself states its scan is
not complete), so it is reported but not treated as a falsifier.

Also audits per-orbit viability (best chi2 seen, any viable fit), which
decides whether entire texture orbits are excluded by the data.

Outputs: research/flavor/results/wp15b_class_reduction.json
"""
import itertools
import json
import math
from collections import defaultdict

from orbit_census import SLOTS, permute

ENTRY_TOL = 0.05            # paper: entries match to 5%
PHI_TOL = math.radians(0.1)  # paper: |phi| agrees to 0.1 deg

PERMS = list(itertools.permutations(range(3)))


def entries_of(member, log_mags):
    """Reconstruct {(sector, i, j): magnitude} from a WP7 record."""
    mu, md = member
    us = [s for k, s in enumerate(SLOTS) if mu & (1 << k)]
    ds = [s for k, s in enumerate(SLOTS) if md & (1 << k)]
    slots = [("u", s) for s in us] + [("d", s) for s in ds]
    return {(sec, s): math.exp(lm)
            for (sec, s), lm in zip(slots, log_mags)}


def support_key(entries):
    return frozenset(entries)


def permuted_entries(entries, pq, pu, pd):
    out = {}
    for (sec, (i, j)), m in entries.items():
        j2 = pu[j] if sec == "u" else pd[j]
        out[(sec, (pq[i], j2))] = m
    return out


def matches(ea, eb, phi_a, phi_b):
    """Paper's class-identification rule for one fit pair."""
    if abs(abs(phi_a) - abs(phi_b)) > PHI_TOL:
        return False
    # candidate permutations: those mapping support a onto support b
    sa, sb = support_key(ea), support_key(eb)
    for pq in PERMS:
        for pu in PERMS:
            for pd in PERMS:
                pe = permuted_entries(ea, pq, pu, pd)
                if support_key(pe) != sb:
                    continue
                if all(abs(pe[k] - eb[k]) <= ENTRY_TOL * eb[k] for k in eb):
                    return True
    return False


def main():
    d = json.load(open("results/wp7_ensemble.json"))
    fits = []
    for o in d["orbits"]:
        for m in o.get("viable_minima", []):
            fits.append({
                "orbit_index": o["orbit_index"],
                "member": tuple(m["member"]),
                "entries": entries_of(m["member"], m["log_mags"]),
                "phi": m["phi"],
                "phi_folded": m["phi_folded"],
                "chi2": m["chi2"],
            })
    print("viable fits loaded:", len(fits))

    # group by S3^3-only support orbit (the paper's class reduction
    # uses row/column permutations only, no sector exchange)
    def canon_s3(member):
        mu, md = member
        best = None
        for pq in PERMS:
            for pu in PERMS:
                for pd in PERMS:
                    a, b = permute(mu, md, pq, pu, pd)
                    if best is None or (a, b) < best:
                        best = (a, b)
        return best

    groups = defaultdict(list)
    for idx, f in enumerate(fits):
        groups[canon_s3(f["member"])].append(idx)

    parent = list(range(len(fits)))

    def find(a):
        while parent[a] != a:
            parent[parent[a]] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    n_pairs = 0
    for idxs in groups.values():
        for x in range(len(idxs)):
            for y in range(x + 1, len(idxs)):
                a, b = fits[idxs[x]], fits[idxs[y]]
                n_pairs += 1
                if matches(a["entries"], b["entries"], a["phi"], b["phi"]):
                    union(idxs[x], idxs[y])
    print("same-orbit fit pairs tested:", n_pairs)

    classes = defaultdict(list)
    for i in range(len(fits)):
        classes[find(i)].append(i)
    print("classes:", len(classes))

    # per-class summary: representative = min chi2 member
    rows = []
    for members in classes.values():
        rep = min(members, key=lambda i: fits[i]["chi2"])
        f = fits[rep]
        rows.append({
            "size": len(members),
            "orbit_index": f["orbit_index"],
            "chi2_min": f["chi2"],
            "phi_abs": abs(f["phi"]),
            "phi_folded": f["phi_folded"],
        })
    rows.sort(key=lambda r: (r["orbit_index"], r["chi2_min"]))

    # folded class-phase histogram at pi/8 multiples (paper Fig. 3)
    def bin22(x):
        return round(math.degrees(x) / 22.5) * 22.5
    hist_classes = defaultdict(int)
    for r in rows:
        hist_classes[bin22(r["phi_folded"])] += 1
    hist_fits = defaultdict(int)
    for f in fits:
        hist_fits[bin22(f["phi_folded"])] += 1

    # per-orbit viability audit
    per_orbit = []
    for o in d["orbits"]:
        per_orbit.append({
            "orbit_index": o["orbit_index"],
            "mask_u": o["mask_u"], "mask_d": o["mask_d"],
            "cycle_length": o["cycle_length"],
            "members_tried": len(o["members_tried"]),
            "escalated": o["escalated"],
            "viable_minima": len(o.get("viable_minima", [])),
            "best_chi2_overall": o.get("best_chi2_overall"),
        })

    out = {
        "purpose": "WP15b: paper-rule (S3^3, 5% entries, 0.1 deg phase) "
                   "class reduction of the WP7 viable-fit ensemble",
        "paper_targets": {"viable_fits": 2398, "classes": 156},
        "scan_density_note": "WP7 sweep: 24-30 members/orbit x 24 "
                             "starts; the paper states its own scan is "
                             "not complete. Raw fit counts are density "
                             "dependent; class count is the comparison "
                             "target.",
        "ensemble_fits": len(fits),
        "same_orbit_pairs_tested": n_pairs,
        "classes": len(rows),
        "class_phase_histogram_folded_deg":
            {str(k): hist_classes[k] for k in sorted(hist_classes)},
        "fit_phase_histogram_folded_deg":
            {str(k): hist_fits[k] for k in sorted(hist_fits)},
        "per_orbit_viability": per_orbit,
        "class_table": rows,
    }
    with open("results/wp15b_class_reduction.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("folded class histogram (deg):", dict(sorted(hist_classes.items())))
    print("folded fit histogram (deg):", dict(sorted(hist_fits.items())))
    for r in per_orbit:
        if r["viable_minima"] == 0:
            print("  NONVIABLE orbit", r["orbit_index"],
                  "u=", r["mask_u"], "d=", r["mask_d"],
                  "cycle", r["cycle_length"],
                  "best chi2:", r["best_chi2_overall"],
                  "escalated:", r["escalated"])


if __name__ == "__main__":
    main()
