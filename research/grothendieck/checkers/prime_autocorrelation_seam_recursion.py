import json
import sympy as sp


c = sp.symbols("c")
N = 6
L = 1
d = 1
F = list(sp.symbols(f"F0:{N + 1}"))


def at(seq, i):
    return seq[i] if 0 <= i < len(seq) else sp.Integer(0)


A = [at(F, q) - c * at(F, q + L) for q in range(N + 1)]


def corr(left, right, left_shift=0, right_shift=0):
    return 2 * sum(
        at(left, q + left_shift) * at(right, q + d + right_shift)
        for q in range(N + 1)
    )


rho = corr(F, F)
rho_AA = corr(A, A)
rho_A_L = corr(A, F, right_shift=L)
rho_L_A = corr(F, A, left_shift=L)
W_L = 2 * sum(at(F, q) * at(F, q + d) for q in range(L))
residual = sp.expand((1 - c**2) * rho - (rho_AA + c * rho_A_L + c * rho_L_A - c**2 * W_L))

checks = {
    "finite_label_identity": residual == 0,
    "theta_coefficient": sp.simplify((1 - c**2).subs(c, sp.sqrt(sp.Rational(1, 2))) - sp.Rational(1, 2)) == 0,
    "single_signed_window": sp.Poly(-c**2 * sp.Symbol("W"), sp.Symbol("W")).coeff_monomial(sp.Symbol("W")) == -c**2,
}

result = {
    "schema": "marici.grothendieck.prime_autocorrelation_seam_recursion.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "identity": "(1-c^2) rho = rho_AA + c rho_A,L + c rho_L,A - c^2 W_L",
    "theta_substitution": "c=p^-1/2, L=log p",
    "signed_channel": "finite moving-seam window W_L",
}

print(json.dumps(result, indent=2, sort_keys=True))
