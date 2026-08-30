"""Exact localization of a closed-loop zero to a calibrated boundary Schur block."""

from fractions import Fraction as F
import json
from pathlib import Path


def det2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def matvec(a, x):
    return [sum(a[i][j]*x[j] for j in range(len(x))) for i in range(len(a))]


def full_matrix(q):
    return [[F(2), F(0), F(1)], [F(0), F(3), F(1)], [F(2), F(3), F(2)+q]]


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def main():
    plant = [[F(2), F(0)], [F(0), F(3)]]
    injection = [F(1), F(1)]
    readout = [F(2), F(3)]
    plant_inverse_injection = [F(1, 2), F(1, 3)]
    loop = sum(c*x for c, x in zip(readout, plant_inverse_injection))
    records = {}
    for q in (F(-1, 2), F(0), F(1, 2)):
        direct = F(2)+q
        schur = direct-loop
        records[str(q)] = {"direct": str(direct), "loop": str(loop), "schur": str(schur), "full_determinant": str(det3(full_matrix(q)))}
    boundary_kernel = [-x for x in plant_inverse_injection] + [F(1)]
    checks = {
        "open_plant_is_invertible_at_closed_loop_zero": det2(plant) == 6,
        "plant_injection_readout_and_direct_blocks_are_separate": loop == 2,
        "schur_complement_is_exactly_q": all(F(k) == F(v["schur"]) for k, v in records.items()),
        "full_determinant_factorizes_as_det_plant_times_schur": all(F(v["full_determinant"]) == 6*F(v["schur"]) for v in records.values()),
        "closed_network_is_singular_only_at_tested_zero": records["0"]["full_determinant"] == "0" and records["-1/2"]["full_determinant"] != "0" and records["1/2"]["full_determinant"] != "0",
        "zero_state_is_a_boundary_feedback_state": matvec(full_matrix(F(0)), boundary_kernel) == [F(0), F(0), F(0)],
        "direct_block_alone_does_not_locate_zero": records["0"]["direct"] == "2",
        "loop_gain_one_is_the_boundary_failure": loop/F(2) == 1,
        "finite_localization_does_not_prove_global_small_gain": True,
    }
    result = {
        "schema": "marici.aspect.closed_loop_boundary_schur_zero.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "records": records,
        "boundary_kernel": [str(x) for x in boundary_kernel],
        "typed_boundary": {
            "source": "one calibrated boundary probe and two internal optical modes",
            "constructor": "boundary injection, open propagation, readout, and direct return closed in that order",
            "detector": "separate block calibration followed by full-network null detection",
            "hostile": "open-plant or direct-block inspection misses the closed-loop zero",
            "completion": "finite localization gives no theta incidence, reciprocal two-sector norm, or completion-stable small-gain theorem",
        },
    }
    out = Path(__file__).parents[1] / "results" / "closed_loop_boundary_schur_zero.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
