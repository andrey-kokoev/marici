"""Supported conormal grades of five-site OS--occurrence attachments."""
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OS = ROOT / "research/benincasa/results/five-site-qg-projective-os.json"
KOSZUL = ROOT / "research/benincasa/results/five-site-qg-occurrence-koszul.json"
OUT = ROOT / "research/benincasa/results/five-site-qg-supported-conormal.json"

os_packet = json.loads(OS.read_text())
koszul_packet = json.loads(KOSZUL.read_text())
os_terms = {x["term_index"]: x for x in os_packet["term_packets"]}
koszul_terms = {x["term_index"]: x for x in koszul_packet["term_packets"]}
assert os_terms.keys() == koszul_terms.keys()

packets = []
profiles = Counter()
aggregate = Counter()
for index in sorted(os_terms):
    betti = os_terms[index]["projective_os_betti"]
    k = koszul_terms[index]["symbol_count"]
    conormal = [math.comb(k, j) for j in range(k + 1)]
    bigraded = [[b * c for c in conormal] for b in betti]
    for j, c in enumerate(conormal):
        aggregate[j] += sum(betti) * c
    key = (tuple(betti), k, tuple(conormal))
    profiles[key] += 1
    packets.append({
        "term_index": index,
        "projective_os_betti": betti,
        "soft_codimension": k,
        "conormal_tor_ranks": conormal,
        "bigraded_ranks": bigraded,
        "excess_tor": 0,
    })

profile_rows = [{"projective_os_betti": key[0], "soft_codimension": key[1],
                 "conormal_tor_ranks": key[2], "term_count": count}
                for key, count in sorted(profiles.items())]
packet = {
    "schema": "marici.benincasa.five_site_qg_supported_conormal.v1",
    "profile_count": len(profile_rows),
    "profile_census": profile_rows,
    "aggregate_conormal_degree_ranks": dict(sorted(aggregate.items())),
    "all_excess_tor_zero": True,
    "typing": "The only supported Tor is the exterior conormal algebra of the already declared regular soft ideal, tensored with the geometric projective OS carrier.",
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"profiles": len(profile_rows),
                  "aggregate": packet["aggregate_conormal_degree_ranks"],
                  "excess_tor": 0}))
