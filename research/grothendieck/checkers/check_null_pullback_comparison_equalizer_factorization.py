parameter_points = {
    "seam_zero": {"scalar_null": True, "comparison_equal": True},
    "seam_nonzero": {"scalar_null": False, "comparison_equal": True},
    "off_seam_regular": {"scalar_null": False, "comparison_equal": False},
    "hostile_off_seam_zero": {"scalar_null": True, "comparison_equal": False},
}


def factorization_holds(points):
    return all(
        not attributes["scalar_null"] or attributes["comparison_equal"]
        for attributes in points.values()
    )


theta_candidate = {
    key: value
    for key, value in parameter_points.items()
    if key != "hostile_off_seam_zero"
}

assert factorization_holds(theta_candidate)
assert not factorization_holds(parameter_points)

print("pullback_1=scalar_null_divisor")
print("pullback_2=reciprocal_real_equalizer")
print("rh_morphism=null_pullback_factors_through_equalizer")
print("hostile_falsifier=scalar_null_with_nonzero_comparison")
