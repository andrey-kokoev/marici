"""Semantic replay without importing the transport-session implementation.
An exported root does not authenticate live vault authority.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
from continuation_coherence import verify_path,compare,digest
from verify_fine_successor import expected_archive
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def check_answer(state,point,answer):
 p=tuple(map(Q,point));lows=[];highs=[]
 for row in state['fine_rows']:
  a,b,c=map(Q,row['normal']);rhs=Q(row['upper'])-a*p[0]-b*p[1]
  if c<0:lows.append(rhs/c)
  elif c>0:highs.append(rhs/c)
  else:assert rhs>=0
 lo,hi=max(lows),min(highs);assert answer['interval']==list(map(str,(lo,hi)))
 if lo>hi:assert answer=={'admitted':False,'interval':list(map(str,(lo,hi)))};return
 assert answer['admitted'] is True;t=tuple(map(Q,answer['source_lift']));assert len(t)==4
 assert all(0<=v<=100+2*j for j,v in enumerate(t));D=Q(1,128**4);h=(t[0]-50)/D
 assert t[1]==51 and lo<=h<=hi
 r=[Q(1,128**j) for j in range(4)];assert sum(t)==206+D*p[0]
 assert sum(a*b for a,b in zip(t,r))==sum(a*b for a,b in zip((50,51,52,53),r))+D*p[1]
 assert all(sum(a*b for a,b in zip(map(Q,row['normal']),(*p,h)))<=Q(row['upper']) for row in state['fine_rows'])
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 report=json.loads((OUT/'evidence-transport-coherence.json').read_text());assert len(report['cases'])==4
 assert {(c['history'],tuple(c['point'])) for c in report['cases']}=={(h,p) for h in ('A','B') for p in (('1','1'),('1/18','1/324'))}
 checked=0
 for case in report['cases']:
  archive=expected_archive(18,case['history']);binding=case['binding'];paths=case['paths'];batches=case['batches']
  states={name:verify_path(archive,binding,batches[name],path) for name,path in paths.items()}
  assert states['P']==states['Q']==states['R']
  assert case['composition_descriptor']['path_tip']==paths['R']['tip']
  assert case['loop_descriptor']==case['initial']['staged']['state']
  assert [(s['session'],s['destination']) for s in case['steps']]==[('direct','R'),('staged','Q'),('staged','R'),('staged','P'),('staged','P'),('staged','Q')]
  receipts=[(r,'P') for r in case['initial'].values()]+[(s['receipt'],s['destination']) for s in case['steps']]
  answers=[]
  for receipt,destination in receipts:
   desc=receipt['state'];assert desc['binding']==binding and desc['point']==case['point']
   assert desc['policy']=='exact-point-only/no-archive-reexposure/v1'
   assert desc['path_tip']==paths[destination]['tip'] and desc['semantic_digest']==digest(states[destination])
   check_answer(states[destination],case['point'],receipt['answer']);answers.append(receipt['answer']);checked+=1
  assert all(a==answers[0] for a in answers)
  assert case['steps'][0]['receipt']['state']==case['steps'][2]['receipt']['state']==case['composition_descriptor']
  expected=compare(archive,binding,batches['Q'],paths['Q'],batches['R'],paths['R'])
  assert case['mathematical_comparison_after_revocation']==expected
 result={'passed':True,'cases':4,'point_answers_replayed':checked,
 'scope':'Independent point arithmetic and path-composition replay. Live authority, trap behavior and revocation remain separately tested in process; exported roots are not attestations.'}
 (OUT/'evidence-transport-coherence-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
