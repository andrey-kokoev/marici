"""WP252: exact pilot background obstruction for the WP251 response."""

import json
from pathlib import Path

from sympy import Rational

ROOT = Path(__file__).resolve().parents[1]
PROV = json.loads((ROOT / "data/cms-mu-tau-background-pilots/provenance.json").read_text())
WP246 = json.loads((ROOT / "results/wp246_tau_channel_feasibility_gate.json").read_text())
WP251 = json.loads((ROOT / "results/wp251_mu_tau_object_match.json").read_text())

def q(value): return Rational(str(value))

def main():
    records = {r["process"]: r for r in PROV["records"]}
    scan = PROV["streaming_response"]
    dy = scan["DYJetsToLL_M-50"]
    tt = scan["TT"]
    dy_eff = q(dy["selected_sum_weight"]) / q(dy["sum_weight"])
    tt_eff = q(tt["selected_sum_weight"]) / q(tt["sum_weight"])
    dy_selected_pb = q(records["DYJetsToLL_M-50"]["cross_section_pb"]) * dy_eff
    tt_selected_pb = q(records["TT"]["cross_section_pb"]) * tt_eff
    signal_preselection_pb = q(WP246["feasibility"]["D"]["produced_tau_pairs_per_fb_per_unit_theta_squared"]) / 1000
    signal_selected_pb = signal_preselection_pb * q(WP251["acceptance_exact"])
    known_ratio = (dy_selected_pb + tt_selected_pb) / signal_selected_pb
    checks = {
        "campaign_common": all("RunIIFall15MiniAODv2" in r["url"] for r in PROV["records"]),
        "menu_joins_exact": scan["menu_status_length_mismatches"] == 0,
        "dy_and_top_have_selected_support": dy["selected"] > 0 and tt["selected"] > 0,
        "known_background_exceeds_signal": known_ratio > 1,
        "zero_W_not_promoted_to_zero_support": "censored" in scan["scope"],
        "qcd_gate_preserved": "data-driven" in PROV["missing_background"],
        "deliberate_zero_background_claim_fails": dy_selected_pb + tt_selected_pb != 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    result = {
        "work_package": "WP252",
        "pilot_efficiencies_exact": {"DY": str(dy_eff), "TT": str(tt_eff), "W_raw": "0/809"},
        "selected_cross_sections_pb_exact": {"DY": str(dy_selected_pb), "TT": str(tt_selected_pb), "signal_D_unit_mixing": str(signal_selected_pb)},
        "known_background_to_signal_ratio_exact": str(known_ratio),
        "known_background_to_signal_ratio_decimal": float(known_ratio),
        "classification": "source-local background pilots falsify rate-only source identification; full shape calibration remains open",
        "smallest_exact_falsifier": "one selected DY event and 38 selected top events give nonzero source-authorized background support",
        "remaining_instrument_gate": "full weighted background shapes, data-driven QCD fake control, uncertainties, mass-grid closure, and rank/power test",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp252_mu_tau_background_pilots.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
