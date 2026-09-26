"""Single-process shared-commit model, NOT a production authorization service.

Authority is external to the resolution calculus. Ticket evidence is registered
by the fixture/operator, never inferred from a caller-supplied witness string.
"""
from copy import deepcopy
from threading import RLock
from reference import Admission
from open_net import OpenNet

class TicketAuthority:
    def __init__(self, grants):
        if not all(type(k) is str and k and type(v) is Admission for k,v in grants.items()):
            raise ValueError('registered ticket admissions required')
        self._grants=dict(grants)
        self._spent={}
        self._branches={}
        self._lock=RLock()

    def register(self,name,net):
        with self._lock:
            if name in self._branches:raise ValueError('duplicate branch')
            net.validate();self._branches[name]=(0,deepcopy(net))

    def fork(self,source,destination):
        with self._lock:
            if destination in self._branches:raise ValueError('duplicate branch')
            _,net=self._branches[source];self._branches[destination]=(0,deepcopy(net))

    def snapshot(self,name):
        with self._lock:
            version,net=self._branches[name]
            return version,deepcopy(net)

    def spent(self):
        with self._lock:return dict(self._spent)

    def accept(self,name,expected_version,slot,ticket):
        with self._lock:
            version,net=self._branches[name]
            if version!=expected_version:raise ValueError('stale branch revision')
            if ticket not in self._grants:raise ValueError('unregistered ticket')
            if ticket in self._spent:raise ValueError('ticket already committed')
            candidate=deepcopy(net)
            # Failures here commit neither the net nor the ownership record.
            candidate.arrive(slot,ticket,self._grants[ticket])
            candidate.validate()
            self._branches[name]=(version+1,candidate)
            self._spent[ticket]=(name,slot,version+1)
            return version+1
