#!/usr/bin/env python3
"""Exact puncture words for all positive kinematic chambers."""
import json
from fractions import Fraction as F
from pathlib import Path

R = Path(__file__).resolve().parents[3]

def word(x, y, z):
    E = x + y + z
    punctures = [(2*x, "2x"), (2*y, "2y"), (2*(x+y), "2(x+y)")]
    return [name for value, name in sorted(punctures, reverse=True) if value < E]

samples = {
    "triangle_x_less_y": (F(3), F(5), F(4)),
    "triangle_y_less_x": (F(5), F(3), F(4)),
    "x_dominant": (F(7), F(2), F(3)),
    "y_dominant": (F(2), F(7), F(3)),
    "z_dominant_x_less_y": (F(2), F(3), F(6)),
    "z_dominant_y_less_x": (F(3), F(2), F(6)),
}
words = {k: word(*v) for k, v in samples.items()}
expected = {
    "triangle_x_less_y": ["2y", "2x"],
    "triangle_y_less_x": ["2x", "2y"],
    "x_dominant": ["2y"],
    "y_dominant": ["2x"],
    "z_dominant_x_less_y": ["2(x+y)", "2y", "2x"],
    "z_dominant_y_less_x": ["2(x+y)", "2x", "2y"],
}
checks = {
    "all_chamber_words_exact": words == expected,
    "x_dominant_single_middle": len(words["x_dominant"]) == 1,
    "y_dominant_single_middle": len(words["y_dominant"]) == 1,
    "dominant_chambers_exchange": words["x_dominant"] == ["2y"] and words["y_dominant"] == ["2x"],
    "triangle_has_two_middle_factors": all(len(words[k]) == 2 for k in ("triangle_x_less_y", "triangle_y_less_x")),
    "z_dominant_has_top_and_both_middle": all(len(words[k]) == 3 for k in ("z_dominant_x_less_y", "z_dominant_y_less_x")),
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.four-kinematic-chamber-braid-words.v1",
    "passed": True,
    "lower_half_plane_puncture_words": words,
    "key_reduction": "x- and y-dominant chambers produce exchanged single-middle-puncture words",
    "missing_test": "lift the two single-middle braid factors to integral Picard-Lefschetz matrices and compare their relative action on the mixed state",
    "checks": checks,
}
p = R / "research/voevodsky/results/four_kinematic_chamber_braid_words.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "x_dominant": words["x_dominant"], "y_dominant": words["y_dominant"]}))
