"""Independent multi-object motion and exact endpoint self-energy enclosures.
Free half-line objects, explicitly declared endpoint attachments; no photon claim.
Standard library only. Exact finite occupation metrics and Catalan convolutions.
"""
from fractions import Fraction as Q
from itertools import product,combinations_with_replacement
from math import comb,factorial,cos,sin,pi
from pathlib import Path
from hashlib import sha256
import json
from check_typed_spin_channels import decode
from check_pentachoron_spin_interfaces import A,mm,adj,add,scale

BASE=Path(__file__).resolve().parents[1]

def matvec(H,v):return [sum((x*y for x,y in zip(row,v)),Q()) for row in H]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
def solve(H,b):
    rows=[[Q(x) for x in row]+[Q(v)] for row,v in zip(H,b)];n=len(rows)
    for j in range(n):
        pivot=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(n):
            if i==j:continue
            c=rows[i][j]
            if c:rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return [row[-1] for row in rows]
def positive_definite(H):
    rows=[[Q(x) for x in row] for row in H]
    assert all(rows[i][j]==rows[j][i] for i in range(len(rows)) for j in range(len(rows)))
    for j in range(len(rows)):
        pivot=rows[j][j]
        if pivot<=0:return False
        for i in range(j+1,len(rows)):
            for l in range(j+1,len(rows)):
                rows[i][l]-=rows[i][j]*rows[j][l]/pivot
    return True

def occupation_model(L,k):
    """Basis is the unnormalized sum of labelled configurations per orbit.
    Gram multiplicity is retained; hopping is not falsely Euclidean symmetric.
    """
    occupations=[]
    for positions in combinations_with_replacement(range(L),k):
        occupations.append(tuple(positions.count(j) for j in range(L)))
    index={v:i for i,v in enumerate(occupations)};n=len(occupations)
    H=[[Q(2*k if i==j else 0) for j in range(n)] for i in range(n)]
    metric=[Q(factorial(k),product_factorials(v)) for v in occupations]
    for i,v in enumerate(occupations):
        for b in range(L):
            if not v[b]:continue
            for a in (b-1,b+1):
                if not 0<=a<L:continue
                source=list(v);source[b]-=1;source[a]+=1
                H[i][index[tuple(source)]]-=v[b]
    vertex=index[(k,)+(0,)*(L-1)]
    e=[Q(i==vertex) for i in range(n)]
    return occupations,H,metric,e

def product_factorials(v):
    out=1
    for x in v:out*=factorial(x)
    return out

def moments(k,N):
    one=[comb(2*(n+1),n+1)//(n+2) for n in range(N+1)]
    out=[1]+[0]*N
    for _ in range(k):
        out=[sum(comb(n,j)*out[j]*one[n-j] for j in range(n+1)) for n in range(N+1)]
    return out

def enclose_g(k,s,ms,N):
    # Endpoint spectral reflection identifies moments of 4kI-H with those of H.
    # g(-s)=-sum_{n>=0} m_n/(s+4k)^(n+1), a positive-series certificate.
    partial=sum((Q(ms[n],(s+4*k)**(n+1)) for n in range(N+1)),Q())
    error=Q(4*k,s+4*k)**(N+1)/s
    return -partial-error,-partial,error

def quadrature_g(k,L,s):
    # Spectral nodes/weights of the length-L one-body Dirichlet truncation.
    nodes=[2-2*cos(j*pi/(L+1)) for j in range(1,L+1)]
    weights=[2/(L+1)*sin(j*pi/(L+1))**2 for j in range(1,L+1)]
    out=0.0
    for indices in product(range(L),repeat=k):
        w=1.0
        for i in indices:w*=weights[i]
        out-=w/(s+sum(nodes[i] for i in indices))
    return out

def encoded_interval(lo,hi):return {'lower':str(lo),'upper':str(hi),'decimal_view':[float(lo),float(hi)]}

def main():
    typed_path=BASE/'results/typed_spin_channels.json'
    typed=json.loads(typed_path.read_text(encoding='utf-8'));assert typed['verification_passed']
    for name,digest in typed['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    decode_matrix=lambda raw:tuple(tuple(decode(x) for x in row) for row in raw)
    Ps=decode_matrix(typed['input_scalar_projector']);Pv=decode_matrix(typed['input_vector_projector'])
    M2=decode_matrix(typed['two_output_map']);M3=decode_matrix(typed['three_output_map'])
    check('typed_vertex_gram_two',mm(adj(M2),M2)==Ps)
    check('typed_vertex_gram_three',mm(adj(M3),M3)==Pv)
    check('typed_projectors_retained',mm(Ps,Ps)==Ps and mm(Pv,Pv)==Pv and add(Ps,Pv)==tuple(tuple(A(i==j) for j in range(4)) for i in range(4)))
    N=384;all_ms={k:moments(k,N) for k in (1,2,3)}
    check('one_object_endpoint_Catalan_controls',all_ms[1][:5]==[1,2,5,14,42])
    check('independent_two_three_mean_energy',all_ms[2][1]==4 and all_ms[3][1]==6)
    check('independent_two_three_variance',all_ms[2][2]-16==2 and all_ms[3][2]-36==3)
    finite=[];enclosures=[]
    for k in (2,3):
        L=4;occupations,H,metric,e=occupation_model(L,k);n=len(H)
        check('occupation_dimension_'+str(k),n==comb(L+k-1,k))
        check('occupation_metric_selfadjoint_'+str(k),all(metric[i]*H[i][j]==metric[j]*H[j][i] for i in range(n) for j in range(n)))
        gramH=[[metric[i]*H[i][j] for j in range(n)] for i in range(n)]
        check('positive_finite_free_H_'+str(k),positive_definite(gramH))
        upper=[[metric[i]*(4*k*(i==j)-H[i][j]) for j in range(n)] for i in range(n)]
        check('finite_band_upper_bound_'+str(k),positive_definite(upper))
        v=list(e);actual=[]
        for order in range(2*L):
            actual.append(dot(e,v));v=matvec(H,v)
        check('exact_finite_infinite_moment_match_'+str(k),actual==all_ms[k][:2*L])
        # Verify the occupation quotient against fully labelled independent moves.
        labelled=list(product(range(L),repeat=k));position_index={v:i for i,v in enumerate(occupations)}
        check('occupation_Gram_matches_labelled_counts_'+str(k),all(metric[i]==sum(tuple(p.count(j) for j in range(L))==v for p in labelled) for i,v in enumerate(occupations)))
        match=True
        for p in labelled:
            row=[Q() for _ in occupations];row[position_index[tuple(p.count(j) for j in range(L))]]=2*k
            for a in range(k):
                for b in (p[a]-1,p[a]+1):
                    if 0<=b<L:
                        target=list(p);target[a]=b
                        row[position_index[tuple(target.count(j) for j in range(L))]]-=1
            match=match and row==H[position_index[tuple(p.count(j) for j in range(L))]]
        check('occupation_operator_equals_labelled_free_sum_'+str(k),match)
        s=1;negative=[[Q(-s*(i==j))-H[i][j] for j in range(n)] for i in range(n)]
        gfinite=dot(e,solve(negative,e))
        check('finite_spectral_quadrature_control_'+str(k),abs(float(gfinite)-quadrature_g(k,L,s))<1e-13)
        lo,hi,_=enclose_g(k,s,all_ms[k],N)
        # First 2L moments agree. Each spectral measure has mass one in [0,4k].
        truncation_bound=2*Q(4*k,s+4*k)**(2*L)/s
        check('finite_vs_infinite_resolvent_bound_'+str(k),lo-truncation_bound<=gfinite<=hi+truncation_bound)
        finite.append({'objects':k,'sites_per_object':L,'labelled_dimension':L**k,'symmetric_orbital_dimension':n,
            'occupations':[list(v) for v in occupations],'Gram_diagonal':list(map(str,metric)),
            'Hamiltonian':[[str(v) for v in row] for row in H],
            'matched_moments':list(map(str,actual)),'endpoint_g_at_minus_one':str(gfinite)})
        for s in (1,2,4):
            lo,hi,error=enclose_g(k,s,all_ms[k],N)
            check('certified_negative_selfenergy_'+str(k)+'_'+str(s),lo<hi<0 and error<Q(1,10**12))
            check('resolvent_norm_bound_'+str(k)+'_'+str(s),-Q(1,s)<=lo and hi<0)
            enclosures.append({'objects':k,'z':str(-s),'g':encoded_interval(lo,hi),
                'series_terms':N+1,'tail_bound':str(error)})
        check('endpoint_measure_not_one_collective_lead_'+str(k),all_ms[k][2]!=(2*k)**2+k*k)
    # Matrix-valued spectral moments: Mk^dag (H_orb^n tensor I) Mk.
    check('matrix_spectral_moment_zero',mm(adj(M2),M2)==Ps and mm(adj(M3),M3)==Pv)
    check('matrix_spectral_first_moment',scale(A(all_ms[2][1]),mm(adj(M2),M2))==scale(A(4),Ps) and scale(A(all_ms[3][1]),mm(adj(M3),M3))==scale(A(6),Pv))
    check('separated_position_records_present',any(sum(x>0 for x in v)>1 for v in finite[0]['occupations']) and any(sum(x>0 for x in v)>1 for v in finite[1]['occupations']))
    # Positive channel density and retarded sign follow from the normalized
    # convolution measures; no finite box is declared to be a continuum.
    result={'verification_passed':all(checks.values()),'checks':checks,
        'one_body_H':'h=2I-shift-shift_dagger on ell2(N0), Dirichlet ghost at -1',
        'multiobject_H':'H_k=sum_a h_a, restricted to exchange-symmetric full object records for outputs',
        'bands':{'incoming_pair':[0,8],'two_output':[0,8],'three_output':[0,12]},
        'one_body_endpoint_density':'rho1(E)=sqrt(E(4-E))/(2pi) for 0<E<4; zero otherwise',
        'multiobject_density':'rho_k=rho1 convolved k times; normalized energy-sum measure',
        'endpoint_g':'g_k(z)=integral rho_k(E)/(z-E) dE',
        'selfenergies':{'incoming_pair':'lambda_in^2 g_2(z) I4; distinguishable declared input pair',
            'two_output':'lambda_2^2 g_2(z) P_scalar','three_output':'lambda_3^2 g_3(z) P_vector'},
        'retarded_width':'Gamma_k(E)=-2 Im Sigma_k(E+i0)=2pi lambda_k^2 rho_k(E) P_k',
        'core_resolvent':'[zI4-H_core-Sigma_in(z)-Sigma_2(z)-Sigma_3(z)]^-1; H_core Hermitian and vertices explicitly declared, not derived native couplings',
        'threshold_density':{'two':'rho2(E)~E^2/(8pi)','three':'rho3(E)~2 E^(7/2)/(105 pi^2)'},
        'finite_controls':finite,'certified_below_band_g':enclosures,
        'endpoint_moments_first_nine':{str(k):ms[:9] for k,ms in all_ms.items()},
        'qualifications':['Independent orbital motion is retained, not diagonal-copy motion.',
            'The free dispersion, product endpoint attachment and couplings are declared.',
            'The symmetric-internal attachment is a subspace of full bosonic object records; antisymmetric internal/orbital channels require additional vertices.',
            'Finite-box resolvents validate the construction but are not used as continuum spectral densities.',
            'No native spinor-core coupling, positron/photon identification, on-band flux probabilities or reaction ratio is yet derived.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (typed_path,Path(__file__),BASE/'checkers/check_typed_spin_channels.py',BASE/'checkers/check_pentachoron_spin_interfaces.py')}}
    (BASE/'results/multiobject_orbital_selfenergy.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'endpoint_g_enclosures':[
        {'objects':v['objects'],'z':v['z'],'decimal_view':v['g']['decimal_view']} for v in enclosures]},indent=2))

if __name__=='__main__':main()
