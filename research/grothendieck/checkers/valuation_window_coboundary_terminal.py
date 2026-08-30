import json
import sympy as sp


N = 8
block = 2
F = list(sp.symbols(f"F0:{N}"))
s = list(sp.symbols(f"s0:{N}"))


def at(seq, i):
    return seq[i] if 0 <= i < len(seq) else sp.Integer(0)


def W(M):
    return sp.expand(sum(
        2 * at(F, q) * at(F, q + d) * at(s, d)
        for q in range(min(M, N))
        for d in range(N)
    ))


increments = [sp.expand(W(min((k + 1) * block, N)) - W(k * block)) for k in range((N + block - 1) // block)]
telescoped = sp.expand(sum(increments))

a, E, K = sp.symbols("a E K")
direct_identity = 2 * a * E + 2 * K
reflected_identity = -2 * a * E - 2 * K

checks = {
    "valuation_blocks_telescope": sp.expand(telescoped - W(N)) == 0,
    "initial_window_zero": W(0) == 0,
    "terminal_window_is_full_forcing": W(N) != 0,
    "reciprocal_sum_is_tautological": sp.expand(direct_identity + reflected_identity) == 0,
    "reciprocal_difference_repeats_original": sp.expand(
        (direct_identity - reflected_identity) - 2 * direct_identity
    ) == 0,
}

result = {
    "schema": "marici.grothendieck.valuation_window_coboundary_terminal.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "coboundary": "Delta_k W = W_((k+1)L)-W_(kL)",
    "terminal": "sum_k Delta_k W = W_infinity = rho",
    "correction": "valuation intervals avoid point-sampling quadrature",
    "remaining_obstruction": "the terminal autocorrelation forcing survives; reciprocal addition cancels both it and the horizontal energy tautologically",
}

print(json.dumps(result, indent=2, sort_keys=True))
