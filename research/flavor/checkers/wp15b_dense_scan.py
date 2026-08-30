"""WP15b-dense: full-member dense viable-fit scan of the nine-link
texture space (marici.Figueiredo).

Densification of the WP7 ensemble toward the paper's App.-V.a scan.
For each census orbit requested, sweep ALL members passing the paper's
(3,3)-in-both filter (WP15a) with the WP7 fitting pipeline (16 phase
anchors + --starts random starts per member), with no early stop and
no cross-member dedup: every viable minimum keeps its member
provenance, and the paper-rule class reduction (wp15b_class_reduction)
does the grouping afterward.

Usage:
  python checkers/wp15b_dense_scan.py --orbits 0,2,4 --workers 12

Output per orbit: research/flavor/results/wp15b_dense_orbit{XX}.json
"""
import argparse
import importlib.util
import itertools
import json
import math
import multiprocessing as mp
import time
from pathlib import Path

from orbit_census import SLOT_INDEX, permute, unique_cycle

BIT33 = SLOT_INDEX[(2, 2)]

# wp7_ensemble.py starts with a digit: load by path.
_spec = importlib.util.spec_from_file_location(
    "wp7_ensemble", str(Path(__file__).with_name("wp7_ensemble.py")))
wp7 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wp7)

CHI2_3SIGMA_7DOF = wp7.CHI2_3SIGMA_7DOF


def filtered_members(mask_u, mask_d):
    """All distinct S3^3 members with (3,3) nonzero in both matrices,
    best-fitting labelings first."""
    members = set()
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            for pd in itertools.permutations(range(3)):
                mu, md = permute(mask_u, mask_d, pq, pu, pd)
                if (mu >> BIT33 & 1) and (md >> BIT33 & 1):
                    members.add((mu, md))
    return sorted(members,
                  key=lambda t: wp7.member_score(*t), reverse=True)


def s3_orbits_of(mask_u, mask_d):
    """The paper scans textures without sector identification, so one
    census (exchange) orbit contributes its two S3^3-only orbits:
    the representative's and the sector-swapped one's (WP15a showed
    every census orbit splits into exactly two S3^3 orbits).  The
    swapped half has independent physics (up/down masses differ) and
    hence independent viability."""
    halves = [(mask_u, mask_d, False), (mask_d, mask_u, True)]
    out = []
    for mu, md, swapped in halves:
        out.append({"representative": [mu, md],
                    "sector_swapped": swapped,
                    "members": filtered_members(mu, md)})
    return out


def _fit_one(args):
    mu, md, starts, seed = args
    psec, pslot = wp7.paper_phase_edge(mu, md)
    minima, best = wp7.fit_member(mu, md, psec, pslot,
                                  n_starts=starts, seed=seed)
    for m in minima:
        m["member"] = [mu, md]
        m["phase_edge"] = [psec, pslot[0], pslot[1]]
    return {"member": [mu, md],
            "viable_minima": minima,
            "best_chi2": best["chi2"] if best else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orbits", type=str, default=None,
                    help="comma-separated census orbit indices; default "
                         "all 18 census orbits (viability of the "
                         "swapped half is independent and unknown)")
    ap.add_argument("--starts", type=int, default=8,
                    help="random starts per member beyond the 16 phase "
                         "anchors")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()

    census = json.load(open("results/orbit_census.json"))
    if args.orbits is None:
        orbit_ids = [o["orbit_index"] for o in census["orbits"]]
    else:
        orbit_ids = [int(x) for x in args.orbits.split(",")]
    # skip orbits already scanned (idempotent reruns)
    orbit_ids = [o for o in orbit_ids
                 if not Path(f"results/wp15b_dense_orbit{o:02d}.json")
                 .exists()]

    for oid in orbit_ids:
        orb = next(o for o in census["orbits"] if o["orbit_index"] == oid)
        t0 = time.time()
        halves_out = []
        for half in s3_orbits_of(orb["mask_u"], orb["mask_d"]):
            members = half["members"]
            jobs = [(mu, md, args.starts,
                     7000 + 1000 * oid + 100000 * half["sector_swapped"]
                     + k)
                    for k, (mu, md) in enumerate(members)]
            results = []
            with mp.Pool(args.workers) as pool:
                for r in pool.imap_unordered(_fit_one, jobs):
                    results.append(r)
                    if len(results) % 20 == 0:
                        print(f"  orbit {oid} swap={half['sector_swapped']}:"
                              f" {len(results)}/{len(members)} members, "
                              f"{time.time() - t0:.0f}s", flush=True)
            halves_out.append({
                "representative": half["representative"],
                "sector_swapped": half["sector_swapped"],
                "members_scanned": len(members),
                "viable_minima_total": sum(len(r["viable_minima"])
                                           for r in results),
                "best_chi2": min((r["best_chi2"] for r in results
                                  if r["best_chi2"] is not None),
                                 default=None),
                "member_results": results,
            })
        n_min = sum(h["viable_minima_total"] for h in halves_out)
        out = {
            "purpose": "WP15b dense full-member scan of one census "
                       "orbit, BOTH S3^3 halves (paper (3,3) filter; "
                       "no early stop; no cross-member dedup)",
            "orbit_index": oid,
            "mask_u": orb["mask_u"], "mask_d": orb["mask_d"],
            "cycle_length": orb["cycle_length"],
            "starts_per_member": 16 + args.starts,
            "members_scanned": sum(h["members_scanned"] for h in halves_out),
            "viable_minima_total": n_min,
            "best_chi2_overall": min((h["best_chi2"] for h in halves_out
                                      if h["best_chi2"] is not None),
                                     default=None),
            "wall_seconds": time.time() - t0,
            "s3_orbits": halves_out,
        }
        path = Path(f"results/wp15b_dense_orbit{oid:02d}.json")
        path.write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"orbit {oid}: {out['members_scanned']} members "
              f"(both S3^3 halves), {n_min} viable minima, best chi2 "
              f"{out['best_chi2_overall']}, {time.time() - t0:.0f}s "
              f"-> {path}", flush=True)


if __name__ == "__main__":
    main()
