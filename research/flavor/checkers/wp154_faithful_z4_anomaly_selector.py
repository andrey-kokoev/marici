"""Exact kernel audit for permutation-invariant faithful Z4 characters."""

from itertools import product
from math import gcd
import json
from pathlib import Path


packets = list(product(range(4), repeat=3))


def anomaly(coefficient: int, packet: tuple[int, int, int]) -> int:
    return coefficient * sum(packet) % 4


def kernel(coefficient: int) -> set[tuple[int, int, int]]:
    return {packet for packet in packets if anomaly(coefficient, packet) == 0}


faithful_coefficients = [coefficient for coefficient in range(4) if gcd(coefficient, 4) == 1]
kernels = {coefficient: kernel(coefficient) for coefficient in range(4)}
target_kernel = {packet for packet in packets if sum(packet) % 4 == 0}
hostile_diagonal = (2, 2, 2)

checks = {
    "packet_space_has_64_elements": len(packets) == 64,
    "invariant_character_family_has_four_coefficients": len(kernels) == 4,
    "faithful_coefficients_are_one_and_three": faithful_coefficients == [1, 3],
    "faithful_kernels_coincide": kernels[1] == kernels[3],
    "faithful_kernel_is_target_sum_kernel": kernels[1] == target_kernel,
    "faithful_kernel_has_16_elements": len(target_kernel) == 16,
    "faithful_kernel_is_proper": 0 < len(target_kernel) < len(packets),
    "wp153_hostile_packet_is_rejected": (1, 1, 1) not in target_kernel,
    "aligned_kernel_requires_amplitude_zero_mod4": [a for a in range(4) if (a, a, a) in target_kernel] == [0],
    "nonfaithful_even_character_has_32_element_kernel": len(kernels[2]) == 32,
    "nonfaithful_character_accepts_hostile_diagonal": hostile_diagonal in kernels[2] and hostile_diagonal not in target_kernel,
    "trivial_character_selects_nothing": len(kernels[0]) == 64,
}

result = {
    "work_package": "WP154",
    "title": "Faithful Z4 anomaly-selector audit",
    "domain": "central fixed-set residue packets f in (Z/4Z)^3",
    "candidate_family": "permutation-invariant linear characters A_c(f)=c sum(f) mod 4",
    "faithful_coefficients": faithful_coefficients,
    "faithful_kernel_size": len(target_kernel),
    "ambient_size": len(packets),
    "classification": "mathematical proper-subspace selector conditional on a source-authorized faithful Z4 anomaly character",
    "selector": "conditional",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": "dropping faithfulness permits c=2, whose 32-element kernel accepts f=(2,2,2) although sum(f)=2 mod 4",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp154_faithful_z4_anomaly_selector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

