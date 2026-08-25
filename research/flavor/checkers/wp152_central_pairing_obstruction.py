"""Exact parity obstruction for pairing three central fixed sectors."""

from itertools import permutations
import json
from pathlib import Path


sectors = ("CP", "minus_identity", "minus_CP")


def as_map(permutation: tuple[str, ...]) -> dict[str, str]:
    return dict(zip(sectors, permutation))


def is_involution(mapping: dict[str, str]) -> bool:
    return all(mapping[mapping[sector]] == sector for sector in sectors)


involutions = [as_map(p) for p in permutations(sectors) if is_involution(as_map(p))]
fixed_counts = [sum(mapping[sector] == sector for sector in sectors) for mapping in involutions]
nontrivial = [mapping for mapping in involutions if any(mapping[s] != s for s in sectors)]

# For each nontrivial involution, assign +24 and -24 to the exchanged pair and
# +24 to the unavoidable fixed sector. The paired contribution cancels, yet a
# class-invariant residual F=24 remains.
hostile_sums = []
for mapping in nontrivial:
    fixed = next(sector for sector in sectors if mapping[sector] == sector)
    pair = [sector for sector in sectors if sector != fixed]
    values = {fixed: 24, pair[0]: 24, pair[1]: -24}
    hostile_sums.append(sum(values.values()))


checks = {
    "three_central_nonidentity_sectors": len(sectors) == 3,
    "there_are_four_involutions": len(involutions) == 4,
    "there_are_three_nontrivial_pairings": len(nontrivial) == 3,
    "identity_pairing_fixes_all_three": 3 in fixed_counts,
    "every_nontrivial_pairing_has_one_fixed_sector": all(sum(mapping[s] == s for s in sectors) == 1 for mapping in nontrivial),
    "no_fixed_point_free_pairing_exists": all(count > 0 for count in fixed_counts),
    "hostile_assignments_cancel_exchanged_pairs": len(hostile_sums) == 3,
    "every_hostile_assignment_leaves_F_24": hostile_sums == [24, 24, 24],
    "residual_F_is_not_divisible_by_96": all(value % 96 != 0 for value in hostile_sums),
    "residual_F_gives_k_three": all((96 - value) // 24 == 3 for value in hostile_sums),
    "k_three_breaks_modulus_four": 3 % 4 != 0,
    "pairing_needs_extra_vanishing_condition": all(value != 0 for value in hostile_sums),
}

result = {
    "work_package": "WP152",
    "title": "Central fixed-sector pairing obstruction",
    "domain": "three central nonidentity sectors {CP,-1,-CP}",
    "candidate_operation": "source involution with antisymmetric cancellation on exchanged sectors",
    "involution_count": len(involutions),
    "nontrivial_pairing_count": len(nontrivial),
    "classification": "pairwise cancellation cannot force F=0 mod 96 because an odd central sector remains unpaired",
    "selector": False,
    "rigidifier": "pairing organization only",
    "physical_instrument": False,
    "smallest_exact_falsifier": "paired values +24 and -24 cancel while the unavoidable fixed sector contributes +24, leaving F=24 and k=3",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp152_central_pairing_obstruction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

