"""WP275: exact linear-feedback noise tradeoff for flavor preparation."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    gain = sp.symbols("gain", nonnegative=True)
    damping, source_noise, sensor_noise = sp.symbols(
        "damping source_noise sensor_noise", positive=True
    )
    stationary_variance = (source_noise + sensor_noise * gain**2) / (damping + gain)
    derivative = sp.factor(sp.diff(stationary_variance, gain))
    optimal_gain = sp.simplify(-damping + sp.sqrt(damping**2 + source_noise / sensor_noise))
    derivative_at_optimum = sp.simplify(derivative.subs(gain, optimal_gain))
    optimum_variance = sp.simplify(stationary_variance.subs(gain, optimal_gain))
    optimum_identity = sp.simplify(optimum_variance - 2 * sensor_noise * optimal_gain)

    # Exact rational packet: gamma=1, D=1/100, R=1/300 gives k*=1.
    packet = {
        damping: sp.Rational(1),
        source_noise: sp.Rational(1, 100),
        sensor_noise: sp.Rational(1, 300),
    }
    packet_gain = sp.simplify(optimal_gain.subs(packet))
    packet_floor = sp.simplify(optimum_variance.subs(packet))
    passive_floor = sp.simplify((source_noise / damping).subs(packet))

    target_variance = sp.Rational(1, 200)
    gain_zero_floor = sp.simplify(stationary_variance.subs(packet).subs(gain, 0))
    gain_large_floor = sp.limit(stationary_variance.subs(packet), gain, sp.oo)

    checks = {
        "stationary_variance_formula_positive": stationary_variance > 0,
        "optimal_gain_stationary_exact": derivative_at_optimum == 0,
        "optimal_gain_positive": sp.simplify((optimal_gain + damping) ** 2 - damping**2) == source_noise / sensor_noise and (source_noise / sensor_noise).is_positive,
        "minimum_variance_identity_exact": optimum_identity == 0,
        "rational_packet_optimal_gain_one": packet_gain == 1,
        "feedback_improves_passive_floor": packet_floor == sp.Rational(1, 150) and packet_floor < passive_floor,
        "optimized_packet_still_misses_tighter_target": packet_floor > target_variance,
        "zero_gain_recovers_passive_floor": gain_zero_floor == passive_floor,
        "infinite_gain_amplifies_sensor_noise": gain_large_floor == sp.oo,
        "deliberate_unbounded_gain_removes_noise_claim_fails": gain_large_floor == sp.oo,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP275",
        "theorem_domain": "linear feedback with intrinsic damping gamma, source diffusion D, controller gain k, and independent sensor-noise intensity R",
        "stationary_variance": str(stationary_variance),
        "optimal_gain": str(optimal_gain),
        "minimum_variance": str(optimum_variance),
        "minimum_identity": "v_min=2*R*k_star",
        "exact_packet": {
            "gamma": "1",
            "D": "1/100",
            "R": "1/300",
            "passive_floor": str(passive_floor),
            "optimal_gain": str(packet_gain),
            "optimized_floor": str(packet_floor),
            "tighter_target_variance": str(target_variance),
        },
        "contextual_partition": "feedback refines the noisy preparation classes only in the enlarged sensor-controller experiment; sensor noise leaves a nonzero optimized floor",
        "classification": "linear feedback can improve an approximate distribution selector but cannot remove noise freely; it requires a new calibrated measurement/control port and remains neither an exact point selector nor a texture rigidifier",
        "first_nonfaithful_arrow": "formal feedback gain -> executable sensor-derived control with calibrated noise",
        "smallest_exact_falsifier": "gamma=1, D=1/100, and R=1/300 optimize at k=1 with floor 1/150, still above target variance 1/200",
        "remaining_physical_instrument_gate": "derive a flavor-sensitive sensor, actuator coupling, sensor noise R, latency/bandwidth, gain bound, energetic cost, stopping rule, and post-feedback stabilization from the source experiment",
        "scope_limit": "nonlinear, adaptive, squeezed, coherent, or error-corrected feedback can change the bound but defines a new instrument and resource law",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp275_feedback_selector_noise_tradeoff.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
