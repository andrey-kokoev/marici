"""Exact source-normalized node-to-e6 comparison at (u,v)=(2,0)."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/benincasa/results/rank12-u2-v0-node-to-e6-gysin.json"

# In the p-chart
#   u=2+p, v=ps, a=2+pA, b=1+pB,
# the source form is
#   Omega111 = da db/(L1 L2 w).
# After multiplying by its forced Rees shift p, and restricting to p=0,
#   p Omega111 = dA dB/((B-1)(A+(s-1)/2)W).
# Put T=3-s-2A.  Then dA=-dT/2, L2|T=0=1 and W=+/-2T.
sheet_residues = (Fraction(-1, 4), Fraction(1, 4))

# Ordered anti-invariant generator tau=e_plus-e_minus.
tau_coefficient = sheet_residues[0]
assert sheet_residues == (tau_coefficient, -tau_coefficient)

# Frozen source bridge: g111_top -> e6/(8*(X1+X2)).
# At the center [E:X2:X3]=[2:0:1], X1=1 and X2=0.
x1_plus_x2 = Fraction(1)
e6_bridge = Fraction(1, 8) / x1_plus_x2

# The unique comparison making the source square commute.
node_to_e6 = e6_bridge / tau_coefficient
assert node_to_e6 == Fraction(-1, 2)
assert tau_coefficient * node_to_e6 == e6_bridge

packet = {
    "schema": "marici.benincasa.rank12_u2_v0_node_to_e6_gysin.v1",
    "center": {"u": 2, "v": 0, "a": 2, "b": 1},
    "p_chart": {
        "substitution": {
            "u": "2+p",
            "v": "p*s",
            "a": "2+p*A",
            "b": "1+p*B",
        },
        "T": "3-s-2*A",
        "exceptional_cover": "W^2=4*T^2",
        "ordered_sheets": ["W=+2*T", "W=-2*T"],
    },
    "source_form": "Omega111=da wedge db/(L1*L2*w)",
    "forced_rees_normalization": "p*Omega111",
    "conductor_restrictions": {"L1/p": "B-1", "L2/p": "1"},
    "ordered_sheet_residues": [str(q) for q in sheet_residues],
    "anti_invariant_generator": "tau=e_plus-e_minus",
    "specialization": "Sp(g111_top)=(-1/4)*tau",
    "frozen_bridge": "g111_top -> e6/(8*(X1+X2))",
    "bridge_at_center": "g111_top -> (1/8)*e6",
    "node_to_e6": "tau -> (-1/2)*e6",
    "commuting_square_checked": True,
    "deck_character_source": -1,
    "deck_character_target": -1,
    "scope": "source-normalized local de Rham/Gysin comparison at the labelled second center; no global Betti normalization claim",
    "classification": "existing soft-node coefficient line maps nontrivially to the existing e6 second-Rees line; no new carrier datum",
}

RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
