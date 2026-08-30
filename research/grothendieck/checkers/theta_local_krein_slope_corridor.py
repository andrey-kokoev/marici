import json
import math


def phi_label(n, u):
    x = math.pi * n * n * math.exp(2.0 * u)
    return math.exp(u / 2.0) * (4.0 * x * x - 6.0 * x) * math.exp(-x)


def phi_label_prime(n, u):
    x = math.pi * n * n * math.exp(2.0 * u)
    phi = phi_label(n, u)
    score = 4.5 + 6.0 / (2.0 * x - 3.0) - 2.0 * x
    return phi * score


def theta_phi_and_prime(u):
    total = 0.0
    derivative = 0.0
    for n in range(1, 100):
        term = phi_label(n, u)
        total += term
        derivative += phi_label_prime(n, u)
        if n > 4 and abs(term) < 1.0e-30 * abs(total):
            break
    return total, derivative


u = 0.1
y = 0.2
d = 1.0e-4
phi, phi_prime = theta_phi_and_prime(u)
k = -phi_prime / phi
lower_slope = y * math.tanh(y * u)
upper_slope = y / math.tanh(y * u)

phi_2, _ = theta_phi_and_prime(u + d)
actual_ratio = phi_2 / phi
lower_ratio = math.sinh(y * u) / math.sinh(y * (u + d))
upper_ratio = math.cosh(y * u) / math.cosh(y * (u + d))

result = {
    "schema": "marici.grothendieck.theta_local_krein_slope_corridor.v1",
    "parameters": {"u": u, "y": y, "d": d},
    "theta_logarithmic_decay": k,
    "infinitesimal_forbidden_corridor": [lower_slope, upper_slope],
    "finite_forbidden_ratio_interval": [lower_ratio, upper_ratio],
    "actual_theta_ratio": actual_ratio,
    "checks": {
        "actual_theta_slope_enters_corridor": lower_slope < k < upper_slope,
        "actual_theta_ratio_enters_finite_interval": lower_ratio < actual_ratio < upper_ratio,
        "near_seam_criterion_holds": 0.0 < u * k < 1.0,
    },
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
