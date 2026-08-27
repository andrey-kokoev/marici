from fractions import Fraction as F
import json
from pathlib import Path


def s(t, z):
    return 1 + t * z


def ds_dt(_t, z):
    return z


def h(z):
    return 1 - z * z


def f(t, z):
    return h(z) * s(t, z)


def df_dt(t, z):
    return h(z) * ds_dt(t, z)


fixtures = [(F(0), F(0)), (F(1, 3), F(1, 2)), (F(2), F(-1, 3))]
for t, z in fixtures:
    assert df_dt(t, z) * s(t, z) - f(t, z) * ds_dt(t, z) == 0

assert f(F(0), F(0)) == s(F(0), F(0)) == 1
assert h(F(1)) == h(F(-1)) == 0
assert s(F(0), F(1)) != 0 and s(F(0), F(-1)) != 0

result = {
    "schema": "marici.rh-source-jet-anchor-obstruction.v1",
    "determinant_family": "S(t,z)=1+tz",
    "endpoint_family": "F(t,z)=(1-z^2)(1+tz)",
    "division_free_source_jet_residual": "(d_t F)S-F(d_t S)=0",
    "source_jet_agreement": True,
    "point_anchor_at_t0_z0": True,
    "divisors_agree": False,
    "extra_endpoint_zeros": ["z=-1", "z=1"],
    "missing_gate": "spectral_anchor_or_source_derived_spectral_evolution_with_uniqueness",
}

out = Path(__file__).parents[1] / "results" / "rh-source-jet-anchor-obstruction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
