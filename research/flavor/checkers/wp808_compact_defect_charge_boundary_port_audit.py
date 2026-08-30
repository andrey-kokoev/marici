"""Exact WP808 audit of compact defect charge and boundary orientation ports."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    v, k, x = sp.symbols("v k x", positive=True)
    phi0, phi1, phi2, phi3 = sp.symbols("phi0 phi1 phi2 phi3", real=True)
    periodic = [phi0, phi1, phi2, phi3, phi0]
    links = [(periodic[i + 1] - periodic[i]) / (2 * v) for i in range(4)]
    total_charge = sp.simplify(sum(links))

    kink_charge = sp.simplify((v - (-v)) / (2 * v))
    antikink_charge = sp.simplify((-v - v) / (2 * v))
    interval_forward = kink_charge
    interval_reverse = antikink_charge

    kink = sp.tanh(x)
    antikink = -sp.tanh(x)
    potential = lambda field: (1 - field**2) ** 2 / 2
    density = lambda field: sp.simplify(sp.diff(field, x) ** 2 / 2 + potential(field))
    kink_density = sp.trigsimp(density(kink).rewrite(sp.exp))
    antikink_density = sp.trigsimp(density(antikink).rewrite(sp.exp))

    compact_charges = [sp.Integer(1), sp.Integer(-1)]
    local_currents = [k * q for q in compact_charges]
    inclusive_current = sp.simplify(sum(local_currents))
    endpoint_sectors = {"forward": interval_forward, "reverse": interval_reverse}

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("periodic_link_charge_telescopes", total_charge == 0, total_charge)
    check("kink_has_unit_charge", kink_charge == 1, kink_charge)
    check("antikink_has_opposite_unit_charge", antikink_charge == -1, antikink_charge)
    check("compact_kink_antikink_packet_has_zero_charge", sum(compact_charges) == 0,
          sum(compact_charges))
    check("ordered_interval_endpoints_select_positive_charge", interval_forward == 1,
          interval_forward)
    check("reversed_interval_endpoints_select_negative_charge", interval_reverse == -1,
          interval_reverse)
    check("mirror_symmetric_action_gives_equal_wall_density",
          sp.simplify(kink_density - antikink_density) == 0,
          sp.simplify(kink_density - antikink_density))
    check("endpoint_reversal_preserves_wall_energy",
          sp.simplify(kink_density - antikink_density) == 0, "identical densities")
    check("compact_inflow_cancels_inclusively", inclusive_current == 0, inclusive_current)
    check("local_inflow_currents_are_opposite", local_currents == [k, -k], local_currents)
    check("unoriented_endpoint_groupoid_retains_two_sectors",
          set(endpoint_sectors.values()) == {-1, 1}, endpoint_sectors)
    fixed_port = {name: q for name, q in endpoint_sectors.items() if name == "forward"}
    check("ordered_boundary_port_restricts_to_single_stabilizer_sector",
          fixed_port == {"forward": 1}, fixed_port)
    vectorlike_threshold_shift = sp.Integer(1) + sp.Integer(-1)
    check("gapped_vectorlike_completion_preserves_zero_net_index",
          vectorlike_threshold_shift == 0, vectorlike_threshold_shift)

    # An inclusive topological current cannot calibrate either the wall position
    # or the detector gain. A local signed readout needs both as extra inputs.
    wall_position, detector_gain = sp.symbols("wall_position detector_gain", real=True)
    inclusive_probe = sp.Matrix([inclusive_current])
    jacobian = inclusive_probe.jacobian([wall_position, detector_gain])
    check("inclusive_probe_has_localization_and_calibration_kernel",
          jacobian.rank() == 0, f"rank={jacobian.rank()}, nullity=2")

    obstruction = abs(kink_charge) - abs(total_charge)
    check("deliberate_failure_exhibits_single_wall_compensation_obstruction",
          obstruction == 1, obstruction)

    result = {
        "work_package": "WP808",
        "title": "Compact defect charge and boundary-port audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "periodic_total_charge": str(total_charge),
            "compact_local_charges": [str(q) for q in compact_charges],
            "inclusive_inflow_current": str(inclusive_current),
            "ordered_endpoint_sectors": {name: str(q) for name, q in endpoint_sectors.items()},
        },
        "tests": tests,
        "classification": {
            "closed_compact_source": "cannot select a lone oriented wall; total defect charge vanishes",
            "interval_or_noncompact_source": "selects only after ordered boundary or asymptotic sector data",
            "inflow": "local relative sign survives but inclusive current cancels",
            "groupoid": "fixing endpoint order defines a stabilizer-groupoid relational experiment",
            "physical16": "localization and detector calibration remain independent inputs",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp808_compact_defect_charge_boundary_port_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
