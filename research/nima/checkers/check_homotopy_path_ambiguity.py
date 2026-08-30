"""Minimal obstruction between two valid chain homotopies, over F_2."""

# Zero differentials imply the Hom differential is zero.
f_minus_g = 0
boundary_s = 0
boundary_t = 0

# S and T are degree -1 maps from <x> to <y>.
s = 1
t = 0
difference = (s - t) % 2

# There is no degree -2 Hom group, hence no possible higher boundary.
hom_minus_two_dimension = 0
higher_boundary = 0

assert boundary_s == boundary_t == f_minus_g
assert difference == 1
assert hom_minus_two_dimension == 0
assert higher_boundary != difference

witness = {
    "code": "homotopy_witness_ambiguity",
    "endpoint_maps_equal": True,
    "both_homotopies_valid": True,
    "difference_class_degree": -1,
    "difference_rank": 1,
    "higher_cell_available": False,
}

print("boundary(S):", boundary_s)
print("boundary(T):", boundary_t)
print("S-T:", difference)
print("rejection witness:", witness)
print("PASS: valid homotopies need not be coherently interchangeable")
