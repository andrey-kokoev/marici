"""Bounded-resource challenge to the necessity of shared tact.

Two private single-worker routes; one job maximum per worker, no queue.
All policies have the same workers, delay schedules, plant, gain, messages,
and disturbances. Async never waits for or triggers the other worker.
Global scheduler units belong to the simulation, not a shared controller
release/commit protocol. Finite scenario tests are not stability theorems.
"""
from pathlib import Path
from fractions import Fraction as Q
import math,json
ROOT=Path(__file__).resolve().parents[3]
HORIZON=1200
GAIN=0.035
TRACK_LIMIT=0.35
AGE_LIMIT=12
SETTLE_LIMIT=120
SCENARIOS={
 'periodic_skew':([1,2,1,3],[4,8,5,10]),
 'bursty_skew':([1,1,4,1,2,3],[3,12,3,11,5,9]),
 'reversed_bottleneck':([9,3,12,5,8],[1,3,1,2]),
 'coprime_patterns':([2,5,1,4,3],[7,11,4,9,6,12,3])}

def simulate(policy,delays,gain=GAIN):
    period=max(max(d) for d in delays)
    jobs=[None,None];last=[None,None];sequence=[0,0]
    launches=[[],[]];completed=[0,0];work=[0,0]
    updates=[];paired=[];aligned_checks=0;prediction_checks=0;ages=[];report_counts=[]
    x=0.0;u=0.0;integrated_u=0.0;target=0.0
    next_batch=0;ready=[None,None];states=[];errors=[];peak_workers=0
    # Unknown-to-controller state kicks; target changes are known when issued.
    reference={100:1.0,500:-0.5,900:0.75}
    kicks={300:0.20,700:-0.15}
    deadlines={k:k+SETTLE_LIMIT for k in reference.keys()|kicks.keys()}
    settled={}
    def release(route,k,snapshot=None):
        assert jobs[route] is None
        j=sequence[route];sequence[route]+=1
        delay=delays[route][j%len(delays[route])]
        state,version,command_sum=(x,k,integrated_u) if snapshot is None else snapshot
        # Same two algebraic routes, with actual sampled state version intact.
        z=Q.from_float(state)
        value=float(Q(1,2)*((Q(1,2)+Q(3,2))*z) if route==0 else Q(1,2)*(Q(1,2)*z)+Q(1,2)*(Q(3,2)*z))
        assert value==state
        jobs[route]={'finish':k+delay,'sample_time':version,'value':value,
                     'command_sum':command_sum,'sample_truth':state}
        launches[route].append(k)
    for k in range(HORIZON):
        if k in reference:target=reference[k]
        if k in kicks:x+=kicks[k]
        arrivals=[]
        for route in (0,1):
            job=jobs[route]
            if job is not None and job['finish']==k:
                jobs[route]=None;last[route]=job;ready[route]=job
                completed[route]+=1;arrivals.append(route)
                assert job['sample_time']<=k
                assert abs(job['value']-job['sample_truth'])<1e-12
        commit=False
        if policy=='fixed_tact':
            commit=k>0 and k==next_batch
        elif policy=='completion_barrier':
            commit=all(r is not None for r in ready)
        elif policy in ('independent_pair','independent_fresh'):
            commit=bool(arrivals)
        else:raise ValueError(policy)
        if commit:
            if policy.startswith('independent'):
                records=[r for r in last if r is not None]
                if policy=='independent_fresh':records=[r for r in records if k-r['sample_time']<=AGE_LIMIT]
            else:records=ready
            assert records and all(r is not None for r in records)
            same=len({r['sample_time'] for r in records})==1
            if not policy.startswith('independent'):assert same
            # Every policy uses the same model-based time alignment.
            # Transport each old reading by the ACTUAL known control integral.
            # No oracle disturbance or current-state value is used here.
            estimates=[r['value']+integrated_u-r['command_sum'] for r in records]
            # Unknown kicks are NOT supplied to the point predictor.
            # With no intervening kick, the transported point should match
            # the plant up to floating-point accumulation error.
            for record,estimate in zip(records,estimates):
                if not any(record['sample_time']<t<=k for t in kicks):
                    scale=max(1.0,abs(x),abs(integrated_u),abs(record['command_sum']),abs(record['value']))
                    assert abs(estimate-x)<1e-10*scale
                    prediction_checks+=1
            estimate=sum(estimates)/len(estimates)
            u=-gain*(estimate-target)
            updates.append(k)
            paired.append(same)
            aligned_checks+=int(same)
            ages.append(max(k-r['sample_time'] for r in records));report_counts.append(len(records))
            if not policy.startswith('independent'):
                ready=[None,None]
                if policy=='completion_barrier':next_batch=k
        if policy.startswith('independent'):
            for route in (0,1):
                if jobs[route] is None:release(route,k)
        elif k==next_batch:
            assert all(job is None for job in jobs)
            snapshot=(x,k,integrated_u)
            release(0,k,snapshot);release(1,k,snapshot)
            next_batch=k+period if policy=='fixed_tact' else -1
        peak_workers=max(peak_workers,sum(j is not None for j in jobs))
        for route in (0,1):work[route]+=int(jobs[route] is not None)
        x+=u;integrated_u+=u
        assert math.isfinite(x)
        states.append(x);errors.append(abs(x-target))
        for event,deadline in deadlines.items():
            if k==deadline:settled[str(event)]=max(errors[k-19:k+1])
    # Tracking envelope is evaluated away from the admitted settling windows.
    admissible=[e for k,e in enumerate(errors) if not any(t<=k<t+SETTLE_LIMIT for t in deadlines)]
    max_settled=max(settled.values())
    release_sets=[set(s) for s in launches]
    simultaneous=len(release_sets[0]&release_sets[1])
    total_releases=len(release_sets[0]|release_sets[1])
    return {'policy':policy,'gain':gain,'max_active_workers':peak_workers,'queue_capacity_per_route':0,
       'completed_jobs':completed,'busy_scheduler_units':work,'control_updates':len(updates),
       'different_version_update_fraction':sum(not same for same in paired)/len(paired),
       'simultaneous_release_fraction':simultaneous/total_releases,
       'release_intervals':[sorted(set(b-a for a,b in zip(s,s[1:]))) for s in launches],
       'maximum_error_outside_settling_windows':max(admissible),
       'maximum_last20_error_at_deadline':max_settled,
       'rms_tracking_error':math.sqrt(sum(e*e for e in errors)/len(errors)),
       'same_version_checks':aligned_checks,'numerically_checked_no_kick_predictions':prediction_checks,
       'maximum_consumed_sample_age':max(ages),'freshness_violations':sum(age>AGE_LIMIT for age in ages),
       'two_report_update_fraction':sum(n==2 for n in report_counts)/len(report_counts),
       'passes_tracking_contract':max(admissible)<TRACK_LIMIT and max_settled<0.03,
       'passes_control_contract':max(admissible)<TRACK_LIMIT and max_settled<0.03 and max(ages)<=AGE_LIMIT,
       'peak_absolute_state':max(map(abs,states))}

results=[]
for name,delays in SCENARIOS.items():
    row={'scenario':name,'route_latencies':delays,
         'policies':[simulate(p,delays) for p in ('fixed_tact','completion_barrier','independent_pair','independent_fresh')]}
    # Contract failure is an experimental outcome, not a reason to relax
    # the thresholds or suppress a scenario.
    assert row['policies'][2]['freshness_violations']>0
    assert all(p['max_active_workers']<=2 for p in row['policies'])
    independent=row['policies'][3]
    assert independent['different_version_update_fraction']>0.25
    assert independent['simultaneous_release_fraction']<0.5
    results.append(row)
pass_counts={p:sum(next(x for x in row['policies'] if x['policy']==p)['passes_control_contract'] for row in results)
             for p in ('fixed_tact','completion_barrier','independent_pair','independent_fresh')}
# Explicit post-baseline diagnostic sweep; original results remain above.
# No threshold, budget, delay sequence or policy is changed in this sweep.
sensitivity=[]
for gain in (0.025,0.035,0.05,0.075,0.15,0.20):
    cases=[]
    for name,delays in SCENARIOS.items():
        policies=[simulate(p,delays,gain) for p in ('fixed_tact','completion_barrier','independent_pair','independent_fresh')]
        cases.append({'scenario':name,'policies':policies})
    sensitivity.append({'gain':gain,'policy_pass_counts':{
        p:sum(next(z for z in c['policies'] if z['policy']==p)['passes_control_contract'] for c in cases)
        for p in ('fixed_tact','completion_barrier','independent_pair','independent_fresh')},'scenarios':cases})
assert next(s for s in sensitivity if s['gain']==GAIN)['scenarios']==[
    {'scenario':r['scenario'],'policies':r['policies']} for r in results]
report={'passed':True,'passed_means':'experiment integrity checks, not success of every control policy',
 'policy_contract_pass_counts':pass_counts,
 'definition_of_shared_tact':'a common periodic release/commit schedule or a barrier requiring both routes to finish a common version before either advances',
 'independent_policy':'each route immediately starts its next job on completion; controller updates on arrivals; no join barrier; fresh variant excludes over-age reports from the current control calculation',
 'shared_information_not_eliminated':['source-version timestamps','known actuator integral','common plant model','physical scheduler used to simulate causality'],
 'resource_budget':{'workers':2,'max_jobs_per_worker':1,'queued_jobs':0,'messages_per_completion':1},
 'control_contract':{'horizon':HORIZON,'gain_for_all_policies':GAIN,'max_age_at_update':AGE_LIMIT,
   'settling_deadline':SETTLE_LIMIT,'max_error_outside_settling':TRACK_LIMIT,'max_last20_error_at_deadline':0.03},
 'scenarios':results,'post_baseline_gain_sensitivity':sensitivity,
 'conclusion':'The naive independent policy violates freshness. Freshness gating is tested separately; its tracking/deadline successes and failures are retained in the per-scenario results. No universal necessity or sufficiency claim follows from this finite experiment.',
 'limits':['finite deterministic schedules, not an adversarial-delay or asymptotic stability theorem',
           'plant model is exact except for specified unannounced additive kicks',
           'equal resource capacity does not imply equal completed-work count; waiting policies can idle',
           'no processor contention, sensor noise, communication loss, model-parameter uncertainty, or Planck-scale physics']}
(ROOT/'research/voevodsky/results/bounded-resource-tact-challenge.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'baseline_policy_pass_counts':pass_counts,
 'post_baseline_sensitivity':[{'gain':s['gain'],'pass_counts':s['policy_pass_counts']} for s in sensitivity]},indent=2))
