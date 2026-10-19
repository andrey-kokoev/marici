"""Exact SU(2) pilot regressions; all-spin claims are the packet's written proofs."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-spectral-scope-su2.v1.json'
NOTE='research/kitaev/yang-mills-spectral-scope-su2-v1.md'
OUT=ROOT/'research/kitaev/results/yang-mills-spectral-scope-su2-v1.json'
I=(F(1),F(0),F(0),F(0))
def mul(a,b):
    w,x,y,z=a;v,r,s,t=b
    return (w*v-x*r-y*s-z*t,w*r+x*v+y*t-z*s,w*s-x*t+y*v+z*r,w*t+x*s-y*r+z*v)
def inv(a):return (a[0],-a[1],-a[2],-a[3])
def prod(xs):
    a=I
    for b in xs:a=mul(a,b)
    return a
def require(ok,msg):
    if not ok:raise ValueError(msg)
def digest(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def report():
    c=json.loads((ROOT/CONTRACT).read_text())
    require(c['target']['group']=='SU(2)' and all(v is False for v in c['boundary'].values()),'scope promotion')
    qs=[I,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
    for q in qs:require(mul(q,inv(q))==I,'unit quaternion')
    gauge_cases=0
    for r in range(6):
        links=[qs[(r+k)%6] for k in range(4)];w=prod(links)
        # Tree gauge puts first three links to identity, keeping the actual loop product.
        gauges=[I,links[0],prod(links[:2]),prod(links[:3])]
        fixed=[mul(mul(gauges[k],links[k]),inv(gauges[(k+1)%4])) for k in range(4)]
        require(fixed[:3]==[I,I,I] and fixed[3]==w,'tree-gauge quotient')
        for s in range(6):
            g=[qs[(s+2*k)%6] for k in range(4)]
            changed=[mul(mul(g[k],links[k]),inv(g[(k+1)%4])) for k in range(4)]
            expected=mul(mul(g[0],w),inv(g[0]));require(prod(changed)==expected,'ordered gauge holonomy')
            require(prod(changed)[0]==w[0],'fundamental trace invariance');gauge_cases+=1
    require(mul(qs[1],qs[2])!=mul(qs[2],qs[1]),'commutative-order hostile')
    spectrum=[{'n':n,'spin':str(F(n,2)),'four_link_casimir':str(4*F(n,2)*(F(n,2)+1))} for n in range(33)]
    require(all(F(r['four_link_casimir'])==r['n']*(r['n']+2) for r in spectrum),'Casimir normalization')
    for n in range(1,33):require(n*(n+2)>=3,'electric Poincare bound')
    # Exact character recurrence: chi_1*chi_n=chi_(n+1)+chi_(n-1), chi_-1=0.
    # W=1-chi_1/2 is tridiagonal and positive; finite supported coefficient tests.
    tests=0
    for x in range(-2,3):
        for y in range(-2,3):
            for z in range(-2,3):
                a=[F(x),F(y),F(z)];wnorm=sum(t*t for t in a)-sum(a[k]*a[k+1] for k in range(2))
                require(wnorm>=0,'nonnegative magnetic multiplication control')
                electric=sum(F(n*(n+2))*a[n]*a[n] for n in range(3))
                require(electric>=3*(a[1]**2+a[2]**2),'full coefficient norm vs energy');tests+=1
    # The first odd character is missed by a center-even projection, and constant vacuum is moved.
    center_hostile={'state':'chi_1','norm_squared':'1','electric_energy_over_kappa':'3','even_reader_norm_squared':'0'}
    magnetic=[]
    for lam in [F(0),F(1,2),F(1),F(2),F(3),F(4)]:
        magnetic.append({'kappa':'1','lambda':str(lam),'gap_lower_bound':str(3-lam),'positive_certificate':lam<3,'constant_vacuum_residual_squared':str(lam*lam/4)})
    require(magnetic[2]['constant_vacuum_residual_squared']=='1/4','unchanged-vacuum hostile')
    scaling=[]
    for g2 in [F(4),F(2),F(1),F(1,2),F(1,4)]:
        k=g2/2;lam=2/g2
        require(lam/k==4/g2**2,'scale ratio')
        scaling.append({'a':'1','g_squared':str(g2),'lambda_over_kappa':str(lam/k),'certified_gap_bound':str(3*k-lam),'positive':lam<3*k})
    require(scaling[0]['positive'] and not scaling[-1]['positive'],'strong-to-weak certificate failure')
    return {'schema':'marici.yang-mills-spectral-scope-su2-result.v1','passed':True,'scope_gate':'selected_definition_and_bounded_source_theorem','verification':'exact_rational_controls_plus_written_imported_harmonic_analysis','gauge_cases':gauge_cases,'electric_characters_checked':spectrum,'coefficient_regressions':tests,'center_even_hostile':center_hostile,'magnetic_bounds':magnetic,'scale_controls':scaling,'source_hashes':{p:digest(p) for p in [CONTRACT,NOTE,'research/kitaev/checkers/check_yang_mills_spectral_scope.py']},'Yang_Mills_proved':False,'continuum_gap_proved':False,'finite_gauge_source_gate_closed':False,'atomic_source_selected':False}
if __name__=='__main__':
    r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':r['passed'],'gauge_cases':r['gauge_cases'],'coefficient_regressions':r['coefficient_regressions'],'electric_gap':'3*kappa','magnetic_gap_lower_bound':'3*kappa-lambda','continuum_gap_proved':False},indent=2))
