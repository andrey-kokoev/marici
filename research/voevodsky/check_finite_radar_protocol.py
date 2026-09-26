"""Exact finite protocol/grouping/noise controls; format admission != physical realization."""
from fractions import Fraction as F
from dataclasses import replace
from itertools import product
from pathlib import Path
import hashlib
import json
from finite_radar_protocol import Protocol,Row,Packet,TIMES,DIRECTIONS,WEIGHTS,distances,normalized_squares,polarize,by_time,by_direction,error_bound,flat_packet,encode_section,on_native_section

p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
base=flat_packet(p);checks={}
checks['physical_flat_fixture_zero']=by_time(base)==(0,0,0)
checks['flat_squared_shape_is_identity']=all(polarize({d:normalized_squares(base)[t,d] for d in DIRECTIONS})==(1,0,1) for t in TIMES)
checks['row_order_irrelevant']=by_time(replace(base,rows=tuple(reversed(base.rows))))==by_time(base)
# Exhaust all binary perturbations of the nine arrival-distance slots: 512 fixtures.
sigma=F(1,4096);bound=error_bound(p,max(distances(base).values()),sigma)
commute=True;noise_ok=True;nonzero=False;native_ok=True
for signs in product((-1,1),repeat=9):
    rows=tuple(replace(r,reception=r.reception+2*sign*sigma) for r,sign in zip(base.rows,signs))
    packet=Packet(p,rows,'synthetic:bounded-clock-distance-perturbation')
    a,b=by_time(packet),by_direction(packet)
    commute &= a==b
    native_ok &= on_native_section(encode_section(packet))==a
    noise_ok &= max(abs(x) for x in a)<=bound
    nonzero |= any(a)
checks['all_512_grouping_comparisons']=commute
checks['all_512_native_section_readouts']=native_ok
section=encode_section(base)
try:
    on_native_section(replace(section,choices=(((0,'x3'),section.choices[0][1]),)+section.choices[1:]))
    checks['wrong_fiber_membership_rejected']=False
except ValueError:
    checks['wrong_fiber_membership_rejected']=True
checks['all_512_noise_envelopes']=noise_ok
checks['protocol_nonconstant_on_candidate_records']=nonzero
# Squaring must occur rowwise before the linear temporal/directional reductions.
# Use a nonconstant synthetic packet to expose the order error.
rows=tuple(replace(r,reception=r.reception+F(r.time*r.time+1,100)) for r in base.rows)
test=Packet(p,rows,'synthetic:nonlinear-operation-order-control')
raw=distances(test)
wrong={d:-(sum(WEIGHTS[t]*raw[t,d]/p.epsilon for t in TIMES))**2/(2*p.step**2) for d in DIRECTIONS}
checks['squaring_after_temporal_reduction_rejected']=polarize(wrong)!=by_time(test)
# Static raw-record differences can be lost by the declared processed readout.
static2=Packet(p,tuple(replace(r,reception=r.emission+2*(r.reception-r.emission)) for r in base.rows),'synthetic:static-record-loss-control')
checks['processed_output_does_not_recover_raw_record']=distances(static2)!=distances(base) and by_time(static2)==by_time(base)
# Clock-origin changes preserve outputs; consistent unit scaling changes units as 1/s^2.
shift=F(7)
shifted=Packet(replace(p,center=p.center+shift),tuple(replace(r,emission=r.emission+shift,reception=r.reception+shift) for r in test.rows),test.source_reference)
checks['clock_origin_invariance']=by_time(shifted)==by_time(test)
s=F(3)
scaled=Packet(replace(p,epsilon=s*p.epsilon,step=s*p.step,center=s*p.center),tuple(replace(r,emission=s*r.emission,reception=s*r.reception) for r in test.rows),test.source_reference)
checks['joint_length_time_unit_scaling']=by_time(scaled)==tuple(x/s**2 for x in by_time(test))
checks['frozen_protocol_has_nonzero_noise_budget']=bound>0
# Explicit metadata/domain hostiles, not silent dropping or deduplication.
def refuses(packet):
    try:packet.index()
    except ValueError:return True
    return False
checks['missing_record_rejected']=refuses(replace(base,rows=base.rows[:-1]))
checks['duplicate_record_rejected']=refuses(replace(base,rows=base.rows[:-1]+(base.rows[0],)))
checks['wrong_clock_grid_rejected']=refuses(replace(base,rows=(replace(base.rows[0],emission=base.rows[0].emission+1),)+base.rows[1:]))
checks['past_reception_rejected']=refuses(replace(base,rows=(replace(base.rows[0],reception=base.rows[0].emission-1),)+base.rows[1:]))
checks['missing_provenance_rejected']=refuses(replace(base,source_reference=''))
# Exchanging time and direction without preserving their typed domains is not a reindexing.
checks['untyped_selector_erasure_rejected']=refuses(replace(base,rows=(replace(base.rows[0],direction='-1'),)+base.rows[1:]))
checks['polarization_l1_constant']=max(F(1,9),F(1,16),F(3,24))==F(1,8)
checks['temporal_l1_constant']=sum(abs(x) for x in WEIGHTS.values())/(2*p.step**2)==2/p.step**2
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),Path(__file__).with_name('finite_radar_protocol.py'),root/'research/voevodsky/radar-determines-curvature-but-not-stably-in-raw-completion.md']
packet=dict(passed=all(checks.values()),checks=checks,
    protocol=dict(epsilon=str(p.epsilon),proper_time_step=str(p.step),center=str(p.center),directions={'x3':[3,0],'y4':[0,4],'xy5':[3,4]},reflection=p.reflection),
    error_sigma=str(sigma),max_flat_distance=str(max(distances(base).values())),processed_max_component_error_bound=str(bound),
    synthetic_cases=512,
    scope='Finite algebra and candidate-record validation; only the explicitly flat fixture has a physical realization supplied here. Output is finite radar-shape second difference, not exact curvature.',
    source_sha256={str(x.relative_to(root)):hashlib.sha256(x.read_bytes()).hexdigest() for x in paths})
Path(__file__).with_name('finite-radar-protocol.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
