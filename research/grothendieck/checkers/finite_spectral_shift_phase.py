"""Finite exact counting model for the spectral-shift target."""

h0 = [1, 3]
h = [2, 4]


def count_below(spectrum, t):
    return sum(value <= t for value in spectrum)


tests = {t: count_below(h, t) - count_below(h0, t) for t in range(6)}
assert tests == {0: 0, 1: -1, 2: 0, 3: -1, 4: 0, 5: 0}

result = {
    "reference_spectrum": h0,
    "perturbed_spectrum": h,
    "counting_difference": tests,
    "determinant_ratio": "((z-2)(z-4))/((z-1)(z-3))",
    "zeros_and_poles_real_for_self_adjoint_pair": True,
    "xi_target": "spectral shift must reproduce -S(T), subject to sign convention",
    "rh_not_proved": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "finite-spectral-shift-phase.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

