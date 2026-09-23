"""An empty derived view retains lineage; it is not the original identity path."""
from hashlib import sha256
from pathlib import Path
import json
edges=(('A','B','e1'),('B','A','e2'),('A','B','e3'),('B','A','e4'))
def H(x):return sha256(repr(x).encode()).hexdigest()
def reduce(view,start):
 es=view['remaining'];removed=es[start:start+2]
 if len(removed)!=2 or removed[0][0]!=removed[-1][1]:raise ValueError('NOT_CLOSED_PAIR')
 return {'origin':view['origin'],'remaining':es[:start]+es[start+2:],'lineage':view['lineage']+({'parent_digest':H(es),'removed_ids':tuple(e[2] for e in removed),'removed_digest':H(removed)},)}
initial={'origin':H(edges),'remaining':edges,'lineage':()}
first=reduce(initial,0);second=reduce(first,0)
assert first['remaining']==edges[2:] and second['remaining']==()
assert len(second['lineage'])==2 and second['origin']==H(edges)
identity={'origin':H(()),'remaining':(),'lineage':()}
assert second!=identity and second['origin']!=identity['origin'] and len(edges)==4
assert second['lineage'][1]['parent_digest']==H(first['remaining'])
report={'passed':True,'final_edge_count':0,'reduction_lineage_length':2,'original_edge_count':4,'empty_derived_view':'not equal original zero-length identity','scope':'Synthetic rewrite lineage only, no actual observed events, source issuer or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/repeated-cycle-reduction-lineage.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
