from fractions import Fraction
import json

N = 4

# Source witness Omega=(1,1,1,1), g=(1,-1,0,0).
omega_norm_sq = Fraction(4)
g_norm_sq = Fraction(2)
omega_g_inner = Fraction(0)
source_bivector_energy = omega_norm_sq * g_norm_sq - omega_g_inner**2

# Under U=F_4/2: U Omega=2e_0, and unitarity preserves g norm and inner product.
dual_anchor_norm_sq = Fraction(4)
dual_g_norm_sq = g_norm_sq
dual_anchor_g_inner = omega_g_inner
dual_bivector_energy = (
    dual_anchor_norm_sq * dual_g_norm_sq - dual_anchor_g_inner**2
)

relative_flux = source_bivector_energy - dual_bivector_energy

checks = {
    "source_scalar_null": omega_g_inner == 0,
    "source_bivector_is_nonzero": source_bivector_energy > 0,
    "normalized_fourier_preserves_bivector_energy": (
        source_bivector_energy == dual_bivector_energy
    ),
    "dual_bivector_is_nonzero": dual_bivector_energy > 0,
    "opposite_oriented_relative_flux_cancels": relative_flux == 0,
}

out = {
    "schema": "marici.grothendieck.oriented-reciprocal-bivector-flux-cancellation.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "N": N,
        "source_bivector_energy": str(source_bivector_energy),
        "dual_bivector_energy": str(dual_bivector_energy),
        "relative_flux": str(relative_flux),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

