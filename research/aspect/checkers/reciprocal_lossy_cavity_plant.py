"""Exact rational checks for the reciprocal lossy cavity plant."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def nz(a):
    return sum(x != 0 for row in a for x in row)


def main():
    r1, t1 = F(3, 5), F(4, 5)
    r2, t2 = F(4, 5), F(3, 5)
    retain, leak = F(3, 5), F(4, 5)

    # Component order: mirror 1, mirror 2, then environmental dilation.
    m1 = [[-r1, t1, 0, 0], [t1, r1, 0, 0],
          [0, 0, 1, 0], [0, 0, 0, 1]]
    m2 = [[1, 0, 0, 0], [0, t2, -r2, 0],
          [0, r2, t2, 0], [0, 0, 0, 1]]
    loss = [[1, 0, 0, 0], [0, 1, 0, 0],
            [0, 0, retain, leak], [0, 0, -leak, retain]]
    dilation = mm(loss, mm(m2, m1))
    dilation_residual = sub(mm(tr(dilation), dilation), eye(4))

    # Dark reflected port does not erase the forward intracavity field.
    u, x = t1, r1
    reflected = -r1 * u + t1 * x
    forward = t1 * u + r1 * x

    # Frozen scalar plant at p=q=1.
    A = retain * r2 * r1
    B = retain * r2 * t1
    C = [[t1], [t2 * r1], [-leak * r2 * r1]]
    D = [[-r1], [t2 * t1], [-leak * r2 * t1]]

    # One analyzer row cannot distinguish these Jones states.
    jones_plus = [[F(1)], [F(1)]]
    jones_minus = [[F(1)], [F(-1)]]
    analyzer = [[F(1), F(0)]]
    same_scalar = mm(analyzer, jones_plus) == mm(analyzer, jones_minus)
    distinct_states = jones_plus != jones_minus
    second_analyzer = [[F(0), F(1)]]
    two_row_readouts_differ = (
        mm(analyzer + second_analyzer, jones_plus)
        != mm(analyzer + second_analyzer, jones_minus)
    )

    # Reciprocal S in energy coordinates; unequal displayed port scaling.
    S = [[-r1, t1], [t1, r1]]
    Dscale = [[F(1), F(0)], [F(0), F(2)]]
    Dinv = [[F(1), F(0)], [F(0), F(1, 2)]]
    Sprime = mm(Dscale, mm(S, Dinv))
    G = [[F(1), F(0)], [F(0), F(1, 4)]]
    euclidean_reciprocity_residual = sub(Sprime, tr(Sprime))
    metric_reciprocity_residual = sub(mm(G, Sprime), mm(tr(Sprime), G))

    checks = {
        "four_port_dilation_is_orthogonal": nz(dilation_residual) == 0,
        "dark_reflection_with_nonzero_intracavity_energy": reflected == 0 and forward * forward > 0,
        "one_analyzer_row_has_hidden_polarization_kernel": same_scalar and distinct_states,
        "two_independent_analyzer_rows_are_jointly_faithful_on_witness": two_row_readouts_differ,
        "euclidean_reciprocity_fails_after_unequal_scaling": nz(euclidean_reciprocity_residual) > 0,
        "energy_metric_repairs_typed_reciprocity": nz(metric_reciprocity_residual) == 0,
    }
    result = {
        "schema": "marici.aspect.reciprocal_lossy_cavity_plant.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "frozen_plant": {
            "dimensions": {
                "state": "C^1", "input_complete": "C^2", "output_complete": "C^3",
                "A": "C^1->C^1", "B": "C^2->C^1", "C": "C^1->C^3", "D": "C^2->C^3",
            },
            "state": ["x_returning"],
            "inputs": ["u_incident", "w_loss_environment"],
            "outputs": ["y_reflected", "y_transmitted", "y_loss_environment"],
            "A": str(A), "B_u": str(B), "B_w": str(leak),
            "C": [[str(v) for v in row] for row in C],
            "D_u": [[str(v) for v in row] for row in D],
            "component_order": ["input_mirror", "forward_phase", "end_mirror", "return_phase", "loss_dilation", "next_state"],
            "energy_metric_scaled_ports": [["1", "0"], ["0", "1/4"]],
            "parameter_domain": {
                "mirrors": "real r_j,t_j with r_j^2+t_j^2=1",
                "phases": "complex p,q with |p|=|q|=1",
                "loss": "real a,ell>=0 with a^2+ell^2=1",
                "delay": "T>0",
            },
            "continuum_delay_relation": "x(t+T)=a*q*r2*p*(t1*u(t)+r1*x(t))+ell*w(t)",
            "analyzer_single": [["1", "0"]],
            "analyzer_joint": [["1", "0"], ["0", "1"]],
        },
        "witnesses": {
            "dark_reflected_amplitude": str(reflected),
            "forward_intracavity_amplitude": str(forward),
            "euclidean_reciprocity_residual": [[str(v) for v in row] for row in euclidean_reciprocity_residual],
            "metric_reciprocity_residual": [[str(v) for v in row] for row in metric_reciprocity_residual],
        },
        "claim_boundary": "physical plant only; no observability, stability, feedback, or controller-authority claim",
    }
    out = Path(__file__).parents[1] / "results" / "reciprocal_lossy_cavity_plant.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
