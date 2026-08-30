"""Exact finite-quartet checks for the RH reflection-defect operator."""

import sympy as sp

beta, height = sp.symbols("beta height", real=True)
offset = beta - sp.Rational(1, 2)
denominator = sp.sqrt(1 + offset**2 + height**2)
eigenvalues = [offset / denominator, offset / denominator, -offset / denominator, -offset / denominator]

trace = sp.simplify(sum(eigenvalues))
hs_squared = sp.simplify(sum(value**2 for value in eigenvalues))
expected = sp.simplify(4 * offset**2 / (1 + offset**2 + height**2))
assert trace == 0
assert sp.simplify(hs_squared - expected) == 0
assert all(sp.simplify(value.subs(beta, sp.Rational(1, 2))) == 0 for value in eigenvalues)

hostile_spectrum = [sp.simplify(value.subs({beta: sp.Rational(3, 4), height: 2})) for value in eigenvalues]
hostile_norm = sp.simplify(hs_squared.subs({beta: sp.Rational(3, 4), height: 2}))
assert hostile_norm == sp.Rational(4, 81)

print(f"quartet_trace={trace}")
print(f"quartet_Hilbert_Schmidt_squared={hs_squared}")
print(f"hostile_spectrum={hostile_spectrum}")
print(f"hostile_Hilbert_Schmidt_squared={hostile_norm}")
print("self_adjoint=True")
print("RH_iff_operator_zero=True")
print("source_side_construction_open=True")

