"""Exact WP627 Standard Model representation and anomaly reconstruction."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

reps = {
    "Q": (3, 2, F(1, 6)), "Hu": (1, 2, F(1, 2)),
    "Hd": (1, 2, F(1, 2)), "u": (3, 1, F(2, 3)),
    "d": (3, 1, F(-1, 3)), "Au": (3, 1, F(2, 3)),
    "Bu": (3, 1, F(2, 3)), "Ad": (3, 1, F(-1, 3)),
    "Bd": (3, 1, F(-1, 3)), "S": (1, 1, F(0)),
    "X": (1, 1, F(0)),
}

def ysum(*terms):
    """Terms are (sign, field); conjugated fields carry sign -1."""
    return sum((sign * reps[field][2] for sign, field in terms), F(0))

residuals = {
    "up_entrance": -reps["Q"][2] - reps["Hu"][2] + reps["Au"][2],
    "up_connector": ysum((-1, "Au"), (1, "S"), (1, "Bu")),
    "up_exit": ysum((-1, "Bu"), (1, "X"), (1, "u")),
    "down_entrance": ysum((-1, "Q"), (1, "Hd"), (1, "Ad")),
    "down_connector": ysum((-1, "Ad"), (1, "S"), (1, "Bd")),
    "down_exit": ysum((-1, "Bd"), (1, "X"), (1, "d")),
}

def vectorlike_anomalies(y):
    # A right-handed partner is represented by its left-handed conjugate.
    return {"su3_cubic": 1 - 1, "u1_cubic": y**3 + (-y)**3,
            "grav_u1": y + (-y), "su3sq_u1": y + (-y)}

anomalies = {name: vectorlike_anomalies(reps[name][2])
             for name in ("Au", "Bu", "Ad", "Bd")}

hostile_plain_hu = -reps["Q"][2] + reps["Hu"][2] + reps["Au"][2]
hostile_bu_down_y = -reps["Au"][2] + reps["Bd"][2]
checks = {
    "six_vertex_hypercharges_close": set(residuals.values()) == {F(0)},
    "both_stages_are_color_triplets": all(reps[x][0] == 3 for x in ("Au", "Bu", "Ad", "Bd")),
    "both_stages_are_weak_singlets": all(reps[x][1] == 1 for x in ("Au", "Bu", "Ad", "Bd")),
    "singlets_transport_sector_representation": reps["Au"] == reps["Bu"] and reps["Ad"] == reps["Bd"],
    "all_vectorlike_anomalies_cancel": all(set(a.values()) == {0} for a in anomalies.values()),
    "plain_up_doublet_is_rejected": hostile_plain_hu == 1,
    "down_type_second_up_stage_is_rejected": hostile_bu_down_y == -1,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP627", "status": "PASS", "checks": checks,
    "representations": {k: [c, w, str(y)] for k, (c, w, y) in reps.items()},
    "vertex_hypercharge_residuals": {k: str(v) for k, v in residuals.items()},
    "classification": "source-derived representation completion; neither selector nor instrument",
    "smallest_exact_falsifiers": {
        "plain_Hu_at_up_entrance": str(hostile_plain_hu),
        "down_type_Bu": str(hostile_bu_down_y),
    },
    "remaining_gates": ["kinetic normalization", "threshold status",
                        "complete RG closure", "one-scheme finite matching",
                        "calibrated physical instrument"],
}
(ROOT / "results" / "wp627_messenger_sm_representation_reconstruction.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

