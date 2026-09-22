"""Refine calibration, not data or priors; certify diagonal budget feasibility."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
from flint import arb

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('task',HERE/'certify_noisy_attachment_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)


def nearest_zero(lo,hi):return Q(0) if lo<=0<=hi else min((lo,hi),key=abs)


def certify_diagonal_budget(data,calibrations,weights,budget):
    """Positive diagonal calibration intervals; exact rational outer/inner certificates.

    Cost is sum weights[i]*abs(source[i]). Unobserved coordinates may be zero.
    UNKNOWN is intentional when correlated true calibrations are not resolved.
    """
    assert len(data)==len(calibrations)==len(weights)
    lower=Q(0);candidate=[]
    for (dl,dh),(el,eh),weight in zip(data,calibrations,weights):
        assert dl<=dh and 0<el<=eh and weight>0
        values=(dl/el,dl/eh,dh/el,dh/eh)
        lower+=weight*abs(nearest_zero(min(values),max(values)))
        il=max(dl/el,dl/eh);ih=min(dh/el,dh/eh)
        candidate.append(nearest_zero(il,ih) if il<=ih else None)
    if lower>budget:
        return {'status':'INFEASIBLE','cost_lower_bound':str(lower),
                'excess_lower_bound':str(lower-budget)}
    if all(x is not None for x in candidate):
        cost=sum(w*abs(x) for w,x in zip(weights,candidate))
        if cost<=budget:
            for (dl,dh),(el,eh),x in zip(data,calibrations,candidate):
                assert dl<=el*x<=dh and dl<=eh*x<=dh
            return {'status':'FEASIBLE','cost_lower_bound':str(lower),
                    'witness':list(map(str,candidate)),'witness_cost':str(cost)}
    return {'status':'UNKNOWN','cost_lower_bound':str(lower)}


def main():
    previous=HERE.parent/'results/vacuum-outcome-branches.json'
    prior=json.loads(previous.read_text(encoding='utf-8'))
    center,radius=map(Q,prior['old_raw_z0'])
    data0=(center-radius,center+radius)
    def response():
        return t.c.scaled_residual(2)*t.c.scaled_residual(12)*(-arb.pi()*148).exp()/5
    old=response();old_bounds=t.endpoints(old)
    t.c.CELLS=32768;t.c.scaled_residual.cache_clear()
    refined=response();new_bounds=t.endpoints(refined)
    assert new_bounds[0]>old_bounds[0] and new_bounds[1]<old_bounds[1]
    weights=(Q(32),Q(8),8*Q(3,2)**12)
    cases=[];counts={}
    for case in prior['outcomes']:
        m,e=Q(case['center']),Q(case['radius'])
        data=(data0,(Q(9,1000),Q(11,1000)),(m-e,m+e))
        old_test=certify_diagonal_budget(data,(old_bounds,(Q(1),Q(1)),(Q(1),Q(1))),weights,Q(40))
        new_test=certify_diagonal_budget(data,(new_bounds,(Q(1),Q(1)),(Q(1),Q(1))),weights,Q(40))
        status=case['status']
        if status=='UNRESOLVED':
            assert old_test['status']=='UNKNOWN' and new_test['status']=='INFEASIBLE'
            status='INFEASIBLE_PRIOR'
        elif status=='INFEASIBLE_PRIOR':assert new_test['status']=='INFEASIBLE'
        else:
            assert new_test['status']=='FEASIBLE'
            witness_keys=['source_witness'] if status=='TASK_CERTIFIED' else ['positive_source','negative_source']
            for key in witness_keys:
                w=case[key];a,b,b3,b4=(Q(w[k]) for k in ('a0_at_2','b2','b3','b4'))
                assert data0[0]<=new_bounds[0]*a<=data0[1]
                assert data0[0]<=new_bounds[1]*a<=data0[1]
                assert Q(9,1000)<=b<=Q(11,1000) and m-e<=b3<=m+e
                assert 32*abs(a)+8*abs(b)+weights[2]*abs(b3)+8*2**12*abs(b4)<=40
        counts[status]=counts.get(status,0)+1
        cases.append({'center':case['center'],'previous_status':case['status'],
                      'status':status,'feasibility_certificate':new_test,
                      'lower_cost_display':t.decimal_bounds(t.A(Q(new_test['cost_lower_bound'])))})
    assert counts=={'INFEASIBLE_PRIOR':6,'AMBIGUOUS':4,'TASK_CERTIFIED':19}
    # Basic API regressions, including negative sources and a genuine unresolved enclosure.
    assert certify_diagonal_budget([(Q(-2),Q(-1))],[(Q(1),Q(1))],[Q(1)],Q(1))['status']=='FEASIBLE'
    assert certify_diagonal_budget([(Q(1),Q(1))],[(Q(1),Q(2))],[Q(1)],Q(1))['status']=='UNKNOWN'
    result={'passed':True,'unchanged_prior':prior['fixed_prior'],
        'unchanged_raw_z0':prior['old_raw_z0'],'baseline_artifact':str(previous),
        'refinement':'2048 to 32768 complete interval cells per scaled residual window; same 192-bit precision, cutoff, physical calibration and acquisition intervals',
        'calibration_enclosures':{'old':str(old),'refined':str(refined)},
        'outcome_counts':counts,'outcomes':cases,
        'scope':'All 29 previously scanned outcomes are now classified, not all possible real intervals. Infeasibility is a necessary source-cost contradiction. Existing sign and ambiguity certificates are preserved; no acquisition is altered and no intrinsic module data are inferred.'}
    out=HERE.parent/'results/resolved-vacuum-outcomes.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'counts':counts,'calibration':result['calibration_enclosures'],
        'resolved_cases':[c for c in cases if c['previous_status']=='UNRESOLVED']},indent=2))


if __name__=='__main__':main()
