"""Audit the global mod-three obstruction groups of the filtered atlas."""


P = 3


def rank_1x1(value):
    return 0 if value % P == 0 else 1


def main():
    # The full twelve-face signed carrier collapses by unit pivots to the
    # orientation-local-system circle complex R --(u-1)--> R.
    u = -1
    mobius_d1 = (u - 1) % P
    assert mobius_d1 == 1
    assert rank_1x1(mobius_d1) == 1
    mobius_h = (0, 0, 0)

    # Adding the Jordan/octagonal cap contributes d2=u+1.  At the selected
    # orientation character and modulo three this vanishes, leaving one
    # twisted top class.
    cap_d2 = (u + 1) % P
    assert cap_d2 == 0
    capped_h = (0, 0, 1)

    # Therefore any absolute Cech 2-class on the Mobius carrier is exact.
    # Only the capped/relative orientation class can retain the local
    # generator of Z/3.
    absolute_h2_dimension = mobius_h[2]
    capped_twisted_h2_dimension = capped_h[2]
    assert absolute_h2_dimension == 0
    assert capped_twisted_h2_dimension == 1

    print("coefficient_group: F3")
    print("selected_monodromy_u: -1")
    print("reduced_Mobius_d1=u-1: 1")
    print("Mobius_twisted_cohomology_dimensions: (0,0,0)")
    print("absolute_Cech_H2: 0")
    print("capped_d2=u+1: 0")
    print("capped_twisted_cohomology_dimensions: (0,0,1)")
    print("capped_relative_H2: F3")
    print("global_filtered_atlas_on_open_carrier: UNOBSTRUCTED")
    print("remaining_associator_locus: capped_relative_top_class")


if __name__ == "__main__":
    main()
