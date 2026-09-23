"""Executable fixed-query comparison with an independently checked destination."""
import json
from pathlib import Path
from moment_comparison_transport import transport,replay,ComparisonSession
from verify_moment_fine_rebase import from_answer,verify_rebase,data
from moment_fine_rebase import propose,solve,compress
from verify_active_cap_moment_master import verify
from fractions import Fraction as Q

fixture=json.loads((Path(__file__).resolve().parent.parent/'results/moment-fine-rebase.json').read_text())
c=fixture['coupled'];base=c['state'];first=c['operation'];second={'block':0,'tail':None,'head':0,'upper':'1/2'}
head=from_answer(base,c['answer'],c['compact']);head=verify_rebase(head,first,c['candidate'])
packet=propose(head,second);head=verify_rebase(head,second,packet)
other=transport(head,base,[first,second],[second,first]);assert other['state']!=head['state']
assert other['result']==head['result'] and other['columns']==head['columns']
# A genuinely fresh semantic replay at the destination, not the transport's
# own checker, tests both the changed row order and an active moment frame.
cold=solve(other['state']);verify(other['state'],cold)
assert cold['status']==other['result']['status']
if cold['status']=='OPTIMUM':assert Q(cold['value'])==Q(other['result']['value'])
assert transport(other,base,[second,first],[first,second])==head
for altered in ([second], [second,{'block':1,'tail':None,'head':5,'upper':'14'}]):
 try:transport(head,base,[first,second],altered)
 except AssertionError:pass
 else:raise AssertionError('false comparison admitted')
# Opaque owner grant binds the event, common base and BOTH paths. No packet
# can manufacture its own approval; revocation is checked on every transfer.
class Owner:
 def __init__(self):self.records={}
 def issue(self,event,base,source,target):
  token=object();self.records[token]=(event,base,source,target);return token
 def check(self,event,base,source,target,token):return self.records.get(token)==(event,base,source,target)
owner=Owner();session=ComparisonSession(head,base,[first,second],owner.check)
old=session.handle;target=[second,first];grant=owner.issue(session.event,base,[first,second],target)
def refuse(fn):
 before=session.snapshot(session.handle)
 try:fn()
 except AssertionError:pass
 else:raise AssertionError('unauthorized comparison accepted')
 assert session.snapshot(session.handle)==before
refuse(lambda:session.compare(old,[first,second],target,object()))
refuse(lambda:session.compare(old,[second,first],target,grant))
new=session.compare(old,[first,second],target,grant);assert session.snapshot(new)==other
refuse(lambda:session.compare(old,[first,second],target,grant))
revoked=owner.issue(session.event,base,target,[first,second]);del owner.records[revoked]
refuse(lambda:session.compare(new,target,[first,second],revoked))
last=session.detach(new);assert session.snapshot(last)==other
refuse(lambda:session.compare(last,target,[first,second],owner.issue(session.event,base,target,[first,second])))
print('PASS: exact comparison transport, reindexed flows, cold destination, owner/stale/revocation refusals and detached replay')
