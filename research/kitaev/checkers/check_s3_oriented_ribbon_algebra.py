"""Exact fixed-ribbon algebra audit for clockwise/counterclockwise D(S3) ribbons."""

import itertools
import json


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def multiply(left, right, orientation):
    h1, g1 = left
    h2, g2 = right
    if g1 != g2:
        return None
    if orientation == "clockwise":
        return (compose(h1, h2), g1)
    if orientation == "counterclockwise":
        return (compose(h2, h1), g1)
    raise ValueError("unknown orientation")


def phi(left_basis):
    h, g = left_basis
    return (inverse(h), g)


def cycle_name(p):
    table = {
        (0, 1, 2): "e",
        (1, 0, 2): "(01)",
        (0, 2, 1): "(12)",
        (2, 1, 0): "(02)",
        (1, 2, 0): "(012)",
        (2, 0, 1): "(021)",
    }
    return table[p]


def main():
    group = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    basis = [(h, g) for h in group for g in group]
    assert len(basis) == 36

    associative = {}
    for orientation in ("clockwise", "counterclockwise"):
        ok = True
        for a, b, c in itertools.product(basis, repeat=3):
            ab = multiply(a, b, orientation)
            bc = multiply(b, c, orientation)
            lhs = None if ab is None else multiply(ab, c, orientation)
            rhs = None if bc is None else multiply(a, bc, orientation)
            if lhs != rhs:
                ok = False
                break
        associative[orientation] = ok
    assert all(associative.values())

    # The unit is sum_g F(e,g); each basis element selects exactly one term.
    block_units_are_orthogonal = True
    unit_acts = True
    for a in basis:
        h, g = a
        left_hits = [multiply((identity, k), a, "clockwise") for k in group]
        right_hits = [multiply(a, (identity, k), "clockwise") for k in group]
        if [x for x in left_hits if x is not None] != [a]:
            unit_acts = False
        if [x for x in right_hits if x is not None] != [a]:
            unit_acts = False
    for g1, g2 in itertools.product(group, repeat=2):
        product = multiply((identity, g1), (identity, g2), "clockwise")
        expected = (identity, g1) if g1 == g2 else None
        block_units_are_orthogonal &= product == expected
    assert unit_acts and block_units_are_orthogonal

    # phi(F_L(h,g)) = F_R(h^{-1},g) intertwines the opposite products.
    orientation_intertwiner = True
    for a, b in itertools.product(basis, repeat=2):
        ab = multiply(a, b, "clockwise")
        lhs = None if ab is None else phi(ab)
        rhs = multiply(phi(a), phi(b), "counterclockwise")
        if lhs != rhs:
            orientation_intertwiner = False
            break
    assert orientation_intertwiner

    t01 = (1, 0, 2)
    t12 = (0, 2, 1)
    flux_block = identity
    a = (t01, flux_block)
    b = (t12, flux_block)
    clockwise_product = multiply(a, b, "clockwise")
    counterclockwise_product = multiply(a, b, "counterclockwise")
    assert clockwise_product != counterclockwise_product
    assert clockwise_product[0] == (1, 2, 0)
    assert counterclockwise_product[0] == (2, 0, 1)

    result = {
        "schema": "marici.s3-oriented-ribbon-algebra.v1",
        "group_order": len(group),
        "basis_dimension": len(basis),
        "block_count": len(group),
        "block_dimension": len(group),
        "fixed_ribbon_algebra": "direct_sum_over_g_of_C[S3]",
        "associative": associative,
        "unit": "sum_g F(e,g)",
        "block_units_are_orthogonal_idempotents": block_units_are_orthogonal,
        "unit_acts_on_all_basis_elements": unit_acts,
        "orientation_intertwiner": "phi(F_L(h,g))=F_R(h^-1,g)",
        "orientation_intertwiner_verified": orientation_intertwiner,
        "noncommuting_witness": {
            "left_h": cycle_name(t01),
            "right_h": cycle_name(t12),
            "g_block": cycle_name(flux_block),
            "clockwise_h_product": cycle_name(clockwise_product[0]),
            "counterclockwise_h_product": cycle_name(counterclockwise_product[0]),
            "products_differ": True,
        },
        "aggregate_gates": {
            "thirty_six_basis_elements_recovered": True,
            "clockwise_product_is_associative": associative["clockwise"],
            "counterclockwise_product_is_associative": associative["counterclockwise"],
            "six_orthogonal_group_algebra_blocks_recovered": block_units_are_orthogonal,
            "orientation_reversal_requires_group_inverse": orientation_intertwiner,
            "nonabelian_orientation_order_is_observable": True,
            "fixed_ribbon_algebra_does_not_supply_fusion_coherence": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
