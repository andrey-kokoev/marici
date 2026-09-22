"""Three-valued task certificate with real raw data and one fixed tail prior.

Fixtures are synthetic exact-rational acquisition intervals, NOT measurements.
"""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('readout',HERE/'check_attachment_readout_stability.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
c=r.c
ctx.prec=192


def A(q):
    q=Q(q);return arb(q.numerator)/q.denominator


def interval(center,radius):return A(center-radius).union(A(center+radius))


def endpoints(ball):
    return Q(str(ball.lower().fmpq())),Q(str(ball.upper().fmpq()))


def decimal_bounds(ball):
    lo,hi=endpoints(ball);scale=10**8
    lo*=scale;hi*=scale
    lower=lo.numerator//lo.denominator
    upper=-((-hi.numerator)//hi.denominator)
    return {'lower':str(Decimal(lower)/Decimal(scale)),
            'upper':str(Decimal(upper)/Decimal(scale))}


def minimum_abs(ball):
    lo,hi=endpoints(ball)
    return Q(0) if lo<=0<=hi else min(abs(lo),abs(hi))


def main():
    eta=16;M=Q(40*2**eta)
    pi=arb.pi()
    K={a:c.scaled_residual(a) for a in (2,12,20)}
    E0=K[2]*K[12]*(-pi*(2**2+12**2)).exp()/5
    Ex=K[2]*K[20]*(-pi*(2**2+20**2)).exp()/5
    assert E0>0 and Ex>0
    mu={a:r.moments(a) for a in (2,4,12,60)}
    s0=(mu[4]-mu[2])*(mu[60]-mu[12])/18
    sx=-(mu[2]-c.L)*(mu[60]-c.L)/18
    assert s0>0 and sx<0
    mid0=Q(str(E0.mid().fmpq()));midx=Q(str(Ex.mid().fmpq()))
    data={'z0':(mid0,mid0/10),'zx':(Q(0),midx/100),
          'vacuum':(Q(1,100),Q(1,1000))}

    def audit(inputs,witness=None):
        boxes={'a0':interval(*inputs['z0'])/E0,
               'ax':interval(*inputs['zx'])/Ex,
               'b':interval(*inputs['vacuum'])}
        lower=2**eta*(32*minimum_abs(boxes['a0'])+
                         32*minimum_abs(boxes['ax'])+8*minimum_abs(boxes['b']))
        answer={'status':'UNRESOLVED','necessary_moment_cost_lower_bound':str(lower),
                'coefficient_outer_boxes':{k:decimal_bounds(v) for k,v in boxes.items()}}
        if lower>M:
            answer.update(status='CERTIFIED_INFEASIBLE',
                          contradiction='Every compatible source exceeds the fixed moment budget.')
            return answer
        if witness is not None:
            a,ax,b=map(Q,witness)
            cost=2**eta*(32*abs(a)+32*abs(ax)+8*abs(b))
            predictions={'z0':A(a)*E0,'zx':A(ax)*Ex,'vacuum':A(b)}
            fits=all(abs(predictions[k]-A(center))<=A(radius)
                     for k,(center,radius) in inputs.items())
            if fits and cost<=M:
                answer.update(status='CERTIFIED_FEASIBLE',
                              finite_source_witness={'a0':str(a),'ax':str(ax),'b':str(b)},
                              witness_moment_cost=str(cost))
        remaining=M-lower
        tail_v=remaining/(8*3**eta)
        tail_r=A(remaining)*(1+arb(3).log())**2/(32*3**eta)
        local_v=boxes['b'];local_r=s0*boxes['a0']+sx*boxes['ax']
        sum_v=local_v+interval(Q(0),tail_v)
        sum_r=local_r+(-tail_r.upper()).union(tail_r.upper())
        answer.update(local_readout_enclosures={'vacuum':decimal_bounds(local_v),'residual_per_w_squared':decimal_bounds(local_r)},
                      unacquired_l1_tail_upper_bounds={'vacuum':decimal_bounds(A(tail_v))['upper'],
                                                      'residual_per_w_squared':decimal_bounds(tail_r)['upper']},
                      aggregate_readout_enclosures={'vacuum':decimal_bounds(sum_v),'residual_per_w_squared':decimal_bounds(sum_r)}, 
                      all_feasible_aggregate_readouts_positive=bool(sum_v>0 and sum_r>0),
                      interval_scope='Outer bounds for every feasible source; empty feasibility is not ruled out unless a witness is certified.')
        return answer

    good=audit(data,(Q(1),Q(0),Q(1,100)))
    assert good['status']=='CERTIFIED_FEASIBLE'
    assert good['all_feasible_aggregate_readouts_positive']
    bad_data=dict(data);bad_data['vacuum']=(Q(2),Q(1,1000))
    bad=audit(bad_data)
    assert bad['status']=='CERTIFIED_INFEASIBLE'
    feature_lower=2**eta*(32*minimum_abs(interval(*data['z0'])/E0)+
                           32*minimum_abs(interval(*data['zx'])/Ex))
    vacuum_lower=2**eta*8*minimum_abs(interval(*bad_data['vacuum']))
    assert feature_lower<M and vacuum_lower<M and feature_lower+vacuum_lower>M
    unresolved=audit(data)
    assert unresolved['status']=='UNRESOLVED' # a lower bound alone is not feasibility
    assert (1+arb(6).log())*(1+arb(210).log())/18<1
    assert eta>2/(1+arb(3).log())
    result={'passed':True,'source_domain':'real coefficients in labelled V_A plus the line spanned by k_A; A>=2 admitted integer backgrounds',
        'prior':{'background_moment_order':eta,'path_moment_budget':str(M),
                 'formula':'sum_A A^16 [32 sum_j |a_(A,j)|+8|b_A|] <= M'},
        'acquired_background':2,
        'input_kind':'Synthetic exact-rational raw scalar intervals with fixed actual-theta calibration; not experimental data',
        'raw_inputs':{k:{'center':str(v[0]),'radius':str(v[1])} for k,v in data.items()},
        'calibration_enclosures':{'E0':str(E0),'Ex':str(Ex),'sigma0':str(s0),'sigmax':str(sx)},
        'feasible_case':good,'infeasible_case':bad,
        'infeasible_case_raw_vacuum_interval':{'center':'2','radius':'1/1000'},
        'witness_withheld_case':unresolved,
        'scope':'Certified sufficient feasibility witness and necessary budget contradiction, not a complete solver for arbitrary correlated calibration intervals. Scalar task recovery only; no intrinsic module boundary or source-calibration map is inferred from these state values.'}
    out=HERE.parent/'results/certified-noisy-attachment-task.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'prior':result['prior'],'calibrations':result['calibration_enclosures'],
                      'feasible_case':good,'infeasible_status':bad['status'],
                      'witness_withheld_status':unresolved['status']},indent=2))


if __name__=='__main__':main()
