import json
from pathlib import Path


def partition(points, probes):
    buckets = {}
    for point in points:
        signature = tuple(probe(point) for probe in probes)
        buckets.setdefault(signature, []).append(point)
    return sorted((sorted(values) for values in buckets.values()), key=str)


def refines(fine, coarse):
    return all(any(set(block) <= set(parent) for parent in coarse) for block in fine)


def main():
    points = [(0, 0), (5, -5), (5, 2)]
    current = [lambda x: x[0] + x[1]]
    with_route_successor = current + [lambda x: x[0]]

    coarse = partition(points, current)
    fine = partition(points, with_route_successor)

    # Minimal classical model of equal one-use effects and different successors.
    # State is the current logical bit. Both instruments report that bit.
    qnd = lambda bit: (bit, bit)          # (record, successor state)
    flip = lambda bit: (bit, bit ^ 1)
    one_use_qnd = qnd(0)[0]
    one_use_flip = flip(0)[0]
    repeat_qnd = qnd(qnd(0)[1])[0]
    repeat_flip = qnd(flip(0)[1])[0]

    # Quotient representatives differing by an even repair; every descending
    # successor depends only on parity.
    repair_pair = (1, 3)
    descending = [lambda x: x % 2, lambda x: (x % 2) * 7]

    gates = {
        "same_present_readout_different_route_lifts": (
            current[0]((0, 0)) == current[0]((5, -5)) == 0
        ),
        "admissible_route_successor_detects_interference": (
            with_route_successor[1]((0, 0)) != with_route_successor[1]((5, -5))
        ),
        "successor_enlargement_refines_classes": refines(fine, coarse),
        "equal_one_use_effect_different_sequential_record": (
            one_use_qnd == one_use_flip and repeat_qnd != repeat_flip
        ),
        "descending_successors_do_not_detect_repairs": all(
            u(repair_pair[0]) == u(repair_pair[1]) for u in descending
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.operative-residue-future-separation.v1",
        "gates": gates,
        "current_partition": coarse,
        "successor_refined_partition": fine,
        "instrument_records": {
            "one_use": [one_use_qnd, one_use_flip],
            "repeat": [repeat_qnd, repeat_flip],
        },
        "conclusion": "residue is operative iff an authorized successor separates equal current readouts",
    }
    out = Path(__file__).parents[1] / "results" / "operative-residue-future-separation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
