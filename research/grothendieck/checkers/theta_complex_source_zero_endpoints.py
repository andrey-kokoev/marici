"""Identify completed-source zeros approached by the first Stokes thimbles."""
import json
from pathlib import Path

from theta_complex_log_curvature_roots import phi_jets


def newton_source_zero(seed, max_label=36, iterations=50):
    u = seed
    for _ in range(iterations):
        phi, first = phi_jets(u, max_label, 1)
        step = phi / first
        u -= step
        if abs(step) < 1e-14:
            break
    phi, first = phi_jets(u, max_label, 1)
    return u, abs(phi), abs(first)


seeds = [complex(-2.1e-5, 0.63853), complex(2.7e-5, 0.63922)]
rows = []
for seed in seeds:
    cutoff_checks = []
    for cutoff in (28, 36):
        root, residual, derivative = newton_source_zero(seed, cutoff)
        cutoff_checks.append({
            "max_label": cutoff,
            "root": [root.real, root.imag],
            "phi_absolute_residual": residual,
            "phi_prime_absolute": derivative,
        })
    rows.append({"seed": [seed.real, seed.imag], "checks": cutoff_checks})

same_root = abs(complex(*rows[0]["checks"][-1]["root"]) - complex(*rows[1]["checks"][-1]["root"])) < 1e-10
second_zero_checks = []
for cutoff in (28, 36):
    root, residual, derivative = newton_source_zero(complex(0.25566, 0.69525), cutoff)
    second_zero_checks.append({
        "max_label": cutoff,
        "root": [root.real, root.imag],
        "phi_absolute_residual": residual,
        "phi_prime_absolute": derivative,
    })
result = {
    "endpoint_rows": rows,
    "both_thimble_endpoint_seeds_converge_to_same_source_zero": same_root,
    "second_source_zero_checks": second_zero_checks,
    "first_two_source_zeros_distinct": abs(
        complex(*rows[0]["checks"][-1]["root"])
        - complex(*second_zero_checks[-1]["root"])
    ) > 0.01,
    "source_zero_is_xi_zero": False,
    "interpretation": "zero of analytically continued Mellin amplitude G, hence a relative-cycle endpoint",
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-complex-source-zero-endpoints.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
