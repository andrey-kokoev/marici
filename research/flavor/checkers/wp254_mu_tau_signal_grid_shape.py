"""WP254: exact finite-grid signal/background shape rank."""

import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[1]
GRID = json.loads((ROOT / "data/cms-mu-tau-signal-grid/provenance.json").read_text())
BG = json.loads((ROOT / "results/wp253_mu_tau_visible_mass_shape.json").read_text())

def main():
    response = GRID["response"]
    s130 = Matrix(response["130"]["raw_hist"])
    s140 = Matrix(response["140"]["raw_hist"])
    s160 = Matrix(response["160"]["raw_hist"])
    background = Matrix(BG["combined_background_template"])
    signal_matrix = Matrix.hstack(s130, s140, s160)
    full_matrix = Matrix.hstack(s130, s140, s160, background)
    signal_minor = Matrix([[s130[i], s140[i], s160[i]] for i in [0, 1, 2]]).det()
    full_minor = Matrix([[s130[i], s140[i], s160[i], background[i]] for i in [0, 1, 2, 5]]).det()
    rate_rank = Matrix([[sum(s130), sum(s140), sum(s160), sum(background)]]).rank()
    checks = {
        "all_menu_joins_exact": all(response[m]["menu_status_length_mismatches"] == 0 for m in ["130", "140", "160"]),
        "signal_grid_rank_three": signal_matrix.rank() == 3,
        "signal_background_rank_four": full_matrix.rank() == 4,
        "signal_minor_nonzero": signal_minor != 0,
        "full_minor_nonzero": full_minor != 0,
        "rate_projection_rank_one": rate_rank == 1,
        "tail_support_distinguishes_160": s130[4] == 0 and s140[4] == 0 and s160[4] == 3,
        "interpolation_authority_withheld": "not admitted" in response["scope"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    result = {
        "work_package": "WP254",
        "signal_templates": {m: response[m]["raw_hist"] for m in ["130", "140", "160"]},
        "background_template": [int(x) for x in background],
        "signal_grid_rank": int(signal_matrix.rank()),
        "signal_background_rank": int(full_matrix.rank()),
        "rate_projection_rank": int(rate_rank),
        "signal_minor_exact": str(signal_minor), "full_minor_exact": str(full_minor),
        "classification": "finite-grid physical/readout shape family is jointly faithful on three labelled mass pilots and background; rate projection is nonfaithful",
        "smallest_exact_falsifier": "all signal-grid 3x3 minors vanish or the 160-GeV tail support disappears under completion",
        "remaining_instrument_gate": "validate interpolation/transport to 133.774 and 151.287 GeV under uncertainties, full weighted samples, QCD, and finite-power rank",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp254_mu_tau_signal_grid_shape.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
