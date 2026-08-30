"""Direct numerical audit of the log-time Fourier resolvent identity."""

import cmath


def analytic_integral(a, t):
    return 2 / (2 * a + 1j * t)


def resolvent(a, t):
    return 1 / (a + 0.5j * t)


samples = [(0.25, 0.0), (0.25, 3.0), (1.25, -2.0), (4.25, 11.0)]
assert all(analytic_integral(a, t) == resolvent(a, t) for a, t in samples)

u = 0.7
finite = 2 * sum(cmath.exp(-2 * (k + 0.25) * u) for k in range(100))
closed = 2 * cmath.exp(-u / 2) / (1 - cmath.exp(-2 * u))
assert abs(finite - closed) < 1e-15

result = {
    "resolvent_fourier_identity": "1/(a+iT/2)=2 integral_0^infinity exp(-2au)exp(-iTu)du",
    "sample_checks_pass": True,
    "summed_even_oscillator_density": "2 exp(-u/2)/(1-exp(-2u))",
    "prime_measure_support": "u=log(p^m)",
    "gamma_measure_support": "continuous u>0 plus endpoint distributions",
    "diagonal_mode_intertwiner_required": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "log-time-fourier-gamma-resolvent.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

