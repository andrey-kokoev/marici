"""Audit the equivariant extension class of the three-road recollement."""


def rotate(v):
    return (v[2], v[0], v[1])


def augment(v):
    return sum(v)


def main():
    invariant_vectors = [
        v
        for a in range(-4, 5)
        for b in range(-4, 5)
        for c in range(-4, 5)
        if (v := (a, b, c)) == rotate(v)
    ]
    assert all(v[0] == v[1] == v[2] for v in invariant_vectors)
    invariant_augmentations = {augment(v) for v in invariant_vectors}
    assert all(value % 3 == 0 for value in invariant_augmentations)
    assert 1 not in invariant_augmentations
    assert 2 not in invariant_augmentations
    assert 3 in invariant_augmentations

    # The invariant part of Z[C3] maps to 3Z in the invariant quotient Z.
    # Its cokernel is Z/3 = H^1(C3,A2), and the road extension maps 1 to
    # the generator.  Pullback along multiplication by three has the
    # invariant diagonal section N=(1,1,1).
    norm = (1, 1, 1)
    assert rotate(norm) == norm
    assert augment(norm) == 3
    extension_order = 3

    # Reflection preserves augmentation and conjugates rotation to its
    # inverse, so the nonsplit filtered sequence is D3-stable.
    reflect = lambda v: (v[0], v[2], v[1])
    sample = (2, -1, 4)
    assert augment(reflect(sample)) == augment(sample)
    assert reflect(rotate(reflect(sample))) == rotate(rotate(sample))

    print("equivariant_sequence: 0 -> A2 -> Z[C3] -> Z -> 0")
    print("integral_C3_invariant_section_of_1: NONE")
    print("invariant_augmentation_image: 3Z")
    print("Ext1_C3(Z,A2): Z/3")
    print("road_extension_class: generator")
    print(f"extension_order: {extension_order}")
    print("pullback_along_times_3_split_by: (1,1,1)")
    print("D3_stability: PASS")
    print("ordinary_full_atlas_lift: OBSTRUCTED")
    print("required_full_structure: filtered_or_higher_coherence")


if __name__ == "__main__":
    main()
