from objective_projection import *
actions=[ActionAssessment('exact',frozenset({'goal'}),8,12,.6,.2,.5,.8,3,.1),ActionAssessment('scout',frozenset({'goal'}),2,3,.3,.9,.9,.5,1,.7)]
def test_objectives_vary():
 assert recommend(Objective('science',ObjectiveKind.SCIENTIFIC_TARGET,'goal','reachability_then_expected_cost'),actions).action=='exact'
 assert recommend(Objective('cheap',ObjectiveKind.COST,'goal','minimum_expected_cost'),actions).action=='scout'
 assert recommend(Objective('falsify',ObjectiveKind.FALSIFICATION,'goal','maximum_falsification_value'),actions).action=='scout'
 assert recommend(Objective('proof',ObjectiveKind.PROOF_QUALITY,'goal','maximum_certificate_strength'),actions).action=='exact'
def test_constraints():
 assert recommend(Objective('budget',ObjectiveKind.COST,'goal','minimum_expected_cost',budget=2),actions).action is None
 assert recommend(Objective('certificate',ObjectiveKind.PROOF_QUALITY,'goal','maximum_certificate_strength',required_certificate=3),actions).action=='exact'
if __name__=='__main__':test_objectives_vary();test_constraints();print('PASS 2/2')
