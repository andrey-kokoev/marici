"""Certified conditioning of all 270 mixed private cubic scalar readings."""
from pathlib import Path
from functools import lru_cache
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

base=load('source_norms','certify_observer_source_lift.py')
g=base.g
ctx.prec=192
pi=arb.pi();T=arb(32);CELLS=2048


def logarithmic_derivative():
    N=4096;s=arb(7)/2
    sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
    for p in range(2,int(N**0.5)+1):
        if sieve[p]:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    total=arb(0)
    for p in range(2,N+1):
        if not sieve[p]:continue
        n=p
        while n<=N:
            total+=arb(p).log()*arb(n)**(-s);n*=p
    total+=base.pos(arb(N)**(1-s)*(arb(N).log()/(s-1)+1/(s-1)**2))
    return 1/s+1/(s-1)-pi.log()/2+(s/2).digamma()/2-total


L=logarithmic_derivative()
assert arb(2).log()*(3*arb(2).log()).tanh()>L


@lru_cache(None)
def scaled_residual(a):
    # Encloses exp(pi*a^2) (J_F-L X_F) for EVERY window [a,p*a], p>=2.
    q0=pi*a*a;assert 3*q0>T
    step=T/CELLS;K=arb(0)
    for j in range(CELLS):
        v=(j*step).union((j+1)*step);q=q0+v;x=(q/pi).log()/2
        density=(2*q-3)*(-v).exp()+(32*q-12)*(-3*q0-4*v).exp()
        ratio=(arb(4)/3)**4*(-7*q).exp()
        density+=base.pos(2*q*81*(-8*q0-9*v).exp()/(1-ratio))
        density*=(x/2).exp()
        K+=step*(x*(3*x).sinh()-L*(3*x).cosh())*density
    H=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
    factor=2*pi**(-arb(7)/4)*H*(-T).exp();q=q0+T
    Xtail=factor*(q**3+3*q**2+6*q+6)
    Jtail=factor*(q**4+4*q**3+12*q**2+24*q+24)
    K+=base.pos(Jtail+abs(L)*Xtail)
    assert K>0
    return K


@lru_cache(None)
def norm(a):return base.norm_enclosure(a)


@lru_cache(None)
def diamond_ratio(a,p,q):
    # S(a;p,q)/(J_[a,pa]-L X_[a,pa]); shared exponential cancels.
    scaled_S=(2*norm(a)+norm(p*a)+norm(q*a))*(pi*a*a).exp()
    return scaled_S/scaled_residual(a)


def main():
    load('kernel_audit','check_joint_cubic_observation_kernel.py').main()
    rows=[]
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            point=2;ratios=[];Ks=[];starts=[];physical_pairs=[]
            for pair,kind in zip(pairs,kinds):
                p,q=(g.PRIMES[j] for j in pair);physical_pairs.append((p,q))
                if kind:
                    ratios.append(diamond_ratio(point,p,q))
                    Ks.append(scaled_residual(point));starts.append(point)
                point*=p*q
            # nu_j/w=2 S_A S_B, E_j=2 h^2 K_A K_B, h^2=1/10.
            gamma=7200*ratios[0]*ratios[1]
            logpath=(pi*sum(a*a for a in starts)+arb(32).log()
                     -(Ks[0]*Ks[1]/5).log())/arb(10).log()
            rows.append({'pairs':physical_pairs,'kinds':kinds,'starts':starts,
                         'gamma':gamma,'logpath':logpath})
    assert len(rows)==270
    gamma_winners=[i for i,r in enumerate(rows)
                   if all(i==j or r['gamma'].lower()>s['gamma'].upper()
                          for j,s in enumerate(rows))]
    path_winners=[i for i,r in enumerate(rows)
                  if all(i==j or r['logpath'].lower()>s['logpath'].upper()
                         for j,s in enumerate(rows))]
    assert len(gamma_winners)==len(path_winners)==1
    winner=rows[gamma_winners[0]];pathwinner=rows[path_winners[0]]
    C=winner['gamma'];logC=pathwinner['logpath']
    assert C.upper()/C.lower()<arb('1.5')
    assert logC>arb(100000000)
    # A rational acquisition budget, conservatively rounded by a decade.
    power=1
    while not C<arb(10)**power:power+=1
    assert C<arb(10)**power
    budget_exponent=power+8
    result={'passed':True,'arithmetic':'Arb 192 bits; complete-cell quadrature and analytic tails',
        'parameters':{'background':2,'spectral_point':'3i','forcing_beta':4,
                      'receiver_gamma':2,'cells':CELLS,'scaled_cutoff':32,'euler_cutoff':4096},
        'source_columns':len(rows),'forcing_starts':norm.cache_info().currsize,
        'residual_starts':scaled_residual.cache_info().currsize,
        'L':str(L),'exact_inverse_formula':'C_R/w=7200 R^6 max_j (S_A/K_A)(S_B/K_B)',
        'Q1_inverse_norm_per_w_seam':str(C),
        'Q1_inverse_upper_bound_power_of_ten':power,
        'Q1_norm_enclosure_ratio_below_1_5':True,
        'maximizing_Gamma_column':{'pairs':winner['pairs'],'kinds':winner['kinds'],'starts':winner['starts']},
        'log10_unweighted_path_inverse_norm':str(logC),
        'maximizing_path_column':{'pairs':pathwinner['pairs'],'kinds':pathwinner['kinds'],'starts':pathwinner['starts']},
        'scalar_l1_noise_sufficient_for_Q1_error_below_1e_minus_8_w':'1e-'+str(budget_exponent),
        'scope':'Fixed 270-row unscaled scalar protocol on the two-feature cubic packet. Noise is TOTAL l1 scalar acquisition error, not per-row error. Exact calibration is assumed; implementation/calibration errors must enter that same error budget. No all-depth stability claim.',
        'row_enclosures':[{'pairs':r['pairs'],'kinds':r['kinds'],
                           'Gamma_inverse_ratio_per_w':str(r['gamma']),
                           'log10_path_inverse_ratio':str(r['logpath'])} for r in rows]}
    out=HERE.parent/'results/certified-joint-cubic-reconstruction.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='row_enclosures'},indent=2))


if __name__=='__main__':main()
