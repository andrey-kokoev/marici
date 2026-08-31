"""Gate a Cayley-Menger or relative-face source for the exceptional triangle filler."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; N=ROOT/'research'/'nima'/'results'; OUT=V/'cosmology_CM_relative_face_source_gate.json'
def load(p):return json.loads(p.read_text())
def main():
 pair=load(V/'cosmology_pair_face_residue_vector.json'); corner=load(N/'cosmology_triple_incidence_boundary_corner_transport.json'); source=load(N/'cosmology_source_principal_wall_cell.json'); total=load(V/'cosmology_exceptional_triangle_total_lift.json')
 assert pair['passed'] and corner['passed'] and source['passed'] and total['passed']
 assert pair['why_Cayley_Menger_empty_face_does_not_help'] and corner['generic_cayley_menger_boundary_at_collision'] is False
 assert source['triple_incidence_base_function']=='x + y + 3*z'
 out={'schema':'marici.voevodsky.cosmology-CM-relative-face-source-gate.v1','status':'current_source_has_no_Cayley_Menger_face_relative_face_remains_unsourced','source_collision':'three marked walls q1,q2,q3 with q3-q1-q2=p','pair_face_obstruction':pair['residue_vector'],'corner_type':corner['transport_type'],'generic_Cayley_Menger_boundary_at_collision':False,'CM_face_generator_available':False,'ordinary_blowup_face_available':False,'decision':'The Cayley-Menger route is not source-admissible in the current corner: the collision is a marked-wall boundary corner, not a generic CM boundary, and the current packet contains no CM face generator.','relative_face_status':'The ordered Cech 2-simplex has the correct formal boundary but lacks a chain map into the resolved/logarithmic carrier; calling it a relative face does not add source provenance.','required_new_input':'an independently derived compactification or incidence correspondence whose actual boundary stratum has the primitive triangle as its boundary and maps to the ordered wall carrier','limitations':['does not rule out a future source-derived CM degeneration in an enlarged geometry','no horn, Bockstein, contour, or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
