"""Joint phase symmetry and whole-state spatial-moment accounting.

Reuse the same source histories, metric, old AB preparation and pulse law.
The moment is the existing target-coordinate intensity diagnostic extended
through the conserved whole anchor; it is not declared mechanical momentum.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import hashlib
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_retained_history_overlap_phase.py'))
exchange=prior['exchange']; ops=exchange['operators']; F=exchange['features']
metric=exchange['metric']; anchor=exchange['anchor']
labels=exchange['labels']; initial=exchange['excited']
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

# Keep fixed labelled pulse operators. Test independent phase weights for
# the common carrier and each of the six persistent records.
charges=S.symbols('q_carrier q0:6',real=True)
charge_operator=S.diag(*([charges[0]]*16+list(charges[1:])))
equations=[v for op in ops.values() for v in charge_operator*op-op*charge_operator]
coeff,rhs=S.linear_eq_to_matrix(equations,charges)
check('phase-weight-constraints-rank-six',coeff.rank()==6)
solution=next(iter(S.linsolve((coeff,rhs),charges)))
check('all-coupled-mode-weights-must-agree',all(v==solution[0] for v in solution))
check('exactly-one-common-phase-weight',len(set().union(*(v.free_symbols for v in solution)))==1)
# Existing complex/canonical structure: Q=z^dagger metric z generates common
# phase (up to orientation convention) and is conserved by every pulse.
for label,op in ops.items():
    P=(S.eye(22)-op)/2
    check('phase-charge-preserved/'+label,op.T*metric*op==metric)
    check('phase-charge-continuous-generator/'+label,P.T*metric==metric*P)
    check('full-anchor-fixed-continuously/'+label,anchor*P==S.zeros(16,22))
neutral_record=S.diag(*([1]*16+[0]*6))
opposite_record=S.diag(*([1]*16+[-1]*6))
check('neutral-record-is-not-fixed-internal-symmetry',any(neutral_record*op!=op*neutral_record for op in ops.values()))
check('opposite-record-is-not-fixed-internal-symmetry',any(opposite_record*op!=op*opposite_record for op in ops.values()))

# Actual source tetrahedral target positions, not arbitrary fitted body maps.
from photon_native_spatial_step import VERTICES
moments=[]
for axis in range(3):
    X=S.diag(*(S.Integer(VERTICES[b][axis]) for a in 'ABCD' for b in 'ABCD'))
    total=anchor.T*X*anchor
    carrier=S.diag(X,S.zeros(6))
    record=S.diag(S.zeros(16),F.T*X*F)
    cross=total-carrier-record
    moments.append((total,carrier,record,cross))
    check('joint-moment-decomposition/'+str(axis),total==carrier+record+cross)
    for label,op in ops.items():
        check('whole-moment-conserved/'+str(axis)+'/'+label,op.T*total*op==total)
        P=(S.eye(22)-op)/2
        check('whole-moment-continuous-generator/'+str(axis)+'/'+label,P.T*total==total*P)
    check('dropping-cross-term-changes-law/'+str(axis),any(op.T*(carrier+record)*op!=carrier+record for op in ops.values()))


def reading(state,block):
    return S.expand((state.conjugate().T*block*state)[0])

def decomposition(state):
    return tuple(S.Matrix([reading(state,m[i]) for m in moments]) for i in range(4))

census={'paths':0,'separate_sector_imbalance':0,'nonzero_cross_compensation':0}
example=None
for key,words in sorted(prior['groups'].items()):
    for word in words:
        before=prior['endpoint_state'](word[:2])
        after=prior['endpoint_state'](word)
        a,b=decomposition(before),decomposition(after)
        delta=[b[i]-a[i] for i in range(4)]
        census['paths']+=1
        check('actual-full-turn-moment-balance/'+','.join(word),delta[0]==S.zeros(3,1) and delta[1]+delta[2]+delta[3]==S.zeros(3,1))
        if delta[1]+delta[2]!=S.zeros(3,1):
            census['separate_sector_imbalance']+=1
            if example is None:example={'word':list(word),'carrier_change':list(map(str,delta[1])),
                'record_change':list(map(str,delta[2])),'cross_change':list(map(str,delta[3]))}
        if delta[3]!=S.zeros(3,1):census['nonzero_cross_compensation']+=1
check('cross-term-needed-on-actual-source-orbit',example is not None)

# Joint consistency on the same previously found nonreal-overlap example.
key,words,cycle_values=prior['example']
V=prior['states_at'](words,1)
for j in range(3):
    state=V[:,j]
    check('phase-charge-on-actual-complex-record/'+str(j),reading(state,metric)==1)
    check('whole-moments-are-phase-neutral/'+str(j),decomposition(S.I*state)==decomposition(state))
# The naive linear anchor-position map instead transforms with phase.
linear=S.Matrix([[VERTICES[b][axis] for a in 'ABCD' for b in 'ABCD'] for axis in range(3)])*anchor
check('linear-spatial-amplitude-is-not-internal-phase-neutral',linear*S.I!=linear)
check('history-cycle-phase-is-not-common-charge-coordinate',prior['gram'](S.I*V)==prior['gram'](V))

result={
    'schema':'marici.nima.joint-phase-retained-moment-balance.v1','status':'pass','checks':checks,
    'phase_result':'fixed six-port pulse dynamics permits one common carrier/record phase weight in the tested diagonal class; neutral/opposite record weights do not commute with those same fixed interactions',
    'phase_quantity':'Q=z^dagger metric z, conserved for the existing complex Hamiltonian realization; magnitude/sign of an external physical charge is not selected',
    'moment_result':'target-coordinate joint moment of a=y+F r is phase-neutral and conserved; separate carrier and record moments require the retained cross term',
    'moment_formula':'a^dagger X a = y^dagger X y + r^dagger F^dagger X F r + 2 Re(y^dagger X F r)',
    'actual_branch_census':census,'first_actual_compensation':example,
    'mechanical_scope':'exact collective first-moment balance, not proof that this quantity is position, mechanical momentum or center of mass; no inertial masses were inserted',
    'charge_scope':'common phase symmetry and neutral relational phase coexist. Dual effects or transforming feature/link data are different contracts, not counterexamples to the fixed-pulse weight test.',
    'source_reused':['same actual 68 branches','same AB excitation','same endpoint geometry','same fixed metric and complex pulses'],
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/joint-phase-retained-moment-balance.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact joint phase/moment checks')
print('Fixed exchanges require the same common phase weight on their coupled carrier and records.')
print('Whole spatial moment is phase-neutral and conserved; actual-branch cross-term census:',census)
print('No independent body masses or new interaction were introduced.')
