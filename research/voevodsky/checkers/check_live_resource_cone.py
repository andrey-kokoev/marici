"""Nine live providers realizing B*(Delta1 x Delta3) for one owning migration.
Arrows compare exact lifting on included domains; not archive authority.
"""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json,gzip,hashlib
from full_segment_checkpoint import FullSegmentSession
from checked_retirement_interface import migrate
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/voevodsky/results'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def brackets(xs):
 if len(xs)==1:return [xs[0]]
 return [compose(a,b) for i in range(1,len(xs)) for a in brackets(xs[:i]) for b in brackets(xs[i:])]
def compose(a,b):
 assert a['target']==b['source'] and a['root']==b['root'] and a['formula']==b['formula']
 return {'source':a['source'],'target':b['target'],'root':a['root'],'formula':a['formula']}
def main():
 plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
 case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
 template=json.loads((OUT/'full-segment-checkpoint.json').read_text())['section']
 producer=migrate(plan,case,retain_lift=True);nodes={};packets={};calls=0
 meshes=[['0','1'],['0','1/2','1'],['0','1/4','3/4','1'],['0','1/3','2/3','1']]
 answers={}
 for cap in ('1/2','3/4','7/8'):
  answers[cap]=producer.refine([1,0],cap).maximize([1,0])
 def admit(name,knots,cap):
  proof=deepcopy(template);proof['vertices']=[[u,u] for u in knots];proof['source_lifts']=[[u,'0','0'] for u in knots]
  service=FullSegmentSession();boot=service.bootstrap(plan,case,retain_lift=True)
  receipt=service.attach_full_segment(boot['handle'],boot['state'],proof['vertices'],proof);sid=receipt['section_id']
  if cap!='1':
   op={'kind':'append-public','normal':['1','0'],'upper':cap}
   receipt=service.advance(receipt['handle'],receipt['state'],op,[1,0],answers[cap])
  nodes[name]={'service':service,'receipt':receipt,'sid':sid,'cap':Q(cap)};packets[name]=proof
 admit('B',meshes[1],'1/2')
 for i,mesh in enumerate(meshes):
  admit('T'+str(i),mesh,'1');admit('R'+str(i),mesh,'3/4')
 formula={'public':'(u,u)','source':['u','0','0']};root=producer.migration_binding
 def observed(name):
  node=nodes[name];s=node['service'];r=node['receipt']
  s._current(r['handle']) # live ownership, not a packet's positive capability bit
  assert s._state.descriptor()==r['state'] and s._state.migration_binding==root
  assert s._state.lift_json is not None and s._state.archive_json is None
  assert node['sid'] in s._covers and json.loads(s._covers[node['sid']])==packets[name]
  proof=packets[name]
  assert all(v[0]==v[1] and t==[v[0],'0','0'] for v,t in zip(proof['vertices'],proof['source_lifts']))
  # Every admitted cell therefore interpolates EXACTLY this common formula.
  frames=r['state']['public_frames'];expected=[] if node['cap']==1 else [{'normal':['1','0'],'upper':str(node['cap'])}]
  assert frames==expected
  return {'name':name,'scope':['0',str(node['cap'])],'root':root,'formula':formula,
   'resources':{'section_digest':digest(proof),'lift_context_digest':digest(json.loads(s._state.lift_json))},
   'capabilities':['exact-fine-lift-on-scope'],'archive_authority':False}
 def edge(a,b):
  nonlocal calls
  oa,ob=observed(a),observed(b);assert nodes[a]['cap']<=nodes[b]['cap']
  assert oa['root']==ob['root'] and oa['formula']==ob['formula']
  # Whole-domain comparison comes from the verified affine formulas, not samples.
  for u in (Q(0),nodes[a]['cap']/2,nodes[a]['cap']):
   x=nodes[a]['service'].covered_lift(nodes[a]['receipt']['handle'],nodes[a]['sid'],[str(u),str(u)])
   y=nodes[b]['service'].covered_lift(nodes[b]['receipt']['handle'],nodes[b]['sid'],[str(u),str(u)])
   assert x==y==[str(u),'0','0'];calls+=2
  return {'source':a,'target':b,'root':root,'formula':formula}
 # Four cone-on-prism top simplices, all with six vertices and five arrows.
 chains=[];checks=0
 for k in range(4):
  names=['B']+['R'+str(i) for i in range(k+1)]+['T'+str(i) for i in range(k,4)]
  arrows=[edge(a,b) for a,b in zip(names,names[1:])]
  results=brackets(arrows);assert len(results)==14 and all(r==edge_result for r in results for edge_result in [results[0]])
  assert results[0]=={'source':'B','target':'T3','root':root,'formula':formula}
  checks+=len(results);chains.append(names)
 snapshots={name:observed(name) for name in nodes}
 assert len({snapshots['T'+str(i)]['resources']['section_digest'] for i in range(4)})==4
 # A real head change invalidates the old provider even though its frozen
 # descriptor, section hash and claimed capability still look correct.
 n=nodes['T0'];op={'kind':'append-public','normal':['1','0'],'upper':'7/8'}
 n['service'].advance(n['receipt']['handle'],n['receipt']['state'],op,[1,0],answers['7/8'])
 refused=False
 try:edge('B','T0')
 except ValueError:refused=True
 assert refused
 report={'passed':True,'nodes':snapshots,'top_simplex_paths':chains,'checked_parenthesizations':checks,
 'live_interpolation_calls':calls,'stale_provider_refused':refused,
 'scope':'Nine live providers in one verified migration, exact lifting on scoped intervals, certified provider substitution. No history-archive authority or identification with the original analytic roles.'}
 (OUT/'live-resource-cone.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'live_vertices':9,'top_simplices':4,'parenthesizations':checks,'live_interpolation_calls':calls,'stale_provider_refused':refused},indent=2))
if __name__=='__main__':main()
