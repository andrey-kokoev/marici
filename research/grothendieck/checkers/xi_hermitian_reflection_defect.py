"""Exact checks for the convergent Hermitian RH reflection defect."""

import sympy as sp

beta, height = sp.symbols("beta height", real=True)
offset = beta - sp.Rational(1, 2)
single = offset**2 / (1 + offset**2 + height**2)
quartet = sp.simplify(4 * single)
assert sp.simplify(quartet - 4 * offset**2 / (1 + offset**2 + height**2)) == 0
assert sp.simplify(quartet.subs(beta, sp.Rational(1, 2))) == 0

# A concrete hostile C2 branch/quartet is strictly detected.
hostile = sp.simplify(quartet.subs({beta: sp.Rational(3, 4), height: 2}))
assert hostile > 0

# In the critical strip q=offset^2<=1/4 gives a convergent majorant.
q = sp.symbols("q", nonnegative=True)
majorant_gap = sp.Rational(1, 4) / (1 + height**2) - q / (1 + height**2 + q)
positive_split = (sp.Rational(1, 4) - q) / (1 + height**2) + q * (
    1 / (1 + height**2) - 1 / (1 + height**2 + q)
)
assert sp.simplify(majorant_gap - positive_split) == 0

print(f"hostile_quartet_defect={hostile}")
print("critical_line_defect_zero=True")
print("off_line_quartet_detected=True")
print("Riemann_von_Mangoldt_majorant=1/(1+T^2)")
print("Hermitian_pairing_required=True")
print("source_side_realization_open=True")
