"""Nima ambiguity -> owner archive -> atomic exact fine successor."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as Q
import json
from atomic_fine_restoration import Session,Vault
from verify_fine_successor import expected_archive,verify
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';OUT=ROOT/'research/voevodsky/results'
def main():
 section=next(p for p in json.loads((N/'scalar-envelope-band-packets.json').read_text()) if p['request']=={'n':18,'eta':'1/100'})
 expected={'family':'owning-m4-moment-curve-two-history-v1','n':18,'eta':'1/100'}
 proof=json.loads((OUT/'fine-refinement-obstruction.json').read_text())['obstruction_packet']
 op={'kind':'append-fine-upper-then-exact-point-admission','h_upper':'1/2'}
 vault=Vault();services={};boots={};ambiguities={};candidates={};rejected=[];reports=[]
 for history in ('A','B',None):
  s=Session(vault);r=s.retire(expected,section,owner_history=history)
  a=s.request_fine(r['handle'],r['state'],op,['1','1'],proof)
  assert a['actual_history'] is None and a['selected_answer'] is None
  services[history]=s;boots[history]=r;ambiguities[history]=a
  archive=expected_archive(18,history or 'A')
  candidates[history]={**archive,'retirement_event':r['retirement_event'],'parent_request_digest':a['request_digest'],
   'fine_rows':archive['fine_rows']+[{'normal':['0','0','1'],'upper':'1/2'}],
   'capabilities':['exact-point-admission','exact-fine-lift'],'archive_reexposure':False}
 def reject(name,s,call):
  before=s.receipt()
  try:call()
  except (ValueError,AssertionError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
  assert s.receipt()==before
 for history in ('A','B'):
  s=services[history];r=boots[history];a=ambiguities[history];candidate=candidates[history];h=r['handle'];state=r['state'];token=r['archive_reference']
  def restore(c=candidate,t=token,rd=a['request_digest']):return s.restore(h,state,rd,t,c)
  bad=deepcopy(candidate);bad['fine_rows'].pop()
  reject('missing-new-evidence',s,lambda:restore(bad))
  bad=deepcopy(candidate);bad['capabilities'].append('archive')
  reject('policy-escalation',s,lambda:restore(bad))
  reject('foreign-archive',s,lambda:restore(t=boots['B' if history=='A' else 'A']['archive_reference']))
  reject('self-asserted-history',s,lambda:restore(t={'history':history}))
  reject('stale-operation',s,lambda:restore(rd='old-request'))
  # Failed restore keeps predecessor ambiguity service usable.
  assert s.request_fine(h,state,op,['1','1'],proof)==a
  restored=restore();new=restored['handle'];fine=restored['state']
  verify(expected_archive(18,history),r['retirement_event'],a,fine)
  answer=s.query_point(new,fine,['1','1']);assert answer['admitted']==(history=='B')
  point=['1/18','1/324'];low=s.query_point(new,fine,point);assert low['admitted']
  for p,response in ((['1','1'],answer),(point,low)):
   if not response['admitted']:
    lo,hi=map(Q,response['interval']);assert lo>hi;continue
   t=tuple(map(Q,response['source_lift']));d=Q(1,128**4);weights=[Q(1,128**j) for j in range(4)]
   assert all(0<=v<=100+2*j for j,v in enumerate(t)) and t[1]==51
   assert sum(t)==206+d*Q(p[0])
   assert sum(x*y for x,y in zip(t,weights))==sum(x*y for x,y in zip((50,51,52,53),weights))+d*Q(p[1])
   scalar=(t[0]-50)/d;assert scalar<=Q(1,2)
   assert all(sum(x*y for x,y in zip(map(Q,row['normal']),(Q(p[0]),Q(p[1]),scalar)))<=Q(row['upper']) for row in fine['fine_rows'])
  reject('stale-coarse-handle',s,lambda:s.query_point(h,state,point))
  reject('old-common-request-path',s,lambda:s.request_fine(new,fine,op,['1','1'],proof))
  reject('archive-reexposure',s,lambda:s.reexpose(new,fine))
  reports.append({'history':history,'ambiguity':a,'successor':restored,'distinguishing_point_answer':answer,'retained_point_answer':low})
 s=services[None];r=boots[None];a=ambiguities[None]
 reject('authority-free-selection',s,lambda:s.restore(r['handle'],r['state'],a['request_digest'],None,candidates[None]))
 # Real token revoked before any successor publication.
 revoked=Session(vault);rr=revoked.retire(expected,section,owner_history='A');aa=revoked.request_fine(rr['handle'],rr['state'],op,['1','1'],proof)
 vault.revoke(rr['archive_reference'])
 reject('revoked-archive',revoked,lambda:revoked.restore(rr['handle'],rr['state'],aa['request_digest'],rr['archive_reference'],candidates['A']))
 result={'passed':True,'restorations':reports,'rejections':rejected,'archive_vault_encoded_bytes':vault.bytes(),
 'scope':'Nima verified ambiguity consumed by an explicitly trusted pre-retirement archive authority; actual fixed-family fine-state replacement. No external provenance authentication or general projection migration.'}
 (OUT/'atomic-fine-restoration.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'restorations':2,'rejections':len(rejected),'A_endpoint_admitted':False,'B_endpoint_admitted':True},indent=2))
if __name__=='__main__':main()
