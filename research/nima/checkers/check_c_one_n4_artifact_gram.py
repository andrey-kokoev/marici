"""Regression gate for invalidated c=1 component and Gram certificates."""
import json
components=json.load(open('research/grothendieck/results/interval-c-one-prime-and-jets.json'))
assert components['status']=='invalidated'
assert components['valid_rows']==[]
assert 'capped at 1024' in components['reason']
print(json.dumps({'schema':'marici.nima.c-one-component-invalidation-regression.v3','status':'passed','component_schema':components['schema'],'component_status':components['status'],'reason':components['reason'],'invalidated_executions':['structured_command_execution:e_11792_1788314192719668300_41','structured_command_execution:e_11792_1788314363951379100_44'],'retracted_claim':'directed coherent c=1 rank-three positivity certificate','surviving_claim':'conditional Sylvester robustness given valid entry boxes','required_repair':components['next_test']},sort_keys=True))
