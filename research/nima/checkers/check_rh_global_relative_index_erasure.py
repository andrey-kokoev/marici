import json
from pathlib import Path


right_inner_index = -1
left_reciprocal_index = 1
off_seam_pair = (right_inner_index, left_reciprocal_index)


def seam_incidence(k):
    return (-k, k)


assert off_seam_pair == seam_incidence(1)

# A support-sensitive carrier distinguishes the same integrated charge by
# locus. These are labels, not zero locations inferred by the checker.
seam_supported = {"normal_support": (0,), "charge": seam_incidence(1)}
bulk_supported = {"normal_support": (-1, 1), "charge": off_seam_pair}
assert seam_supported["charge"] == bulk_supported["charge"]
assert seam_supported["normal_support"] != bulk_supported["normal_support"]

result = {
    "right_inner_index": right_inner_index,
    "left_reciprocal_index": left_reciprocal_index,
    "off_seam_pair_charge": off_seam_pair,
    "natural_seam_incidence_of_one": seam_incidence(1),
    "global_relative_class": 0,
    "global_relative_index_detects_hostile": False,
    "seam_supported_model": seam_supported,
    "bulk_supported_model": bulk_supported,
    "support_sensitive_carrier_distinguishes_them": True,
    "verdict": "global relative charge erases a reciprocal off-seam pair; support must be retained before quotienting",
}

output = Path(__file__).parents[1] / "results" / "rh-global-relative-index-erasure.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

