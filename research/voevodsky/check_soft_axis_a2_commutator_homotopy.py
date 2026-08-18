"""Verify the a^2 multiplication commutator and its principal-K homotopy."""

import importlib.util
from pathlib import Path

source = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", source)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

a2 = d.power(d.a, 2)
sectors = ((1, 1), (1, 0), (0, 1), (0, 0))

for conjugate in (False, True):
    l2 = d.L2_plus if conjugate else d.L2_minus
    for sector in sectors:
        sa, sb = sector
        ea, eb = 2 - sa, 2 - sb
        base = d.mul(d.power(d.L1, ea), d.power(l2, eb))
        for ai in range(3):
            for bi in range(3):
                f = d.mul(d.power(d.a, ai), d.power(d.b, bi))
                for is_q in (False, True):
                    left = d.exact(sector, d.mul(a2, f), is_q, conjugate)
                    right = d.mul(a2, d.exact(sector, f, is_q, conjugate))
                    commutator = d.add(left, d.scale(right, -1))
                    expected = (
                        d.scale(d.mul(d.a, f, base, d.K), 2) if is_q else {}
                    )
                    assert commutator == expected

print("[p,a^2]=0 in every sector and deck lattice")
print("[q,a^2](f)=2 a f L1^ea L2^eb K")
print("principal-resolution homotopy coefficient: 2 a f L1^ea L2^eb")
print("verdict: the commutator factors canonically through K")
print("remaining gate: lift this factorization through the retained gradient/KS complex")
