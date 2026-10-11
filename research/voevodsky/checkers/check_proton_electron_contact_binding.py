"""Source-embedded, number-preserving singlet/record coupling with a fixed reference.
Exact interface/gate checks and rational bound-state certificates. The 1D and
3D relative lattices are explicitly supplied spatial models, not derived space.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_pentachoron_spin_interfaces import A, S2, S3, S5, CI, ZERO, ONE, I, pauli, add, scale, mm, adj
from check_pentachoron_cycle_transport import eye, act
from check_native_operation_energy_lift import geo, SOURCE, verify

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]


def decode(z):
    coefficients = [F(0)]*16
    for k,v in z.items():
        coefficients[int(k)] = F(v)
    return A(tuple(coefficients))


def decode_matrix(m):
    return tuple(tuple(decode(x) for x in row) for row in m)


def native_coefficient(v):
    a,b,c,d = map(F,v)
    return A(a)+b*S2+CI*S3*(A(c)+d*S2)


def outer(v):
    return tuple(tuple(x*y.flip(8) for y in v) for x in v)


def norm(v):
    return sum((x.flip(8)*x for x in v),ZERO)


def kron(a,b):
    return tuple(tuple(a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def polynomial(x,t,delta,g):
    return x*(x+4*t)*(x+delta)*(x+delta+4*t)-g**4


def isolate_infinite(t,delta,g):
    lo,hi=F(0),g
    assert polynomial(lo,t,delta,g)<0<polynomial(hi,t,delta,g)
    for _ in range(48):
        mid=(lo+hi)/2
        if polynomial(mid,t,delta,g)<0:lo=mid
        else:hi=mid
    assert polynomial(lo,t,delta,g)<0<polynomial(hi,t,delta,g)
    return lo,hi


def finite_green(x,t,radius):
    # Dirichlet interval [-radius,radius], diagonal 2t even at endpoints.
    denominator=2*t+x
    for _ in range(radius-1):
        denominator=2*t+x-t*t/denominator
    return 1/(2*t+x-2*t*t/denominator)


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8'))
    certificate,_=verify(source)
    assert certificate['verified']
    geometry=source['objects'][source['objects'][source['root']]['geometry']]['payload']
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face]=geo.mean([points[k] for k in face])
    placements=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    v=[]
    for row in placements:
        f,a,b=(points[k] for k in row['triangle'])
        v.extend(A(f[j])-A(a[j]+b[j])/2+CI*S3*A(a[j]-b[j])/2 for j in range(3))
    assert len(v)==36 and norm(v)==80
    v=tuple(x/(4*S5) for x in v)
    assert norm(v)==1
    native_path=BASE/'results/native_operation_energy_lift_store.json'
    native=json.loads(native_path.read_text(encoding='utf-8'))
    assert native['source_sha256']['proton']==sha256(SOURCE.read_bytes()).hexdigest()
    p=native['carriers']['proton']
    assert all(F(d)==1 for d in p['metric_denominators'])
    for key,expected in [('entries',(ZERO,)*36),('return_entries',v)]:
        out=[ZERO]*36
        for i,j,z in p[key]:out[i]+=native_coefficient(z)*v[j]
        assert tuple(out)==expected
    # Declared spin extension of the original rank-one proton, not a claim that
    # the original vector carrier was already a spinor.
    proton=tuple(tuple(v[i]*A(s==j) for j in range(2)) for i in range(36) for s in range(2))
    assert mm(adj(proton),proton)==I
    singlet=(ZERO,ONE/S2,-ONE/S2,ZERO)
    singlet_projector=outer(singlet)
    assert norm(singlet)==1 and mm(singlet_projector,singlet_projector)==singlet_projector
    quaternions=set(tuple(F(s if i==k else 0) for i in range(4)) for k in range(4) for s in (-1,1))
    quaternions.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    for q in quaternions:
        u=add(scale(A(q[0]),I),scale(-CI,pauli(tuple(A(x) for x in q[1:]))))
        assert act(kron(u,u),singlet)==singlet
    for phase in (ONE,CI,(A(3)+4*CI)/5):
        assert phase*phase.flip(8)==1
        assert act(kron(scale(phase,I),scale(phase.flip(8),I)),singlet)==singlet
    # Each species has vacuum + logical spin doublet; the effect never converts
    # species or destroys constituents. Opposite charge weights are supplied.
    nine=[ZERO]*9;nine[1*3+2]=ONE/S2;nine[2*3+1]=-ONE/S2
    pair_effect=outer(nine)
    number_p=tuple(tuple(A(i==j and i//3!=0) for j in range(9)) for i in range(9))
    number_e=tuple(tuple(A(i==j and i%3!=0) for j in range(9)) for i in range(9))
    for number in (number_p,number_e,add(number_p,scale(A(-1),number_e))):
        assert mm(number,pair_effect)==mm(pair_effect,number)
    for i in range(9):
        if i//3==0 or i%3==0:assert all(x==0 for x in pair_effect[i])

    cycle_path=BASE/'results/pentachoron_cycle_transport.json'
    cycle=json.loads(cycle_path.read_text(encoding='utf-8'))
    assert cycle['verification_passed']
    for name,digest in cycle['source_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    embedded=[]
    old_spinor_path=BASE/'results/electron_tetrahedral_spinor_store.json'
    old=json.loads(old_spinor_path.read_text(encoding='utf-8'))
    def old_complex(z):
        return A(F(z[0][0]))+S3*F(z[0][1])+CI*(A(F(z[1][0]))+S3*F(z[1][1]))
    for result in cycle['chirality_results']:
        for lift,key in [('displayed','attachment_encoding'),('opposite','opposite_lift_attachment_encoding')]:
            encoding=result['conditional_cycle_defect_extension'][key]
            electron=decode_matrix(encoding['face_isometry'])
            assert len(electron)==40 and mm(adj(electron),electron)==I
            for old_index,d in enumerate((3,2,1,0)):
                location=encoding['face_order'].index([4,d])
                old_projector=tuple(tuple(old_complex(x) for x in row) for row in old['face_projectors'][old_index])
                assert scale(S5,electron[2*location:2*location+2])==scale(ONE/S2,old_projector)
            # Factorized rank-one projector: retain every raw port without
            # allocating a 2880 by 2880 dense matrix.
            raw=tuple((p[0]*e[1]-p[1]*e[0])/S2 for p in proton for e in electron)
            assert len(raw)==2880 and norm(raw)==1
            # Recover the logical pair from the actual raw coefficients.
            partial=tuple(tuple(sum((proton[i][a].flip(8)*raw[40*i+j] for i in range(72)),ZERO)
                                for j in range(40)) for a in range(2))
            recovered=tuple(sum((partial[a][j]*electron[j][b].flip(8) for j in range(40)),ZERO)
                            for a in range(2) for b in range(2))
            assert recovered==singlet
            embedded.append(dict(chirality=result['chirality'],lift=lift,raw_dimension=len(raw),
                nonzero_raw_coefficients=sum(x!=0 for x in raw),norm='1',attachment_projectors_recovered=True))

    # Prior signed-record construction, now controlled by contact AND singlet.
    x=((ZERO,ONE),(ONE,ZERO));i4=eye(4);i8=eye(8)
    for at_contact in (False,True):
        control=singlet_projector if at_contact else scale(ZERO,i4)
        inactive=add(i4,scale(A(-1),control))
        rp=add(kron(inactive,I),kron(control,x))
        rm=add(scale(A(-1),kron(inactive,I)),kron(control,x))
        for r in (rp,rm):assert adj(r)==r and mm(r,r)==i8
        gates=scale(A(F(1,2)),add(add(i8,scale(A(-1),rp)),add(i8,scale(A(-1),rm))))
        assert gates==add(i8,scale(A(-1),kron(control,x)))
        if not at_contact:assert gates==i8

    # Exact controls for the analytic decaying Green kernel used in the proof.
    for hopping in (F(1),F(2,3),F(3,2)):
        for decay in (F(1,2),F(2,3),F(3,4)):
            energy=hopping*(1-decay)**2/decay
            diagonal=1/(hopping*(1/decay-decay))
            assert diagonal**2*energy*(energy+4*hopping)==1
            assert (2*hopping+energy)*decay-hopping*(1+decay**2)==0
            assert (2*hopping+energy-2*hopping*decay)*diagonal==1
    t,delta,g=F(1),F(1),F(1,2)
    lo,hi=isolate_infinite(t,delta,g)
    assert 0<lo<hi<g
    finite=[]
    for radius in (4,8,16,32,64):
        def condition(x):return g*g*finite_green(x,t,radius)*finite_green(x+delta,t,radius)-1
        exists=condition(F(0))>0
        row=dict(radius=radius,negative_level=exists,threshold_test=str(condition(F(0))))
        if exists:
            left,right=F(0),hi
            assert condition(left)>0>condition(right)
            for _ in range(32):
                mid=(left+right)/2
                if condition(mid)>0:left=mid
                else:right=mid
            assert condition(left)>0>condition(right)
            assert right<lo  # finite box binds less strongly than the full line
            row['binding_interval']=[str(left),str(right)]
        finite.append(row)
    # General 3D sufficient nonbinding bound, proved by the Fourier integral
    # in the note: G_3(0) <= sqrt(3)*pi/(8t), G_3(delta)<=1/delta.
    # sqrt(3)<7/4 and pi<22/7 give a rational upper certificate.
    assert F(7,4)**2>3
    bound=g*g*F(7,4)*F(22,7)/(8*t*delta)
    assert bound==F(11,64) and bound<1
    paths=[SOURCE,native_path,cycle_path,old_spinor_path,Path(__file__),
           BASE/'checkers/check_electron_pairing_coupling.py',
           BASE/'checkers/check_finite_record_mediator_constructor.py']
    report=dict(verification_passed=True,proton_spin_extension_explicit=True,
        normalized_pair_effect_rank=1,source_embeddings=embedded,
        common_binary_tetrahedral_rotations_checked=len(quaternions),
        species_numbers_preserved=True,opposite_phase_weights_supplied_not_derived=True,
        retained_signed_gate_identity=True,reference='One fixed mediator, common scalar +g at contact and separation',
        model=dict(t=str(t),delta=str(delta),g=str(g),relative_lattice_admitted_not_derived=True),
        one_dimensional=dict(bound_state_count_below_threshold=1,
            binding_energy_interval=[str(lo),str(hi)],decimal_interval=[float(lo),float(hi)],
            equation='x(x+4t)(x+Delta)(x+Delta+4t)=g^4; x=-E>0',
            finite_dirichlet_controls=finite,triplet_bound_states=0),
        three_dimensional=dict(birman_schwinger_product_upper_bound=str(bound),
            negative_energy_bound_state=False,scope='same onsite contact, t=Delta=1,g=1/2 on Z^3'),
        hydrogen_binding_derived=False,physical_units_calibrated=False,
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in paths})
    output=BASE/'results/proton_electron_contact_binding.json'
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
