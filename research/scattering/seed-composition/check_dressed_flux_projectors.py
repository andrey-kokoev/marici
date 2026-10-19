"""Exact dressed projectors over the quadratic extension and retained flux covariance."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_charged_spinor_closure import audit as closure_audit
from check_native_endpoint_face_lines import audit as face_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,ROOT,BASE
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import qm,spin
from check_diagonal_spin_networks import CI

DEST=BASE/'results/dressed-flux-projectors.v1.json'


# a+b*r, r^2-v*r-1=0; r is the positive real branch. No numerical roots.
class Field:
    def __init__(self,v):self.v=A(v);self.zero=(ZERO,ZERO);self.one=(ONE,ZERO)
    def cast(self,x):return x if isinstance(x,tuple) else (A(x),ZERO)
    def add(self,x,y):return (x[0]+y[0],x[1]+y[1])
    def neg(self,x):return (-x[0],-x[1])
    def mul(self,x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+self.v*x[1]*y[1])
    def inverse(self,x):
        a,b=x;norm=a*a+self.v*a*b-b*b
        return ((a+self.v*b)/norm,-b/norm)
    def conj(self,x):return (x[0].flip(8),x[1].flip(8))
    def matrix(self,M):return tuple(tuple((x,ZERO) for x in row) for row in M)
    def zeros(self,n,m=None):return tuple(tuple(self.zero for _ in range(n if m is None else m)) for _ in range(n))
    def sum(self,xs):
        out=self.zero
        for x in xs:out=self.add(out,x)
        return out
    def mm(self,M,N):return tuple(tuple(self.sum(self.mul(x,y) for x,y in zip(row,col)) for col in zip(*N)) for row in M)
    def adj(self,M):return tuple(tuple(self.conj(x) for x in row) for row in zip(*M))
    def madd(self,M,N):return tuple(tuple(self.add(x,y) for x,y in zip(row,col)) for row,col in zip(M,N))
    def scale(self,c,M):return tuple(tuple(self.mul(c,x) for x in row) for row in M)
    def rank(self,M):
        rows=[list(row) for row in M];k=0
        for j in range(len(rows[0])):
            pivot=next((i for i in range(k,len(rows)) if rows[i][j]!=self.zero),None)
            if pivot is None:continue
            rows[k],rows[pivot]=rows[pivot],rows[k];inv=self.inverse(rows[k][j]);rows[k]=[self.mul(inv,x) for x in rows[k]]
            for i in range(k+1,len(rows)):
                c=rows[i][j];rows[i]=[self.add(x,self.neg(self.mul(c,y))) for x,y in zip(rows[i],rows[k])]
            k+=1
        return k
    def record(self,M):return [[{'constant':x[0].record(),'r':x[1].record()} for x in row] for row in M]


def audit():
    previous=closure_audit();spec=load('research/strominger/contracts/common-endpoint-charging.json');v=F(spec['beta'])/4
    op=load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']
    K=tuple(tuple(decode(x) for x in row) for row in op['kinetic_operator']);Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q))
    f=Field(v);r=(ZERO,ONE);I=f.matrix(eye(4));Pr=f.matrix(P);low=[];grounds=[];blocks=[];reports=[]
    norm=f.add(f.one,f.mul(r,r));inverse_norm=f.inverse(norm)
    for i in range(4):
        e=tuple((ONE if j==i else ZERO,) for j in range(4));qe=mm(Q,e)
        z=add(e,qe);Z=scale(A(F(1,2)),mm(z,adj(z)))
        g=f.madd(f.scale(r,f.matrix(e)),f.matrix(qe))
        G=f.scale(inverse_norm,f.mm(g,f.adj(g)))
        zero_line=f.matrix(add(P,scale(A(-1),Z)))
        Pi=f.madd(zero_line,G)
        Ei=tuple(tuple(ONE if a==b==i else ZERO for b in range(4)) for a in range(4))
        H=f.matrix(add(K,scale(A(-v),Ei)))
        assert f.mm(H,G)==f.scale(f.add(f.one,f.neg(r)),G)
        assert f.mm(H,zero_line)==f.zeros(4)
        assert f.mm(G,zero_line)==f.zeros(4)
        assert f.mm(Pi,Pi)==Pi and f.adj(Pi)==Pi and f.rank(Pi)==2
        assert f.mm(Pi,H)==f.mm(H,Pi)
        assert f.rank(G)==f.rank(zero_line)==1
        assert Pi!=Pr
        low.append(Pi);grounds.append(G);blocks.append(H)
        reports.append({'lead':i,'ground_projector':f.record(G),'zero_line_projector':record(add(P,scale(A(-1),Z))),
                        'low_projector':f.record(Pi),'low_rank':2,'ground_rank':1})
    common_constraints=tuple(row for Pi in low for row in f.madd(I,f.scale((-ONE,ZERO),Pi)))
    assert f.rank(common_constraints)==4  # common intersection is zero
    # Any common invariant subspace for Hermitian H_i is reducing. Differences
    # H_i-H_j=-v(E_i-E_j) force its projector diagonal, then dense K forces scalar.
    assert all(K[i][j]!=ZERO for i in range(4) for j in range(4) if i!=j)
    assert v>0

    # Actual native binary-tetrahedral actions, not fitted projectors transports.
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    V=tuple(tuple(decode(x) for x in row) for row in face_audit()['adapter']['V'])
    n0=mm(adj(V),V)[0][0];D=scale(n0.inverse(),adj(V))
    quats={tuple(F(s if i==k else 0) for i in range(4)) for k in range(4) for s in (-1,1)}
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    actions={};action_rows=[]
    for q in sorted(quats):
        U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        perm=[face.index(mm(mm(U,p),adj(U))) for p in face]
        raw=tuple(tuple(U[i%2][j%2] if i//2==perm[j//2] else ZERO for j in range(8)) for i in range(8))
        T=mm(mm(D,raw),V);actions[q]=T
        assert mm(adj(T),T)==eye(4) and mm(T,K)==mm(K,T)
        Tf=f.matrix(T)
        for i in range(4):
            assert f.mm(Tf,blocks[i])==f.mm(blocks[perm[i]],Tf)
            assert f.mm(f.mm(Tf,low[i]),f.adj(Tf))==low[perm[i]]
            assert f.mm(f.mm(Tf,grounds[i]),f.adj(Tf))==grounds[perm[i]]
        action_rows.append({'quaternion':list(map(str,q)),'lead_permutation':perm,'line_transport':record(T)})
    for q,T in actions.items():
        for p,S in actions.items():assert mm(T,S)==actions[qm(q,p)]
    assert actions[(-F(1),F(0),F(0),F(0))]==scale(A(-1),eye(4))
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_dressed_flux_projectors.py'}
    return {
        'schema':'marici.scattering.dressed-flux-projectors.v1',
        'status':'exact_flux_dependent_low_planes_covariant_under_joint_native_symmetry_no_common_fixed_matter_plane',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'field':{'extension':'a+b*r over prior exact multiquadratic field','relation':'r^2-v*r-1=0',
                  'v':str(v),'branch':'r=(v+sqrt(v^2+4))/2>1'},
        'projectors':reports,
        'construction':{'ground':'G_i=(r*e_i+Qe_i)(r*e_i+Qe_i)^*/(r^2+1)',
                         'zero_line':'Z0_i=P-(e_i+Qe_i)(e_i+Qe_i)^*/2',
                         'low':'Pi_i=G_i+Z0_i','low_eigenvalues':['1-r','0'],
                         'complement_eigenvalues':['1+1/r','2'],'both_records_retained':True},
        'fixed_carrier_gate':{'intersection_of_four_low_planes_dimension':0,
                              'any_common_nontrivial_invariant_matter_subspace':False,
                              'proof':'Common reducing projector commutes with all H_i differences, hence all diagonal E_i; it is diagonal. Dense K connects every coordinate, forcing a scalar projector.',
                              'scope':'one matter carrier shared across all fixed unit-lead blocks, with unchanged charged operators'},
        'joint_source_symmetry':{'native_actions':action_rows,'group_elements':24,'group_compositions_checked':576,
                                 'matter_and_lead_covariance':True,'central_minus_one_acts_as_minus_identity':True,
                                 'direct_sum_low_rank':8,'direct_sum_ground_rank':4,
                                 'full_field_ground_is_rank_two':False,
                                 'source_symmetry_is_physical_spin_rotation':False},
        'boundary':{'all_flux_labelled_spinor_transports_excluded':False,'lead_labels_silently_erased':False,
                    'physical_charge_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Decompose the four-dimensional flux-labelled ground representation under the native binary-tetrahedral action. Test whether rank-two spinorial sectors exist and whether the retained source/charge/flux observables select one without discarding lead history.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale dressed-flux receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact dressed rank-two projectors commute with their own flux blocks; common intersection is zero.')
    print('PASS: 24 native actions and 576 compositions preserve joint matter/lead covariance and rank-four ground space.')
    print('Boundary: flux-labelled dressed transport exists, not a common fixed matter doublet or physical spin identification.')


if __name__=='__main__':main()
