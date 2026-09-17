#!/usr/bin/env python3
"""Can the later physical-normal GM adapter select PS1C's moving coefficient?"""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
gm=json.loads((R/'physical-normal-gauss-manin-lift.json').read_text())
cech=json.loads((R/'physical-normal-lift-cech-coherence.json').read_text())
ps=json.loads((R/'results/PS1C1a1i_materialize_moving_Theta101.json').read_text())
assert gm['status']=='passed' and cech['status']=='passed' and ps['resolution']=='-+'
# The adapter gives vector fields/tangent response classes, not the missing
# coefficient object Theta_E; its own scope explicitly withholds full physical-boundary tangency.
out={'schema':'marici.benincasa.PS1M12-physical-normal-lift-transfer-gate.v1','prospective_action':'PS1M12_transfer_rank34_GM_adapter_to_select_moving_Theta101','resolution':'--','available':{'source_family':gm['source_family'],'normal_lift_formula':gm['local_lift_formula'],'cech_gluing':cech['cech_class'],'normal_count':cech['normal_count']},'type_mismatch':{'required_object':'E-dependent Theta101 coefficient in the PS1C moving-wall frame','available_object':'tangent vector-field response class for a generic six-scale rank-34 four-wall lower family','required_walls':['b+x-E','a+y-E'],'available_wall_labels':sorted(set(q for z in gm['normal_lifts'] for q in z['active_marked_walls']))},'withheld_by_source':gm['scope_warning'],'conclusion':'The physical-normal adapter cannot select the arbitrary E*F coefficient: it transports a different source family and produces a de Rham-Cech response class, not a coefficient-level section of the PS1C restriction map. Importing it would be an untyped cross-family identification.','next':'derive the same tangency/Cartan construction directly in the PS1C moving-wall source, including every signed-minor boundary, then test whether its coefficient projection kills the E*F kernel','passed':True}
(R/'results/PS1M12_physical_normal_lift_transfer_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
