"""Task-scoped continuation checks using the actual three source examples."""
import contextlib
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import io
import json
from pathlib import Path
import runpy
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
with contextlib.redirect_stdout(io.StringIO()):
    schedule=runpy.run_path(str(ROOT/'research/strominger/checkers/check_generating_horizontal_schedule.py'))
    relation=runpy.run_path(str(ROOT/'research/strominger/checkers/check_relation_wg_packets.py'))
    energy=runpy.run_path(str(ROOT/'research/strominger/checkers/check_energy_task_reduction.py'))
a=schedule['a']

@dataclass(frozen=True)
class System:
    step: object
    observe: object

def run(system,state,commands):
    history=[state]
    for command in commands:
        state=system.step(state,command)
        history.append(state)
    return state,tuple(history)

def check_map(source,target,projection,state,commands):
    current=state
    for command in commands:
        assert projection(source.step(current,command))==target.step(projection(current),command)
        assert target.observe(projection(current))==source.observe(current)
        current=source.step(current,command)
    end,history=run(source,state,commands)
    reduced,_=run(target,projection(state),commands)
    assert target.observe(reduced)==source.observe(end)
    return history

# Fixed task: add a known matrix offset to the independent direct reference;
# observe the weighted comparison residual. Source forests/policies stay retained.
def shift(terminal,offset):
    b=terminal.binding
    assigned=dict(b.assignment)
    assigned['d']=a['owner']['add'](b.direct_value,offset)
    return a['finish'](a['bind'](b.generated_packet,assigned),terminal.policy)

def projection(t):
    a['verify_terminal'](t)
    return a['diagram']['mean'](a['verify'](t.binding)),t.binding.direct_value
add=a['owner']['add']; scale=a['owner']['scale']
source=System(shift,a['verify_terminal'])
quotient=System(lambda s,c:(s[0],add(s[1],c)),lambda s:add(s[0],scale(-1,s[1])))
commands=(a['owner']['H'],scale(-1,a['owner']['H']),a['owner']['I'])
checks={}
for policy,nodes in schedule['examples'].items():
    upper=schedule['terminal'](nodes[-1])
    lower=schedule['terminal'](schedule['generate'](nodes[2]))
    assert upper==lower and nodes[-1].trace!=schedule['generate'](nodes[2]).trace
    history=check_map(source,quotient,projection,upper,commands)
    for i,t in enumerate(history):
        assert t.binding.generated_packet==upper.binding.generated_packet
        assert t.policy==policy
    # Two successive offsets versus their composed command.
    x=shift(shift(upper,commands[0]),commands[2])
    y=shift(upper,add(commands[0],commands[2]))
    assert x==y
    checks[policy+'_reference_task_commutes_and_composes']=True
    checks[policy+'_route_histories_not_identified']=True

# Same leaf/readout task state does not imply identity for an OUTER-family task.
x=a['terminals']['inherited']; y=a['terminals']['common']
assert projection(x)==projection(y)
next_outer=lambda t:a['promote'](a['unindex'](t.view),3,t.policy)
assert len(next_outer(x))==32 and len(next_outer(y))==1
checks['leaf_readout_quotient_fails_extended_family_task']=True

# Actual local right-b matrix versus the disconnected graded substitution.
def mv(matrix,v): return tuple(sum(a*b for a,b in zip(row,v)) for row in matrix)
R=relation['actual_action']; D=relation['graded_action']
v=(1,0,0)
assert mv(R,v)==(0,0,1) and mv(D,v)==(0,0,0)
assert mv(R,mv(R,v))==(0,0,0)
checks['equal_coordinates_do_not_authorize_changed_source_action']=True
product_arrow=relation['p4'].product
zero_arrow=relation['Arrow'](product_arrow.start,product_arrow.end,())
assert relation['observe'](product_arrow)==relation['observe'](zero_arrow)=={}
probe=product_arrow.terms[0][0]
assert dict(product_arrow.terms)[probe]!=dict(zero_arrow.terms).get(probe,0)
checks['terminal_relation_observation_does_not_supply_product_detector']=True

# Reuse the actual invertible shared-leg hostile, not an invented scalar pair.
SL,SB=energy['SL'],energy['SB']
q=energy['S'].Rational(1,2)
assert SL.energy==SB.energy and energy['gain_step'](SL,q).result.energy!=energy['gain_step'](SB,q).result.energy
checks['actual_equal_energy_hostile_rejects_current_scalar_identity']=True

# Composition/reflection scope: this turn only reuses the energy hostile.
# The positive predictive quotient/probe interface is the separate next task.
assert all(checks.values())
out={'schema':'marici.continuation-interface.v1','status':'pass','checks':checks,
     'task_map_laws':['observation preservation','step intertwining'],
     'formal_consequence':'preserves every finite command word; maps compose',
     'reflection':'not inferred; requires inverse/reconstruction data',
     'schedule_task':'declared direct-reference shifts and weighted residual',
     'schedule_countertask':'one further retained incoming promotion and outer row count',
     'relation_task':'actual right-b action and retained product coefficient detector',
     'energy_scope':'actual equal-current-energy hostile replay; positive energy interface remains separate'}
(ROOT/'research/strominger/results/continuation-interface-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
