#!/usr/bin/env python3
"""Regression tests for durable exactly-one action resolutions."""
from interpretation_planner import Action,Branch,Coherence,Decoder,Effect,Implication,Justification,Planner,Proposition,Resolution,State,OUTCOMES
s=State(frozenset({'H'}),frozenset({'I'}));sid=s.identity();r=Resolution('A',sid,'++')
checks={'selected_retained':r.selected_outcome=='++','three_excluded':r.excluded_outcomes==('+-','-+','--'),'relation_exactly_one':r.relation=='exactly_one'}
rs=s.resolve('A','++');record=next(iter(rs.resolutions));checks['state_records_resolution']=record==r
facts={(f.args[-1],f.positive) for f in rs.facts if f.name=='outcome'}
checks['selected_fact_positive']=('++',True) in facts
checks['alternatives_explicitly_negative']=all((o,False) in facts for o in ('+-','-+','--'))
# Applying an effect must preserve the durable resolution.
ns=Effect(add=frozenset({'J'})).apply(rs);checks['effect_preserves_resolution']=r in ns.resolutions
# Same action name at a different starting state is a distinct event.
rs2=ns.resolve('A','+-');checks['different_start_is_distinct']=len(rs2.resolutions)==2
# The planner must materialize only the selected branch on each traversal.
def branch(o):return Branch(.25,Effect(add=frozenset({f'A:{o}'})),(Implication(f'A={o}','entails',f'A:{o}'),))
a=Action('A',1,frozenset({'I'}),{o:branch(o) for o in OUTCOMES});p=Planner([a],[],target='never',require_implications=True);p.solve_expected(s);checks['planner_accepts_complete_disjunction']=True
# Invalid disjunctions fail at construction.
try:Resolution('A',sid,'++',('++','++'))
except ValueError:checks['duplicate_alternatives_rejected']=True
try:State(frozenset(),facts=frozenset({Proposition('P'),Proposition('P',positive=False)}))
except ValueError:checks['contradictory_facts_rejected']=True
left=s.resolve('M','++');right=s.resolve('M','+-')
try:left.merge(right)
except ValueError:checks['conflicting_replay_merge_rejected']=True
checks['compatible_merge']=len(left.merge(s).resolutions)==1
premise=Proposition('branch',('A','++'));typed=Implication(premise,'entails',Proposition('J'))
checks['inactive_premise_does_not_fire']=Proposition('J') not in s.derive((typed,)).facts
derived=State(s.hypotheses,s.interfaces,facts=frozenset({premise})).derive((typed,));checks['typed_conclusion_derived']=Proposition('J') in derived.facts
p=Proposition('P');q=Proposition('Q');z=Proposition('Z')
rules=(Implication(p,'entails',q),Implication((p,q),'entails',z))
closed=State(frozenset(),facts=frozenset({p})).derive(rules);checks['multi_premise_fixed_point_closure']={p,q,z}<=set(closed.facts)
checks['justifications_recorded']=len(closed.justifications)==2
retracted=closed.invalidate(p);checks['invalidation_adds_negation']=p.negate() in retracted.facts
checks['invalidation_cascades']=q not in retracted.facts and z not in retracted.facts
checks['dead_justifications_removed']=not retracted.justifications
r=Proposition('R');shared=Proposition('Shared');parallel=(Implication(p,'entails',shared),Implication(r,'entails',shared))
parallel_state=State(frozenset(),facts=frozenset({p,r})).derive(parallel)
checks['alternative_supports_recorded']=len([j for j in parallel_state.justifications if j.conclusion==shared])==2
checks['one_live_support_retains_conclusion']=shared in parallel_state.invalidate(p).facts
j1=Justification(shared,frozenset({p}),'entails');j2=Justification(shared,frozenset({r}),'entails')
coh=Coherence(j1.path_id,j2.path_id,'equivalent','commuting diamond certificate')
strict=State(frozenset(),facts=frozenset({p,r})).derive(parallel,coherences=frozenset({coh}),require_path_coherence=True)
checks['coherent_parallel_paths_admitted']=shared in strict.facts
try:State(frozenset(),facts=frozenset({p,r})).derive(parallel,require_path_coherence=True)
except ValueError:checks['unwitnessed_parallel_paths_rejected']=True
badcoh=Coherence(j1.path_id,j2.path_id,'incompatible','hostile diamond')
try:State(frozenset(),facts=frozenset({p,r})).derive(parallel,coherences=frozenset({badcoh}))
except ValueError:checks['incompatible_paths_rejected']=True
try:
 bad=Action('B',1,frozenset(),{o:Branch(.25,Effect(add=frozenset({'X'})),(Implication('observed','entails',Proposition('Y')),)) for o in OUTCOMES})
 Planner([bad],[],target='never',require_implications=True)
except ValueError:checks['effect_implication_disagreement_rejected']=True
try:Implication('P','maybe','Q')
except ValueError:checks['unknown_relation_rejected']=True
assert all(checks.values()),checks
print(f"PASS {len(checks)}/{len(checks)}")
