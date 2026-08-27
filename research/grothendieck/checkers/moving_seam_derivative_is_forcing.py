import json
import sympy as sp


N = 6
F = list(sp.symbols(f"F0:{N + 1}"))
s = list(sp.symbols(f"s0:{N + 1}"))
m = 2


def at(seq, i):
    return seq[i] if 0 <= i < len(seq) else sp.Integer(0)


def window(M):
    return sum(
        2 * at(F, q) * at(F, q + d) * at(s, d)
        for q in range(M)
        for d in range(N + 1)
    )


increment = sp.expand(window(m + 1) - window(m))
local_forcing = sp.expand(
    at(F, m) * 2 * sum(at(F, m + d) * at(s, d) for d in range(N + 1))
)

checks = {
    "finite_moving_seam_increment": sp.expand(increment - local_forcing) == 0,
    "empty_window": window(0) == 0,
    "full_window_is_full_forcing": sp.expand(
        window(N + 1)
        - sum(2 * at(F, q) * at(F, q + d) * at(s, d) for q in range(N + 1) for d in range(N + 1))
    ) == 0,
}

result = {
    "schema": "marici.grothendieck.moving_seam_derivative_is_forcing.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "continuous_identity": "d/dL K_W(L,z)=Phi(L)(H_+(L,z)-H_-(L,z))",
    "integrated_identity": "K(z)=integral_0^infinity dK_W(L,z)/dL dL",
    "remaining_gate": "prime recursions sample L=log p; no continuous telescoping measure is yet derived",
}

print(json.dumps(result, indent=2, sort_keys=True))
