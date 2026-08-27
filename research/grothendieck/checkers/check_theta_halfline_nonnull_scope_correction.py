regions = ("left", "seam", "right")

nonnull_reason = {
    "left": "H(z)_minimum_phase",
    "seam": "H(z)_positive_sine_or_mass",
    "right": "H(-z)_reflected_minimum_phase",
}

assert set(regions) == set(nonnull_reason)

print("full_lift_nonnull=all_complex_z")
print("scalar_zero_type=antipodal_nonzero_incidence")
print("rh_target=confine_projective_antipode_to_seam")
print("common_zero_target=withdrawn_as_rh_reduction")
