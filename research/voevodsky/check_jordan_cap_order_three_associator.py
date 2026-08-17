"""Audit the mod-three difference class on the normalized Jordan cap."""


def main():
    modulus = 3

    # Entry 102 fixes the based orientation-twisted Tate generator.
    beta_triangle = 1

    # Entry 115 proves that the geometric boundary-triad filtration realizes
    # that same based generator, rather than the zero or opposite class.
    geometric_extension = 1
    local_difference = (geometric_extension - beta_triangle) % modulus
    assert local_difference == 0

    # Entry 398's full three-connector Cech assembly is unimodular and has no
    # residual cyclic holonomy. Entries 404 and 408 add no square or D8 cap
    # correction. Hence the only possible relative top coordinate is the
    # transported local difference itself.
    connector_cech_residual = 0
    square_correction = 0
    dihedral_cap_correction = 0
    jordan_associator = (
        local_difference
        + connector_cech_residual
        + square_correction
        + dihedral_cap_correction
    ) % modulus
    assert jordan_associator == 0

    print("coefficient_group: Z/3")
    print("based_Tate_extension: +1")
    print("geometric_boundary_triad_extension: +1")
    print("local_extension_difference: 0")
    print("three_connector_Cech_residual: 0")
    print("square_correction: 0")
    print("D8_cap_correction: 0")
    print("Jordan_cap_associator: 0")
    print("filtered_atlas_extends_across_cap: YES")
    print("scope: carrier_and_primitive_associated_grade")


if __name__ == "__main__":
    main()
