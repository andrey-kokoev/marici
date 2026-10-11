"""Numerical regressions for success-first, expected-cost-second planning."""
from interpretation_planner import Action, Branch, Decoder, Effect, Planner, State, OUTCOMES
from objective_projection import ActionAssessment, Objective, ObjectiveKind, recommend

def action(name,p,cost):
    branches={o:Branch(0,Effect(remove=frozenset({'live'}))) for o in OUTCOMES}
    branches['++']=Branch(p,Effect(raw='certificate'))
    branches['+-']=Branch(1-p,Effect(remove=frozenset({'live'})))
    return Action(name,cost,frozenset({'live'}),branches)

def solve(p,cost,q,other_cost):
    actions=[action('cheap',p,cost),action('other',q,other_cost)]
    decoders=[Decoder(a.name,'certificate',frozenset(),'target') for a in actions]
    return Planner(actions,decoders,'target').solve_expected(State(frozenset(),frozenset({'live'})))

assert solve(.3,1,.30000000000000004,8).first_action=='cheap'
assert solve(.3,1,.31,8).first_action=='other'
assert solve(0,0,1e-30,1).first_action=='other'
objective=Objective('closure',ObjectiveKind.SCIENTIFIC_TARGET,'target','reachability_then_expected_cost')
a=[ActionAssessment('cheap',frozenset({'target'}),1,1,.3),ActionAssessment('other',frozenset({'target'}),8,8,.30000000000000004)]
assert recommend(objective,a).action=='cheap'
print('PASS 4/4')
