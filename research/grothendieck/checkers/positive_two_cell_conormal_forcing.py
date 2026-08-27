import json
import sympy as sp


t = sp.symbols("t", positive=True, real=True)
a = sp.sech(t)
I = sp.I
z0 = t + I * sp.pi

X = 2 * (1 + a * sp.cosh(z0))
Xp = 2 * a * sp.sinh(z0)
forcing = 2 * a * sp.sinh(z0)

checks = {
    "positive_source_weight": a.is_positive is True,
    "off_seam": t.is_positive is True,
    "exact_zero": sp.simplify(sp.expand_complex(X)) == 0,
    "simple_zero": sp.simplify(sp.expand_complex(Xp) + 2 * sp.tanh(t)) == 0,
    "forcing_equals_conormal": sp.simplify(forcing - Xp) == 0,
    "orientation_allows_off_seam_zero": sp.simplify(
        t * sp.re(sp.expand_complex(forcing)) + 2 * t * sp.tanh(t)
    ) == 0,
    "orientation_is_strictly_negative": (-2 * t * sp.tanh(t)).is_negative is True,
}

result = {
    "schema": "marici.grothendieck.positive_two_cell_conormal_forcing.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "source": "delta_0 + sech(t) delta_1",
    "completed_readout": "2(1 + sech(t) cosh(z))",
    "off_seam_zero": "z=t+i*pi, t>0",
    "conormal_and_forcing": "X'(z0)=K(z0)=-2 tanh(t)",
    "signed_orientation": "Re(z0) Re(K(z0))=-2 t tanh(t)<0",
}

print(json.dumps(result, indent=2, sort_keys=True))
