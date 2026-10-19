"""Eight local photon Ward/Bose covariants and their forward restriction (exact rationals)."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_primary_loop_v1 as primary
CONTRACT=HOME/'contracts/photon-local-ward-basis-v1.json'
PROOF=HOME/'photon-local-ward-basis-v1.md'
TEST=HOME/'checkers/test_photon_local_ward_basis_v1.py'
MANIFEST=HOME/'scc-models/photon-local-ward-basis-v1.json'
SOURCE=HOME/'sources/photon-scattering-2024-local-spinor-excerpt.tex'
RESULT=HOME/'results/photon-local-ward-basis-v1.json'
NAMES=('g2','f2','g3','f3','h3','g4','g4prime','f4')
DEGREES=(2,2,3,3,3,4,4,4)
E=((Q(),Q(1)),(Q(-1),Q()));Z=((Q(),Q()),(Q(),Q()))
PAIRS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
PHI=((1,1,-1,-1),(1,1,1,1),(1,-1,-1,1),(1,-1,1,-1),(1,1,-1,1))


def transpose(A):return tuple(zip(*A))
def mm(A,B):return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(2)),Q()) for j in range(2)) for i in range(2))
def ma(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def ms(c,A):return tuple(tuple(c*x for x in r) for r in A)
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def bracket(a,b):return a[0]*b[1]-a[1]*b[0]
def determinant(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def frob(A,B):return sum((A[i][j]*B[i][j] for i in range(2) for j in range(2)),Q())
def dual(F):return mm(mm(E,F),transpose(E))
def sym(A):return ms(Q(1,2),ma(A,transpose(A)))
def contract(F,G):return frob(F,dual(G))
def nonzero(F):return any(x for row in F for x in row)


def fields(q,e):
    """Chiral field strengths. e is the scaled polarization bispinor; see packet normalization."""
    return sym(mm(mm(q,E),transpose(e))),sym(mm(mm(transpose(q),E),e))


def minor_term(fi,fj,fk,tm,qi):
    if not all(map(nonzero,(fi,fj,fk,tm))):return Q()
    return frob(fi,mm(mm(mm(dual(fj),qi),dual(tm)),transpose(mm(dual(fk),qi))))


def covariants(q,e):
    """Four-vector multilinear forms: Ward via field strengths, Bose via complete label sums."""
    F,T=zip(*(fields(p,v) for p,v in zip(q,e)))
    s={(i,j):determinant(ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    def x(i,j,k,l):return (s[i,j]+s[k,l])/2
    def w(i,j,k,l):return (s[i,k]*s[i,l]+s[j,k]*s[j,l]+s[k,i]*s[k,j]+s[l,i]*s[l,j])/4
    S2=sum((s[i,j]**2 for i,j in combinations(range(4),2)),Q())/2
    out=[Q() for _ in NAMES]
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j));P=contract(F[i],F[j])*contract(T[k],T[l]);X=x(i,j,k,l)
        out[0]+=P;out[2]+=X*P;out[5]+=X*X*P;out[6]+=w(i,j,k,l)*P
    for (i,j),(k,l) in PAIRS:
        P=contract(F[i],F[j])*contract(F[k],F[l])+contract(T[i],T[j])*contract(T[k],T[l])
        out[1]+=P;out[3]+=x(i,j,k,l)*P/3
    out[7]=S2*out[1]
    for m in range(4):
        for i in range(4):
            if i==m:continue
            j,k=tuple(a for a in range(4) if a not in (i,m))
            out[4]+=(minor_term(F[i],F[j],F[k],T[m],q[i])+
                     minor_term(T[i],T[j],T[k],F[m],transpose(q[i])))/3
    return tuple(out)


def cm(c=Q(3,5),s=Q(4,5),scale=Q(1)):
    assert c*c+s*s==1 and scale>0
    a=((Q(1),Q()),(Q(),Q(1)),(c,s),(-s,c))
    b=(a[0],a[1],tuple(-x for x in a[2]),tuple(-x for x in a[3]))
    a=tuple(tuple(scale*x for x in v) for v in a);b=tuple(tuple(scale*x for x in v) for v in b)
    q=tuple(outer(u,v) for u,v in zip(a,b));assert ma(ma(q[0],q[1]),ma(q[2],q[3]))==Z
    return a,b,q


def reference(v,alternative=False):
    options=((Q(1),Q(1)),(Q(1),Q(-1)),(Q(),Q(1)),(Q(1),Q())) if alternative else ((Q(1),Q()),(Q(),Q(1)))
    return next(r for r in options if bracket(v,r))


def polarizations(a,b,helicities,alternative=False):
    e=[]
    for u,v,h in zip(a,b,helicities):
        if h==1:
            r=reference(v,alternative);e.append(ms(1/bracket(v,r),outer(u,r)))
        else:
            r=reference(u,alternative);e.append(ms(1/bracket(u,r),outer(r,v)))
    return tuple(e)


def spinor_oracle(a,b,h):
    """Independent helicity polynomial evaluation; not the field-strength contraction algorithm."""
    A=lambda i,j:bracket(a[i],a[j]);B=lambda i,j:bracket(b[i],b[j])
    inv=lambda i,j:A(i,j)*B(i,j)
    out=[Q() for _ in NAMES];plus=[i for i in range(4) if h[i]==1];minus=[i for i in range(4) if h[i]==-1]
    if len(plus) in (0,4):
        C=A if plus else B
        S2=sum((inv(i,j)**2 for i,j in combinations(range(4),2)),Q())/2
        for (i,j),(k,l) in PAIRS:
            P=(C(i,j)*C(k,l))**2;out[1]+=P;out[3]+=inv(i,j)*P/3
        out[7]=S2*out[1]
    elif len(plus)==2:
        i,j=plus;k,l=minus;P=(A(i,j)*B(k,l))**2;X=inv(i,j)
        out[0]=P;out[2]=X*P;out[5]=X*X*P;out[6]=inv(i,k)*inv(i,l)*P
    else:
        majority=plus if len(plus)==3 else minus;m=(minus if len(plus)==3 else plus)[0]
        i,j,k=majority;C,D=(A,B) if len(plus)==3 else (B,A)
        out[4]=(D(m,i)*C(i,j)*C(i,k))**2
    return tuple(out)


VECTOR_BASIS=tuple(tuple(tuple(Q(int((i,j)==(a,b))) for j in range(2)) for i in range(2))
                   for a,b in product(range(2),repeat=2))


def tensor_components(q):
    return {indices:covariants(q,tuple(VECTOR_BASIS[i] for i in indices))
            for indices in product(range(4),repeat=4)}


def amplitude_rows(c,s,scale=Q(1)):
    a,b,q=cm(c,s,scale)
    return tuple(covariants(q,polarizations(a,b,h)) for h in PHI)


def reduced_rows(A):
    A=[list(map(Q,r)) for r in A];pivots=[];r=0
    for col in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][col]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];v=A[r][col];A[r]=[x/v for x in A[r]]
        for i in range(len(A)):
            if i!=r:
                v=A[i][col];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
        pivots.append(col);r+=1
        if r==len(A):break
    return tuple(tuple(row) for row in A),tuple(pivots)


def nullspace(A):
    R,pivots=reduced_rows(A);vectors=[]
    for free in (i for i in range(len(A[0])) if i not in pivots):
        v=[Q() for _ in A[0]];v[free]=Q(1)
        for row,p in enumerate(pivots):v[p]=-R[row][free]
        vectors.append(tuple(v))
    return tuple(vectors)


def forward_map():
    # Each covariant has proved homogeneous Mandelstam degree DEGREES[j].
    phi=amplitude_rows(Q(1),Q())
    return tuple(tuple(x if DEGREES[j]==n else Q() for j,x in enumerate(phi[i]))
                 for i,n in ((0,2),(0,3),(0,4),(1,2),(1,4)))


def source_cm_expected(S,T,U):
    g=lambda x,y,z:(x*x,Q(),x**3,Q(),Q(),x**4,x*x*y*z,Q())
    return (g(S,T,U),(Q(),S*S+T*T+U*U,Q(),S*T*U,Q(),Q(),Q(),(S*S+T*T+U*U)**2),
            g(U,T,S),g(T,S,U),(Q(),Q(),Q(),Q(),S*T*U,Q(),Q(),Q()))


def capture_source(path):
    data=path.read_bytes();provenance=json.loads(primary.PROVENANCE.read_text(encoding='utf-8'))
    assert hashlib.sha256(data).hexdigest()==provenance['input_sha256']['tex']
    lines=data.decode('utf-8').splitlines(keepends=True)
    text=('% Attributed unmodified quotations from Haring et al., Bounds on photon scattering, JHEP10(2024)103.\n'
          '% CC-BY-4.0; DOI:10.1007/JHEP10(2024)103; source https://arxiv.org/src/2211.05795\n'
          '% Full source SHA256: '+provenance['input_sha256']['tex']+'\n')
    for first,last in ((2890,2948),(3048,3111)):
        text+=f'\n% main.tex lines {first}-{last}; B.88-B.89 / B.107-B.112.\n'+''.join(lines[first-1:last])
    data=text.encode('utf-8')
    if SOURCE.exists():assert SOURCE.read_bytes()==data,'refusing changed source quotation'
    else:SOURCE.write_bytes(data)
    print(json.dumps({'captured_sha256':hashlib.sha256(data).hexdigest(),'path':SOURCE.relative_to(ROOT).as_posix()}))


def validate_contract(c):
    assert c['schema']=='marici.photon-local-ward-basis.v1' and c['owner']=='marici.Nima'
    assert c['coefficient_order']==list(NAMES) and c['mandelstam_degrees']==list(DEGREES)
    assert c['forward_kernel']==['f3','h3','g4prime']
    for k in ('local_covariant_basis_constructed','all_helicity_sectors_retained','forward_rank_and_kernel_verified'):
        assert c[k] is True,k
    for k in ('loop_tensor_lift_constructed','window_shift_lift_constructed','joint_analyticity_of_full_amplitude_derived',
              'off_shell_operator_basis_exhausted','finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived'):
        assert c[k] is False,k
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==c['primary_spinor_excerpt_sha256']


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    upstream=primary.build();counts={k:0 for k in ('helicity','reference','Ward','Bose','Lorentz','parity','homogeneity')}
    configurations=((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(1),Q()),(Q(),Q(1)))
    # All 16 sectors including forward/backward gauge patches.
    for cc,ss in configurations:
        a,b,q=cm(cc,ss)
        for h in product((1,-1),repeat=4):
            e=polarizations(a,b,h);values=covariants(q,e)
            assert values==spinor_oracle(a,b,h);counts['helicity']+=1
            assert values==covariants(q,polarizations(a,b,h,True));counts['reference']+=1
        assert amplitude_rows(cc,ss)==source_cm_expected(Q(1),-ss*ss,-cc*cc)
    a,b,q=cm();allplus=(1,1,1,1)
    # Three helicity patterns cover all nonzero covariant families in the S4 controls.
    for h in ((1,1,-1,-1),allplus,(1,1,1,-1)):
        e=polarizations(a,b,h);value=covariants(q,e)
        for p in permutations(range(4)):
            assert covariants(tuple(q[i] for i in p),tuple(e[i] for i in p))==value;counts['Bose']+=1
        for i in range(4):
            gauge=list(e);gauge[i]=q[i];assert covariants(q,tuple(gauge))==(Q(),)*8;counts['Ward']+=1
        assert covariants(tuple(map(transpose,q)),tuple(map(transpose,e)))==value;counts['parity']+=1
        for L,R in ((((Q(1),Q(1)),(Q(),Q(1))),((Q(1),Q()),(Q(1),Q(1)))),
                    (((Q(2),Q()),(Q(),Q(1,2))),((Q(3),Q()),(Q(),Q(1,3))))):
            move=lambda M:mm(mm(L,M),transpose(R))
            assert covariants(tuple(map(move,q)),tuple(map(move,e)))==value;counts['Lorentz']+=1
    # General polarizations exercise simultaneous chiral components, not just pure-helicity zeros.
    general=tuple(((Q(i+1),Q(2-i)),(Q(3),Q(i+2))) for i in range(4))
    value=covariants(q,general)
    for i in range(4):
        gauge=list(general);gauge[i]=q[i];assert covariants(q,tuple(gauge))==(Q(),)*8;counts['Ward']+=1
        shift=list(general);shift[i]=ma(shift[i],ms(Q(7,3),q[i]));assert covariants(q,tuple(shift))==value
        rescale=list(general);rescale[i]=ms(Q(3),rescale[i]);assert covariants(q,tuple(rescale))==tuple(3*x for x in value)
    for row1,row2 in zip(amplitude_rows(Q(3,5),Q(4,5)),amplitude_rows(Q(3,5),Q(4,5),Q(2))):
        assert row2==tuple(x*16**degree for x,degree in zip(row1,DEGREES));counts['homogeneity']+=1
    components=tensor_components(q);component_Ward=0
    for leg in range(4):
        for others in product(range(4),repeat=3):
            total=[Q() for _ in NAMES]
            for component in range(4):
                indices=list(others);indices.insert(leg,component)
                coefficient=q[leg][component//2][component%2]
                total=[x+coefficient*y for x,y in zip(total,components[tuple(indices)])]
            assert total==[Q()]*8;component_Ward+=8
    forward=forward_map();_,pivots=reduced_rows(forward);kernel=nullspace(forward)
    assert len(pivots)==5 and tuple(NAMES[next(i for i,x in enumerate(v) if x)] for v in kernel)==('f3','h3','g4prime')
    full=[]
    for scale in (Q(1),Q(2),Q(3)):full.append(amplitude_rows(Q(1),Q(),scale)[0])
    for scale in (Q(1),Q(2)):full.append(amplitude_rows(Q(1),Q(),scale)[1])
    nonforward=amplitude_rows(Q(3,5),Q(4,5));full.extend((nonforward[0],nonforward[1],nonforward[4]))
    assert len(reduced_rows(full)[1])==8
    invisible=tuple(tuple(row[j] for j in (3,4,6)) for row in (nonforward[1],nonforward[4],nonforward[0]))
    assert invisible==((Q(144,625),Q(),Q()),(Q(),Q(144,625),Q()),(Q(),Q(),Q(144,625)))
    # Removing h3 leaves forward output unchanged but loses a genuine helicity sector/full rank.
    dropped=[tuple(Q() if j==4 else x for j,x in enumerate(row)) for row in full]
    assert len(reduced_rows(dropped)[1])==7 and all(row[4]==0 for row in forward)
    # A one-pair f2 alternative is Ward but not Bose: the nonzero residual is exact.
    ea=polarizations(a,b,allplus)
    def single_pair(qq,ee):
        ff,_=zip(*(fields(p,v) for p,v in zip(qq,ee)))
        return contract(ff[0],ff[1])*contract(ff[2],ff[3])
    p=(0,2,1,3);bose_defect=single_pair(q,ea)-single_pair(tuple(q[i] for i in p),tuple(ea[i] for i in p))
    assert bose_defect==Q(369,625)
    refused=['drop_h3_forward_invisible_sector','one_pair_f2_Ward_without_Bose']
    for k in ('loop_tensor_lift_constructed','window_shift_lift_constructed','joint_analyticity_of_full_amplitude_derived',
              'off_shell_operator_basis_exhausted','finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived'):
        bad=copy.deepcopy(c);bad[k]=True
        try:validate_contract(bad)
        except AssertionError:refused.append(k)
        else:raise AssertionError('unsupported local-basis promotion: '+k)
    paths={ROOT/p for p in upstream['source_sha256']}
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,SOURCE,Path(__file__).resolve()))
    return {'schema':'marici.photon-local-ward-basis-receipt.v1','status':'pass',
        'scope':'explicit_local_covariant_multilinear_basis_in_sourced_on_shell_EFT_jet_not_full_loop_tensor',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'coefficient_order':list(NAMES),'counts':counts,'one_point_tensor_components':len(components)*8,
        'one_point_component_Ward_constraints':component_Ward,'forward_map_rows':[[str(x) for x in r] for r in forward],
        'forward_rank':len(pivots),'full_evaluation_rank':8,'forward_kernel':[[str(x) for x in v] for v in kernel],
        'nonforward_invisible_minor':[[str(x) for x in r] for r in invisible],
        'full_independence_witness_rows':[[str(x) for x in r] for r in full],
        'drop_h3_full_rank':7,'single_pair_f2_Bose_defect':str(bose_defect),
        **{k:v for k,v in c.items() if isinstance(v,bool)},
        'general_Ward_Bose_and_Lorentz_proof_machine_formalized':False,'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');p.add_argument('--capture-source',type=Path);a=p.parse_args()
    if a.capture_source:capture_source(a.capture_source);return
    r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale local Ward basis receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','forward_rank','full_evaluation_rank','counts','loop_tensor_lift_constructed','window_shift_lift_constructed')}))

if __name__=='__main__':main()
