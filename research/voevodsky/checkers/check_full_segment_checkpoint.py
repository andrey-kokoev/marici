"""Owning forced-zero migration: full two-cell coverage and later restriction."""
from fractions import Fraction as Q
from itertools import combinations
from copy import deepcopy
from pathlib import Path
import gzip,json
from full_segment_checkpoint import FullSegmentSession,coverage_rows,segment_targets,verify_full_segment
from checked_retirement_interface import migrate
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/voevodsky/results'
def certificate(rows,target):
 n,b=target
 for i,(a,h) in enumerate(rows):
  for j in range(2):
   if a[j]:
    w=n[j]/a[j]
    if w>=0 and tuple(w*x for x in a)==n and w*h<=b:
     result=[Q(0)]*len(rows);result[i]=w;return list(map(str,result))
 for i,j in combinations(range(len(rows)),2):
  a,h=rows[i];c,k=rows[j];det=a[0]*c[1]-a[1]*c[0]
  if not det:continue
  u=(n[0]*c[1]-n[1]*c[0])/det;v=(a[0]*n[1]-a[1]*n[0])/det
  if u>=0 and v>=0 and u*h+v*k<=b:
   result=[Q(0)]*len(rows);result[i]=u;result[j]=v;return list(map(str,result))
 raise AssertionError('no two-row certificate')
def main():
 plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
 case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
 producer=migrate(plan,case,retain_lift=True);s=FullSegmentSession();boot=s.bootstrap(plan,case,retain_lift=True)
 vertices=[['0','0'],['1/2','1/2'],['1','1']];_,targets=segment_targets(tuple(map(Q,vertices[0])),tuple(map(Q,vertices[-1])))
 packet={'migration_binding':boot['state']['migration_binding'],'vertices':vertices,
  'source_lifts':[['0','0','0'],['1/2','0','0'],['1','0','0']],
  'coverage_weights':[certificate(coverage_rows(producer),t) for t in targets]}
 rejected=[]
 def reject(name,f):
  try:f()
  except (AssertionError,ValueError,PermissionError,StopIteration):rejected.append(name)
  else:raise AssertionError(name+' accepted')
 for mode in ('missing-implication','negative-weight','wrong-source-lift','unordered-knots','foreign-migration'):
  bad=deepcopy(packet)
  if mode=='missing-implication':bad['coverage_weights'].pop()
  elif mode=='negative-weight':bad['coverage_weights'][0][0]='-1'
  elif mode=='wrong-source-lift':bad['source_lifts'][1]=['0','0','0']
  elif mode=='unordered-knots':bad['vertices'][1]=['2','2']
  else:bad['migration_binding']='foreign'
  reject(mode,lambda:s.attach_full_segment(boot['handle'],boot['state'],vertices,bad))
 attached=s.attach_full_segment(boot['handle'],boot['state'],vertices,packet);sid=attached['section_id'];handle=attached['handle']
 assert verify_full_segment(producer,vertices,packet)==attached['attachment_work']
 for t in ('0','1/4','1/2','3/4','1'):assert s.covered_lift(handle,sid,[t,t])==[t,'0','0']
 reject('off-line-point',lambda:s.covered_lift(handle,sid,['1/2','1/3']))
 op={'kind':'append-public','normal':['1','0'],'upper':'3/4'};refined=producer.refine(op['normal'],op['upper']);answer=refined.maximize([1,0])
 after=s.advance(handle,attached['state'],op,[1,0],answer)
 assert s.covered_lift(after['handle'],sid,['3/4','3/4'])==['3/4','0','0']
 reject('excluded-endpoint',lambda:s.covered_lift(after['handle'],sid,['1','1']))
 reject('stale-handle',lambda:s.covered_lift(handle,sid,['0','0']))
 reject('archive-escalation',lambda:s.reexpose(after['handle']))
 report={'passed':True,'migration':plan['name'],'section':packet,'attachment':attached,'successor':after,
 'rejections':rejected,'scope':'Full coverage for the real rank-one forced-zero migration, two cells with a shared vertex array. Not a general higher-dimensional triangulation verifier.'}
 (OUT/'full-segment-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'attachment_work':attached['attachment_work'],'rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
