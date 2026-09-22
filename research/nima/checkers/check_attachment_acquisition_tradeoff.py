"""Precision/prior plans with sufficient bounds and actual ambiguity witnesses.

Default: nine precision policies and orders 1..20. Optional single-plan CLI.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import argparse
import json
from flint import arb

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('task',HERE/'certify_noisy_attachment_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
A=t.A


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eta',type=int)
    parser.add_argument('--rho0',default='1/10')
    parser.add_argument('--rhox',default='1/100')
    parser.add_argument('--budget',default='40')
    parser.add_argument('--vacuum-radius',default='1/1000')
    args=parser.parse_args()
    budget=Q(args.budget);vr=Q(args.vacuum_radius);bc=Q(1,100)
    assert budget>0 and 0<vr<bc
    if args.eta is not None:assert args.eta>=1
    K={a:t.c.scaled_residual(a) for a in (2,12,20)}
    E0=K[2]*K[12]*(-arb.pi()*148).exp()/5
    Ex=K[2]*K[20]*(-arb.pi()*404).exp()/5
    mu={a:t.r.moments(a) for a in (2,4,12,60)}
    s0=(mu[4]-mu[2])*(mu[60]-mu[12])/18
    sx=-(mu[2]-t.c.L)*(mu[60]-t.c.L)/18
    assert s0>0 and sx<0
    mid0=Q(str(E0.mid().fmpq()));midx=Q(str(Ex.mid().fmpq()))
    E0lo,E0hi=t.endpoints(E0)
    s0lo=t.endpoints(s0)[0];sxlo=t.endpoints(sx)[0]
    policies=[(Q(args.rho0),Q(args.rhox))] if args.eta else [
        (r0,rx) for r0 in (Q(1,4),Q(1,10),Q(1,20))
        for rx in (Q(1,100),Q(1,10),Q(1,2))]
    orders=[args.eta] if args.eta else list(range(1,21))
    results=[];summaries=[]
    for rho0,rhox in policies:
        assert 0<rho0<1 and rhox>0
        raw0=(mid0,rho0*mid0);rawx=(Q(0),rhox*midx)
        box0=t.interval(*raw0)/E0;boxx=t.interval(*rawx)/Ex
        amin=t.endpoints(box0)[0];cmax=t.endpoints(boxx)[1];bmin=bc-vr
        assert amin>0 and cmax>0 and bmin>0
        # Robust finite witness interval: fits ALL values in calibration enclosure.
        robust_lo=(raw0[0]-raw0[1])/E0lo
        robust_hi=(raw0[0]+raw0[1])/E0hi
        robust_a=robust_lo+(robust_hi-robust_lo)/1000
        robust_b=bmin+2*vr/1000
        low_source=(robust_a,Q(0),robust_b)

        def cost(source):
            a,c,b=source;return 32*(abs(a)+abs(c))+8*abs(b)

        def fits(source):
            a,c,b=source
            return (bool(abs(A(a)*E0-A(raw0[0]))<=A(raw0[1])) and
                    bool(abs(A(c)*Ex)<=A(rawx[1])) and abs(b-bc)<=vr)

        positives=[s for s in ((Q(1),Q(0),bc),low_source)
                   if cost(s)<=budget and fits(s) and s[2]>0 and s0*A(s[0])+sx*A(s[1])>0]
        positive=positives[0] if positives else None
        local_negative=(Q(39,50),Q(93,200),bc)
        neg_ok=(cost(local_negative)<=budget and fits(local_negative) and
                bool(s0*A(local_negative[0])+sx*A(local_negative[1])<0))
        cases=[]
        for eta in orders:
            theta=Q(2,3)**eta
            lower_cost=32*amin+8*bmin
            case={'eta':eta,'status':'UNRESOLVED_BOUNDS'}
            if lower_cost>budget:
                case['status']='CERTIFIED_INFEASIBLE'
            else:
                remaining=budget-lower_cost
                # Exact minimum of the conservative, budget-coupled target relaxation.
                R=t.endpoints((1+arb(3).log())**2*A(theta)/32)[1]
                cross=min(cmax,remaining/32) if sxlo+32*R<0 else Q(0)
                residual_lower=s0lo*amin+sxlo*cross-R*(remaining-32*cross)
                vacuum_lower=bmin-remaining*theta/8
                case['universal_target_lower_bounds']={
                    'vacuum':t.decimal_bounds(A(vacuum_lower))['lower'],
                    'residual_per_w_squared':t.decimal_bounds(A(residual_lower))['lower']}
                if positive is not None and vacuum_lower>0 and residual_lower>0:
                    case['status']='SUFFICIENT_PLAN'
                elif positive is not None and neg_ok:
                    case.update(status='AMBIGUOUS_LOCAL_DATA',
                                witness='local_negative_source',
                                negative_residual_enclosure=t.decimal_bounds(
                                    s0*A(local_negative[0])+sx*A(local_negative[1])))
                elif positive is not None and cost(low_source)<=budget and fits(low_source):
                    tail=-(budget-cost(low_source))*theta/8
                    total=low_source[2]+tail
                    assert cost(low_source)+8*abs(tail)/theta==budget
                    if total<0:
                        case.update(status='AMBIGUOUS_UNACQUIRED_TAIL',
                                    witness='low_source_plus_vacuum_tail_at_A_3',
                                    negative_vacuum_sum=t.decimal_bounds(A(total)))
            cases.append(case)
        policy={'rho0':str(rho0),'rhox':str(rhox),
            'raw_feature_intervals':{'z0':{'center':str(raw0[0]),'radius':str(raw0[1])},
                                     'zx':{'center':'0','radius':str(rawx[1])}},
            'positive_source':list(map(str,positive)) if positive else None,
            'low_source':list(map(str,low_source)),
            'local_negative_source':list(map(str,local_negative)),
            'tail_witness_rule':'b_3=-(budget-cost(low_source))*(2/3)^eta/8; all other unobserved coefficients zero',
            'cases':cases}
        results.append(policy)
        sufficient=[c['eta'] for c in cases if c['status']=='SUFFICIENT_PLAN']
        summaries.append({'rho0':str(rho0),'rhox':str(rhox),
            'first_certified_eta_in_scan':min(sufficient) if sufficient else None,
            'statuses':{s:[c['eta'] for c in cases if c['status']==s]
                        for s in sorted({c['status'] for c in cases})}})
    if args.eta is None:
        statuses={case['status'] for policy in results for case in policy['cases']}
        assert {'SUFFICIENT_PLAN','AMBIGUOUS_LOCAL_DATA','AMBIGUOUS_UNACQUIRED_TAIL','UNRESOLVED_BOUNDS'}<=statuses
    result={'passed':True,'prior':'sum_A (A/2)^eta p(x_A) <= budget',
        'budget':str(budget),'vacuum_input':{'center':str(bc),'radius':str(vr)},
        'background_domain':'integer arithmetic backgrounds A>=2; A=3 is explicitly admitted for tail witnesses',
        'task':'both real aggregate vacuum and normalized residual readouts are strictly positive',
        'input_kind':'synthetic raw intervals; calibrated source responses, not experimental measurements',
        'policy_summaries':summaries,'policies':results,
        'scope':'Sufficient plans are not claimed optimal. Ambiguity statuses have actual finite source witnesses under the same data/prior. Unresolved means neither certificate is obtained. Changing eta is changing an independently required prior, not learning it from the readings.'}
    out=HERE.parent/'results/attachment-acquisition-tradeoff.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'budget':str(budget),'policy_summaries':summaries},indent=2))


if __name__=='__main__':main()
