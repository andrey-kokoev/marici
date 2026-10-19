"""Actual arithmetic Gaussian packet, finite zero scout and exact rounded attachment.

Existing read-only mpmath dependency is used; no provisioning or source mutation.
Numerical consistency checks are not rigorous error certificates or an RH proof.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
from check_proton_native_task_catalogue import ROOT,mm,adj,madd,rank,sparse,vector
from check_proton_single_probe_cycle import inverse
from check_proton_unitary_probe_repair import restore
from verify_proton_native_task_catalogue import realify,multiply as qmm
try:
    import mpmath as mp
except ModuleNotFoundError:
    sys.path.insert(0,str(ROOT/'research/flavor/.venv/Lib/site-packages'))
    import mpmath as mp


def prime_powers(N):
    prime=[True]*(N+1);prime[0]=prime[1]=False
    for p in range(2,int(N**.5)+1):
        if prime[p]:
            for n in range(p*p,N+1,p):prime[n]=False
    terms=[]
    for p in range(2,N+1):
        if prime[p]:
            n=p
            while n<=N:terms.append((n,p));n*=p
    return sorted(terms)

def calculate(contract,dps):
    with mp.workdps(dps):
        t=mp.mpf(contract['t']);centres=list(map(mp.mpf,contract['frequency_centres']));N=contract['prime_cutoff']
        terms=[(mp.log(p)/mp.sqrt(n),mp.log(n)) for n,p in prime_powers(N)]
        n=len(centres);end=[[mp.mpf(0)]*n for _ in range(n)];gam=[[mp.mpf(0)]*n for _ in range(n)];pri=[[mp.mpf(0)]*n for _ in range(n)]
        for i,a in enumerate(centres):
            for j in range(i,n):
                b=centres[j];xi=(a+b)/2;factor=mp.exp(-t*(a-b)**2/4)
                e=mp.exp(t/4-t*xi**2)*mp.cos(t*xi)
                def integrand(u):return mp.exp(-t*(u-xi)**2)*mp.re(mp.digamma(mp.mpf(1)/4+mp.j*u/2))
                width=10/mp.sqrt(t)
                cuts=sorted(set([xi-width,xi,xi+width]+[mp.mpf(v) for v in (-64,-32,-16,-8,-4,-2,-1,0,1,2,4,8,16,32,64)]))
                integral=mp.quad(integrand,[-mp.inf]+cuts+[mp.inf])
                g=-mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t))+integral/(4*mp.pi)
                p=-mp.fsum(c*mp.exp(-ell**2/(4*t))*mp.cos(xi*ell) for c,ell in terms)/(2*mp.sqrt(mp.pi*t))
                end[i][j]=end[j][i]=factor*e;gam[i][j]=gam[j][i]=factor*g;pri[i][j]=pri[j][i]=factor*p
        arithmetic=[[end[i][j]+gam[i][j]+pri[i][j] for j in range(n)] for i in range(n)]
        zeros=[mp.zetazero(k) for k in range(1,contract['zero_count']+1)];ordinates=[mp.im(z) for z in zeros]
        spectral=[[mp.fsum((mp.exp(-t*((u-a)**2+(u-b)**2)/2)+mp.exp(-t*((-u-a)**2+(-u-b)**2)/2))/2 for u in ordinates) for b in centres] for a in centres]
        # Lambda(n)<=log n, |cos|<=1 and a decreasing majorant for n>=N.
        # Integral_N^infty log(x)/sqrt(x)*exp(-log(x)^2/(4t)) dx.
        v=mp.log(N);assert 1/v-mp.mpf('0.5')-v/(2*t)<0
        z=v-t
        integral_bound=mp.exp(t/4)*(2*t*mp.exp(-z*z/(4*t))+t*mp.sqrt(mp.pi*t)*mp.erfc(z/(2*mp.sqrt(t))))
        prime_tail=integral_bound/(2*mp.sqrt(mp.pi*t))
        eig=mp.eigsy(mp.matrix(arithmetic),eigvals_only=True)
        stringify=lambda M:[[mp.nstr(x,dps) for x in row] for row in M]
        return {'precision':dps,'endpoint':stringify(end),'gamma':stringify(gam),'prime_partial_sum':stringify(pri),
          'arithmetic_packet':stringify(arithmetic),'finite_zero_packet':stringify(spectral),
          'max_arithmetic_zero_difference':mp.nstr(max(abs(arithmetic[i][j]-spectral[i][j]) for i in range(n) for j in range(n)),dps),
          'analytic_prime_tail_majorant_numerical_value':mp.nstr(prime_tail,dps),
          'critical_line_zero_samples':[{'index':k+1,'real_part':mp.nstr(mp.re(z),dps),'ordinate':mp.nstr(mp.im(z),dps)} for k,z in enumerate(zeros)],
          'arithmetic_eigenvalue_scout':[mp.nstr(x,dps) for x in eig],
          'prime_power_terms':len(terms)}


def main():
    cp=ROOT/'research/voevodsky/inputs/rh-gaussian-seed-packet-v1.json';contract=json.loads(cp.read_text())
    signed_path=ROOT/'research/voevodsky/results/rh-seed-signed-attachment-v1.json';signed=json.loads(signed_path.read_text())
    for p,h in signed['source_hashes'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    results=[calculate(contract,p) for p in contract['precisions']]
    with mp.workdps(max(contract['precisions'])):
        low,high=results;G=[[mp.mpf(x) for x in row] for row in high['arithmetic_packet']]
        delta=max(abs(mp.mpf(low['arithmetic_packet'][i][j])-G[i][j]) for i in range(3) for j in range(3))
        # Numerical gate only. Failure is not evidence for or against RH.
        assert delta<mp.mpf('1e-30'), 'precision convergence failed'
        residual=mp.mpf(high['max_arithmetic_zero_difference'])
        assert residual<mp.mpf('1e-30'), 'finite source/zero scout comparison failed'
        digits=contract['rounding_decimal_places'];den=10**digits
        rounded=[[(F(int(mp.nint(z*den)),den),F(0)) for z in row] for row in G]
        rounding=max(abs(G[i][j]-mp.mpf(rounded[i][j][0].numerator)/rounded[i][j][0].denominator) for i in range(3) for j in range(3))
        delta_string=mp.nstr(delta,60);rounding_string=mp.nstr(rounding,60)
    X=[r[:3] for r in restore(signed['native_source_basis'])];Y=[r[:3] for r in restore(signed['native_sink_basis'])]
    D=mm(adj(X),X);B=madd(X,mm(mm(Y,inverse(D)),rounded))
    prior_path=ROOT/'research/voevodsky/results/proton-native-relationship-structure-v1.json';prior=json.loads(prior_path.read_text())
    K=restore(prior['hermitian_analysis']['K'])
    assert rank(B)==3 and mm(mm(adj(B),K),B)==rounded
    assert qmm(qmm(realify(sparse(adj(B))),realify(sparse(K))),realify(sparse(B)))==realify(sparse(rounded))
    files=[cp,ROOT/contract['source_formula'],signed_path,prior_path,Path(__file__),Path(mp.__file__)]
    hashes={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in files}
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.rh-gaussian-seed-packet.v1',
      'classification':'numerical_arithmetic_packet_and_finite_zero_consistency_with_exact_rounded_signed_attachment',
      'active_obligation':contract['active_obligation'],'parameters':contract,'calculations':results,
      'max_precision_change':delta_string,'max_rounding_change':rounding_string,'rounded_packet':sparse(rounded),'native_attachment':sparse(B),
      'exact_rounded_pullback_verified':True,'independent_rational_pullback_verified':True,
      'gaussian_polarization_identity':'g_i(u)g_j(u)=exp(-t(a_i-a_j)^2/4) exp(-t(u-(a_i+a_j)/2)^2), g_i=exp(-t(u-a_i)^2/2)',
      'source_term_labels_preserved':['endpoint','gamma','prime_partial_sum','analytic_prime_tail_majorant'],
      'numerical_gamma_error_certified':False,'prime_tail_rounding_interval_certified':False,
      'zero_sum_tail_certified':False,'zero_list_exhaustive_off_critical_line':False,
      'external_explicit_formula_verification_completed':False,'seed_face_incidence_or_generator_attachment_constructed':False,
      'RH_proved':False,'source_hashes':hashes,'shared_sources_or_stores_modified':False}
    out=ROOT/'research/voevodsky/results/rh-gaussian-seed-packet-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','precision_change':delta_string,'finite_source_zero_difference':results[-1]['max_arithmetic_zero_difference'],
      'prime_tail_majorant':results[-1]['analytic_prime_tail_majorant_numerical_value'],
      'eigenvalue_scout':results[-1]['arithmetic_eigenvalue_scout'],'exact_rounded_attachment':True,'RH_proved':False},indent=2))
if __name__=='__main__':main()
