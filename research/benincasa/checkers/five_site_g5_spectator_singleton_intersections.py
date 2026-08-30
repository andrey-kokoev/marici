import json
from pathlib import Path

n=5
pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
orbits=[]; seen=set()
for p in pairs:
    if p in seen:continue
    orb=[((p[0]+k)%n,(p[1]+k)%n) for k in range(n)]
    seen.update(orb);orbits.append(orb)
assert len(pairs)==20 and len(orbits)==4 and all(len(o)==5 for o in orbits)

# At fixed loop variables, (E_T,X_i,X_j) -> (q_e,g_i,g_j) has identity
# energy Jacobian. Loop-distance terms are constants in this block.
jacobian=[[1,0,0],[0,1,0],[0,0,1]]
det=1

packet={
 'schema':'marici.five_site_g5_spectator_singleton_intersections.v1',
 'labelled_intersection_count':len(pairs),
 'cyclic_orbit_count':len(orbits),
 'cyclic_orbit_sizes':[len(o) for o in orbits],
 'orbit_invariants_mod_5':[1,2,3,4],
 'energy_jacobian':jacobian,
 'energy_jacobian_determinant':det,
 'base_transverse':True,
 'coefficient_tensor_product_proved':False,
 'loop_gradient_audit_required':True,
 'classification':'existing marked-wall carrier incidence; integrated three-wall coefficient uncomputed',
}
Path('research/benincasa/results/five-site-g5-spectator-singleton-intersections.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
