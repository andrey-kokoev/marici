"""Exact rational hostile control for residue/integration interchange.
No numerical quadrature and no claim about the actual cosmological period.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

def clean(p):
    return {k: F(v) for k, v in p.items() if v}

def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return clean(r)

def neg(p):
    return {k: -v for k, v in p.items()}

def mul(p, q):
    r = {}
    for (a, b), v in p.items():
        for (c, d), w in q.items():
            k = (a+c, b+d)
            r[k] = r.get(k, 0) + v*w
    return clean(r)

def dy(p):
    return clean({(a, b-1): b*v for (a, b), v in p.items() if b})

def at_y(p, value):
    r = {}
    for (a, b), v in p.items():
        k = (a, 0)
        r[k] = r.get(k, 0) + v*F(value)**b
    return clean(r)

class Rational:
    def __init__(self, n, d=None):
        self.n = clean(n)
        self.d = clean({(0, 0): 1} if d is None else d)
        if not self.d:
            raise ValueError('zero denominator')
    def __add__(self, other):
        return Rational(add(mul(self.n, other.d), mul(other.n, self.d)), mul(self.d, other.d))
    def __neg__(self):
        return Rational(neg(self.n), self.d)
    def __sub__(self, other):
        return self + (-other)
    def __mul__(self, other):
        return Rational(mul(self.n, other.n), mul(self.d, other.d))
    def inv(self):
        return Rational(self.d, self.n)
    def derivative_y(self):
        return Rational(add(mul(dy(self.n), self.d), neg(mul(self.n, dy(self.d)))), mul(self.d, self.d))
    def substitute_y(self, y):
        return Rational(at_y(self.n, y), at_y(self.d, y))
    def equals(self, other):
        return not add(mul(self.n, other.d), neg(mul(other.n, self.d)))
    def simple_residue_E(self):
        if not self.n:
            return Rational({})
        n_order = min(a for a, b in self.n)
        d_order = min(a for a, b in self.d)
        order = n_order-d_order
        if order < -1:
            raise ValueError('not a simple-pole residue calculation')
        if order > -1:
            return Rational({})
        return Rational({(0, b): v for (a, b), v in self.n.items() if a == n_order},
                        {(0, b): v for (a, b), v in self.d.items() if a == d_order})

sources = [HERE/'check_period_residue_boundary.py',
    ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex',
    ROOT/'temp/arxiv-2408.16386-source/sections/method.tex',
    ROOT/'research/nima/total-energy-period-residue-interchange-dpc.md',
    ROOT/'research/nima/total-energy-amplitude-proportionality-typing-dpc.md',
    ROOT/'research/benincasa/cyclic_q_assembly_certificate.md']
def inventory():
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}

before = inventory()
expected = '3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b'
assert before['temp/arxiv-2408.16386-source/sections/applications.tex'] == expected
E = Rational({(1, 0): 1})
y = Rational({(0, 1): 1})
one = Rational({(0, 0): 1})
two = one+one

# For E>0, integrate on the SAME oriented interval [0,1].
# f = 1/E + 1/(E+y)^2, primitive = y/E - 1/(E+y).
f = E.inv() + (E+y).inv()*(E+y).inv()
primitive = y*E.inv() - (E+y).inv()
assert primitive.derivative_y().equals(f)
period = primitive.substitute_y(1)-primitive.substitute_y(0)
assert period.equals(two*E.inv()-(E+one).inv())
assert f.simple_residue_E().equals(one)  # coefficient in Q(y)((E)), y != 0
assert period.simple_residue_E().equals(two)
assert not period.simple_residue_E().equals(one)

# Positive control: no colliding endpoint pole.
good = E.inv()
good_primitive = y*E.inv()
assert good_primitive.derivative_y().equals(good)
good_period = good_primitive.substitute_y(1)-good_primitive.substitute_y(0)
assert good.simple_residue_E().equals(one)
assert good_period.simple_residue_E().equals(one)
# Source-derived boundary layer in E*f: k_E = E/(E+y)^2.
kernel = E*(E+y).inv()*(E+y).inv()
assert (E*f).equals(one+kernel)
kernel_primitive = -(E*(E+y).inv())
assert kernel_primitive.derivative_y().equals(kernel)
cumulative = kernel_primitive-kernel_primitive.substitute_y(0)
assert cumulative.equals(y*(E+y).inv())
mass = cumulative.substitute_y(1)
assert mass.equals((E+one).inv())
# Blow up y=E*t (the symbol y below denotes t); include Jacobian E.
blown_up = E*(E+E*y).inv()*(E+E*y).inv()*E
assert blown_up.equals((one+y).inv()*(one+y).inv())
# Half the layer mass sits on [0,E], whose Lebesgue measure tends to zero.
assert (E*(E+E).inv()).equals(Rational({(0, 0): F(1, 2)}))
# Tail for a positive cutoff y=delta: integral_delta^1 k_E.
tail = kernel_primitive.substitute_y(1)-kernel_primitive
assert tail.equals(E*(E+y).inv()-E*(E+one).inv())
# Exact bounds at E=1/n^2, delta=1/n, for tests with sup norm and Lipschitz
# constant at most one. The analytic all-test argument is in the note.
rate_samples = []
for n in (10, 100, 1000, 10000):
    e, delta = F(1, n*n), F(1, n)
    bound = delta + 2*e/(e+delta) + e/(1+e)
    assert 0 < bound < F(3, n)+F(1, n*n)
    rate_samples.append({'n': n, 'E': str(e), 'delta': str(delta), 'bound': str(bound)})
after = inventory()
assert before == after
report = {
    'passed': True, 'arithmetic': 'exact sparse bivariate rational identities over Fraction',
    'source_sha256': before, 'source_unchanged': True,
    'negative_control': {'integrand': '1/E + 1/(E+y)^2', 'domain': 'E>0; y in [0,1]',
        'primitive': 'y/E - 1/(E+y)', 'period': '2/E - 1/(E+1)',
        'formal_integrand_residue': 1, 'integrated_formal_residue': 1,
        'period_residue': 2, 'interchange_fails': True,
        'cause': 'moving pole y=-E collides with fixed endpoint y=0'},
    'positive_control': {'integrand': '1/E', 'both_residues': 1},
    'boundary_layer': {'kernel': 'E/(E+y)^2', 'mass': '1/(1+E)',
        'cumulative_mass': 'delta/(E+delta)', 'mass_on_0_E': '1/2',
        'blowup_y_Et_with_jacobian': '1/(1+t)^2',
        'weak_star_limit': 'delta_0', 'repaired_scaled_reading': 'integral phi dy + phi(0)',
        'total_variation_distance_to_delta_0': '1 + 1/(1+E)',
        'rate_samples': rate_samples,
        'verification_boundary': 'Rational identities and bound samples are machine checked; general continuous-test convergence and total variation argument are written mathematical proofs in endpoint-observation-completion.md, not a formalized analytic theorem.'},
    'scope': 'Counterexample to automatic interchange, not a counterexample to the frozen cosmological period; physical source completion remains unproved.'}
(HERE/'period-residue-boundary.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
