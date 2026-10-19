"""Keep full native source dynamics in a common metric-sphere action.

L=1/2 ||D_t z||² - <z,K z>, ||z||=1; internal phase charge +1.
H=-Delta_S/2 + <z,K z>. Exact source PSD checks and Haar-moment
variational bounds, not eigenvalues guessed from tr(K).
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,read_operator,product,sharp,integer_trace,plus,scaled,tr


def field(values,masks):
    c=[F(0)]*16
    for x,m in zip(values,masks):c[m]=F(x)
    return A(tuple(c))
def sign_real(x):
    if any(x.c[8:]):raise ValueError('Nonreal Hermitian pivot')
    terms=[(i,c) for i,c in enumerate(x.c[1:8],1) if c]
    a=x.c[0]
    if not terms:return (a>0)-(a<0)
    if len(terms)!=1:raise ValueError('Pivot outside single-radical sign checker')
    mask,b=terms[0];rad=1
    for bit,p in ((1,2),(2,3),(4,5)):
        if mask&bit:rad*=p
    if a>=0 and b>0:return 1
    if a<=0 and b<0:return -1
    if a>0:return 1 if a*a>rad*b*b else -1
    return 1 if rad*b*b>a*a else -1

def positive_rank(K,metric):
    n=len(metric);M=[[K.get((i,j),ZERO)*A(metric[i]) for j in range(n)] for i in range(n)]
    assert all(M[i][j]==M[j][i].flip(8) for i in range(n) for j in range(n))
    rank=0
    for k in range(n):
        pivot=M[k][k];s=sign_real(pivot)
        if s<0:raise AssertionError('Negative source energy direction')
        if s==0:
            assert all(M[k][j]==ZERO for j in range(k+1,n));continue
        rank+=1;inv=pivot.inverse()
        for i in range(k+1,n):
            if M[i][k]==ZERO:continue
            for j in range(i,n):
                M[i][j]=M[i][j]-M[i][k]*inv*M[k][j]
                M[j][i]=M[i][j].flip(8)
    return rank


def rational(x):
    assert all(c==0 for c in x.c[1:]);return x.c[0]

def main():
    base=ROOT/'research/voevodsky';nativepath=base/'results/native_operation_energy_lift_store.json';native=json.loads(nativepath.read_text())['carriers']
    ep=base/'results/electron_tetrahedral_spinor_store.json';electron=json.loads(ep.read_text())
    bridgepath=ROOT/'research/strominger/results/neutron-arrow-native-bridge.json';bridge=json.loads(bridgepath.read_text())
    assert bridge['status']=='passed'
    for p,h in bridge['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    results={};checks={}
    for name,key in (('proton','proton'),('neutron','belt'),('electron',None)):
        if key:
            row=native[key];metric=[1/F(x) for x in row['metric_denominators']];n=len(metric)
            K={(i,j):field(v,[0,1,10,11])/4 for i,j,v in row['entries']}
            N={(i,j):field(v,[0,1,10,11]) for i,j,v in row['return_entries']}
        else:
            n=8;metric=[F(1)]*n;ops={s:{} for s in 'LGN'}
            for r in electron['arrows']:ops[r['stage']][r['target'],r['source']]=field([x for pair in r['weight'] for x in pair],[0,2,8,10])
            N=ops['N'];I={(i,i):ONE for i in range(n)}
            K=plus(scaled(A(3),I),scaled(A(-1),ops['L']),scaled(A(-2),N))
        assert sharp(K,metric)==K and sharp(N,metric)==N and product(N,N)==N and product(K,N)=={}
        nullity=n-positive_rank(K,metric)
        assert nullity==integer_trace(N)
        t=rational(tr(K));t2=rational(tr(product(K,K)))
        # Full sphere S^(2n-1). Harmonic degree l has kinetic energy
        # l(l+2n-2)/2. Internal phase weight +1 has minimum l=1.
        lower=F(2*n-1,2)
        # Normalized trial f(z)=<v,z>, v in ker K. Complex sphere moments
        # E|z_i|²=1/n; E|z_i|²|z_j|²=(1+delta_ij)/(n(n+1)).
        # Ratio <f,Vf>/<f,f> = tr K/(n+1); no dropped native directions.
        assert F(2,n*(n+1))+(n-1)*F(1,n*(n+1))==F(1,n)
        potential_trial=t/(n+1);upper=lower+potential_trial
        variance=((n+1)*t2-t*t)/((n+1)**2*(n+2))
        assert variance>0 # first harmonic is not an eigenstate of V or H
        results[name]={'full_complex_dimension':n,'native_zero_dimension':nullity,'native_energy_trace':str(t),'native_energy_squared_trace':str(t2),
                       'occupied_energy_lower':str(lower),'occupied_energy_upper':str(upper),'trial_potential_expectation':str(potential_trial),
                       'trial_potential_variance':str(variance),'bounds_not_eigenvalues':True}
        checks[name+'_exact_metric_PSD_and_native_kernel']=True
        checks[name+'_full_space_variational_bound']=True
        checks[name+'_trial_is_not_silently_treated_as_eigenstate']=True
    pl,pu=F(results['proton']['occupied_energy_lower']),F(results['proton']['occupied_energy_upper'])
    el,eu=F(results['electron']['occupied_energy_lower']),F(results['electron']['occupied_energy_upper'])
    bound=[pl/eu,pu/el]
    refspecpath=base/'contracts/source-gauss-operator-charging.v1.json';refspec=json.loads(refspecpath.read_text());ref=refspec['held_out_reference'];refpath=ROOT/ref['path']
    assert hashlib.sha256(refpath.read_bytes()).hexdigest()==ref['sha256']
    rp=F(json.loads(refpath.read_text())['inputs']['proton_me'])
    assert bound[1]<rp
    checks['proton_electron_hierarchy_excluded_at_shared_fixture']=True
    report={'status':'passed','action':'L=1/2||D_t z||_metric^2-<z,Kz>_metric on full unit sphere; H=-Delta_S/2+<z,Kz>; conserved internal phase charge +1',
            'empty_energy':'0','common_coefficients':{'hbar':'1','F_squared':'1','source_potential_multiplier':'1'},
            'source_K':'Actual proton/belt native operation energy in prior E_star units; electron native (I-L)+2(I-N) in same declared unit',
            'carriers':results,'proton_per_electron_interval':list(map(str,bound)),'checks':checks,
            'disposition':'Native dynamics retained and all occupied energies positive, but proton/electron ratio is at most 5.072072... at this common fixture. No exact ordering between proton and neutron is certified by these overlapping bounds.',
            'scope':'Chosen full normalized-amplitude action and Laplace-Beltrami quantization. These bounds do not exclude other common kinetic/potential ratios or a different sourced configuration space.'}
    paths=[Path(__file__).resolve(),nativepath,ep,bridgepath,refspecpath,refpath,Path(__file__).with_name('assemble_metric_coefficient_protocol.py'),base/'checkers/check_pentachoron_spin_interfaces.py']
    report['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out=ROOT/'research/strominger/results/full-source-kinetic-action.json';out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2))

if __name__=='__main__':main()
