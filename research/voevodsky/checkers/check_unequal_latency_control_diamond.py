"""Deterministic unequal-cost control diamond; standard library only.

Plant: x[k+1]=x[k]+u[k]. Controller: u=-g*y, zero-order-held between
updates. Two linear routes implement A(B+C)x=ABx+ACx=x at the SAME
source version. Delays are stipulated integer scheduler units, not a
physical fundamental tick. Event-driven policy has no fixed update period.
"""
from pathlib import Path
from fractions import Fraction as Q
import math,json
ROOT=Path(__file__).resolve().parents[3]
A=Q(1,2);B=Q(1,2);C=Q(3,2)
def sp(x):return A*((B+C)*x)
def ps(x):return A*(B*x)+A*(C*x)
for x in map(Q,('0','1','-2','3/7')):assert sp(x)==ps(x)==x
HORIZON=240
GAIN=0.08

def simulate(policy,gain=GAIN,slow_extra=0):
    fast_delays=(1,2,1,2)
    slow_delays=tuple(d+slow_extra for d in (3,5,4,6))
    period=max(slow_delays)
    pending={};matched={};latest={};x=1.0;u=0.0;version=0
    launches=[];updates=[];discrepancies=[];states=[];next_launch=0;ready=None
    def launch(k,value):
        nonlocal version
        v=version;version+=1;launches.append(k)
        # The actual operators agree; only scheduling differs. Both receive
        # the identical immutable source snapshot on this launch.
        for name,delay,operator in (('SP',fast_delays[v%4],sp),('PS',slow_delays[v%4],ps)):
            reading=float(operator(Q.from_float(value)))
            pending.setdefault(k+delay,[]).append({'route':name,'version':v,'sample_time':k,'value':reading})
    for k in range(HORIZON):
        # Complete work before launching the next fixed/event batch.
        arrivals=pending.pop(k,[])
        for item in arrivals:
            latest[item['route']]=item
            matched.setdefault(item['version'],{})[item['route']]=item
        complete=[v for v,pair in matched.items() if len(pair)==2]
        for v in sorted(complete):
            pair=matched.pop(v)
            assert pair['SP']['sample_time']==pair['PS']['sample_time']
            assert pair['SP']['value']==pair['PS']['value']
            if policy!='free_running':
                assert ready is None
                ready=pair
        if arrivals and len(latest)==2:
            discrepancies.append({'time':k,'absolute_difference':abs(latest['SP']['value']-latest['PS']['value']),
              'same_version':latest['SP']['version']==latest['PS']['version']})
        if policy=='free_running':
            if arrivals and len(latest)==2:
                u=-gain*(latest['SP']['value']+latest['PS']['value'])/2
                updates.append({'time':k,'same_version':latest['SP']['version']==latest['PS']['version'],
                                'max_age':max(k-z['sample_time'] for z in latest.values())})
            launch(k,x)
        elif policy in ('fixed_tact','version_barrier'):
            commit=(ready is not None and
                    (policy=='version_barrier' or k==next_launch))
            if commit:
                # Fixed tact waits for the scheduled common boundary;
                # the event barrier commits as soon as both routes finish.
                assert ready['SP']['version']==ready['PS']['version']
                u=-gain*ready['SP']['value']
                updates.append({'time':k,'same_version':True,'max_age':k-ready['SP']['sample_time']})
                ready=None
                if policy=='version_barrier':next_launch=k
            if k==next_launch:
                launch(k,x)
                next_launch=(k+period if policy=='fixed_tact' else -1)
        else:raise ValueError('policy')
        # One common, declared disturbance tests response after settling.
        x+=u+(0.2 if k==120 else 0)
        assert math.isfinite(x)
        states.append(x)
    return {'policy':policy,'gain':gain,'slow_extra':slow_extra,
      'launch_intervals':sorted(set(b-a for a,b in zip(launches,launches[1:]))),
      'launches':len(launches),'control_updates':len(updates),
      'mismatched_control_updates':sum(not z['same_version'] for z in updates),
      'maximum_update_age':max(z['max_age'] for z in updates),
      'maximum_unmatched_latest_output_difference':max(z['absolute_difference'] for z in discrepancies),
      'peak_absolute_state':max(map(abs,states)),
      'last_40_state_rms':math.sqrt(sum(x*x for x in states[-40:])/40),
      'final_state':states[-1]}

ordinary=[simulate(policy) for policy in ('free_running','fixed_tact','version_barrier')]
assert ordinary[0]['mismatched_control_updates']>0
assert ordinary[0]['maximum_unmatched_latest_output_difference']>0
assert all(r['mismatched_control_updates']==0 for r in ordinary[1:])
assert len(ordinary[1]['launch_intervals'])==1
assert len(ordinary[2]['launch_intervals'])>1
assert all(r['last_40_state_rms']<0.02 for r in ordinary)
# Agreement is not sufficient for control performance. Use the same gain
# and a longer slow path, keeping source-version matching intact.
# Hold the gain FIXED to isolate the latency change.
stale=[simulate(policy,gain=GAIN,slow_extra=24) for policy in ('fixed_tact','version_barrier')]
assert all(r['mismatched_control_updates']==0 for r in stale)
assert all(r['peak_absolute_state']>10 for r in stale)
report={'passed':True,'route_identity':'A(B+C)x = ABx+ACx = x',
 'cost_model':{'fast_latencies':[1,2,1,2],'slow_latencies':[3,5,4,6],
   'assumptions':'unlimited parallel jobs for free-running; one outstanding batch otherwise; no queue contention'},
 'plant':'x[k+1]=x[k]+u[k], u=-gain*y held until next controller update',
 'ordinary_cases':ordinary,'stale_same_gain_cases':stale,
 'checks':{'same_version_route_outputs_equal':True,'free_running_can_mix_versions':True,
   'fixed_tact_and_event_barrier_both_align_versions':True,
   'event_barrier_operates_with_nonconstant_intervals':True,
   'aligned_but_stale_feedback_can_fail':True},
 'interpretation':'Unequal route cost motivates explicit version alignment and freshness constraints. Fixed tact is sufficient here, not necessary; an event-driven barrier also works. Mismatch is not by itself a proof of instability.',
 'scope':'Finite deterministic control experiment with stipulated costs and float plant simulation. Finite-horizon behavior is not an asymptotic stability theorem. Scheduler units do not establish a physical minimum time or Planck-scale interpretation.'}
(ROOT/'research/voevodsky/results/unequal-latency-control-diamond.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
