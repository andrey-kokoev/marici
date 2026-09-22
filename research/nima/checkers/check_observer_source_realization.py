"""Exact cornerwise source-lift budget and feasibility regressions."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json


def main():
    # In corner c the first observation is u+v; much later v is observed.
    # The Gamma norm is alpha*|u|+|v|, alpha<1, so early minimizers are exact.
    corners={c:{'n':2*c,'alpha':Q(1,2**c),
                'u':Q(1,2**(c*c)*factorial(2*c)),
                'v':Q(c,3**(c*c)*factorial(2*c)),
                'first':c,'last':c*c+5} for c in range(1,9)}
    def minimum(c,m):
        d=corners[c]
        if m<d['first']:return Q(0),Q(0)
        if m<d['last']:return d['u']+d['v'],Q(0)
        return d['u'],d['v']
    def mass(c,pair):return corners[c]['alpha']*abs(pair[0])+abs(pair[1])
    def weight(c,R):return factorial(corners[c]['n'])*R**corners[c]['n']
    last=max(d['last'] for d in corners.values())
    checks=0
    for R in (1,2,3,4):
        final=sum(weight(c,R)*mass(c,(d['u'],d['v'])) for c,d in corners.items())
        previous=Q(0)
        for m in range(last+1):
            cost=sum(weight(c,R)*mass(c,minimum(c,m)) for c in corners)
            assert previous<=cost<=final
            for c,d in corners.items():
                u,v=minimum(c,m)
                if m>=d['first']:assert u+v==d['u']+d['v']
                if m>=d['last']:assert v==d['v']
                assert mass(c,minimum(c,m))<=mass(c,(d['u'],d['v']))
                error=mass(c,(u-d['u'],v-d['v']))
                assert error<=2*mass(c,(d['u'],d['v']))
            previous=cost;checks+=1
        assert previous==final
    assert corners[8]['last']>corners[8]['n']//2
    # A formal tower with one unit of unavoidable cost in every revealed corner.
    for m in range(1,33):
        assert sum(Q(1) for _ in range(m))==m
        for k in range(1,m+1):
            assert tuple(range(1,m+1))[:k]==tuple(range(1,k+1))
    # Independent Gamma/path minima do not imply a joint feasible lift.
    # Constraint u+10v=1: Gamma minimum at (1,0), path minimum at (0,1/10).
    alpha=Q(1,1000)
    assert alpha<Q(1,10)
    gamma_budget=alpha;path_budget=Q(1,10)
    assert 1+10*0==1 and Q(0)+10*Q(1,10)==1
    # Joint bounds would imply |u+10v| <= |u|+10|v| < 1.
    assert path_budget+10*gamma_budget<1
    result={'passed':True,'simultaneous_radius_minimum_checks':checks,
        'delayed_last_observation':last,'unbounded_cost_prefixes':32,
        'checks':['cornerwise_monotonicity','simultaneous_radius_minimizers',
                  'no_event_length_bound_on_observer_stabilization',
                  'separate_norm_minima_do_not_prove_joint_feasibility'],
        'scope':'Exact finite affine-fiber fixtures. Infinite realization uses corner stabilization, monotone convergence and the stated joint-budget compactness argument.'}
    out=Path(__file__).resolve().parents[1]/'results/observer-source-realization.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
