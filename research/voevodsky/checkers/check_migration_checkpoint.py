"""Real owning migrations, independent answer proofs, and cached point lifts."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as Q
import json,gzip
from migration_checkpoint import Session
from checked_retirement_interface import migrate,verify_answer
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/voevodsky/results'
def main():
 plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
 cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
 rejected=[];reports=[]
 def reject(name,call):
  try:call()
  except (ValueError,AssertionError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
 for i in (0,2):
  plan,case=plans[i],cases[i];s=Session();p=deepcopy(plan);c=deepcopy(case)
  bad=deepcopy(c);bad['runtime']['frames'].pop()
  reject('invalid-migration',lambda:s.bootstrap(p,bad,retain_lift=True))
  receipt=s.bootstrap(p,c,retain_lift=True);before=deepcopy(receipt['state']);handle=receipt['handle']
  # No archive retained; independent producer supplies successor query packets.
  producer=migrate(plan,case,retain_lift=True);d=2+len(case['runtime']['audits']);objective=[1]+[0]*(d-1)
  answer=producer.maximize(objective);point=answer['proof']['point'];upper=answer['proof']['value']
  t=s.fine_lift(handle,point);t[0]='-999' # returned list must not poison cache
  assert s.fine_lift(handle,point)[0]!='-999'
  p['frames']=[];c['runtime']['frames']=[];receipt['state']['capabilities']['reexpose']=True
  row=objective;operation={'kind':'append-public','normal':row,'upper':upper}
  refined=producer.refine(row,upper);fresh=refined.maximize(objective)
  bad=deepcopy(fresh);bad['state']['capabilities']['reexpose']=True
  reject('capability-escalation',lambda:s.advance(handle,before,operation,objective,bad))
  reject('stale-query',lambda:s.advance(handle,before,operation,objective,answer))
  reject('hidden-refinement',lambda:s.advance(handle,before,{'kind':'append-fine','normal':row,'upper':upper},objective,fresh))
  reject('foreign-handle',lambda:s.advance('foreign',before,operation,objective,fresh))
  reject('wrong-objective',lambda:s.advance(handle,before,operation,[0]*d,fresh))
  advanced=s.advance(handle,before,operation,objective,fresh);new=advanced['handle']
  reject('stale-handle',lambda:s.fine_lift(handle,point))
  s.fine_lift(new,point);reject('section-is-not-archive',lambda:s.reexpose(new))
  # A later valid refinement excludes the cached optimum. Even if its local
  # source witness remains true, it cannot be returned for the successor.
  operation2={'kind':'append-public','normal':objective,'upper':str(Q(upper)-1)}
  refined2=refined.refine(objective,Q(upper)-1);fresh2=refined2.maximize(objective)
  final=s.advance(new,advanced['state'],operation2,objective,fresh2)
  reject('excluded-cached-point',lambda:s.fine_lift(final['handle'],point))
  # Separate policies: answer-only cannot lift; archive-only can reconstruct
  # the relation but does not gain the lift method.
  answer_session=Session();ar=answer_session.bootstrap(plan,case)
  reject('answer-only-lift',lambda:answer_session.fine_lift(ar['handle'],point))
  archived=Session();rr=archived.bootstrap(plan,case,retain_archive=True)
  assert archived.reexpose(rr['handle'])==plan
  reject('archive-only-lift',lambda:archived.fine_lift(rr['handle'],point))
  verify_answer(refined.descriptor(),list(map(str,objective)),fresh)
  verify_answer(refined2.descriptor(),list(map(str,objective)),fresh2)
  assert final['work']=={'migration_checks':1,'answer_checks':2,'fine_witness_checks':1,'fine_witness_hits':2}
  reports.append({'name':plan['name'],'final':final,'fresh_answers':[fresh,fresh2]})
 report={'passed':True,'owning_migrations':2,'rejections':rejected,'cases':reports,
 'scope':'Migration-gated point-witness checkpoint reuse. Not domain-section attachment or integration into Nima checkpoint backend. Full original migration evidence is required at bootstrap.'}
 (OUT/'migration-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'owning_migrations':2,'rejections':len(rejected),'per_session_work':reports[0]['final']['work']},indent=2))
if __name__=='__main__':main()
