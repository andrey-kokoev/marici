"""Compose two certified difference-coordinate blocks of a balanced source.
Shared interface: zero anchor, first atom, split atom, last atom. The chord
belongs to the right block. Every block is bounded through the shared anchor.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_chain_audit_elimination import close
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def block(nodes,edges,interface):
 pos={v:i for i,v in enumerate(nodes)}
 local=[(pos[u],pos[v],w) for u,v,w in edges]
 d,paths=close(len(nodes)-1,local,range(len(nodes)))
 assert all(d[i][i]==0 for i in range(len(nodes)))
 summary=[(u,v,d[pos[u]][pos[v]]) for u in interface for v in interface if u!=v]
 return {'nodes':nodes,'interface':interface,'edges':[[u,v,str(w)] for u,v,w in edges],
 'distance':[[str(w) for w in row] for row in d],'paths':paths,'summary':[[u,v,str(w)] for u,v,w in summary]}
def main():
 original=json.loads((OUT/'balanced-gain-elimination.json').read_text())['packets'];packets=[]
 for p in original:
  m=p['m'];split=m//2;edges=[(u,v,Q(w)) for u,v,w in p['normalized_edges']]
  left_nodes=list(range(split+1));right_nodes=[0,1]+list(range(split,m+1))
  left=[];right=[]
  for e in edges:
   u,v,w=e
   # Duplicate shared-node cap constraints harmlessly; other edges have one owner.
   if u in left_nodes and v in left_nodes:left.append(e)
   if u in right_nodes and v in right_nodes:right.append(e)
  assert set(left)|set(right)==set(edges)
  l=block(left_nodes,left,[0,1,split]);r=block(right_nodes,right,[0,1,split,m])
  interface=[0,1,split,m]
  merged=[(u,v,Q(w)) for b in (l,r) for u,v,w in b['summary']]
  bridge=block(interface,merged,[0,1,m]);idx={v:i for i,v in enumerate(interface)}
  d=[[Q(w) for w in row] for row in bridge['distance']];global_d=[[Q(w) for w in row] for row in p['distance']]
  assert all(d[idx[a]][idx[b]]==global_d[a][b] for a in interface for b in interface)
  lifts=[]
  for sample in p['samples']:
   outer=dict(zip([0,1,m],map(Q,sample['scaled_public'])))
   shared={v:min(outer[a]+d[idx[a]][idx[v]] for a in outer) for v in interface}
   z={}
   for b in (l,r):
    positions={v:i for i,v in enumerate(b['nodes'])};D=[[Q(w) for w in row] for row in b['distance']]
    local={v:min(shared[a]+D[positions[a]][positions[v]] for a in b['interface']) for v in b['nodes']}
    for v,value in local.items():
     if v in z:assert z[v]==value
     z[v]=value
   assert all(z[v]-z[u]<=w for u,v,w in edges)
   assert all(z[a]==v for a,v in outer.items())
   lifts.append({'public':list(map(str,[outer[a] for a in [0,1,m]])),
     'shared':{str(k):str(v) for k,v in shared.items()},'normalized_lift':[str(z[v]) for v in range(m+1)]})
  packets.append({'m':m,'blocks':[l,r],'composed':bridge,'lifts':lifts})
 (OUT/'composed-gain-blocks.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps({'passed':True,'systems':len(packets),'block_summaries':2*len(packets),'composed_lifts':sum(len(p['lifts']) for p in packets)}))
if __name__=='__main__':main()
