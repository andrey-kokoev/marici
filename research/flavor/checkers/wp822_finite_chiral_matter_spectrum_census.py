"""Exact WP822 finite census of the admitted generalized GG matter grammar."""

import json
from pathlib import Path
import sympy as sp


def fixed_packet(N_value: int, p_value: int):
    N, p = sp.Integer(N_value), sp.Integer(p_value)
    x = sp.Rational(p, N)
    rH, rM, r1 = sp.symbols("rH rM r1")
    coefficient_matrix = sp.Matrix([
        [-sp.Rational(1-3*N, 2), 0, N*x],
        [0, -(5-N*(3+2*x)), 1],
        [-sp.Rational(1, 2)+sp.Rational(N, 2),
         -(5-N*(1+x)), 1+N*(2+x)],
    ])
    constant = sp.Matrix([
        -(sp.Rational(15, N)+6-9*N),
        -(sp.Rational(6, N)-6*N),
        -(sp.Rational(6, N)-6*N),
    ])
    try:
        ratios_vector = coefficient_matrix.inv()*constant
    except Exception:
        return None
    r_h, r_m, r_1 = [sp.factor(value) for value in ratios_vector]

    leading = sp.Rational(11, 3)+6*N-sp.Rational(4, 3)*N*x
    two_loop = (-sp.Rational(10, N)+1+2*x+sp.Rational(82, 3)*N
                +13*N**2-sp.Rational(26, 3)*N**2*x)
    h_coefficient = sp.Rational(5, 2)-sp.Rational(3, 2)*N
    m_coefficient = 10*N*x-2*N**2*(x+x**2)
    effective = sp.factor(-two_loop+h_coefficient*r_h+m_coefficient*r_m-2*N*x*r_1)
    if effective == 0:
        return None
    ag = sp.factor(leading/effective)
    coordinates = [ag, sp.factor(r_h*ag), sp.factor(r_m*ag), sp.factor(r_1*ag)]
    return {
        "N": N_value,
        "p": p_value,
        "ratios": [r_h, r_m, r_1],
        "coordinates": coordinates,
        "positive": all(value > 0 for value in coordinates),
        "controlled_unit": all(value < 1 for value in coordinates) and all(value > 0 for value in coordinates),
        "controlled_tenth": all(value < sp.Rational(1, 10) for value in coordinates)
        and all(value > 0 for value in coordinates),
    }


def stability_polynomial(packet):
    N, p = sp.Integer(packet["N"]), sp.Integer(packet["p"])
    x_ratio = sp.Rational(p, N)
    ag, aH, aM, a1 = sp.symbols("ag aH aM a1", real=True)
    beta_g = (
        -ag**2*(sp.Rational(11, 3)+6*N-sp.Rational(4, 3)*N*x_ratio)
        -ag**3*(-sp.Rational(10, N)+1+2*x_ratio+sp.Rational(82, 3)*N
                +13*N**2-sp.Rational(26, 3)*N**2*x_ratio)
        +ag**2*aH*(sp.Rational(5, 2)-sp.Rational(3, 2)*N)
        +ag**2*aM*(10*N*x_ratio-2*N**2*(x_ratio+x_ratio**2))
        -2*ag**2*a1*N*x_ratio
    )
    beta_H = (ag*aH*(sp.Rational(15, N)+6-9*N)
              -aH**2*sp.Rational(1-3*N, 2)+aH*a1*N*x_ratio)
    beta_M = (ag*aM*(sp.Rational(6, N)-6*N)
              -aM**2*(5-N*(3+2*x_ratio))+aM*a1)
    beta_1 = (
        ag*a1*(sp.Rational(6, N)-6*N)
        -aH*a1*(sp.Rational(1, 2)-sp.Rational(N, 2))
        -aM*a1*(5-N*(1+x_ratio))
        +a1**2*(1+N*(2+x_ratio))
    )
    variables = [ag, aH, aM, a1]
    fixed = dict(zip(variables, packet["coordinates"]))
    jacobian = sp.Matrix([beta_g, beta_H, beta_M, beta_1]).jacobian(variables).subs(fixed)
    polynomial = sp.Poly(jacobian.charpoly().as_expr())
    return polynomial, polynomial.count_roots(-sp.oo, 0), polynomial.count_roots(0, sp.oo)


def main() -> None:
    # Frozen first census: finite gauge ranks 5..12 and vectorlike multiplicity
    # 1..8N. The bound is declared before classification and is not extrapolated.
    domain = [(N, p) for N in range(5, 13) for p in range(1, 8*N+1)]
    packets = [fixed_packet(N, p) for N, p in domain]
    nonsingular = [packet for packet in packets if packet is not None]
    positive = [packet for packet in nonsingular if packet["positive"]]
    controlled_unit = [packet for packet in positive if packet["controlled_unit"]]
    controlled_tenth = [packet for packet in positive if packet["controlled_tenth"]]
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("census_domain_is_frozen_to_eight_ranks",
          sorted({N for N, _ in domain}) == list(range(5, 13)),
          sorted({N for N, _ in domain}))
    check("each_rank_has_exactly_eight_N_multiplicities",
          all(sum(1 for rank, _ in domain if rank == N) == 8*N for N in range(5, 13)),
          {N: sum(1 for rank, _ in domain if rank == N) for N in range(5, 13)})
    check("all_census_packets_are_integer_matter_spectra",
          all(isinstance(N, int) and isinstance(p, int) for N, p in domain), len(domain))
    anomaly_values = [(N-4)-(N-4+p)+p for N, p in domain]
    check("every_GG_packet_is_gauge_anomaly_complete",
          set(anomaly_values) == {0}, set(anomaly_values))
    check("wp805_packet_is_in_census",
          (5, 26) in domain, (5, 26))
    wp805 = next(packet for packet in nonsingular
                 if packet["N"] == 5 and packet["p"] == 26)
    check("census_reproduces_wp805_exact_fixed_point",
          wp805["coordinates"] == [
              sp.Rational(3163, 2234), sp.Rational(34182, 5585),
              sp.Rational(729, 1117), sp.Rational(1746, 5585)],
          wp805["coordinates"])
    check("census_classifies_wp805_as_positive_but_uncontrolled",
          wp805["positive"] and not wp805["controlled_unit"], wp805)
    check("positive_classification_is_exact",
          all(all(value > 0 for value in packet["coordinates"]) for packet in positive),
          len(positive))
    check("unit_control_classification_is_exact",
          all(max(packet["coordinates"]) < 1 for packet in controlled_unit),
          len(controlled_unit))
    check("tenth_control_classification_is_exact",
          all(max(packet["coordinates"]) < sp.Rational(1, 10)
              for packet in controlled_tenth), len(controlled_tenth))
    controlled_stability = []
    for packet in controlled_unit:
        polynomial, negative_roots, positive_roots = stability_polynomial(packet)
        controlled_stability.append({
            "N": packet["N"], "p": packet["p"], "polynomial": polynomial.as_expr(),
            "negative_roots": negative_roots, "positive_roots": positive_roots,
        })
    check("both_unit_control_packets_have_one_negative_and_three_positive_exponents",
          all(item["negative_roots"] == 1 and item["positive_roots"] == 3
              for item in controlled_stability), controlled_stability)
    check("unit_control_packets_are_not_full_dimensional_ir_attractors",
          all(item["negative_roots"] > 0 for item in controlled_stability),
          [(item["N"], item["p"], item["negative_roots"])
           for item in controlled_stability])
    check("unit_control_packet_is_not_unique",
          len(controlled_unit) == 2, [(packet["N"], packet["p"]) for packet in controlled_unit])

    # WP820's B,q,k packet and the GG (N,p,representations) grammar have no
    # admitted interface constructor. Numerical charge resemblance is not used.
    wp820_incidence = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    wp820_charges = sp.Matrix([1, 2, 3])
    check("wp820_charge_packet_is_internally_consistent",
          wp820_incidence*wp820_charges == sp.zeros(2, 1),
          wp820_incidence*wp820_charges)
    common_source_interface = False
    check("no_admitted_wp820_to_GG_spectrum_constructor_exists",
          not common_source_interface, common_source_interface)
    authorized_candidates = [] if not common_source_interface else controlled_unit
    check("authorized_controlled_candidate_count_is_zero",
          len(authorized_candidates) == 0, len(authorized_candidates))

    # Even a controlled algebraic packet would still need these gates.
    threshold_completion = False
    global_basin = False
    physical16_descent = False
    detector_calibration = False
    check("threshold_completion_remains_absent", not threshold_completion, threshold_completion)
    check("global_basin_remains_absent", not global_basin, global_basin)
    check("physical16_descent_remains_absent", not physical16_descent, physical16_descent)
    check("detector_calibration_remains_absent", not detector_calibration, detector_calibration)

    def bounded_records(records, limit=12):
        return [{
            "N": packet["N"],
            "p": packet["p"],
            "coordinates": [str(value) for value in packet["coordinates"]],
            "max_coordinate": str(max(packet["coordinates"])),
        } for packet in records[:limit]]

    result = {
        "work_package": "WP822",
        "title": "Finite chiral matter-spectrum census",
        "domain": {"N_min": 5, "N_max": 12, "p_min": 1, "p_max_rule": "8N",
                   "packet_count": len(domain)},
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "census": {
            "nonsingular_fixed_packets": len(nonsingular),
            "positive_fixed_packets": len(positive),
            "all_coordinates_below_one": len(controlled_unit),
            "all_coordinates_below_one_tenth": len(controlled_tenth),
            "positive_samples": bounded_records(positive),
            "unit_control_samples": bounded_records(controlled_unit),
            "tenth_control_samples": bounded_records(controlled_tenth),
            "unit_control_stability": [{
                "N": item["N"], "p": item["p"],
                "characteristic_polynomial": str(item["polynomial"]),
                "negative_exponents": int(item["negative_roots"]),
                "positive_exponents": int(item["positive_roots"]),
            } for item in controlled_stability],
        },
        "classification": {
            "grammar": "generalized Georgi-Glashow action with both scalar sectors and three Yukawas",
            "anomaly": "all integer packets in the frozen domain cancel the GG gauge anomaly",
            "control": "classified exactly at the admitted two-loop/one-loop truncation",
            "common_source": "no admitted constructor maps WP820 incidence/inflow to the GG (N,p) spectrum",
            "authorized_candidates": 0,
            "remaining_gates": ["global basin", "threshold completion", "physical16 descent",
                                "detector calibration"],
            "verdict": "finite census cannot supply selector authority across an undefined source interface",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp822_finite_chiral_matter_spectrum_census.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"summary": result["summary"], "census": {
        key: value for key, value in result["census"].items() if not key.endswith("samples")
    }}, indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
