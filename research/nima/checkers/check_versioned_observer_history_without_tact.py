"""Temporal observer coherence without a shared release/completion barrier.

Exact bounded-error integrator histories, immutable versioned interval reports,
and two algebraically equivalent routes. No control-performance theorem.
"""
from pathlib import Path
from fractions import Fraction as Q
import ast,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OWNER=ROOT.parent/'voevodsky/checkers/check_bounded_resource_tact_challenge.py'
tree=ast.parse(OWNER.read_text())
SCHEDULES=next(ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign)
               and any(isinstance(target,ast.Name) and target.id=='SCENARIOS' for target in node.targets))
HORIZON=48;AGE=12;DELTA=Q(1,10);SENSOR=Q(1,50)


def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def affine(interval,g,b):return sorted((g*interval[0]+b,g*interval[1]+b))
def transport(interval,s,t,U,delta):
    if t<s:raise ValueError('forward time required')
    return [interval[0]+U[t]-U[s]-(t-s)*delta,interval[1]+U[t]-U[s]+(t-s)*delta]


class EmptyHistory(ValueError):pass


class History:
    """Closed difference-bound matrix: d[i][j] bounds x_j-x_i.

    Node 0 is the constant zero; node t+1 is x[t]. Contains the whole joint
    trajectory constraint, not a Cartesian product of state marginals.
    """
    def __init__(self,U,delta):
        n=len(U);self.d=[[Q(0)]*(n+1) for _ in range(n+1)]
        for t in range(n):
            self.d[0][t+1]=Q(1)+U[t]+t*delta
            self.d[t+1][0]=Q(1)-U[t]+t*delta
            for s in range(n):self.d[t+1][s+1]=U[s]-U[t]+abs(s-t)*delta
    def constrain(self,i,j,c):
        d=self.d
        if c+d[j][i]<0:raise EmptyHistory('joint evidence contradicts the declared model')
        if c>=d[i][j]:return
        left=[row[i] for row in d];right=d[j][:]
        self.d=[[min(value,left[a]+c+right[b]) for b,value in enumerate(row)] for a,row in enumerate(d)]
    def observe(self,report):
        lo,hi=map(Q,report['interval']);node=report['sample_time']+1
        if lo>hi:raise ValueError('reversed report interval')
        self.constrain(0,node,hi);self.constrain(node,0,-lo)
    def bounds(self,t):return [-self.d[t+1][0],self.d[0][t+1]]


def closure(matrix):
    # Independent cubic-time closure for checking the incremental implementation.
    d=[row[:] for row in matrix]
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    if any(d[i][i]<0 for i in range(len(d))):raise EmptyHistory('negative cycle')
    return d


def simulate(name,latencies):
    commands=[Q((t%7)-3,100) for t in range(HORIZON)]
    U=[Q(0)]
    for u in commands:U.append(U[-1]+u)
    # Used ONLY by the fixture producer and containment oracle, not by History
    # or transport. Receivers know DELTA, not these disturbance locations/values.
    kicks={7:Q(1,10),19:Q(-2,25),33:Q(9,100)}
    truth=[Q(0)]
    for t,u in enumerate(commands):truth.append(truth[-1]+u+kicks.get(t+1,Q(0)))
    history=History(U,DELTA);jobs=[None,None];seq=[0,0];latest=[None,None]
    archive=[];frozen={};launches=[[],[]];work=[0,0];decisions=[]
    mixed=0;expired=0;single=0;coherence=0;point_misses=0;path_checks=0
    frames=((Q(1),Q(0)),(Q(2),Q(1)),(Q(-1),Q(3)))
    for now in range(HORIZON+1):
        arrivals=[]
        for route in (0,1):
            job=jobs[route]
            if job is not None and job['completion_time']==now:
                jobs[route]=None;archive.append(job);frozen[job['id']]=digest(job)
                latest[route]=job;history.observe(job);arrivals.append(job)
        if arrivals:
            selected=[report for report in latest if report is not None and now-report['sample_time']<=AGE]
            omitted=[report for report in latest if report is not None and now-report['sample_time']>AGE]
            expired+=len(omitted);single+=int(len(selected)==1)
            mixed+=int(len(selected)==2 and selected[0]['sample_time']!=selected[1]['sample_time'])
            assert selected # A newly completed job has latency at most AGE.
            predicted=[]
            for report in selected:
                s=report['sample_time'];original=list(map(Q,report['interval']))
                assert report['command_integral']==str(U[s])
                aligned=transport(original,s,now,U,DELTA)
                assert aligned[0]<=truth[now]<=aligned[1]
                midpoint=sum(original)/2+U[now]-U[s]
                point_misses+=int(abs(midpoint-truth[now])>SENSOR)
                for gain,offset in frames:
                    observer=affine(original,gain,offset)
                    shifted=[observer[0]+gain*(U[now]-U[s])-abs(gain)*(now-s)*DELTA,
                             observer[1]+gain*(U[now]-U[s])+abs(gain)*(now-s)*DELTA]
                    assert affine(shifted,1/gain,-offset/gain)==aligned
                    coherence+=1
                middle=(s+now)//2
                assert transport(transport(original,s,middle,U,DELTA),middle,now,U,DELTA)==aligned
                path_checks+=1;predicted.append(aligned)
            intersection=[max(i[0] for i in predicted),min(i[1] for i in predicted)]
            assert intersection[0]<=truth[now]<=intersection[1]
            joint=history.bounds(now)
            assert intersection[0]<=joint[0]<=truth[now]<=joint[1]<=intersection[1]
            decisions.append({'time':now,'current_report_ids':[r['id'] for r in selected],
                              'excluded_as_stale_ids':[r['id'] for r in omitted],
                              'fresh_report_intersection':list(map(str,intersection)),
                              'retained_history_projection':list(map(str,joint))})
        if now==HORIZON:break
        for route in (0,1):
            if jobs[route] is None:
                number=seq[route];seq[route]+=1
                delay=latencies[route][number%len(latencies[route])]
                center=truth[now]+Q((-1)**(number+route),100)
                # Immutable sampled value shared within this algebraic route.
                left=Q(1,2)*(Q(1,2)+Q(3,2))*center
                right=Q(1,2)*Q(1,2)*center+Q(1,2)*Q(3,2)*center
                assert left==right==center
                jobs[route]={'id':name+':'+str(route)+':'+str(number),'route':route,
                    'sample_time':now,'completion_time':now+delay,
                    'interval':[str(center-SENSOR),str(center+SENSOR)],
                    'command_integral':str(U[now]),'normalization':'unit source-state observation',
                    'provenance':'synthetic bounded sensor interval'}
                launches[route].append(now)
            work[route]+=1
    # Every expired report is still present and unchanged in the evidence archive.
    assert all(digest(report)==frozen[report['id']] for report in archive)
    archived_ids={report['id'] for report in archive}
    assert all(set(decision['excluded_as_stale_ids'])<=archived_ids for decision in decisions)
    reverse=History(U,DELTA)
    for report in reversed(archive):reverse.observe(report)
    assert reverse.d==history.d # Order-independent intersection of joint evidence.
    raw=History(U,DELTA).d
    for report in archive:
        lo,hi=map(Q,report['interval']);node=report['sample_time']+1
        raw[0][node]=min(raw[0][node],hi);raw[node][0]=min(raw[node][0],-lo)
    assert closure(raw)==history.d
    assert mixed>0 and point_misses>0
    # Joint path constraints must not be replaced by independent state intervals.
    bad_marginals=False
    for time in range(HORIZON):
        lo=history.bounds(time)[0];hi=history.bounds(time+1)[1]
        if hi-lo>commands[time]+DELTA:bad_marginals=True;break
    assert bad_marginals
    zero_budget=History(U,Q(0));zero_rejected=False
    try:
        for report in archive:zero_budget.observe(report)
    except EmptyHistory:zero_rejected=True
    assert zero_rejected
    contradiction=json.loads(json.dumps(archive[0]));contradiction['interval']=['10','11']
    inconsistent=History(U,DELTA)
    for report in archive:inconsistent.observe(report)
    try:inconsistent.observe(contradiction)
    except EmptyHistory:pass
    else:raise AssertionError('contradictory evidence accepted')
    pending=[job for job in jobs if job is not None]
    assert len(archive)+len(pending)==sum(seq)
    assert all(job['completion_time']>HORIZON for job in pending)
    common=set(launches[0])&set(launches[1])
    assert len(common)<len(set(launches[0])|set(launches[1]))
    result={'scenario':name,'completed_reports':len(archive),'pending_worker_snapshots_retained':len(pending),'mixed_version_updates':mixed,
        'single_fresh_report_updates':single,'stale_exclusions_retained':expired,
        'frame_time_squares':coherence,'time_composition_checks':path_checks,
        'point_predictor_misses_sensor_only_bound':point_misses,
        'launch_times':launches,'busy_worker_units':work,
        'coincident_releases':len(common),'archive_sha256':digest(archive),
        'checks':{'joint_history_independent_of_arrival_order':True,
                  'incremental_history_matches_independent_full_closure':True,
                  'truth_contained_without_receiver_access_to_kicks':True,
                  'archived_stale_reports_unchanged':True,'independent_marginals_lose_dynamics':True,
                  'unjustified_zero_disturbance_model_rejected':zero_rejected,
                  'contradictory_evidence_gives_empty_history':True}}
    evidence={'scenario':name,'commands':list(map(str,commands)),
              'model':{'plant':'x[t+1]=x[t]+u[t]+w[t+1]','initial_state_interval':['-1','1'],
                       'disturbance_per_step_bound':str(DELTA),'sensor_radius':str(SENSOR),
                       'unknown_to_receiver':'actual kick locations and values'},
              'retained_reports':archive,'pending_worker_snapshots':pending,
              'pending_visibility':'worker-retained, not yet delivered and not used in observer updates',
              'decisions':decisions,
              'joint_history':{'meaning':'matrix entry i,j bounds x_j-x_i; node 0 is constant zero, node t+1 is state at t',
                               'closed_difference_bounds':[[str(x) for x in row] for row in history.d]}}
    return result,evidence


def main():
    results=[];example=None
    for name,schedules in SCHEDULES.items():
        result,evidence=simulate(name,schedules);results.append(result)
        if name=='bursty_skew':example=evidence
    assert sum(result['stale_exclusions_retained'] for result in results)>0
    report={'schema':'versioned-observer-history-without-tact-v1','passed':True,
        'owning_schedule_source_sha256':hashlib.sha256(OWNER.read_bytes()).hexdigest(),
        'resource_contract':'two dedicated single-job workers, no queue, independent immediate restarts, one report per completion',
        'shared_tact_definition':'common periodic release/commit schedule or repeated completion barrier; neither is imposed',
        'retained_common_structure':'causal timestamps, known command history, source/observer labels and explicit error bounds',
        'scenarios':results,
        'scope':'Exact temporal coherence/retention test, not a controller. Open-loop commands and a declared conservative disturbance bound are used. No tracking, settling, equal-energy, adversarial-delay, packet-loss or shared-processor theorem is claimed.'}
    directory=ROOT/'results/versioned-observer-history';directory.mkdir(exist_ok=True)
    (directory/'tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (directory/'retained-history-example.json').write_text(json.dumps(example,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
