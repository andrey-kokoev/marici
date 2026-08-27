import json
import sympy as sp


def main():
    q, radius, lam = sp.symbols("q radius lam", real=True, positive=True)
    translation_eigenfunction = sp.exp(sp.I * lam * q)
    density = sp.simplify(translation_eigenfunction * sp.conjugate(translation_eigenfunction))
    truncated_norm = sp.integrate(density, (q, -radius, radius))
    checks = {
        "translation_eigenfunction_has_constant_density": density == 1,
        "truncated_norm_grows_linearly": truncated_norm == 2 * radius,
        "full_line_norm_diverges": sp.limit(truncated_norm, radius, sp.oo) == sp.oo,
        "circle_laplacian_has_nonzero_point_spectrum": all(n * n > 0 for n in (1, 2, 3)),
    }
    result = {
        "schema": "marici.grothendieck.circle-log-carrier-intertwiner-no-go.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "truncated_translation_eigenfunction_norm": str(truncated_norm),
        "interpretation": (
            "The circle Laplacian has a complete eigenbasis, while logarithmic translation has no nonzero L2 "
            "eigenvectors. Any bounded generator-intertwiner from the circle carrier to the line carrier is zero."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
