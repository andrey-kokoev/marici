"""Existential hiding: retain internal schema/evidence, restrict public queries."""
from copy import deepcopy
from pathlib import Path
import json
from check_simplex_schema_tail import certify
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def translate(state,public,query):
 internal=state['audits'];assert set(public)<=set(internal)
 if query['kind']!='maximize':raise ValueError('UNSUPPORTED_QUERY')
 a=query['objective']
 if len(a)!=2+len(public):raise ValueError('UNDECLARED_OBSERVABLE')
 return {'kind':'maximize','objective':a[:2]+[a[2+public.index(j)] if j in public else '0' for j in internal]}
def hidden_certificate(state,public,query):
 internal_query=translate(state,public,query)
 return {'expected_internal_state':deepcopy(state),'public_audits':list(public),'public_query':deepcopy(query),
         'internal_certificate':certify(state,internal_query)}
def main():
 packets=[]
 for m in (3,4,8,16):
  # U=x0 makes all other nonnegative atom masses zero. The x0 audit bound
  # therefore constrains public U even when x0 is no longer public.
  state={'source':'tail-box-100+2j-128^-j-v1','m':m,'audits':[0],
   'frames':[{'a':['1','0','-1'],'b':'0'},{'a':['-1','0','1'],'b':'0'},{'a':['0','0','1'],'b':'1'}]}
  query={'kind':'maximize','objective':['1','0']}
  packet=hidden_certificate(state,[],query)
  assert packet['internal_certificate']['value']=='1'
  # Compare before retirement in the old public language.
  before=certify(state,{'kind':'maximize','objective':['1','0','0']})
  assert before['value']==packet['internal_certificate']['value']
  try:hidden_certificate(state,[],{'kind':'maximize','objective':['0','0','1']})
  except ValueError:pass
  else:raise AssertionError('retired coordinate query accepted')
  # Removing the former audit bound admits a much larger U: this is a
  # deliberate negative control, never used as the projected state.
  dropped=deepcopy(state);dropped['frames'].pop()
  bad=certify(dropped,{'kind':'maximize','objective':['1','0','0']})
  assert bad['value']=='100'
  packets.append({'hidden':packet,'dropped_frame_control':bad})
 (OUT/'projected-tail-interface.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps({'passed':True,'cases':len(packets),'hidden_optimum':1,'dropped_evidence_optimum':100}))
if __name__=='__main__':main()
