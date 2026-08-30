"""Finite commutator falsifier for a typed direct-image reducer."""

# Matrices over F_2, represented here in the one-dimensional minimal case.
d_source = 1   # D_1(h) = k
d_target = 1   # Dbar_1(hbar) = kbar
r_degree_1 = 1 # retain the visible pairwise cell
r_degree_2 = 0 # erase the triple target

left = (d_target * r_degree_1) % 2
right = (r_degree_2 * d_source) % 2
commutator = (left - right) % 2

assert left == 1
assert right == 0
assert commutator == 1

witness = {
    "code": "direct_image_not_chain_map",
    "degree": 1,
    "source_basis": "h",
    "residual_basis": "k_bar",
    "residual": commutator,
}

print("Dbar R(h):", left)
print("R D(h):", right)
print("commutator:", commutator)
print("rejection witness:", witness)
print("PASS: visible pairwise preservation does not imply coherent direct image")
