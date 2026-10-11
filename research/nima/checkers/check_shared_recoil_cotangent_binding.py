"""One all-port recoil/cotangent embedding, with a strict 3D-body falsifier.

The target is a constrained generalized-body representation of the SAME
pulses. Neither physical particles, mass units, charge nor free flight are
inferred. The strict comparison retains BOTH old local amplitude readings.
"""
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from itertools import permutations, product
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/shared-recoil-cotangent-binding.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(HERE/'check_exchange_recoil_readout.py'))
    canon=runpy.run_path(str(HERE/'check_relative_anchor_canonical_chart.py'))
K=canon['K'];Ki=canon['Ki'];b=canon['b'];mu=canon['mu']
D=K-S.eye(6);Di=D.inv();labels=canon['labels'];F=canon['F']
ref=labels.index('AB');e0=S.eye(6)[:,ref];s=D*e0
checks=[]
def check(name,ok):
    if not ok:raise AssertionError(name)
    checks.append(name)
def expand(A):return A.applyfunc(S.expand)
def scalar(x):return S.simplify(S.expand(x))
def J(n):return S.zeros(n).row_join(S.eye(n)).col_join((-S.eye(n)).row_join(S.zeros(n)))
def reject(name,fn):
    try:fn()
    except ValueError:checks.append(name);return
    raise AssertionError('expected refusal: '+name)

check('source-carrier-contact-Gram',D==F.T*canon['prior']['ns']['H']*F)
check('six-independent-unit-contact-directions',D.rank()==6 and D.is_positive_definite and all(D[i,i]==1 for i in range(6)))
check('metric-derived-matched-center',D*(e0-b)==b and K*b==s)
C=K/2
source_normals=F.col_join(-S.eye(6))/S.sqrt(2)
source_sums=F.col_join(S.eye(6))/S.sqrt(2)
check('actual-source-normal-Gram',source_normals.T*canon['G']*source_normals==C)
check('actual-source-sum-normal-Gram',source_sums.T*canon['G']*source_normals==(D-S.eye(6))/2)
check('all-normals-in-prepared-linear-carrier',canon['T']*S.zeros(1,6).col_join(-S.eye(6)/S.sqrt(2))==source_normals)
check('every-port-overlaps-every-other',all(C[i,j]!=0 for i in range(6) for j in range(6) if i!=j))
# Source sum sigma_i=(a_i+r_i)/sqrt(2) and difference nu_i=(a_i-r_i)/sqrt(2).
# Against another active normal, both have the SAME overlap C_ij.
# In a vector collision star the corresponding pair COM normal zeta_i obeys
# <zeta_i,nu_j>=sqrt(M/m_i)*<nu_i,nu_j>, i!=j. This relation does not depend
# on the dimension or contact direction. Matching the old named sum forces
# m_i=M, not just a choice of a new scalar body view for each port.
M,m,t=S.symbols('M m t',positive=True)
normal_overlap=S.sqrt(m/(M+m))*t
sum_overlap=S.sqrt(M/(M+m))*t
check('vector-star-sum-to-difference-ratio',scalar((sum_overlap/normal_overlap)**2-M/m)==0)
check('literal-sum-reading-forces-equal-mass',S.solve(M/m-1,m)==[M])
# Concrete two-port rival: its reflection Gram matches, but M=1,m0=2,m1=1
# spoils the old port-0 sum reading. Thus a normal-only match is insufficient.
cosine=S.sqrt(3)*C[0,1]
a0=S.Matrix([1,0]);a1=S.Matrix([cosine,S.sqrt(1-cosine**2)])
n0=(S.sqrt(S.Rational(2,3))*a0).col_join(-a0/S.sqrt(3)).col_join(S.zeros(2,1))
n1=(a1/S.sqrt(2)).col_join(S.zeros(2,1)).col_join(-a1/S.sqrt(2))
zeta0=(a0/S.sqrt(3)).col_join(S.sqrt(S.Rational(2,3))*a0).col_join(S.zeros(2,1))
check('normal-only-rival-is-unit',scalar((n0.T*n0)[0])==1 and scalar((n1.T*n1)[0])==1)
check('normal-only-rival-matches-overlap',scalar((n0.T*n1)[0])==C[0,1])
sum_residual=scalar((zeta0.T*n1)[0]-C[0,1])
check('normal-only-rival-fails-old-sum',sum_residual!=0 and sum_residual==scalar(C[0,1]*(1/S.sqrt(2)-1)))
for i,label in enumerate(labels):
    for j,other in enumerate(labels):
        if i==j:continue
        check('source-sum-and-normal-overlap/'+label+'/'+other,((D-S.eye(6))/2)[i,j]==C[i,j])
# Consistent orientation flips cannot change the squared ratio.
for signs in product((-1,1),repeat=2):
    check('orientation-does-not-change-mass-condition/'+str(signs),
          scalar((signs[0]*sum_overlap/(signs[1]*normal_overlap))**2-M/m)==0)
# Equal masses require the central-body contact Gram 2*C-I=D. A 3D body
# cannot carry its six independent directions, even with inactive spectators.
contact_gram=2*C-S.eye(6)
check('strict-three-dimensional-vector-star-rejected',contact_gram.rank()==6 and contact_gram.det()>0)

# Positive shared model: one carrier on V=span(F), metric D, six scalar
# partner coordinates along its unit directions e_i. Transverse partner
# components can be retained as inactive spectators in V-valued bodies.
# P0 is a V-covector; r are partner scalar momenta. X0 and x are positions.
B=S.diag(D,S.eye(6));Bi=S.diag(Di,S.eye(6))
Bp=(-D).col_join(S.eye(6));Br=b.col_join(b)
Bx=S.eye(6).col_join(-S.eye(6))*Ki
Cp=Br.row_join(Bp).row_join(S.zeros(12,6))
Cx=S.zeros(12,7).row_join(Bx)
embedding=Cx.col_join(Cp)  # columns R,q,p; rows body X,body P
check('one-cotangent-embedding',expand(embedding.T*J(12)*embedding)==S.diag(0,J(6)))
check('full-source-budget',expand(Cp.T*Bi*Cp+Cx.T*B*Cx/4)==S.diag(mu,K,Ki/4))
check('faithful-real-state-embedding',embedding.rank()==13)
# Full form includes the retained reference phase/charge pair.
full_jac=S.zeros(24,14)
full_jac[:,0]=embedding[:,0]
full_jac[:,2:]=embedding[:,1:]
ref_form=canon['dcharge']*canon['ephi'].T-canon['ephi']*canon['dcharge'].T
check('global-reference-form-retained',expand(full_jac.T*J(12)*full_jac+ref_form-canon['Omega'])==S.zeros(14))
vars13=S.Matrix([canon['R'],*canon['q'],*canon['p']])
body_theta=(Cp*vars13).T*full_jac[:12,:]-canon['charge']*canon['ephi'].T
check('action-endpoint-term-retained',expand(-canon['beta']-body_theta-canon['boundary'])==S.zeros(1,14))

body_generators={};body_reflections={};body_H={}
active_embedding=embedding[:,1:]
source_budget=S.diag(B/4,Bi)
for i,label in enumerate(labels):
    ei=S.eye(6)[:,i]
    lp=(-ei.T).row_join(ei.T)
    lx=lp*B
    H=S.diag(lx.T*lx/8,lp.T*lp/2)
    A=2*J(12)*H
    body_generators[label]=A;body_H[label]=H
    check('same-whole-Hamiltonian/'+label,expand(embedding.T*H*embedding)==S.diag(0,canon['Hs'][label]))
    check('same-continuous-pulse/'+label,A*active_embedding==active_embedding*canon['As'][label])
    check('matched-reference-fixed/'+label,A*embedding[:,0]==S.zeros(24,1))
    check('body-generator-symplectic/'+label,A.T*J(12)+J(12)*A==S.zeros(24))
    check('body-budget-preserved/'+label,A.T*source_budget+source_budget*A==S.zeros(24))
    check('same-pulse-polynomial/'+label,A**3==-A)
    Ep=S.eye(12)-B*lp.T*lp
    Ex=Ep.T
    body_reflections[label]=Ep
    check('common-cotangent-endpoint/'+label,S.eye(24)+2*A*A==S.diag(Ex,Ep))
    check('common-kinetic-pairing/'+label,Ep.T*Bi*Ep==Bi)
    # Exact old local pair readings: a_i=e_i^T P0, r_i=partner momentum.
    pair=ei.T.row_join(S.zeros(1,6)).col_join(S.zeros(1,6).row_join(ei.T))
    check('old-local-pair-swapped/'+label,pair*Ep==S.Matrix([[0,1],[1,0]])*pair)
    total=S.eye(6).row_join(D)
    check('whole-generalized-momentum-conserved/'+label,total*Ep==total)
    check('contact-gap-fixed-position-section/'+label,(Ex-S.eye(12))==-lp.T*lx)
    # Keeping positions fixed OUTSIDE contact is not the same symplectic map.
    fixed_position=S.diag(S.eye(12),Ep)
    check('arbitrary-fixed-position-kick-refused/'+label,fixed_position.T*J(12)*fixed_position!=J(12))
    # A common positive mass scale is free: reciprocal canonical rescaling.
    scale=S.diag(S.eye(12)/S.sqrt(m),S.sqrt(m)*S.eye(12))
    Hm=S.diag(m*H[:12,:12],H[12:,12:]/m)
    check('mass-scale-not-selected/'+label,expand(scale.T*Hm*scale-H)==S.zeros(24))
check('common-mass-rescaling-canonical',scale.T*J(12)*scale==J(12))
# No added full kinetic drift: h_i contains only the selected relative mode.
check('not-the-full-free-body-Hamiltonian',all(H[12:,12:].rank()==1 for H in body_H.values()) and Bi.rank()==12)

@dataclass(frozen=True)
class BodyPacket:
    position: object
    momentum: object
    phase: object
    charge: object
    record: object

def to_body(packet):
    eta,_=canon['from_chart'](packet)
    radius=S.sqrt(scalar(eta[0]*S.conjugate(eta[0])))
    position=expand(Bx*packet.p)
    momentum=expand(Br*radius+Bp*packet.q)
    return BodyPacket(S.ImmutableMatrix(position),S.ImmutableMatrix(momentum),packet.phase,packet.charge,packet.record)

def from_body(packet):
    X=S.Matrix(packet.position);P=S.Matrix(packet.momentum)
    if X.shape!=(12,1) or P.shape!=(12,1) or any(S.im(x)!=0 for x in list(X)+list(P)):
        raise ValueError('real constrained body coordinates required')
    if expand(X[:6,:]+X[6:,:])!=S.zeros(6,1):raise ValueError('outside retained position section')
    total=expand(P[:6,:]+D*P[6:,:]);radius=total[ref]
    if radius.is_positive is not True or expand(total-s*radius)!=S.zeros(6,1):
        raise ValueError('outside nonzero prepared anchor line')
    budget=scalar((P.T*Bi*P)[0]+(X.T*B*X)[0]/4)
    if budget!=packet.charge:raise ValueError('phase quantity does not match body budget')
    q=expand(P[6:,:]-b*radius);p=expand(K*X[:6,:])
    restored=canon['Chart'](packet.phase,packet.charge,S.ImmutableMatrix(q),S.ImmutableMatrix(p),packet.record)
    canon['from_chart'](restored)  # retains phase/domain validation
    return restored

census={'retained_paths':0,'state_samples':0,'nonzero_endpoint_impulses':0,
        'zero_endpoint_positions':0,'nonzero_endpoint_momenta':0,
        'nonzero_midpoint_positions':0}
first_impulse=None
spatial_reader_hostile=None
for packet in canon['packets']:
    family,slot,sample=packet.record
    word=tuple(edge[2] for edge in family.paths[slot]);label=word[-1];i=labels.index(label)
    body=to_body(packet);restored=from_body(body)
    z=canon['prior']['states_at']([word],sample)[:,0]
    eta,_=canon['from_chart'](restored)
    name=str(census['state_samples']);census['state_samples']+=1
    check('actual-full-state-recovery/'+name,expand(canon['T']*eta-z)==S.zeros(22,1))
    check('original-record-identity/'+name,restored.record is packet.record)
    # Complex local amplitudes, not just the real endpoint values, recover.
    Yhat=expand(Di*body.momentum[:6,:]-S.I*body.position[:6,:]/2)
    rhat=expand(body.momentum[6:,:]-S.I*body.position[6:,:]/2)
    check('all-local-complex-readings/'+name,expand(F*Yhat*body.phase-z[:16,:])==S.zeros(16,1) and expand(rhat*body.phase-z[16:,:])==S.zeros(6,1))
    check('body-phase-quantity/'+name,scalar((body.momentum.T*Bi*body.momentum)[0]+(body.position.T*B*body.position)[0]/4)==1)
    check('actual-generalized-total-momentum/'+name,expand(body.momentum[:6,:]+D*body.momentum[6:,:])==s)
    initial_z=canon['prior']['endpoint_state'](word[:-1])
    initial_eta=S.Matrix([1]+list(initial_z[16:,:]))
    start=to_body(canon['to_chart'](initial_eta,packet.record))
    A=body_generators[label]
    flow=S.eye(24)+A+A*A if sample==1 else S.eye(24)+2*A*A
    check('actual-body-pulse/'+name,expand(flow*start.position.col_join(start.momentum)-body.position.col_join(body.momentum))==S.zeros(24,1))
    if sample==1:
        if body.position!=S.zeros(12,1):census['nonzero_midpoint_positions']+=1
    else:
        census['retained_paths']+=1
        if body.position==S.zeros(12,1):census['zero_endpoint_positions']+=1
        if body.momentum!=S.zeros(12,1):census['nonzero_endpoint_momenta']+=1
        old_spatial=expand(canon['X']*packet.q)
        new_configuration=expand(canon['X']*body.position[:6,:])
        if spatial_reader_hostile is None and old_spatial!=new_configuration:
            spatial_reader_hostile={'word':list(word),'old_endpoint_vector':list(map(str,old_spatial)),
                'new_carrier_configuration':list(map(str,new_configuration)),
                'scope':'actual endpoint; transport preserves the old reading but does not identify it with the new configuration'}
        change=expand(body.momentum-start.momentum)
        impulse=scalar(start.momentum[6+i]-start.momentum[i])
        ei=S.eye(6)[:,i]
        check('actual-balanced-pair-impulse/'+name,change==(D*ei).col_join(-ei)*impulse)
        check('actual-endpoint-kinetic-energy/'+name,scalar((body.momentum.T*Bi*body.momentum)[0]/2)==S.Rational(1,2))
        if impulse!=0:
            census['nonzero_endpoint_impulses']+=1
            if first_impulse is None:first_impulse={'word':list(word),'port':label,'scalar_impulse':str(impulse),
                'carrier_covector_impulse':list(map(str,change[:6,:])),
                'partner_scalar_impulse':str(change[6+i])}
check('same-source-path-census',census['retained_paths']==68 and census['state_samples']==136)
check('actual-endpoint-recoil-nonzero',census['nonzero_endpoint_impulses']==62)
check('real-endpoints-are-contact-section',census['zero_endpoint_positions']==68)
check('endpoint-momentum-not-erased',census['nonzero_endpoint_momenta']==68)
check('intermediate-positions-retained',census['nonzero_midpoint_positions']==62)
check('old-spatial-reader-not-new-configuration',spatial_reader_hostile is not None)

# Explicit domain/metadata hostiles, not silent projection into this image.
fixture=to_body(canon['packets'][0])
bad_X=S.Matrix(fixture.position);bad_X[0]+=1
reject('foreign-position-section-refused',lambda:from_body(replace(fixture,position=bad_X)))
bad_P=S.Matrix(fixture.momentum);bad_P[1]+=1
reject('foreign-anchor-line-refused',lambda:from_body(replace(fixture,momentum=bad_P)))
reject('wrong-budget-refused',lambda:from_body(replace(fixture,charge=fixture.charge+1)))
reject('nonunit-reference-refused',lambda:from_body(replace(fixture,phase=2)))
reject('zero-anchor-refused',lambda:from_body(BodyPacket(S.zeros(12,1),S.zeros(12,1),1,0,None)))
for g in [S.I,(3+4*S.I)/5]:
    eta,_=canon['from_chart'](canon['packets'][0])
    moved=to_body(canon['to_chart'](g*eta,fixture.record))
    check('common-phase-neutral-body/'+str(g),moved.position==fixture.position and moved.momentum==fixture.momentum and scalar(moved.phase-g*fixture.phase)==0)

# Source endpoint-vector/internal split of the GENERALIZED carrier V.
# This uses D, not the different earlier record-coordinate metric K.
X=canon['X'];spatial_metric=(X*Di*X.T).inv()
lift=Di*X.T*spatial_metric;internal=S.eye(6)-lift*X
check('source-vector-plus-internal-split',X.rank()==3 and internal.rank()==3 and X*lift==S.eye(3))
check('metric-orthogonal-internal-sector',internal.T*D*lift==S.zeros(6,3))
check('whole-kinetic-split-retained',D==X.T*spatial_metric*X+internal.T*D*internal)
check('vector-cotangent-pair',X*lift==S.eye(3))
check('all-ports-have-internal-component',all(internal*S.eye(6)[:,i]!=S.zeros(6,1) for i in range(6)))
check('internal-deletion-loses-contact-Gram',(D-X.T*spatial_metric*X).rank()==3)
# The old x=X*q remains a momentum-affine reading in the new representation.
check('old-spatial-reading-transported',X*Cp[6:,:]-X*b*S.eye(13)[0,:]==S.zeros(3,1).row_join(X).row_join(S.zeros(3,6)))
for perm in permutations(range(4)):
    V=canon['tetra'];perm_matrix=S.Matrix(4,4,lambda i,j:int(i==perm[j]))
    O=V*perm_matrix*V.T/4
    moved_X=O*X;moved_metric=(moved_X*Di*moved_X.T).inv()
    check('spatial-metric-source-frame/'+str(perm),moved_metric==O*spatial_metric*O.T)
    check('internal-source-frame/'+str(perm),S.eye(6)-Di*moved_X.T*moved_metric*moved_X==internal)

hashes=dict(canon['result']['source_sha256'])
for f in [Path(__file__),HERE/'check_exchange_recoil_readout.py']:
    hashes[str(f.relative_to(ROOT))]=hashlib.sha256(f.read_bytes()).hexdigest()
result={'schema':'marici.nima.shared-recoil-cotangent-binding.v1','status':'pass',
    'checks':checks,'check_count':len(checks),'source_sha256':hashes,
    'upstream_checks':{'single_port_recoil':len(old['checks']),'relative_anchor':canon['result']['check_count'],
                       'spatial_response':canon['result']['upstream_check_count']},
    'strict_vector_star':{'dimension_requested':3,'minimum_contact_dimension':6,
        'mass_condition':'all partner masses equal the common carrier mass when BOTH old local readings are preserved',
        'contact_Gram':[[str(x) for x in D.row(i)] for i in range(6)],'determinant':str(D.det()),
        'scope':'one vector carrier/six partners, one kinetic isometry, fixed contact directions, old mixed local sum AND difference readings; not a normal-Gram-only or universal mechanics classification'},
    'normal_only_hostile_sum_residual':str(sum_residual),
    'positive_embedding':{'momentum':'P0=b*R-D*q; partner momenta=b*R+q',
        'position':'X0=K^-1*p; partner positions=-K^-1*p',
        'Hamiltonian':'h_i=(r_i-P0_i)^2/2+(x_i-(D*X0)_i)^2/8',
        'conserved_momentum':'P0+D*r=s*R',
        'scope':'constrained cotangent embedding, not twelve independent source pairs or newly added oscillators'},
    'census':census,'first_nonzero_impulse':first_impulse,'spatial_reader_hostile':spatial_reader_hostile,
    'spatial_metric':[[str(x) for x in spatial_metric.row(i)] for i in range(3)],
    'spatial_internal_contact_defect_rank':3,
    'not_claimed':['source labels are physical particles','physical mass scale selected','electric charge coupling',
        'new free flight or full kinetic drift','old endpoint-vector reading became a new configuration reading',
        'no three-dimensional mechanics with any other body architecture or nonlinear readout'],
    'verification_scope':'fresh exact 22/882/455-check upstream chain plus symbolic whole-map and actual source-path controls; no formal proof root or NumPy/137-port comparison',
    'python':sys.executable,'sympy':S.__version__}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} shared recoil/cotangent checks')
print('Strict old-reading-preserving vector star: equal masses and contact rank 6, not 3')
print('One generalized carrier/partner map preserves all six Hamiltonian pulses')
print('Source census:',census)
print('Internal contact-Gram defect rank: 3')
