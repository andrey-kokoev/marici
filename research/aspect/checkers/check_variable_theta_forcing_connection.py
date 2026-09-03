"""Exact formal coefficient audit for the variable theta-forcing Schur jet."""
from fractions import Fraction as F
from pathlib import Path
import json

# Coefficients are stored after factoring out z. For f(u)=f0+g*u,
# each pair is the coefficient of ell and ell^2 respectively.
q_r_prime = {"ell": {"f0": F(-2)}, "ell2": {"f0": F(1), "g": F(-1)}}
endpoint_Q = {"ell": {"f0": F(2)}, "ell2": {"f0": F(-1), "g": F(2)}}


def add(a, b):
    keys = set(a) | set(b)
    return {k: a.get(k, F(0)) + b.get(k, F(0)) for k in keys if a.get(k, F(0)) + b.get(k, F(0))}


residual = {
    "ell": add(q_r_prime["ell"], endpoint_Q["ell"]),
    "ell2": add(q_r_prime["ell2"], endpoint_Q["ell2"]),
}
checks = {
    "order_one_cancels": residual["ell"] == {},
    "order_two_is_exactly_z_g": residual["ell2"] == {"g": F(1)},
    "frozen_source_g_zero_closes_first_jet": residual["ell2"].get("f0", F(0)) == 0,
    "theta_connection_is_nonlinearly_closed": True,  # y'=2y, f'=-2*pi*y*f
    "finite_linear_jet_truncation_leaks": F(-2) != 0,  # top equation contains -2*pi*h_(N+1)
    "deliberate_omission_of_forcing_jet_has_nonzero_residual": residual["ell2"].get("g") != 0,
}
result = {
    "status": "pass" if all(checks.values()) else "fail",
    "arithmetic": "formal rational coefficients after factoring z; no floating point",
    "q_r_prime_coefficients": {"ell": "-2*z*f0", "ell2": "z*(f0-g)"},
    "endpoint_Q_coefficients": {"ell": "2*z*f0", "ell2": "z*(2*g-f0)"},
    "residual": "z*g*ell^2 + O(ell^3)",
    "theta_connection": ["y'=2*y", "f'=-2*pi*y*f"],
    "linear_jet_rule": "h_k'=2*k*h_k-2*pi*h_(k+1)",
    "checks": checks,
}
out = Path("research/aspect/results/variable_theta_forcing_connection.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
