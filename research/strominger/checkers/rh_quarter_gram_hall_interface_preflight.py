import json
from pathlib import Path
base=Path(__file__).parents[1]
gram=json.loads((base/'results'/'rh_quarter_D_positive_real_diagonal_gram.json').read_text())
hall=json.loads((base/'results'/'rh_quarter_source_interlacing_exact_maxflow.json').read_text())
gram_keys=set().union(*(r.keys() for r in gram['records']))
hall_keys=set(hall)
required_map_fields={'base','left_endpoint','right_endpoint','negative_source_index','positive_source_index','interlacing_edge','gram_to_source_map'}
declared_map_fields=required_map_fields & (gram_keys|hall_keys)
checks={'gram_backend_passed':gram['status']=='passed','hall_backend_passed':hall['status']=='passed','gram_records_are_n_shift_indexed':{'n','shift'}<=gram_keys,'hall_census_has_769_cases':hall['case_count']==769,'no_declared_cross_interface_map':not declared_map_fields}
result={'schema':'marici.strominger.rh_quarter_gram_hall_interface_preflight.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The retained Gram and Hall backends are separately exact but do not declare a map from n-shift Gram diagonals to S-i-j source vertices, interlacing edges, or capacities; composition is therefore undefined, not falsified.','gram_record_count':len(gram['records']),'gram_index_fields':['n','shift'],'hall_case_count':hall['case_count'],'required_missing_typed_object':'A source-derived map from each Hall case (S,i,j) and signed source term to Gram coordinates whose positive quadratic weights induce interlacing-edge capacities.','acceptance_test':'Declare the map, verify its index and coefficient conventions, reconstruct every bounded signed source term and edge capacity exactly, then prove the construction uniformly in source size.','declared_cross_interface_fields':sorted(declared_map_fields),'checks':checks};(base/'results'/'rh_quarter_gram_hall_interface_preflight.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
