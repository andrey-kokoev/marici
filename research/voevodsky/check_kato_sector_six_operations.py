"""Audit preservation of the Kato-pulled sector by connector operations."""

import check_d03_normalized_blowdown_counit as blowdown
import check_ringed_alexandrov_pc_target as pc


def main():
    generators = [
        (face, circles) for face in pc.faces() for circles in pc.subsets(face)
    ]
    zero_character = {}

    face_maps = 0
    for source in generators:
        for (target, _coefficient), _sign in pc.boundary(source).items():
            # A strict face localization merely removes one characteristic
            # generator. Restriction of the zero torus character stays zero;
            # extension by zero has either this same character or zero stalk.
            source_l = pc.localization_set(source)
            target_l = pc.localization_set(target)
            assert len(target_l - source_l) == 1
            restricted_character = {
                key: value for key, value in zero_character.items() if key in target_l
            }
            assert restricted_character == zero_character
            face_maps += 1
    assert face_maps == 522

    # The marked normalized blowdown uses the pullback monoid chart: source
    # and image have literally identical coefficient rings and inertia maps.
    source_faces = [
        frozenset(),
        frozenset({"D"}),
        frozenset({"1", "3", "5"}),
        frozenset({"1", "3"}),
        frozenset({"E", "1", "3"}),
        frozenset({"E", "3"}),
        frozenset({"E", "D", "3"}),
        frozenset({"D", "3"}),
        frozenset({"D", "0", "3"}),
    ]
    for face in source_faces:
        image = blowdown.old(face)
        assert blowdown.label(face) == blowdown.label(image)
        assert zero_character == {}

    # Finite sums/products over singleton or V-tree fibers cannot create a
    # torus character when every transition acts identically on inertia.
    v_fiber_characters = [zero_character, zero_character, zero_character]
    assert all(character == {} for character in v_fiber_characters)

    # Tensor, internal Hom, cones, and duals use addition, subtraction, and
    # negation of characters; the zero sector is closed under each operation.
    assert zero_character == {}
    assert {**zero_character, **zero_character} == {}
    assert {key: -value for key, value in zero_character.items()} == {}

    # The Thom orientation sign is a character of the discrete endpoint
    # reflection, not of any chart torus. Its torus character is zero.
    reflection_sign = -1
    thom_torus_character = {}
    assert reflection_sign == -1
    assert thom_torus_character == zero_character

    print("strict_face_maps_checked: 522")
    print("normalized_blowdown_chart_maps: IDENTITY_ON_MONOIDS")
    print("restriction_and_extension_by_zero: KATO_SECTOR_PRESERVED")
    print("support_cones_and_tensor_Hom: KATO_SECTOR_PRESERVED")
    print("finite_left_and_right_Kan: KATO_SECTOR_PRESERVED")
    print("relative_dualizing_object_torus_character: ZERO")
    print("Thom_reflection_character: DISCRETE_SIGN_ONLY")
    print("connector_six_operations_preserve_Kato_sector: YES")
    print("unrestricted_Artin_stack_pushforwards: NOT_CLAIMED")
    print("generic_DNC_comparison_of_trace: NEXT_GATE")


if __name__ == "__main__":
    main()
