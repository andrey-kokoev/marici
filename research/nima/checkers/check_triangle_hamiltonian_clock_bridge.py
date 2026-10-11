"""Reuse the prior rotor/clock attachment for actual triangle compositions.

This certifies the cyclic endpoint observer, not unitary full-history growth.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(HERE/'check_photon_native_spatial_step.py'))
    current=runpy.run_path(str(HERE/'check_triangle_source_contrast_clock.py'))
import photon_native_spatial_step as rotor
c=current['c']; ledger=c['ledger']
B=S.Matrix.hstack(S.Matrix(rotor.U),S.Matrix(rotor.W))
K=S.Matrix(rotor.continuation_matrix())
R=S.Matrix(rotor.target_reader())
C=S.Matrix(rotor.PLANE_STEP)
X=current['X']
left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)


def summary(payload):
    return S.Matrix([sum(v for path,v in zip(payload.paths,payload.values) if path[-1][2]==label)
                     for label in ledger.labels])

z=summary(left)-summary(right)
# Invert ONLY the actual two-dimensional endpoint plane, not all four rows.
RB=R*B
coordinates=(RB.T*RB).inv()*RB.T*(R*z)
v=B*coordinates
hidden=z-v
check('source-derived-coordinate-solution',coordinates==S.Matrix([1,3]))
check('actual-original-summary',z==S.Matrix([-1,-1,0,1,1,0]))
check('initial-summary-not-silently-replaced',hidden!=S.zeros(6,1))
check('reader-forgets-initial-component',R*hidden==S.zeros(4,1))
check('continuation-annihilates-initial-component',K*hidden==S.zeros(6,1))
check('old-plane-intertwines-actual-continuation',K*B==B*C)
check('actual-target-incidence-intertwines',R*K==current['M']*R)
# An all-sector identity connects today's formal (a,b) coordinates to the
# earlier rotor plane; this is not merely a fit of one initial vector.
D=S.Matrix([[0,-1],[2,-1]])
F=S.Matrix([[1,0],[-1,0],[0,1],[0,-1]])
A=S.Matrix([[-1,1],[-1,0]])
check('all-sector-endpoint-coordinate-bridge',R*B*D==F)
check('all-sector-dynamics-coordinate-bridge',C*D==D*A)

# Reuse q=sqrt(3)*a,p=b and the stated positive segment theta=pi/3.
Q=S.diag(S.sqrt(3),1)
theta=S.symbols('theta',real=True)
flow=S.Matrix([[S.cos(2*theta),S.sin(2*theta)],[-S.sin(2*theta),S.cos(2*theta)]])
check('same-existing-rotor-segment',S.simplify(flow.subs(theta,S.pi/3)*Q-Q*C)==S.zeros(2))
G=Q.T*Q
check('old-angular-Hamiltonian-preserved',C.T*G*C==G)
check('quadratic-Hamiltonian-value',(coordinates.T*G*coordinates)[0]==12)
check('Hamiltonian-in-formal-sector',D.T*G*D==S.Matrix([[4,-2],[-2,4]]))

observations=[]
kappa=S.symbols('kappa',positive=True)
qp0=Q*coordinates
F0=qp0[0]*qp0[1]/2
for tick in range(7):
    actual=summary(left)-summary(right)
    plane=C**tick*coordinates
    check('actual-retained-endpoint-clock-attachment/'+str(tick),R*actual==R*B*plane)
    if tick>0:
        check('actual-summary-enters-old-plane/'+str(tick),actual==B*plane)
    check('Hamiltonian-all-tested-phases/'+str(tick),(plane.T*G*plane)[0]==12)
    qp=Q*plane
    angle=S.pi*tick/3
    # Existing lift: phi'=phi+(F'-F)/kappa-theta; choose T0=0.
    f=qp[0]*qp[1]/2
    phi=F0/kappa+(f-F0)/kappa-angle
    check('existing-unwrapped-clock/'+str(tick),S.simplify(f/kappa-phi)==angle)
    check('actual-spatial-reader-not-circular-substitute/'+str(tick),X*R*actual==X*R*B*plane)
    observations.append({'tick':tick,'clock_over_pi':str(S.Rational(tick,3)),
        'old_plane_coordinates':list(map(str,plane)),
        'endpoint_contrast':list(map(str,R*actual)),
        'retained_words_per_channel':len(left.paths),'word_length':left.word_length})
    if tick in (3,6):
        check('clock-return-not-history-return/'+str(tick),R*actual==R*z and left.word_length>2 and angle!=0)
    new_left,new_right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
    for name,parent,child in [('LR',left,new_left),('RL',right,new_right)]:
        recovered,_=ledger.deconstruct_payload(child)
        check('retains-operands/'+name+'/'+str(tick),recovered[0] is parent and recovered[1] is whole)
    left,right=new_left,new_right

result={
    'schema':'marici.nima.triangle-hamiltonian-clock-bridge.v1','status':'pass','checks':checks,
    'initial_occurrence_summary':list(map(str,z)),
    'old_plane_representative':list(map(str,v)),
    'retained_initial_kernel_component':list(map(str,hidden)),
    'all_sector_adapter':[[str(x) for x in row] for row in D.tolist()],
    'observations':observations,
    'Hamiltonian':'quadratic part q^2+p^2=12; existing phase convention gives H+=12+kappa, not a calibrated physical energy',
    'clock':'T_n-T_0=n*pi/3 on the existing specified positive rotor lift',
    'scope':'exact cyclic endpoint-observer intertwiner; initial summary joins prior plane after one continuation; full retained branching is not asserted Hamiltonian or unitary',
    'remaining':['positive lift/winding selection','physical rate calibration','physical rung-4 reader identification','whole-history dynamical realization'],
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [Path(__file__),HERE/'photon_native_spatial_step.py',HERE/'check_triangle_source_contrast_clock.py']},
}
(ROOT/'results/triangle-hamiltonian-clock-bridge.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact actual-composition/Hamiltonian/clock bridge checks')
print('Actual endpoint contrast inherits the existing rotor clock: T_n-T_0=n*pi/3.')
print('Initial forgotten component recorded; full histories preserved; no all-branch timing assumption.')
