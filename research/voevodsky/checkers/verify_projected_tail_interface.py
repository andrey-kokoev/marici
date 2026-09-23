"""Independent public/internal statement binding and source arithmetic replay."""
from pathlib import Path
from copy import deepcopy
import json
from verify_schema_relative_tail_lp import check
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def verify(state,public,query,packet):
 assert packet['expected_internal_state']==state and packet['public_audits']==public and packet['public_query']==query
 assert len(query['objective'])==2+len(public) and set(public)<=set(state['audits'])
 a=query['objective'];translated=a[:2]+[a[2+public.index(j)] if j in public else '0' for j in state['audits']]
 check(state,{'kind':'maximize','objective':translated},packet['internal_certificate'])
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'projected-tail-interface.json').read_text())['packets'];assert len(packets)==4
 rejected=0
 for m,p in zip((3,4,8,16),packets):
  s={'source':'tail-box-100+2j-128^-j-v1','m':m,'audits':[0],
   'frames':[{'a':['1','0','-1'],'b':'0'},{'a':['-1','0','1'],'b':'0'},{'a':['0','0','1'],'b':'1'}]}
  q={'kind':'maximize','objective':['1','0']}
  verify(s,[],q,p['hidden']);assert p['hidden']['internal_certificate']['value']=='1'
  reduced=deepcopy(s);reduced['frames'].pop()
  check(reduced,{'kind':'maximize','objective':['1','0','0']},p['dropped_frame_control'])
  assert p['dropped_frame_control']['value']=='100'
  for attack in ('drop','expose','query'):
   bad=deepcopy(p['hidden'])
   if attack=='drop':bad['internal_certificate']=p['dropped_frame_control']
   elif attack=='expose':bad['public_audits']=[0]
   else:bad['public_query']['objective']=['0','1']
   try:verify(s,[],q,bad)
   except AssertionError:rejected+=1
   else:raise AssertionError('bad projection envelope accepted')
 result={'passed':True,'projection_cases':4,'arithmetic_certificates':8,'binding_attacks_rejected':rejected,
 'scope':'Public-query restriction with full internal evidence; no storage reclamation or confidentiality claim.'}
 (OUT/'projected-tail-interface-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
