"""Validate role-to-coordinate links and report uncovered generic roles."""
import json
from pathlib import Path
ROOT=Path(__file__).parents[1]
REG=ROOT/'coherence-pyramid-role-coordinate-registry.json';SIG=ROOT/'coherence-pyramid-computad-signature.json';CELLS=ROOT/'coherence-pyramid-cells-and-laws.json';OUT=ROOT/'results'/'coherence-pyramid-role-coordinate-registry.json'
def main():
 r=json.loads(REG.read_text());s=json.loads(SIG.read_text());c=json.loads(CELLS.read_text());allowed=set(r['allowed_statuses']);systems=r['coordinate_systems'];edges=r['edge_instances'];faces=r['face_instances'];edge_ids={x['id'] for x in edges}
 assert len(edge_ids)==len(edges);assert all(x['status'] in allowed for x in edges+faces)
 bad=[]
 for x in edges:
  cs=systems[x['coordinate_system']];verts=cs['vertices'];
  if x['source'] not in verts or x['target'] not in verts:bad.append(x['id'])
 for f in faces:
  if not set(f['boundary_edges'])<=edge_ids:bad.append(f['id'])
 signature_edge_roles=set(s['one_generators']);signature_face_roles=set(c['cells']);used_edge_roles={x['role'] for x in edges};used_face_roles={x['role'] for x in faces}
 unknown_face_roles=sorted(used_face_roles-signature_face_roles)
 rows=[]
 for x in edges:
  cs=systems[x['coordinate_system']];verts=cs['vertices'];coord=lambda key: verts[key] if isinstance(verts,dict) else key;rows.append({'id':x['id'],'role':x['role'],'source_coordinate':coord(x['source']),'target_coordinate':coord(x['target']),'status':x['status'],'expected_analytic_form':x['expected_analytic_form']})
 checks={'coordinates_well_typed':not bad,'all_boundary_edges_exist':not bad,'edge_roles_declared':used_edge_roles<=signature_edge_roles,'all_coordinate_face_roles_declared':not unknown_face_roles,'no_mapping_promoted_to_realized':all(x['status']!='realized' for x in edges+faces)}
 out={'schema':'marici.voevodsky.coherence-pyramid-role-coordinate-registry-check.v1','summary':{'edge_instances':len(edges),'face_instances':len(faces),'realized_links':sum(x['status']=='realized' for x in edges+faces),'signature_edge_roles_without_coordinate_instance':sorted(signature_edge_roles-used_edge_roles),'signature_face_roles_without_coordinate_instance':sorted(signature_face_roles-used_face_roles),'coordinate_roles_missing_from_signature':unknown_face_roles},'edge_table':rows,'face_table':faces,'checks':checks,'passed':all(checks.values()),'next_gate':'Attach typed analytical evidence for ABC and ABD composition comparisons before promoting either mapping to realized.'}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
