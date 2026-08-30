"""WP15a: audit the paper's texture space against the exhaustive census
(marici.Figueiredo).

The paper's scan space (App. V.a of arXiv:2607.27315v1): pairs of
full-rank 3x3 matrices (Y_u, Y_d) with nine total nonzero entries,
split 4+5 / 5+4 / 6+3 / 3+6, entry (3,3) nonzero in BOTH matrices,
a single closed loop of 4 or 6 links.

The existing exhaustive census (orbit_census.py / orbit_census.json):
nine total links, full-rank sectors (perfect matching each), connected
combined nine-node graph (hence b1 = 1), modulo S3^3 x sector exchange:
6552 supports, 18 orbits.

This checker verifies the two automatic matches and computes the one
restrictive filter:

  1. splits: full rank forces >= 3 links per sector, so with nine
     total the split is automatically in {3+6, 4+5, 5+4, 6+3};
  2. loop length: the nine-node graph is bipartite between the three Q
     nodes and the six u^c/d^c nodes, so every cycle alternates Q nodes
     and has length 2 * (#Q nodes on cycle) in {4, 6} automatically;
  3. (3,3) in both: NOT automatic — count the sub-ensemble.

Reports: filtered support count, filtered orbit count (both mod
S3^3 x exchange and mod S3^3 alone, since the paper does not identify
sectors at texture level), and the per-orbit member weights the WP15b
scan must use.

All arithmetic exact combinatorics (no fitting).

Output: research/flavor/results/wp15a_texture_space_audit.json
"""
import itertools
import json
from collections import defaultdict

from orbit_census import (SLOTS, SLOT_INDEX, canonical, connected,
                          has_perfect_matching, permute, unique_cycle)

BIT33 = SLOT_INDEX[(2, 2)]  # the (3,3) entry, 1-based row/col 3


def main():
    perms = list(itertools.permutations(range(3)))
    masks = [m for m in range(512) if has_perfect_matching(m)]

    all_supports = []
    for mu in masks:
        for md in masks:
            if bin(mu).count("1") + bin(md).count("1") != 9:
                continue
            if not connected(mu, md):
                continue
            all_supports.append((mu, md))

    # sanity: split and cycle-length claims on the full census
    splits = defaultdict(int)
    cycle_lens = defaultdict(int)
    for mu, md in enumerate(all_supports):
        pass
    for mu, md in all_supports:
        splits[(bin(mu).count("1"), bin(md).count("1"))] += 1
        cycle_lens[len(unique_cycle(mu, md))] += 1

    # the paper's (3,3) filter
    filtered = [(mu, md) for mu, md in all_supports
                if (mu >> BIT33 & 1) and (md >> BIT33 & 1)]

    # orbit reduction, both conventions
    orb_ex = defaultdict(list)   # mod S3^3 x sector exchange (census convention)
    orb_s3 = defaultdict(list)   # mod S3^3 only (paper's texture-level convention)

    def canon_s3(mu, md):
        best = None
        for pq in perms:
            for pu in perms:
                for pd in perms:
                    a, b = permute(mu, md, pq, pu, pd)
                    if best is None or (a, b) < best:
                        best = (a, b)
        return best

    for mu, md in filtered:
        orb_ex[canonical(mu, md)].append((mu, md))
        orb_s3[canon_s3(mu, md)].append((mu, md))

    per_orbit = []
    for canon_key, members in sorted(orb_ex.items()):
        mu, md = canon_key
        cyc = unique_cycle(mu, md)
        per_orbit.append({
            "mask_u": mu,
            "mask_d": md,
            "split": [bin(mu).count("1"), bin(md).count("1")],
            "cycle_length": len(cyc),
            "filtered_members": len(members),
            "s3_orbits_inside": len({canon_s3(a, b) for a, b in members}),
        })

    out = {
        "purpose": "WP15a: the paper's App-V.a texture space as a "
                   "sub-ensemble of the exhaustive nine-link census",
        "census_supports": len(all_supports),
        "census_splits": {f"{a}+{b}": n for (a, b), n in sorted(splits.items())},
        "census_cycle_lengths": {str(k): v for k, v in sorted(cycle_lens.items())},
        "split_restriction_automatic": all(a + b == 9 and a >= 3 and b >= 3
                                           for (a, b) in splits),
        "loop_length_restriction_automatic": set(cycle_lens) <= {4, 6},
        "filtered_supports_33_in_both": len(filtered),
        "filtered_orbits_s3xexchange": len(orb_ex),
        "filtered_orbits_s3_only": len(orb_s3),
        "per_orbit_s3xexchange": per_orbit,
    }
    with open("results/wp15a_texture_space_audit.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("census supports:", len(all_supports),
          "| splits:", dict(splits),
          "| cycle lengths:", dict(cycle_lens))
    print("filtered (3,3)-in-both supports:", len(filtered))
    print("filtered orbits mod S3^3 x exchange:", len(orb_ex),
          "| mod S3^3 only:", len(orb_s3))
    for row in per_orbit:
        print("  orbit u={mask_u} d={mask_d} split={split} "
              "cycle={cycle_length} members={filtered_members} "
              "s3_orbits={s3_orbits_inside}".format(**row))


if __name__ == "__main__":
    main()
