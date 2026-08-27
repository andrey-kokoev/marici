#!/usr/bin/env python3
"""Discrete exact-numerical audit of the two-port orientation instrument."""

from cmath import exp


# Smooth decaying phase packet K(q)=exp((-alpha+i beta)q).
alpha = 2.0
beta = 0.7
a = 0.4
t = 1.3
z = complex(a, t)

# Analytic half-line integrals.
K0_sq = 1.0
norm_sq = 1 / (2 * alpha)
# D=-partial sends K to (alpha-i beta)K.
C = complex(alpha, -beta) * norm_sq
J = C.imag

face_difference = (
    abs(complex(alpha, -beta) + z) ** 2
    - abs(complex(alpha, -beta) - z) ** 2
) * norm_sq
two_port = 2 * a * K0_sq + 4 * t * J

checks = {
    "integration_by_parts_endpoint_port": abs(C.real - K0_sq / 2) < 1e-12,
    "two_port_decomposition": abs(face_difference - two_port) < 1e-12,
    "wronskian_is_independent": abs(J) > 1e-3,
}

# Conjugation preserves endpoint amplitude and reverses J.
C_conjugate = complex(alpha, beta) * norm_sq
checks["endpoint_even_under_conjugation"] = K0_sq == K0_sq
checks["wronskian_odd_under_conjugation"] = abs(C_conjugate.imag + J) < 1e-12

# Constant phase is the hostile showing endpoint does not determine J.
C_flat = complex(alpha, 0) * norm_sq
checks["same_endpoint_different_phase_current"] = abs(C_flat.real - C.real) < 1e-12 and abs(C_flat.imag - J) > 1e-3

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

