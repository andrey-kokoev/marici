"""WP273: exact finite-resource audit for dissipative fixed-state preparation."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    time = sp.symbols("time", nonnegative=True)
    rate = sp.symbols("rate", positive=True)
    amplitude = sp.symbols("amplitude", positive=True)
    tolerance = sp.symbols("tolerance", positive=True)

    deviation = amplitude * sp.exp(-rate * time)
    flow_residual = sp.simplify(sp.diff(deviation, time) + rate * deviation)
    required_time = sp.log(amplitude / tolerance) / rate
    residual_at_required_time = sp.simplify(deviation.subs(time, required_time))

    # Frozen bounded-domain instrument packet.
    packet = {rate: 1, amplitude: 10, tolerance: sp.Rational(1, 100)}
    packet_time = sp.simplify(required_time.subs(packet))
    packet_residual = sp.simplify(deviation.subs(packet).subs(time, packet_time))

    # Hostile initial amplitude outside the bounded packet at the same runtime.
    hostile_amplitude = sp.Rational(20)
    hostile_residual = sp.simplify(
        deviation.subs({rate: 1, amplitude: hostile_amplitude, time: packet_time})
    )

    # General adversary: for any finite runtime T, choose A=2*epsilon*exp(gamma*T).
    adversarial_amplitude = 2 * tolerance * sp.exp(rate * time)
    adversarial_residual = sp.simplify(deviation.subs(amplitude, adversarial_amplitude))
    finite_map_derivative = sp.diff(deviation, amplitude)

    checks = {
        "relaxation_solution_exact": flow_residual == 0,
        "finite_time_map_is_injective": finite_map_derivative == sp.exp(-rate * time) and finite_map_derivative != 0,
        "bounded_domain_runtime_formula_exact": residual_at_required_time == tolerance,
        "frozen_packet_runtime_is_log_1000": packet_time == sp.log(1000),
        "frozen_packet_reaches_tolerance": packet_residual == sp.Rational(1, 100),
        "same_runtime_fails_larger_unadmitted_amplitude": hostile_residual == sp.Rational(1, 50),
        "unbounded_domain_adversary_always_exceeds_tolerance": adversarial_residual == 2 * tolerance,
        "deliberate_uniform_finite_time_claim_fails": adversarial_residual > tolerance,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP273",
        "theorem_domain": "dissipative deviation dynamics dz/dt=-gamma*z with finite runtime and detector/preparation tolerance epsilon",
        "exact_deviation": str(deviation),
        "finite_time_derivative_with_respect_to_initial_amplitude": str(finite_map_derivative),
        "bounded_domain_runtime": str(required_time),
        "frozen_instrument_packet": {
            "gamma": "1",
            "maximum_initial_amplitude": "10",
            "tolerance": "1/100",
            "runtime": str(packet_time),
            "terminal_residual": str(packet_residual),
        },
        "hostile_unbounded_witness": {
            "same_runtime_amplitude": str(hostile_amplitude),
            "terminal_residual": str(hostile_residual),
            "general_adversarial_amplitude": str(adversarial_amplitude),
            "general_terminal_residual": str(adversarial_residual),
        },
        "contextual_partition": "finite-time dynamics preserves exact amplitudes; a tolerance quotient collapses them only on a declared bounded initial domain after a calibrated runtime",
        "classification": "unique dissipative vacuum supplies conditional approximate preparation, not an exact finite-time selector; uniform executable authority additionally requires a source-bounded domain, rate, tolerance, and runtime",
        "first_nonfaithful_arrow": "asymptotic unique vacuum -> uniform finite-resource preparation",
        "smallest_exact_falsifier": "the runtime log(1000) prepares amplitudes up to 10 within 1/100, but amplitude 20 retains residual 1/50",
        "remaining_physical_instrument_gate": "derive the initial-domain bound, damping rate, noise floor, stopping rule, stabilization, reset/degradation budget, and coupling to the physical flavor substrate",
        "scope_limit": "compact source domains with calibrated rates and tolerances can yield finite approximate preparation; exact finite-time projection or unbounded-domain uniformity is not established",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp273_dissipative_preparation_resource_bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
