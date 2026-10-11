"""Continuous rotor lift through actual path-family endpoint observations.

Reuses L=E*A*P. Histories remain labelled; this is not autonomous creation
of successor records. Both inherited and rotor-compatible metrics are tested.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(HERE/'check_rotor_rung4_intertwiner.py'))
    prior=runpy.run_path(str(HERE/'check_triangle_hamiltonian_clock_bridge.py'))
c=prior['c']; ledger=c['ledger']
RB=prior['R']*prior['B']; RBplus=(RB.T*RB).inv()*RB.T
A=S.Matrix([[0,2/S.sqrt(3)],[-2*S.sqrt(3),0]])
H=S.diag(3,1)
J=S.Matrix([[0,S.sqrt(3)],[-S.sqrt(3),0]])
C=prior['C']; theta=S.symbols('theta',real=True)
V=S.simplify(prior['Q'].inv()*prior['flow']*prior['Q'])
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('same-angular-Hamiltonian',J*A== -2*H)
check('same-continuous-rotor',S.simplify(S.diff(V,theta)-A*V)==S.zeros(2))
check('same-discrete-tick',S.simplify(V.subs(theta,S.pi/3)-C)==S.zeros(2))
frame=ledger.root
weights=[S.Rational(1)]*6
left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
profiles=[]
previous=None
for tick in range(3):
    child=ledger.successor(frame)
    counts=[child.parent_slots.count(i) for i in range(len(frame.paths))]
    weights=[weights[i]/counts[i] for i in child.parent_slots]
    frame=child
    n=len(frame.paths)
    G=S.diag(*weights)
    O=S.Matrix([[int(path[-1][1]==v) for path in frame.paths] for v in 'ABCD'])
    P=RBplus*O
    covariance=P*G.inv()*P.T
    E=G.inv()*P.T*covariance.inv()
    N=S.eye(n)-E*P
    L=E*A*P
    check('right-inverse/'+str(tick),P*E==S.eye(2))
    check('actual-endpoint-section/'+str(tick),O*E==RB)
    check('continuous-generator-intertwiner/'+str(tick),P*L==A*P)
    check('hidden-component-fixed/'+str(tick),L*N==S.zeros(n) and N*L==S.zeros(n))
    # Exact all-theta formula: W=N+E*V(theta)*P, since PE=I and PN=NE=0.
    W=N+E*V*P
    check('all-theta-observer-intertwiner/'+str(tick),S.simplify(P*W-V*P)==S.zeros(2,n))
    check('all-theta-history-reconstruction/'+str(tick),S.simplify((N+E*V.subs(theta,-theta)*P)*W-S.eye(n))==S.zeros(n))
    check('inherited-metric-not-rotor-invariant/'+str(tick),A*covariance+covariance*A.T!=S.zeros(2))
    # A necessary condition for ANY inherited-G-skew L satisfying PL=AP
    # is A*(P G^-1 P^T)+(P G^-1 P^T)*A^T=0. Its failure is not specific to E.
    compatible=P.T*H*P+N.T*G*N
    check('compatible-metric-keeps-hidden-norm/'+str(tick),N.T*compatible*N==N.T*G*N)
    check('compatible-metric-active-isometry/'+str(tick),E.T*compatible*E==H)
    check('compatible-generator-skew/'+str(tick),L.T*compatible+compatible*L==S.zeros(n))
    # Positivity follows from x=E(Px)+Nx and positive H,G; no extra quotient.
    check('metric-positive-decomposition/'+str(tick),E*P+N==S.eye(n) and all(w>0 for w in weights))
    omega=P.T*J*P
    energy=P.T*H*P
    check('pulled-back-Hamilton-equation/'+str(tick),omega*L==-2*energy)
    check('presymplectic-not-hidden-symplectic-claim/'+str(tick),omega.rank()==2)
    ld=dict(zip(left.paths,left.values)); rd=dict(zip(right.paths,right.values))
    x=S.Matrix([ld.get(path,0)-rd.get(path,0) for path in frame.paths])
    observed=P*x
    check('actual-source-coordinate/'+str(tick),observed==C**tick*prior['coordinates'])
    check('actual-hidden-is-endpoint-invisible/'+str(tick),O*N*x==S.zeros(4,1))
    check('actual-between-tick-endpoint-reading/'+str(tick),S.simplify(O*W*x-RB*V*observed)==S.zeros(4,1))
    check('actual-Hamiltonian-twelve/'+str(tick),(x.T*energy*x)[0]==12)
    if previous is not None:
        lastP,lastL=previous
        copy=S.Matrix(frame.step_lift)
        check('native-extension-observation-square/'+str(tick),P*copy==C*lastP)
        defect=L*copy-copy*lastL
        check('extension-generator-defect-reader-invisible/'+str(tick),P*defect==S.zeros(2,copy.cols))
        full_extension_compatible=defect==S.zeros(*defect.shape)
    else:full_extension_compatible=None
    profiles.append({'words':n,'observer_rank':P.rank(),'hidden_dimension':n-2,
                     'induced_observer_covariance':[[str(v) for v in row] for row in covariance.tolist()],
                     'full_extension_generator_compatible':full_extension_compatible})
    previous=P,L
    left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)

result={
    'schema':'marici.nima.triangle-continuous-generator-lift.v1','status':'pass','checks':checks,
    'profiles':profiles,
    'generator':'L=E*A*P; continuous evolution W(theta)=N+E*V(theta)*P',
    'positive_result':'actual endpoint observer intertwines for ALL theta and history-hidden coordinates are retained and fixed within each stage',
    'metric_boundary':'the inherited decoder metric fails a necessary covariance condition; a separately declared rotor-compatible metric is exhibited, not inferred physical geometry',
    'Hamiltonian_scope':'pulled-back rotor energy is 12 on actual inputs; its presymplectic form has rank two, with fixed hidden parameters',
    'execution_boundary':'native path extension and continuous within-stage evolution agree under the cyclic observer; full hidden-sector generator transport must not be inferred from that equality',
    'clock':'existing chosen angular lift T=theta; no new timing assignment or seconds calibration',
}
(ROOT/'results/triangle-continuous-generator-lift.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact continuous-generator lift checks')
print('Actual endpoint readings agree with the existing rotor for all theta; hidden records remain retained.')
print('Inherited counting/decoder metric is incompatible; rotor-compatible metric is an explicit alternative.')
print('Stage profiles:',profiles)
