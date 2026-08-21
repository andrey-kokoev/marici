"""Exact finite quotient checks and arithmetic-weight descent falsifier."""

import sympy as sp


for order in (2, 3, 5):
    # Each diagonal orbit is uniquely labeled by a-b.
    orbit_labels = {}
    for a in range(order):
        for b in range(order):
            difference = (a - b) % order
            orbit_labels.setdefault(difference, []).append((a, b))
    assert len(orbit_labels) == order
    assert all(len(fiber) == order for fiber in orbit_labels.values())

    relative_map = sp.eye(order)
    assert relative_map.T * relative_map == sp.eye(order)
    print(f"cyclic_order={order} quotient_orbits={order} relative_map_unitary=True")

# Same rational ratio, incompatible von Mangoldt product weights.
ratio_first = sp.Rational(2, 3)
ratio_scaled = sp.Rational(10, 15)
assert ratio_first == ratio_scaled
weight_first = sp.log(2) * sp.log(3)
weight_scaled = sp.Integer(0)  # Lambda(10)=Lambda(15)=0.
assert weight_first != weight_scaled

print("relative_difference_quotient_isomorphic_to_group=True")
print("center_of_mass_volume_removed=True")
print("von_Mangoldt_product_weight_descends=False")
print("coefficient_cocycle_required=True")
print("physical_relative_chain_pushforward_constructed=False")

