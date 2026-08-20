"""Projective Orlik--Solomon Hilbert series of five-site marked matroids."""
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-qg-intersection-matroid.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-projective-os.json"


def divide_by_one_plus_t(coefficients):
    # coefficients[k] = quotient[k] + quotient[k-1].
    quotient = []
    previous = 0
    for coefficient in coefficients:
        current = coefficient - previous
        quotient.append(current)
        previous = current
    assert quotient[-1] == 0
    return quotient[:-1]


source = json.loads(SOURCE.read_text())
packets = []
profiles = Counter()
for term in source["term_packets"]:
    m = term["geometric_marks"]
    circuits = [tuple(row["subset"]) for row in term["circuits"]]
    broken = {tuple(c[1:]) for c in circuits}  # fixed ground-set order
    central = [0] * (m + 1)
    nbc_sets = []
    for size in range(m + 1):
        for subset in itertools.combinations(range(m), size):
            chosen = set(subset)
            if any(set(bc) <= chosen for bc in broken):
                continue
            central[size] += 1
            nbc_sets.append(subset)
    # Essential rank five: central OS vanishes above degree five and has the
    # Euler factor (1+t) relative to the projective arrangement complement.
    assert all(value == 0 for value in central[6:])
    central = central[:6]
    projective = divide_by_one_plus_t(central)
    assert len(projective) == 5 and all(x >= 0 for x in projective)
    key = (m, tuple(central), tuple(projective))
    profiles[key] += 1
    packets.append({
        "term_index": term["term_index"],
        "geometric_marks": m,
        "central_os_betti": central,
        "projective_os_betti": projective,
        "central_nbc_count": sum(central),
        "projective_total_rank": sum(projective),
    })

profile_rows = [{
    "geometric_marks": key[0],
    "central_os_betti": key[1],
    "projective_os_betti": key[2],
    "projective_total_rank": sum(key[2]),
    "term_count": count,
    "cyclic_orbits": count // 5,
} for key, count in sorted(profiles.items())]
assert all(row["term_count"] % 5 == 0 for row in profile_rows)
packet = {
    "schema": "marici.benincasa.five_site_qg_projective_os.v1",
    "geometric_profile_count": len(profile_rows),
    "profile_census": profile_rows,
    "term_packets": packets,
    "occurrence_qualification": "Coincident source labels are not duplicated as geometric dlog generators. Their multiplicities remain external labelled occurrence data for subsequent coefficient and transition maps.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profiles": profile_rows}))
