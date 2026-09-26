"""Export the existing exact two-source fixture, not a new physics model."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json
import runpy

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/nima'
original = BASE / 'checkers/check_machian_newtonian_localization.py'
ns = runpy.run_path(str(original))
sources = ns['sources_a']
phi, grad, hess = ns['jet_a']
D = 1728

def integer(q):
    q = Fraction(q)
    assert q.denominator == 1
    n = q.numerator
    return f'pos {n}' if n >= 0 else f'negsuc {-n-1}'

def vec(name, values):
    return f'{name} : Vec\n' + ''.join(
        f'{name} {a} = {integer(v)}\n' for a, v in zip('xyz', values))

text = '''{-# OPTIONS --safe --cubical --guardedness #-}
-- Generated from check_machian_newtonian_localization.py, sources_a/jet_a.
module NewtonianTidalFixture where
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)
open import NewtonianTidalKernel

'''
assert len(sources) == 2
for name, (mass, coords) in zip(('a', 'b'), sources):
    r2 = sum(v*v for v in coords)
    r = isqrt(r2.numerator)
    assert r2 == r*r and r > 0
    direction = [v/r for v in coords]
    assert sum(v*v for v in direction) == 1
    text += vec(name+'Direction', direction)
    text += f'{name} : Source\n{name} = source ({integer(mass)}) ({integer(r)}) ({integer(Fraction(D, r**3))}) {name}Direction\n\n'
text += f'denominator : ℤ\ndenominator = pos {D}\n\n'
text += vec('exportedGradient', [v*D for v in grad])
text += 'exportedTensor : Tensor\n'
for i, ai in enumerate('xyz'):
    for j, aj in enumerate('xyz'):
        text += f'exportedTensor {ai} {aj} = {integer(hess[i][j]*D)}\n'
text += f'exportedJet : Jet\nexportedJet = jet ({integer(phi*D)}) exportedGradient exportedTensor\n'
# Independently reconstruct using normalized radial directions.
for i in range(3):
    for j in range(3):
        value = Fraction(0)
        for m, coords in sources:
            r = isqrt(sum(v*v for v in coords).numerator)
            value += m/Fraction(r**3) * ((1 if i == j else 0)-3*coords[i]*coords[j]/r**2)
        assert value == hess[i][j]
fixture = BASE / 'agda/NewtonianTidalFixture.agda'
fixture.write_text(text, encoding='utf-8')
paths = [original, Path(__file__), fixture,
         BASE/'agda/NewtonianTidalKernel.agda', BASE/'agda/NewtonianTidalCertificate.agda']
receipt = {'status': 'export-consistent-not-a-compiler-receipt',
           'scope': 'sources_a, G=1; assumed Newtonian potential; shared Fraction backend',
           'denominator': D, 'tensor': [[str(v) for v in row] for row in hess],
           'sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in paths if p.exists()}}
(BASE/'results/newtonian-tidal-export.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print('Export consistent: tidal diagonal (-229,74,155)/1728')
