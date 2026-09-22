"""Arb source-lift certificate and a finite-description all-depth tail.

Actual H4 theta norms, not response samples, control the source costs.
All physical w_seam factors remain symbolic in the artifact.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('growth',HERE/'check_translated_cubic_observer_growth.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
f=g.f
ctx.prec=192
pi=arb.pi();CELLS=2048;V=arb(32)


def pos(x):return arb(0).union(x.upper())


def tail_polynomial(q):
    return sum((arb(comb(10,k)*factorial(k))*q**(10-k)/2**(k+1)
                for k in range(11)),arb(0))


def norm_enclosure(a):
    q0=pi*a*a
    assert 3*q0>V # core lies in EVERY actual window with multiplier >=2
    step=V/CELLS;core=arb(0)
    for j in range(CELLS):
        v=(j*step).union((j+1)*step)
        q=q0+v;x=(q/pi).log()/2
        P=(4*q*q-6*q)*(-v).exp()+(64*q*q-24*q)*(-3*q0-4*v).exp()
        ratio=(arb(4)/3)**4*(-7*q).exp()
        assert ratio<1
        P+=pos(4*q*q*81*(-8*q0-9*v).exp()/(1-ratio))
        core+=step*(9*x).exp()*(1+x)**2*P**2/(2*q)
    ratio=(arb(3)/2)**4*(-5*q0).exp()
    H=1+16*(-3*q0).exp()/(1-ratio)
    constant=8*pi**(-arb(9)/2)*H**2
    tail=constant*(-2*V).exp()*tail_polynomial(q0+V)
    enclosed=(core+pos(tail)).sqrt()*(-q0).exp()
    assert enclosed>0
    return enclosed


def main():
    # A coarse analytic bound on the ENTIRE forcing tail from log 2.
    q0=4*pi
    H=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
    global_squared=8*pi**(-arb(9)/2)*H**2*(-2*q0).exp()*tail_polynomial(q0)
    assert global_squared<1
    starts=(2,4,6,10,12,20,60,84,140)
    norms={a:norm_enclosure(a) for a in starts}
    # Uniform per-start enclosures apply to each of the actual finite windows.
    S23=2*norms[2]+norms[4]+norms[6]
    S57=2*norms[12]+norms[60]+norms[84]
    S25=2*norms[2]+norms[4]+norms[10]
    S37=2*norms[20]+norms[60]+norms[140]
    mass0=2*S23*S57;massx=2*S25*S37
    minimum=factorial(6)*(mass0+massx/2) # Q1 minimum divided by w_seam
    assert minimum>0 and minimum<arb('1e-170')
    assert minimum.upper()/minimum.lower()<arb('1.2')
    keys=[((('e',0,1,1),('e',3,7,1),('e',15,31,0)),((),(),(),())),
          ((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),(),(),()))]
    seen=set();visible=[];columns=0
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            cols=[f['relation'](pair,kind) for pair,kind in zip(pairs,kinds)]
            source=f['chain_product'](cols)
            assert not seen.intersection(source);seen.update(source)
            start=0;ds=[]
            for pair,col in zip(pairs,cols):
                ds.append(g.one(f['derivative'](start,col)))
                start|=sum(1<<j for j in pair)
            image=g.join(g.join(ds[0],ds[1]),ds[2])
            row=tuple(image.get(key,0) for key in keys)
            if any(row):visible.append((pairs,kinds,row))
            columns+=1
    assert columns==270
    assert [v[2] for v in visible]==[(1,0),(0,1)]
    v0=f['chain_product']([f['relation']((0,1),1),f['relation']((2,3),1),f['relation']((4,5),0)])
    vx=f['chain_product']([f['relation']((0,2),1),f['relation']((1,3),1),f['relation']((4,5),0)])
    v4=f['chain_product']([f['relation']((2*i,2*i+1),int(i<3)) for i in range(4)])
    assert len(v0)==len(vx)==32 and not set(v0).intersection(vx)
    assert len(v4)==128
    denominator=2**16*factorial(8)*2*4**3
    prefix=[]
    for column,multiplier,wpower in ((v0,Q(1),'0'),(vx,Q(1,2),'0'),(v4,Q(1,denominator),'-1/2')):
        for (word,marks),c in column.items():
            prefix.append({'event_indices':list(word),'marks':list(marks),
                           'rational_coefficient':str(c*multiplier),'w_seam_power':wpower})
    assert len(prefix)==192
    all_tail=Q(1,2**16)/(1-Q(1,2**9))
    after_four=Q(1,2**25)/(1-Q(1,2**11))
    assert all_tail==Q(1,65408)
    assert after_four==Q(1,33538048) and after_four<Q(3,10**8)
    assert Q(1,10**170)+all_tail<Q(1,10**4)
    radius_bounds={}
    for R in (1,2,4,8,16,32):
        k=max(4,(R-1).bit_length())
        ratio=Q(R*R,2**(2*k+1))
        assert ratio<=Q(1,2)
        bound=sum((Q(R**(2*r),2**(r*r)) for r in range(4,k)),Q(0))
        bound+=Q(R**(2*k),2**(k*k))/(1-ratio)
        radius_bounds[str(R)]={'tail_bound_per_w':str(bound),'geometric_start':k}
    result={'passed':True,'arithmetic':'Arb 192 bits; exact rational tail bounds',
        'parameters':{'forcing_beta':4,'source_constraints':['private_0=1','private_cross=1/2'],
                      'source_domain':'J_3; actual-letter and common-path intersection',
                      'cells_per_scaled_norm':CELLS,'scaled_tail_start':32},
        'balls':{'global_H4_norm_squared_upper':str(global_squared),
                 'minimum_Q1_lift_cost_per_w_seam':str(minimum)},
        'forcing_norm_enclosures_by_start':{str(a):str(v) for a,v in norms.items()},
        'claims':{'minimum_cost_positive_and_below_1e_minus_170_per_w':True,
                  'upper_lower_minimum_cost_ratio_below_1_2':True,
                  'entire_infinite_source_Q1_below_1e_minus_4_times_w':True,
                  'depth_four_prefix_Q1_error_below_3e_minus_8_times_w':True},
        'tail_rule':'coefficient(v_r)=w_seam^((3-r)/2)/(2^(r^2)*(2r)!*2*4^(r-1)), r>=4',
        'all_radius_tail_bounds':radius_bounds,'actual_source_basis_columns_checked':columns,
        'finite_prefix':{'initial_arithmetic_vertex':2,'event_primes':[2,3,5,7,11,13,17,19],
                         'terms':prefix},
        'scope':'Certificate for specified exact normalized private data and a specified all-depth source-tail rule. It does not certify arbitrary unknown future data or turn response noise into exact coefficients.'}
    out=HERE.parent/'results/certified-observer-source-lift.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('passed','arithmetic','balls','claims','actual_source_basis_columns_checked')},indent=2))
    print('Exact 192-term prefix and tail rule saved in',out)


if __name__=='__main__':main()
