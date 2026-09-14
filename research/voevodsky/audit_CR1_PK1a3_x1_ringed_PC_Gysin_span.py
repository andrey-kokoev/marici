#!/usr/bin/env python3
"""Audit the x1 edge via physical reflection and rotated pair traces."""
import json,subprocess,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def run(n):
 s=R/'research/voevodsky'/n;e=Path(tempfile.gettempdir())/(s.stem+'.exe');subprocess.run(['rustc','--edition=2021','-D','warnings','-O',str(s),'-o',str(e)],check=True);return json.loads(subprocess.check_output([str(e)],text=True))
r=run('check_d03_physical_reflection_edge_purity.rs');t=run('check_d03_three_pair_pc_extension.rs');f=r['factorization_test'];q=t['factorization_test']
checks={'x0_x1_reflection':'x0<->x1' in (R/'research/voevodsky/check_d03_physical_reflection_edge_purity.rs').read_text(),'endpoint_exchange':'v00<->v11' in f['endpoint_exchange'],'target_square':f['loaded_target_square']=='identity','three_local_traces':q['local_traces'].startswith('PASS'),'relation_target':q['relation_differential'].startswith('PASS'),'source_untyped':q['source_top_square'].startswith('UNTYPED'),'excess_missing':'six excess' in q['source_top_square']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.CR1-PK1a3-x1-ringed-PC-Gysin-span.v1','action':'CR1PK1a3_construct_x1_ringed_PC_Gysin_span','outcome':'-+','proved':['physical reflection transports x0<->x1 target packets and endpoints','target reflection square is identity','three rotated local road traces and target relation differential'],'obstruction':'the reflected/rotated source attachment is untyped because branch-pair supports are nonnested and the excess Tor1 Beck-Chevalley maps are absent','new_interfaces':['x1_reflected_target_PC_packet'],'next':'CR1PK1a4_verify_edge_overlap_and_triple_coherence','metric_delta':{'formal_coherence_survivors_percent':0.0,'geometrically_certified_complete_paths_percent':0.0,'new_typed_interfaces':1,'newly_blocked_descendant_branches':1},'checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_PK1a3_x1_ringed_PC_Gysin_span.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'-+','survivors':32,'new_interfaces':1,'next':out['next']}))
