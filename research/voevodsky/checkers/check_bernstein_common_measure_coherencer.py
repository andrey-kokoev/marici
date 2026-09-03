from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Abstract moments of a common positive base measure in feature z.
    mu0, mu1, mu2 = sp.symbols("mu0 mu1 mu2", positive=True, real=True)
    rank_two = sp.Matrix([[mu0, mu1], [mu1, mu2]])
    determinant = sp.factor(rank_two.det())
    assert determinant == mu0 * mu2 - mu1**2

    mean = mu1 / mu0
    variance = sp.simplify(mu2 / mu0 - mean**2)
    assert sp.simplify(determinant - mu0**2 * variance) == 0

    # Exact Beta(a,2) radial-filter fixture for Z=e^{-hR}, feature Y=1-Z.
    a = sp.symbols("a", positive=True, real=True)
    mean_z = a / (a + 2)
    variance_z = 2 * a / ((a + 2) ** 2 * (a + 3))
    mean_y = 1 - mean_z
    second_y = sp.simplify(variance_z + mean_y**2)
    normalized_det = sp.simplify(second_y - mean_y**2)
    assert normalized_det == variance_z
    assert sp.limit(variance_z, a, 0, dir="+") == 0
    assert sp.limit(variance_z, a, sp.oo) == 0

    result = {
        "schema":"marici.voevodsky.bernstein-common-measure-coherencer-check.v1",
        "status":"common_measure_covariance_identity_verified",
        "rank_two_determinant":"mu0^2 Var(Y)",
        "beta_fixture":"Z~Beta(a,2), Y=1-Z",
        "beta_variance":"2a/((a+2)^2(a+3))",
        "entrywise_saddle_comparison_required":False,
        "signed_prime_relative_bound":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
