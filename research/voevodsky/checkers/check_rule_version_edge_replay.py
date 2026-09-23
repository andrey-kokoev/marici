"""Equal local Boolean outcome does not license relabelling an edge's rule version."""
from hashlib import sha256
from pathlib import Path
import json
def H(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
edge={'from':'synthetic-P','to':'synthetic-Q','source':'synthetic-rows-v1','rule':'comparison@1','targets':[[1,0,2],[1,0,2]]}
new=dict(edge,rule='comparison@2')
assert edge['targets']==new['targets'] and H(edge)!=H(new)
def scope(commit,request):return 'EXACT_RULE_VERSION_OR_EDGE_MISMATCH' if H(commit)!=H(request) else 'STRUCTURAL_MATCH_NOT_OBSERVED'
assert scope(edge,new)=='EXACT_RULE_VERSION_OR_EDGE_MISMATCH'
assert scope(edge,edge)=='STRUCTURAL_MATCH_NOT_OBSERVED'
report={'passed':True,'both_target_comparisons':'same local equality outcome under hypothetical @1/@2','edge_digests':'different because rule version is committed','replay_as_new_version':'EXACT_RULE_VERSION_OR_EDGE_MISMATCH','scope':'No real version-2 semantics, signature verification, owner grant, observed event or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/rule-version-edge-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
