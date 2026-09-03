from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/shifted-gaussian-versus-translate-gram-interface-v1.json")
SOURCE = Path("research/grothendieck/explicit-two-variable-weil-heat-source-formula.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "h_(t,xi)(u)=exp[-t(u-xi)^2]" in source
    assert "Fourier convention" in source

    u, t, xi, d, sigma = sp.symbols("u t xi d sigma", positive=True, real=True)
    shifted = sp.exp(-t * (u - xi) ** 2)
    character_weighted = sp.exp(-t * u**2) * sp.exp(-sp.I * d * u)
    ratio = sp.simplify(shifted / character_weighted)
    assert sp.simplify(sp.diff(ratio, u)) != 0

    # Translate phases polarize to a difference character.
    a, b = sp.symbols("a b", real=True)
    phase_product = sp.exp(-sp.I * a * u) * sp.exp(sp.I * b * u)
    assert sp.simplify(phase_product - sp.exp(-sp.I * (a - b) * u)) == 0

    # The Gaussian Fourier modulus has doubled exponent in the Gram product.
    gaussian_fourier = sp.sqrt(4 * sp.pi * sigma) * sp.exp(-sigma * u**2)
    modulus_product = sp.simplify(gaussian_fourier**2 * phase_product)
    expected = 4 * sp.pi * sigma * sp.exp(-2 * sigma * u**2) * sp.exp(-sp.I * (a - b) * u)
    assert sp.simplify(modulus_product - expected) == 0

    # Spectral shifting corresponds to modulation in the inverse-Fourier source.
    x = sp.symbols("x", real=True)
    shifted_inverse_shape = sp.exp(-x**2 / (4 * t)) * sp.exp(sp.I * xi * x)
    assert sp.simplify(shifted_inverse_shape.subs(xi, 0) - sp.exp(-x**2 / (4 * t))) == 0
    assert sp.simplify(sp.diff(shifted_inverse_shape, xi).subs(xi, 0)) != 0

    status = contract["status"]
    assert status["direct_identification"] == "refuted"
    assert status["polarization_interface"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.shifted-gaussian-versus-translate-gram-interface-check.v1",
        "status":"gaussian_interface_type_mismatch_verified",
        "translate_phase_difference_identity":True,
        "gram_width_doubling":True,
        "spectral_shift_is_source_modulation":True,
        "shifted_probe_equals_translate_gram_test":False,
        "polarization_interface_supplied":False,
        "all_translate_psd_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
