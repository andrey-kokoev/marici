# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Native-boundary validated experiment compilation and retained packet tests."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np
from labelled_exchange_experiment import Experiment

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/labelled-exchange-experiment.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    native=runpy.run_path(str(HERE/'check_shared_leg_dg_realization.py'))
_,boundary,_,_,routes=native['build']({'a':(0,0),'s':(0,0)})
experiment=Experiment(); events=[]; witnesses=[]
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        for j in range(size):
            witness=routes(tag,i,j)[0]; witnesses.append(witness)
            label=experiment.labels[len(events)]
            events.append(experiment.compile(label,witness,boundary,'shared-leg-DG:roots00'))
assert len(events)==137

def rejected(fn):
    try: fn()
    except ValueError: return
    raise AssertionError('hostile accepted')
rejected(lambda: experiment.compile(experiment.labels[0],witnesses[1],boundary,'source'))
rejected(lambda: experiment.compile(experiment.labels[0],witnesses[0],boundary,'source',composition='native-path'))
rejected(lambda: experiment.compile(('a',(0,1),(0,2)),witnesses[0],boundary,'source'))
rejected(lambda: experiment.prepare(np.zeros(16),np.zeros(137),-np.eye(153),'bad'))

w=np.zeros(137); w[11]=1
packet=experiment.prepare(np.zeros(16),w,np.eye(153)/2,'declared-coherent-X-preparation')
word=[events[i] for i in (11,0,1,12)]
whole=experiment.run(packet,word)
split=experiment.run(experiment.run(packet,word[:2]),word[2:])
tol=1e-10
assert np.max(np.abs(experiment.state(whole)-experiment.state(split)))<tol
assert whole.history==split.history==tuple(word)
assert np.max(np.abs(whole.anchor-packet.anchor))<tol
assert np.max(np.abs(whole.covariance-packet.covariance))<tol
assert abs(experiment.state(whole)[16+11])<tol
assert np.linalg.norm(experiment.state(whole)-experiment.state(packet))>.5
returned=experiment.run(whole,reversed(word))
assert np.max(np.abs(experiment.state(returned)-experiment.state(packet)))<tol
assert len(returned.history)==8 and returned.history!=packet.history
assert returned.preparation_id==packet.preparation_id

# Two native witness routes compile to the same event operation but distinct provenance.
f,s,_=routes('a',1,1)
alternate=experiment.compile(experiment.labels[12],s,boundary,'shared-leg-DG:roots00')
p1=experiment.run(packet,[events[12]]); p2=experiment.run(packet,[alternate])
assert np.max(np.abs(experiment.state(p1)-experiment.state(p2)))<tol
assert p1.history!=p2.history

# Transport the complete state, covariance and event addresses; native witnesses
# remain in their original source frame rather than being silently rewritten.
pa=(1,2,3,0); pb=(2,0,3,1)
target,transported,O=experiment.relabel(whole,pa,pb)
_,initial_transported,_=experiment.relabel(packet,pa,pb)
other=target.run(initial_transported,transported.history)
assert np.max(np.abs(target.state(other)-target.state(transported)))<tol
assert np.max(np.abs(other.covariance-transported.covariance))<tol
for old,new in zip(whole.history,transported.history):
    assert old.witness==new.witness and old.source_label==new.source_label
    assert old.source_reference==new.source_reference
    assert new.instrument_reference==target.reference
rejected(lambda: target.run(initial_transported,word))
assert np.max(np.abs(O.T@O-np.eye(153)))<tol

# Nonisotropic covariance must also travel, not just the invariant vacuum.
v=np.arange(153,dtype=float)/153
p=experiment.prepare(np.zeros(16),w,np.outer(v,v),'declared-correlated-preparation')
p_after=experiment.run(p,word)
x0=experiment.state(p); x1=experiment.state(p_after)
assert abs(x0@x0+np.trace(p.covariance)-x1@x1-np.trace(p_after.covariance))<tol
_,t0,_=experiment.relabel(p,pa,pb)
_,t1,_=experiment.relabel(p_after,pa,pb)
t2=target.run(t0,t1.history)
assert np.max(np.abs(t1.covariance-t2.covariance))<tol

result={
 'status':'passed','classification':'conditional_native_boundary_validated_labelled_experiment_compiler',
 'tolerance':tol,
 'checks':{'all137_native_witness_boundaries_validated':True,'wrong_boundary_rejected':True,
           'native_path_flattening_rejected':True,'excluded_slot_rejected':True,
           'invalid_covariance_rejected':True,'event_concatenation':True,
           'anchor_mismatch_reconstruction':True,'distinct_witness_provenance_retained':True,
           'reference_transport_with_covariance':True,'stale_frame_rejected':True,
           'inverse_endpoint_keeps_eight_event_history':True},
 'conclusion':'A reusable compiler now validates source witness boundaries and executes attached-memory exchange experiments while retaining preparation identity, source provenance, anchors, mismatches, covariance and chronological histories. It deliberately does not claim native shared-leg operator factorization.',
 'missing':['native_selection_of_attachment_and_pulse','physical_preparation_and_detector_calibration',
            'absolute_current_field_coupling'],
 'next_falsifier':'Audit a complete prepared and measured experiment through this compiler, including detector gain, loss and phase uncertainty, without replacing absolute calibration by the1/137 share.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
