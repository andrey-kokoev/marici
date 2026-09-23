"""Verify simplex packets without importing SymPy or the proposal backend."""
from pathlib import Path
import json,copy
from fractions import Fraction as Q
from verify_schema_relative_tail_lp import expected,check
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 p=json.loads((OUT/'simplex-schema-tail.json').read_text());contexts=list(expected((3,4,8,16)))
 assert p['m_values']==[3,4,8,16] and len(p['packets'])==len(contexts)==44
 for k,((s,q),packet) in enumerate(zip(contexts,p['packets'])):
  check(s,q,packet)
  assert (packet['status']=='EMPTY')==(k%11 in (6,7,10))
 for start in range(0,44,11):
  for i in (0,1):assert Q(p['packets'][start+i]['value'])==Q(p['packets'][start+i+2]['value'])
 # Compare the reference backend where it was actually run.
 old=json.loads((OUT/'schema-relative-tail-lp.json').read_text())['packets']
 for a,b in zip(old,p['packets']):
  assert a['state']==b['state'] and a['query']==b['query'] and a['status']==b['status']
  if 'value' in a:assert Q(a['value'])==Q(b['value'])
 attacks=0
 for field in ('state','query','x','weights'):
  b=copy.deepcopy(p['packets'][4]);s,q=contexts[4]
  if field=='state':b['state']['audits'].reverse()
  elif field=='query':b['query']['objective'][0]='2'
  elif field=='x':b['x'][0]='-1'
  else:b['weights'][0][1]=str(Q(b['weights'][0][1])+1)
  try:check(s,q,b)
  except AssertionError:attacks+=1
  else:raise AssertionError('corruption accepted')
 result={'passed':True,'certificates':44,'reference_comparisons':len(old),'attacks_rejected':attacks,'m_values':[3,4,8,16]}
 (OUT/'simplex-schema-tail-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
