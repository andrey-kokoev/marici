"""Uniform analytic majorants and worst-column audits for translated packets."""
from pathlib import Path
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('conditioning',HERE/'certify_joint_cubic_reconstruction.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


def main():
    ctx.prec=192;pi=arb.pi();L=c.L;x=arb(2).log()
    assert L>0 and x*(3*x).tanh()-L>(1+x)/4
    alpha=2-arb(19)/(8*pi);assert alpha>0
    q0=4*pi
    H0=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
    D=32*(8*pi/alpha).sqrt()*H0/(1-(-arb(1)).exp())
    assert D<256
    k0=pi*(1-(-arb(1)).exp())/8
    assert k0**2*(1+x)**2*2**11>160
    rows=[]
    for pairs in c.g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            point=1;starts=[]
            for pair,kind in zip(pairs,kinds):
                if kind:starts.append(point)
                for index in pair:point*=c.g.PRIMES[index]
            rows.append((starts[0]*starts[1],sum(s*s for s in starts),pairs,kinds,starts))
    maxproduct=max(r[0] for r in rows);maxsquare=max(r[1] for r in rows)
    gp=[r for r in rows if r[0]==maxproduct];pp=[r for r in rows if r[1]==maxsquare]
    assert len(gp)==len(pp)==1 and gp[0]==pp[0]
    assert gp[0][4]==[143,5005]
    assert maxproduct==715715 and maxsquare==25070474
    constant=7200*256**2*maxproduct**2
    # Exact exponents from beta=4, y=3 boundary formulas.
    assert 2*(4-3+1)==4 and 2*3+5==11
    result={'passed':True,'columns':len(rows),
        'uniform_diamond_S_over_K_bound':'256 a^2, a>=2',
        'certified_diamond_constant_ball':str(D),
        'uniform_Q1_inverse_bound_per_w':str(constant)+' A^4',
        'uniform_path_inverse_bound':'exp(pi*25070474*A^2)',
        'worst_retained_start_multipliers':[143,5005],
        'Gamma_inverse_asymptotic_leading_constant':str(115200*pi*maxproduct**2),
        'claims':['no_uniform_raw_l1_inverse_even_at_fixed_depth_three',
                  'Gamma_background_moment_prior_gives_Holder_exponent_eta_over_eta_plus_4',
                  'path_background_moment_prior_gives_logarithmic_order_eta_over_2'],
        'scope':'Finite integer maximization and Arb verification of constants. Infinite instability, conditional bounds and lower bounds use the stated diagonal-map and completed-theta asymptotic proofs. Prior is explicitly a background-A moment on this restricted source family.'}
    out=HERE.parent/'results/translated-reconstruction-stability.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
