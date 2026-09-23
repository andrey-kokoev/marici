"""Ambiguity is not resolution; archives must retain event-bound identity."""
from pathlib import Path
from copy import deepcopy
import json
from authority_aware_upgrade import ArchiveAuthority,UpgradeSession
from approximate_section_checkpoint import initial
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';OUT=ROOT/'research/voevodsky/results'
def main():
 request={'n':18,'eta':'1/100'};expected=initial(request)
 section=next(p for p in json.loads((N/'scalar-envelope-band-packets.json').read_text()) if p['request']==request)
 obstruction=json.loads((OUT/'fine-refinement-obstruction.json').read_text())['obstruction_packet']
 operation={'kind':'fine-upper-point-admission','h_upper':'1/2','point':['1','1']}
 authority=ArchiveAuthority();sessions={};receipts={};rejected=[]
 for history in ('A','B'):
  sessions[history]=UpgradeSession(authority)
  receipts[history]=sessions[history].retire(expected,section,owner_history=history)
 assert receipts['A']['state']==receipts['B']['state']
 a,b=sessions['A'],sessions['B'];ra,rb=receipts['A'],receipts['B']
 # Same selected source answer in both histories cannot identify the original.
 assert a.lift(ra['handle'],['1','1'])['source_lift']==b.lift(rb['handle'],['1','1'])['source_lift']
 def reject(name,session,call):
  before=session.receipt()
  try:call()
  except (AssertionError,ValueError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
  assert session.receipt()==before # failed request must not publish or poison
 ambiguous=[]
 for name,s in sessions.items():
  r=receipts[name];h=r['handle']
  old=s.receipt();ambiguous.append(s.request_upgrade(h,expected,operation,obstruction));assert s.receipt()==old
  for label,fake in (('self-asserted-history',{'history':name}),('family-only-archive',{'histories':['A','B']}),('chosen-lift',s.lift(h,['1','1'])['source_lift']),('forged-reference','not-issued')):
   reject(label,s,lambda:s.resolve(h,expected,operation,obstruction,fake))
  other=receipts['B' if name=='A' else 'A']['archive_reference']
  reject('foreign-event',s,lambda:s.resolve(h,expected,operation,obstruction,other))
  bad=deepcopy(obstruction);bad['A_combined_upper']='0'
  reject('false-obstruction',s,lambda:s.resolve(h,expected,operation,bad,r['archive_reference']))
 resolutions=[]
 for name,s in sessions.items():
  r=receipts[name];answer=s.resolve(r['handle'],expected,operation,obstruction,r['archive_reference'])
  assert answer['resolution']['admits_point']==(name=='B')
  reject('stale-head',s,lambda:s.resolve(r['handle'],expected,operation,obstruction,r['archive_reference']))
  resolutions.append(answer['resolution'])
 # Irreversible forgetting: no identity entry was created; another event's
 # true archive cannot be repurposed to restore this one.
 forgotten=UpgradeSession(authority);fr=forgotten.retire(expected,section,owner_history='A',retain_identity=False)
 assert fr['archive_reference'] is None
 assert forgotten.request_upgrade(fr['handle'],expected,operation,obstruction)['status']=='AMBIGUOUS'
 reject('forgotten-identity',forgotten,lambda:forgotten.resolve(fr['handle'],expected,operation,obstruction,ra['archive_reference']))
 revoked=UpgradeSession(authority);rr=revoked.retire(expected,section,owner_history='B')
 authority.revoke(rr['archive_reference'])
 reject('revoked-reference',revoked,lambda:revoked.resolve(rr['handle'],expected,operation,obstruction,rr['archive_reference']))
 report={'passed':True,'ambiguous_requests':ambiguous,'resolved_requests':resolutions,'rejections':rejected,
 'authority_encoded_bytes':authority.encoded_bytes(),
 'accounting':'Two original-history selectors retained outside equal live semantic descriptors. Event identifiers and vault references also carry authority; they are not free shared state.',
 'scope':'Fixed-family exact admission upgrade only. Owner identity admitted before retirement; no observation authentication, general migration binding, or actual fine-state replacement.'}
 (OUT/'authority-aware-upgrade.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'resolutions':[(r['history'],r['admits_point']) for r in resolutions],'rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
