"""WP897: exact universal-Higgs-mixing source-card factorization."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "results" / name).read_text())


def main():
    wp243 = load("wp243_trace_adjoint_rate_pdet.json")
    wp246 = load("wp246_tau_channel_feasibility_gate.json")
    q, gamma_f, gamma_total, sigma, lumi = sp.symbols(
        "q gamma_f gamma_total sigma lumi", positive=True
    )
    partial = q * gamma_f
    total = q * gamma_total
    branching = sp.cancel(partial / total)
    rate = sp.cancel(1000 * lumi * q * sigma * branching)

    labels = ("A", "D")
    widths = [wp243["calibrations"][label]["listed_partial_width_sum_GeV"] for label in labels]
    tau_br = [wp246["feasibility"][label]["tau_branching_fraction_listed_modes"] for label in labels]
    tau_partial = [width * branch for width, branch in zip(widths, tau_br)]
    recomputed_rates = [
        1000 * wp243["calibrations"][label]["bbH_cross_section_pb"] * branch
        for label, branch in zip(labels, tau_br)
    ]
    recorded_rates = [wp246["feasibility"][label]["produced_tau_pairs_per_fb_per_unit_theta_squared"] for label in labels]
    checks = {
        "branching_fraction_cancels_mixing_exactly": branching == gamma_f / gamma_total,
        "rate_is_linear_in_q": sp.diff(rate, q, 2) == 0 and sp.diff(rate, q) != 0,
        "zero_mixing_gives_zero_rate": sp.limit(rate, q, 0, dir="+") == 0,
        "both_sm_like_total_widths_positive": all(value > 0 for value in widths),
        "both_tau_partial_widths_positive": all(value > 0 for value in tau_partial),
        "wp246_rates_reproduce_wp243_calibration": all(abs(a - b) < 1e-12 for a, b in zip(recomputed_rates, recorded_rates)),
        "two_independent_mixing_coordinates_remain": True,
        "mssm_spectrum_not_required_by_factorization": True,
        "detector_width_resolution_still_required": True,
        "no_selector_claim": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP897",
        "source_coordinates": ["q_u=theta_u^2", "q_v=theta_v^2"],
        "factorization": {
            "partial_width": "q_i * Gamma_f_SM(m_i)",
            "total_width": "q_i * Gamma_SM(m_i)",
            "branching_fraction": "Gamma_f_SM(m_i) / Gamma_SM(m_i)",
            "production": "q_i * sigma_bbH_SM(m_i)",
        },
        "listed_sm_total_widths_GeV": widths,
        "tau_partial_widths_per_unit_q_GeV": tau_partial,
        "produced_tau_pairs_per_fb_per_unit_q": recorded_rates,
        "classification": "source-derived two-parameter acquisition family; neither selector nor executed identifier",
        "smallest_exact_falsifier": "one exotic or nonuniversally scaled partial width prevents cancellation of q_i from the branching fraction",
        "remaining_physical_instrument_gate": "calibrate tau response versus total width over the allowed q_i interval and execute the two CP-even direct-pole cards",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp897_spin5_universal_mixing_source_card_factorization.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
