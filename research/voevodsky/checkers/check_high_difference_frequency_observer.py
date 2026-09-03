from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    t, h, q, r = sp.symbols("t h q r", positive=True, real=True)
    weight = sp.exp(-t * r) * (1 - sp.exp(-h * r)) ** q
    log_derivative = sp.simplify(sp.diff(sp.log(weight), r))
    expected = -t + q * h / (sp.exp(h * r) - 1)
    assert sp.simplify(log_derivative - expected) == 0

    r_star = sp.log(1 + q * h / t) / h
    assert sp.simplify(log_derivative.subs(r, r_star)) == 0
    second = sp.simplify(sp.diff(sp.log(weight), r, 2))
    assert sp.simplify(second.subs(r, r_star) + t * (t + q * h) / q) == 0

    # Fourier-cosine transform of one heat atom.
    xi, a = sp.symbols("xi a", positive=True, real=True)
    cosine_integral = sp.integrate(sp.exp(-t * xi**2) * sp.cos(2 * sp.sqrt(a) * xi), (xi, 0, sp.oo))
    expected_integral = sp.sqrt(sp.pi) / (2 * sp.sqrt(t)) * sp.exp(-a / t)
    assert sp.simplify(cosine_integral - expected_integral) == 0

    result = {
        "schema":"marici.voevodsky.high-difference-frequency-observer-check.v1",
        "status":"frequency_filter_identity_verified",
        "filter":"exp(-t xi^2)(1-exp(-h xi^2))^q",
        "peak_frequency_squared":"log(1+q h/t)/h",
        "log_weight_curvature_at_peak":"-t(t+q h)/q",
        "cosine_transform_constant":True,
        "prime_bound":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
