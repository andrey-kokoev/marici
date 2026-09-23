"""Independent acceptance of reverse-translated packets; no translator import."""
from pathlib import Path
import sys,json,gzip,copy
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_two_free_tail_queries import verify
from verify_two_free_schema_bridge import expected_translation
from verify_schema_relative_tail_lp import check

def main():
 if not __debug__:raise RuntimeError('Assertions required')
 requests=json.loads((N/'two-free-tail-query-contract.json').read_text())['requests']
 inputs=json.loads(gzip.decompress((N/'two-free-schema-bridge-packet.json.gz').read_bytes()))
 output=json.loads((OUT/'reverse-precision-bridge.json').read_text());assert set(output['outputs'])==set(inputs)
 count=0
 for name,routes in output['outputs'].items():
  req=requests[name];state=req['state'];target=expected_translation(state);assert set(routes)=={'transported','mixed'}
  for route,packet in routes.items():
   status=verify(state,req['query'],packet);assert status==req['status']
   entry=inputs[name];proofs=entry['general'] if route=='transported' else [p['certificate'] if p['status']=='VERIFIED' else entry['general'][i] for i,p in enumerate(entry['simplex'])]
   for sign,p in zip((-1,1),proofs):
    a=['0']*(state['m']+2);a[2+state['free'][0]]=str(sign);check(target,{'kind':'maximize','objective':a},p)
   if status=='INCONSISTENT':assert all(p['status']=='EMPTY' for p in proofs)
   else:
    assert list(map(Q,packet['result']['interval']))==[-Q(proofs[0]['value']),Q(proofs[1]['value'])]
   count+=1
 # Acceptance checks do not rely on provenance or producer arithmetic alone.
 name=next(n for n,p in output['outputs'].items() if p['transported']['result']['status']!='INCONSISTENT')
 req=requests[name];good=output['outputs'][name]['transported'];rejected=0
 for mode in ('history','threshold','dual','point'):
  p=copy.deepcopy(good)
  if mode=='history':p['state']['source_binding']='foreign'
  elif mode=='threshold':p['query']['threshold']=str(Q(p['query']['threshold'])+1)
  elif mode=='dual':p['result']['maximum']['dual']=[]
  else:p['result']['maximum']['point']=['-1','-1']
  try:verify(req['state'],req['query'],p)
  except AssertionError:rejected+=1
  else:raise AssertionError('mutation accepted')
 result={'passed':True,'reverse_packets':count,'independent_state_query_checks':count,'mutations_rejected':rejected,
 'scope':'Both input and output proofs independently validated; no solver or reverse translator imported.'}
 (OUT/'reverse-precision-bridge-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
