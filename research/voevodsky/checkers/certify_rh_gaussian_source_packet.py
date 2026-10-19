"""Arb integration and analytic tail enclosures for the existing source packet.
No critical-zero locations are used. Positivity is conditional only on the
specified source-form convention, not on RH. Requires existing python-flint.
"""
from pathlib import Path
from hashlib import sha256
import json,sys
ROOT=Path(__file__).resolve().parents[3]
try:
    from flint import arb,acb,ctx
except ModuleNotFoundError:
    sys.path.insert(0,str(ROOT/'research/flavor/.venv/Lib/site-packages'))
    from flint import arb,acb,ctx
import flint
from check_rh_gaussian_seed_packet import prime_powers

def main():
    cp=ROOT/'research/voevodsky/inputs/rh-gaussian-source-certification-v1.json';c=json.loads(cp.read_text());ctx.prec=c['precision_bits']
    t=arb(1)/10;pi=arb.pi();centres=[arb(a) for a in c['frequency_centres']];N=c['prime_cutoff'];R=c['gamma_cutoff'];n=len(centres)
    tol=arb(c['integration_absolute_tolerance']);I=acb(0,1)
    prime_terms=[(arb(p).log()/arb(k).sqrt(),arb(k).log()) for k,p in prime_powers(N)]
    v=arb(N).log();assert 1/v-arb(1)/2-v/(2*t)<0
    z=v-t
    prime_tail=(t/4).exp()*(2*t*(-z*z/(4*t)).exp()+t*(pi*t).sqrt()*(z/(2*t.sqrt())).erfc())/(2*(pi*t).sqrt())
    assert prime_tail>0 and prime_tail<arb('1e-50')
    prime_radius=arb(0,arb('1e-50'))
    G=[[arb(0) for _ in range(n)] for _ in range(n)];terms=[]
    for i in range(n):
        for j in range(i,n):
            a,b=centres[i],centres[j];xi=(a+b)/2;factor=(-t*(a-b)**2/4).exp()
            endpoint=(t/4-t*xi*xi).exp()*(t*xi).cos()
            def integrand(u,analytic):
                # Meromorphic digamma evaluation returns nonfinite balls at
                # poles; unlike .real, this expression is holomorphic near R.
                psi=((acb(1)/4+I*u/2).digamma()+(acb(1)/4-I*u/2).digamma())/2
                return (-acb(t)*(u-acb(xi))**2).exp()*psi
            # Explicit rational cuts; no floating endpoints in certified calls.
            cut_values=sorted(set([-64,-32,-16,-8,-4,-2,-1,0,1,2,4,8,16,32,64]+[int((int(c['frequency_centres'][i])+int(c['frequency_centres'][j]))//2)]))
            cuts=[acb(k) for k in cut_values];integral=acb(0)
            for left,right in zip(cuts,cuts[1:]):
                value=acb.integral(integrand,left,right,abs_tol=tol,rel_tol=tol,eval_limit=100000,depth_limit=40)
                assert value.is_finite(),'certified integration inconclusive'
                integral+=value
            assert integral.imag.contains(0)
            d=arb(R)-abs(xi);assert d>0
            J0=pi.sqrt()*(t.sqrt()*d).erfc()/(2*t.sqrt())
            J2=d*(-t*d*d).exp()/(2*t)+J0/(2*t)
            gamma_tail=2*((10+4*xi*xi)*J0+4*J2)/(4*pi)
            assert gamma_tail>=0 and gamma_tail<arb('1e-70')
            gamma=-pi.log()/(4*(pi*t).sqrt())+integral.real/(4*pi)+arb(0,arb('1e-70'))
            prime=-sum((coef*(-ell*ell/(4*t)).exp()*(xi*ell).cos() for coef,ell in prime_terms),arb(0))/(2*(pi*t).sqrt())+prime_radius
            value=factor*(endpoint+gamma+prime)
            assert value.is_finite();G[i][j]=G[j][i]=value
            terms.append({'indices':[i,j],'mixed_gaussian_prefactor':str(factor),'endpoint':str(factor*endpoint),
                          'gamma_with_infinite_tail':str(factor*gamma),'prime_with_infinite_tail':str(factor*prime),
                          'gamma_integral_complex_ball':str(integral),'analytic_gamma_tail_bound':str(gamma_tail),
                          'certified_entry':str(value)})
    L=[[arb(i==j) for j in range(n)] for i in range(n)];D=[]
    for j in range(n):
        d=G[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0))
        assert d>0,f'positive pivot not certified: {j}, {d}'
        D.append(d)
        for i in range(j+1,n):L[i][j]=(G[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/d
    # Comparison with the old scout is a check, not an ingredient of proof.
    oldpath=ROOT/'research/voevodsky/results/rh-gaussian-seed-packet-v1.json';old=json.loads(oldpath.read_text())
    scout=old['calculations'][-1]['arithmetic_packet'];rounded=old['rounded_packet'];roundvals=[[arb(0)]*n for _ in range(n)]
    for i,j,x,y in rounded['entries']:assert y=='0';roundvals[i][j]=arb(x)
    differences=[[str(G[i][j]-roundvals[i][j]) for j in range(n)] for i in range(n)]
    assert all(G[i][j].contains(arb(scout[i][j])) for i in range(n) for j in range(n))
    paths=[cp,ROOT/c['source_formula'],oldpath,Path(__file__),Path(__file__).with_name('check_rh_gaussian_seed_packet.py'),Path(flint.__file__)]
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.rh-gaussian-source-certificate.v1',
        'classification':'interval_certified_finite_arithmetic_packet_positive_definite_in_specified_source_convention',
        'active_obligation':c['active_obligation'],'parameters':c,'arithmetic':'Arb/Acb rigorous ball integration with analytic meromorphic callback',
        'prime_tail_analytic_majorant':str(prime_tail),'prime_tail_added_absolute_radius':'1e-50',
        'gamma_tail_added_absolute_radius_per_scalar_integral_term':'1e-70',
        'term_enclosures':terms,'matrix_enclosure':[[str(x) for x in row] for row in G],
        'ldl_positive_pivots':[str(x) for x in D],'ldl_relative_accuracy_bits':[x.rel_accuracy_bits() for x in D],
        'analytic_arithmetic_packet_positive_definite':True,'scout_values_contained_in_certificate':True,
        'difference_from_rational_rounding_enclosures':differences,
        'gamma_error_and_infinite_tail_certified':True,'prime_infinite_tail_certified':True,
        'zero_side_exhaustion_certified':False,'external_explicit_formula_authority_verified':False,
        'seed_face_operation_attachment_constructed':False,'RH_proved':False,
        'source_hashes':{str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in paths},'shared_sources_or_stores_modified':False}
    out=ROOT/'research/voevodsky/results/rh-gaussian-source-certification-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','positive_pivots':result['ldl_positive_pivots'],'prime_tail_bound':str(prime_tail),
                     'analytic_packet_certified':True,'RH_proved':False},indent=2))
if __name__=='__main__':main()
