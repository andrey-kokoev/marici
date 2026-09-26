"""Independent tree-class admission, pending work measure and semantic observer.

Not called by the rewrite engine: reference flatten is used only as an oracle.
"""
from reference import Admission, Package, Rule, Seed, Step, flatten

def outer_size(history):
    if isinstance(history, Seed):return 1
    return 1 + sum(outer_size(p) for p in history.premises)

def audit(net):
    net.validate()
    seen = set()
    def walk(port, pure=False):
        i, entry = port
        if i == 0 or i in seen:raise ValueError('cycle, alias or boundary in subtree')
        seen.add(i);a=net.agents[i]
        if type(a.level) is not int or a.level < 0:raise ValueError('invalid level')
        if a.kind == 'flatten':
            if pure or entry != 1 or a.arity != 1 or a.payload is not None:
                raise ValueError('invalid pending flatten position/signature')
            h, cost, syntax=walk(net.wires[i,0],True)
            if a.level != h.level or h.level < 1 or cost:raise ValueError('invalid flatten input layer')
            return flatten(h),outer_size(h),('F',syntax)
        if entry != 0:raise ValueError('constructor entered through an auxiliary port')
        if a.kind == 'seed':
            if a.arity == 0 and isinstance(a.payload,Admission):
                h=Seed(a.payload.package,a.payload);cost=0;syntax=('S0',a.payload)
            elif a.arity == 1 and isinstance(a.payload,Package):
                inner,cost,child=walk(net.wires[i,1],True)
                h=Seed(a.payload,inner);syntax=('S1',a.payload,child)
            else:raise ValueError('invalid seed signature')
        elif a.kind == 'step' and isinstance(a.payload,Rule):
            if a.arity != len(a.payload.inputs):raise ValueError('invalid rule arity')
            children=[walk(net.wires[i,k],pure) for k in range(1,a.arity+1)]
            h=Step(a.payload,tuple(c[0] for c in children));cost=sum(c[1] for c in children)
            syntax=('U' if a.arity==1 else 'B',a.payload,tuple(c[2] for c in children))
        else:raise ValueError('unknown signature')
        if h.level != a.level:raise ValueError('constructor level mismatch')
        return h,cost,syntax
    answer=walk(net.wires[0,0])
    if seen != set(net.agents):raise ValueError('unreachable agents')
    return answer
