"""Reference-relative canonical coordinates for the EXISTING port pulses.

The full reference phase/charge pair is retained. No physical clock, mass,
new Hamiltonian, measurement rule, or averaged-state rank-one rule is added.
"""
from contextlib import redirect_stdout
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/relative-anchor-canonical-chart.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_retained_spatial_response_closure.py'))
M=prior['M'];T=prior['T'];F=prior['F'];G=prior['metric'];labels=prior['labels']
projectors=prior['projectors'];blocks=prior['blocks'];source=prior['source']
vertices=prior['VERTICES'];checks=[]
def check(name,ok):
    if not ok:raise AssertionError(name)
    checks.append(name)
def expand(B):return B.applyfunc(S.expand)
def scalar(x):return S.simplify(S.expand(x))
def J(n):return S.zeros(n).row_join(S.eye(n)).col_join((-S.eye(n)).row_join(S.zeros(n)))

def reject(name,fn):
    try:fn()
    except ValueError:checks.append(name);return
    raise AssertionError('expected refusal: '+name)

# Complete the square in the old metric, rather than fitting a center.
K=M[1:,1:];Ki=K.inv();s=-M[1:,0];b=Ki*s
mu=scalar(M[0,0]-(s.T*b)[0])
L=S.eye(7);L[1:,0]=b
check('positive-anchor-and-active-metric',mu>0 and K.is_positive_definite)
check('metric-derived-orthogonal-split',L.T*M*L==S.diag(mu,K))
check('old-unit-feature-normalization',all(K[i,i]==2 for i in range(6)))

def active_budget(q,p):return scalar((q.T*K*q)[0]+(p.T*Ki*p)[0]/4)

@dataclass(frozen=True)
class Chart:
    phase: object       # c/|c|, not an unwrapped history or a physical clock
    charge: object      # old total quadratic phase quantity
    q: object
    p: object
    record: object      # exact original source-family/slot/pulse record

def to_chart(eta,record):
    c=eta[0]
    if c==0:raise ValueError('zero-anchor chart is unavailable')
    radius=S.sqrt(scalar(S.conjugate(c)*c))
    phase=scalar(c/radius)
    u=expand(S.conjugate(phase)*(eta[1:,:]-b*c))
    q=u.applyfunc(lambda x:scalar(S.re(x)))
    p=expand(2*K*u.applyfunc(lambda x:scalar(S.im(x))))
    charge=scalar((eta.conjugate().T*M*eta)[0])
    return Chart(phase,charge,S.ImmutableMatrix(q),S.ImmutableMatrix(p),record)

def from_chart(packet):
    if scalar(packet.phase*S.conjugate(packet.phase))!=1:
        raise ValueError('reference phase must have unit modulus')
    if any(S.im(x)!=0 for x in list(packet.q)+list(packet.p)):
        raise ValueError('canonical coordinates must be real')
    radius2=scalar((packet.charge-active_budget(packet.q,packet.p))/mu)
    if radius2.is_positive is not True:
        raise ValueError('reference radius must be strictly positive')
    c=S.sqrt(radius2)*packet.phase
    r=expand(b*c+packet.phase*(packet.q+S.I*Ki*packet.p/2))
    return S.Matrix([c]).col_join(r),packet.record

def relative_from_coherence(C):
    if C.shape!=(7,7) or C.conjugate().T!=C or C[0,0].is_positive is not True:
        raise ValueError('nonzero positive anchor entry required')
    if C.rank()!=1:raise ValueError('mixed coherence does not obey pure reconstruction')
    return expand(C[1:,0]/C[0,0])

# All-variable global form: eta=e^(i phi) L (R,q+i K^-1 p/2).
# By phase invariance it suffices to evaluate its Jacobian at phi=0.
R=S.Symbol('R',positive=True)
q=S.Matrix(S.symbols('q0:6',real=True));p=S.Matrix(S.symbols('p0:6',real=True))
u=q+S.I*Ki*p/2
centered=S.Matrix([R]).col_join(u)
Jac=S.eye(7)[:,0].row_join(S.I*centered).row_join(S.zeros(1,6).col_join(S.eye(6))).row_join(S.zeros(1,6).col_join(S.I*Ki/2))
Omega=expand(2*(Jac.conjugate().T*S.diag(mu,K)*Jac).applyfunc(S.im))
energy=active_budget(q,p);charge=mu*R**2+energy
coords=[R,S.Symbol('phi',real=True),*q,*p]
dcharge=S.Matrix([S.diff(charge,x) for x in coords]);ephi=S.eye(14)[:,1]
expected=S.diag(S.zeros(2),J(6))+dcharge*ephi.T-ephi*dcharge.T
check('global-form-includes-reference-charge',expand(Omega-expected)==S.zeros(14))
check('reference-coupling-not-zero',Omega[:2,2:]!=S.zeros(2,12))
# Transport the action primitive too: dropping this exact endpoint term
# would preserve equations but not the same retained action comparison.
beta=expand((centered.conjugate().T*S.diag(mu,K)*Jac).applyfunc(S.im))
canonical_oneform=S.Matrix([[0,-charge,*p,*([0]*6)]])
boundary=S.Matrix([[S.diff((q.T*p)[0]/2,x) for x in coords]])
check('action-primitive-endpoint-term',expand(-beta-canonical_oneform+boundary)==S.zeros(1,14))
# Replace (R,phi) by (phi, pi_phi=-charge), retaining its true cross terms.
change=S.zeros(14)
change[0,1]=-1/(2*mu*R)
change[0,2:8]=-(K*q).T/(mu*R)
change[0,8:14]=-(Ki*p).T/(4*mu*R)
change[1,0]=1
change[2:14,2:14]=S.eye(12)
expected_canonical=S.diag(J(1),J(6))
check('global-canonical-reference-pair',expand(change.T*Omega*change-expected_canonical)==S.zeros(14))
check('fixed-reference-form-canonical',Omega[2:,2:]==J(6))
# This reduction is justified only AFTER deriving the global form: restrict
# Q and quotient its common-phase direction, on this nonzero-anchor chart.
fixed_charge_inclusion=S.eye(14)[:,[0]+list(range(2,14))]
fixed_charge_form=fixed_charge_inclusion.T*expected_canonical*fixed_charge_inclusion
check('fixed-charge-phase-radical',fixed_charge_form==S.diag(S.zeros(1),J(6)) and fixed_charge_form.rank()==12)
# Raw ratios alone have a reference-intensity metric factor on a fixed fiber.
check('raw-relative-quadratures-are-not-naively-canonical',2*K!=S.eye(6))

# One shared q,p chart for ALL ports; derive each Hamiltonian from the old one.
C=S.eye(6).row_join(S.I*Ki/2)
embedding=S.eye(7)[:,0].row_join(S.zeros(1,12).col_join(C))
As={};Hs={};orth_projectors={}
for i,label in enumerate(labels):
    ei=S.eye(6)[:,i];rank_one=ei*ei.T
    D=rank_one*K/2
    old=L.inv()*projectors[label]*L
    check('centered-old-generator/'+label,old==S.diag(0,D))
    H=S.diag(K*rank_one*K/2,rank_one/8)
    A=2*J(6)*H
    As[label]=A;Hs[label]=H;orth_projectors[label]=D
    check('Hamiltonian-intertwiner/'+label,expand(C*A+S.I*D*C)==S.zeros(6,12))
    pulled=embedding.conjugate().T*L.T*M*projectors[label]*L*embedding
    check('old-Hamiltonian-equals-canonical-one/'+label,
          expand(pulled.applyfunc(S.re)-S.diag(0,H))==S.zeros(13))
    check('all-port-symplectic-generator/'+label,A.T*J(6)+J(6)*A==S.zeros(12))
    check('same-pulse-frequency-polynomial/'+label,A**3==-A)
    budget=S.diag(K,Ki/4)
    check('old-active-budget-preserved/'+label,A.T*budget+budget*A==S.zeros(12))
    reflection=S.eye(6)-rank_one*K
    check('full-exchange-is-cotangent-lift/'+label,
          S.eye(12)+2*A*A==S.diag(reflection,reflection.inv().T))
check('ordered-pulses-not-replaceable-by-summed-flow',As['AB']*As['BA']!=As['BA']*As['AB'])

# Reuse complete registered family objects, not just decoded numerical words.
ledger=source['ledger'];whole=ledger.retain_payload(ledger.root,(1,)*6)
packets=[];census={'retained_paths':0,'midpoint_and_endpoint_recoveries':0,
                   'nonzero_midpoint_momenta':0,'zero_endpoint_momenta':0}
for role,left,right in [('LR',source['L'],source['R']),('RL',source['R'],source['L'])]:
    family=ledger.compose_payloads(left,right)
    for _ in range(6):family=ledger.compose_payloads(family,whole)
    for slot,path in enumerate(family.paths):
        word=tuple(e[2] for e in path);census['retained_paths']+=1
        before=prior['endpoint_state'](word[:-1])
        eta_before=S.Matrix([1]+list(before[16:,:]))
        start=to_chart(eta_before,(family,slot,'before-final-pulse'))
        qp0=start.q.col_join(start.p)
        for sample in (1,2):
            z=prior['states_at']([word],sample)[:,0]
            eta=S.Matrix([1]+list(z[16:,:]))
            record=(family,slot,sample)
            packet=to_chart(eta,record);packets.append(packet)
            if sample==1 and packet.p!=S.zeros(6,1):census['nonzero_midpoint_momenta']+=1
            if sample==2 and packet.p==S.zeros(6,1):census['zero_endpoint_momenta']+=1
            restored,kept=from_chart(packet)
            check('actual-full-state-recovery/'+str(len(packets)),expand(T*restored-z)==S.zeros(22,1))
            check('retained-family-identity/'+str(len(packets)),kept is record and kept[0] is family)
            A=As[word[-1]]
            flow=S.eye(12)+A+A*A if sample==1 else S.eye(12)+2*A*A
            check('actual-canonical-pulse/'+str(len(packets)),expand(flow*qp0-packet.q.col_join(packet.p))==S.zeros(12,1))
            check('actual-charge-and-anchor/'+str(len(packets)),packet.charge==1 and packet.phase==1)
            check('all-prior-readings-recovered/'+str(len(packets)),
                  all(prior['reading'](restored,B)==prior['reading'](eta,B) for row in blocks for B in row))
            census['midpoint_and_endpoint_recoveries']+=1
check('same-68-retained-paths',census['retained_paths']==68)
check('canonical-momentum-response-nonvacuous',census['nonzero_midpoint_momenta']>0)
check('real-exchange-endpoints-are-turning-points-in-this-chart',census['zero_endpoint_momenta']==68)
# All-current coordinates needed to reconstruct every old overlap, not merely
# the selected intensity profile. Identity of reconstructed vectors proves it.
for packet in packets[:3]:
    eta,record=from_chart(packet)
    for g in [S.I,-1,(3+4*S.I)/5]:
        moved=to_chart(g*eta,record)
        check('common-phase-neutral/'+str(len(checks)),moved.q==packet.q and moved.p==packet.p and moved.charge==packet.charge)
        check('reference-co-transforms/'+str(len(checks)),scalar(moved.phase-g*packet.phase)==0)
    coh=expand(eta*eta.conjugate().T)
    xi=relative_from_coherence(coh)
    check('relative-amplitude-from-coherence/'+str(len(checks)),xi==expand(eta[1:,:]/eta[0]))
    check('rank-one-coherence-recovery/'+str(len(checks)),
          expand(coh[1:,1:]-coh[1:,0]*coh[0,1:]/coh[0,0])==S.zeros(6))
    conjugate=to_chart(S.conjugate(eta),record)
    check('relative-phase-is-not-erased/'+str(len(checks)),conjugate.q==packet.q and conjugate.p==-packet.p)

# Keep failures as explicit domain boundaries.
reject('zero-anchor-refused',lambda:to_chart(S.Matrix([0,1,0,0,0,0,0]),None))
reject('vacuum-refused',lambda:to_chart(S.zeros(7,1),None))
zero_anchor_state=S.Matrix([0,1,0,0,0,0,0])
raw_after=(S.eye(7)-2*projectors['AB'])*zero_anchor_state
check('zero-anchor-is-regular-in-original-state',raw_after[0]==0 and raw_after!=zero_anchor_state)
eta,_=from_chart(packets[0]);scaled=(3+4*S.I)*eta
check('nonunit-anchor-radius-roundtrip',expand(from_chart(to_chart(scaled,None))[0]-scaled)==S.zeros(7,1))
reject('mixed-coherence-refused',lambda:relative_from_coherence(S.eye(7)))
reject('nonunit-reference-refused',lambda:from_chart(Chart(2,1,S.zeros(6,1),S.zeros(6,1),None)))
reject('zero-reference-radius-refused',lambda:from_chart(Chart(1,0,S.zeros(6,1),S.zeros(6,1),None)))
# Changing the anchor basis by i is a passive canonical quadrature rotation,
# NOT evidence for a unique physical configuration/momentum polarization.
frame=S.zeros(6).row_join(-Ki/2).col_join((2*K).row_join(S.zeros(6)))
check('reference-basis-rotation-symplectic',frame.T*J(6)*frame==J(6))
for label,H in Hs.items():check('reference-basis-Hamiltonian-transport/'+label,frame.T*H*frame==H)

# Source endpoint-vector canonical split; retain the three internal pairs.
X=S.Matrix([[vertices[prior['registry'][label][1]][axis] for label in labels] for axis in range(3)])
W=(X*X.T).inv()*X;N=S.eye(6)-X.T*W
spatial=S.diag(X,W);internal=S.diag(N,N)
check('endpoint-vector-rank',X.rank()==3 and N.rank()==3)
check('spatial-canonical-pair',spatial*J(6)*spatial.T==J(3))
check('spatial-internal-decoupled-brackets',spatial*J(6)*internal.T==S.zeros(6,12))
check('full-split-reconstruction',S.diag(W.T,X.T)*spatial+internal==S.eye(12))
leak={label:(spatial*A*internal).rank() for label,A in As.items()}
check('spatial-block-alone-not-closed',any(leak.values()))
# Equal new spatial q,p, reference phase and total charge can still have
# unequal same-port responses. This is a state-domain, not 68-path, hostile.
internal_hostile=None
for i,label in enumerate(labels):
    v=N*S.eye(6)[:,i]
    plus=S.zeros(6,1).col_join(v);minus=-plus
    if spatial*As[label]*plus!=S.zeros(6,1):
        check('internal-hostile-same-spatial-state',spatial*plus==spatial*minus)
        check('internal-hostile-same-charge',active_budget(plus[:6,:],plus[6:,:])==active_budget(minus[:6,:],minus[6:,:]))
        check('internal-hostile-different-response',spatial*As[label]*plus!=spatial*As[label]*minus)
        internal_hostile={'port':label,'internal_momentum':list(map(str,v)),
            'positive_spatial_response':list(map(str,spatial*As[label]*plus)),
            'scope':'same c=1 and same charge in the declared state domain; not claimed as two of the 68 fixed forward histories'}
        break
check('internal-hostile-exists',internal_hostile is not None)
for perm in permutations(range(4)):
    vertex_matrix=S.Matrix(4,4,lambda i,j:int(i==perm[j]))
    tetra=S.Matrix.hstack(*(S.Matrix(vertices[v]) for v in 'ABCD'))
    O=tetra*vertex_matrix*tetra.T/4
    tensor_frame=S.kronecker_product(vertex_matrix,vertex_matrix)
    moved_F=tensor_frame*F;moved_f0=tensor_frame*prior['f0'];Hcarrier=prior['ns']['H']
    check('source-metric-and-anchor-frame/'+str(perm),
          S.eye(6)+moved_F.T*Hcarrier*moved_F==K and moved_F.T*Hcarrier*moved_f0==s)
    moved_T=moved_f0.col_join(S.zeros(6,1)).row_join((-moved_F).col_join(S.eye(6)))
    check('full-chart-source-frame/'+str(perm),moved_T==S.diag(tensor_frame,S.eye(6))*T)
    moved_X=S.Matrix.hstack(*(S.Matrix(vertices['ABCD'[perm['ABCD'.index(prior['registry'][label][1])]]]) for label in labels))
    moved_W=(moved_X*moved_X.T).inv()*moved_X
    check('source-spatial-frame/'+str(perm),moved_X==O*X and moved_W==O*W)
    check('internal-projector-frame/'+str(perm),S.eye(6)-moved_X.T*moved_W==N)

files=[Path(__file__),HERE/'check_retained_spatial_response_closure.py']
source_hashes=dict(prior['result']['source_sha256'])
source_hashes.update({str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files})
result={'schema':'marici.nima.relative-anchor-canonical-chart.v1','status':'pass','checks':checks,'check_count':len(checks),
    'source_sha256':source_hashes,'upstream_check_count':prior['result']['check_count'],
    'anchor_schur_coefficient':str(mu),'metric_center':list(map(str,b)),
    'coordinate_law':'g=c/abs(c); u=conjugate(g)*(r-b*c); q=Re(u); p=2*K*Im(u)',
    'charge_law':'Q=mu*abs(c)^2+q^T*K*q+p^T*K^-1*p/4',
    'global_form':'Omega=sum dq_i wedge dp_i + dQ wedge dphi; pi_phi=-Q',
    'action_primitive':'-Im(eta^dagger M d eta)=sum p_i dq_i-Q dphi-d(q^T p)/2',
    'domain':'c!=0; equivalently Q>q^T*K*q+p^T*K^-1*p/4; phi local modulo 2pi, full histories retained',
    'port_Hamiltonian':'h_i=(K*q)_i^2/2+p_i^2/8, exactly the existing pulse generator in the new coordinates',
    'census':census,'spatial_internal_leak_ranks':leak,'internal_hostile':internal_hostile,
    'positive':'one phase-neutral canonical six-pair chart for all ports, with retained reference phase/charge pair and complete source recovery; covariant three-vector pair plus three internal pairs',
    'not_claimed':['physical positions or inertial masses selected','a new autonomous summed Hamiltonian','a new physical clock',
        'closure after discarding internal pairs','extension through a zero anchor','pure-state inversion for a mixed coherence matrix','unique physical quadrature polarization'],
    'verification_scope':'fresh exact source-derived response checker rerun; no new formal proof root or NumPy/137-port comparison',
    'python':sys.executable,'sympy':S.__version__}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} relative-anchor canonical-chart checks; upstream {prior["result"]["check_count"]} checks rerun')
print('Actual source recovery:',census)
print('Global form: dq wedge dp + dQ wedge dphi; reference momentum is -Q')
print('All-port Hamiltonian: (Kq)_i^2/2 + p_i^2/8')
print('Spatial/internal coupling ranks:',leak)
