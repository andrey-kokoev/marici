"""Overlapping closed subpaths can have equal residual shapes but different provenance."""
from hashlib import sha256
from pathlib import Path
import json
edges=(('A','B','e1'),('B','A','e2'),('A','B','e3'),('B','A','e4'))
def H(x):return sha256(repr(x).encode()).hexdigest()
def reduce(start):
 selected=edges[start:start+2]
 assert len(selected)==2 and selected[0][0]==selected[-1][1]
 remaining=edges[:start]+edges[start+2:]
 return {'original':H(edges),'removed_ids':tuple(e[2] for e in selected),'removed_digest':H(selected),'residual':remaining,'residual_digest':H(remaining)}
left=reduce(0);middle=reduce(1);right=reduce(2)
assert left['original']==middle['original']==right['original']
assert left['removed_digest']!=middle['removed_digest']!=right['removed_digest']
assert tuple((e[0],e[1]) for e in left['residual'])==tuple((e[0],e[1]) for e in middle['residual'])==(('A','B'),('B','A'))
assert left['residual_digest']!=middle['residual_digest'] and len(edges)==4
report={'passed':True,'overlapping_two_edge_cycles':'three choices in four-edge A-B-A-B-A walk','same_residual_vertex_shape':'A-B-A','distinct_removed_edge_ids_and_residual_digests':True,'original':'immutable four-edge walk','scope':'Synthetic path IDs only, no observed audit log, row issuer or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/overlapping-cycle-reductions.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
