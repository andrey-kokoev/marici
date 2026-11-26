"""Verify the predecessor datum behind the 76-edge gate; no 35-vertex endpoint as input. graph6 has 351 payload bits at order 27 (3 trailing zero pad bits). For a degree-7 vertex in a hypothetical (3,9) on 35, deleting its closed red neighborhood leaves a legal (3,8) of order 27. If t vertices have degree 7 and s of them neighbor this vertex, that core has 84-t/2+s edges. Minimum 85 forces delta(G[degree7])>t/2, impossible triangle-free. Thus 8-regular and the 26 blue core has 140-8*8=76 edges."""
import json,gzip,collections,hashlib
from ramsey_retention_slice import CAT,D
p=CAT/'r38_27.g6.gz';H=collections.Counter();weights=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)])
with gzip.open(p,'rb') as f:
 for l in f:
  l=l.rstrip();assert len(l)==60 and l[0]==90 and (l[-1]-63)&7==0;H[sum(l[1:].translate(weights))]+=1
assert min(H)==85 and sum(H.values())==477142
(D.parent/'ramsey_gain35_regular_gate.json').write_text(json.dumps(dict(catalogue=p.name,gzip_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),hist=H,forced_core_edges=76,forced_support_size=7))+'\n');print(min(H),sum(H.values()))
