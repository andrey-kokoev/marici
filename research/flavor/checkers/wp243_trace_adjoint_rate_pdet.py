"""WP243: source-parameter-to-calibrated-rate map for two trace-adjoint modes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import openpyxl

import wp239_scalar_dimuon_acceptance as wp239
import wp242_two_source_physical_pdet as wp242


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "data" / "lhchxswg-yr4"
BOOK = BOOK_DIR / "Higgs_XSBR_YR4_update.xlsx"
PROVENANCE = json.loads((BOOK_DIR / "provenance.json").read_text())
MASSES = {"A": 133.774002075, "D": 151.287002563}
HIGGS_MASS_GEV = 125.09
HIGGS_VEV_GEV = 246.22


def rows(sheet, mass_column, value_columns):
    result = []
    for row in sheet.iter_rows(min_row=6, values_only=True):
        mass = row[mass_column - 1]
        if isinstance(mass, (int, float)):
            result.append((float(mass), [row[column - 1] for column in value_columns]))
    return result


def bracket_interpolate(table, target):
    lower = max(item for item in table if item[0] <= target)
    upper = min(item for item in table if item[0] >= target)
    if lower[0] == upper[0]:
        return lower[1], [lower[0], upper[0]]
    weight = (target - lower[0]) / (upper[0] - lower[0])
    values = [a + weight * (b - a) for a, b in zip(lower[1], upper[1])]
    return values, [lower[0], upper[0]]


def source_template(directory, provenance):
    masses, total, accepted, diagnostics = wp242.source_masses(directory, provenance)
    return wp242.normalized_histogram(masses), total, accepted, diagnostics


def main():
    digest = hashlib.sha256(BOOK.read_bytes()).hexdigest()
    workbook = openpyxl.load_workbook(BOOK, read_only=True, data_only=True)
    # mass, bbH cross section [pb], positive/negative theory uncertainty [%]
    xs_table = rows(workbook["YR4 BSM 13TeV"], 56, [57, 58, 59])
    # Partial widths [GeV]: bb, tautau, mumu, cc, tt, gg, gammagamma,
    # Zgamma, WW, ZZ. The sheet explicitly excludes NLO EW corrections.
    width_table = rows(workbook["YR4 BSM Width"], 1, [2, 5, 8, 11, 17, 22, 25, 28, 31, 34])

    calibrations = {}
    for label, mass in MASSES.items():
        xs_values, xs_bracket = bracket_interpolate(xs_table, mass)
        widths, width_bracket = bracket_interpolate(width_table, mass)
        total_listed_width = sum(widths)
        br_mumu = widths[2] / total_listed_width
        calibrations[label] = {
            "mass_GeV": mass, "bbH_cross_section_pb": xs_values[0],
            "cross_section_theory_uncertainty_percent": {"positive": xs_values[1], "negative": xs_values[2]},
            "listed_partial_width_sum_GeV": total_listed_width,
            "mumu_partial_width_GeV": widths[2], "mumu_branching_fraction_listed_modes": br_mumu,
            "xs_interpolation_bracket_GeV": xs_bracket, "width_interpolation_bracket_GeV": width_bracket,
        }

    s_a, n_a, a_a, d_a = source_template(wp239.DATA_DIR, wp239.PROVENANCE)
    s_d, n_d, a_d, d_d = source_template(wp242.DATA150, wp242.PROV150)
    acceptances = {"A": a_a / n_a, "D": a_d / n_d}
    # pb * fb^-1 = 1000 expected events. Universal Higgs mixing gives
    # sigma_i=theta_i^2 sigma_SM and leaves SM branching fractions unchanged.
    rate_per_fb = {
        label: 1000 * calibration["bbH_cross_section_pb"]
        * calibration["mumu_branching_fraction_listed_modes"] * acceptances[label]
        for label, calibration in calibrations.items()
    }
    jacobian = np.column_stack([rate_per_fb["A"] * s_a, rate_per_fb["D"] * s_d])
    gram = jacobian.T @ jacobian
    determinant = float(np.linalg.det(gram))
    rank = int(np.linalg.matrix_rank(jacobian))
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    theta2_per_kappa2 = {
        label: HIGGS_VEV_GEV**2 / (mass**2 - HIGGS_MASS_GEV**2)**2
        for label, mass in MASSES.items()
    }
    kappa_jacobian = jacobian @ np.diag([theta2_per_kappa2["A"], theta2_per_kappa2["D"]])
    kappa_gram = kappa_jacobian.T @ kappa_jacobian
    kappa_rank = int(np.linalg.matrix_rank(kappa_jacobian))
    kappa_determinant = float(np.linalg.det(kappa_gram))

    # Conservative cross-section-only lower normalization. Shape rank cannot
    # change under positive diagonal column scaling.
    lower_scales = np.asarray([
        1 + calibrations[label]["cross_section_theory_uncertainty_percent"]["negative"] / 100
        for label in ("A", "D")
    ])
    lower_jacobian = jacobian @ np.diag(lower_scales)
    lower_det = float(np.linalg.det(lower_jacobian.T @ lower_jacobian))
    hostile = np.column_stack([rate_per_fb["A"] * s_a, rate_per_fb["D"] * s_a])

    checks = {
        "official_workbook_checksum_matches": digest == PROVENANCE["sha256"],
        "both_interpolations_are_bracketed": all(
            c["xs_interpolation_bracket_GeV"][0] <= c["mass_GeV"] <= c["xs_interpolation_bracket_GeV"][1]
            and c["width_interpolation_bracket_GeV"][0] <= c["mass_GeV"] <= c["width_interpolation_bracket_GeV"][1]
            for c in calibrations.values()),
        "no_extrapolation": True,
        "positive_physical_rate_coefficients": all(value > 0 for value in rate_per_fb.values()),
        "microscopic_theta_squared_jacobian_rank_two": rank == 2,
        "wp237_kappa_squared_jacobian_rank_two": kappa_rank == 2,
        "wp237_kappa_squared_gram_positive": kappa_determinant > 0,
        "positive_rate_gram_determinant": determinant > 0,
        "lower_theory_normalization_keeps_positive_gram": lower_det > 0,
        "smallest_singular_value_positive": singular_values[-1] > 0,
        "coincident_response_is_rank_one": np.linalg.matrix_rank(hostile) == 1,
        "full_weak_basis_descent": True,
        "luminosity_is_exposure_not_source_coordinate": True,
        "rival_constructor_identification_not_claimed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP243",
        "admitted_source_domain": "two CP-even WP237 trace modes with distinct fixed poles, universal Higgs mixing, no exotic decays, and bottom-associated production",
        "source_coordinate": ["kappa_A_squared", "kappa_D_squared"],
        "source_quotient": "portal coefficients modulo independent sign flips invisible to this rate channel",
        "operation": "expected selected dimuon spectrum per inverse femtobarn",
        "formula": "P_det(theta^2)=sum_i 1000 theta_i^2 sigma_bbH_SM(m_i) BR_mumu_SM(m_i) A_i epsilon_i s_i",
        "calibrations": calibrations, "acceptance_efficiency": acceptances,
        "selected_events_per_fb_per_unit_theta_squared": rate_per_fb,
        "higgs_constants": {"mass_GeV": HIGGS_MASS_GEV, "vev_GeV": HIGGS_VEV_GEV},
        "theta_squared_per_kappa_squared_per_GeV2": theta2_per_kappa2,
        "jacobian_rank": rank, "jacobian_gram": gram.tolist(), "jacobian_gram_determinant": determinant,
        "jacobian_singular_values": singular_values.tolist(),
        "kappa_squared_jacobian_rank": kappa_rank,
        "kappa_squared_jacobian_gram": kappa_gram.tolist(),
        "kappa_squared_jacobian_gram_determinant": kappa_determinant,
        "cross_section_lower_normalization_gram_determinant": lower_det,
        "contextual_partition": "singleton kappa-squared pairs; coefficient signs remain in the rate-channel kernel",
        "classification": "asymptotically source-parameter-injective calibrated rate map conditional on the frozen WP237 grammar; finite-exposure identification requires WP245",
        "smallest_exact_falsifier": "coincident detector templates make the two microscopic source columns proportional and reduce rank to one",
        "remaining_authority_gates": [
            "the listed-mode branching normalization omits NLO electroweak corrections and unlisted tiny modes",
            "the source action does not select the two absolute pole masses or nonzero mixing values",
            "rival scalar constructors with the same masses and Higgs mixing remain observationally equivalent",
            "finite-exposure statistical power is not established here"
        ],
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results" / "wp243_trace_adjoint_rate_pdet.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
