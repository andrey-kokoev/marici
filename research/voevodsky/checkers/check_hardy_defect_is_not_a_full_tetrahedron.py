"""Exact scalar obstruction to filling the Hardy defect triangle as the claimed tetrahedron."""
import json
from pathlib import Path
# Scalar contraction m=0 has defect d=1. A B->C edge T would need T*m=d.
m=0;d=1
out={'incoming_to_outgoing':'m=0','incoming_to_defect':'d=sqrt(1-|m|^2)=1','required_B_to_C_face_equation':'T*m=d','left_side_for_every_T':0,'right_side':1,'factorization_exists':False,'conclusion':'The canonical contraction/defect construction is a Stinespring column (a span or isometric dilation), not a full elementary tetrahedron. A B-to-C edge requires extra factorization data and fails for a valid contraction.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'hardy-defect-not-full-tetrahedron.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
