"""Exact response/closure test on the existing six-port exchange.

Only SymPy is needed. Count-checked AST extraction reuses the exact rational
source setup, without executing its NumPy comparison to the larger old model.
No dependency stubs, fitted mass, or alternate exchange law are used.
"""
from contextlib import redirect_stdout
from functools import lru_cache
from pathlib import Path
from collections import defaultdict
import ast
import hashlib
import io
import json
import sys
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/retained-spatial-response-closure.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

def tree(name):return ast.parse((HERE/name).read_text(encoding='utf-8'))
def evaluate(nodes,namespace):
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),
                 '<count-checked-source-extract>','exec'),namespace)
def assign(t,name):
    found=[n for n in t.body if isinstance(n,ast.Assign) and
           any(isinstance(v,ast.Name) and v.id==name for v in n.targets)]
    check('unique-source-assignment/'+name,len(found)==1)
    return found[0]

with redirect_stdout(io.StringIO()):
    import runpy
    source=runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
from photon_native_spatial_step import VERTICES
registry=source['registry'];labels=tuple(registry)
# These equations are taken from the original binding, not hand-copied.
t=tree('check_seed_port_exchange_binding.py')
ns={'S':S,'registry':registry,'labels':labels,'check':check}
evaluate([assign(t,n) for n in ['vertices','G','H','features','metric','operators']],ns)
loops=[n for n in t.body if isinstance(n,ast.For) and
       ast.unparse(n.target)=='(i, label)' and ast.unparse(n.iter)=='enumerate(labels)' and
       any(isinstance(v,ast.Assign) and any(ast.unparse(a)=='operators[label]' for a in v.targets)
           for v in n.body)]
check('unique-source-operator-constructor',len(loops)==1)
body=loops[0].body
check('source-operator-prefix-boundary',ast.unparse(body[10])=='a, b = registry[label]')
check('source-operator-prefix-shape',len(body[:10])==10 and
      [type(v).__name__ for v in body[:10]]==
      ['Assign']*5+['Expr']*3+['Assign','Expr'])
evaluate([ast.For(target=loops[0].target,iter=loops[0].iter,body=body[:10],orelse=[])],ns)
metric=ns['metric'];F=ns['features'];ops=ns['operators'];anchor=ns['anchor']
initial=S.zeros(22,1);initial[16+labels.index('AB')]=1
# Reuse the previous interpolation function and exact endpoint recursion.
history_tree=tree('check_retained_history_overlap_phase.py')
functions=[n for n in history_tree.body if isinstance(n,ast.FunctionDef) and
           n.name in ['endpoint_state','states_at']]
check('both-existing-history-evaluators-found',len(functions)==2)
hns={'S':S,'ops':ops,'initial':initial,'lru_cache':lru_cache}
evaluate(functions,hns)
endpoint_state=hns['endpoint_state'];states_at=hns['states_at']
# Reuse the first six statements of the existing target-moment construction.
joint_tree=tree('check_joint_phase_and_retained_moment_balance.py')
ml=[n for n in joint_tree.body if isinstance(n,ast.For) and ast.unparse(n.target)=='axis']
check('unique-source-moment-constructor',len(ml)==1)
check('source-moment-prefix-boundary',ast.unparse(ml[0].body[5])=='moments.append((total, carrier, record, cross))')
mn={'S':S,'F':F,'anchor':anchor,'VERTICES':VERTICES,'moments':[]}
evaluate([ast.For(target=ml[0].target,iter=ml[0].iter,body=ml[0].body[:6],orelse=[])],mn)
moments=mn['moments']

# The orbit lies in a 7-complex-dimensional invariant linear carrier:
# a=y+F r=f_AB*c, hence y=f_AB*c-F*r. No coordinate is discarded here.
f0=F[:,labels.index('AB')]
T=f0.col_join(S.zeros(6,1)).row_join((-F).col_join(S.eye(6)))
M=T.T*metric*T
check('faithful-compact-carrier',T.rank()==7 and M.is_positive_definite)
eta0=S.Matrix([1]+list(initial[16:,:]))
check('original-preparation-recovered',T*eta0==initial)
projectors={}
for label,E in ops.items():
    P=(S.eye(22)-E)/2
    compact=S.zeros(1,7).col_join((P*T)[16:,:])
    check('pulse-intertwiner/'+label,P*T==T*compact)
    check('pulse-projector/'+label,compact*compact==compact)
    check('Hamiltonian-adjoint/'+label,compact.T*M==M*compact)
    projectors[label]=compact
blocks=[tuple(T.T*b*T for b in row) for row in moments]

def expand(B):return B.applyfunc(S.expand)
def derivative(B,P):return expand(S.I*(P.T*B-B*P))
def reading(v,B):return S.expand((v.conjugate().T*B*v)[0])
def vector_read(v,forms):return S.Matrix([reading(v,B) for B in forms])
def compact_state(z):
    v=S.Matrix([1]+list(z[16:,:]))
    check('actual-state-reconstruction/'+str(len(checks)),expand(T*v-z)==S.zeros(22,1))
    return v

responses={};accelerations={}
for label,P in projectors.items():
    responses[label]=[tuple(derivative(B,P) for B in row) for row in blocks]
    accelerations[label]=[tuple(derivative(B,P) for B in row) for row in responses[label]]
    for axis,row in enumerate(blocks):
        R=responses[label][axis];A=accelerations[label][axis]
        check('response-Hermitian/'+label+'/'+str(axis),all(B.conjugate().T==B for B in R+A))
        check('whole-response-zero/'+label+'/'+str(axis),R[0]==S.zeros(7))
        check('cross-response-balance/'+label+'/'+str(axis),sum(R[1:],S.zeros(7))==S.zeros(7))
        check('second-response-balance/'+label+'/'+str(axis),sum(A[1:],S.zeros(7))==S.zeros(7))
        # P^2=P gives a literal third-derivative identity, not numeric differencing.
        check('fixed-port-third-derivative/'+label+'/'+str(axis),
              all(derivative(A[j],P)==-R[j] for j in range(4)))
    check('phase-charge-response-zero/'+label,derivative(M,P)==S.zeros(7))

ledger=source['ledger'];whole=ledger.retain_payload(ledger.root,(1,)*6)
groups=defaultdict(list)
for role,payload in [('LR',ledger.compose_payloads(source['L'],source['R'])),
                     ('RL',ledger.compose_payloads(source['R'],source['L']))]:
    for _ in range(6):payload=ledger.compose_payloads(payload,whole)
    for path in payload.paths:
        groups[(role,path[0][0],path[-1][1])].append(tuple(e[2] for e in path))
words=sorted(w for group in groups.values() for w in group)
check('actual-branch-census',len(words)==68)
actual_states=[];census={'paths':68,'nonzero_carrier_response':0,'nonzero_cross_response':0}
hostile=None
for word in words:
    v=compact_state(states_at([word],1)[:,0]);actual_states.append(v)
    R=responses[word[-1]]
    readings=[vector_read(v,[row[j] for row in blocks]) for j in range(4)]
    changes=[vector_read(v,[row[j] for row in R]) for j in range(4)]
    check('actual-response-balance/'+','.join(word),sum(changes[1:],S.zeros(3,1))==S.zeros(3,1))
    check('actual-unit-phase-quantity/'+','.join(word),reading(v,M)==1)
    if changes[1]!=S.zeros(3,1):census['nonzero_carrier_response']+=1
    if changes[3]!=S.zeros(3,1):census['nonzero_cross_response']+=1
    if hostile is None and changes[1]!=S.zeros(3,1):
        conjugate=S.conjugate(v)
        check('conjugation-retains-all-spatial-readings',
              all(vector_read(conjugate,[row[j] for row in blocks])==readings[j] for j in range(4)))
        check('conjugation-retains-charge',reading(conjugate,M)==reading(v,M))
        check('conjugation-reverses-response',
              all(vector_read(conjugate,[row[j] for row in R])==-changes[j] for j in range(4)))
        check('common-phase-cannot-explain-hostile',
              all(vector_read(S.I*v,[row[j] for row in R])==changes[j] for j in range(4)))
        hostile={'word':list(word),'port':word[-1],
            'carrier_response':list(map(str,changes[1])),
            'record_response':list(map(str,changes[2])),
            'cross_response':list(map(str,changes[3])),
            'scope':'first state is an actual forward midpoint; its conjugate is a state-domain hostile, also obtained by the same final projector at area -pi/2; not asserted to be another of the 68 forward midpoints'}
check('nonzero-response-hostile-exists',hostile is not None)
check('actual-midpoints-span-compact-carrier',S.Matrix.hstack(*actual_states).rank()==7)

# Ordinary positions must Poisson commute under the inherited symplectic form.
# Omega=2 Im(dz^dagger M dz); i_X Omega=dh and h_e=z^dagger M P_e z.
inv=M.inv()
def poisson(B,C):return expand(S.I*(C*inv*B-B*inv*C))
# Also fix the prepared anchor c=1: the actual affine six-coordinate sector
# has inherited metric M_rr. Check that the obstruction is not an artifact
# of allowing the otherwise conserved anchor coordinate to vary.
fixed_anchor_inv=S.diag(0,M[1:,1:].inv())
poisson_residuals={}
for i in range(3):
    for j in range(i+1,3):
        residual=poisson(blocks[i][1],blocks[j][1])
        nonzero_values=[reading(v,residual) for v in actual_states]
        B,C=blocks[i][1],blocks[j][1]
        fixed_residual=expand(S.I*(C*fixed_anchor_inv*B-B*fixed_anchor_inv*C))
        poisson_residuals[f'{i},{j}']={'nonzero':residual!=S.zeros(7),'rank':residual.rank(),
            'actual_midpoints_nonzero':sum(value!=0 for value in nonzero_values),
            'first_nonzero_value':str(next((v for v in nonzero_values if v!=0),0)),
            'fixed_anchor_rank':fixed_residual.rank(),
            'fixed_anchor_actual_midpoints_nonzero':sum(reading(v,fixed_residual)!=0 for v in actual_states)}
check('candidate-positions-not-canonical',any(v['nonzero'] for v in poisson_residuals.values()))
check('position-bracket-obstruction-on-actual-midpoints',
      any(v['actual_midpoints_nonzero'] for v in poisson_residuals.values()))
check('position-bracket-obstruction-with-prepared-anchor-fixed',
      any(v['fixed_anchor_actual_midpoints_nonzero'] for v in poisson_residuals.values()))
for label,P in projectors.items():
    for axis in range(3):
        B=blocks[axis][1];H=M*P
        check('inherited-Hamilton-response/'+label+'/'+str(axis),
              poisson(B,H)==responses[label][axis][1])
        check('fixed-anchor-Hamilton-response/'+label+'/'+str(axis),
              expand(S.I*(H*fixed_anchor_inv*B-B*fixed_anchor_inv*H))==responses[label][axis][1])
# Same fixed canonical x,p and H_e=T(p)+V_e(x) would give one x response.
common_velocity=all(responses[label][axis][1]==responses[labels[0]][axis][1]
                    for label in labels for axis in range(3))
check('common-kinetic-plus-position-potential-test-fails',not common_velocity)

# A nonorthogonal state chart must transport the metric and all forms.
chart=S.diag(*range(1,8));chart_inv=chart.inv();chart_M=chart.T*M*chart
for label,P in projectors.items():
    chart_P=chart_inv*P*chart
    for axis in range(3):
        B=blocks[axis][1]
        check('response-chart-transport/'+label+'/'+str(axis),
              derivative(chart.T*B*chart,chart_P)==chart.T*derivative(B,P)*chart)
for i in range(3):
    for j in range(i+1,3):
        B,C=chart.T*blocks[i][1]*chart,chart.T*blocks[j][1]*chart
        moved=expand(S.I*(C*chart_M.inv()*B-B*chart_M.inv()*C))
        check('Poisson-chart-transport/'+str(i)+'/'+str(j),
              moved==chart.T*poisson(blocks[i][1],blocks[j][1])*chart)
# The complete raw coherence matrix closes, without a probability postulate.
v=actual_states[0];C=v*v.conjugate().T
for label,P in projectors.items():
    dotC=-S.I*(P*C-C*P.T)
    check('coherence-charge-preserved/'+label,S.expand(S.trace(M*dotC))==0)
    for axis in range(3):
        check('coherence-readout-response/'+label+'/'+str(axis),
              S.expand(S.trace(blocks[axis][1]*dotC))==reading(v,responses[label][axis][1]))
check('coherence-common-phase-neutral',(S.I*v)*(S.I*v).conjugate().T==C)

# Exact real span of Hermitian forms, not an asserted count of physical DOFs.
def encode(B):
    return [S.re(B[i,i]) for i in range(7)]+[
        part(B[i,j]) for i in range(7) for j in range(i+1,7) for part in (S.re,S.im)]
rows={};basis=[]
def add(B,name):
    v=encode(B)
    for pivot,row in sorted(rows.items()):
        c=v[pivot]
        if c:v=[x-c*y for x,y in zip(v,row)]
    pivot=next((i for i,x in enumerate(v) if x),None)
    if pivot is None:return False
    c=v[pivot];rows[pivot]=[x/c for x in v]
    basis.append((B,name));return True
for axis,row in enumerate(blocks):
    for j,B in enumerate(row):add(B,f'moment/{axis}/{j}')
add(M,'phase-quantity')
ranks=[len(basis)];front=list(basis);rounds=[]
while front:
    start=len(basis)
    for B,name in front:
        for label,P in projectors.items():add(derivative(B,P),f'D_{label}({name})')
    front=basis[start:]
    rounds.append({'order':len(rounds)+1,'rank':len(basis),'new_forms':len(front)})
    if front:ranks.append(len(basis))
    check('bounded-Hermitian-span/'+str(len(rounds)),len(basis)<=49)
check('first-response-packet-not-linearly-closed',len(ranks)>2 and ranks[2]>ranks[1])
check('full-Hermitian-closure',len(basis)==49)

files=[Path(__file__),HERE/'check_seed_port_exchange_binding.py',
       HERE/'check_actual_triangle_branch_composition.py',
       HERE/'check_retained_history_overlap_phase.py',
       HERE/'check_joint_phase_and_retained_moment_balance.py',
       HERE/'photon_native_spatial_step.py',HERE/'check_natural_tower_return.py',
       HERE/'retained_path_successor.py']
result={'schema':'marici.nima.retained-spatial-response-closure.v1','status':'pass',
    'checks':checks,'check_count':len(checks),'parameter':'declared pulse area alpha, not a newly calibrated physical time',
    'compact_carrier_complex_dimension':7,'actual_midpoint_census':census,
    'conjugation_hostile':hostile,'carrier_position_Poisson_residuals':poisson_residuals,
    'linear_quadratic_observer_ranks':ranks,'closure_rounds':rounds,
    'common_kinetic_natural_mechanics_candidate':{'H':'T(p)+V_e(x), same canonical x,p and T for all ports',
        'passes':False,'reasons':['candidate carrier readings do not Poisson commute','first responses depend on port']},
    'positive':'exact phase-neutral first and second responses; carrier+record+cross responses balance; whole seven-coordinate coherence matrix closes under all ports',
    'negative':'spatial first moments alone fail state-domain response descent; including all first responses still fails linear quadratic closure',
    'not_claimed':['no general collective-mechanics no-go','49 observable directions are not 49 independent state degrees of freedom',
        'no physical mass, velocity, momentum or time calibration','conjugate hostile not claimed forward-midpoint reachable'],
    'verification_scope':'count-checked exact AST extraction plus fresh actual branch construction; the old NumPy/137-port numeric comparison and previous phase census were not rerun',
    'python':sys.executable,'sympy':S.__version__,
    'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact spatial-response checks')
print('Actual midpoint response census:',census)
print('Quadratic observer ranks:',ranks)
print('Noncommuting carrier-coordinate brackets:',poisson_residuals)
print('First hostile:',hostile['word'],hostile['carrier_response'])
