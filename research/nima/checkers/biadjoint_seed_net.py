"""Coupling-stripped planar biadjoint primitives with separate conventions.
UNIT emits J(i)=1 (amputated current seed); PROP emits 1/X for a nonzero
exact channel value. No i epsilon, coupling, color tensor or external propagator
is inferred. Attributed rational evaluation is one primitive local rule.
"""
from dataclasses import dataclass
from fractions import Fraction
from amplitude_identity_net import IdentityNet, Scalar, PORTS
PORTS.update({'UNIT':('p',), 'PROP':('p',)})

@dataclass(frozen=True)
class UnitCurrent:
    leg: str
    def __post_init__(self):
        if not isinstance(self.leg,str) or not self.leg:
            raise ValueError('nonempty external-leg label required')

@dataclass(frozen=True)
class Channel:
    label: str
    value: Fraction
    def __post_init__(self):
        if not isinstance(self.label,str) or not self.label:
            raise ValueError('channel label required')
        if not isinstance(self.value,Fraction):raise TypeError('exact Fraction required')
        if self.value==0:raise ValueError('channel pole: cannot evaluate 1/0')

class PrimitiveNet(IdentityNet):
    def __init__(self,request):
        if not isinstance(request,(UnitCurrent,Channel)):
            raise TypeError('UnitCurrent or Channel required')
        super().__init__(Scalar(Fraction(1)))
        node=next(n for n,(k,_) in self.nodes.items() if k=='INPUT')
        self.nodes[node]=('UNIT' if isinstance(request,UnitCurrent) else 'PROP',request)
        self.request=request
        self.validate()

    @staticmethod
    def evaluate(request):
        return Scalar(Fraction(1) if isinstance(request,UnitCurrent) else 1/request.value)

    def enabled(self):
        result=super().enabled()
        for n,(kind,_) in self.nodes.items():
            if kind not in ('UNIT','PROP'):continue
            peer,port=self.wires[n,'p']
            if port=='p' and self.nodes[peer][0]=='ID':result.append((n,peer))
        return result

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive or consumed pair')
        n,_=pair;kind,payload=self.nodes[n]
        if kind in ('UNIT','PROP'):
            # Shared replacement template: this dispatch is not a scheduled
            # intermediate state. The local rule computes its emitted payload.
            self.nodes[n]=('INPUT',self.evaluate(payload))
        super().step(pair)

    def meaning(self):
        requests=[v for k,v in self.nodes.values() if k in ('UNIT','PROP')]
        if requests:
            if len(requests)!=1:raise ValueError('duplicated primitive')
            return self.evaluate(requests[0])
        return super().meaning()
