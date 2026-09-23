"""A path commitment must bind ordered typed edges, not only occurrence vertices."""
from hashlib import sha256
import json
from pathlib import Path
vertices=('source','middle','end')
a=(('source','middle','weakening'),('middle','end','weakening'))
b=(('source','middle','comparison'),('middle','end','weakening'))
def H(x):return sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
assert H(vertices)==H(vertices) and H(a)!=H(b)
def validate(edges):
 if len(edges)!=len(vertices)-1:return False
 return all(edge[0]==vertices[i] and edge[1]==vertices[i+1] and edge[2]=='weakening' for i,edge in enumerate(edges))
assert validate(a) and not validate(b)
commit=lambda edges:H({'vertices':vertices,'edges':edges,'version':1})
assert commit(a)!=commit(b)
report={'passed':True,'vertex_only_digest':'collides across distinct edge types','typed_ordered_path_digest':'distinguishes weakening from comparison','validation':'only two correctly typed consecutive weakening edges pass','scope':'Synthetic path commitments, not observed events or source publication authority.'}
out=Path(__file__).resolve().parents[1]/'results/path-digest-edge-binding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
