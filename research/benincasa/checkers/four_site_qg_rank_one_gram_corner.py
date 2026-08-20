"""Two-normal inertia audit at a generic rank-one Gram corner."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-rank-one-gram-corner.json"

# G=diag(1,s,t), adj(G)=diag(st,t,s).  Coefficients of x1,x2,x3 have
# valuation vectors (1,1),(0,1),(1,0).  A loop around a normal flips exactly
# the coordinates whose valuation in that normal is odd.
valuations = {"x1": (1, 1), "x2": (0, 1), "x3": (1, 0)}
s_flip = {name: bool(v[0] % 2) for name, v in valuations.items()}
t_flip = {name: bool(v[1] % 2) for name, v in valuations.items()}
s_count = sum(s_flip.values())
t_count = sum(t_flip.values())
both_flip = {name: s_flip[name] != t_flip[name] for name in valuations}
both_count = sum(both_flip.values())

assert (s_count, t_count, both_count) == (2, 2, 2)
assert (-1) ** s_count == 1
assert (-1) ** t_count == 1
assert (-1) ** both_count == 1

packet = {
    "schema": "marici.benincasa.four_site_qg_rank_one_gram_corner.v1",
    "gram_normal_form": "G(s,t)=diag(1,s,t)",
    "adjugate": "adj(G)=diag(st,t,s)",
    "cover_normal_form": "W^2-st*x1^2-t*x2^2-s*x3^2=0",
    "coefficient_valuations": valuations,
    "s_deck_flips": [name for name, flip in s_flip.items() if flip],
    "t_deck_flips": [name for name, flip in t_flip.items() if flip],
    "combined_deck_flips": [name for name, flip in both_flip.items() if flip],
    "monodromy_s": 1,
    "monodromy_t": 1,
    "monodromy_st": 1,
    "commutator": 0,
    "support": ["s=0", "t=0", "s=t=0"],
    "support_classification": "existing labelled Gram-minor incidence corner",
    "qualification": "Inertia is closed; the supported corner costalk and extension are not computed here.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"flips": [s_count, t_count, both_count], "monodromies": [1, 1, 1], "commutator": 0}))
