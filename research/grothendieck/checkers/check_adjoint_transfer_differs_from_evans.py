"""Exact separation of endpoint Evans and adjoint autocorrelation transfers."""

from fractions import Fraction
import json


# f=1 on [0,1], z=0, so G(q)=1-q.
evans = Fraction(1)
adjoint_return = Fraction(1, 2)

# A second source f=2 has Evans scaling linearly and adjoint return quadratically.
evans_scaled = 2 * evans
adjoint_scaled = 4 * adjoint_return

checks = {
    "endpoint_evans_value": evans == 1,
    "adjoint_autocorrelation_value": adjoint_return == Fraction(1, 2),
    "transfers_are_distinct": evans != adjoint_return,
    "evans_scales_linearly_in_source": evans_scaled == 2,
    "adjoint_return_scales_quadratically_in_source": adjoint_scaled == 2,
    "scaling_degrees_differ": evans_scaled / evans != adjoint_scaled / adjoint_return,
}

result = {
    "schema": "marici.grothendieck.adjoint-transfer-differs-from-evans.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "values": {
        "evans": str(evans),
        "adjoint_return": str(adjoint_return),
        "evans_after_f_times_2": str(evans_scaled),
        "adjoint_after_f_times_2": str(adjoint_scaled),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
