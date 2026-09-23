"""Migration lifecycle against real owning proof packets."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,copy
from checked_retirement_interface import migrate,verify_answer,source,dec,freeze
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 contract=json.loads((G/'audit-elimination-contract.json').read_text());packets=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))
 reports=[];rejected=0
 for idx in (0,2):
  plan=contract['plans'][idx];case=packets['compactions'][idx]
  answer=migrate(plan,case);lift=migrate(plan,case,retain_lift=True);archive=migrate(plan,case,retain_archive=True)
  d=2+len(case['runtime']['audits']);objective=[1]+[0]*(d-1)
  old=answer.maximize(objective);assert old['proof']['status']=='OPTIMUM'
  optimum=Q(old['proof']['value']);new=answer.refine(objective,optimum)
  expected=new.descriptor();fresh=new.maximize(objective);verify_answer(expected,list(map(str,objective)),fresh)
  try:verify_answer(expected,list(map(str,objective)),old)
  except AssertionError:rejected+=1
  else:raise AssertionError('stale answer accepted')
  point=tuple(map(Q,fresh['proof']['point']));t=lift.refine(objective,optimum).fine_lift(point)
  _,_,observe,caps=source(plan['m'],plan['audits']);joint=observe(t)
  assert all(0<=x<=b for x,b in zip(t,caps)) and all(sum(a*x for a,x in zip(n,joint))<=b for n,b in map(dec,plan['frames']))
  restored=archive.refine(objective,optimum).reexpose();assert len(restored['frames'])==len(plan['frames'])+1
  assert restored['frames'][:-1]==plan['frames']
  for state,method,arg in [(answer,'fine_lift',point),(lift,'reexpose',None),(answer,'reexpose',None)]:
   try:getattr(state,method)(arg) if arg is not None else getattr(state,method)()
   except PermissionError:rejected+=1
   else:raise AssertionError('capability escalation')
  try:answer.refine([0]*(d+1),0)
  except ValueError:rejected+=1
  else:raise AssertionError('nonpublic frame accepted')
  # Empty later public refinement must not be forgotten by lift or archive.
  negative=[0]*d
  try:lift.refine(negative,-1).fine_lift(point)
  except ValueError:rejected+=1
  else:raise AssertionError('empty state lifted')
  assert archive.refine(negative,-1).reexpose()['frames'][-1]['upper']=='-1'
  bad=copy.deepcopy(case);bad['runtime']['frames'].pop()
  try:migrate(plan,bad)
  except AssertionError:rejected+=1
  else:raise AssertionError('unchecked migration accepted')
  reports.append({'name':plan['name'],'fresh_answer':fresh,'fine_lift':list(map(str,t)),
   'bytes':{'live_answer_state':len(freeze(answer.descriptor()).encode()),
    'optional_lift_context':len(lift.lift_json.encode()),'optional_archive':len(archive.archive_json.encode()),
    'migration_packet':len(freeze(case).encode())}})
 result={'passed':True,'owning_migrations':len(reports),'rejected_lifecycle_violations':rejected,'cases':reports,
 'scope':'Owning projection checker gates factory construction. Research wrapper; direct dataclass construction is not a security boundary. Lift context retains fine rows and is not information-theoretically weaker than an archive.'}
 (OUT/'checked-retirement-lifecycle.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
