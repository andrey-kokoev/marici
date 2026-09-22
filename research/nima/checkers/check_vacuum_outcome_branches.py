"""Outcome-dependent vacuum acquisition with explicit feasible-source witnesses."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
from flint import arb

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('next_probe',HERE/'check_next_vacuum_acquisition.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
t=n.t;A=t.A


def main():
    n.main() # fresh baseline residual bound and prior audit
    eta=12;q3=Q(3,2)**eta;q4=Q(2)**eta
    E=t.c.scaled_residual(2)*t.c.scaled_residual(12)*(-arb.pi()*148).exp()/5
    mid=Q(str(E.mid().fmpq()));raw=(mid,mid/10)
    amin=t.endpoints(t.interval(*raw)/E)[0]
    el,eh=t.endpoints(E)
    al=(raw[0]-raw[1])/el;ah=(raw[0]+raw[1])/eh
    a=al+(ah-al)/1000
    assert abs(A(a)*E-A(mid))<=A(mid/10)

    def witness(b,b3,b4):
        cost=32*a+8*abs(b)+8*q3*abs(b3)+8*q4*abs(b4)
        assert cost<=40
        return {'a0_at_2':str(a),'b2':str(b),'b3':str(b3),'b4':str(b4),
                'normalized_moment_cost':str(cost),'vacuum_sum':str(b+b3+b4)}

    def classify(center,radius,blo=Q(9,1000),bhi=Q(11,1000)):
        B=40-32*amin-8*blo
        lo=max(center-radius,-B/(8*q3));hi=min(center+radius,B/(8*q3))
        out={'center':str(center),'radius':str(radius),'status':'UNRESOLVED'}
        if lo>hi:
            out['status']='INFEASIBLE_PRIOR';return out
        lower=blo+lo-(B-8*q3*abs(lo))/(8*q4)
        upper=bhi+hi+(B-8*q3*abs(hi))/(8*q4)
        out['universal_vacuum_bounds']={'lower':t.decimal_bounds(A(lower))['lower'],
                                         'upper':t.decimal_bounds(A(upper))['upper']}
        pos=None;neg=None;any_witness=None
        for b in (blo+(bhi-blo)/1000,(blo+bhi)/2,bhi-(bhi-blo)/1000):
            cap=(40-32*a-8*b)/(8*q3)
            if cap<0:continue
            wl=max(center-radius,-cap);wh=min(center+radius,cap)
            if wl>wh:continue
            candidates={wl,wh,(wl+wh)/2,max(wl,min(wh,-b))}
            for b3 in candidates:
                tail=(40-32*a-8*b-8*q3*abs(b3))/(8*q4)
                assert tail>=0
                for b4 in (-tail,Q(0),tail):
                    w=witness(b,b3,b4);any_witness=w
                    total=b+b3+b4
                    if total>0:pos=w
                    if total<0:neg=w
        if any_witness is not None and lower>0:
            out.update(status='TASK_CERTIFIED',source_witness=any_witness)
        elif any_witness is not None and upper<0:
            out.update(status='TASK_CONTRADICTED',source_witness=any_witness)
        elif pos is not None and neg is not None:
            out.update(status='AMBIGUOUS',positive_source=pos,negative_source=neg)
        return out

    grid=[classify(Q(i,1000),Q(1,1000)) for i in range(-14,15)]
    favorable=classify(Q(0),Q(1,1000));assert favorable['status']=='TASK_CERTIFIED'
    ambiguous=classify(Q(-1,100),Q(1,1000));assert ambiguous['status']=='AMBIGUOUS'
    # Same b3, identical b4=0, opposite signs: measuring the next background cannot help.
    local_pair=[witness(b,Q(-1,100),Q(0)) for b in (Q(91,10000),Q(109,10000))]
    assert Q(local_pair[0]['vacuum_sum'])<0<Q(local_pair[1]['vacuum_sum'])
    refined=classify(Q(-96,10000),Q(1,100000),Q(999,100000),Q(1001,100000))
    assert refined['status']=='TASK_CERTIFIED'
    result={'passed':True,'fixed_prior':'sum_A (A/2)^12 p(x_A)<=40',
        'old_b2_interval':['0.009','0.011'],'old_raw_z0':list(map(str,raw)),
        'scan':'centers -0.014 through 0.014, step 0.001; radius 0.001',
        'outcome_counts':{s:sum(x['status']==s for x in grid) for s in sorted({x['status'] for x in grid})},
        'outcomes':grid,'ambiguous_branch':ambiguous,
        'why_b4_alone_cannot_resolve':local_pair,
        'conditional_refinement':{'b2_interval':['0.00999','0.01001'],
                                  'b3_interval':['-0.00961','-0.00959'],'certificate':refined},
        'scope':'Finite outcome grid, not exhaustive partition of all real returned intervals. A negative bound is not a contradiction without a feasible witness. Residual positivity remains the fresh baseline guarantee; A3 vacuum data do not acquire A3 features. Refinement is conditional on returned intervals, not a prediction or an optimal-cost claim.'}
    out=HERE.parent/'results/vacuum-outcome-branches.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'counts':result['outcome_counts'],
        'conditional_refinement':{'status':refined['status'],'bounds':refined['universal_vacuum_bounds']}},indent=2))


if __name__=='__main__':main()
