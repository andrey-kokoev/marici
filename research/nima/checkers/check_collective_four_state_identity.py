"""Twelve four-state elements: explicit common-mode gathering and shared-unit control.

Primitive arrows are endpoint pairs. No context/history tags multiply counts.
The explicit gather/scatter graph and the algebraic identification of local units
are different implementations and are reported separately.
"""
from fractions import Fraction as F
from pathlib import Path
import cmath
import math
import json


def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def transpose(a): return tuple(zip(*a))
def mm(a,b): return tuple(tuple(sum((x*y for x,y in zip(r,c)),F(0)) for c in transpose(b)) for r in a)
def mv(a,v): return tuple(sum((x*y for x,y in zip(r,v)),F(0)) for r in a)
def sub(a,b): return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))
def rank(a):
    a=[list(map(F,r)) for r in a];k=0
    for j in range(len(a[0])):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k];pivot=a[k][j]
        a[k]=[x/pivot for x in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][j]:
                c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k


def main():
    # Four diagonal state coefficients split as one common unit plus three contrasts.
    Q4=tuple(tuple(F(1,4) for _ in range(4)) for _ in range(4))
    H4=sub(eye(4),Q4)
    assert mm(Q4,Q4)==Q4 and mm(H4,H4)==H4
    assert rank(Q4)==1 and rank(H4)==3
    contrasts=tuple(tuple(F(i==a)-F(i==3) for i in range(4)) for a in range(3))
    assert rank(contrasts)==3
    assert all(mv(Q4,h)==(0,)*4 and mv(H4,h)==h for h in contrasts)
    assert mv(Q4,(1,)*4)==(1,)*4
    # Explicit gathering to Omega, then scattering back to the twelve local unit ports.
    gather=(tuple(F(1,12) for _ in range(12)),)
    scatter=tuple((F(1),) for _ in range(12))
    P=mm(scatter,gather);relative=sub(eye(12),P)
    assert mm(P,P)==P and rank(P)==1 and rank(relative)==11
    assert mm(gather,scatter)==((F(1),),)
    assert mv(gather,(1,)*12)==(F(1),)
    assert mv(P,(1,)*12)==(1,)*12
    assert mv(P,(1,-1)*6)==(0,)*12
    phase_spread=tuple(cmath.exp(2j*math.pi*c/12) for c in range(12))
    cancellation=abs(sum(phase_spread)/12)
    assert cancellation<1e-12
    common_phase=cmath.exp(1j*math.pi/3)
    assert max(abs(a-common_phase) for a in mv(P,(common_phase,)*12))<1e-12
    # A phase-scaled operator is not itself an algebraic identity except at phase 1.
    assert abs(common_phase**2-common_phase)>0.5
    # Retaining Pz and (I-P)z is lossless; Pz alone removes relative components.
    probe=tuple(F(c*c-3*c,7) for c in range(12))
    assert tuple(a+b for a,b in zip(mv(P,probe),mv(relative,probe)))==probe
    omega=('common','I')
    gather_arrows={((c,'I'),omega) for c in range(12)}
    scatter_arrows={(omega,(c,'I')) for c in range(12)}
    active={((c,s,a),((c+1)%12,s,b)) for c in range(12)
            for s,n in (('R',12),('H',3)) for a in range(n) for b in range(n)}
    explicit=active|gather_arrows|scatter_arrows
    assert len(active)==1836 and len(gather_arrows|scatter_arrows)==24
    assert len(explicit)==1860
    assert len({x for arrow in explicit for x in arrow})==193
    # Simultaneous two-way hub transport. Its square fixes the coherent mode
    # and the hub but projects away independent relative local-unit inputs.
    W=tuple(tuple(F(1) if i<12 and j==12 else
                  F(1,12) if i==12 and j<12 else F(0)
                  for j in range(13)) for i in range(13))
    W2=mm(W,W)
    assert rank(W2)==2 and mm(W2,W2)==W2
    W12=eye(13)
    for _ in range(12): W12=mm(W,W12)
    assert W12==W2 and W12!=eye(13)
    aligned=(F(1),)*12+(F(0),)
    assert mv(W12,aligned)==aligned
    # If local units are embeddings of the SAME tensor-product identity, their
    # eleven differences are presentation redundancies, not physical modes.
    # One-body operator space: span{I_global, traceless local matrices at each site}.
    constraints=[]
    for c in range(11):
        r=[F(0)]*192
        for a in range(4):
            r[16*c+5*a]=1;r[16*11+5*a]=-1
        constraints.append(r)
    assert rank(constraints)==11
    one_body_dimension=192-rank(constraints)
    assert one_body_dimension==181==1+12*(12+3)
    report={'status':'passed','local_states':['A','B','C','D'],
            'local_operator_split':{'unit':1,'diagonal_contrasts':3,'off_diagonal_relations':12},
            'collective_projector':{'formula':'P=ones(12,12)/12','rank':rank(P),'idempotent':True,
                                    'relative_complement_rank':rank(relative)},
            'phase_tests':{'aligned_inputs_produce_unit':True,'alternating_sign_inputs_cancel':True,
                           'uniform_phase_spread_mean_magnitude':cancellation,
                           'global_phase_preserves_projector_line_but_not_unit_operator':True},
            'explicit_gather_scatter':{'active_arrows':1836,'gather_arrows':12,'scatter_arrows':12,
                                      'total_unique_arrows':1860,'port_nodes':193,
                                      'projector_matrix_nonzeros':144,
                                      'hub_square_rank':rank(W2),
                                      'hub_twelve_step_return':'identity on coherent/hub subspace; projects out eleven relative modes',
                                      'note':'The 24-step-arrow factorization and the 144 matrix entries of its composite are different arrow alphabets.'},
            'shared_algebraic_unit':{'raw_local_matrix_coordinates':192,'unit_identification_relations':11,
                                     'one_body_dimension':one_body_dimension,'active_transport_arrows':1836,
                                     'global_unit_self_loop_if_counted':1,
                                     'note':'Shared-unit identification uses no gather transport. It must not be substituted for the explicit 24-arrow implementation without saying so.'},
            'outcome':'One collective identity is verified. Explicit gather/return adds 24 arrows. A shared algebraic unit instead gives 181 independent one-body coordinates; twelve independent local unit amplitudes still have eleven relative modes.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'collective-four-state-identity.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: four-state split; collective rank-one identity; phase controls; 24 explicit gather/return arrows; 1860 total. Shared-unit alternative has 181 coordinates.')

if __name__=='__main__': main()
