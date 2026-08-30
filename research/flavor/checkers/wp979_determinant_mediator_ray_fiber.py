"""Exact WP979 determinant-mediator coefficient-ray fiber checker."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

lambda_aux = Fraction(1)
gamma = Fraction(8)
mu = Fraction(1)
m_a_squared = Fraction(1)
crossing = Fraction(24696)

def ray_ratio(m_s_squared):
    return gamma**2 * mu**4 / (m_s_squared * m_a_squared**5)

packets = (
    {"m_s_squared": Fraction(1), "ratio": ray_ratio(Fraction(1))},
    {"m_s_squared": Fraction(1, 512), "ratio": ray_ratio(Fraction(1, 512))},
)
stability_margin = lambda_aux - abs(gamma) / 16

checks = {
    "both_scalar_masses_are_positive": all(packet["m_s_squared"] > 0 for packet in packets),
    "both_packets_share_strict_coercivity_margin": stability_margin == Fraction(1, 2),
    "benchmark_packet_ratio_is_sixty_four": packets[0]["ratio"] == 64,
    "hostile_packet_ratio_is_32768": packets[1]["ratio"] == 32768,
    "first_packet_lies_below_crossing": packets[0]["ratio"] < crossing,
    "second_packet_lies_above_crossing": packets[1]["ratio"] > crossing,
    "coercivity_does_not_select_crossing_side": packets[0]["ratio"] < crossing < packets[1]["ratio"],
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.determinant-mediator-ray-fiber.v1",
    "work_package": "WP979",
    "status": "PASS",
    "checks": checks,
    "domain": "positive WP977 auxiliary masses and strict auxiliary coercivity",
    "quotient": "source-parameter packets modulo field relabeling only",
    "fixed_parameters": {"lambda": "1", "gamma": "8", "mu": "1", "m_A_squared": "1"},
    "stability_margin": str(stability_margin),
    "crossing_ratio": str(crossing),
    "packets": [
        {"m_s_squared": str(packet["m_s_squared"]), "k_over_q": str(packet["ratio"])}
        for packet in packets
    ],
    "classification": "operator constructor with a continuous coefficient-ray fiber; not a numerical selector",
    "remaining_gate": "independently derive the mass/coupling relation and prove controlled elimination plus global vacuum",
}
out = ROOT / "results" / "wp979_determinant_mediator_ray_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
