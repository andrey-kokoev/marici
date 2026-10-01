"""Does the rung diagram and a unit rung4 reference select a Gram transport?

Conditional coordinate models: nested probe spaces with invariant Gram aI+bJ.
Every discarded coefficient is retained. The r-dimensional chart assignment is
an explicit test model, not an identification with the record-family tower.
"""
from fractions import Fraction as F
from itertools import permutations
from dataclasses import dataclass


@dataclass(frozen=True)
class Chart:
    live: tuple
    records: tuple=()  # (old dimension, removed signed coefficient)


class Model:
    def __init__(self,a,b):
        self.a,self.b=F(a),F(b)
        assert self.a>0 and all(self.a+n*self.b>0 for n in range(4,13))
        self.normalization=self.a+4*self.b

    def inner(self,x,y):
        return (self.a*sum((u*v for u,v in zip(x,y)),F(0))+self.b*sum(x)*sum(y))/self.normalization

    def move(self,state,n):
        x=list(state.live); history=list(state.records)
        while len(x)>n:
            k=len(x); removed=x[-1]
            history.append((k,removed))
            x=[v+self.b*removed/(self.a+(k-1)*self.b) for v in x[:-1]]
        return Chart(tuple(x),tuple(history))

    def restore(self,state):
        x=list(state.live)
        for k,removed in reversed(state.records):
            assert len(x)==k-1
            x=[v-self.b*removed/(self.a+(k-1)*self.b) for v in x]+[removed]
        return tuple(x)

    def budget(self,state):
        return self.inner(state.live,state.live)+sum((self.a*(self.a+k*self.b)/(self.a+(k-1)*self.b)
                        *removed*removed/self.normalization for k,removed in state.records),F(0))


reference=(F(1,2),)*4
seeds=[tuple(F(i==j) for i in range(12)) for j in range(12)]
seeds += [tuple(F(i+1) for i in range(12)),(F(1),F(-1))+(F(0),)*10]
models=[Model(10,1),Model(2,1),Model(1,0)]
for model in models:
    assert model.inner(reference,reference)==1
    for p in permutations(range(4)):
        x=(F(1),F(2),F(-1),F(3))
        assert model.inner(tuple(x[i] for i in p),tuple(x[i] for i in p))==model.inner(x,x)
    for seed in seeds:
        s12=Chart(seed)
        s11=model.move(s12,11); s10=model.move(s11,10)
        s6=model.move(s12,6)                 # T9
        s5=model.move(s11,5)                 # T8
        s4=model.move(s10,4)                 # T7
        assert model.move(s6,5)==s5
        assert model.move(s5,4)==s4==model.move(s12,4)
        assert model.restore(s4)==seed
        assert model.budget(s4)==model.inner(seed,seed)
        direct=tuple(seed[i]+model.b*sum(seed[4:])/(model.a+4*model.b) for i in range(4))
        assert s4.live==direct
        # Retained residual is orthogonal to the target subspace.
        residual=tuple(seed[i]-(s4.live[i] if i<4 else 0) for i in range(12))
        for j in range(4):
            assert model.inner(residual,tuple(F(i==j) for i in range(12)))==0

# Same unit reference and same bottom data, but different contrast costs.
contrast=(F(1),F(-1),F(0),F(0))
assert [model.inner(contrast,contrast) for model in models]==[F(10,7),F(2,3),F(2)]
# The transport itself also differs for data outside the bottom subspace.
assert models[0].move(Chart(seeds[11]),4).live!=(models[1].move(Chart(seeds[11]),4).live)
# Existing S12 stabilizer probes select a=10,b=1 only after that probe/measure
# realization is imposed: common and contrast eigenvalues are22 and10 at12,
# then14 and10 at4, before the single rung4 reference normalization.
assert models[0].a+12*models[0].b==22
assert models[0].a+4*models[0].b==14
assert models[0].a/(models[0].a+4*models[0].b)==F(5,7)
print('Three invariant Gram models pass both rung squares, exact retained reconstruction and orthogonal budget conservation.')
print('The same rung4 reference has unit norm in every model; contrast costs and horizontal transports still differ.')
print('Fixed S12 stabilizer-indicator probes select G=10I+J and normalized bottom contrast coefficient5/7, conditional on that realization.')
print('This is a retained Gram-chart model. Its identification with label/from/to family presentations and physical energy remains an additional adapter.')
