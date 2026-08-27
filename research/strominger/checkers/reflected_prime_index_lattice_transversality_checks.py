import json
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


def line(p, generator):
    return {
        ((t * generator[0]) % p, (t * generator[1]) % p)
        for t in range(p)
    }


def swap(vector):
    return vector[1], vector[0]


records = []
gates = []

for p in PRIMES:
    projective_generators = [(1, slope) for slope in range(p)] + [(0, 1)]
    seen_lines = set()
    for generator in projective_generators:
        source_line = frozenset(line(p, generator))
        if source_line in seen_lines:
            continue
        seen_lines.add(source_line)
        reflected_line = frozenset(swap(v) for v in source_line)
        invariant = source_line == reflected_line
        intersection_size = len(source_line & reflected_line)
        sum_set = {
            ((a[0] + b[0]) % p, (a[1] + b[1]) % p)
            for a in source_line for b in reflected_line
        }
        stable_packet_order = p if invariant else p * p
        expected_intersection = p if invariant else 1
        expected_sum = p if invariant else p * p
        passed = (
            intersection_size == expected_intersection
            and len(sum_set) == expected_sum
        )
        gates.append(passed)
        records.append({
            "prime": p,
            "generator": generator,
            "reflection_invariant": invariant,
            "mod_p_intersection_order": intersection_size,
            "mod_p_sum_order": len(sum_set),
            "stable_packet_order": stable_packet_order,
            "relative_eigenspace_order": p if (not invariant and p % 2 == 1) else None,
            "passed": passed,
        })

magnetic = next(
    record for record in records
    if record["prime"] == 7 and record["generator"] == (1, 5)
)
# (2,3) is projectively (1,5) modulo seven.
magnetic_gate = (
    not magnetic["reflection_invariant"]
    and magnetic["stable_packet_order"] == 49
    and magnetic["relative_eigenspace_order"] == 7
)
gates.append(magnetic_gate)

invariant_counts = {
    str(p): sum(
        1 for record in records
        if record["prime"] == p and record["reflection_invariant"]
    )
    for p in PRIMES
}

result = {
    "schema": "marici.strominger.reflected_prime_index_lattice_transversality.v1",
    "primes": PRIMES,
    "projective_line_records": records,
    "reflection_invariant_line_counts": invariant_counts,
    "magnetic_projective_generator": (1, 5),
    "magnetic_transverse_packet_order": magnetic["stable_packet_order"],
    "magnetic_relative_sector_order": magnetic["relative_eigenspace_order"],
    "semantic_fields": {
        "invariant_case": "one_chart_discriminant_order_p",
        "transverse_case": "stable_discriminant_order_p_squared",
        "odd_prime_relative_sector": "order_p",
        "p_equals_2_boundary": "symmetric_and_antisymmetric_characters_coincide",
    },
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "reflected_prime_index_lattice_transversality_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps({
    "schema": result["schema"],
    "primes": result["primes"],
    "records_checked": len(records),
    "reflection_invariant_line_counts": invariant_counts,
    "magnetic_transverse_packet_order": result["magnetic_transverse_packet_order"],
    "magnetic_relative_sector_order": result["magnetic_relative_sector_order"],
    "gates_passed": result["gates_passed"],
    "gates_total": result["gates_total"],
    "all_passed": result["all_passed"],
}, indent=2))
raise SystemExit(0 if all(gates) else 1)
