"""Exact distributed observer-decision test on the admitted source history.

Observer A reads the INITIAL terminal aP+aQ. Observer B reads an affine
presentation of the FINAL canonical vacuum aP after appending P-Q twice.
Task: certify the sign of aQ with margin 1/20 by deadline 5. This is a
source-decision task, not a simulation of subsequent physical actuation.
"""
from pathlib import Path
from fractions import Fraction as Q
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
n=runpy.run_path(str(ROOT/'research/nima/checkers/check_uncertain_presentation_history_bridge.py'))
a=n['a'];mm=n['mm'];polygon=n['polygon'];inequalities=n['inequalities'];f=a.f
H=[Q(1),Q(-1)]
T10=a.action(H,1);T=mm(a.action(H,2),T10)
vacuum=(('e',0,1,0),('e',3,7,0),('e',15,31,0))
for q in a.basis(2):
    full=a.paths(a.apply(T,q),0,3)
    assert full==f['multiply'](f['multiply'](a.paths(q,0,1),a.paths(H,1,1)),a.paths(H,2,1))
    assert f['vacuum_rows'](0,63,full,3).get(vacuum,0)==q[0]
    assert not f['rho_column'](0,full)
PRIOR=inequalities([[Q(1),Q(0)],[Q(0),Q(1)]],[[-Q(2),Q(2)],[-Q(2),Q(2)]])
DEADLINE=5;MARGIN=Q(1,20)
def records(q):
    total=sum(q);display=2*q[0]+3
    return {
      'A':{'id':'A-initial-terminal','observer':'A','history_id':'append-two-forgotten-diamonds-v1',
        'source_stage':0,'sample_time':0,'completion_time':1,'anchor':[Q(1),Q(1)],
        'gain':Q(1),'offset':Q(0),'interval':[total-Q(1,10),total+Q(1,10)]},
      'B':{'id':'B-final-vacuum-affine','observer':'B','history_id':'append-two-forgotten-diamonds-v1',
        'source_stage':2,'sample_time':2,'completion_time':4,'anchor':[Q(1),Q(0)],
        'gain':Q(2),'offset':Q(3),'interval':[display-Q(1,5),display+Q(1,5)]}}
def fiber(evidence):
    constraints=list(PRIOR)
    for report in evidence:
        assert report['history_id']=='append-two-forgotten-diamonds-v1'
        gain,offset=report['gain'],report['offset']
        lo,hi=sorted((bound-offset)/gain for bound in report['interval'])
        constraints+=inequalities([report['anchor']],[(lo,hi)])
    return polygon(constraints)
def certify(points):
    if not points:return 'inconsistent'
    lo=min(p[1] for p in points);hi=max(p[1] for p in points)
    return 'positive' if lo>=MARGIN else 'negative' if hi<=-MARGIN else 'undetermined'
def wired(report):
    return {key:([str(v) for v in val] if key in ('anchor','interval') else str(val) if key in ('gain','offset') else val)
            for key,val in report.items()}
def run(q,back_delay):
    rec=records(q);forward_delay=3
    arrivals={
      'A':[(1,rec['A']),(4+back_delay,rec['B'])],
      'B':[(4,rec['B']),(1+forward_delay,rec['A'])]}
    decisions={};snapshots={};traces={};ack_arrival={}
    for observer in ('A','B'):
        evidence=[];trace=[];issued=None
        for now in sorted({time for time,r in arrivals[observer]}):
            evidence.extend(r for time,r in arrivals[observer] if time==now)
            points=fiber(evidence)
            assert points and all(a.dot(row,q)<=bound for row,bound in PRIOR)
            # Truth containment is checked against all admitted evidence, not
            # supplied to the decision rule (which sees only the polygon).
            for r in evidence:
                value=r['gain']*a.dot(r['anchor'],q)+r['offset']
                assert r['interval'][0]<=value<=r['interval'][1]
            certificate=certify(points)
            trace.append({'time':now,'evidence_ids':[r['id'] for r in evidence],
                          'aQ_interval':[str(min(p[1] for p in points)),str(max(p[1] for p in points))],
                          'certificate':certificate})
            if certificate in ('positive','negative') and issued is None:
                issued=now;decisions[observer]={'time':now,'certificate':certificate}
        traces[observer]=trace
        visible=[r for time,r in arrivals[observer] if time<=DEADLINE]
        snapshots[observer]=[wired(r) for r in visible]
        assert issued is not None
        # Same acknowledgement messages are available to every policy;
        # independent certification does not wait for their delivery.
        recipient='B' if observer=='A' else 'A'
        ack_arrival[recipient]=issued+(forward_delay if observer=='A' else back_delay)
    final=fiber(list(rec.values()))
    assert final==fiber(list(reversed(list(rec.values()))))
    assert certify(fiber([rec['A']]))==certify(fiber([rec['B']]))=='undetermined'
    independent_pass=all(d['time']<=DEADLINE for d in decisions.values())
    # A scheduled commit at 5 also works when evidence is available. No
    # claim that only the asynchronous policy succeeds is manufactured.
    fixed_pass=independent_pass
    # This PARTICULAR handshake waits until both ready acknowledgements
    # have arrived; it is not a lower bound on every barrier protocol.
    handshake_time=max(max(d['time'] for d in decisions.values()),max(ack_arrival.values()))
    return {'source_pair':[str(x) for x in q],'B_to_A_message_delay':back_delay,
      'local_traces':traces,'evidence_at_deadline':snapshots,'independent_decisions':decisions,
      'independent_meets_deadline':independent_pass,'fixed_commit_at_5_meets_deadline':fixed_pass,
      'mutual_ready_acknowledgement_time':handshake_time,
      'mutual_ack_protocol_meets_deadline':handshake_time<=DEADLINE,
      'joint_initial_source_polygon':[[str(x) for x in p] for p in final],
      'full_history_vertices':[[str(x) for x in a.apply(a.basis(2)+T10+T[1:],p)] for p in final]}
positive=(Q(7,10),Q(3,10));negative=(Q(13,10),Q(-3,10))
fast=[run(q,1) for q in (positive,negative)]
slow=[run(q,6) for q in (positive,negative)]
for case in fast:
    assert case['independent_meets_deadline'] and case['fixed_commit_at_5_meets_deadline']
    assert case['independent_decisions']['B']['time']==4
    assert case['independent_decisions']['A']['time']==5
    assert case['mutual_ready_acknowledgement_time']==8
    assert not case['mutual_ack_protocol_meets_deadline']
for case in slow:assert not case['independent_meets_deadline']
# An information-theoretic obstruction, not just a failed controller:
# A's entire received evidence at the deadline is identical in two worlds
# requiring opposite certificates. No rule using that transcript can
# always issue the correct sign in both worlds by the deadline.
assert slow[0]['evidence_at_deadline']['A']==slow[1]['evidence_at_deadline']['A']
assert slow[0]['independent_decisions']['A']['certificate']=='positive'
assert slow[1]['independent_decisions']['A']['certificate']=='negative'
assert certify(fiber([records(positive)['A']]))=='undetermined'
# Coordinate transfer matters; treating B's affine display as the canonical
# vacuum value makes otherwise valid evidence inconsistent with the prior.
r=records(positive);bad=dict(r['B'],gain=Q(1),offset=Q(0))
assert not fiber([r['A'],bad])
# Initial and final terminal evidence are distinct. The actual final source
# is in I, hence has terminal zero; moving A's initial terminal report to
# that final terminal row creates a false contradiction.
bad=dict(r['A'],source_stage=2,anchor=[Q(0),Q(0)])
assert not fiber([bad,r['B']])
report={'passed':True,'decision_task':'certify sign of initial aQ with margin 1/20, at each observer by time 5',
 'source_history':'the admitted initial P/Q pair, followed by P-Q in blocks two and three',
 'shared_contract':['source/history identity','stage labels','affine observation anchors','interval error bounds','message timing model'],
 'not_required_by_independent_policy':['simultaneous sampling','confirmation of the peer evidence version','mutual readiness acknowledgement','common commit time'],
 'source_prior':['-2 <= aP <= 2','-2 <= aQ <= 2'],
 'bounded_protocol':{'observations_per_observer':1,'processing_jobs_per_observer':1,
    'cross_observer_data_messages':2,'acknowledgement_messages':2,
    'policies_share_the_same_evidence_and_message_schedules':True},
 'fast_cases':fast,'delayed_cases':slow,
 'checks':{'source_anchors_rebuilt_from_actual_products':True,'whole_correlated_history_preserved':True,
   'independent_local_certificates_meet_common_deadline_without_common_commit':True,
   'scheduled_commit_can_also_succeed':True,
   'specified_ack_barrier_can_miss_deadline':True,
   'identical_local_transcripts_require_opposite_decisions_in_delayed_case':True,
   'presentation_and_stage_confusion_rejected_by_inconsistency':True},
 'scope':'Exact synthetic finite observer-decision experiment, not actuation or closed-loop stability. Dynamics, support, error bounds and reliable message times are admitted. No claim about arbitrary distributed agreement tasks, physical acquisition or a fundamental time quantum.'}
(ROOT/'research/voevodsky/results/observer-coordination-deadline.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'fast_local_decision_times':fast[0]['independent_decisions'],
 'specified_barrier_time':fast[0]['mutual_ready_acknowledgement_time'],
 'deadline':DEADLINE,'delayed_local_decision_times':slow[0]['independent_decisions'],
 'indistinguishable_local_transcript_obstruction':True},indent=2))
