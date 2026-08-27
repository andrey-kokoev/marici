import cmath
import math


def discrepancy(z, u, omega):
    parity_path = cmath.exp(-z * u) * omega
    real_path = cmath.exp(z.conjugate() * u) * omega
    factored = -2 * cmath.exp(-1j * z.imag * u) * math.sinh(z.real * u) * omega
    assert abs((parity_path - real_path) - factored) < 1e-12
    return abs(factored) ** 2


for imaginary in (0.0, 1.0, 14.0):
    assert discrepancy(complex(0.0, imaginary), 1.25, 0.7) < 1e-24

for real in (-2.0, -0.25, 0.25, 2.0):
    assert discrepancy(complex(real, 3.0), 1.25, 0.7) > 0

print("transported_2cell_norm_zero_iff=Re(z)=0")
print("critical_offset_after_centering=Re(s)=1/2")
print("scalar_null_to_2cell_null_bridge=not_proved")
print("forbidden_task=scalar_null_with_nonzero_distinction")
