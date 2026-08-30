from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "three_hostiles_against_timeless_calculus.json"


def schur_hostile():
    # First jets at z=0 for scalar blocks A, B, C, E.
    A, Ap = F(2), F(1)
    B, Bp = F(3), F(2)
    C, Cp = F(5), F(3)
    E, Ep = F(11), F(7)
    S = E - C / A * B
    Sp = Ep - Cp / A * B + C / A * Ap / A * B - C / A * Bp
    full = Sp / S
    diagonal_only = Ep / E
    return {
        "S": str(S), "S_prime": str(Sp),
        "complete_log_jet": str(full), "diagonal_only_log_jet": str(diagonal_only),
        "deletion_residual": str(diagonal_only - full),
        "passes": S == F(7, 2) and Sp == F(5, 4) and diagonal_only - full == F(43, 154),
    }


def flavor_hostile():
    first = {"k": F(2), "c": F(3)}
    second = {"k": F(4), "c": F(3, 2)}
    q1, q2 = first["k"] * first["c"], second["k"] * second["c"]
    m1, m2 = first["k"] ** 2, second["k"] ** 2
    e1, e2 = 1 / m1, 1 / m2
    kernel_tangent = (first["k"], -first["c"])
    dq = first["c"] * kernel_tangent[0] + first["k"] * kernel_tangent[1]
    dm = 2 * first["k"] * kernel_tangent[0]
    return {
        "common_anomaly_product": str(q1), "masses": [str(m1), str(m2)],
        "exchange_strengths": [str(e1), str(e2)],
        "kernel_tangent": [str(x) for x in kernel_tangent],
        "completion_derivative": str(dq), "mass_derivative": str(dm),
        "passes": q1 == q2 == 6 and m2 / m1 == 4 and e2 / e1 == F(1, 4)
                  and dq == 0 and dm == 8,
    }


def clark_lift_hostile():
    # trace(x,y)=x. Two lifts have the same endpoint incidence.
    s = F(1)
    J0, J1, N = (s, F(0)), (s, s), (F(0), s)
    probe = (F(0), s)
    trace = lambda v: v[0]
    pairing = lambda x, y: sum(a * b for a, b in zip(x, y))
    r0, r1 = pairing(J0, probe), pairing(J1, probe)
    return {
        "trace_J0": str(trace(J0)), "trace_J1": str(trace(J1)),
        "kernel_shift_trace": str(trace(N)),
        "relation_J0": str(r0), "relation_J1": str(r1),
        "torsor_residual": str(r1 - r0),
        "passes": trace(J0) == trace(J1) == 1 and trace(N) == 0 and r1 - r0 == 1,
    }


def main():
    cases = {
        "theta_schur_first_jet": schur_hostile(),
        "flavor_green_schwarz_fiber": flavor_hostile(),
        "clark_tail_lift_torsor": clark_lift_hostile(),
    }
    assert all(case["passes"] for case in cases.values())
    out = {
        "schema": "marici.aspect.three-hostiles-timeless-calculus.v1",
        "status": "pass", "cases": cases,
        "common_proof_pattern": "a local completion is constant along a carrier-kernel direction while the target relation has a nonzero contraction along that direction",
        "architecture_verdicts": {
            "theta": "retain old block, new block, both incidences, and first jets until the Schur mate",
            "flavor": "retain k and c carrier coordinates until a source realization selects scale and orientation; product completion is not selection",
            "clark": "retain the graph-valued lift until Green sewing; endpoint incidence does not select a torsor origin",
        },
        "time_used": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
