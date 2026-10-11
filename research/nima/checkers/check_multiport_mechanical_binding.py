"""Global consistency test, not another per-port mass fit.

Tests six labelled port reflections against one scalar carrier body and six
scalar partner bodies with arbitrary positive masses. Rejects only this
specific simultaneous elastic-collision architecture.
"""
from contextlib import redirect_stdout
from itertools import combinations
from pathlib import Path
import io
import json
import runpy
import sympy as S

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(HERE/'check_seed_port_exchange_binding.py'))
labels, F, H = source['labels'], source['features'], source['H']
# Unit reflection normals in the established carrier+record metric.
Gram = (S.eye(6)+F.T*H*F)/2
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


check('six-independent-reflection-normals', Gram.rank() == 6)
check('unit-normals', all(Gram[i,i] == 1 for i in range(6)))
check('every-port-pair-overlaps', all(Gram[i,j] != 0 for i,j in combinations(range(6),2)))

# Any shared-carrier scalar collision star has normals n_i in mass-weighted
# momentum space: sqrt(m_i/(M+m_i))*e0 - sqrt(M/(M+m_i))*e_i.
# Thus off-diagonal normal Gram entries factor as v_i*v_j. Independent
# sign choices of normals do not change any four-distinct-index tetrad.
M = S.symbols('M', positive=True)
m = S.symbols('m0:6', positive=True)
v = [S.sqrt(mi/(M+mi)) for mi in m]
star = S.Matrix(6,6,lambda i,j: 1 if i==j else v[i]*v[j])
violations = []
for i,j,k,l in combinations(range(6),4):
    check('star-tetrad/'+str((i,j,k,l)), S.simplify(star[i,j]*star[k,l]-star[i,k]*star[j,l]) == 0)
    residual = Gram[i,j]*Gram[k,l]-Gram[i,k]*Gram[j,l]
    if residual != 0:
        violations.append({'ports':[labels[t] for t in (i,j,k,l)],'residual':str(residual)})
check('native-port-Gram-rejects-star', bool(violations))

# Relating the positive-form dynamics by ONE linear isometry preserves the
# Gram of their rank-one reflection normals, up to independent signs. Thus
# this obstruction is not removed by rotating the common state basis.
i,j,k,l = next(indices for indices in combinations(range(6),4)
              if Gram[indices[0],indices[1]]*Gram[indices[2],indices[3]]
              != Gram[indices[0],indices[2]]*Gram[indices[1],indices[3]])
r = Gram[i,j]*Gram[k,l]-Gram[i,k]*Gram[j,l]
from itertools import product
for signs in product((-1,1),repeat=4):
    a,b,c,d = signs
    changed = a*b*Gram[i,j]*c*d*Gram[k,l]-a*c*Gram[i,k]*b*d*Gram[j,l]
    check('normal-sign-cannot-remove-obstruction/'+str(signs), changed == a*b*c*d*r and changed != 0)

result = {
    'schema':'marici.nima.multiport-mechanical-binding.v1','status':'pass','checks':checks,
    'candidate':'one scalar carrier body and six scalar partners, positive masses, standard elastic collisions, one metric-preserving linear identification',
    'candidate_disposition':'rejected by nonzero reflection-normal Gram tetrads',
    'port_order':list(labels),
    'bound_port_Gram':[[str(x) for x in Gram.row(i)] for i in range(6)],
    'violations':violations,
    'reason':'collision-star off-diagonal overlaps factor v_i*v_j; the actual port overlaps do not',
    'preserved_positive_result':'each isolated port separately admits an arbitrary-positive-mass elastic readout',
    'scope':'does not rule out vector-valued bodies, internal modes, non-isometric observers, nonlinear maps or other interaction networks',
    'charge_boundary':'prior neutral linear evaluation selects inverse phase character, not a matter coupling, force law or coupling strength',
}
(HERE.parent/'results/multiport-mechanical-binding.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact global-binding checks; source adapter rerun')
print('REJECTED: one common scalar carrier-body elastic-collision interpretation.')
print('First invariant witness:', violations[0])
