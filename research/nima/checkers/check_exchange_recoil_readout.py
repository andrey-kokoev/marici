"""Mechanical readout test of one port of the established exchange.

At every normalized port a=f^T H y and b=r exchange exactly. Tests local
body assignment first, then an explicit mass-dependent mixed readout.
No physical units, masses, charges or excitation are source-derived.
"""
from pathlib import Path
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
a, b = S.symbols('a b', real=True)
alpha, beta = S.symbols('alpha beta', positive=True)
m1, m2 = S.symbols('m1 m2', positive=True)
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


swap = S.Matrix([[0, 1], [1, 0]])
v = S.Matrix([a, b])
# Local identification cannot mix the two putative bodies.
momentum_residual = S.expand(alpha*b+beta*a-alpha*a-beta*b)
energy_residual = S.expand(alpha**2*(b*b-a*a)/(2*m1)+beta**2*(a*a-b*b)/(2*m2))
check('local-total-momentum-residual', S.expand(momentum_residual-(alpha-beta)*(b-a)) == 0)
check('momentum-selects-common-scale', S.solve(S.Poly(momentum_residual, a, b).coeffs(), beta) == {beta: alpha})
check('equal-scale-energy-residual', S.factor(energy_residual.subs(beta, alpha)) ==
      S.factor(alpha**2*(b*b-a*a)*(1/m1-1/m2)/2))
check('local-energy-selects-equal-masses', S.solve(S.expand(energy_residual.subs(beta, alpha)).coeff(b, 2), m2) == [m1])
# Explicit original unequal-mass fixture shows a kinetic defect, not an
# isolated equal-mass collision under a new label.
check('unequal-mass-local-hostile', energy_residual.subs({alpha:1,beta:1,m1:2,m2:3,a:0,b:1}) == S.Rational(1,12))

# With supplied masses one can instead rotate the body readout. This mixes
# carrier and record amplitudes; it is NOT the local assignment above.
eplus = S.Matrix([1, 1])/S.sqrt(2)
eminus = S.Matrix([1, -1])/S.sqrt(2)
u = S.Matrix([S.sqrt(m1), S.sqrt(m2)])/S.sqrt(m1+m2)
n = S.Matrix([S.sqrt(m2), -S.sqrt(m1)])/S.sqrt(m1+m2)
O = u*eplus.T+n*eminus.T
MassRoot = S.diag(S.sqrt(m1), S.sqrt(m2))
B = MassRoot*O
E = S.simplify(B*swap*B.inv())
expected = S.Matrix([[(m1-m2)/(m1+m2), 2*m1/(m1+m2)],
                     [2*m2/(m1+m2), (m2-m1)/(m1+m2)]])
check('mass-weighted-view-orthogonal', S.simplify(O.T*O-S.eye(2)) == S.zeros(2))
check('mixed-readout-elastic-collision', S.simplify(E-expected) == S.zeros(2))
check('collision-preserves-total-momentum', S.simplify(S.ones(1,2)*E-S.ones(1,2)) == S.zeros(1,2))
K = S.diag(1/m1,1/m2)
check('collision-preserves-kinetic-energy', S.simplify(E.T*K*E-K) == S.zeros(2))
check('source-budget-becomes-kinetic', S.simplify(B.T*K*B-S.eye(2)) == S.zeros(2))
check('collision-involution', S.simplify(E*E-S.eye(2)) == S.zeros(2))
p1,p2 = S.symbols('p1 p2', real=True)
p = S.Matrix([p1,p2])
J = S.factor((E*p-p)[0])
check('recoil-opposite', S.simplify((E*p-p)[1]+J) == 0)
check('impulse-from-relative-velocity', S.simplify(J-2*m1*m2/(m1+m2)*(p2/m2-p1/m1)) == 0)
check('mass-dependent-velocity-ratio', S.simplify((-J/m2)/(J/m1)+m1/m2) == 0)
check('unequal-mass-fixture', S.simplify(E.subs({m1:2,m2:3})*S.Matrix([0,1])-S.Matrix([S.Rational(4,5),S.Rational(1,5)])) == S.zeros(2,1))
check('from-rest-no-excitation', E*S.zeros(2,1) == S.zeros(2,1))

# The original triangle's scalar port can package this impulse if its kernel
# is chosen as J/(q1 q2), but that is a state-dependent definition, not a
# derivation of the original fixed-kernel charge law.
charge1, charge2, kernel = S.symbols('charge1 charge2 kernel', nonzero=True, real=True)
check('kernel-fit-is-only-identity', S.simplify(charge1*charge2*(J/(charge1*charge2))-J) == 0)
check('fixed-exchange-independent-of-charge-sign', S.diff(J, charge1) == 0)
check('neutrality-not-enforced', J.subs({m1:2,m2:3,p1:0,p2:1}) != 0)
# A charge-dependent event scheduler could turn neutral interactions off,
# but it is new control data and cannot change this charge-blind port law.

# Canonical mechanics requires position variables not present in the real
# amplitude pair. An enlarged cotangent lift is possible, but moves them.
q1,q2 = S.symbols('q1 q2', real=True)
q = S.Matrix([q1,q2])
qmap = S.simplify(E.inv().T)
C = S.diag(qmap,E)
Omega = S.zeros(2).row_join(S.eye(2)).col_join((-S.eye(2)).row_join(S.zeros(2)))
check('declared-cotangent-enlargement-canonical', S.simplify(C.T*Omega*C-Omega) == S.zeros(4))
fixed_q = S.diag(S.eye(2),E)
check('fixed-position-kick-is-not-this-canonical-map', S.simplify(fixed_q.T*Omega*fixed_q-Omega) != S.zeros(4))
check('contact-positions-fixed-by-cotangent-lift',
      S.simplify(qmap*S.ones(2,1)-S.ones(2,1)) == S.zeros(2,1))

result = {
    'schema':'marici.nima.exchange-recoil-readout.v1','status':'pass','checks':checks,
    'local_readout':'separate carrier/record body momenta plus norm-as-kinetic require equal masses',
    'unequal_mass_readout':'supplied mass-dependent mixing yields the standard one-dimensional elastic collision map',
    'impulse':str(J),
    'collision_matrix':[[str(x) for x in E.row(i)] for i in range(2)],
    'selection_boundary':'every positive mass pair admits such a mixed view; exchange does not select the masses',
    'charge_boundary':'exchange impulse has no charge dependence; neutrality and sign reversal require an additional interaction law',
    'preparation_boundary':'zero physical momenta remain zero; the earlier impulse from rest cannot be supplied by this isolated elastic readout',
    'position_boundary':'cotangent lift adds positions and generally transforms them; it fixes equal contact positions. Keeping arbitrary positions fixed is not symplectic on unrestricted phase space; no contact event law is derived',
    'global_boundary':'one-port construction only; no simultaneous body assignment across all overlapping native ports, three-dimensional spatial readout, or clock map proved',
}
(ROOT/'results/exchange-recoil-readout.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact symbolic mechanical-readout checks')
print('Local body assignment requires equal masses. Mixed mass-dependent view realizes elastic recoil.')
print('Charge law, excitation, positions and multiport physical binding remain unselected.')
