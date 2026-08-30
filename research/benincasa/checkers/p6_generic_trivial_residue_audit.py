import json
from pathlib import Path

root = Path("research/benincasa/results")
paths = sorted(root.glob("p6-generic-trivial-*.json"))
records = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
assert len(records) == 18
assert {r["prime"] for r in records} == {2305843009213693951, 2305843009213693921}
assert {r["source_direction"] for r in records} == {"top", "wall1", "wall2"}
assert all(r["target_line"] == "trivial_algebraic" for r in records)
assert all(r["accepted_samples"] == 72 and r["verification_samples"] == 24 for r in records)
assert all(r["valuation"] == 0 and not r["logarithmic_residue_nonzero"] for r in records)

points = sorted({(r["prime"], *r["point_mod_p"]) for r in records})
assert len(points) == 6
for point in points:
    group = [r for r in records if (r["prime"], *r["point_mod_p"]) == point]
    assert len(group) == 3
    assert {r["source_direction"] for r in group} == {"top", "wall1", "wall2"}

packet = {
    "schema": "marici.p6_generic_trivial_residue_audit.v1",
    "primes": sorted({r["prime"] for r in records}),
    "generic_p6_points": [list(p) for p in points],
    "point_count": len(points),
    "source_directions": ["top", "wall1", "wall2"],
    "reconstruction_count": len(records),
    "heldout_samples_per_reconstruction": 24,
    "valuations": sorted({r["valuation"] for r in records}),
    "logarithmic_residue_nonzero_count": sum(r["logarithmic_residue_nonzero"] for r in records),
    "status": "multiprime evidence: generic P6 trivial-line resonance is unoccupied",
}
(root / "p6-generic-trivial-residue-audit.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
