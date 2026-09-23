"""Compose independently checked scalar sections, source norms and reuse."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import json
from approximate_section_checkpoint import Session,initial,check,domain
from verify_approximate_atom_lift import verify
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';OUT=ROOT/'research/voevodsky/results'
def main():
 packets=json.loads((N/'scalar-envelope-band-packets.json').read_text());rejected=[];reports=[]
 def reject(name,call):
  try:call()
  except (AssertionError,ValueError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
 for eta in ('1/1000','1/100'):
  packet=next(p for p in packets if p['request']=={'n':18,'eta':eta})
  request={'n':18,'eta':eta};expected=initial(request);s=Session()
  bad=deepcopy(packet);bad['cells'][0]['formula'][2]='100'
  reject('corrupt-section',lambda:s.bootstrap(expected,bad))
  candidate=deepcopy(packet);boot=s.bootstrap(expected,candidate);h=boot['handle'];polygon=domain(18)
  p=[str(sum(v[j] for v in polygon)/len(polygon)) for j in range(2)]
  answer=s.lift(h,p);assert verify(expected,p,answer)
  # Independent responses at every original vertex, not only the centroid.
  for v in polygon:
   point=list(map(str,v));assert verify(expected,point,s.lift(h,point))
  # Caller mutation of the candidate and receipt must not poison trust.
  candidate['cells'][0]['formula'][2]='100'
  boot['state']['capabilities']['archive']=True
  op={'kind':'append-public','normal':['1','0'],'upper':'3/4'}
  next_receipt=s.restrict(h,expected,op);after=next_receipt['state'];new=next_receipt['handle']
  fresh=s.lift(new,p);assert verify(after,p,fresh)
  boot['state']=deepcopy(expected) # restore report copy after mutation control
  # Fresh whole-polygon replay remains a valid stronger proof for restriction.
  full=check(request,packet);assert next_receipt['reuse']['verified_cells_retained']==full['cells']
  reject('stale-handle',lambda:s.lift(h,p))
  reject('excluded-point',lambda:s.lift(new,['1','1']))
  reject('fine-refinement',lambda:s.restrict(new,after,{'kind':'append-fine','normal':['1','0'],'upper':'1'}))
  reject('archive-request',lambda:s.reexpose(new))
  bad=deepcopy(fresh);bad['source_lift'][0]='0'
  reject('corrupt-atom-answer',lambda:verify(after,p,bad))
  reject('stale-answer-binding',lambda:verify(after,p,answer))
  report={'request':request,'bootstrap':boot,'successor':next_receipt,'answer':fresh,
   'full_replay_plane_vertex_checks':full['plane_vertex_checks']}
  reports.append(report)
 result={'passed':True,'cases':reports,'rejections':rejected,
 'scope':'Nima whole-polygon proofs + independently checked original-atom approximate answers; process-local restriction reuse. Not exact-fiber reexposure, arbitrary migration compilation, or Nima backend integration.'}
 (OUT/'approximate-section-checkpoint.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'cases':len(reports),'rejections':len(rejected),
  'reused_cells':[r['successor']['reuse']['verified_cells_retained'] for r in reports],
  'full_replay_plane_vertex_checks':[r['full_replay_plane_vertex_checks'] for r in reports]},indent=2))
if __name__=='__main__':main()
