"""Two-boundary identity interface, not a two-point scattering amplitude.
Fixed agent signature with exact rational attributed payloads.
"""
from dataclasses import dataclass
from fractions import Fraction

PORTS={'INPUT':('p',),'ID':('p','out','ack'),'VALUE':('p',),
       'OUT':('p',),'ACK':('p',),'CLEAN':('p','ack'),
       'TICKET':('p',),'DONE':('p',)}

@dataclass(frozen=True)
class Scalar:
    value: Fraction
    def __post_init__(self):
        if not isinstance(self.value,Fraction):
            raise TypeError('exact Fraction required')

class IdentityNet:
    def __init__(self,payload):
        if not isinstance(payload,Scalar):raise TypeError('Scalar input required')
        self.nodes={};self.wires={};self.serial=0
        inp=self.add('INPUT',payload);identity=self.add('ID')
        self.out=self.add('OUT');self.ack=self.add('ACK')
        self.link((inp,'p'),(identity,'p'))
        self.link((identity,'out'),(self.out,'p'))
        self.link((identity,'ack'),(self.ack,'p'))
        self.validate()

    def add(self,kind,payload=None):
        if kind not in PORTS:raise ValueError('unknown kind')
        n=self.serial;self.serial+=1;self.nodes[n]=(kind,payload);return n

    def link(self,a,b):
        if a==b or a in self.wires or b in self.wires:raise ValueError('nonlinear port')
        for n,p in (a,b):
            if n not in self.nodes or p not in PORTS[self.nodes[n][0]]:
                raise ValueError('unknown port')
        self.wires[a]=b;self.wires[b]=a

    def validate(self):
        ports={(n,p) for n,(kind,_) in self.nodes.items() for p in PORTS[kind]}
        if ports!=set(self.wires):raise ValueError('unwired or foreign port')
        if any(a==b or self.wires.get(b)!=a for a,b in self.wires.items()):
            raise ValueError('asymmetric wiring')
        if self.nodes and self.serial<=max(self.nodes):raise ValueError('stale allocator')

    def enabled(self):
        self.validate();result=[]
        for n,(kind,_) in self.nodes.items():
            m,p=self.wires[n,'p']
            if p=='p' and (kind,self.nodes[m][0]) in (('INPUT','ID'),('CLEAN','TICKET')):
                result.append((n,m))
        return result

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive or consumed pair')
        a,b=pair;kind,payload=self.nodes[a]
        if kind=='INPUT':
            output=self.wires[b,'out'];ack=self.wires[b,'ack']
        else:ack=self.wires[a,'ack']
        for n in pair:
            for p in PORTS[self.nodes[n][0]]:
                endpoint=(n,p)
                if endpoint in self.wires:
                    peer=self.wires.pop(endpoint);del self.wires[peer]
            del self.nodes[n]
        if kind=='INPUT':
            value=self.add('VALUE',payload);clean=self.add('CLEAN');ticket=self.add('TICKET')
            self.link((value,'p'),output);self.link((clean,'p'),(ticket,'p'))
            self.link((clean,'ack'),ack)
        else:
            done=self.add('DONE');self.link((done,'p'),ack)
        self.validate()

    def observe(self):
        """Immutable (value-or-None, complete) snapshot; zero is not pending."""
        peer,_=self.wires[self.out,'p'];kind,payload=self.nodes[peer]
        ack,_=self.wires[self.ack,'p']
        return (payload if kind=='VALUE' else None,self.nodes[ack][0]=='DONE')

    def meaning(self):
        carriers=[p for k,p in self.nodes.values() if k in ('INPUT','VALUE')]
        if len(carriers)!=1:raise ValueError('lost or duplicated scalar')
        return carriers[0]
