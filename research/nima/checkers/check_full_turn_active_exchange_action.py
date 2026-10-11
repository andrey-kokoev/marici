"""Full-turn branch action on the existing six-dimensional exchange sector.

Retain every actual branch; do not turn their sum into a single pulse.
Classify the joint invariants before importing local mechanical readouts.
"""
from contextlib import redirect_stdout
from pathlib import Path
from functools import lru_cache
import io
import json
import hashlib
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_rotor_exchange_source_operation_comparison.py'))
exchange=prior['exchange']; source=prior['source']; ledger=source['ledger']
labels=exchange['labels']; K=exchange['K']; B=exchange['B']
G=K.inv(); ops=exchange['operators']
active={label:S.eye(6)-K[:,i]*S.eye(6)[i,:] for i,label in enumerate(labels)}
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('active-metric-positive',all(v>0 for v in K.LDLdecomposition(hermitian=False)[1].diagonal()))
for label,T in active.items():
    check('exact-existing-active-action/'+label,B*ops[label]==T*B)
    check('active-involution/'+label,T*T==S.eye(6))
    check('active-energy-conservation/'+label,T.T*G*T==G)
    projector=(S.eye(6)-T)/2
    check('continuous-pulse-self-adjoint/'+label,projector.T*G==G*projector)
    check('continuous-pulse-projector/'+label,projector*projector==projector)

@lru_cache(None)
def act(word):
    if not word:return S.eye(6)
    return active[word[-1]]*act(word[:-1])

left=ledger.compose_payloads(source['L'],source['R'])
right=ledger.compose_payloads(source['R'],source['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
initial={tuple(e[2] for e in path):role for role,p in [('LR',left),('RL',right)] for path in p.paths}
for _ in range(6):
    left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
check('actual-full-turn-branch-count',len(left.paths)==len(right.paths)==34)
probe=B*exchange['excited']  # Reuse original AB-record preparation.
energy=(probe.T*G*probe)[0]
branching={v:sum(a==v for label,a,b in source['PACKETS']) for v in 'ABCD'}
branches=[]; common_return=[]; weights_by_prefix={p:S.Rational(0) for p in initial}
weighted_energy=S.Rational(0)
for role,payload in [('LR',left),('RL',right)]:
    for path in payload.paths:
        word=tuple(e[2] for e in path); prefix,suffix=word[:2],word[2:]
        check('same-actual-prefix/'+','.join(word),initial[prefix]==role and len(suffix)==6)
        T=act(suffix)
        check('full-turn-active-energy/'+','.join(word),T.T*G*T==G)
        # The initial two-arrow preparation is retained, not counted as one
        # of the six subsequent rotor-clocked continuation steps.
        before=act(prefix)*probe; after=T*before
        check('prefix-to-whole-action/'+','.join(word),after==act(word)*probe)
        weight=S.Rational(1,2)
        for edge in path[2:]:weight/=branching[edge[0]]
        weights_by_prefix[prefix]+=weight
        weighted_energy+=weight*(after.T*G*after)[0]
        common_return.append(T-S.eye(6))
        branches.append({'role':role,'prefix':list(prefix),'six_step_word':list(suffix),
                         'returned_endpoint':path[1][1]==path[-1][1],
                         'action_rank':int((T-S.eye(6)).rank()),
                         'existing_probe_changed':after!=before,
                         'inherited_weight':str(weight)})
check('inherited-family-weight-not-created',all(w==S.Rational(1,2) for w in weights_by_prefix.values()))
check('weighted-active-energy-preserved',weighted_energy==2*energy)
check('no-common-full-turn-active-fixed-vector',S.Matrix.vstack(*common_return).rank()==6)

# A single charge or total momentum that is LINEAR in these active variables
# and conserved under every primitive would need a common invariant covector.
covector_constraints=S.Matrix.vstack(*(T.T-S.eye(6) for T in active.values()))
check('no-common-active-linear-conserved-reading',covector_constraints.rank()==6)

# Compute the FULL real commutant, not just diagonal invariants or one orbit.
variables=S.symbols('x0:36')
X=S.Matrix(6,6,variables)
equations=[entry for T in active.values() for entry in X*T-T*X]
coefficients,rhs=S.linear_eq_to_matrix(equations,variables)
check('commutant-dimension-one',coefficients.rank()==35 and rhs==S.zeros(len(equations),1))
check('commutant-generated-by-identity',coefficients*S.Matrix(list(S.eye(6)))==S.zeros(len(equations),1))
# Positive G and G-orthogonal involutions imply an invariant subspace would
# have a commuting G-orthogonal projector. Scalar commutant => irreducible.
# Also every invariant symmetric quadratic Q has G^-1 Q in this commutant:
# Q must be a scalar multiple of G, hence cannot distinguish charge signs.

# Concrete local recoil compatibility is retained, not claimed absent.
# At each port carrier a=f^T H y and record b swap. Their sum is locally
# fixed but is disturbed in general by a DIFFERENT overlapping port.
local_momenta={}
for i,label in enumerate(labels):
    row=(exchange['features'][:,i].T*exchange['H']).row_join(S.eye(6)[i,:])
    check('local-total-momentum-candidate-conserved/'+label,row*ops[label]==row)
    local_momenta[label]=row
cross_disturbances=[(a,b) for a,row in local_momenta.items() for b,op in ops.items() if row*op!=row]
check('local-momentum-is-not-global',len(cross_disturbances)==30)

result={
    'schema':'marici.nima.full-turn-active-exchange-action.v1','status':'pass','checks':checks,
    'active_metric':[[str(v) for v in row] for row in G.tolist()],
    'branch_actions':branches,
    'branch_summary':{'total':len(branches),'endpoint_closed':sum(b['returned_endpoint'] for b in branches),
                      'changed_on_existing_probe':sum(b['existing_probe_changed'] for b in branches)},
    'existing_probe_active_energy':str(energy),'weighted_family_active_energy':str(weighted_energy),
    'invariants':{'active_dimension':6,'common_full_turn_fixed_dimension':0,
                  'common_linear_conserved_dimension':0,'commutant_dimension':1},
    'positive_result':'all 68 actual full-turn branches have exact ordered six-dimensional actions preserving the SAME positive quadratic form; the family is not reduced to a single summed pulse',
    'global_structure':'the active six-port representation is irreducible over R; its invariant symmetric quadratic forms are scalar multiples of the existing metric',
    'charge_scope':'no nonzero common linear active charge and no independent quadratic invariant in this class; nonlinear, complex-dual and anchored charge structures are not excluded',
    'recoil_scope':'single-port elastic recoil remains valid, but its local momentum sum changes under every other port. A nontrivial closed linear two-body momentum reading cannot be obtained by identifying all these local sums.',
    'not_assumed':['Born probabilities for inherited weights','physical summation of branches','a single selected trajectory','new masses or charge couplings','work generated from phase return'],
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/full-turn-active-exchange-action.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact full-turn active-action checks')
print('Branch summary:',result['branch_summary'])
print('All branches conserve active energy. Six-dimensional action is irreducible; scalar commutant only.')
print('Local recoil sums are conserved at their own port but changed by all 30 cross-port pairs.')
