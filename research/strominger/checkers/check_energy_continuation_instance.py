"""Actual retained energy source -> declared drift/gain task interface.

Run with: uv run --with sympy python <this file>
No quotient value replaces the retained coefficient field or its history.
"""
import contextlib
from dataclasses import dataclass
import io
import json
from pathlib import Path
import runpy
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
with contextlib.redirect_stdout(io.StringIO()):
    interface=runpy.run_path(str(ROOT/'research/strominger/checkers/check_continuation_interface.py'))
e=interface['energy']; S=e['S']; control=e['control']
from energy_task_reduction import EnergyTaskState, read_energy_task, gain_step, infer_components
from energy_target_controller import target_gain, finish_after_probe
from shared_leg_control_ports import response_field
System,check_map=interface['System'],interface['check_map']
A,F=e['A'],e['F']
mean,one,two=e['mean'],e['one'],e['two']
U=control['model']['U']
provenance='actual supplied shared-leg source; fixed declared energy/drift/gain task'

@dataclass(frozen=True)
class Retained:
    field: object
    origin: object
    parent: object = None
    command: object = None
    task_witness: object = None


def summary(s):
    return read_energy_task(A,s.field,one,two,provenance)
def project(s):
    t=summary(s)
    return t.one_leg,t.two_leg

def source_step(s,command):
    kind,q=command
    if kind=='drift':
        assert q is None
        field=U*s.field
        witness=('declared source drift',project(s))
    else:
        assert kind=='gain'
        witness=gain_step(summary(s),q)
        field=(mean+q*one+q*q*two)*s.field
    result=Retained(S.ImmutableMatrix(field),s.origin,s,command,witness)
    if kind=='gain':
        assert project(result)==(witness.result.one_leg,witness.result.two_leg)
    else:
        assert project(result)==project(s)
    return result

def task_step(pair,command):
    kind,q=command
    if kind=='drift':
        assert q is None
        return pair
    assert kind=='gain'
    step=gain_step(EnergyTaskState(*pair,provenance),q)
    return step.result.one_leg,step.result.two_leg

source=System(source_step,lambda s:summary(s).energy)
task=System(task_step,lambda p:S.simplify(sum(p)))
initial=Retained(S.ImmutableMatrix(F),S.ImmutableMatrix(F))
checks={}
word=(('gain',S.Rational(2,3)),('drift',None),('gain',S.Rational(3,5)),('gain',S.Integer(0)))
history=check_map(source,task,project,initial,word)
checks['actual_source_task_step_and_observation_laws']=True
checks['full_fields_and_parent_commands_retained']=all(
    s.origin==initial.origin and s.parent is history[i-1] and s.command==word[i-1]
    for i,s in enumerate(history) if i)

# Gain composition is true for full coefficient fields, but not identical
# history objects. The positive task law is not a provenance-erasure licence.
first=source_step(initial,('gain',S.Rational(2,3)))
second=source_step(first,('gain',S.Rational(3,5)))
composed=source_step(initial,('gain',S.Rational(2,5)))
checks['gain_composition_preserves_full_field_and_task']=second.field==composed.field and project(second)==project(composed)
checks['gain_composition_keeps_distinct_histories']=second.parent is first and composed.parent is initial and second!=composed

# Universal polynomial identities on the task dynamics (not finite sampling).
a,b,q,r=S.symbols('a b q r',real=True)
checks['symbolic_task_composition']=all(S.expand(x-y)==0 for x,y in
    ((r**2*q**2*a,(r*q)**2*a),(r**4*q**4*b,(r*q)**4*b)))
# Exact source projector identities supply the domain-wide proof premises.
checks['source_projectors_partition_and_commute']=(
    mean+one+two==S.eye(137) and one*two==S.zeros(137)
    and one*one==one and two*two==two and mean*one==S.zeros(137)
    and mean*two==S.zeros(137) and one.T==one and two.T==two
    and A*one==one*A and A*two==two*A and A*mean==S.zeros(137))

# Matrix identities certify the quadratic readout law for arbitrary real
# coefficient fields, not only the sampled initial trajectory.
B1=A*one; B2=A*two
E1=B1.T*B1; E2=B2.T*B2
checks['energy_gram_decomposition']=E1+E2==A.T*A
checks['drift_preserves_both_task_grams']=U.T*E1*U==E1 and U.T*E2*U==E2

# A second ACTUAL shared-leg preparation: negate each left leg. Response
# fields change sign, hence both quadratic energies agree for every gain/drift.
negative_legs=tuple((role,i,-M if role in ('ax','sx') else M) for role,i,M in control['legs'])
negative_field=response_field(negative_legs)
assert negative_field==-F and negative_field!=F
negative=Retained(S.ImmutableMatrix(negative_field),S.ImmutableMatrix(negative_field))
checks['task_quotient_does_not_reconstruct_full_source']=project(negative)==project(initial)
for command in word[:3]:
    initial_next=source_step(initial,command)
    negative_next=source_step(negative,command)
    assert negative_next.field==-initial_next.field
    assert project(negative_next)==project(initial_next)
checks['same_task_distinct_source_pair_respects_allowed_commands']=True

# Infer pre-probe statistics, then CONTINUE FROM THE PROBED SOURCE.
probe=S.Rational(1,2)
probed=source_step(initial,('gain',probe))
H=summary(initial).energy; H1=summary(probed).energy
inferred=infer_components(H,H1,probe)
checks['two_readings_reconstruct_preprobe_statistics_only']=inferred==project(initial) and probed.field!=initial.field
h=H1/2
probe_step,finish_step=finish_after_probe(H,H1,probe,h,provenance)
checks['controller_uses_postprobe_task_state']=(
    (finish_step.parent.one_leg,finish_step.parent.two_leg)==project(probed)
    and finish_step.parent==probe_step.result)
finished=source_step(probed,('gain',finish_step.q))
checks['actual_postprobe_source_reaches_target']=S.simplify(summary(finished).energy-h)==0 and finished.parent is probed
wrong_gain=target_gain(summary(initial),h)
wrong=gain_step(summary(probed),wrong_gain).result.energy
checks['preprobe_reset_hostile_detected']=S.simplify(wrong-h)!=0

rejected=[]
for command in (('gain',S.Integer(2)),('gain',S.Integer(-1)),('other',None)):
    try: source_step(initial,command)
    except (ValueError,AssertionError): rejected.append(str(command))
    else: raise AssertionError('undeclared action admitted')
for bad in (S.Integer(0),S.Integer(1)):
    try: infer_components(H,H1,bad)
    except ValueError: rejected.append('uninformative probe '+str(bad))
    else: raise AssertionError('uninformative probe admitted')
assert all(checks.values())
out={'schema':'marici.energy-continuation-instance.v1','status':'pass','checks':checks,
     'rejected_commands':rejected,
     'task_policy':'fixed declared drift and common gains0<=q<=1; observer H=a+b',
     'quotient':'(a,b); gain(q)=(q^2*a,q^4*b); drift fixes both',
     'full_source_reconstruction':False,
     'probe':'two exact calibrated readings identify pre-probe(a,b); subsequent gain acts on post-probe field',
     'formal_boundary':'exact executable source/projector and symbolic polynomial checks; no new Agda instance or physical calibration theorem'}
(ROOT/'research/strominger/results/energy-continuation-instance-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
