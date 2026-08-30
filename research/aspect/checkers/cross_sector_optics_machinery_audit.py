"""Exact fixtures for typed cross-sector optics correspondences."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def main():
    # Control bridge: dark reflected port, nonzero scalar state and C row.
    u, x = F(4, 5), F(3, 5)
    C_ref, D_ref = F(4, 5), F(-3, 5)
    reflected = C_ref * x + D_ref * u
    forward = F(4, 5) * u + F(3, 5) * x

    # Ordered transport bridge: exact noncommuting Jones operations.
    R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    A = [[F(3, 5), F(0)], [F(0), F(1)]]
    RA, AR = mm(R, A), mm(A, R)

    # Flavor/calibration bridge.
    analyzer_one = [[F(1), F(0)]]
    analyzer_two = [[F(1), F(0)], [F(0), F(1)]]
    hidden = [[F(0)], [F(1)]]

    # Memory bridge: same integral, different temporal carrier profiles.
    profile_a = [F(1), F(-1), F(0)]
    profile_b = [F(0), F(0), F(0)]

    # Distinction-preserving completion hostile Q=(1,0), R=I.
    q_hidden = mm(analyzer_one, hidden)
    r_hidden = mm(analyzer_two, hidden)

    # Phase-only scattering loses amplitude and is undefined at zero.
    phase_packet_a = (F(1), F(0))
    phase_packet_b = (F(2), F(0))
    phase_readout_a = (F(1), F(0))
    phase_readout_b = (F(1), F(0))
    zero_amplitude = (F(0), F(0))

    # Selected transmission zero and faithful complementary row.
    selected = F(-1, 2) * F(1) + F(1, 2) * F(1)
    complement = F(1, 2) * F(1) + F(1, 2) * F(1)

    checks = {
        "control_darkness_does_not_erase_state_or_observation_coefficient": reflected == 0 and x != 0 and C_ref != 0 and forward == 1,
        "ordered_transports_do_not_commute": RA != AR,
        "one_analyzer_has_kernel_two_rows_repair_declared_class": mm(analyzer_one, hidden) == [[0]] and mm(analyzer_two, hidden) == hidden,
        "memory_integral_is_not_full_temporal_carrier": sum(profile_a) == sum(profile_b) == 0 and profile_a != profile_b,
        "full_readout_does_not_descend_through_scalar_projection": q_hidden == [[0]] and r_hidden != [[0], [0]],
        "phase_readout_is_not_amplitude_faithful": phase_readout_a == phase_readout_b and phase_packet_a != phase_packet_b,
        "zero_amplitude_has_no_phase_coordinate": zero_amplitude == (0, 0),
        "selected_zero_survives_faithful_complement": selected == 0 and complement == 1,
    }
    result = {
        "schema": "marici.aspect.cross_sector_optics_machinery_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "bridges": {
            "control": "frozen optical plant -> separately audited state/control properties",
            "topological_transport": "ordered Jones products -> holonomy template under admitted frame group",
            "flavor": "calibrated analyzer rank -> coordinate observability template",
            "radiative_memory": "temporal carrier -> integrated/DC readout with kernel",
            "completion": "optical compression -> kernel inclusion and uniform descent gate",
            "theta_scattering": "multiport amplitude -> phase quotient and selected-channel zero taxonomy",
        },
        "prohibited_authority_transfers": [
            "optical calibration to flavor source authority",
            "Jones group to topological or arithmetic coefficient group",
            "optical temporal mode to Bondi news",
            "finite rank to uniform completion",
            "phase unitarity or tomography to scalar zero exclusion",
            "dark-port optics to an RH claim",
        ],
        "residuals": {
            "ordered_transport_RA": [[str(v) for v in row] for row in RA],
            "ordered_transport_AR": [[str(v) for v in row] for row in AR],
            "equal_memory_integrals": [str(sum(profile_a)), str(sum(profile_b))],
            "selected_and_complement_outputs": [str(selected), str(complement)],
        },
    }
    out = Path(__file__).parents[1] / "results" / "cross_sector_optics_machinery_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
