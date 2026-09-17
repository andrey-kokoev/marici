#!/usr/bin/env python3
"""Register the positive-filler frontier without promoting signed coherence."""
import json
from pathlib import Path
root=Path(__file__).parents[1];res=root/'results'
tri=json.loads((res/'seven_transition_triangle_prototypes.json').read_text());tet=json.loads((res/'seven_transition_tetrahedron_prototypes.json').read_text());geo=json.loads((res/'esd7_tetrahedron_prototype_registry.json').read_text());audit=json.loads((res/'uniform_weil_proof_gate_audit_v2.json').read_text())
allowed={'positive_certified','conditional_positive','signed_only','obstructed'}
tri_rows={k:{'status':'signed_only','analytical_form':v['form'],'reason':'typed analytical 2-cell; no universal positive realization certificate'} for k,v in tri['prototypes'].items()}
tet_rows={k:{'status':'signed_only','analytical_form':v['analytical_form'],'reason':'typed analytical 3-cell; source-faithful positive lift not certified'} for k,v in tet['prototypes'].items()}
gates={
 'source_faithful_positive_realization':False,
 'directed_robust_complement_blocks':False,
 'moving_critical_bundle_all_slabs':False,
 'shared_face_translation_dagger_refinement_positive_compatibility':False,
 'terminal_6_to_7_pro_horn_resolved':False,
 'unconditional_weighted_hankel_and_explicit_N0':False,
 'all_finite_thresholds_below_N0_directed':False,
}
checks={'signed_registry_present':geo['passed'],'all_triangle_prototypes_registered':len(tri_rows)==8,'all_tetrahedron_prototypes_registered':len(tet_rows)==12,'statuses_in_vocabulary':all(x['status'] in allowed for x in [*tri_rows.values(),*tet_rows.values()]),'no_signed_cell_promoted_to_positive':not any(x['status']=='positive_certified' for x in [*tri_rows.values(),*tet_rows.values()]),'global_audit_agrees_not_positive':not audit['global_weil_positivity_established'],'all_seven_positive_gates_explicit':len(gates)==7}
out={'schema':'marici.voevodsky.eight-lattice-positive-filler-frontier.v1','status_vocabulary':sorted(allowed),'triangle_prototypes':tri_rows,'tetrahedron_prototypes':tet_rows,'geometric_cells':{'count':geo['tetrahedron_count'],'uniform_status':'signed_only','qualification':'each finite cell has a signed/relative filler; positivity is not inherited from the prototype registry'},'positive_gates':gates,'terminal_obstruction':{'status':'obstructed','slab':'6->7','reason':'linear trace growth lacks a uniform relative trace-class cancellation on H234'},'checks':checks,'passed_registration':all(checks.values()),'universal_positive_filler_certified':False,'rh_proved':False};p=res/'eight_lattice_positive_filler_frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'counts':{'triangles':len(tri_rows),'tetrahedra':len(tet_rows),'geometric_cells':geo['tetrahedron_count']},'positive_gates':gates,'terminal_obstruction':out['terminal_obstruction'],'checks':checks,'passed_registration':out['passed_registration'],'universal_positive_filler_certified':False},indent=2));assert out['passed_registration'] and not out['universal_positive_filler_certified']
