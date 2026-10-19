"""Independent spectral computation: complete finite window plus off-line-safe tail.
The arithmetic result is read only AFTER spectral generation. See companion
note for the unconditional Jensen zero-count majorant and tail derivation.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
from check_proton_native_task_catalogue import ROOT,ZERO,mm,adj,madd,msub,mzero,parse,sparse
from check_rh_two_seed_route_audit import build
from check_rh_source_kernel_generation import ar,bounds,dump,midmatrix,PAIRS,arb,acb,ctx
import flint


def completed_xi(s,pi):
    return s*(s-1)/2*(-s*pi.log()/2).exp()*(s/2).gamma()*s.zeta()

def from_bounds(bs):
    lo,hi=map(F,bs);return ar((lo+hi)/2)+arb(0,ar((hi-lo)/2))

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-full-divisor-window-v1.json';c=json.loads(cp.read_text());ctx.prec=c['precision_bits']
    t=ar(c['t']);centres=list(map(ar,c['frequency_centres']));T=c['window_height'];pi=arb.pi();I=acb(0,1)
    assert t>0 and T>=13 and all(abs(x)<T for x in centres)
    contract=ROOT/c['count_contract'];assert 'multiplicities' in contract.read_text()
    # Constants in the analytic ALL-height Jensen majorant. Its monotonic
    # inequalities are derived in the note; not an extrapolation of samples.
    assert pi>3 and arb(18).log()<3 and arb(2).log()>ar('1/2') and arb(16).log()<4
    assert F(16)**2/2-16-6>0
    count_ball=arb(T).zeta_nzeros();count=count_ball.unique_fmpz();assert count is not None
    n=int(count);assert n==21
    stable_count=arb(T,ar('1/100')).zeta_nzeros();assert stable_count.unique_fmpz()==count
    proposals=acb.zeta_zeros(1,n);radius=arb(c['critical_root_bracket_radius']);roots=[];root_records=[];last=F(0)
    for index,proposal in enumerate(proposals,1):
        assert proposal.is_finite() and proposal.real==ar('1/2')
        # Root existence is certified by IVT, not by zeta(ball).contains(0).
        gamma=proposal.imag.mid()+arb(0,radius);lo,hi=bounds(gamma)
        assert last<lo<hi<T;last=hi
        endpoints=[completed_xi(acb(ar('1/2'),ar(x)),pi) for x in (lo,hi)]
        assert all(x.imag.contains(0) and x.is_finite() for x in endpoints)
        assert endpoints[0].real*endpoints[1].real<0
        # 21 disjoint brackets + total multiplicity count21 => one simple
        # root in each, no omitted off-line root in the complete window.
        roots.append(acb(ar('1/2'),gamma))
        root_records.append({'index':index,'proposal':str(proposal),'certified_ordinate_bracket':list(map(str,(lo,hi))),
          'xi_left':str(endpoints[0]),'xi_right':str(endpoints[1]),'opposite_signs':True,'multiplicity':1})
    windows=[];full=[];tails=[];records=[]
    for i,j in PAIRS:
        xi=(centres[i]+centres[j])/2;factor=(-t*(centres[i]-centres[j])**2/4).exp()
        def h(u):return acb(factor)*(-acb(t)*(u-acb(xi))**2).exp()
        total=acb(0)
        for rho in roots:
            # Actual complex-node definition. Finite beta=1/2 is certified,
            # not silently imposed as a condition on the whole divisor.
            total+=(h((rho-ar('1/2'))/I)+h((rho.conjugate()-ar('1/2'))/I))/2
        assert total.is_finite() and total.imag.contains(0)
        q=abs(xi);d=arb(T)-q
        # Half of both conjugate halves is bounded using |Im u|<=1/2,
        # N(v)<=(v+3)^2, and integration by parts on the Gaussian weight.
        tail=factor*(t/4).exp()*((-t*d*d).exp()*((arb(T)+3)**2+1/t)
                    +(q+3)*(pi/t).sqrt()*(t.sqrt()*d).erfc())
        assert tail>0 and tail<arb('1e-140')
        window=total.real;enclosure=window+arb(0,tail)
        windows.append(window);full.append(enclosure);tails.append(tail)
        records.append({'indices':[i,j],'complete_window':dump(window),'off_critical_infinite_tail_bound':dump(tail),
                        'full_divisor':dump(enclosure)})
    # Independently certify positivity on precisely this finite test span.
    SG=[[arb(0) for _ in range(3)] for _ in range(3)]
    for value,(i,j) in zip(full,PAIRS):SG[i][j]=SG[j][i]=value
    SL=[[arb(i==j) for j in range(3)] for i in range(3)];SD=[]
    for j in range(3):
        pivot=SG[j][j]-sum((SL[j][k]**2*SD[k] for k in range(j)),arb(0));assert pivot>0
        SD.append(pivot)
        for i in range(j+1,3):SL[i][j]=(SG[i][j]-sum((SL[i][k]*SL[j][k]*SD[k] for k in range(j)),arb(0)))/pivot
    # Full divisor generation is complete before any arithmetic values read.
    ap=ROOT/c['arithmetic_result'];ai=ROOT/c['arithmetic_input'];a=json.loads(ap.read_text());params=json.loads(ai.read_text())
    assert params['t']==c['t'] and params['frequency_centres']==c['frequency_centres']
    assert a['passed'] and a['primary_source']['Gaussian_formula_convention_verified']
    for p,digest in a['source_hashes'].items():assert sha256(Path(p).read_bytes()).hexdigest()==digest,p
    arithmetic=[];differences=[];pointA=[[ZERO]*3 for _ in range(3)]
    for k,(i,j) in enumerate(PAIRS):
        bs=a['generated_matrix'][i][j]['rational_bounds'];value=from_bounds(bs);delta=value-full[k]
        assert delta.contains(0)
        assert not (value-2*full[k]).contains(0),'wrong factor must be rejected'
        lo,hi=map(F,bs);pointA[i][j]=pointA[j][i]=((lo+hi)/2,F(0))
        arithmetic.append(value);differences.append(delta);records[k]['arithmetic_minus_divisor']=dump(delta)
    pointZ=midmatrix(full);pointD=msub(pointA,pointZ)
    assert pointD!=mzero(3,3),'point approximations are not asserted identical'
    # Structural countercontrol: imaginary spectral displacements must NOT
    # be replaced by real ordinates or by positive absolute squares.
    u=20*pi;eta=ar('1/4');quartet=[acb(sign*u,shift*eta) for sign in (-1,1) for shift in (-1,1)]
    hostile=sum(((-acb(t)*z*z).exp() for z in quartet),acb(0))/2
    real_only=2*(-t*u*u).exp()
    assert hostile.imag.contains(0) and hostile.real<0 and real_only>0
    # Fresh native reconstruction with the actual neutron numerator metric.
    pp,np=ROOT/c['proton'],ROOT/c['neutron'];_,pops=parse(json.loads(pp.read_text()))
    neutron=json.loads(np.read_text());ds=[F(x['d']) for x in neutron['coordinates']];nops=[mzero(36,36) for _ in range(3)]
    for r in neutron['arrows']:
        aa,bb,cc,dd=map(F,r['numerator']);assert bb==dd==0
        nops['LGN'.index(r['stage'])][r['target']][r['source']]=(aa/ds[r['source']],cc/ds[r['source']])
    native={}
    for name,ops,metric in (('protonlike',pops,[F(1)]*36),('neutron',nops,[1/x for x in ds])):
        bank=build(name,ops,metric);BA=bank['attach'](pointA);BZ=bank['attach'](pointZ);BD=bank['attach'](pointD)
        for B,G in ((BA,pointA),(BZ,pointZ),(BD,pointD)):assert mm(mm(adj(B),bank['H']),B)==G
        naive=msub(BA,BZ);assert mm(mm(adj(naive),bank['H']),naive)==mzero(3,3)
        assert madd(naive,bank['X'])==BD
        native[name]={'stage_ranks':bank['ranks'],'arithmetic_attachment':sparse(BA),'divisor_attachment':sparse(BZ),
           'difference_attachment':sparse(BD),'signed_form_pullbacks_verified':True,'shared_source_reinserted_for_difference':True,
           'naive_lift_difference_has_zero_form_not_difference_form':True}
    result={'schema':'marici.rh-full-divisor-window.v1','passed':True,'iteration':5,'parameters':c,
      'software':{'python_flint':flint.__version__,'FLINT':flint.__FLINT_VERSION__},
      'certified_positive_ordinate_count':n,'certified_count_ball':str(count_ball),'count_in_cutoff_neighborhood':str(stable_count),
      'complete_window_including_multiplicities_verified':True,'critical_line_verified_only_for_this_window':True,
      'zero_window_certificates':root_records,'spectral_entries':records,
      'independent_full_divisor_positive_LDL_pivots':[dump(x) for x in SD],
      'positivity_certified_only_on_this_three_test_span':True,
      'all_height_zero_count_majorant':{'bound':'N(v)<=(v+3)^2, v>=13','basis':'Jensen and theta-integral completed xi representation',
        'RH_assumed':False,'derivation':'research/voevodsky/rh-full-divisor-window-v1.md'},
      'full_divisor_tail_certified':True,'tail_allows_off_critical_zeros':True,
      'spectral_generation_uses_arithmetic_matrices_or_zeros_from_old_scout':False,
      'arithmetic_and_full_divisor_enclosures_overlap':True,'enclosure_overlap_is_exact_numerical_equality':False,
      'wrong_divisor_factor_rejected':True,'complex_node_negative_control':{'synthetic_not_actual_zeta_divisor':True,
        'signed_half_quartet':str(hostile),'incorrect_real_ordinates':str(real_only)},
      'comparison_midpoint_forms':{'arithmetic':sparse(pointA),'full_divisor':sparse(pointZ),'difference':sparse(pointD)},
      'both_native_comparison_attachments':native,'same_finite_RH_comparison_survives_as_signed_forms_in_both':True,
      'native_triangles_execute_these_analytic_evaluators':False,'all_test_positivity_proved':False,'RH_proved':False,
      'scope':c['scope'],'shared_sources_modified':False,
      'next_obligation':'Operation-bearing analytic completion or native evaluator construction; one finite positive Gaussian span is not the complete RH criterion.'}
    files=[cp,contract,ap,ai,pp,np,Path(__file__),Path(flint.__file__)]
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in files}
    (base/'results/rh-full-divisor-window-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'complete_window_positive_count':n,'full_off_critical_safe_tail_certified':True,
       'independent_full_divisor_packet_enclosed':True,'arithmetic_comparison_consistent':True,
       'same_signed_comparison_in_both':True,'native_analytic_execution':False,'RH_proved':False},indent=2))
if __name__=='__main__':main()
