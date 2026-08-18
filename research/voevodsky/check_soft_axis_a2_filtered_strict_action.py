"""Verify that Entry 508's strict action respects D -> D+2 cutoffs."""
import importlib.util
from pathlib import Path

p = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
s = importlib.util.spec_from_file_location("deck", p)
d = importlib.util.module_from_spec(s)
s.loader.exec_module(d)

for cutoff in (12, 16, 20, 24):
    admitted = 0
    for sector in ((1, 1), (1, 0), (0, 1), (0, 0)):
        sa, sb = sector
        ea, eb = 2 - sa, 2 - sb
        base = d.mul(d.power(d.L1, ea), d.power(d.L2_minus, eb))
        for total in range(cutoff + 1):
            for ai in range(total + 1):
                f = d.mul(d.power(d.a, ai), d.power(d.b, total - ai))
                q = d.exact(sector, f, True, False)
                if not q or max(m[1] + m[2] for m in q) > cutoff:
                    continue
                h = d.scale(d.mul(d.a, f, base), 2)
                assert max(m[1] + m[2] for m in h) <= cutoff - 2
                admitted += 1
    print(f"D={cutoff}: admitted_q={admitted}, all h in P_(D-2)")

print("verdict: (f,p)->(a^2 f,a^2 p-h(f)) defines a filtered D->D+2 map")
