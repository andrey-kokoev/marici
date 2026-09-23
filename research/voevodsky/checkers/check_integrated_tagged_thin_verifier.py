"""Independent bounded checker for proof leaves, rooted rotations and thin view."""
from hashlib import sha256
from pathlib import Path
import json
ANCHOR={'a':((-1,0),(1,0),(0,-1),(0,1)), 'bounds':(0,1,0,1)}
ROWS=ANCHOR['a'];BOUNDS=ANCHOR['bounds']
root_hash=sha256(repr((ROWS,BOUNDS)).encode()).hexdigest()
LEAF={'a':((1,2,0,0),(1,0),2),'b':((0,0,1,2),(0,1),2),
      'c':((0,1,0,0),(1,0),1),'d':((0,0,0,1),(0,1),1)}
def children(t):return () if isinstance(t,str) else (t[0],t[1])
def leaves(t):return (t,) if isinstance(t,str) else leaves(t[0])+leaves(t[1])
def rotations(t):
 if isinstance(t,str):return set()
 x,y=t;out=set()
 if isinstance(x,tuple):out.add((x[0],(x[1],y)))
 out|={(q,y) for q in rotations(x)}|{(x,q) for q in rotations(y)}
 return out
def verify(packet):
 rows=packet['rows'];bounds=packet['bounds']
 if sha256(repr((rows,bounds)).encode()).hexdigest()!=root_hash:return 'SOURCE_ANCHOR_MISMATCH'
 for m,v,T in LEAF.values():
  if any(z<0 for z in m) or tuple(sum(rows[i][j]*m[i] for i in range(4)) for j in range(2))!=v or sum(bounds[i]*m[i] for i in range(4))!=T:return 'INVALID_FARKAS_LEAF'
 path=packet['path']
 if not path or any(leaves(t)!=('a','b','c','d') for t in path):return 'INVALID_LEAF_TAGS'
 if any(y not in rotations(x) for x,y in zip(path,path[1:])):return 'INVALID_ROTATION'
 graph=packet['support']
 def rooted(node,stack=()):
  if node in stack:return False
  if node=='trusted-row-anchor':return True
  if node in LEAF:return node in graph and graph[node]==('trusted-row-anchor',)
  return node in graph and bool(graph[node]) and all(rooted(k,stack+(node,)) for k in graph[node])
 if any(not rooted('edge-'+str(i)) for i in range(len(path)-1)):return 'UNROOTED_EDGE'
 if packet['thin']!=(path[0],path[-1]):return 'FORGED_THIN_PROJECTION'
 if packet.get('authorize_actual_execution'):return 'NO_EXECUTION_AUTHORITY'
 return 'MATHEMATICALLY_VERIFIED_LOCAL_RECORD'
a=((('a','b'),'c'),'d');mid=(('a','b'),('c','d'));end=('a',('b',('c','d')))
support={**{k:('trusted-row-anchor',) for k in LEAF},'edge-0':tuple(LEAF),'edge-1':('edge-0',)+tuple(LEAF)}
p={'rows':ROWS,'bounds':BOUNDS,'path':(a,mid,end),'thin':(a,end),'support':support}
assert verify(p)=='MATHEMATICALLY_VERIFIED_LOCAL_RECORD'
assert verify({**p,'bounds':(0,2,0,1)})=='SOURCE_ANCHOR_MISMATCH'
assert verify({**p,'path':(a,end),'thin':(a,end)})=='INVALID_ROTATION'
assert verify({**p,'support':{**support,'edge-0':('edge-1',)}})=='UNROOTED_EDGE'
assert verify({**p,'thin':(a,mid)})=='FORGED_THIN_PROJECTION'
assert verify({**p,'authorize_actual_execution':True})=='NO_EXECUTION_AUTHORITY'
report={'passed':True,'accepted':'MATHEMATICALLY_VERIFIED_LOCAL_RECORD','distinct_refusals':['SOURCE_ANCHOR_MISMATCH','INVALID_ROTATION','UNROOTED_EDGE','FORGED_THIN_PROJECTION','NO_EXECUTION_AUTHORITY'],'leaf_certificates_checked':4,'rotation_edges_checked':2,'trust_boundary':'Local hardcoded source anchor and dependency graph; neither provider authentication nor historical execution or pentagon higher filler.'}
out=Path(__file__).resolve().parents[1]/'results/integrated-tagged-thin-verifier.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
