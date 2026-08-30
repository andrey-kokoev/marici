"""Exact minimum redundancy for the eight-valued D(S3) sector record."""

import itertools
import json


def bits(x, n):
    return tuple((x >> i) & 1 for i in range(n))


def distance(a, b):
    return sum(x != y for x, y in zip(a, b))


def main():
    residues = (0, 1, 2, 3, 6, 7, 4, 5)
    raw = [bits(r, 3) for r in residues]
    assert len(set(raw)) == 8
    raw_mislabels = 0
    for word in raw:
        for i in range(3):
            corrupt = list(word); corrupt[i] ^= 1
            assert tuple(corrupt) in raw
            raw_mislabels += 1
    assert raw_mislabels == 24

    # Columns are 100,010,001,110,101,011: the length-seven simplex code
    # punctured at column 111.
    columns = ((1, 0, 0), (0, 1, 0), (0, 0, 1),
               (1, 1, 0), (1, 0, 1), (0, 1, 1))
    code = []
    for message in itertools.product((0, 1), repeat=3):
        codeword = tuple(sum(m * c for m, c in zip(message, col)) % 2
                         for col in columns)
        code.append(codeword)
    assert len(set(code)) == 8
    pair_distances = [distance(a, b) for i, a in enumerate(code)
                      for b in code[i + 1:]]
    assert min(pair_distances) == 3

    corrupted = {}
    for label, word in enumerate(code):
        for i in range(6):
            received = list(word); received[i] ^= 1
            received = tuple(received)
            nearest = [j for j, candidate in enumerate(code)
                       if distance(received, candidate) <= 1]
            assert nearest == [label]
            assert received not in corrupted or corrupted[received] == label
            corrupted[received] = label
    assert len(corrupted) == 48

    hamming_bound = {n: 8 * (n + 1) <= 2 ** n for n in range(3, 7)}
    assert hamming_bound == {3: False, 4: False, 5: False, 6: True}

    result = {
        "schema": "marici.s3-sector-record-redundancy.v1",
        "raw_record": {
            "bits": 3,
            "labels": 8,
            "single_bit_flips": 24,
            "single_bit_flips_that_mislabel": raw_mislabels,
            "minimum_distance": 1,
        },
        "protected_record": {
            "code": "punctured_binary_simplex_[6,3,3]",
            "generator_columns": [list(c) for c in columns],
            "bits": 6,
            "labels": 8,
            "minimum_distance": min(pair_distances),
            "single_bit_corruptions_uniquely_decoded": len(corrupted),
            "additional_record_bits": 3,
        },
        "lower_bound": {
            "radius_one_hamming_bound_by_length": {
                str(n): value for n, value in hamming_bound.items()
            },
            "minimum_length": 6,
        },
        "scope_boundary": {
            "protects": "one_bit_flip_after_correct_label_encoding",
            "does_not_protect": [
                "controlled_power_fault",
                "inverse_F8_fault",
                "wrong_label_before_encoding",
                "encoder_gate_fault_without_fault_tolerant_schedule",
            ],
        },
        "aggregate_gates": {
            "all_raw_single_bit_flips_mislabel": True,
            "length_at_most_five_is_impossible_by_hamming_bound": True,
            "length_six_distance_three_code_exists": True,
            "all_forty_eight_single_bit_corruptions_decode_uniquely": True,
            "record_protection_does_not_supply_controlled_powers": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

