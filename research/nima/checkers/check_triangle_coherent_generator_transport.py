"""Transport the prior rotor section instead of re-minimizing at each stage.

E_next=F E C^-1 uses the actual retained successor F and existing rotor tick C.
This changes no source words or coefficients. The chosen initial section and
rotor-compatible metric remain explicit realization data.
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
    previous=runpy.run_path(str(HERE/'check_triangle_continuous_generator_lift.py'))
prior=previous['prior']; c=prior['c']; ledger=c['ledger']
RB=prior['R']*prior['B']; RBplus=(RB.T*RB).inv()*RB.T
A=previous['A']; H=previous['H']; C=prior['C']; V=previous['V']
theta=previous['theta']
frame=ledger.root
weights=[S.Rational(1)]*6
left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('existing-tick-commutes-with-generator',A*C==C*A)
check('existing-tick-preserves-active-metric',C.T*H*C==H)
check('all-endpoint-counts-reader-square',RBplus*prior['current']['M']==C*RBplus)
profiles=[]
old=None
for tick in range(4):
    child=ledger.successor(frame)
    sizes=[child.parent_slots.count(i) for i in range(len(frame.paths))]
    weights=[weights[i]/sizes[i] for i in child.parent_slots]
    frame=child
    F=S.Matrix(frame.step_lift)
    G=S.diag(*weights)
    n=len(frame.paths)
    O=S.Matrix([[int(path[-1][1]==v) for path in frame.paths] for v in 'ABCD'])
    P=RBplus*O
    if old is None:
        E=G.inv()*P.T*(P*G.inv()*P.T).inv()
    else:
        E=F*old['E']*C.inv()
    N=S.eye(n)-E*P
    L=E*A*P
    metric=P.T*H*P+N.T*G*N
    check('coherent-section/'+str(tick),P*E==S.eye(2))
    check('actual-endpoint-section/'+str(tick),O*E==RB)
    check('generator-observer/'+str(tick),P*L==A*P)
    check('fixed-hidden-coordinate/'+str(tick),L*N==S.zeros(n) and N*L==S.zeros(n))
    check('compatible-metric/'+str(tick),L.T*metric+metric*L==S.zeros(n))
    check('positive-metric-decomposition/'+str(tick),E*P+N==S.eye(n) and all(w>0 for w in weights))
    if old is not None:
        check('native-reader-square/'+str(tick),P*F==C*old['P'])
        check('full-generator-square/'+str(tick),L*F==F*old['L'])
        check('full-hidden-square/'+str(tick),N*F==F*old['N'])
        check('inherited-history-isometry/'+str(tick),F.T*G*F==old['G'])
        check('compatible-metric-history-isometry/'+str(tick),F.T*metric*F==old['metric'])
        # V(theta)=cos(2theta)I+sin(2theta)A/2. Comparing its three
        # coefficient matrices proves the flow square for every theta.
        check('all-theta-flow-square/'+str(tick),
              N*F==F*old['N'] and E*P*F==F*old['E']*old['P']
              and E*A*P*F==F*old['E']*A*old['P'])
    ld=dict(zip(left.paths,left.values));rd=dict(zip(right.paths,right.values))
    x=S.Matrix([ld.get(path,0)-rd.get(path,0) for path in frame.paths])
    check('actual-source-coordinates/'+str(tick),P*x==C**tick*prior['coordinates'])
    check('actual-Hamiltonian/'+str(tick),((P*x).T*H*(P*x))[0]==12)
    check('hidden-reader-zero/'+str(tick),O*N*x==S.zeros(4,1))
    if old is not None:
        check('actual-source-is-native-copy/'+str(tick),x==F*old['x'])
        check('actual-hidden-source-retained/'+str(tick),N*x==F*old['N']*old['x'])
        check('actual-total-realization-norm-conserved/'+str(tick),(x.T*metric*x)[0]==old['budget'])
    # Actual path labels and operand records are retained; no direct-limit
    # quotient identifies a longer history with its prefix.
    check('actual-history-length/'+str(tick),left.word_length==tick+2)
    budget=(x.T*metric*x)[0]
    profiles.append({'word_length':left.word_length,'frame_words':n,
                     'words_per_role':len(left.paths),'Hamiltonian':12,
                     'compatible_total_squared_norm':str(budget),
                     'hidden_squared_norm':str(((N*x).T*G*(N*x))[0])})
    old={'E':E,'P':P,'N':N,'L':L,'G':G,'metric':metric,'x':x,'budget':budget}
    new_left,new_right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
    for name,parent,child in [('LR',left,new_left),('RL',right,new_right)]:
        recovered,_=ledger.deconstruct_payload(child)
        check('retained-operand-identities/'+name+'/'+str(tick),recovered[0] is parent and recovered[1] is whole)
    left,right=new_left,new_right

result={
    'schema':'marici.nima.triangle-coherent-generator-transport.v1','status':'pass','checks':checks,
    'profiles':profiles,
    'section_rule':'E_next=F E C^-1; initial section is the earlier inherited-metric minimal section',
    'exact_identities':['P_next F=C P','L_next F=F L','N_next F=F N','F^T Grot_next F=Grot','W_next(theta) F=F W(theta)'],
    'positive_result':'transporting rather than re-minimizing the section repairs full cross-stage generator and hidden-sector compatibility',
    'scope':'coherent stagewise continuous realization with labelled history retention, not autonomous Hamiltonian creation of new stages',
    'remaining':['physical selection of initial section and rotor-compatible metric','continuous lift and rate calibration','physical rung4 observation and coupling'],
}
(ROOT/'results/triangle-coherent-generator-transport.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact coherent generator-transport checks')
print('Full generator, hidden component and compatible metric now transport through native extension.')
print('All-theta flow square holds; no history quotient or new clock was introduced.')
print('Profiles:',profiles)
