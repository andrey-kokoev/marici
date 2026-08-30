"""WP253: exact visible-mass shape rank and rate-collapse obstruction."""

import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[1]
PROV = json.loads((ROOT / "data/cms-mu-tau-background-pilots/provenance.json").read_text())

def main():
    shape = PROV["visible_mass_shape"]
    signal = Matrix(shape["signal_140_raw"])
    background = Matrix([sum(x) for x in zip(shape["DY_raw"], shape["TT_raw"], shape["W_raw"])])
    shape_matrix = Matrix.hstack(signal, background)
    rate_matrix = Matrix([[sum(signal), sum(background)]])
    tail_signal = sum(shape["signal_140_raw"][4:])
    tail_background = sum(background[4:])
    checks = {
        "six_bins_frozen": len(shape["bins_GeV"]) == 7,
        "shape_response_rank_two": shape_matrix.rank() == 2,
        "rate_projection_rank_one": rate_matrix.rank() == 1,
        "tail_support_separates": tail_signal == 0 and tail_background == 6,
        "deliberate_proportionality_failure_nonzero": shape["signal_140_raw"][1] * int(background[0]) - shape["signal_140_raw"][0] * int(background[1]) != 0,
        "finite_pilot_scope_preserved": "finite-pilot" in shape["scope"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    result = {
        "work_package": "WP253",
        "signal_template": [int(x) for x in signal], "combined_background_template": [int(x) for x in background],
        "shape_rank": int(shape_matrix.rank()), "rate_projection_rank": int(rate_matrix.rank()),
        "smallest_support_separator": {"region": "visible mass >= 140 GeV", "signal": int(tail_signal), "background": int(tail_background)},
        "proportionality_minor": shape["signal_140_raw"][1] * int(background[0]) - shape["signal_140_raw"][0] * int(background[1]),
        "classification": "finite-pilot physical/readout shape separates 140-GeV signal from admitted simulated background while rate projection is nonfaithful",
        "smallest_exact_falsifier": "the visible-mass shape would fail if every 2x2 signal/background minor vanished",
        "remaining_instrument_gate": "weighted full-dataset shapes, QCD control, uncertainties, 130/160 signal columns, and two-source rank/power",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp253_mu_tau_visible_mass_shape.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
