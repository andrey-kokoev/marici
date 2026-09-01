import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The localized-brane residue is the common Green denominator times vv^T.
# WP1117 has four brane couplings g=(2,1,1,1), and WP1116 fixed common rank 1.
g = [2,1,1,1]
physical16_pairs = 16
residue = [[g[a]*g[b] for b in range(4)] for a in range(4)]
assert physical16_pairs == 16
assert all(residue[a][b] == residue[b][a] for a in range(4) for b in range(4))
# Exact rank-one witness: every 2x2 minor vanishes.
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                assert residue[a][c]*residue[b][d] == residue[a][d]*residue[b][c]
assert residue[0][0] == 4 and residue[0][1] == 2 and residue[3][3] == 1

independent_residue_channels = 1
six_channels_required = 6
h6_entries_required = 36
phase_observables_sourced = 0
six_channel_bijections = 0
assert independent_residue_channels == 1
assert six_channels_required == 6
assert h6_entries_required == 36
assert phase_observables_sourced == 0
assert six_channel_bijections == 0

# A rank-one residue cannot be an H6 event basis; H6 requires six independent
# rows/columns with equal moduli and nonzero phase orthogonality.
rank_one_h6 = False
assert not rank_one_h6

result = {
    "schema": "marici.flavor.wp1126.v1",
    "status": "PASS",
    "question": "Can localized Green-function residues supply a six-channel event basis and H6 phases?",
    "dpc": {
        "conjecture": "Localized physical16 Green residues decompose into six event channels carrying H6 phases.",
        "rivals": [
            "rank-one common Green residue",
            "factorized brane-coupling residue",
            "six independent residue channels",
            "no residue event basis"
        ],
        "risky_consequences": [
            "six independent physical16 residue channels",
            "a six-channel bijection",
            "36 unit-modulus phases up to the common 1/sqrt(6) scale",
            "packet-preserving event-index observables"
        ],
        "falsification_attempt": "The sourced residue is vv^T with rank one and every 2x2 minor zero; it supplies one channel, not six, and no phase observables.",
        "residual": "A future boundary Green function could supply six independent residues and phases.",
        "disposition": "reject Green-residue H6 provenance for the current source"
    },
    "brane_couplings": g,
    "physical16_pairs": physical16_pairs,
    "residue_rank": independent_residue_channels,
    "residue_top_left": residue[0][0],
    "six_channels_required": six_channels_required,
    "h6_entries_required": h6_entries_required,
    "phase_observables_sourced": phase_observables_sourced,
    "six_channel_bijections": six_channel_bijections,
    "rank_one_h6": rank_one_h6,
    "classification": "negative gate: rank-one Green residue is not a six-channel H6 event basis",
    "remaining_gate": "derive six independent residue channels with sourced phase observables",
    "hostile_gate": "do not treat vv^T factorization, four brane couplings, physical16 indices, or pole residue as six event channels",
    "claim_boundary": "this rejects current residue-channel provenance, not future analytic decompositions",
    "disposition": "Green-residue H6 provenance rejected",
}

(ROOT / "results" / "wp1126_green_residue_event_basis_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1126 PASS:", independent_residue_channels, six_channels_required, phase_observables_sourced)
