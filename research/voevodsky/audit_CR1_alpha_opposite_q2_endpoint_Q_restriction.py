#!/usr/bin/env python3
"""Audit the opposite q2 endpoint restriction against the exact endpoint hull."""
import json,subprocess,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def run(n):
 s=R/'research/voevodsky'/n;e=Path(tempfile.gettempdir())/(s.stem+'.exe');subprocess.run(['rustc','--edition=2021','-D','warnings','-O',str(s),'-o',str(e)],check=True);return json.loads(subprocess.check_output([str(e)],text=True))
t=run('check_d03_thom_endpoint_bc.rs');q=run('check_d03_q0_endpoint_exit_flags.rs');f=t['factorization_test'];g=q['factorization_test']
checks={'exact_two_endpoint_hull':f['exact_hull'].startswith('PASS'),'q2_formal_evaluation':'(x1)^vee' in f['principal_ideal_evaluation'],'conditional_BC':'b2=x5*a2' in f['two_path_BC'],'q0_geometric_only':g['marked_q0_flag'].startswith('UNIQUE'),'road_generizations_absent':f['actual_road_generizations']=='NOT SUPPLIED by the tensor model','extraordinary_absent':f['actual_extraordinary_push_pull']=='NOT CONSTRUCTED'}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.CR1-alpha-opposite-q2-endpoint-Q-restriction.v1','action':'CR1ALPHA2a1_construct_opposite_q2_endpoint_Q_restriction','outcome':'-+','proved':['exact augmented q0/q2 Koszul hull','formal q2 principal-line endpoint evaluation +1','conditional BC criterion b2 in (x5), a2=b2/x5'],'obstruction':'unlike q0, no independently marked K6 road flag derives the q2 road generization b2 before base change; assigning b2=x5 would fit the desired unit','missing':'geometric q2-to-road flag/correspondence retaining the x5 ideal line','next':'CR1ALPHA2a1a_enumerate_q2_compatible_marked_K6_exit_flags','metric_delta':{'constructed_endpoint_restrictions':0,'blocked_endpoint_restrictions':1,'new_typed_interfaces':0,'formal_outcome_entropy_bits':-2.0},'checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_alpha_opposite_q2_endpoint_Q_restriction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'-+','q0_geometric':True,'q2_geometric':False,'next':out['next']}))
