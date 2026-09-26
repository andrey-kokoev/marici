"""Independent truncated-polynomial potential differentiation, exact Fraction.
No jet product rules or direct tensor formula are used by this route.
The binomial expansion is local about the source-free observation point.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
import runpy

BASE = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(BASE/'checkers/check_machian_newtonian_localization.py'))
ZERO = (0, 0, 0)

def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return out

def scale(c, a):
    return {k: c*v for k, v in a.items()}

def multiply(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x+y for x, y in zip(ka, kb))
            if sum(k) <= 2:
                out[k] = out.get(k, F(0)) + va*vb
    return out

def potential_polynomial(sources, quadratic=F(3, 8)):
    out = {}
    for mass, rvec in sources:
        r2 = sum(v*v for v in rvec)
        r = isqrt(r2.numerator)
        assert r*r == r2 and r > 0
        q = {}
        for i in range(3):
            linear, square = [0]*3, [0]*3
            linear[i], square[i] = 1, 2
            q[tuple(linear)] = -2*rvec[i]/r2
            q[tuple(square)] = 1/r2
        inv = add({ZERO: F(1)}, add(scale(F(-1, 2), q), scale(quadratic, multiply(q, q))))
        # Independently check the reciprocal square-root equation modulo degree 3.
        residual = multiply(multiply(inv, inv), add({ZERO: F(1)}, q))
        if quadratic == F(3, 8):
            assert all(v == (1 if k == ZERO else 0) for k, v in residual.items())
        out = add(out, scale(-mass/r, inv))
    return out

def hessian(p):
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            e = [0]*3
            e[i] += 1
            e[j] += 1
            row.append(p.get(tuple(e), F(0)) * (2 if i == j else 1))
        out.append(tuple(row))
    return tuple(out)

checks = []
for name in ('a', 'b'):
    sources = ns['sources_'+name]
    poly = potential_polynomial(sources)
    expected = ns['jet_'+name]
    assert poly[ZERO] == expected[0]
    assert hessian(poly) == expected[2]
    assert hessian(potential_polynomial(sources, F(3, 16))) != expected[2]
    assert hessian(scale(-1, poly)) != expected[2]
    checks.append({'fixture': name, 'hessian': [[str(v) for v in row] for row in hessian(poly)],
                   'wrong_quadratic_rejected': True, 'wrong_sign_rejected': True})
# Cross derivatives are zero in the selected axial fixture. Add a non-axial
# rational-radius computational control so mixed derivatives are exercised.
oblique = [(F(2), (F(3), F(4), F(0)))]
assert hessian(potential_polynomial(oblique)) == ns['source_jet_at_origin'](oblique)[2]
assert hessian(potential_polynomial(oblique))[0][1] != 0
paths = [Path(__file__), BASE/'agda/NewtonianPotentialJet.agda', BASE/'agda/NewtonianTidalRoutes.agda']
packet = {'status': 'potential-and-geometry-agree', 'checks': checks,
          'nonaxial_mixed_derivative_control': True,
          'scope': 'Exact degree-two polynomial differentiation; shared Fraction backend; no new continuum theorem',
          'sha256': {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(BASE/'results/newtonian-potential-routes.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('Potential polynomial and geometric evaluator agree; quadratic/sign and mixed-derivative controls passed.')
