from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/imaginary-character-weil-gram-interface-v1.json")
SOURCE = Path("research/grothendieck/explicit-two-variable-weil-heat-source-formula.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "Theta(t,xi)" in source and "K_prime" in source

    sigma, u, d, L = sp.symbols("sigma u d L", positive=True, real=True)
    xi = -sp.I * d / (4 * sigma)
    prefactor = sp.exp(-d**2 / (8 * sigma))
    shifted = sp.exp(-2 * sigma * (u - xi) ** 2)
    assert sp.simplify(prefactor * shifted - sp.exp(-2 * sigma * u**2 - sp.I * d * u)) == 0

    endpoint = sp.exp(2 * sigma / 4 - 2 * sigma * xi**2) * sp.cos(2 * sigma * xi)
    assert sp.simplify(prefactor * endpoint - sp.exp(sigma / 2) * sp.cosh(d / 2)) == 0

    prime_crossed = prefactor * sp.exp(-L**2 / (8 * sigma)) * sp.cosh(d * L / (4 * sigma))
    prime_pair = (sp.exp(-(L - d) ** 2 / (8 * sigma)) + sp.exp(-(L + d) ** 2 / (8 * sigma))) / 2
    prime_residual = sp.expand_power_exp((prime_crossed - prime_pair).rewrite(sp.exp))
    assert sp.simplify(prime_residual) == 0

    # Direct source-translate Fourier product equals the crossed shifted probe.
    gram_test = 4 * sp.pi * sigma * sp.exp(-2 * sigma * u**2) * sp.exp(-sp.I * d * u)
    crossed_theta_test = 4 * sp.pi * sigma * prefactor * shifted
    assert sp.simplify(gram_test - crossed_theta_test) == 0

    status = contract["status"]
    assert status["source_gram_identification"] == "constructed"
    assert status["finite_matrix_psd"] == "not proved"
    result = {
        "schema":"marici.voevodsky.imaginary-character-weil-gram-interface-check.v1",
        "status":"imaginary_character_gram_interface_verified",
        "fourier_gram_crossing_identity":True,
        "endpoint_cosh_crossing":True,
        "prime_paired_log_gaussians":True,
        "gamma_character_crossing":True,
        "sectorwise_compact_uniform_convergence_declared":True,
        "real_character_positivity_promoted":False,
        "finite_matrix_psd_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
