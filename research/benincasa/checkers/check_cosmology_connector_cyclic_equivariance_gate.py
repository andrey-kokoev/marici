#!/usr/bin/env python3
"""Test sourced cyclic equivariance of connector axis assignments."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_connector_axis_orientation_classification.json').read_text())['passed']
D=('q_g1','q_g2','q_G12');T=('G12:e6','G23:e6','G31:e6')
rS={'q_g1':'q_g2','q_g2':'q_g3','q_g3':'q_g1','q_G12':'q_G23','q_G23':'q_G31','q_G31':'q_G12'}
rT={'G12:e6':'G23:e6','G23:e6':'G31:e6','G31:e6':'G12:e6'}
f={'q_g1':'G23:e6','q_g2':'G31:e6','q_G12':'G12:e6'}
closure=tuple(rS.keys());assert set(D)!=set(rS[x] for x in D) and len(closure)==6
checks=[]
for x in D:
 y=rS[x]
 checks.append({'axis':x,'rotated_axis':y,'defined_after_rotation':y in f,'equivariant_when_defined':(y in f and f[y]==rT[f[x]])})
assert sum(c['equivariant_when_defined'] for c in checks)==1
F={'q_g1':'G23:e6','q_g2':'G31:e6','q_g3':'G12:e6','q_G12':'G12:e6','q_G23':'G23:e6','q_G31':'G31:e6'}
assert all(F[rS[x]]==rT[F[x]] for x in closure)
out={'schema':'marici.benincasa.cosmology-connector-cyclic-equivariance-gate.v1','three_axis_domain':list(D),'sourced_rotation_images':[rS[x] for x in D],'domain_closed_under_rotation':False,'complement_heuristic_partial_checks':checks,'source_authorized_equivariant_bijections':0,'minimal_cyclic_closure':list(closure),'closure_axis_count':6,'equivariant_closure_map':F,'closure_map_fiber_sizes':{t:sum(v==t for v in F.values()) for t in T},'closure_map_is_bijection':False,'conclusion':'cyclic equivariance cannot select a three-axis connector; it forces the six-axis closure and a two-to-one axis map','next_test':'construct the six-axis cyclic connector presentation and test whether identifying each two-element axis fiber preserves deletion-cube coherence','passed':True};(R/'cosmology_connector_cyclic_equivariance_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
