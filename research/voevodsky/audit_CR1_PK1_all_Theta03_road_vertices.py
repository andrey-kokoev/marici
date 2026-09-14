#!/usr/bin/env python3
"""Resolve PK1 against the existing four-corner and Cox/Cousin checkers."""
import json,subprocess,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def run(src):
 exe=Path(tempfile.gettempdir())/(src.stem+'.exe');subprocess.run(['rustc','--edition=2021','-D','warnings','-O',str(src),'-o',str(exe)],check=True);return json.loads(subprocess.check_output([str(exe)],text=True))
four=run(R/'research/voevodsky/check_d03_four_corner_descent_obstruction.rs');cox=run(R/'research/voevodsky/check_d03_toric_cox_cousin_trace.rs')
checks={'four_corner_cellular_descent':four['factorization_test']['full_total'].startswith('PASS'),'generic_lcm_cocycle':four['factorization_test']['generic_lcm_cocycle'].startswith('PASS'),'formal_four_values':len(cox['trace']['formal_corner_values'])==4,'x3_edge_v00_v10':cox['checks']['v00_v10_residues'].startswith('PASS'),'actual_PC_Gysin_missing':cox['checks']['actual_PC_Gysin']=='UNCONSTRUCTED','supported_reconstruction_fails':'falsified_corner_local_cohomology_reconstruction' in four['claims']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.CR1-PK1-all-Theta03-road-vertices.v1','action':'CR1PK1_assemble_all_Theta03_road_vertices','outcome':'+-','outcome_meaning':'the formal four-corner principal-line cocycle is assembled and the x3 edge is geometrically realized at v00/v10, but the remaining edge Gysin maps and full supported Theta03 identification are absent','formal_corner_values':cox['trace']['formal_corner_values'],'geometric_vertices':['v00','v10'],'formal_only_vertices':['v01','v11'],'blockers':['other three ringed edge Gysin maps','higher overlap coherence','identification with full normalized Theta03 trace'],'next':'CR1PK1a_construct_remaining_ringed_edge_Gysin_maps','checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_PK1_all_Theta03_road_vertices.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'+-','geometric':2,'formal_only':2,'next':out['next']}))
