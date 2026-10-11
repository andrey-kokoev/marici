"""A declared spinor extension of the four-face negative-circulation carrier.
Exact tetrahedral tight-frame encoding; this changes the carrier and readout,
not merely the phase convention of the old vector model.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_electron_charge_spin_frontier import ga,gs,gm,gc,gt,gmm,spin,qm,G0,G1,GI,cartan

BASE=Path(__file__).resolve().parents[1]
@dataclass(frozen=True,eq=False)
class D:
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    def __add__(self,x):
        x=cast(x);return D(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return D(-self.a,-self.b)
    def __sub__(self,x):return self+-cast(x)
    def __rsub__(self,x):return cast(x)+-self
    def __mul__(self,x):
        x=cast(x);return D(self.a*x.a+3*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=cast(x);den=x.a*x.a-3*x.b*x.b
        if not den:raise ZeroDivisionError()
        return self*D(x.a/den,-x.b/den)
    def __eq__(self,x):
        if isinstance(x,(int,F,D)):x=cast(x);return self.a==x.a and self.b==x.b
        return False
    def __hash__(self):return hash(self.a) if not self.b else hash((self.a,self.b))
def cast(x):return x if isinstance(x,D) else D(x)
def pos(x):
    x=cast(x)
    if x.a>=0 and x.b>=0:return x!=0
    if x.a<=0 and x.b<=0:return False
    return x.a*x.a>3*x.b*x.b if x.a>0 else 3*x.b*x.b>x.a*x.a

def ident(n):return tuple(tuple(G1 if i==j else G0 for j in range(n)) for i in range(n))
def adj(a):return tuple(tuple(gc(x) for x in row) for row in zip(*a))
def sm(q,a):return tuple(tuple(gs(q,x) for x in row) for row in a)
def ma(a,b):return tuple(tuple(ga(x,y) for x,y in zip(rx,ry)) for rx,ry in zip(a,b))
def act(a,v):return tuple(gt(gm(x,y) for x,y in zip(row,v)) for row in a)
def trace(a):return gt(a[i][i] for i in range(len(a)))
def norm(v):return gt(gm(gc(x),x) for x in v)[0]
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def encode(z):return [[str(cast(x).a),str(cast(x).b)] for x in z]

def main():
    prior=BASE/'results/electron_charge_spin_frontier.json';raw=prior.read_bytes();assert json.loads(raw)['verification_passed']
    normals=[tuple(D(0,F(s,3)) for s in n) for n in [(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1)]]
    I=ident(2);sigma=[];P=[]
    for x,y,z in normals:
        h=(((z,D()),(x,-y)),((x,y),(-z,D())))
        p=sm(F(1,2),ma(I,sm(-1,h)));sigma.append(h);P.append(p)
        assert gmm(p,p)==p and adj(p)==p and trace(p)==G1 and gmm(h,p)==sm(-1,p)
    psum=tuple(tuple(gt(p[i][j] for p in P) for j in range(2)) for i in range(2))
    assert psum==sm(2,I)
    # J_i=P_i/sqrt(2), so J*J=I_2. Build JJ* without square roots.
    L=tuple(tuple(P[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(8)) for i in range(8))
    N=tuple(tuple(gs(F(1,2),gmm(P[i//2],P[j//2])[i%2][j%2]) for j in range(8)) for i in range(8))
    H=tuple(tuple(sigma[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(8)) for i in range(8))
    G=N
    assert gmm(N,N)==N and trace(N)==(F(2),F(0)) and adj(N)==N
    assert gmm(L,N)==gmm(N,L)==N and gmm(N,gmm(G,L))==N
    assert gmm(H,N)==gmm(N,H)==sm(-1,N)
    matrices={'L':L,'G':G,'N':N};supports={s:{(i,j):m[i][j] for i in range(8) for j in range(8) if m[i][j]!=G0} for s,m in matrices.items()}
    cycle_sum=G0;used={s:set() for s in supports};cycles=0
    for (i,k),g in supports['G'].items():
        for j in range(8):
            if (k,j) not in supports['L'] or (j,i) not in supports['N']:continue
            w=gm(N[j][i],gm(g,L[k][j]));assert w[1]==0 and pos(w[0])
            cycle_sum=ga(cycle_sum,w);cycles+=1
            used['G'].add((i,k));used['L'].add((k,j));used['N'].add((j,i))
    assert cycle_sum==(F(2),F(0)) and all(used[s]==set(supports[s]) for s in supports)
    assert [len(supports[s]) for s in ('L','G','N')]==[16,64,64]
    # Explicit source enlargement: binary tetrahedral spin matrices.
    quats=set()
    for k in range(4):
        for s in (-1,1):quats.add(tuple(F(s if i==k else 0) for i in range(4)))
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    perms={};actions={}
    for q in quats:
        U=spin(q);permutation=[]
        for h in sigma:
            image=gmm(gmm(U,h),adj(U));permutation.append(sigma.index(image))
        assert sorted(permutation)==list(range(4));perms[q]=permutation
        T=tuple(tuple(U[i%2][j%2] if i//2==permutation[j//2] else G0 for j in range(8)) for i in range(8))
        actions[q]=T
        assert gmm(T,N)==gmm(N,T) and gmm(adj(T),T)==ident(8)
        logical=sm(F(1,2),tuple(tuple(gt(gmm(gmm(P[permutation[k]],U),P[k])[i][j] for k in range(4)) for j in range(2)) for i in range(2)))
        assert logical==U
    for q in quats:
        for r in quats:assert perms[qm(q,r)]==[perms[q][perms[r][i]] for i in range(4)]
    minus_one=(-F(1),F(0),F(0),F(0));assert actions[minus_one]==sm(-1,ident(8))
    qi=(F(0),F(1),F(0),F(0));qj=(F(0),F(0),F(1),F(0))
    assert qm(qm(qm(qi,qj),tuple(-x for x in qi)),tuple(-x for x in qj))==minus_one
    # The central element is a commutator: no 1D character can carry its -1.
    # Thus rank two, not a single coherent line, is the necessary spinorial change.
    # Cartan map in Pauli-compatible coordinates: flip its third component.
    # Check actual face spinors and the tetrahedral second-moment identity.
    assert all(sum(n[a]*n[b] for n in normals)==(F(4,3) if a==b else 0) for a in range(3) for b in range(3))
    samples=((G1,G0),(G0,G1),((F(3,5),F(0)),(F(0),F(4,5))))
    for z in samples:
        assert norm(z)==1;power2=D()
        for n,p in zip(normals,P):
            psi=act(p,z);vv=cartan(psi);v=(vv[0],vv[1],gs(-1,vv[2]))
            A=cross(tuple(x[0] for x in v),tuple(x[1] for x in v));power=norm(psi)
            assert A==tuple(-power*power*x for x in n)
            power2+=power*power/4 # the actual J_i includes 1/sqrt(2)
        assert power2==F(1,3)
    # Underdetermination controls: the same encoded spinor permits multiple
    # U(1) charge characters and gapped scalar energies. Algebraically these
    # commute for every scalar, since all rotations commute with N.
    complement=ma(ident(8),sm(-1,N))
    for charge in (-2,-1,0,1,2):
        Q=sm(charge,N)
        assert gmm(Q,N)==sm(charge,N)
        assert all(gmm(T,Q)==gmm(Q,T) for T in actions.values())
    for mass in (F(1,100),F(1),F(1836)):
        energy=ma(sm(mass,ident(8)),sm(1,complement))
        assert gmm(energy,N)==sm(mass,N)
        assert gmm(energy,complement)==sm(mass+1,complement)
    # Exchange is not selected by the rotation representation alone.
    swap=tuple(tuple(G1 if (i//2,i%2)==(j%2,j//2) else G0 for j in range(4)) for i in range(4))
    assert gmm(swap,swap)==ident(4)
    assert trace(sm(F(1,2),ma(ident(4),swap)))==(F(3),F(0))
    assert trace(sm(F(1,2),ma(ident(4),sm(-1,swap))))==G1
    for q in quats:
        U=spin(q);tensor=tuple(tuple(gm(U[i//2][j//2],U[i%2][j%2]) for j in range(4)) for i in range(4))
        assert gmm(tensor,swap)==gmm(swap,tensor)
    checks={
        'four_face_Pauli_projectors_have_rank_one_and_negative_polarization':True,
        'tetrahedral_tight_frame_sum_P_equals_two_I':True,
        'collective_projector_rank_two_and_idempotent':True,
        'negative_polarization_sharp_on_entire_logical_doublet':gmm(H,N)==sm(-1,N),
        'explicit_three_stage_protocol_support_144':sum(map(len,supports.values()))==144,
        'all_144_arrows_in_positive_closed_cycles':all(used[s]==set(supports[s]) for s in supports),
        'all_24_binary_rotations_preserve_coherent_subspace':True,
        'induced_logical_action_equals_fundamental_spinor_representation':True,
        'two_pi_central_rotation_is_minus_identity':True,
        'one_dimensional_spinorial_return_obstructed_by_central_commutator':True,
        'Cartan_image_has_actual_negative_face_circulation':True,
        'tetrahedral_second_moment_makes_Cartan_flux_spin_independent':True,
        'multiple_integer_charge_characters_preserve_identical_spinor_return':True,
        'arbitrary_scalar_ground_energy_preserves_identical_spinor_return':True,
        'symmetric_and_antisymmetric_exchange_sectors_both_rotation_invariant':True,
        'prior_artifact_unchanged':prior.read_bytes()==raw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'construction':'New spinor carrier, not a re-expression of the original vector coefficients.',
        'definitions':{'face_projector':'P_i=(I-n_i.sigma)/2','encoding':'J z=(P_0 z,...,P_3 z)/sqrt(2)',
            'collective_return':'N_ij=P_i P_j/2','protocol':'L=diag(P_i), G=N, return stage N; NGL=N',
            'polarization_observable':'H=diag(n_i.sigma); HJ=-J'},
        'logical_dimension':2,'raw_complex_coordinates':8,'support':{s:len(v) for s,v in supports.items()},
        'total_transfers':sum(map(len,supports.values())),'positive_three_step_cycles':cycles,'cycle_trace_sum':'2',
        'spin':'Fundamental binary tetrahedral doublet; central 2pi lift acts as -I. Covariance extends over rotated normals via U(n.sigma)U*=Rn.sigma.',
        'readout_boundary':{'spinor_polarization':'-1 on every unit logical state',
            'old_vector_flux_of_literal_Cartan_image':'-1/(24*sqrt(3)) at unit logical norm in the fixed original tetrahedral coordinates',
            'reason':'Cartan is quadratic in the spinor, so the old vector quadratic flux becomes quartic. Sum_i ||J_i z||^4=1/3.',
            'not_equated':'The new Pauli polarization is not silently identified with electromagnetic charge or the old amplitude-calibrated flux.'},
        'underdetermination':{'charge':'Q_q=qN; every integer q defines a periodic U(1) action on the doublet and commutes with the retained rotations.',
            'energy':'E_m=mI+(I-N) has the same rank-two ground sector with energy m and gap 1, for any scalar m; no particular m is selected.',
            'exchange':'Both swap and minus swap commute with U tensor U. Symmetric rank 3 and antisymmetric rank 1 sectors both survive; no statistics selector is supplied.'},
        'not_generated':['The old vector protocol does not generate the two-component spinor carrier or its double-cover transport.',
            'No physical U(1) coupling, fermionic exchange rule, energy functional or electron mass is derived.'],
        'resource_boundary':'144 is the support of this explicitly supplied protocol, not a minimal count and not an electron mass. Relative to 1836 the count ratio is 51/4.',
        'source_sha256':sha256(raw).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'field':'Q(sqrt(3),i); complex coefficients [[real_rational,real_sqrt3],[imag_rational,imag_sqrt3]]',
        'normals':[[[str(x.a),str(x.b)] for x in n] for n in normals],
        'face_projectors':[[[encode(x) for x in row] for row in p] for p in P],
        'arrows':[{'stage':s,'target':i,'source':j,'weight':encode(v)} for s,entries in supports.items() for (i,j),v in sorted(entries.items())]}
    (BASE/'results/electron_tetrahedral_spinor.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/electron_tetrahedral_spinor_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
