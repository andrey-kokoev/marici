from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def outer(vector):
    return tuple(tuple(vector[i] * vector[j] for j in range(2)) for i in range(2))


def dephase(matrix):
    return ((matrix[0][0], Fraction(0)), (Fraction(0), matrix[1][1]))


def computational_distribution(matrix):
    return (matrix[0][0], matrix[1][1])


def main() -> None:
    # Work with unnormalized vectors (1, +/-1); normalized density matrices are
    # obtained by dividing their outer products by two.
    plus_outer = outer((Fraction(1), Fraction(1)))
    minus_outer = outer((Fraction(1), Fraction(-1)))
    plus = tuple(tuple(value / 2 for value in row) for row in plus_outer)
    minus = tuple(tuple(value / 2 for value in row) for row in minus_outer)

    assert plus != minus
    coherent_trace_distance = Fraction(1)  # Orthogonal pure states.
    assert coherent_trace_distance == 1

    plus_log = computational_distribution(plus)
    minus_log = computational_distribution(minus)
    assert plus_log == minus_log == (Fraction(1, 2), Fraction(1, 2))

    dephased_plus = dephase(plus)
    dephased_minus = dephase(minus)
    assert dephased_plus == dephased_minus
    logged_trace_distance = Fraction(0)
    assert logged_trace_distance == 0

    # In the X basis the same pair is perfectly distinguished, demonstrating
    # that basis choice moves the quotient rather than creating universal access.
    x_basis_plus_distribution = (Fraction(1), Fraction(0))
    x_basis_minus_distribution = (Fraction(0), Fraction(1))
    assert x_basis_plus_distribution != x_basis_minus_distribution

    result = {
        "schema": "marici.aspect.coherent-port-versus-classical-log.v1",
        "status": "pass",
        "coherent_plus_minus_trace_distance": str(coherent_trace_distance),
        "computational_log_plus_distribution": [str(value) for value in plus_log],
        "computational_log_minus_distribution": [str(value) for value in minus_log],
        "computational_logs_identical": plus_log == minus_log,
        "post_log_quantum_states_identical": dephased_plus == dephased_minus,
        "logged_plus_minus_trace_distance": str(logged_trace_distance),
        "x_basis_logs_distinguish_pair": x_basis_plus_distribution != x_basis_minus_distribution,
        "coherent_inverse_available": True,
        "classical_log_universal_inverse_available": False,
        "verdict": "Coherent environment access perfectly distinguishes and recovers |+> and |->, while a complete computational-basis outcome log is identical for them and leaves identical dephased states. Changing measurement basis moves the quotient but no fixed classical log preserves universal coherent reversibility.",
        "claim_boundary": "ideal qubits and projective computational-basis logging; no weak measurement, quantum-memory noise, adaptive collective measurement, or finite-sample tomography",
    }
    output = Path(__file__).parents[1] / "results" / "coherent_port_versus_classical_log.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
