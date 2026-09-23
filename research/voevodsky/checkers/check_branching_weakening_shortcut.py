"""Endpoint packet equality cannot select one synthetic branching audit path."""
from hashlib import sha256
from pathlib import Path
import json
packets={'start':(1,0),'middle-A':(2,1),'middle-B':(2,1),'end':(3,2)}
paths=(('start','middle-A','end'),('start','middle-B','end'))
def H(x):return sha256(repr(x).encode()).hexdigest()
def validate(path):
 assert all(packets[path[i+1]][0]>=packets[path[i]][0] and packets[path[i+1]][1]-packets[path[i]][1]==packets[path[i+1]][0]-packets[path[i]][0] for i in range(len(path)-1))
 return {'type':'derived-shortcut','from':path[0],'to':path[-1],'parent_path_ids':path,'parent_path_digest':H(path),'observed_direct_edge':False}
a,b=map(validate,paths)
assert packets[paths[0][0]]==packets[paths[1][0]] and packets[paths[0][-1]]==packets[paths[1][-1]]
assert a['parent_path_digest']!=b['parent_path_digest']
def pick_by_endpoints(start,end):
 matches=[p for p in paths if p[0]==start and p[-1]==end]
 if len(matches)!=1:raise ValueError('AMBIGUOUS_PATH')
 return validate(matches[0])
try:pick_by_endpoints('start','end')
except ValueError as err:assert str(err)=='AMBIGUOUS_PATH'
else:raise AssertionError('endpoint-only shortcut silently chose path')
report={'passed':True,'middle_math':'equal packet (x<=2, surplus1), different occurrence IDs','endpoint_math':'equal x<=3, surplus2','endpoint_only':'AMBIGUOUS_PATH','selected_shortcuts':'two separate source-path digests; no observed direct edge','scope':'Fictional branching audit fixture, not actual observation, issuer permission or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/branching-weakening-shortcut.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
