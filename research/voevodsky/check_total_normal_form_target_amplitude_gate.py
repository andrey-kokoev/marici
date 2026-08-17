"""Audit the amplitude gate between the tensor and facewise PC models."""

from math import comb


def support(profile):
    return [degree for degree, rank in enumerate(profile) if rank]


def main():
    # K6 has faces indexed by dissection size 0,1,2,3.
    face_counts = [1, 9, 21, 14]
    target = [0, 0, 0, 0]
    for face_size, count in enumerate(face_counts):
        for circle_size in range(face_size + 1):
            degree = 3 - face_size + circle_size
            target[degree] += count * comb(face_size, circle_size)
    assert target == [14, 63, 93, 45]
    assert sum(target) == 215

    # The two endpoint faces are two size-three Boolean normal packets.
    endpoints = [2 * comb(3, degree) for degree in range(4)]
    endpoint_quotient = [
        target_degree - endpoint_degree
        for target_degree, endpoint_degree in zip(target, endpoints)
    ]
    assert endpoints == [2, 6, 6, 2]
    assert endpoint_quotient == [12, 57, 87, 43]

    tensor_normal_form = [1, 6, 15, 20, 15, 6, 1]
    assert support(tensor_normal_form) == list(range(7))
    assert support(endpoint_quotient) == list(range(4))

    # A degree-preserving injection after one global shift requires every
    # occupied source degree to land in an occupied target degree.
    admissible_shifts = []
    for shift in range(-12, 13):
        if all(
            0 <= degree + shift < len(endpoint_quotient)
            and endpoint_quotient[degree + shift] >= rank
            for degree, rank in enumerate(tensor_normal_form)
            if rank
        ):
            admissible_shifts.append(shift)
    assert admissible_shifts == []

    print("absolute_PC_degree_ranks: 14,63,93,45")
    print("endpoint_packet_degree_ranks: 2,6,6,2")
    print("endpoint_quotient_degree_ranks: 12,57,87,43")
    print("tensor_normal_form_degree_ranks: 1,6,15,20,15,6,1")
    print("source_amplitude: 6")
    print("target_amplitude: 3")
    print("degree_shifted_strict_embedding: IMPOSSIBLE")
    print("required_operation: EXTRAORDINARY_TRANSFER_OR_COLLAPSE")
    print("full_loaded_chain_map: STILL_UNCONSTRUCTED")


if __name__ == "__main__":
    main()
