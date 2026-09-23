"""Independent replay of migration, retired statement and fine witness.
Does not import the retirement wrapper or any optimizer. Expected plans and
refinement policy come from the owning contract and this frozen workload.
"""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import sys,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
from verify_audit_elimination import verify_case,verify_lp,source,dec

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def binding(plan,case):return hashlib.sha256(canonical({'expected':plan,'case':case}).encode()).hexdigest()
def expected_statement(plan,case):
 d=2+len(case['runtime']['audits']);objective=[str(int(i==0)) for i in range(d)]
 # The workload adds U<=the previously certified migration-query optimum.
 # It is independently available in the owning verified packet, not read
 # from the lifecycle answer under verification.
 upper=case['queries'][0]['value']
 state={'runtime':case['runtime'],'migration_binding':binding(plan,case),
  'public_frames':[{'normal':objective,'upper':upper}],
  'capabilities':{'lift':False,'reexpose':False}}
 return state,objective

def verify_record(plan,case,record):
 verify_case(plan,case)
 assert record['name']==plan['name']
 expected,objective=expected_statement(plan,case);answer=record['fresh_answer']
 assert answer['state']==expected and answer['objective']==objective
 runtime=expected['runtime'];frames=list(map(dec,runtime['frames']))+list(map(dec,expected['public_frames']))
 verify_lp(runtime['m'],runtime['audits'],frames,tuple(map(Q,objective)),answer['proof'])
 assert answer['proof']['status']=='OPTIMUM'
 # An old-compatible lift is stronger than a generic coarse-source lift.
 # Validate it against the independently expected ORIGINAL fine evidence.
 t=tuple(map(Q,record['fine_lift']));_,_,observe,caps=source(plan['m'],plan['audits'])
 assert len(t)==plan['m'] and all(0<=v<=cap for v,cap in zip(t,caps))
 fine=observe(t);k=2+plan['audits'].index(plan['retire']);public=fine[:k]+fine[k+1:]
 assert public==tuple(map(Q,answer['proof']['point']))
 assert all(sum(a*x for a,x in zip(n,fine))<=b for n,b in map(dec,plan['frames']))
 assert all(sum(a*x for a,x in zip(n,public))<=b for n,b in frames)
 # The archived restoration rule preserves old rows and pulls back all new
 # public rows with zero coefficient on the retired coordinate. Validate
 # the resulting witness obligations without trusting a wrapper method.
 for n,b in map(dec,expected['public_frames']):
  translated=n[:k]+(Q(0),)+n[k:]
  assert sum(a*x for a,x in zip(translated,fine))<=b

def main():
 if not __debug__:raise RuntimeError('Assertions required')
 c=json.loads((G/'audit-elimination-contract.json').read_text())
 owning=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))
 result=json.loads((OUT/'checked-retirement-lifecycle.json').read_text());assert len(result['cases'])==2
 contexts=[(c['plans'][i],owning['compactions'][i]) for i in (0,2)]
 for (plan,case),record in zip(contexts,result['cases']):verify_record(plan,case,record)
 plan,case=contexts[0];record=result['cases'][0];rejected=[]
 for mode in ('migration','history','capabilities','query','fine_lift','schema'):
  bad=deepcopy(record);answer=bad['fresh_answer']
  if mode=='migration':answer['state']['migration_binding']='foreign'
  elif mode=='history':answer['state']['public_frames']=[]
  elif mode=='capabilities':answer['state']['capabilities']['reexpose']=True
  elif mode=='query':answer['objective'][0]='2'
  elif mode=='fine_lift':bad['fine_lift'][0]='-1'
  else:answer['state']['runtime']['audits']=[0]
  try:verify_record(plan,case,bad)
  except (AssertionError,IndexError,KeyError,ValueError):rejected.append(mode)
  else:raise AssertionError('lifecycle mutation accepted')
 report={'passed':True,'owning_lifecycles':2,'mutations_rejected':rejected,
 'scope':'Independent migration/statement/answer/fine-lift replay. Runtime refusal behavior remains producer-tested, not proved by packet arithmetic.'}
 (OUT/'checked-retirement-lifecycle-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
