"""Shared-subproof DAG admits multiple valid temporal linearizations."""
from pathlib import Path
import json
primitive={'X':((1,0),1),'Y':((0,1),1)}
derivations={'Z':(('X',1),('Y',1)),'W':(('Z',1),('X',1)),'V':(('Z',1),('Y',1)),'T':(('W',1),('V',1))}
def packet(deps,known):return (tuple(sum(weight*known[node][0][j] for node,weight in deps) for j in (0,1)),sum(weight*known[node][1] for node,weight in deps))
def replay(order):
 known=dict(primitive)
 for node in order:
  if node in known or any(dep not in known for dep,_ in derivations[node]):raise ValueError('INVALID_TEMPORAL_REPLAY')
  known[node]=packet(derivations[node],known)
 return known
first=('Z','W','V','T');second=('Z','V','W','T')
a=replay(first);b=replay(second)
assert a==b and a['Z']==((1,1),2) and a['W']==((2,1),3) and a['V']==((1,2),3) and a['T']==((3,3),6)
assert first!=second and set(first)==set(second)==set(derivations)
# T unfolds the shared Z TWICE but its DAG has ONE Z node/event.
def unfolded(node):
 if node in primitive:return (node,)
 return tuple(x for dep,_ in derivations[node] for x in unfolded(dep))
assert unfolded('T').count('X')==3 and unfolded('T').count('Y')==3
assert first.count('Z')==second.count('Z')==1
try:replay(('Z','T','W','V'))
except ValueError as err:assert str(err)=='INVALID_TEMPORAL_REPLAY'
else:raise AssertionError('out of order accepted')
report={'passed':True,'shared_subproof':'Z','DAG_node_count':4,'valid_temporal_orders':[list(first),list(second)],'same_derived_row_packets':True,'same_DAG_different_order':True,'invalid_order_refused':True,'historical_replay_requires':'chosen event order and event IDs beyond DAG dependencies','scope':'Frozen square source proof DAG, not actual observed execution, source-owner grant, or analytic role assignment.'}
out=Path(__file__).resolve().parents[1]/'results/shared-square-derivation-dag.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
