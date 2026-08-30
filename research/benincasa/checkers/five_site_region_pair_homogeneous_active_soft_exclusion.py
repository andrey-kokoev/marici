import contextlib
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
with contextlib.redirect_stdout(io.StringIO()):
    import five_site_disjoint_region_pair_source_residue as source


def interval_packet(value):
    return {
        "exact": [str(value.lo), str(value.hi)],
        "decimal": [float(value.lo), float(value.hi)],
    }


records = []
expected_signs = [1, -1, 1, -1]

for soft_edge, expected_sign in zip(range(1, 5), expected_signs):
    # On the homogeneous physical slice, the five edge energies are the
    # Euclidean distances from the loop point to the five polygon vertices.
    edge_energies = []
    for vertex_index, vertex in enumerate(source.c):
        if vertex_index == soft_edge:
            edge_energies.append(source.I(0))
            continue
        displacement = source.vsub(source.c[soft_edge], vertex)
        edge_energies.append(source.sqrt_i(source.dot(displacement, displacement)))
    assert edge_energies[soft_edge].lo == edge_energies[soft_edge].hi == 0

    # Simultaneous vanishing of g_123 and g_125 requires
    # y_3+y_5=y_2+y_4 after eliminating the common site-energy scale.
    mismatch = edge_energies[2] + edge_energies[4] - edge_energies[1] - edge_energies[3]
    sign = 1 if mismatch.lo > 0 else -1 if mismatch.hi < 0 else 0
    assert sign == expected_sign

    records.append({
        "soft_edge_zero_based": soft_edge,
        "soft_edge_one_based": soft_edge + 1,
        "edge_energy_intervals": [interval_packet(value) for value in edge_energies],
        "active_wall_compatibility_mismatch": interval_packet(mismatch),
        "certified_sign": sign,
        "zero_excluded": True,
    })

packet = {
    "schema": "marici.five_site_region_pair_homogeneous_active_soft_exclusion.v1",
    "representative_active_walls": ["g_123", "g_125"],
    "compatibility_equation": "y_3+y_5-y_2-y_4=0",
    "homogeneous_slice": "edge energies are distances from the loop point to the five fixed polygon vertices",
    "records": records,
    "all_four_soft_endpoints_excluded": all(record["zero_excluded"] for record in records),
    "scope": "the homogeneous five-site physical slice; no claim about the dehomogeneous source family",
}

output = Path("research/benincasa/results/five-site-region-pair-homogeneous-active-soft-exclusion.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "all_four_soft_endpoints_excluded": packet["all_four_soft_endpoints_excluded"],
    "certified_signs": [record["certified_sign"] for record in records],
}, sort_keys=True))
