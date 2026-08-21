from math import gcd, lcm


def radical(n):
    out = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            out *= p
            while n % p == 0:
                n //= p
        p += 1
    return out * n


# C60 -> C30 -> C6; cyclic conjugation actions are trivial.
rho_identity = radical(1)
rho_phi = radical(2)
rho_psi = radical(5)
rho_composite = radical(10)

assert rho_identity == 1
assert lcm(rho_identity, rho_phi) == rho_phi
assert lcm(rho_phi, rho_psi) == rho_composite

indices = range(1, 61)
U_phi = {n for n in indices if gcd(n, rho_phi) == 1}
U_psi = {n for n in indices if gcd(n, rho_psi) == 1}
U_composite = {n for n in indices if gcd(n, rho_composite) == 1}
assert U_composite == U_phi & U_psi

print({
    "tower": "C60->C30->C6",
    "resonance_costs": [rho_identity, rho_phi, rho_psi, rho_composite],
    "spectrum_sizes_1_to_60": [len(U_phi), len(U_psi), len(U_composite)],
    "identity_and_composition_laws": "pass",
    "checks": "pass",
})
