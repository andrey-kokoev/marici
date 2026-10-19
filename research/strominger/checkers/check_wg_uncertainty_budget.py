"""Finite admitted-ensemble uncertainty on full retained WG attachments.

Exact collision budget; no statistical/physical ensemble is inferred.
"""
import contextlib
import copy
from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import lru_cache
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
# Instantiate the owner's finite square functions. Its full main additionally
# needs a saved physical model absent from this checkout; no such run claimed.
scalar=runpy.run_path(str(ROOT/'research/nima/checkers/check_source_observer_coherence.py'))
base={'model':scalar['s'].MODEL,'rows':[{'data':['-1','1'],'calibration':['1','2'],'weight':'1'} for _ in range(2)],
      'budget':'4','target':{'coefficients':['1','1'],'threshold':'0'}}
def source_edit(problem): problem['budget']='2'
def observer_edit(problem):
    for row in problem['rows']:
        lo,hi=map(F,row['calibration']); row['calibration'][1]=str((lo+hi)/2)
    problem['rows'][0]['data']=['5/2','5'];problem['rows'][1]['data']=['-7/10','7/10']
scalar_square=scalar['square'](base,[F(2),F(3)],[F(5),F(7)],source_edit,observer_edit)
assert scalar['t'].verify_square(scalar_square)
bad_scalar=copy.deepcopy(scalar_square)
bad_scalar['edges']['10->11'].update(source_scale=['2','2'],observation_scale=['10','14'],target_scale='2')
assert scalar['t'].verify_transition(bad_scalar['nodes']['10'],bad_scalar['nodes']['11'],bad_scalar['edges']['10->11'])
try: scalar['t'].verify_square(bad_scalar)
except ValueError as exc: assert 'routes' in str(exc)
else: raise AssertionError('noncommuting scalar square accepted')
with contextlib.redirect_stdout(io.StringIO()):
    w=runpy.run_path(str(ROOT/'research/strominger/checkers/check_wg_retained_assembly.py'))
S=w['S']; advance=w['advance']; validate=w['validate']

@dataclass(frozen=True)
class Alternative:
    label: str
    probability: F
    initial_commands: tuple
    state: object

@dataclass(frozen=True)
class Ensemble:
    alternatives: tuple
    shared_commands: tuple=()
    parent: object=None
    evidence: tuple=()

root=w['seed']('inherited')
@lru_cache(None)
def reconstruct(commands):
    state=root
    for command in commands: state=advance(state,command)
    return state

validated_states={}
def checked_state(state):
    # Cache only exact unchanged object snapshots, including mutable maps.
    snapshot=repr(state)
    previous=validated_states.get(id(state))
    if previous is None or previous[0] is not state or previous[1]!=snapshot:
        validate(state)
        validated_states[id(state)]=(state,snapshot)

def validate_ensemble(ensemble):
    alternatives=ensemble.alternatives
    assert alternatives and len({x.label for x in alternatives})==len(alternatives)
    assert all(x.probability>0 for x in alternatives) and sum(x.probability for x in alternatives)==1
    for alt in alternatives:
        assert alt.state==reconstruct(alt.initial_commands+ensemble.shared_commands)
        checked_state(alt.state)
    if ensemble.parent is not None:
        validate_ensemble(ensemble.parent)
        previous={x.label:x for x in ensemble.parent.alternatives}
        if ensemble.evidence:
            assert ensemble.shared_commands==ensemble.parent.shared_commands
            assert set(previous)>=set(x.label for x in alternatives)
            labels=set(ensemble.evidence)
            assert labels=={x.label for x in alternatives}
            mass=sum(previous[label].probability for label in labels)
            assert all(x.probability==previous[x.label].probability/mass and x.state==previous[x.label].state for x in alternatives)
        else:
            assert ensemble.shared_commands[:-1]==ensemble.parent.shared_commands
            assert {x.label for x in alternatives}==set(previous)
            assert all(x.probability==previous[x.label].probability and x.initial_commands==previous[x.label].initial_commands
                       and x.state.parent is previous[x.label].state for x in alternatives)
    return True

def step(ensemble,command):
    validate_ensemble(ensemble)
    result=Ensemble(tuple(replace(x,state=advance(x.state,command)) for x in ensemble.alternatives),
                    ensemble.shared_commands+(command,),ensemble)
    validate_ensemble(result)
    return result

def condition(ensemble,labels):
    validate_ensemble(ensemble)
    chosen=tuple(x for x in ensemble.alternatives if x.label in labels)
    if not chosen: return None # Empty evidence is not a fictitious feasible state.
    mass=sum(x.probability for x in chosen)
    result=Ensemble(tuple(replace(x,probability=x.probability/mass) for x in chosen),
                    ensemble.shared_commands,ensemble,tuple(sorted(labels)))
    validate_ensemble(result)
    return result

def task_observation(state):
    obs=w['observations'](state)
    return tuple((key,obs[key]) for key in sorted(obs))

def history_observation(state):
    history=[]
    while state.parent is not None:
        history.append(state.command); state=state.parent
    return tuple(reversed(history))

def budget(ensemble,observer):
    validate_ensemble(ensemble)
    masses={}
    for x in ensemble.alternatives:
        value=observer(x.state)
        masses[value]=masses.get(value,F(0))+x.probability
    source_collision=sum(x.probability**2 for x in ensemble.alternatives)
    observed_collision=sum(mass**2 for mass in masses.values())
    # Ordered pairs of independent draws from the supplied prior:
    # B=Pr(labels differ); D=Pr(readouts differ); R=Pr(labels differ,readouts equal).
    B=1-source_collision; D=1-observed_collision; R=observed_collision-source_collision
    assert B==D+R and R>=0
    return {'total_distinction_budget':B,'observable_distinctions':D,'unresolved_ambiguity':R,
            'observer_blocks':len(masses)}

commands=(('x',(('gain',S.Rational(2,3)),('gain',S.Rational(3,5)))),
          ('y',(('gain',S.Rational(2,5)),)),
          ('z',(('gain',S.Rational(3,4)),)))
initial=Ensemble(tuple(Alternative(label,F(1,3),trace,reconstruct(trace)) for label,trace in commands))
validate_ensemble(initial)
checks={'owning_finite_scalar_square_and_noncommuting_hostile_rerun':True}; receipts={}
b=budget(initial,task_observation)
assert (b['total_distinction_budget'],b['observable_distinctions'],b['unresolved_ambiguity'])==(F(2,3),F(4,9),F(2,9))
h=budget(initial,history_observation)
assert h['observable_distinctions']==F(2,3) and h['unresolved_ambiguity']==0
checks['task_ambiguity_and_history_distinctions_are_different']=True
receipts['initial_task']=b; receipts['initial_history']=h

current=initial
for command in (('drift',None),('gain',S.Rational(1,2)),('gain',S.Rational(0))):
    next_state=step(current,command)
    before=budget(current,task_observation); after=budget(next_state,task_observation)
    assert before['total_distinction_budget']==after['total_distinction_budget']
    assert after['observable_distinctions']-before['observable_distinctions']==-(after['unresolved_ambiguity']-before['unresolved_ambiguity'])
    current=next_state
final=budget(current,task_observation)
assert final['observable_distinctions']==0 and final['unresolved_ambiguity']==F(2,3)
assert budget(current,history_observation)['unresolved_ambiguity']==0
checks['fixed_prior_transport_has_exact_D_plus_R_balance']=True
checks['gain_zero_collapses_readouts_but_not_retained_alternatives']=True
receipts['after_gain_zero']=final

# A positive change of units is an injective observer map. Re-boxing or
# rescaling a radius without its inverse would be a different evidence law.
energy=lambda state:w['observations'](state)['energy']
assert budget(initial,energy)==budget(initial,lambda state:7*energy(state))
center=F(5,3); epsilon=F(2,7); scale=F(7)
old=(center-epsilon,center+epsilon)
new=(scale*old[0],scale*old[1])
assert (new[0]/scale,new[1]/scale)==old and (scale*epsilon)/scale==epsilon
checks['positive_observer_units_preserve_partition_and_pulled_back_radius']=True

# Conditioning is explicit evidence, keeps the parent and changes the budget.
refined=condition(initial,{'x','y'})
small=budget(refined,task_observation)
assert small['total_distinction_budget']==F(1,2) and small['unresolved_ambiguity']==F(1,2)
assert refined.parent is initial and refined.evidence==('x','y')
assert condition(initial,{'absent'}) is None
checks['conditioning_changes_prior_and_empty_refinement_is_not_feasibility']=True
receipts['conditioned_xy']=small

# Shared latent history/command labels bind the entire attachment tuple.
# An energy state from z cannot be combined with x's other attachments.
x,y,z=initial.alternatives
assert task_observation(x.state)==task_observation(y.state) and x.state!=y.state
controls={}
def rejects(name,bad):
    try: validate_ensemble(bad)
    except (AssertionError,AttributeError,TypeError): controls[name]=True
    else: raise AssertionError('accepted hostile: '+name)
rejects('independent_reboxing_of_energy_and_relation',replace(initial,alternatives=(replace(x,state=replace(x.state,energy=z.state.energy)),y,z)))
rejects('erased_balanced_cut_attachment',replace(initial,alternatives=(replace(x,state=replace(x.state,cuts=())),y,z)))
rejects('equal_readouts_used_to_replace_history',replace(initial,alternatives=(replace(x,state=y.state),y,z)))
rejects('conditioned_prior_without_evidence',replace(refined,evidence=()))
rejects('stale_comparison_filler_after_transport',replace(current,alternatives=(replace(current.alternatives[0],state=replace(current.alternatives[0].state,comparison=None)),)+current.alternatives[1:]))
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.wg-uncertainty-budget.v1','status':'pass','checks':checks,'rejected_hostiles':controls,
     'budgets':receipts,'law':'B=1-sum(p_s^2)=D+R; D=1-sum(p_y^2); R=sum(p_y^2)-sum(p_s^2). Fixed-prior deterministic retained transport gives deltaD=-deltaR.',
     'statistical_assumptions':'caller-admitted finite three-history ensemble with probabilities1/3; pair probabilities describe two independent draws, not independent packet fields or physical repeated acquisitions',
     'scope':'exact finite joint alternatives over actual complete attachments; neither universal Shannon/variance conservation nor source-ideal filtration transport'}
(ROOT/'research/strominger/results/wg-uncertainty-budget-v1.json').write_text(json.dumps(out,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,default=str))
