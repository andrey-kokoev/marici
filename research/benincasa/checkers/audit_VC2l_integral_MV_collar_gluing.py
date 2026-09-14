#!/usr/bin/env python3
"""VC2l: test whether the known BD interval glues the a=0,b=0 endpoint collars."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
local=json.loads((ROOT/'research/benincasa/results/VC2k_BD_continued_endpoint_collar.json').read_text())
nearby=json.loads((ROOT/'research/benincasa/et-cut-nearby-normal-form.json').read_text())
endpoints=json.loads((ROOT/'research/benincasa/physical-cycle-endpoint-normal-lifts.json').read_text())
checks={'local_collars_exist':local['resolution']=='+-','known_interval_boundary':nearby['canonical_boundary_vector']==[-1,1],'known_interval_center_is_marked_corner':nearby['physical_real_corner']=='(a,b)=(y,x); the other sign corners are occurrence/deck companions','collar_faces_are_axes':{x['endpoint'] for x in endpoints['checks']}=={'a=0','b=0','c=0'},'no_label_map_in_local_packet':all(k not in local for k in ('endpoint_to_exceptional_map','specialization_map')),'known_interval_basis_uses_p_labels':nearby['relative_basis']==['[pminus]-[p0]','[pplus]-[p0]']}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.VC2l-integral-Mayer-Vietoris-collar-gluing-audit.v1','prospective_action':'VC2l_integral_Mayer_Vietoris_collar_gluing','resolution':'--','reason':'The available BD interval has endpoints pminus,pplus in the exceptional blowup at the nonzero marked corner (a,b)=(y,x). The collar germs are labelled by the distinct signed-minor axis faces a=0 and b=0. Equality of boundary vectors (-1,1) does not define a map between these endpoint lattices.','prohibited_shortcut':'Identify (a=0,b=0) with (pminus,pplus) by rank and orientation alone.','missing_interface':'signed_minor_axis_to_exceptional_endpoint_specialization','repair':'Construct the simultaneous continuation/resolution map carrying the a=0 and b=0 boundary strata into the E=0 blowup, then compute their images in the pminus,p0,pplus lattice.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/VC2l_integral_MV_collar_gluing_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'--','missing':out['missing_interface']}))
