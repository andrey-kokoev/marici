"""Exact fixed-point correction audit for an order-96 topology action."""

from fractions import Fraction
import json
from pathlib import Path


GROUP_ORDER = 96


def packet(chi_quotient: int, fixed_sum: int) -> dict[str, object]:
    # Burnside Euler formula: 96 chi(X/G) = chi(X) + F.
    chi_x = GROUP_ORDER * chi_quotient - fixed_sum
    k = Fraction(chi_x, 24)
    integral = k.denominator == 1
    k_int = int(k) if integral else None
    accessible = integral and k_int > 0 and Fraction(1, k_int) < Fraction(9, 16)
    return {
        "chi_quotient": chi_quotient,
        "fixed_sum": fixed_sum,
        "chi_x": chi_x,
        "k": k_int if integral else str(k),
        "integral": integral,
        "modulus_four": integral and k_int % 4 == 0,
        "accessible": accessible,
    }


residue_packets = [packet(1, 24 * residue) for residue in range(4)]
free_packet = residue_packets[0]
inaccessible_packet = residue_packets[3]
restored_packet = packet(2, 96)

checks = {
    "free_packet_gives_k_four": free_packet["k"] == 4,
    "free_packet_preserves_modulus_four": free_packet["modulus_four"],
    "fixed_sum_24_gives_k_three": residue_packets[1]["k"] == 3,
    "fixed_sum_48_gives_k_two": residue_packets[2]["k"] == 2,
    "fixed_sum_72_gives_k_one": inaccessible_packet["k"] == 1,
    "all_four_residue_packets_are_integral": all(p["integral"] for p in residue_packets),
    "only_zero_residue_preserves_modulus_four": [p["modulus_four"] for p in residue_packets] == [True, False, False, False],
    "fixed_corrections_span_all_k_residues_mod_four": {int(p["k"]) % 4 for p in residue_packets} == {0, 1, 2, 3},
    "fixed_correction_can_restore_inaccessible_sector": not inaccessible_packet["accessible"],
    "correction_multiple_96_can_preserve_modulus": restored_packet["k"] == 4 and restored_packet["modulus_four"],
    "modulus_condition_is_fixed_sum_divisible_by_96": all((24 * r) % 96 == 0 if r % 4 == 0 else (24 * r) % 96 != 0 for r in range(8)),
    "group_order_alone_does_not_fix_accessibility": free_packet["accessible"] != inaccessible_packet["accessible"],
}

result = {
    "work_package": "WP150",
    "title": "Fixed-point Euler-correction audit",
    "domain": "finite order-96 cellular actions with integral k=chi(X)/24",
    "identity": "k=4 chi(X/G)-F/24, F=sum_(g!=e) chi(X^g)",
    "contextual_partition": {
        "F/24 mod 4 = 0": "k=0 mod 4",
        "F/24 mod 4 = 1": "k=3 mod 4",
        "F/24 mod 4 = 2": "k=2 mod 4",
        "F/24 mod 4 = 3": "k=1 mod 4",
    },
    "classification": "fixed-point-corrected quotient does not select k in 4N unless an additional F=0 mod 96 law is sourced",
    "selector": False,
    "rigidifier": "order-96 presentation grammar only",
    "physical_instrument": False,
    "smallest_exact_falsifier": "chi(X/G)=1 and F=24 give chi(X)=72 and k=3, not k=0 mod 4",
    "hostile_accessibility_falsifier": "chi(X/G)=1 and F=72 give k=1, which is inaccessible",
    "packets": residue_packets,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp150_fixed_point_euler_correction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

