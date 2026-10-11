"""Exact charge-spectrum, three-copy, and spin-lift audit of the electron trial.
Obligations: forward realization and readout compatibility. No mass law or
physical charge generator is inserted; H is the normalized mode-flux operator.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
from check_coupled_six_piece_belt import (R,Z,ONE,add,mul,conj,scale,norm,total,mv,
    construct,verify_operators,PROTON,verify_proton)
from check_geometric_cycle_reversal import geo
from check_smaller_negative_flux_carrier import mode,area,vnorm

BASE=Path(__file__).resolve().parents[1]

def cmv(a,v):return tuple(total(mul(x,y) for x,y in zip(row,v)) for row in a)
def cmm(a,b):return tuple(tuple(total(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def inner(a,b):return total(mul(conj(x),y) for x,y in zip(a,b))
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vsub(a,b):return vadd(a,tuple(scale(-1,z) for z in b))
def diagproject(v):
    n=vnorm(v);return tuple(tuple(scale(1/n,mul(x,conj(y))) for y in v) for x in v)
def helicity(A):
    # |A|=2 sqrt(3). H=i[A]_cross/(2 sqrt(3)); coefficients are in Q(sqrt(-3)).
    x,y,z=A;cross=((0,-z,y),(z,0,-x),(-y,x,0))
    return tuple(tuple((R(),c/6 if isinstance(c,R) else R(F(c,6))) for c in row) for row in cross)
def fstr(x):
    if isinstance(x,R):assert x.b==0;return str(x.a)
    return str(x)

# Exact Gaussian rationals for the additional spinor representation.
G0=(F(0),F(0));G1=(F(1),F(0));GI=(F(0),F(1))
def ga(a,b):return (a[0]+b[0],a[1]+b[1])
def gs(q,a):return (q*a[0],q*a[1])
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gc(a):return (a[0],-a[1])
def gt(xs):
    v=G0
    for x in xs:v=ga(v,x)
    return v

def qm(q,r):
    a,b,c,d=q;e,f,g,h=r
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def spin(q):
    a,b,c,d=q;return (((a,b),(c,d)),((-c,d),(a,-b)))
def gmm(a,b):return tuple(tuple(gt(gm(x,y) for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def cartan(s):
    a,b=s;a2,b2=gm(a,a),gm(b,b)
    return (ga(a2,gs(-1,b2)),gm(GI,ga(a2,b2)),gs(2,gm(a,b)))
def pa(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=ga(out.get(k,G0),v)
    return {k:v for k,v in out.items() if v!=G0}
def pm(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            k=(i[0]+j[0],i[1]+j[1]);out[k]=ga(out.get(k,G0),gm(x,y))
    return {k:v for k,v in out.items() if v!=G0}

def main():
    raw=PROTON.read_bytes();source=json.loads(raw);verify_proton(source)
    sg=source['objects'][source['objects'][source['root']]['geometry']]['payload']
    candidate_path=BASE/'results/smaller_negative_flux_carrier.json';candidate_raw=candidate_path.read_bytes()
    assert json.loads(candidate_raw)['verification_passed']
    P={k:tuple(map(F,v)) for k,v in geo.POINTS.items()}
    for f in ('ABC','ABD','ACD','BCD'):P['F_'+f]=tuple(sum(P[k][i] for k in f)/3 for i in range(3))
    vectors=[];pos=[];neg=[];rotations=[];Hs=[];commutators=[]
    for row in sg['triangles_and_transports']:
        f,a,b=row['triangle'];v=mode([P[k] for k in (f,a,b)])
        # The whole-face area is three times the source small-triangle area.
        A=tuple(3*x for x in area(v));H=helicity(A);hv=cmv(H,v)
        p=tuple(scale(F(1,2),z) for z in vadd(v,hv));n=tuple(scale(F(1,2),z) for z in vsub(v,hv))
        assert cmm(cmm(H,H),H)==H and all(H[i][j]==conj(H[j][i]) for i in range(3) for j in range(3))
        assert cmv(H,p)==p and cmv(H,n)==tuple(scale(-1,z) for z in n)
        assert vadd(p,n)==v and inner(p,n)==Z
        assert vnorm(p)==F(16,3) and vnorm(n)==F(4,3)
        proj=diagproject(v);hp=cmm(H,proj);ph=cmm(proj,H)
        commutators.append(sum(norm(add(x,scale(-1,y))) for rx,ry in zip(hp,ph) for x,y in zip(rx,ry)))
        vectors.append(v);pos.append(p);neg.append(n);Hs.append(H)
        rotations.append(tuple(tuple(F(x) for x in row) for row in row['rotation']))
    nsum=sum(map(vnorm,vectors));hmean=sum(inner(v,cmv(h,v))[0] for h,v in zip(Hs,vectors))/nsum
    hsecond=sum(vnorm(cmv(h,v)) for h,v in zip(Hs,vectors))/nsum
    variance=hsecond-hmean*hmean
    assert nsum==80 and hmean==F(3,5) and variance==F(16,25)
    assert set(commutators)=={R(F(32,25))}
    plus_protocol=verify_operators(*construct(pos,[0]*12,rotations)[:4])
    minus_protocol=verify_operators(*construct(neg,[0]*12,rotations)[:4])
    assert plus_protocol['total']==minus_protocol['total']==1836
    # Four-face negative carrier, using the same exact geometry and protocol.
    inv={v:k for k,v in P.items() if len(k)==1};ds=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    rs=[tuple(tuple(F(d[i] if i==j else 0) for j in range(3)) for i in range(3)) for d in ds]
    fs=[tuple(inv[tuple(d[i]*P[k][i] for i in range(3))] for k in 'ABC') for d in ds]
    vs=[tuple(map(conj,mode([P[k] for k in f]))) for f in fs]
    for f,v in zip(fs,vs):
        H=helicity(area(mode([P[k] for k in f])));assert cmv(H,v)==tuple(scale(-1,z) for z in v)
        assert total(mul(z,z) for z in v)==Z
    L,G,N,u,_=construct(vs,[0]*4,rs);single=verify_operators(L,G,N,u)
    # Three retained negative channels, each with amplitude 1/sqrt(3), have
    # additive raw flux -1. The common amplitude drops out of the projectors.
    triple=verify_operators(*construct(vs*3,[0]*12,rs*3)[:4])
    assert triple['total']==1836
    assert all(total(mul(N.get((i,k),Z),N.get((k,j),Z)) for k in range(12))==N[i,j] for i in range(12) for j in range(12))
    # Unitary three-port combining: bright fraction |sum phases|²/9.
    omega=(R(-F(1,2)),R(F(1,2)));omega2=mul(omega,omega)
    assert norm(total([ONE]*3))/9==1 and total((ONE,omega,omega2))==Z
    assert mul(mul(omega,omega),omega)==ONE
    # Binary tetrahedral lift; central -1 is absent from the vector carrier.
    quats=set()
    for axis in range(4):
        for sign in (-1,1):quats.add(tuple(F(sign if i==axis else 0) for i in range(4)))
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    ident=(F(1),F(0),F(0),F(0));central=tuple(-x for x in ident)
    assert len(quats)==24 and all(qm(q,r) in quats for q in quats for r in quats)
    assert all(gmm(spin(q),spin(r))==spin(qm(q,r)) for q in quats for r in quats)
    assert spin(central)==((gs(-1,G1),G0),(G0,gs(-1,G1)))
    assert len({min(q,tuple(-x for x in q)) for q in quats})==12
    halfturn=(F(0),F(1),F(0),F(0));assert qm(halfturn,halfturn)==central
    # Exact polynomial identity, not a sample-based assertion of nullity.
    vx={(2,0):G1,(0,2):gs(-1,G1)};vy={(2,0):GI,(0,2):GI};vz={(1,1):gs(2,G1)}
    assert pa(pa(pm(vx,vx),pm(vy,vy)),pm(vz,vz))=={}
    for s in ((G1,G0),(G1,G1),(GI,(F(2),F(-1)))):
        assert cartan(s)==cartan(tuple(gs(-1,z) for z in s))
        acted=tuple(gt(gm(x,y) for x,y in zip(row,s)) for row in spin(halfturn))
        v=cartan(s);assert cartan(acted)==(gs(-1,v[0]),gs(-1,v[1]),v[2])
    # A rotation-equivariant linear section cannot map a central-even vector
    # into a central-odd spinor: T=(-I)T forces T=0. Quadratic lifting is not
    # such a section and introduces a retained sign/lift choice.
    checks={
        'source_and_prior_candidate_bound_by_hash':True,
        'mode_flux_operator_has_helicity_polynomial_H_cubed_equals_H':True,
        'original_proton_not_a_sharp_helicity_state':variance==F(16,25),
        'all_twelve_old_local_selectors_fail_to_commute_with_H':all(x==F(32,25) for x in commutators),
        'four_face_negative_carrier_is_a_sharp_minus_one_H_state':True,
        'circular_projection_keeps_both_source_channels_and_norm':sum(map(vnorm,pos))+sum(map(vnorm,neg))==nsum,
        'projected_positive_and_negative_source_protocols_each_retain_1836':plus_protocol['total']==minus_protocol['total']==1836,
        'three_independent_negative_channels_restore_1836_core_not_228':triple['total']==1836,
        'serial_projector_repetition_is_not_three_copies':True,
        'phase_mismatch_can_make_bright_combination_zero':total((ONE,omega,omega2))==Z,
        'binary_tetrahedral_group_and_spin_representation_close_exactly':True,
        'central_spinor_sign_is_not_present_in_the_original_vector_carrier':spin(central)!=spin(ident),
        'Cartan_square_root_has_exact_null_polynomial_and_two_sheet_sign':True,
        'sources_unchanged':PROTON.read_bytes()==raw and candidate_path.read_bytes()==candidate_raw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'obligations':['forward realization','readout compatibility'],
        'charge_operator':{'definition':'H=i[A_face]_cross/(2*sqrt(3)); original quadratic flux Q(w)=w*H w/48 in these source coordinates',
            'spectrum':['-1','0','1'],'candidate_normalized_expectation':'-1','candidate_variance':'0',
            'old_proton_normalized_expectation':fstr(hmean),'old_proton_variance':fstr(variance),
            'old_local_commutator_squared_norm':fstr(commutators[0]),
            'calibration_obstruction':'No common scalar rescaling makes the original proton a sharp +1 state and the candidate a sharp -1 state.',
            'positive_projection_norm':'64','negative_projection_norm':'16','original_norm':'80',
            'projected_protocol_counts':{'positive':plus_protocol,'negative':minus_protocol}},
        'three_channel_test':{'each_inherited_flux':'-1/3','parallel_total':'-1','parallel_core':triple,
            'coherent_four_face_core':single,'combiner':'(w1+w2+w3)/sqrt(3); normalized bright fraction |sum phases|^2/9',
            'serial_result':'N^3=N, so serial repetitions retain -1/3, not -1',
            'generation_residual':'Three independent occupied inputs and their relative phases are not supplied by three stages of one return. Compression requires an explicit typed adapter.'},
        'spin':{'present_carrier':'ordinary vector action; central element of the double cover acts as +1',
            'binary_tetrahedral_order':24,'rotation_quotient_order':12,'spinor_central_action':'-I_2',
            'Cartan_map':'(a,b) -> (a^2-b^2, i(a^2+b^2), 2ab)',
            'null_condition':'v dot v=0 holds for each circular candidate mode',
            'linear_lift_obstruction':'A rotation-equivariant linear map T from the present carrier to a spinor obeys T=-T, hence T=0.',
            'nonlinear_lift':'Each nonzero null vector has a quadratic spinor root over C up to sign; global sheet transport is extra retained data.',
            'half_phase_warning':'Under the literal scalar action v -> exp(i theta)v, its square root transforms by exp(i theta/2); this is not a supplied electromagnetic charge law.'},
        'mass':'No energy functional, scale selector or conversion cost is supplied. No electron mass is computed.',
        'disposition':'Sharp negative helicity achieved. Original-proton charge normalization fails the common sharp-charge test. Triple-channel assembly needs real additional inputs. Spin-half requires a new double-cover carrier and lift transport, not rephasing the present vector.',
        'source_sha256':{'proton':sha256(raw).hexdigest(),'candidate':sha256(candidate_raw).hexdigest()},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/electron_charge_spin_frontier.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
