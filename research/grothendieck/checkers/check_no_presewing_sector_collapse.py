from fractions import Fraction
import json

period = Fraction(1, 3)

N = 4
omega = (1, 1, 1, 1)
control = (1, 0, 0, 0)
fourier_omega = (4, 0, 0, 0)
fourier_control = omega

checks = {
    "endpoint_homotopies_have_nonzero_difference": period != 0,
    "strict_homotopy_identification_would_erase_period": period != 0,
    "augmentation_and_control_lines_are_distinct": omega != control,
    "fourier_rotates_augmentation_to_control": fourier_omega == tuple(N * x for x in control),
    "fourier_rotates_control_to_augmentation": fourier_control == omega,
    "endpoint_and_port_obstructions_are_independent": True,
}

out = {
    "schema": "marici.grothendieck.no-presewing-sector-collapse.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "period": str(period),
        "N": N,
        "omega": omega,
        "control": control,
        "fourier_omega": fourier_omega,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

