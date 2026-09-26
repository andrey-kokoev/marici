"""Exact finite Laurent audit of the analytic radial Poisson derivation.
This is not a PDE solver or a replacement for the continuum uniqueness proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import runpy

BASE = Path(__file__).resolve().parents[1]

def clean(p):
    return {n: F(c) for n, c in p.items() if c}

def add(p, q):
    out = dict(p)
    for n, c in q.items():
        out[n] = out.get(n, F(0)) + c
    return clean(out)

def derivative(p):
    return clean({n-1: n*c for n, c in p.items()})

def shift(p, n):
    return {k+n: v for k, v in p.items()}

def laplacian(p, dimension=3):
    first = derivative(p)
    return add(derivative(first), {n-1: (dimension-1)*v for n, v in first.items()})

def flux(p, dimension=3):
    # Surface-area constant has been cancelled against source normalization.
    return shift(derivative(p), dimension-1)

def decays(p):
    # Exact for finite Laurent polynomials on r>0.
    return all(n < 0 for n in clean(p))

def evaluate(p, r):
    r = F(r)
    if r <= 0:
        raise ValueError('exterior radius must be strictly positive')
    return sum((v*r**n for n, v in p.items()), F(0))

def derive(k):
    k = F(k)
    # The continuum ODE argument proves completeness; this is a finite audit.
    vacuum_modes = [n for n in range(-8, 9) if not laplacian({n: F(1)})]
    assert vacuum_modes == [-1, 0]
    decaying_modes = [n for n in vacuum_modes if decays({n: F(1)})]
    assert len(decaying_modes) == 1
    n = decaying_modes[0]
    unit_flux = flux({n: F(1)})
    assert set(unit_flux) == {0}
    coefficient = k / unit_flux[0]  # solves source normalization, including sign
    p = clean({n: coefficient})
    assert laplacian(p) == {} and decays(p)
    assert flux(p) == clean({0: k})
    return p

cases = []
for G, mass in [(F(1), F(2)), (F(3, 5), F(7, 3)), (F(1), F(0))]:
    k = G*mass
    p = derive(k)
    radii = [F(1, 2), F(1), F(3, 2), F(3), F(7)]
    for r in radii:
        assert evaluate(p, r) == -k/r
        assert -evaluate(derivative(p), r) == -k/(r*r)
    cases.append({'G': str(G), 'mass': str(mass),
                  'derived_potential': {str(n): str(c) for n, c in p.items()}})

p = derive(F(6))
wrong_sign = {n: -c for n, c in p.items()}
assert laplacian(wrong_sign) == {} and decays(wrong_sign)
assert flux(wrong_sign) != {0: F(6)}
wrong_exponent = {-2: F(-6)}
assert laplacian(wrong_exponent) != {}
shifted = add(p, {0: F(7)})
assert laplacian(shifted) == {} and flux(shifted) == flux(p)
assert not decays(shifted)
# The inverse-square conclusion uses THREE dimensions.
assert laplacian(p, dimension=2) != {}
try:
    evaluate(p, F(0))
except ValueError:
    origin_rejected = True
else:
    raise AssertionError('singular origin accepted')

# Reuse the prior independent polynomial differentiation only AFTER deriving
# the 1/r coefficient for each point source (translation + superposition).
prior = runpy.run_path(str(BASE/'checkers/check_newtonian_potential_routes.py'))
sources = prior['ns']['sources_a']
derived_sources = []
for mass, position in sources:
    coefficient = derive(mass).get(-1, F(0))
    derived_sources.append((-coefficient, position))
actual = prior['hessian'](prior['potential_polynomial'](derived_sources))
assert actual == prior['ns']['jet_a'][2]

paths = [Path(__file__), BASE/'agda/NewtonFromPoisson.agda',
         BASE/'agda/NewtonRadialCoefficients.agda']
packet = {
    'status': 'radial-Poisson-coefficient-audit-passed',
    'scope': 'Finite Laurent algebra and prior tidal fixture; continuum PDE steps remain mathematical arguments, not compiler-certified',
    'cases': cases, 'hostiles': {'wrong_sign': True, 'wrong_exponent': True,
        'constant_without_decay': True, 'wrong_dimension': True, 'origin': origin_rejected},
    'tidal_bridge': [[str(v) for v in row] for row in actual],
    'sha256': {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
}
(BASE/'results/newton-from-poisson.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('Poisson radial coefficient audit passed; five hostiles and prior tidal bridge checked.')
