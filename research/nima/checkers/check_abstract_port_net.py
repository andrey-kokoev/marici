"""Theory-free tests: linear handles, local replacement and transactional refusal."""
from abstract_port_net import PortNet,Signature,Agent
from pathlib import Path
import json

class Opaque:
    def __deepcopy__(self,memo):raise AssertionError('core must not copy payload')
    def __add__(self,other):raise AssertionError('core must not perform arithmetic')

payloads={'handle-A':Opaque()}
signatures={'REQUEST':Signature('p'), 'EMIT':Signature('p',('out','ack')),
            'VALUE':Signature('p'),'OUT':Signature('p'),'ACK':Signature('p'),
            'CLEAN':Signature('p',('ack',)),'TICKET':Signature('p'),'DONE':Signature('p')}

def fixture():
    net=PortNet(signatures)
    request=net.add('REQUEST',('handle-A',));emit=net.add('EMIT')
    out=net.add('OUT');ack=net.add('ACK')
    net.link((request,'p'),(emit,'p'));net.link((emit,'out'),(out,'p'))
    net.link((emit,'ack'),(ack,'p'));net.validate()
    return net,request,emit,out,ack

def snapshot(net):return dict(net.nodes),dict(net.wires),net.serial
net,a,b,out,ack=fixture()
initial_object=payloads['handle-A']
# This host-defined protocol is a client of the core, not a built-in rule.
ids=net.replace((a,b),(Agent('VALUE',('handle-A',)),Agent('CLEAN'),Agent('TICKET')),
                (((1,'p'),(2,'p')),),{(b,'out'):(0,'p'),(b,'ack'):(1,'ack')})
assert net.nodes[net.wires[out,'p'][0]].kind=='VALUE'
assert net.nodes[net.wires[ack,'p'][0]].kind=='CLEAN'
assert payloads['handle-A'] is initial_object
value,clean,ticket=ids
net.replace((clean,ticket),(Agent('DONE'),),(),{(clean,'ack'):(0,'p')})
assert net.nodes[net.wires[ack,'p'][0]].kind=='DONE'
assert net.nodes[value].handles==('handle-A',)
# Boundary principal wires remain structural pairs; only a client rule table
# decides which of those pairs is executable.
assert len(net.principal_pairs())==2
refusals=[]
for name,replacements,internal,boundary in (
    ('lost handle',(Agent('VALUE'),Agent('DONE')),(),{(b,'out'):(0,'p'),(b,'ack'):(1,'p')}),
    ('duplicated handle',(Agent('VALUE',('handle-A',)),Agent('DONE',('handle-A',))),(),{(b,'out'):(0,'p'),(b,'ack'):(1,'p')}),
    ('invented handle',(Agent('VALUE',('handle-A','new')),Agent('DONE')),(),{(b,'out'):(0,'p'),(b,'ack'):(1,'p')}),
    ('omitted boundary',(Agent('VALUE',('handle-A',)),Agent('DONE')),(),{(b,'out'):(0,'p')}),
    ('late invalid wiring',(Agent('VALUE',('handle-A',)),Agent('DONE')),(),{(b,'out'):(0,'p'),(b,'ack'):(1,'missing')}),
    ('unwired new port',(Agent('VALUE',('handle-A',)),Agent('CLEAN')),(),{(b,'out'):(0,'p'),(b,'ack'):(1,'p')})):
    bad,a,b,_,_=fixture();before=snapshot(bad)
    try:bad.replace((a,b),replacements,internal,boundary)
    except ValueError:pass
    else:raise AssertionError(name)
    assert snapshot(bad)==before
    refusals.append(name)
report={'passed':True,'opaque_payload_neither_copied_nor_evaluated':True,
 'publication_completion_protocol_defined_outside_core':True,
 'transactional_refusals':refusals,
 'scope':'Structural linear port core with explicit handle conservation; no physical rules, payload arithmetic, general confluence theorem, concurrency or unrestricted internal-redex topology.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/abstract-port-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
