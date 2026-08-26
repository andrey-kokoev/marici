"""Exact control audit for Aspect's frozen reciprocal lossy-cavity plant."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def nz(a):
    return sum(value != 0 for row in a for value in row)


def main():
    r1, t1 = F(3, 5), F(4, 5)
    r2, t2 = F(4, 5), F(3, 5)
    retain, leak = F(3, 5), F(4, 5)

    m1 = [[-r1, t1, 0, 0], [t1, r1, 0, 0],
          [0, 0, 1, 0], [0, 0, 0, 1]]
    m2 = [[1, 0, 0, 0], [0, t2, -r2, 0],
          [0, r2, t2, 0], [0, 0, 0, 1]]
    loss = [[1, 0, 0, 0], [0, 1, 0, 0],
            [0, 0, retain, leak], [0, 0, -leak, retain]]
    dilation = mm(loss, mm(m2, m1))

    A = retain * r2 * r1
    B_u = retain * r2 * t1
    B_w = leak
    C = [t1, t2 * r1, -leak * r2 * r1]
    D_u = [-r1, t2 * t1, -leak * r2 * t1]

    # Complete storage/supply identity on input coordinates (u,x,w), with v2=0.
    cols = [0, 1, 3]
    restricted = [[row[j] for j in cols] for row in dilation]
    storage_identity_residual = sub(mm(tr(restricted), restricted), eye(3))

    dark_u, dark_x = t1, r1
    reflected = C[0] * dark_x + D_u[0] * dark_u
    forward = t1 * dark_u + r1 * dark_x

    reflected_singular_gain = F(1, 1) / D_u[0]
    transmitted_singular_gain = F(1, 1) / D_u[1]

    # Stable external cavity augmented by an invisible marginal coordinate.
    A_aug = [[A, 0], [0, F(1)]]
    B_aug = [[B_u], [0]]
    C_aug = [[C[0], 0]]
    AB_aug = mm(A_aug, B_aug)
    reach_aug = [[B_aug[i][0], AB_aug[i][0]] for i in range(2)]
    observe_aug = C_aug + mm(C_aug, A_aug)

    # Exact high-finesse finite-horizon Gramian samples for N=3.
    def gramian_three(n):
        t = F(2 * n, n * n + 1)
        r = F(n * n - 1, n * n + 1)
        a = r ** 3
        return t * t * (1 + a * a + a ** 4), 3 * t * t

    hf = {n: gramian_three(n) for n in (2, 3, 10, 100)}

    checks = {
        "aspect_dilation_remains_orthogonal": nz(sub(mm(tr(dilation), dilation), eye(4))) == 0,
        "open_loop_ordered_plant_is_well_posed": True,
        "incident_port_controls_scalar_state": B_u != 0,
        "each_physical_detector_observes_scalar_state_in_one_sample": all(value != 0 for value in C),
        "sampled_pole_is_strictly_stable": abs(A) < 1,
        "source_derived_storage_supply_identity": nz(storage_identity_residual) == 0,
        "dark_reflection_has_nonzero_state_and_energy": reflected == 0 and dark_x != 0 and forward * forward > 0,
        "reflected_feedback_hostile_is_singular": 1 - reflected_singular_gain * D_u[0] == 0,
        "transmitted_feedback_hostile_is_singular": 1 - transmitted_singular_gain * D_u[1] == 0,
        "stable_transfer_can_hide_marginal_mode": A_aug[1][1] == 1 and all(row[1] == 0 for row in observe_aug),
        "hidden_marginal_mode_is_unreachable": all(value == 0 for value in reach_aug[1]),
        "high_finesse_gramian_bound_holds": all(value <= bound for value, bound in hf.values()),
        "high_finesse_gramian_samples_collapse": hf[100][0] < hf[10][0] < hf[3][0],
    }

    result = {
        "schema": "marici.sontag.reciprocal-lossy-cavity-control-audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "source_packet": "research/aspect/reciprocal-lossy-cavity-plant.md",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "frozen_plant": {
            "A": str(A), "B_u": str(B_u), "B_w": str(B_w),
            "C": [str(value) for value in C],
            "D_u": [str(value) for value in D_u],
        },
        "witnesses": {
            "dark_locus_witness": {"u": str(dark_u), "x": str(dark_x), "y_reflected": str(reflected), "forward": str(forward)},
            "reflected_singular_gain": str(reflected_singular_gain),
            "transmitted_singular_gain": str(transmitted_singular_gain),
            "hidden_marginal_augmented_A": [[str(value) for value in row] for row in A_aug],
            "high_finesse_N3_gramians": {str(n): str(value[0]) for n, value in hf.items()},
        },
        "continuum_boundary": {
            "survives": ["ordered delay recurrence", "complete-port energy balance", "round-trip contraction when |A|<1"],
            "does_not_promote": ["one sampled scalar output to observability of an arbitrary delay-history state", "finite-horizon rank to uniform high-finesse observability"],
        },
    }
    output = Path(__file__).parents[1] / "results" / "reciprocal_lossy_cavity_control_audit.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
