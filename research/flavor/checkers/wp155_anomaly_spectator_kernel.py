"""Exact projection audit for a Z4 anomaly with spectator residue."""

from itertools import product
import json
from pathlib import Path


flavor_packets = list(product(range(4), repeat=3))
spectator_residues = range(4)


def total_anomaly(packet: tuple[int, int, int], spectator: int) -> int:
    return (sum(packet) + spectator) % 4


closed_kernel = {packet for packet in flavor_packets if total_anomaly(packet, 0) == 0}
extended_kernel = {
    (packet, spectator)
    for packet in flavor_packets
    for spectator in spectator_residues
    if total_anomaly(packet, spectator) == 0
}
projected_flavor = {packet for packet, _ in extended_kernel}
even_spectator_kernel = {
    (packet, spectator)
    for packet in flavor_packets
    for spectator in (0, 2)
    if total_anomaly(packet, spectator) == 0
}
even_projection = {packet for packet, _ in even_spectator_kernel}

hostile_packet = (1, 1, 1)
hostile_spectator = 1

checks = {
    "flavor_space_has_64_packets": len(flavor_packets) == 64,
    "spectator_free_kernel_has_16_packets": len(closed_kernel) == 16,
    "extended_anomaly_free_space_has_64_packets": len(extended_kernel) == 64,
    "every_flavor_packet_has_unique_canceling_spectator": all(sum(1 for s in spectator_residues if total_anomaly(packet, s) == 0) == 1 for packet in flavor_packets),
    "extended_projection_is_surjective": projected_flavor == set(flavor_packets),
    "open_domain_selects_no_flavor_packet": len(projected_flavor) == 64,
    "hostile_wp153_packet_fails_closed_constraint": hostile_packet not in closed_kernel,
    "hostile_packet_is_repaired_by_spectator": total_anomaly(hostile_packet, hostile_spectator) == 0,
    "hostile_packet_reenters_projection": hostile_packet in projected_flavor,
    "even_spectators_give_partial_32_packet_projection": len(even_projection) == 32,
    "even_spectator_projection_is_not_target_kernel": even_projection != closed_kernel,
    "extended_kernel_projects_bijectively_but_not_selectively": len(extended_kernel) == len(projected_flavor) and len(projected_flavor) > len(closed_kernel),
}

result = {
    "work_package": "WP155",
    "title": "Anomaly spectator-kernel audit",
    "domain": "extended residues (f1,f2,f3;s) in (Z/4Z)^4",
    "constraint": "f1+f2+f3+s=0 mod 4",
    "closed_flavor_kernel_size": len(closed_kernel),
    "extended_kernel_size": len(extended_kernel),
    "projected_flavor_size": len(projected_flavor),
    "classification": "faithful total-anomaly constraint does not select flavor on an open spectator domain",
    "selector": "only on a frozen spectator-free domain",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": "f=(1,1,1) is rejected at s=0 but becomes anomaly-free with spectator residue s=1",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp155_anomaly_spectator_kernel.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
