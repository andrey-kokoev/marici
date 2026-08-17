"""Audit the variance conflict between the V-map and conductor ring gluing."""


def main():
    # Truncate k[x] and k[y] at degree n only to count the underlying free
    # modules. Evaluation at zero is the conductor restriction.
    n = 6
    sheet_rank = n + 1
    conductor_rank = 1

    # The nodal/conductor fiber product consists of pairs with equal constant
    # term, hence has rank (n+1)+(n+1)-1.
    normalization_conductor_pullback_rank = 2 * sheet_rank - conductor_rank
    assert normalization_conductor_pullback_rank == 2 * n + 1

    # With the topology forced by the exceptional map, c<e+ and c<e-. An
    # ordinary sheaf is covariant along these specializations and therefore
    # needs C -> A+ and C -> A-. Compatible global tuples are determined only
    # by the single conductor value; this diagram does not recover the node.
    covariant_diagram_limit_rank = conductor_rank
    assert covariant_diagram_limit_rank == 1
    assert covariant_diagram_limit_rank != normalization_conductor_pullback_rank

    # Reversing the order permits the actual evaluation maps A+ -> C <- A-
    # and recovers the fiber product, but h<r+ would have to map to c<e+,
    # which is false in the reversed target order e+<c.
    source_relation = ("h", "r+")
    forced_images = {"h": "c", "r+": "e+"}
    reversed_target_relations = {("e+", "c"), ("e-", "c")}
    image_relation = (forced_images[source_relation[0]], forced_images[source_relation[1]])
    assert image_relation not in reversed_target_relations

    print("normalization_conductor_ring_diagram: A+ -> C <- A-")
    print(f"truncated_node_fiber_product_rank: {normalization_conductor_pullback_rank}")
    print("forced_geometric_order: c<e-, c<e+")
    print("ordinary_sheaf_ring_direction: C -> A-, C -> A+")
    print(f"ordinary_covariant_limit_rank: {covariant_diagram_limit_rank}")
    print("ordinary_ringed_left_morphism: IMPOSSIBLE")
    print("reversed_order_recovers_rings: YES")
    print("reversed_order_preserves_V_map: NO")
    print("required_left_leg: MIXED_VARIANCE_RECOLLEMENT_KERNEL")
    print("explicit_bimodule_kernel: NEXT_GATE")


if __name__ == "__main__":
    main()
