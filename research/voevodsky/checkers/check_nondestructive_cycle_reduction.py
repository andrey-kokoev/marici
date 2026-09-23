"""Cycle contraction creates a derived view pinned to an immutable original path."""
from hashlib import sha256
from pathlib import Path
import json
from copy import deepcopy
path=(('S','P','comparison@1'),('P','Q','comparison@1'),('Q','P','comparison@1'),('P','T','comparison@1'))
def H(x):return sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def reduce(source):
 if source[1:3]!=(('P','Q','comparison@1'),('Q','P','comparison@1')):raise ValueError('NO_EXACT_CYCLE')
 return {'kind':'derived-cycle-reduced-view','edges':source[:1]+source[3:],'original_path_digest':H(source),'removed_segment_digest':H(source[1:3]),'observed_replacement':False}
original=deepcopy(path);view=reduce(path)
assert path==original and len(path)==4 and len(view['edges'])==2
assert view['edges']==(path[0],path[-1]) and view['original_path_digest']==H(path)
tampered=path[:2]+(('Q','R','comparison@1'),)+path[3:]
try:reduce(tampered)
except ValueError as err:assert str(err)=='NO_EXACT_CYCLE'
else:raise AssertionError('tampered cycle reduced')
report={'passed':True,'original':'four edges preserved','view':'two edges, references original and removed segment digests; not observed replacement','tampered_cycle':'rejected','scope':'Synthetic path structure only, not proof endpoint checks, real history, issuer or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/nondestructive-cycle-reduction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
