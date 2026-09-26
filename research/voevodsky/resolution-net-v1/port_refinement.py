"""Executable closed-port/abstract-term diagram, including explicit pure compression."""
from dataclasses import dataclass
from reference import Seed,Step

@dataclass(frozen=True)
class Term:
    kind: str
    payload: object
    children: tuple = ()

def compact(term):
    if term.kind in ('keep','pending'):return term
    children=tuple(compact(t) for t in term.children)
    if all(t.kind=='keep' for t in children):
        return Term('keep',Step(term.payload,tuple(t.payload for t in children)))
    return Term(term.kind,term.payload,children)

def reify(net):
    net.validate()
    if getattr(net,'boundaries',{}):raise ValueError('closed-port refinement only')
    seen=set();paths={}
    def pure(port):
        i,entry=port
        if entry!=0 or i in seen:raise ValueError('invalid pure region')
        seen.add(i);a=net.agents[i]
        if a.kind=='flatten':raise ValueError('nested pending region')
        if a.kind=='seed':
            if a.arity==0:return Seed(a.payload.package,a.payload)
            return Seed(a.payload,pure(net.wires[i,1]))
        return Step(a.payload,tuple(pure(net.wires[i,k]) for k in range(1,a.arity+1)))
    def visit(port,path):
        i,entry=port;a=net.agents[i]
        if a.kind=='flatten':
            if entry!=1 or i in seen:raise ValueError('invalid pending entry')
            seen.add(i);paths[i]=path
            return Term('pending',pure(net.wires[i,0]))
        if a.kind=='seed':return Term('keep',pure(port))
        if entry!=0 or i in seen:raise ValueError('invalid constructor entry')
        seen.add(i)
        children=tuple(visit(net.wires[i,k],path+(k-1,)) for k in range(1,a.arity+1))
        return compact(Term('one' if a.arity==1 else 'two',a.payload,children))
    term=visit(net.wires[0,0],())
    if seen!=set(net.agents):raise ValueError('lost agents during reification')
    return term,paths

def contract(term,path):
    """Exactly one abstract contextual root step; no reference flatten call."""
    if path:
        if term.kind not in ('one','two'):raise ValueError('path enters pure/pending region')
        index=path[0]
        if index<0 or index>=len(term.children):raise ValueError('invalid context slot')
        children=list(term.children);children[index],rule=contract(children[index],path[1:])
        return Term(term.kind,term.payload,tuple(children)),rule
    if term.kind!='pending':raise ValueError('selected location is not pending')
    d=term.payload
    if isinstance(d,Seed):return Term('keep',d.evidence),'F-seed'
    return Term('one' if len(d.premises)==1 else 'two',d.rule,
                tuple(Term('pending',p) for p in d.premises)),('F-unary' if len(d.premises)==1 else 'F-binary')

def diagram(before,pair,after):
    term,paths=reify(before)
    if pair not in before.active():raise ValueError('no source active pair')
    result,rule=contract(term,paths[pair[0]])
    actual,_=reify(after)
    if compact(result)!=actual:raise ValueError('wire rewrite does not simulate contextual contraction plus pure compression')
    return {'context_path':paths[pair[0]],'rule':rule,'pure_compression_required':result!=actual}
