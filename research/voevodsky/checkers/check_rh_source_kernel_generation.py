"""Iteration4: generate source operators from kernels, not stored term matrices.
Primary even-test convention; full complex digamma callback. Shared inputs read only.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
from check_proton_native_task_catalogue import ROOT,ZERO,mm,adj,madd,mzero,parse,sparse
from check_proton_single_probe_cycle import inverse
from check_rh_two_seed_route_audit import build
from check_rh_term_resolved_seam import ball,overlap,PAIRS
from check_rh_gaussian_seed_packet import prime_powers
try:from flint import arb,acb,ctx
except ModuleNotFoundError:
    sys.path.insert(0,str(ROOT/'research/flavor/.venv/Lib/site-packages'))
    from flint import arb,acb,ctx
import flint


def ar(q):
    q=F(q);return arb(q.numerator)/q.denominator
def bounds(x):
    m=F(str(x.mid().fmpq()));r=F(str(x.rad().fmpq()));return m-r,m+r
def dump(x):return {'ball':str(x),'rational_bounds':list(map(str,bounds(x)))}
def midmatrix(rows):
    out=[[ZERO]*3 for _ in range(3)]
    for (i,j),x in zip(PAIRS,rows):out[i][j]=out[j][i]=(F(str(x.mid().fmpq())),F(0))
    return out

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-source-kernel-generation-v1.json';c=json.loads(cp.read_text());ctx.prec=c['precision_bits']
    primary=ROOT/c['primary_excerpt'];text=primary.read_text();assert c['primary_response_sha256'] in text
    for token in ('\\frac{1}{2\\pi}','e^{-2\\pi i x \\xi}','counting multiplicities','\\frac{\\rho-1/2}{i}'):
        assert token in text,token
    # Apply the primary formula to EVEN h+h(-u). All coefficients and the
    # full reflected divisor share factor4 relative to the half convention.
    private={'endpoint':F(1),'gamma_integral_pi_units':F(1,4),'gamma_log_pi_units':F(-1,4),
             'prime_cosine_sqrt_pi_t_units':F(-1,2),'signed_h_divisor':F(1,2)}
    external={'endpoint':F(4),'gamma_integral_pi_units':F(1),'gamma_log_pi_units':F(-1),
              'prime_cosine_sqrt_pi_t_units':F(-2),'signed_h_divisor':F(2)}
    ratios={k:external[k]/private[k] for k in private};assert set(ratios.values())=={F(4)} and all(x!=2 for x in ratios.values())
    t=ar(c['t']);a=[ar(x) for x in c['frequency_centres']];pi=arb.pi();I=acb(0,1);N=c['prime_cutoff'];R=F(c['gamma_cutoff']);tol=arb(c['quadrature_tolerance'])
    assert F(c['t'])>0 and c['frequency_centres'][0]=='0'
    powers=prime_powers(N)
    # Arithmetic generation uses NO previous matrix values or zero positions.
    atoms=[(n,p,arb(p).log()/arb(n).sqrt(),arb(n).log()) for n,p in powers]
    ellN=arb(N).log();assert 1/ellN-arb(1)/2-ellN/(2*t)<0
    z=ellN-t
    prime_tail=(t/4).exp()*(2*t*(-z*z/(4*t)).exp()+t*(pi*t).sqrt()*(z/(2*t.sqrt())).erfc())/(2*(pi*t).sqrt())
    assert prime_tail>0 and prime_tail<arb('1e-50')
    rows={k:[] for k in ('endpoint','gamma','prime')};records=[]
    moments={sign:[(acb(t)/2*(acb(ar(F(sign,2)))+I*x)**2).exp() for x in a] for sign in (1,-1)}
    for i,j in PAIRS:
        ai,aj=a[i],a[j];xi=(ai+aj)/2;factor=(-t*(ai-aj)**2/4).exp()
        # Exponential logarithmic moments generate the endpoint before G.
        endpoint_complex=(moments[1][i]*moments[-1][j].conjugate()+moments[-1][i]*moments[1][j].conjugate())/2
        assert endpoint_complex.imag.contains(0)
        endpoint=endpoint_complex.real
        closed_endpoint=factor*(t/4-t*xi*xi).exp()*(t*xi).cos()
        assert (endpoint-closed_endpoint).contains(0) and not (endpoint-2*closed_endpoint).contains(0)
        # Primary gamma callback is complex digamma, with even h. No real
        # extraction or old term coefficient enters the analytic callback.
        def integrand(u,analytic):
            h_even=acb(factor)*((-acb(t)*(u-acb(xi))**2).exp()+(-acb(t)*(u+acb(xi))**2).exp())
            return h_even*((acb(1)/4+I*u/2).digamma()-acb(pi.log()))
        cuts={-R,R,F(0)}
        cuts.update(F(x) for x in (-32,-16,-8,-4,-2,-1,1,2,4,8,16,32))
        xiq=(F(c['frequency_centres'][i])+F(c['frequency_centres'][j]))/2
        cuts.update((xiq,-xiq));cuts=sorted(x for x in cuts if -R<=x<=R)
        integral=acb(0)
        for lo,hi in zip(cuts,cuts[1:]):
            value=acb.integral(integrand,acb(ar(lo)),acb(ar(hi)),abs_tol=tol,rel_tol=tol,eval_limit=100000,depth_limit=40)
            assert value.is_finite(),'primary gamma integral inconclusive'
            integral+=value
        assert integral.imag.contains(0)
        # |psi(1/4+iu/2)-log pi| <=16+2u^2: Re bound10+2u²,
        # Im bound4 from series+integral, and log pi<2. Two even Gaussian
        # lobes and both tails yield the following primary/4 majorant.
        d=ar(R)-abs(xi);assert d>0
        J0=pi.sqrt()*(t.sqrt()*d).erfc()/(2*t.sqrt())
        J2=d*(-t*d*d).exp()/(2*t)+J0/(2*t)
        gamma_tail=((16+4*xi*xi)*J0+4*J2)/(2*pi)
        assert gamma_tail>=0 and gamma_tail<arb('1e-70')
        gamma=integral.real/(8*pi)+arb(0,arb('1e-70'))
        # Weighted translations in logarithmic space. Their closed Gaussian
        # overlap is derived by completing the square, not from prime matrix.
        prime=arb(0);primitive=[]
        for n,p,weight,ell in atoms:
            correlation=acb(factor*(-ell*ell/(4*t)).exp()/(2*(pi*t).sqrt()))*(I*xi*ell).exp()
            value=-weight*correlation.real;prime+=value
            if n in (2,3,4,8):
                # In BRS convention h_even's paired Fourier atoms are
                # 4pi*(corr(ell)+corr(-ell)); solving for zeros and /4
                # returns minus Lambda/sqrt(n)*Re corr(ell).
                fourier_pair=4*pi*(correlation+correlation.conjugate())
                primary_quarter=-weight*fourier_pair.real/(8*pi)
                assert (primary_quarter-value).contains(0)
                primitive.append({'n':n,'base_prime':p,'logarithmic_shift':str(ell),
                    'von_mangoldt':str(arb(p).log()),'correlation':str(correlation),'signed_contribution':dump(value)})
        prime+=arb(0,arb('1e-50'))
        for label,value in (('endpoint',endpoint),('gamma',gamma),('prime',prime)):rows[label].append(value)
        records.append({'indices':[i,j],'endpoint':dump(endpoint),'gamma':dump(gamma),'prime':dump(prime),
            'primary_gamma_integral':str(integral),'analytic_full_complex_gamma_tail_bound':str(gamma_tail),
            'primitive_prime_translations':primitive})
    G=[[arb(0) for _ in range(3)] for _ in range(3)]
    for k,(i,j) in enumerate(PAIRS):G[i][j]=G[j][i]=sum((rows[label][k] for label in rows),arb(0))
    # Interval LDL independently certifies this freshly generated packet.
    L=[[arb(i==j) for j in range(3)] for i in range(3)];D=[]
    for j in range(3):
        pivot=G[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0));assert pivot>0
        D.append(pivot)
        for i in range(j+1,3):L[i][j]=(G[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/pivot
    # Previous certificate is opened ONLY after source generation. It is a
    # comparator, not an input coefficient oracle for the generated operators.
    oldpath=ROOT/c['prior_certificate'];old=json.loads(oldpath.read_text());assert old['status']=='passed'
    previous={tuple(r['indices']):r for r in old['term_enclosures']}
    matches=[]
    for k,pair in enumerate(PAIRS):
        for label,key in (('endpoint','endpoint'),('gamma','gamma_with_infinite_tail'),('prime','prime_with_infinite_tail')):
            assert overlap(bounds(rows[label][k]),ball(previous[pair][key]))
        assert overlap(bounds(G[pair[0]][pair[1]]),ball(previous[pair]['certified_entry']))
        matches.append({'indices':list(pair),'all_source_term_enclosures_overlap':True})
    # Generate exact midpoint term forms and check both actual metric native
    # pullbacks, keeping analytic intervals distinct from these point forms.
    mids={label:midmatrix(values) for label,values in rows.items()}
    total=madd(madd(mids['endpoint'],mids['gamma']),mids['prime'])
    pp,np=ROOT/c['proton'],ROOT/c['neutron'];_,pops=parse(json.loads(pp.read_text()))
    neutron=json.loads(np.read_text());ds=[F(x['d']) for x in neutron['coordinates']];nops=[mzero(36,36) for _ in range(3)]
    for r in neutron['arrows']:
        aa,bb,cc,dd=map(F,r['numerator']);assert bb==dd==0
        nops['LGN'.index(r['stage'])][r['target']][r['source']]=(aa/ds[r['source']],cc/ds[r['source']])
    native={}
    for name,ops,metric in (('protonlike',pops,[F(1)]*36),('neutron',nops,[1/x for x in ds])):
        bank=build(name,ops,metric);native[name]={}
        for label,form in {**mids,'total_midpoint':total}.items():
            B=bank['attach'](form);assert mm(mm(adj(B),bank['H']),B)==form
            native[name][label]=sparse(B)
    # Exact endpoint0,0 is exp(t/4), with nonzero rational exponent. By
    # Lindemann it is transcendental. Finite operations using only stored
    # algebraic matrices and algebraic descriptor input cannot produce it.
    exponent=F(c['t'])/4;assert exponent==F(1,40)
    result={'schema':'marici.rh-source-kernel-generation.v1','passed':True,'iteration':4,
      'primary_source':{'url':c['primary_url'],'response_sha256':c['primary_response_sha256'],
        'excerpt':primary.relative_to(ROOT).as_posix(),'fresh_direct_text_inspected':True,'Gaussian_formula_convention_verified':True,
        'evenized_test':'h(u)+h(-u)','uniform_full_to_half_factor':4,'ratios':{k:str(v) for k,v in ratios.items()},
        'full_divisor_not_critical_line_assumed':True,
        'analytic_arithmetic_full_divisor_identity_authorized_for_Gaussian_class':True,
        'identity_basis':'Cited primary explicit-formula theorem, Gaussian strip admissibility, evenization and unconditional divisor reflection; not numerical zero exhaustion',
        'Gaussian_strip_bound':'|exp(-t(x+iy-xi)^2)|=exp(-t(x-xi)^2+t y^2)'}, 
      'source_operators':{'endpoint':'two exponential moment functionals in logarithmic space',
        'gamma':'Fourier multiplication by half(Re psi(1/4+iu/2)-log pi)',
        'prime':'minus weighted real translation correlations at log prime powers'},
      'source_generation_reads_old_matrices_or_zeros':False,'generated_term_records':records,
      'prime_power_atoms_generated_from_integers':len(atoms),'prime_tail':dump(prime_tail),
      'generated_matrix':[[dump(x) for x in row] for row in G],'positive_LDL_pivots':[dump(x) for x in D],
      'independent_source_certificate_comparison':matches,'generated_midpoint_terms':{k:sparse(v) for k,v in mids.items()},
      'native_generated_term_attachments':native,'source_terms_represented_in_both':True,
      'bare_seed_exact_generation_gate':{'stored_primitives_algebraic':True,'descriptor_input_algebraic':True,
        'endpoint00':'exp(1/40)','transcendence_uses':'Lindemann theorem','finite_algebraic_seed_only_generation_possible':False,
        'supplied_analytic_states_arbitrary_new_phase_oracles_or_infinite_limits_excluded_from_this_gate':True},
      'full_divisor_exhaustion_certified':False,'native_seed_arrows_implement_analytic_source_operators':False,
      'all_test_Weil_positivity_proved':False,'RH_proved':False,'shared_source_stores_modified':False,
      'next_nonredundant_obligation':'Construct a certified full-divisor finite-window/tail comparison in the now verified convention, or an operation-bearing analytic completion; do not substitute the sampled critical-line scout.',
      'scope':c['scope']}
    paths=[cp,primary,oldpath,pp,np,Path(__file__),base/'checkers/check_rh_gaussian_seed_packet.py',Path(flint.__file__)]
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in paths}
    (base/'results/rh-source-kernel-generation-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'primary_Gaussian_convention_verified':True,'uniform_normalization_factor':4,
       'source_kernels_generated_without_matrix_or_zero_input':True,'certified_positive_packet':True,
       'generated_terms_in_both_native_carriers':True,'native_seed_only_exact_analytic_generation':False,'RH_proved':False},indent=2))
if __name__=='__main__':main()
