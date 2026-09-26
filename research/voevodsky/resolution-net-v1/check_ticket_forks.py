from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from pathlib import Path
import hashlib,json
from reference import Package,Admission,Rule
from pending import Hole,Branch
from open_net import OpenNet
from ticket_authority_model import TicketAuthority
p=Package('P');e=Admission(p,'registered-proof');initial=OpenNet(Hole('input',p))
# Counterexample: local receipt checks accept the same ticket in two forks.
left=deepcopy(initial);right=deepcopy(initial)
for net in (left,right):
 net.arrive('input','shared',e)
 while net.active():net.rewrite(net.active()[0])
 if not net.released():raise RuntimeError('fork witness failed')
if left.receipts!=right.receipts:raise RuntimeError('expected identical consumption evidence')
serial=[]
for order in (('left','right'),('right','left')):
 authority=TicketAuthority({'shared':e});authority.register('left',initial);authority.fork('left','right');success=[]
 for branch in order:
  try:authority.accept(branch,0,'input','shared');success.append(branch)
  except ValueError:pass
 if success!=[order[0]] or len(authority.spent())!=1:raise RuntimeError('serial duplicate consumption')
 serial.append(success[0])
# Real threads racing through the same model authority.
authority=TicketAuthority({'shared':e});authority.register('left',initial);authority.fork('left','right');gate=Barrier(2)
def race(name):
 gate.wait()
 try:authority.accept(name,0,'input','shared');return True
 except ValueError:return False
with ThreadPoolExecutor(max_workers=2) as pool:outcomes=list(pool.map(race,('left','right')))
if sum(outcomes)!=1:raise RuntimeError('race did not serialize')
# Invalid package/slot and unregistered ticket leave both ledgers unchanged.
authority=TicketAuthority({'good':e,'wrong':Admission(Package('Q'),'q')});authority.register('x',initial)
for slot,ticket in (('missing','good'),('input','wrong'),('input','unknown')):
 version,before=authority.snapshot('x');spent=authority.spent()
 try:authority.accept('x',version,slot,ticket)
 except ValueError:pass
 else:raise RuntimeError('bad request accepted')
 now,after=authority.snapshot('x')
 if now!=version or before.__dict__!=after.__dict__ or spent!=authority.spent():raise RuntimeError('failed request changed authority')
# CAS detects stale branch even when the next ticket is independent.
rule=Rule('join',(p,p),p,'v');two=OpenNet(Branch(rule,(Hole('a',p),Hole('b',p))))
authority=TicketAuthority({'t1':e,'t2':e});authority.register('x',two);authority.accept('x',0,'a','t1')
try:authority.accept('x',0,'b','t2')
except ValueError:pass
else:raise RuntimeError('stale request accepted')
if 't2' in authority.spent():raise RuntimeError('stale attempt spent ticket')
authority.accept('x',1,'b','t2')
if len(authority.spent())!=2:raise RuntimeError('independent tickets blocked')
# Crucial boundary: duplicating the authority realm restores the counterexample.
realms=[TicketAuthority({'shared':e}),TicketAuthority({'shared':e})]
for realm in realms:realm.register('x',initial);realm.accept('x',0,'input','shared')
root=Path(__file__).parent
report={'passed':True,'uncoordinated_forks_both_consume':True,'single_authority_serial_winners':serial,'same_authority_concurrent_successes':sum(outcomes),'atomic_invalid_requests':3,'stale_revision_rejected_without_spend':True,'independent_tickets_same_evidence_accepted':True,'separate_authority_realms_both_consume':True,'new_internal_net_primitives':0,'scope':'One single-process lock-protected authority model. Explicitly not distributed consensus, durable transactions, cryptographic authentication, fairness or enforcement against bypass/copying the authority.','source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('ticket_authority_model.py','check_ticket_forks.py','open_net.py')}}
(root/'results/ticket-forks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
