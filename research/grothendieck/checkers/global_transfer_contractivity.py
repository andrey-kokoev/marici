"""Hostile scalar quartet and conditional contractivity checks."""

import sympy as sp

w, height = sp.symbols("w T", real=True)
c = w**2 + sp.sqrt(2) * w + 2
reflected = c.subs(w, -w)
paired = sp.expand(1 - c * reflected)
assert paired == -(w**4 + 2 * w**2 + 3)

critical_value = sp.simplify(paired.subs(w, sp.I * height))
critical_norm_form = sp.simplify(1 - c.subs(w, sp.I * height) * sp.conjugate(c.subs(w, sp.I * height)))
assert sp.simplify(sp.expand_complex(critical_value - critical_norm_form)) == 0

roots = [complex(root) for root in sp.nroots(w**4 + 2 * w**2 + 3, n=30, maxsteps=100)]
assert all(abs(root.real) > 1e-10 and abs(root.imag) > 1e-10 for root in roots)
assert all(any(abs(candidate + root) < 1e-20 for candidate in roots) for root in roots)
assert all(any(abs(candidate - root.conjugate()) < 1e-20 for candidate in roots) for root in roots)

# Finite operator contractivity implies invertibility by the Neumann series.
strict = sp.diag(sp.Rational(1, 2), sp.Rational(3, 4))
assert (sp.eye(2) - strict).det() != 0
threshold = sp.diag(1, sp.Rational(3, 4))
assert (sp.eye(2) - threshold).det() == 0

print(f"hostile_off_line_quartet={roots}")
print("reflection_and_line_Hermitian_structure_imply_RH=False")
print("strict_transfer_contractivity_implies_off_line_invertibility=True")
print("unit_singular_value_is_threshold_zero=True")
print("canonical_Xi_transfer_operator_constructed=False")

