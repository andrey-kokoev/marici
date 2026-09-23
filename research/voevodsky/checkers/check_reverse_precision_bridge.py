"""Reverse full-source proof translation on the exact translated pinned subfamily.
No producer or optimization backend imported. Validate input before transport.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,gzip
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_two_free_schema_bridge import expected_translation
from verify_schema_relative_tail_lp import check
from verify_two_free_tail_queries import verify,digest,combination,reconstruct

def reverse_one(origin,proof,sign):
 target=expected_translation(origin);m=origin['m'];free=origin['free'];pins=dict((j,Q(h)) for j,h in origin['pins'])
 objective=['0']*(m+2);objective[2+free[0]]=str(sign)
 check(target,{'kind':'maximize','objective':objective},proof)
 terms={};slack=Q(0)
 for index,value in proof['weights']:
  w=Q(value)
  if index<2*m:
   j=index//2;upper=index%2==0
   if j in pins:
    slack+=w*((100+2*j)-pins[j] if upper else pins[j]);continue
   k=2*free.index(j)+(1 if upper else 0)
  elif index<2*m+2*len(pins):continue # pin equalities become 0<=0
  else:k=4+index-(2*m+2*len(pins))
  terms[k]=terms.get(k,Q(0))+w
 terms=[[k,str(w)] for k,w in sorted(terms.items()) if w]
 n,b=combination(reconstruct(origin),terms)
 if proof['status']=='EMPTY':
  assert n==(0,0) and b<0
  return {'farkas':terms,'discarded_slack':str(slack)}
 assert slack==0 # tight feasible optimum cannot use positive constant slack
 point=[proof['x'][j] for j in free]
 assert n==(sign,0) and b==Q(proof['value'])
 return {'point':point,'value':proof['value'],'dual':terms,'discarded_slack':str(slack)}
def reverse_pair(origin,query,proofs):
 low,high=[reverse_one(origin,p,s) for p,s in zip(proofs,(-1,1))]
 if 'farkas' in low:
  assert 'farkas' in high;result={'status':'INCONSISTENT','farkas':low['farkas']}
 else:
  assert 'farkas' not in high
  for p in (low,high):p.pop('discarded_slack')
  lo,hi=-Q(low['value']),Q(high['value']);h=Q(query['threshold'])
  result={'status':'FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED',
   'interval':[str(lo),str(hi)],'minimum':low,'maximum':high}
 sd=digest(origin)
 packet={'schema':'two-free-tail-certificate-v1','state':origin,'query':query,'state_digest':sd,
 'query_digest':digest({'state_digest':sd,'query':query}),'result':result}
 verify(origin,query,packet);return packet

def main():
 requests=json.loads((N/'two-free-tail-query-contract.json').read_text())['requests']
 raw=(N/'two-free-schema-bridge-packet.json.gz').read_bytes();inputs=json.loads(gzip.decompress(raw))
 outputs={};costs=[]
 enc=lambda x:len(json.dumps(x,separators=(',',':')).encode())
 for name,entry in inputs.items():
  req=requests[name];outputs[name]={}
  for route in ('transported','mixed'):
   proofs=entry['general'] if route=='transported' else [p['certificate'] if p['status']=='VERIFIED' else entry['general'][i] for i,p in enumerate(entry['simplex'])]
   packet=reverse_pair(req['state'],req['query'],proofs);outputs[name][route]=packet
   costs.append({'name':name,'route':route,'input_pair_bytes':enc(proofs),'output_packet_bytes':enc(packet),
    'input_nonzeros':sum(len(p['weights']) for p in proofs),
    'output_nonzeros':len(packet['result']['farkas']) if packet['result']['status']=='INCONSISTENT' else sum(len(packet['result'][side]['dual']) for side in ('minimum','maximum'))})
 report={'outputs':outputs,'costs':costs,'input_path':'research/nima/results/two-free-schema-bridge-packet.json.gz',
 'scope':'Translated pinned states only; proof transport without optimization. Mixed route uses verified simplex proposals where present, transported fallback otherwise.'}
 (OUT/'reverse-precision-bridge.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'cases':len(outputs),'reconstructed_packets':len(costs),'solver_calls':0,
 'aggregate_input_pair_bytes':sum(c['input_pair_bytes'] for c in costs),'aggregate_output_bytes':sum(c['output_packet_bytes'] for c in costs)},indent=2))
if __name__=='__main__':main()
