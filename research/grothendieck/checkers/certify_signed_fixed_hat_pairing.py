"""Direct signed fixed-hat pairings via digamma and von Mangoldt kernels.

No projection enlargement. Prime powers through N; a proved Chebyshev tail,
whole-cell Taylor bounds for the archimedean integral, and an origin bound.
"""
from pathlib import Path
from fractions import Fraction as Q
from bisect import bisect_right
import importlib.util,json,hashlib
from flint import arb,arb_series,acb,acb_series,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
quad=module('quad',HERE/'refine_theta_mass_quadrature.py')
def rat(p):return arb(p[0])/arb(p[1])
def ends(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def enc(x):
    a,b=ends(x);return {'lower':str(a),'upper':str(b),'display':x.str(24)}
def upper(x):return arb(x.upper())
def sym(x):return (-upper(x)).union(upper(x))
def ball(q):return arb(q.numerator)/q.denominator
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def compute(N=1000000,bits=192,mesh_divisions=32):
    assert type(N) is int and N>=1000
    assert type(mesh_divisions) is int and mesh_divisions>=16
    ctx.prec=bits;ctx.cap=5
    path=OUT/'time-bin-cubic-observer.json';filters=json.loads(path.read_text(encoding='utf-8'))['filters']
    times=[rat(p) for p in filters['nodes']];tf=[float(x) for x in times]
    rational_times=[Q(int(p[0]),int(p[1])) for p in filters['nodes']]
    s=arb(7)/2;beta=arb(3)/2;a=s-1;lam=s+beta-1;d=s-beta
    assert times[0]==0 and times[-1]==64
    values=[];slopes=[]
    for side in (0,1):
        f=filters['bulk'][side];normalizer=rat(f['normalizer']);assert normalizer>0
        vs=[arb(n)/filters['nodal_denominator']/normalizer for n in f['nodal_numerators']]
        assert vs[-1]==0
        values.append(vs);slopes.append([(z-y)/(hi-lo) for lo,hi,y,z in zip(times,times[1:],vs,vs[1:])])
    # Exact primitives of linear hats. T_i is the right tail with rate 4;
    # J_i is the left integral with rate -2.
    T=[arb(0)]*len(times);J=[arb(0)]*len(times)
    for i in range(len(times)-2,-1,-1):
        b=slopes[0][i];lo,hi=times[i:i+2];p,z=values[0][i:i+2]
        T[i]=T[i+1]+(-lam*lo).exp()*(p/lam+b/lam**2)-(-lam*hi).exp()*(z/lam+b/lam**2)
    for i in range(len(times)-1):
        b=slopes[1][i];lo,hi=times[i:i+2];p,z=values[1][i:i+2]
        J[i+1]=J[i]+(d*hi).exp()*(z/d-b/d**2)-(d*lo).exp()*(p/d-b/d**2)
    B0=T[0]
    cp=[T[i+1]-(-lam*times[i+1]).exp()*(values[0][i+1]/lam+slopes[0][i]/lam**2) for i in range(len(times)-1)]
    cm=[J[i]-(d*times[i]).exp()*(values[1][i]/d-slopes[1][i]/d**2) for i in range(len(times)-1)]
    def kernel(u,i):
        pp=values[0][i]+slopes[0][i]*(u-times[i]);pm=values[1][i]+slopes[1][i]*(u-times[i])
        if i==0:
            # Enforce the exact zero at the origin before any evaluation.
            kp=B0*((-s*u).exp()-(a*u).exp())+(values[0][0]/lam+slopes[0][0]/lam**2)*((a*u).exp()-(-beta*u).exp())-slopes[0][0]/lam*u*(-beta*u).exp()
            km=(values[1][0]/d-slopes[1][0]/d**2)*((-s*u).exp()-(-beta*u).exp())-slopes[1][0]/d*u*(-beta*u).exp()
        else:
            kp=B0*(-s*u).exp()-(-beta*u).exp()*(pp/lam+slopes[0][i]/lam**2)-cp[i]*(a*u).exp()
            km=-cm[i]*(-s*u).exp()-(-beta*u).exp()*(pm/d-slopes[1][i]/d**2)
        return kp,km
    # Removable singularity at u=0. Divided exponentials are bounded using
    # (exp(r*u)-exp(t*u))/u=(r-t)*integral_0^1 exp((t+v*(r-t))*u) dv.
    eps=arb(1)/2**28;assert eps<times[1]
    u=arb(0).union(eps)
    def divided(r,t):return (r-t)*(r.union(t)*u).exp()
    ratio=(arb(1)/2).union((2*eps).exp()/2)
    kp=ratio*(B0*divided(-s,a)+(values[0][0]/lam+slopes[0][0]/lam**2)*divided(a,-beta)-slopes[0][0]/lam*(-beta*u).exp())
    km=ratio*((values[1][0]/d-slopes[1][0]/d**2)*divided(-s,-beta)-slopes[1][0]/d*(-beta*u).exp())
    arch=[eps*kp,eps*km];origin=list(arch);error=[arb(0),arb(0)];count=0
    for i in range(len(times)-1):
        left_q=max(Q(1,2**28),rational_times[i]);hi_q=rational_times[i+1]
        while left_q<hi_q:
            right_q=min(hi_q,left_q+Q(1,mesh_divisions),left_q*Q(mesh_divisions+1,mesh_divisions))
            lo=ball(left_q);right=ball(right_q)
            def integrand(x):
                den=1-(-2*x).exp()
                return tuple(v/den for v in kernel(x,i))
            vals,errs=quad.integrate_cell(integrand,lo,right)
            for k in (0,1):arch[k]+=vals[k];error[k]+=errs[k]
            left_q=right_q;count+=1
    tail_integral=(-s*times[-1]).exp()/(s*(1-(-2*times[-1]).exp()))
    arch[0]+=sym(abs(B0)*tail_integral);arch[1]+=sym(abs(J[-1])*tail_integral)
    print('Archimedean cells:',count,flush=True)
    sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
    from math import isqrt
    for p in range(2,isqrt(N)+1):
        if sieve[p]:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    sums=[arb(0),arb(0)];psi=arb(0);terms=0
    for p in range(2,N+1):
        if not sieve[p]:continue
        lp=arb(p).log();n=p;k=1
        while n<=N:
            u=k*lp;i=bisect_right(tf,float(u))-1
            assert 0<=i<len(times)-1 and times[i]<=u<=times[i+1]
            root=arb(n).sqrt();ns=1/(n**3*root);nb=1/(n*root)
            pp=values[0][i]+slopes[0][i]*(u-times[i]);pm=values[1][i]+slopes[1][i]*(u-times[i])
            sums[0]+=lp*(B0*ns-nb*(pp/lam+slopes[0][i]/lam**2)-cp[i]*n**2*root)
            sums[1]+=lp*(-cm[i]*ns-nb*(pm/d-slopes[1][i]/d**2))
            psi+=lp;terms+=1;n*=p;k+=1
    logN=arb(N).log();i=bisect_right(tf,float(logN))-1
    assert times[i]<=logN<=times[i+1]
    maxima=[]
    for k in (0,1):
        here=values[k][i]+slopes[k][i]*(logN-times[i])
        maxima.append(max([upper(abs(here))]+[upper(abs(v)) for v in values[k][i+1:]]))
    currentJ=J[i]+(d*logN).exp()*((values[1][i]+slopes[1][i]*(logN-times[i]))/d-slopes[1][i]/d**2)-(d*times[i]).exp()*(values[1][i]/d-slopes[1][i]/d**2)
    # psi(x)<=2 log(2)*x+log(x)+log(2), from binomial recursion.
    def mangoldt_tail(power):
        n=arb(N)
        bound=2*arb(2).log()*power/(power-1)*n**(1-power)+n**(-power)*(logN+1/power+arb(2).log()-psi)
        assert bound>0
        return upper(bound)
    ts=mangoldt_tail(s);tb=mangoldt_tail(beta)
    prime_tail=[abs(B0)*ts+maxima[0]/lam*tb,
                (abs(currentJ)+maxima[1]*arb(N)**2/d)*ts+maxima[1]/d*tb]
    z=acb_series([acb(s),1],2).zeta();Ds=(acb(s)/2).digamma().real/2-arb.pi().log()/2+(z[1]/z[0]).real
    bulk_base=[2*Ds*B0+arch[0]+sums[0],arch[1]+sums[1]]
    bulk=[bulk_base[0]+sym(prime_tail[0]),bulk_base[1]+sym(prime_tail[1])]
    weak=filters['weak'];wn=rat(weak['normalizer']);assert wn>0
    wv=[arb(n)/filters['nodal_denominator']/wn for n in weak['nodal_numerators']]
    h=arb(0)
    for lo,hi,p,z in zip(times,times[1:],wv,wv[1:]):
        slope=(z-p)/(hi-lo)
        h+=(-lam*lo).exp()*(p/lam+slope/lam**2)-(-lam*hi).exp()*(z/lam+slope/lam**2)
    assert h>0
    direction=[rat(p) for p in filters['endpoint_direction']]
    endpoint=(arb(2)/5*direction[0]+arb(2)/7*direction[1])/rat(filters['endpoint_normalizer'])
    C=bulk[0]+bulk[1]+endpoint+h
    return C,{'analytic_parameters':{'s':'7/2','beta':'3/2','lambda':'4','d':'2'},'N':N,'bits':bits,'mesh_divisions':mesh_divisions,'origin_cutoff':'1/268435456','archimedean_cells':count,'prime_power_terms':terms,
              'filter_sha256':sha(path),'bulk_pairings':[enc(x) for x in bulk],'bulk_before_prime_tail':[enc(x) for x in bulk_base],
              'archimedean_integrals':[enc(x) for x in arch],'origin_integrals':[enc(x) for x in origin],
              'quadrature_remainder_bounds':[enc(x) for x in error],
              'finite_prime_sums':[enc(x) for x in sums],'prime_tail_bounds':[enc(x) for x in prime_tail],
              'psi_N':enc(psi),'mangoldt_tail_s':enc(ts),'mangoldt_tail_beta':enc(tb),
              'future_hat_suprema':[enc(x) for x in maxima],'J_at_log_N':enc(currentJ),'J_at_64':enc(J[-1]),'D_s':enc(Ds),'B0':enc(B0),
              'endpoint':enc(endpoint),'h':enc(h),'C':enc(C)}
if __name__=='__main__':
    C,result=compute()
    (OUT/'signed-fixed-hat-pairing.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Direct signed C:',C.str(24))
