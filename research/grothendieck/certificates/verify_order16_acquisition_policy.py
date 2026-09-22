"""Exact, portable decision policy for the frozen middle task.

Needs verify_order16_vacuum_bridge.py and verify_source_task_transition.py.
All conclusions are conditional on their source/calibration/prior premises and
valid acquisition errors. UNRESOLVED is not evidence of physical ambiguity.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,copy,sys,json
s=importlib.util.spec_from_file_location('bridge',Path(__file__).with_name('verify_order16_vacuum_bridge.py'))
b=importlib.util.module_from_spec(s);s.loader.exec_module(b);v=b.v
CONTRACT={'vacuum':'chi3_and_chi4_unit_rows_on_the_same_unknown_source',
          'reference':'same_positive_filter_on_known_unit_v_2_0_with_total_preparation_and_acquisition_error',
          'method':'necessary_outer_cost_and_calibration_uniform_source_witness',
          'scope':'conditional_policy_no_measurement_no_probability_no_cost_optimality',
          'unresolved':'not_a_proof_of_physical_ambiguity_or_impossibility'}

def verify(p):
    v.fields(p,('version','contract','base','base_certificate','bridge','threshold','vacuum_cost_cap',
                'robust_cost_deficit','reference_radius','worst_case_infeasible_below','worst_case_task_at_least'))
    v.require(type(p['version']) is int and p['version']==1 and p['contract']==CONTRACT,'Wrong policy scope')
    v.node(p['base'],p['base_certificate']);b.bridge(p['bridge'])
    raw,gains,sigma,D,M,outer,weights,L=v.problem(p['base'])
    v.require(raw['vacuum']==(Q(1,100),Q(1,100)) and raw['crossed']==(Q(0),Q(0)), 'Not the middle-task slice')
    lo,hi=raw['positive'];glo,ghi=gains['positive'];W=weights['positive'];fixed=Q(weights['vacuum'],100)
    v.require(lo>0 and M>fixed and W<=M,'Invalid source/reference budget')
    # This makes the raw upper endpoint nonbinding for every reference subinterval.
    v.require(lo/glo<=hi/ghi,'Robust interval may be empty for a different reason')
    threshold=lo/((M-fixed)/W);outer_slack=M-L;deficit=fixed+W*lo/glo-M
    v.require(glo<threshold<ghi and outer_slack>0 and deficit>0,'Not a straddling middle case')
    v.require(p['base_certificate']['status']=='UNRESOLVED','Root is not unresolved')
    expected={'threshold':threshold,'vacuum_cost_cap':outer_slack,'robust_cost_deficit':deficit}
    for key,value in expected.items():v.require(v.q(p[key])==value,'Wrong decision threshold')
    radius=v.q(p['reference_radius']);v.require(radius>0,'Positive total-error contract required')
    v.require(glo+2*radius<threshold<ghi-2*radius,'Precision does not leave both worst-case branches')
    v.require(v.q(p['worst_case_infeasible_below'])==threshold-2*radius and
              v.q(p['worst_case_task_at_least'])==threshold+2*radius,'Wrong worst-case error factor')
    # At the inclusive reference threshold a robust witness exists and both
    # universal task lower bounds are positive. All higher-gain subintervals
    # must retain positivity: check the entire high-side interval at once.
    conditioned=copy.deepcopy(p['base']);conditioned['gains']['positive']=[str(threshold),str(ghi)]
    _,bounds,_=b.expected(conditioned,{'parts':[prior(3,M)]},{})
    v.require(all(x[0]>0 for x in bounds.values()),'High-side task positivity not proved')
    return True

def prior(start,M):
    return {'start':start,'end':None,'kind':'prior','data':[str(-M/(8*start**16)),str(M/(8*start**16))],'gain':['1','1']}

def decide(p,q):
    verify(p)
    v.require(type(q) is dict,'Expected query object')
    base=copy.deepcopy(p['base']);M=v.q(base['budget']);raw,gains,_,_,_,_,weights,L=v.problem(base)
    if q.get('kind')=='vacuum_error_envelope':
        v.fields(q,('kind','true_values','radii'));v.fields(q['true_values'],('3','4'));v.fields(q['radii'],('3','4'))
        values={A:v.q(q['true_values'][str(A)]) for A in (3,4)}
        radii={A:v.q(q['radii'][str(A)]) for A in (3,4)}
        v.require(all(r>=0 for r in radii.values()),'Negative vacuum error radius')
        minimum=sum(8*A**16*max(abs(values[A])-2*radii[A],Q(0)) for A in (3,4))
        maximum=sum(8*A**16*abs(values[A]) for A in (3,4))
        cap=v.q(p['vacuum_cost_cap'])
        outcome=('ALL_ERRORS_PRIOR_INCOMPATIBLE' if minimum>cap else
                 'ALL_ERRORS_UNRESOLVED' if maximum<=cap else 'ERROR_DEPENDENT')
        return {'outcome':outcome,'minimum_returned_necessary_cost':str(minimum),
                'maximum_returned_necessary_cost':str(maximum),
                'scope':'hypothetical_true_values_and_rectangular_bounded_errors_not_actual_measurements'}
    if q.get('kind')=='vacuum':
        v.fields(q,('kind','readings'));v.fields(q['readings'],('3','4'))
        readings=q['readings'];cost=sum(8*A**16*v.minimum(v.box(readings[str(A)])) for A in (3,4))
        n={'parts':[{'start':A,'end':A,'kind':'acquired','data':readings[str(A)],'gain':['1','1']} for A in (3,4)]+[prior(5,M)]}
        lower,bounds,tails=b.expected(base,n,readings)
        v.require(lower==L+cost,'Cost decomposition failed')
        status='SOURCE_PRIOR_INCOMPATIBLE' if cost>v.q(p['vacuum_cost_cap']) else 'UNRESOLVED'
        return {'outcome':status,'added_necessary_cost':str(cost),'necessary_cost':str(lower),
                'robust_cost_deficit':str(v.q(p['robust_cost_deficit'])+cost),
                'bounds':None if bounds is None else {k:list(map(str,x)) for k,x in bounds.items()},
                'tails':tails,'witness':None,'positive_task':False}
    v.fields(q,('kind','center'));v.require(q['kind']=='reference','Unknown acquisition')
    center=v.q(q['center']);radius=v.q(p['reference_radius']);glo,ghi=gains['positive']
    a,z=max(glo,center-radius),min(ghi,center+radius)
    if a>z:return {'outcome':'CALIBRATION_INCOMPATIBLE'}
    base['gains']['positive']=[str(a),str(z)]
    lower,bounds,tails=b.expected(base,{'parts':[prior(3,M)]},{})
    h=v.q(p['threshold'])
    outcome=('SOURCE_PRIOR_INCOMPATIBLE' if center+radius<h else
             'TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE' if center-radius>=h else 'UNRESOLVED')
    witness=None
    if outcome=='TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE':
        witness={'positive':str(raw['positive'][0]/a),'crossed':'0','vacuum':'1/100'}
        cert={'version':1,'problem_sha256':v.sha(base),'status':'CERTIFIED_FEASIBLE','necessary_cost':str(lower),
              'aggregate_bounds':{k:list(map(str,x)) for k,x in bounds.items()},'positive_task':True,'witness':witness}
        v.node(base,cert)
    if outcome=='SOURCE_PRIOR_INCOMPATIBLE':v.require(lower>M,'Missing contradiction')
    else:v.require(lower<=M,'Unexpected contradiction')
    return {'outcome':outcome,'conditioned_gain':[str(a),str(z)],'necessary_cost':str(lower),
            'bounds':None if bounds is None else {k:list(map(str,x)) for k,x in bounds.items()},
            'tails':tails,'witness':witness,'positive_task':witness is not None}

if __name__=='__main__':
    if len(sys.argv) not in (2,3):raise SystemExit('Usage: python verify_order16_acquisition_policy.py policy.json [query.json]')
    p=v.load(sys.argv[1]);verify(p)
    print(json.dumps(decide(p,v.load(sys.argv[2])),indent=2) if len(sys.argv)==3 else 'VALID conditional order-16 acquisition policy; no acquisition asserted')
