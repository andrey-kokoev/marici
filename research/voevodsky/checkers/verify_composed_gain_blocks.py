"""Independent closure, block coverage and glued-lift replay."""
from pathlib import Path
from fractions import Fraction as Q
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def check_block(b,expected):
 nodes=b['nodes'];assert len(set(nodes))==len(nodes);pos={v:i for i,v in enumerate(nodes)}
 e=[(u,v,Q(w)) for u,v,w in b['edges']];assert e==expected
 D=[[Q(w) for w in row] for row in b['distance']];n=len(nodes)
 assert len(D)==n and all(len(row)==n for row in D)
 for i in range(n):
  assert D[i][i]==0
  for j in range(n):
   node=nodes[i];bound=Q(0)
   for k in b['paths'][i][j]:
    assert type(k) is int and 0<=k<len(e);u,v,w=e[k];assert u==node;node=v;bound+=w
   assert node==nodes[j] and bound==D[i][j]
   assert all(D[i][j]<=D[i][k]+D[k][j] for k in range(n))
 assert all(D[pos[u]][pos[v]]<=w for u,v,w in e)
 A=b['interface'];assert len(set(A))==len(A) and set(A)<=set(nodes)
 assert b['summary']==[[u,v,str(D[pos[u]][pos[v]])] for u in A for v in A if u!=v]
 return D,pos

def main():
 if not __debug__:raise RuntimeError('Assertions required')
 subprocess.run([sys.executable,str(Path(__file__).with_name('verify_balanced_gain_elimination.py'))],check=True,capture_output=True)
 parents=json.loads((OUT/'balanced-gain-elimination.json').read_text())['packets']
 packets=json.loads((OUT/'composed-gain-blocks.json').read_text())['packets'];assert len(packets)==len(parents)==3
 for parent,p in zip(parents,packets):
  m=parent['m'];assert p['m']==m
  E=[(u,v,Q(w)) for u,v,w in parent['normalized_edges']];blocks=p['blocks'];assert len(blocks)==2
  covered=set();interfaces=[];merged=[]
  for b in blocks:
   expected=[e for e in E if e[0] in b['nodes'] and e[1] in b['nodes']]
   check_block(b,expected);covered.update(expected);interfaces.append(set(b['interface']))
   merged.extend((u,v,Q(w)) for u,v,w in b['summary'])
  assert covered==set(E)
  shared=set(blocks[0]['nodes'])&set(blocks[1]['nodes'])
  assert shared<=interfaces[0]&interfaces[1]
  assert set().union(*(set(b['nodes']) for b in blocks))==set(range(m+1))
  c=p['composed'];assert set(c['nodes'])==set.union(*interfaces) and c['interface']==[0,1,m]
  D,pos=check_block(c,merged);G=[[Q(w) for w in r] for r in parent['distance']]
  assert all(D[pos[u]][pos[v]]==G[u][v] for u in c['nodes'] for v in c['nodes'])
  for sample in p['lifts']:
   z=list(map(Q,sample['normalized_lift']));assert len(z)==m+1 and z[0]==0
   assert all(z[v]-z[u]<=w for u,v,w in E)
   assert [z[a] for a in (0,1,m)]==list(map(Q,sample['public']))
   assert all(z[int(v)]==Q(w) for v,w in sample['shared'].items())
   scales=list(map(Q,parent['scales']));x=[scales[j]*z[j+1] for j in range(m)]
   assert all(0<=v<=100+2*j for j,v in enumerate(x))
   assert all(x[v]<=Q(g)*x[u]+Q(w) for u,v,g,w in parent['gain_rows'])
 result={'passed':True,'systems':3,'certified_blocks':6,'composed_interfaces':3,'source_lifts':6,
 'scope':'Block summaries and gluing checked independently; shared coordinate charts fixed by parent certificates.'}
 (OUT/'composed-gain-blocks-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
