import cmath
import math


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


a = 2.0
b = 1.0
c = 1.0
delta = a - b

for k in range(-10, 11):
    z_squared = -(math.log(c) + 1j * (2 * k + 1) * math.pi) / delta
    for z in [cmath.sqrt(z_squared), -cmath.sqrt(z_squared)]:
        F = cmath.exp(-a * z * z) + c * cmath.exp(-b * z * z)
        Fp = -2 * a * z * cmath.exp(-a * z * z) - 2 * b * c * z * cmath.exp(-b * z * z)
        closed_form_Fp = 2 * c * delta * z * cmath.exp(-b * z * z)
        gate(abs(F) < 1e-8 * max(1.0, abs(cmath.exp(-b * z * z))))
        gate(abs(z.real) > 1e-10)
        gate(abs(z.imag) > 1e-10)
        gate(abs(Fp) > 1e-10)
        gate(abs(Fp - closed_form_Fp) < 1e-8 * max(1.0, abs(Fp)))

# The source is a sum of positive Gaussians at representative real points.
for u in range(-20, 21):
    phi = math.exp(-(u * u) / (4 * a)) / math.sqrt(4 * math.pi * a)
    phi += c * math.exp(-(u * u) / (4 * b)) / math.sqrt(4 * math.pi * b)
    gate(phi > 0)

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
