"""Typed edge commitments must include source manifest and exact target scopes."""
from hashlib import sha256
from pathlib import Path
import json
rows1=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
rows2=rows1[:1]+(((1,0),2),)+rows1[2:]
def H(value):return sha256(json.dumps(value,separators=(',',':'),sort_keys=True).encode()).hexdigest()
base={'from':'fictional-x1','to':'fictional-x2','rule':'bound-weakening','manifest':H(rows1),'source_target':{'normal':[1,0],'bound':1},'dest_target':{'normal':[1,0],'bound':2}}
changed_source=dict(base,manifest=H(rows2));changed_target=dict(base,dest_target={'normal':[1,0],'bound':3})
coarse=lambda edge:H((edge['from'],edge['to'],edge['rule']))
assert coarse(base)==coarse(changed_source)==coarse(changed_target)
assert len({H(base),H(changed_source),H(changed_target)})==3
def replay(edge,source_rows,source_target,dest_target):
 if edge['manifest']!=H(source_rows):return 'SOURCE_MANIFEST_MISMATCH'
 if edge['source_target']!=source_target or edge['dest_target']!=dest_target:return 'EXACT_TARGET_MISMATCH'
 return 'STRUCTURAL_SCOPE_MATCH_ONLY'
assert replay(base,rows1,base['source_target'],base['dest_target'])=='STRUCTURAL_SCOPE_MATCH_ONLY'
assert replay(base,rows2,base['source_target'],base['dest_target'])=='SOURCE_MANIFEST_MISMATCH'
assert replay(base,rows1,base['source_target'],changed_target['dest_target'])=='EXACT_TARGET_MISMATCH'
report={'passed':True,'coarse_vertex_rule_commitment':'collides on changed rows or changed destination bound','full_commitment':'distinct across source row digests and exact endpoint targets','replay':'rejects changed manifest or target; matching scope does not prove valid Farkas packets or observed events','scope':'Local synthetic binding only, no authorized source issuer or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/path-edge-manifest-target-binding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
