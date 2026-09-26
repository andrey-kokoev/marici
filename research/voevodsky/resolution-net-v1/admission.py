"""Fail-closed finite tree-net admission. No flattening or history evaluation."""
from reference import Admission, Package, Rule

def require(ok, message):
    if not ok:raise ValueError(message)

def package(p):
    require(type(p) is Package and type(p.name) is str and type(p.data) is tuple
            and all(type(x) is str for x in p.data), 'invalid immutable package')

def validate(net, boundaries=None):
    boundaries = {} if boundaries is None else boundaries
    require(type(boundaries) is dict, 'invalid boundary store')
    slots=set()
    for i,contract in boundaries.items():
        require(type(i) is int and i<0 and type(contract) is tuple and len(contract)==2, 'invalid input boundary')
        slot,p=contract
        require(type(slot) is str and slot not in slots, 'duplicate input slot')
        package(p);slots.add(slot)
    require(type(net.agents) is dict and type(net.wires) is dict, 'invalid stores')
    require(all(type(i) is int and i>0 for i in net.agents), 'invalid agent ID')
    require(type(net.next_id) is int and net.next_id>max(net.agents,default=0), 'allocator collision')
    for a in net.agents.values():
        require(type(a.level) is int and a.level>=0, 'invalid layer')
        require(type(a.arity) is int, 'invalid arity')
        require((a.kind,a.arity) in (('flatten',1),('seed',0),('seed',1),('step',1),('step',2)), 'unknown signature')
    ports={(0,0)}|{(i,0) for i in boundaries}|{(i,k) for i,a in net.agents.items() for k in range(a.arity+1)}
    require(set(net.wires)==ports, 'missing or extra wire ports')
    for p,q in net.wires.items():
        require(type(q) is tuple and len(q)==2 and all(type(x) is int for x in q), 'invalid endpoint')
        require(q in ports and p!=q and net.wires[q]==p, 'nonreciprocal or self wire')
    seen=set()
    def visit(port,pure=False):
        i,entry=port
        require(i!=0 and i not in seen, 'cycle, alias or internal boundary')
        seen.add(i)
        if i in boundaries:
            require(entry==0, 'invalid input boundary port')
            return boundaries[i][1],0
        a=net.agents[i]
        if a.kind=='flatten':
            require(not pure and entry==1 and a.payload is None, 'invalid pending region')
            p,level=visit(net.wires[i,0],True)
            require(level==a.level and level>0, 'invalid flatten layer')
            return p,level-1
        require(entry==0, 'auxiliary constructor entry')
        if a.kind=='seed':
            if a.arity==0:
                require(type(a.payload) is Admission and type(a.payload.witness) is str, 'invalid admission witness')
                p=a.payload.package;package(p);level=0
            else:
                p=a.payload;package(p);child,level=visit(net.wires[i,1],True)
                require(child==p, 'seed evidence package mismatch');level+=1
        else:
            r=a.payload
            require(type(r) is Rule and type(r.inputs) is tuple and len(r.inputs)==a.arity
                    and type(r.name) is str and type(r.witness) is str, 'invalid rule witness')
            package(r.output)
            for p in r.inputs:package(p)
            children=[visit(net.wires[i,k],pure) for k in range(1,a.arity+1)]
            require(tuple(p for p,_ in children)==r.inputs, 'rule premise mismatch')
            require(len({level for _,level in children})==1, 'mixed premise layers')
            p=r.output;level=children[0][1]
        require(a.level==level, 'constructor layer mismatch')
        return p,level
    interface=visit(net.wires[0,0])
    require(seen==set(net.agents)|set(boundaries), 'unreachable agents or input boundaries')
    return interface
