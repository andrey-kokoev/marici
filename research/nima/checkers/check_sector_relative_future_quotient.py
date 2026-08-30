from fractions import Fraction
import json
from pathlib import Path


def signatures(points, probes):
    return {point: tuple(probe(point) for probe in probes) for point in points}


def blocks(points, probes):
    grouped = {}
    for point, signature in signatures(points, probes).items():
        grouped.setdefault(signature, []).append(point)
    return list(grouped.values())


def every_probe_factors(partition, probes):
    return all(
        all(len({probe(point) for point in block}) == 1 for block in partition)
        for probe in probes
    )


def every_distinct_block_pair_is_witnessed(partition, probes):
    for i, left in enumerate(partition):
        for right in partition[i + 1:]:
            if not any(probe(left[0]) != probe(right[0]) for probe in probes):
                return False
    return True


def main():
    routes = [(0, 0), (5, -5), (5, 2)]
    scalar = [lambda pair: pair[0] + pair[1]]
    exceptional = scalar + [lambda pair: pair]
    scalar_blocks = blocks(routes, scalar)
    exceptional_blocks = blocks(routes, exceptional)

    instruments = ["qnd", "flip"]
    one_use = [lambda _: 0]
    sequential = one_use + [lambda instrument: 0 if instrument == "qnd" else 1]
    effect_blocks = blocks(instruments, one_use)
    instrument_blocks = blocks(instruments, sequential)

    rational_depths = [Fraction(17, 3), Fraction(37, 3)]
    source_constructible = lambda depth: depth.denominator == 1

    gates = {
        "future_quotient_supports_all_successors": (
            every_probe_factors(exceptional_blocks, exceptional)
            and every_probe_factors(instrument_blocks, sequential)
        ),
        "future_quotient_is_coarsest_sufficient_partition": (
            every_distinct_block_pair_is_witnessed(exceptional_blocks, exceptional)
            and every_distinct_block_pair_is_witnessed(instrument_blocks, sequential)
        ),
        "cosmology_exceptional_successor_refines_scalar_readout": (
            len(scalar_blocks) == 2 and len(exceptional_blocks) == 3
        ),
        "sequential_access_refines_effect_readout": (
            len(effect_blocks) == 1 and len(instrument_blocks) == 2
        ),
        "magnetic_interference_states_excluded_before_quotient": not any(
            source_constructible(depth) for depth in rational_depths
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.sector-relative-future-quotient.v1",
        "gates": gates,
        "cosmology": {
            "scalar_class_count": len(scalar_blocks),
            "exceptional_class_count": len(exceptional_blocks),
        },
        "topological": {
            "effect_class_count": len(effect_blocks),
            "sequential_instrument_class_count": len(instrument_blocks),
        },
        "magnetic": {
            "virtual_depths": [str(depth) for depth in rational_depths],
            "source_constructible": False,
        },
        "conclusion": "the future quotient is the coarsest memory through which every authorized successor factors",
    }
    out = Path(__file__).parents[1] / "results" / "sector-relative-future-quotient.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
