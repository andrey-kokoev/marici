unit_circle_points = (1, -1, 1j, -1j)

hb_forbidden = {rho for rho in unit_circle_points if abs(rho) == 1}
rh_forbidden = {-1}

assert rh_forbidden < hb_forbidden
assert 1j in hb_forbidden
assert 1j not in rh_forbidden
assert 1 + (-1) == 0
assert 1 + 1j != 0

print("rh_forbidden_projective_points=1")
print("de_branges_forbidden_locus=unit_circle")
print("strict_strength_gap=yes")
print("minimal_target=off_seam_antipode_exclusion")
