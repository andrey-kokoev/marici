"""Exact Weyl-area and finite operator checks for the coupled mechanism."""

import sympy as sp

energy, a, b = sp.symbols("E a b", positive=True)
x = sp.symbols("x", positive=True)
area = sp.integrate(energy / x - b, (x, a, energy / b))
expected_area = energy * sp.log(energy / (a * b)) - energy + a * b
assert sp.simplify(area - expected_area) == 0

weyl = sp.simplify(expected_area.subs(a * b, 2 * sp.pi) / (2 * sp.pi))
expected_weyl = energy / (2 * sp.pi) * sp.log(energy / (2 * sp.pi)) - energy / (2 * sp.pi) + 1
assert sp.simplify(weyl - expected_weyl) == 0

# Finite shadows: a confining diagonal sector plus a symmetric interaction
# stays self-adjoint; multiplication by i is skew-adjoint.
for rank in (3, 5, 8):
    h0 = sp.diag(*[index + 1 for index in range(rank)])
    interaction = sp.zeros(rank)
    for index in range(rank - 1):
        interaction[index, index + 1] = sp.Rational(1, 3)
        interaction[index + 1, index] = sp.Rational(1, 3)
    hamiltonian = h0 + interaction
    zero_coordinate = sp.I * hamiltonian
    assert hamiltonian.H == hamiltonian
    assert zero_coordinate.H == -zero_coordinate
    print(f"rank={rank} coupled_self_adjoint=True zero_coordinate_skew_adjoint=True")

# A nonsymmetric hostile interaction breaks the adjoint identity.
hostile = sp.Matrix([[1, 1], [0, 2]])
assert hostile.H != hostile
assert (sp.I * hostile).H != -sp.I * hostile

print(f"phase_space_area={area}")
print(f"smooth_Weyl_count={weyl}")
print("constant_boundary_correction_needed=-1/8")
print("nonsymmetric_prime_interaction_breaks_skew_adjointness=True")
print("Xi_operator_constructed=False")

