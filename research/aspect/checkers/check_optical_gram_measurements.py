"""Exact rational audit of intensity reconstruction of two-route Gram invariants."""
from fractions import Fraction as F
from pathlib import Path
import json

# Gram data u,v,c=r+i q. Interference conventions:
# I0=||b1+b2||^2=u+v+2r; I90=||b1+i b2||^2=u+v-2q.
u,v,r,q=F(5),F(3),F(1),F(2)
trace=u+v; i0=trace+2*r; i90=trace-2*q
rr=(i0-trace)/2; qq=(trace-i90)/2; det=u*v-rr*rr-qq*qq
# Hostile has same u,v,I0 but opposite/nonzero unseen quadrature magnitude changed.
q_hostile=F(1); i0_hostile=trace+2*r; det_hostile=u*v-r*r-q_hostile*q_hostile
checks={"trace_reconstructed":trace==8,"real_overlap_reconstructed":rr==r,
 "imaginary_overlap_reconstructed":qq==q,"determinant_reconstructed":det==10,
 "single_phase_is_not_faithful":i0_hostile==i0 and det_hostile!=det,
 "reciprocal_real_overlap_reduces_to_three_measurements":u*v-rr*rr==14}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only",
 "measurements":{"u":str(u),"v":str(v),"I0":str(i0),"I90":str(i90)},
 "reconstructed":{"trace":str(trace),"real_overlap":str(rr),"imaginary_overlap":str(qq),"determinant":str(det)},
 "hostile":{"same_u_v_I0":True,"determinant":str(det_hostile)},"checks":checks}
out=Path("research/aspect/results/optical_gram_measurements.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
