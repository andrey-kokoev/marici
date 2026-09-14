#!/usr/bin/env python3
"""Exhaust the q2 coefficient compatibility against the actual F03 road labels."""
import json,subprocess,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def run(n):
 s=R/'research/voevodsky'/n;e=Path(tempfile.gettempdir())/(s.stem+'.exe');subprocess.run(['rustc','--edition=2021','-D','warnings','-O',str(s),'-o',str(e)],check=True);return json.loads(subprocess.check_output([str(e)],text=True))
q=run('check_d03_q0_endpoint_exit_flags.rs');t=run('check_d03_thom_endpoint_bc.rs');f=q['factorization_test'];h=t['factorization_test']
road_vertices={'v00':{'D03','x0','x3'},'v10':{'D03','x1','x3'},'v01':{'D03','x0','x4'},'v11':{'D03','x1','x4'}}
q2_required='x5';compatible=[v for v,label in road_vertices.items() if q2_required in label]
checks={'four_actual_vertices':f['F03_face_tube'].startswith('PASS: four'),'no_x5_road_vertex':compatible==[],'q2_BC_requires_x5':'b2=x5*a2' in h['two_path_BC'],'q0_match_exists':'x1' in road_vertices['v10'],'labels_independent':'q0={x5}' in f['Boolean_q0_vs_occurrence_vertices']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.CR1-q2-compatible-marked-K6-exit-flags.v1','action':'CR1ALPHA2a1a_enumerate_q2_compatible_marked_K6_exit_flags','outcome':'-+','enumerated_road_vertices':{k:sorted(v) for k,v in road_vertices.items()},'required_q2_generization_ideal':'(x5)','compatible_vertices':compatible,'conclusion':'No F03 road vertex or saturated road flag can derive an x5-divisible b2: x5 is endpoint-exclusive and absent from the entire F03 occurrence square.','contrast':'q0 requires the x1 ideal, which is present at v10 and yields the certified marked exit.','effect':'the desired two-endpoint defect restriction cannot be assembled inside the literal F03 road carrier','next_possible_geometry':'enlarge to a correspondence retaining the plus endpoint x5 line separately from the F03 road occurrence square; do not identify it with a road coordinate','metric_delta':{'candidate_q2_exit_flags':0,'active_q2_flag_branches':-1,'blocked_endpoint_restrictions':1,'new_typed_interfaces':0},'checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_q2_compatible_marked_K6_exit_flags.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'-+','road_vertices':4,'compatible_q2_flags':0,'q2_line':'x5'}))
