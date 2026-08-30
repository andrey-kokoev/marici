# First-order local model at a simple seam zero.
# Tangential coordinate y has d(0,y)=0 while X(0,y)=y.
# Normal coordinate x has d(x,0)=v*x while X(x,0)=a*x.

a = 3.0
v = (2.0, -1.0)

tangential_ratios = []
for y in (1.0, 0.5, 0.25, 0.125):
    x_value = y
    d_value = (0.0, 0.0)
    tangential_ratios.append(tuple(component / x_value for component in d_value))

normal_ratios = []
for x in (1.0, 0.5, 0.25, 0.125):
    x_value = a * x
    d_value = tuple(component * x for component in v)
    normal_ratios.append(tuple(component / x_value for component in d_value))

assert all(ratio == (0.0, 0.0) for ratio in tangential_ratios)
assert all(ratio == (v[0] / a, v[1] / a) for ratio in normal_ratios)
assert tangential_ratios[-1] != normal_ratios[-1]

print("ambient_continuous_multiplier=impossible_at_simple_seam_zero")
print("obstruction=direction_dependent_d_over_X_limit")
print("required_factorization_domain=null_pullback_only")
print("candidate_proof_type=green_or_boundary_state_identity")
