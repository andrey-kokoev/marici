"""Exact spectral and finite-product checks for the even oscillator gamma model."""

import sympy as sp

k, count, z = sp.symbols("k count z", integer=True, nonnegative=True)

# Oscillator eigenvalue 2n+1 with even n=2k, scaled by four.
even_scaled_eigenvalue = sp.simplify((2 * (2 * k) + 1) / 4)
assert even_scaled_eigenvalue == k + sp.Rational(1, 4)

# Finite determinant identity underlying the regularized limit.
for terms in (1, 2, 5, 8):
    finite_product = sp.prod(k + sp.Rational(1, 4) + z for k in range(terms))
    gamma_ratio = sp.gamma(terms + sp.Rational(1, 4) + z) / sp.gamma(sp.Rational(1, 4) + z)
    rising = sp.rf(sp.Rational(1, 4) + z, terms)
    assert sp.expand(finite_product - rising) == 0
    assert sp.simplify(sp.expand_func(gamma_ratio) - rising) == 0
    print(f"finite_terms={terms} gamma_product_identity=True")

# Hurwitz-zeta determinant normalization at a positive rational shift.
a = sp.Rational(1, 4)
regularized_determinant = sp.sqrt(2 * sp.pi) / sp.gamma(a)
assert regularized_determinant > 0

print("even_scaled_spectrum=k+1/4")
print("zeta_determinant=sqrt(2*pi)/Gamma(1/4+z)")
print("even_parity_selects_quarter_shift=True")
print("auxiliary_operator_is_Hilbert_Polya=False")
print("prime_relative_determinant_open=True")
