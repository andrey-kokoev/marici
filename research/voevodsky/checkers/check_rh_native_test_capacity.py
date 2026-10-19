"""Positive15-dimensional Weil witness versus inherited signed native index14.
No assumption on complex encoder coefficients; no no-go for nonlinear maps.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,mm,adj,madd,msub,mzero,parse,sparse,trace,eye
from check_rh_two_seed_route_audit import build,diagonal,blockdiag,multiply_scalar
from check_rh_full_divisor_window import completed_xi
from check_rh_source_kernel_generation import ar,bounds,dump,arb,acb,ctx
import flint


def grid(blocks):
    n=len(blocks[0][0]);return [[blocks[i//n][j//n][i%n][j%n] for j in range(3*n)] for i in range(3*n)]

def native_inertia(name,ops,metric):
    bank=build(name,ops,metric);L,G,N=ops;n=len(L);Z=mzero(n,n);A=msub(L,N);B=msub(G,N)
    half=lambda x:multiply_scalar(x,F(1,2))
    def transient(sign):
        return grid([[half(A),multiply_scalar(A,F(sign,2)),Z],
                     [multiply_scalar(A,F(sign,2)),half(madd(A,B)),multiply_scalar(B,F(sign,2))],
                     [Z,multiply_scalar(B,F(sign,2)),half(B)]])
    core1=grid([[multiply_scalar(N,F(1,3)) for _ in range(3)] for _ in range(3)])
    plus=transient(1);minus=madd(transient(-1),msub(blockdiag([N]*3),core1))
    zero=msub(eye(3*n),madd(madd(core1,plus),minus))
    P={'1':core1,'1/2':plus,'-1/2':minus,'0':zero}
    K=mm(diagonal([1/x for x in metric]*3),bank['H'])
    assert K==madd(msub(half(plus),half(minus)),core1)
    certs={};mult={}
    for value,projector in P.items():
        assert mm(projector,projector)==projector
        assert mm(bank['Ms'],projector)==mm(adj(projector),bank['Ms'])
        assert mm(K,projector)==multiply_scalar(projector,F(value))
        r,im=trace(projector);assert im==0 and r.denominator==1
        mult[value]=int(r)
        certs[value]={'multiplicity':int(r),'idempotent':True,'metric_self_adjoint':True,'exact_eigenprojector':True,
                      'projector_sha256':sha256(json.dumps(sparse(projector),sort_keys=True).encode()).hexdigest()}
    assert mult=={'1':1,'1/2':13,'-1/2':15,'0':79}
    # Orthogonal metric-self-adjoint projections summing to I give a complete
    # metric eigenbasis. On each subspace H has sign of its exact eigenvalue.
    assert all(x>0 for x in metric)
    inertia=[sum(r for v,r in mult.items() if F(v)>0),sum(r for v,r in mult.items() if F(v)<0),mult['0']]
    assert inertia==[14,15,79]
    return {'stage_ranks':bank['ranks'],'native_dimension':3*n,'inertia_positive_negative_zero':inertia,
            'exact_metric_eigenprojectors':certs,'arbitrary_complex_fixed_linear_encoder_positive_capacity':inertia[0]}

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-native-test-capacity-v1.json';c=json.loads(cp.read_text());ctx.prec=c['precision_bits']
    t=ar(c['t']);a=list(map(ar,c['frequency_centres']));m=len(a);T=c['window_height'];pi=arb.pi();I=acb(0,1)
    assert m==15 and len(set(c['frequency_centres']))==m and t>0 and T>=13 and all(abs(x)<T for x in a)
    refs=[ROOT/c[k] for k in ('count_contract','tail_derivation','primary_convention')]
    assert 'multiplicities' in refs[0].read_text() and 'Jensen' in refs[1].read_text() and 'even' in refs[2].read_text()
    assert pi>3 and arb(18).log()<3 and arb(2).log()>ar('1/2') and arb(16).log()<4 and F(16)**2/2-16-6>0
    count=arb(T).zeta_nzeros();n=count.unique_fmpz();assert n is not None and int(n)==c['expected_positive_ordinate_count']
    stable=arb(T,ar('1/100')).zeta_nzeros();assert stable.unique_fmpz()==n
    # Proposal -> rigorous opposite-sign brackets -> total count completeness.
    roots=[];certs=[];last=F(0);radius=arb(c['root_bracket_radius'])
    for k,p in enumerate(acb.zeta_zeros(1,int(n)),1):
        assert p.is_finite() and p.real==ar('1/2')
        gamma=p.imag.mid()+arb(0,radius);lo,hi=bounds(gamma);assert last<lo<hi<T;last=hi
        xi=[completed_xi(acb(ar('1/2'),ar(x)),pi) for x in (lo,hi)]
        assert all(x.imag.contains(0) and x.is_finite() for x in xi) and xi[0].real*xi[1].real<0
        roots.append(acb(ar('1/2'),gamma))
        certs.append({'index':k,'ordinate_bracket':list(map(str,(lo,hi))),'xi_endpoint_signs':[1 if x.real>0 else -1 for x in xi],
                      'simple_by_total_count':True})
    # All full-divisor coefficients are generated from root certificates and
    # the RH-free Jensen tail, not from an arithmetic table or assumed RH.
    S=[[arb(0) for _ in range(m)] for _ in range(m)];entries=[]
    for i in range(m):
        for j in range(i,m):
            centre=(a[i]+a[j])/2;prefactor=(-t*(a[i]-a[j])**2/4).exp()
            def h(u):return acb(prefactor)*(-acb(t)*(u-acb(centre))**2).exp()
            window=sum(((h((r-ar('1/2'))/I)+h((r.conjugate()-ar('1/2'))/I))/2 for r in roots),acb(0))
            assert window.imag.contains(0)
            q=abs(centre);d=arb(T)-q
            tail=prefactor*(t/4).exp()*((-t*d*d).exp()*((arb(T)+3)**2+1/t)
                  +(q+3)*(pi/t).sqrt()*(t.sqrt()*d).erfc())
            assert tail>0 and tail<arb('1e-300')
            S[i][j]=S[j][i]=window.real+arb(0,tail)
            entries.append({'indices':[i,j],'full_divisor_enclosure':dump(S[i][j]),'off_critical_safe_tail':dump(tail)})
    L=[[arb(i==j) for j in range(m)] for i in range(m)];D=[]
    for j in range(m):
        pivot=S[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0));assert pivot>0,(j,str(pivot))
        D.append(pivot)
        for i in range(j+1,m):L[i][j]=(S[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/pivot
    pp,np=ROOT/c['proton'],ROOT/c['neutron'];_,pops=parse(json.loads(pp.read_text()))
    ns=json.loads(np.read_text());ds=[F(x['d']) for x in ns['coordinates']];nops=[mzero(36,36) for _ in range(3)]
    for row in ns['arrows']:
        aa,bb,cc,dd=map(F,row['numerator']);assert bb==dd==0
        nops['LGN'.index(row['stage'])][row['target']][row['source']]=(aa/ds[row['source']],cc/ds[row['source']])
    native={'protonlike':native_inertia('protonlike',pops,[F(1)]*36),
            'neutron':native_inertia('neutron',nops,[1/x for x in ds])}
    assert all(m>x['arbitrary_complex_fixed_linear_encoder_positive_capacity'] for x in native.values())
    # Sylvester index bound: E*HE=S>0 on C^15 forces E injective and its
    # image a positive15-subspace. Both H have maximum positive dimension14.
    result={'schema':'marici.rh-native-test-capacity.v1','passed':True,'iteration':6,'parameters':c,
      'software':{'python_flint':flint.__version__,'FLINT':flint.__FLINT_VERSION__},
      'complete_positive_ordinate_window_count':int(n),'count_cutoff_neighborhood':str(stable),
      'window_root_certificates':certs,'full_divisor_entries':entries,'positive_interval_LDL_pivots':[dump(x) for x in D],
      'certified_full_divisor_positive_index_lower_bound':m,'tail_allows_off_critical_zeros':True,
      'spectral_generation_uses_stored_arithmetic_matrix':False,'native_inertias':native,
      'same_capacity_obstruction_in_both':True,'fixed_linear_encoder_to_retained_H_exists_for_this15_span':False,
      'even_arbitrary_transcendental_encoder_coefficients_do_not_remove_index_barrier':True,
      'three_test_attachment_invalidated':False,'one_adjustable_point_readout_is_a_full_test_encoder':False,
      'arithmetic15_span_independently_numerically_generated':False,
      'arithmetic15_span_identity_basis':'The primary explicit-formula theorem applies to the same admissible evenized Gaussian products; source equality is analytic, not a new120-entry arithmetic numerical certificate.',
      'no_go_for_all_possible_RH_models_or_readouts':False,'native_analytic_generator_constructed':False,
      'all_test_positivity_proved':False,'RH_proved':False,'shared_sources_modified':False,
      'scope':c['scope'],
      'next_obligation':'Specify an operation-bearing infinite analytic test/dual completion, with fixed pairing and evaluators, rather than claiming the fixed native H carries all test quantifiers.'}
    files=[cp,*refs,pp,np,Path(__file__),base/'checkers/check_rh_full_divisor_window.py',base/'checkers/check_rh_two_seed_route_audit.py',Path(flint.__file__)]
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in files}
    (base/'results/rh-native-test-capacity-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'complete_positive_window_count':int(n),'full_divisor_positive15_span_certified':True,
      'native_inertias':{k:v['inertia_positive_negative_zero'] for k,v in native.items()},
      'fixed_linear_full_test_encoder_to_retained_H_in_either':False,'prior_three_test_comparison_still_valid':True,'RH_proved':False},indent=2))
if __name__=='__main__':main()
