"""Real migration-bound segment section and restriction across its interior."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import json,gzip
from migration_section_checkpoint import SectionSession,check_section
from checked_retirement_interface import migrate,source,dec
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/voevodsky/results'
def main():
 plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
 cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
 plan,case=plans[2],cases[2];s=SectionSession();boot=s.bootstrap(plan,case,retain_lift=True)
 records=sorted(case['queries'][:2],key=lambda q:Q(q['public'][0]));vertices=[q['public'] for q in records]
 proof={'migration_binding':boot['state']['migration_binding'],'vertices':vertices,'source_lifts':[q['source_lift'] for q in records]}
 rejected=[]
 def reject(name,call):
  try:call()
  except (ValueError,AssertionError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
 for mode in ('foreign-migration','invalid-witness','global-coverage-claim','wrong-domain'):
  bad=deepcopy(proof)
  if mode=='foreign-migration':bad['migration_binding']='unrelated'
  elif mode=='invalid-witness':bad['source_lifts'][0][0]='-1'
  elif mode=='global-coverage-claim':bad['covers_entire_runtime']=True
  else:bad['vertices'][0][0]='0'
  reject(mode,lambda:s.attach(boot['handle'],boot['state'],vertices,bad))
 attached=s.attach(boot['handle'],boot['state'],vertices,proof);sid=attached['section_id'];handle=attached['handle']
 reject('stale-bootstrap',lambda:s.section_lift(boot['handle'],sid,vertices[0],['1','0']))
 midpoint=[str((Q(a)+Q(b))/2) for a,b in zip(*vertices)]
 first=s.section_lift(handle,sid,midpoint,['1/2','1/2'])
 reject('wrong-barycentric-point',lambda:s.section_lift(handle,sid,vertices[0],['1/2','1/2']))
 reject('negative-weight',lambda:s.section_lift(handle,sid,midpoint,['-1','2']))
 producer=migrate(plan,case,retain_lift=True);objective=[1]+[0]*(len(midpoint)-1)
 # Independent full section replay against owning fine context.
 assert check_section(producer,vertices,proof)==2
 operation={'kind':'append-public','normal':objective,'upper':midpoint[0]}
 refined=producer.refine(objective,midpoint[0]);answer=refined.maximize(objective)
 advanced=s.advance(handle,attached['state'],operation,objective,answer)
 second=s.section_lift(advanced['handle'],sid,midpoint,['1/2','1/2'])
 assert first['source_lift']==second['source_lift']
 reject('excluded-section-vertex',lambda:s.section_lift(advanced['handle'],sid,vertices[1],['0','1']))
 reject('section-is-not-archive',lambda:s.reexpose(advanced['handle']))
 # Direct exact checking of interpolated source against expected original history
 # and NEW public evidence; does not rely on interpolation service's claim.
 t=tuple(map(Q,second['source_lift']));_,_,observe,caps=source(plan['m'],plan['audits']);joint=observe(t)
 assert all(0<=x<=b for x,b in zip(t,caps))
 assert all(sum(a*x for a,x in zip(n,joint))<=b for n,b in map(dec,plan['frames']))
 k=2+plan['audits'].index(plan['retire']);assert joint[:k]+joint[k+1:]==tuple(map(Q,midpoint))
 assert Q(midpoint[0])<=Q(operation['upper'])
 assert advanced['section_work']['vertex_checks']==2
 no_lift=SectionSession();a=no_lift.bootstrap(plan,case)
 reject('answer-only-attachment',lambda:no_lift.attach(a['handle'],a['state'],vertices,proof))
 report={'passed':True,'migration':plan['name'],'section':proof,'attached_receipt':attached,
 'refined_receipt':advanced,'interpolated_before':first,'interpolated_after':second,
 'rejections':rejected,'scope':'A declared segment bound to a real owning migration. Full-domain coverage is neither requested nor certified. No Nima backend integration.'}
 (OUT/'migration-section-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'vertex_checks':2,'rejections':len(rejected),'coverage':'declared-segment-only'},indent=2))
if __name__=='__main__':main()
