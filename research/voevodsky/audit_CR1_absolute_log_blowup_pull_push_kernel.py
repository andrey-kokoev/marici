#!/usr/bin/env python3
"""Repository evidence audit for the absolute log-blowup pull-push kernel."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2];files=list((R/'research/voevodsky').glob('check_*.rs'));hits=[]
for p in files:
 s=p.read_text()
 if 'log-blowup' in s or 'logarithmic blowup' in s:hits.append(p.name)
central=(R/'research/voevodsky/check_d03_central_flip_dnc_obstruction.rs').read_text()
checks={'only_relevant_checker':hits==['check_d03_central_flip_dnc_obstruction.rs'],'explicitly_conditional':'full_filtered_PC_two_cell' in central and 'CONDITIONAL' in central,'kernel_requested_not_constructed':'Construct the log-blowup or iterated-nearby-cycle pull-push kernel' in central,'local_geometry_available':'relative_dualizing_class' in central and 'EXISTS canonically' in central}
assert all(checks.values()),(hits,checks)
out={'schema':'marici.voevodsky.CR1-absolute-log-blowup-pull-push-kernel.v1','action':'CR1PK1a1a1a1_construct_absolute_log_blowup_pull_push_kernel','outcome':'--','available':'local logarithmic blowup, relative dualizing class, and fixed-beta Cartier residue','missing':'an object or morphism implementing log-blowup/iterated-nearby-cycle pull-push on the absolute support-PC category','repository_search':{'checkers':len(files),'relevant':hits,'positive_kernel_constructions':0},'branch_disposition':'blocked pending new six-functor geometry; continue independent x0/x1 edge branches','next':'CR1PK1a2_construct_x0_ringed_PC_Gysin_span','metric_delta':{'formal_coherence_survivors_percent':0.0,'geometrically_certified_complete_paths_percent':0.0,'active_local_specialization_branches':-1,'blocked_branches':1},'checks':checks,'passed':True};p=R/'research/voevodsky/results/CR1_absolute_log_blowup_pull_push_kernel.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'--','relevant_checkers':len(hits),'positive_kernels':0,'next':out['next']}))
