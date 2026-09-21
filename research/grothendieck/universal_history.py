"""Exact finite jets of the full degree-completed tensor history.

A word is a tuple of source-generator labels. Jet products and inverse
coefficients are computed at a declared order; no finite jet is called the
whole completed history. Coefficients may be exact rationals or symbolic.
"""
from dataclasses import dataclass

@dataclass
class Jet:
    order: int
    terms: dict

    def __post_init__(self):
        if not isinstance(self.order,int) or self.order<0:
            raise ValueError('Order must be a nonnegative integer')
        if any(not isinstance(k,tuple) or len(k)>self.order for k in self.terms):
            raise ValueError('A word exceeds the jet order or is not a tuple')
        self.terms={k:v for k,v in self.terms.items() if v!=0}

    @classmethod
    def unit(cls,order): return cls(order,{():1})

    @classmethod
    def event(cls,order,window):
        """window maps chamber label to its linear incidence coefficient."""
        return cls(order,{():1,**({(k,):v for k,v in window.items()} if order else {})})

    def project(self,order):
        if not 0<=order<=self.order:
            raise ValueError('Projection cannot manufacture higher coefficients')
        return Jet(order,{k:v for k,v in self.terms.items() if len(k)<=order})

    def __add__(self,other):
        if self.order!=other.order: raise ValueError('Orders must agree')
        out=dict(self.terms)
        for k,v in other.terms.items():out[k]=out.get(k,0)+v
        return Jet(self.order,out)

    def scale(self,a):return Jet(self.order,{k:a*v for k,v in self.terms.items()})

    def __mul__(self,other):
        if self.order!=other.order: raise ValueError('Orders must agree')
        out={}
        for u,a in self.terms.items():
            for v,b in other.terms.items():
                if len(u)+len(v)<=self.order:
                    out[u+v]=out.get(u+v,0)+a*b
        return Jet(self.order,out)

    def inverse(self):
        """Geometric inverse of a unit-augmented jet, exactly to this order."""
        if self.terms.get((),0)!=1:
            raise ValueError('Expected augmentation one')
        a=self+Jet.unit(self.order).scale(-1)
        out=Jet.unit(self.order); power=out
        for k in range(1,self.order+1):
            power=power*a
            out=out+power.scale((-1)**k)
        return out


def record(order,windows):
    out=Jet.unit(order)
    for window in windows:out=out*Jet.event(order,window)
    return out
