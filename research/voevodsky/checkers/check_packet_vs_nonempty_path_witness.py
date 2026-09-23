"""A proof packet cannot substitute for a nonempty path from another occurrence."""
from pathlib import Path
import json
packet={'id':'fictional-end','weights':(0,1,0,0),'surplus':1,'target':((1,0),2)}
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def valid(p):
 m=p['weights'];c=p['surplus']
 return min((*m,c))>=0 and tuple(sum(m[i]*rows[i][0][j] for i in range(4)) for j in (0,1))==p['target'][0] and sum(m[i]*rows[i][1] for i in range(4))+c==p['target'][1]
def path(start,end,edges):
 if not edges:return 'NO_NONEMPTY_PATH_WITNESS'
 cursor=start
 for frm,to,rule in edges:
  if frm!=cursor or rule!='bound-weakening@1':return 'BROKEN_OR_UNKNOWN_EDGE'
  cursor=to
 return 'SYNTHETIC_PATH_SHAPE_ONLY' if cursor==end else 'WRONG_TERMINAL_OCCURRENCE'
assert valid(packet)
assert path('fictional-start',packet['id'],[])=='NO_NONEMPTY_PATH_WITNESS'
assert path('fictional-start',packet['id'],[('fictional-start',packet['id'],'bound-weakening@1')])=='SYNTHETIC_PATH_SHAPE_ONLY'
assert path('fictional-start',packet['id'],[('wrong',packet['id'],'bound-weakening@1')])=='BROKEN_OR_UNKNOWN_EDGE'
report={'passed':True,'standalone_packet':'valid x<=2 math','claimed_distinct_start_with_no_edges':'NO_NONEMPTY_PATH_WITNESS','typed_edge':'synthetic path shape only, no packet-edge semantic or historical verification','scope':'No observed occurrence, authenticated source event, owner grant or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/packet-vs-nonempty-path-witness.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
