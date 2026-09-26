"""Theory-neutral linear port infrastructure.
No arithmetic, observer, physical convention or automatic payload copying.
Replacement transfers opaque payload handles by explicit one-to-one ownership.
Single-threaded transactional mutation; no concurrency guarantees.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Signature:
    principal: str
    auxiliaries: tuple = ()
    @property
    def ports(self):
        return (self.principal,)+self.auxiliaries
    def __post_init__(self):
        if not isinstance(self.auxiliaries,tuple):raise TypeError('tuple auxiliaries required')
        if any(not isinstance(p,str) or not p for p in self.ports):raise ValueError('invalid port')
        if len(set(self.ports))!=len(self.ports):raise ValueError('duplicate port')

@dataclass(frozen=True)
class Agent:
    kind: str
    handles: tuple = ()

class PortNet:
    def __init__(self,signatures):
        if not signatures or any(not isinstance(v,Signature) for v in signatures.values()):
            raise ValueError('explicit signatures required')
        self.signatures=dict(signatures)
        self.nodes={};self.wires={};self.serial=0

    def add(self,kind,handles=()):
        if kind not in self.signatures:raise ValueError('undeclared agent')
        if not isinstance(handles,tuple):raise TypeError('tuple handles required')
        try: unique=set(handles)
        except TypeError as exc:raise TypeError('handles must be hashable identifiers') from exc
        owned={h for a in self.nodes.values() for h in a.handles}
        if len(unique)!=len(handles) or unique & owned:raise ValueError('duplicate handle owner')
        n=self.serial;self.serial+=1;self.nodes[n]=Agent(kind,handles);return n

    def ports(self):
        return {(n,p) for n,a in self.nodes.items() for p in self.signatures[a.kind].ports}

    def link(self,a,b):
        ports=self.ports()
        if a not in ports or b not in ports:raise ValueError('unknown endpoint')
        if a==b or a in self.wires or b in self.wires:raise ValueError('nonlinear wiring')
        self.wires[a]=b;self.wires[b]=a

    def validate(self):
        if self.ports()!=set(self.wires):raise ValueError('open or foreign endpoint')
        if any(a==b or self.wires.get(b)!=a for a,b in self.wires.items()):
            raise ValueError('asymmetric wiring')
        handles=[h for a in self.nodes.values() for h in a.handles]
        if len(handles)!=len(set(handles)):raise ValueError('duplicate ownership')
        if self.nodes and self.serial<=max(self.nodes):raise ValueError('stale allocator')

    def principal_pairs(self):
        self.validate();pairs=[]
        for n,a in self.nodes.items():
            peer,p=self.wires[n,self.signatures[a.kind].principal]
            if n<peer and p==self.signatures[self.nodes[peer].kind].principal:
                pairs.append((n,peer))
        return pairs

    def replace(self,pair,replacements,internal,boundary):
        """Atomic principal-pair replacement, not an authorization of a theory rule.
        replacements: tuple Agent; internal: pairs of (new-index,port).
        boundary: old auxiliary endpoint -> (new-index,port), bijective coverage.
        All old handles must occur exactly once among replacement agents.
        Extra edges inside the redex are outside this initial contract.
        """
        self.validate()
        a,b=pair
        if a==b or tuple(sorted(pair)) not in self.principal_pairs():
            raise ValueError('not a principal pair')
        old_boundary={}
        for n in pair:
            for p in self.signatures[self.nodes[n].kind].auxiliaries:
                peer=self.wires[n,p]
                if peer[0] in pair:raise ValueError('extra internal redex edge')
                old_boundary[n,p]=peer
        if set(boundary)!=set(old_boundary):raise ValueError('boundary mismatch')
        old_handles=[h for n in pair for h in self.nodes[n].handles]
        new_handles=[h for agent in replacements for h in agent.handles]
        if len(new_handles)!=len(set(new_handles)) or set(new_handles)!=set(old_handles):
            raise ValueError('payload loss, duplication or invention')
        # Stage only structural state; no copying or inspecting payload objects.
        trial=PortNet(self.signatures)
        trial.nodes=dict(self.nodes);trial.wires=dict(self.wires);trial.serial=self.serial
        for n in pair:
            for p in self.signatures[trial.nodes[n].kind].ports:
                ep=(n,p)
                if ep in trial.wires:
                    other=trial.wires.pop(ep);del trial.wires[other]
            del trial.nodes[n]
        ids=[trial.add(agent.kind,agent.handles) for agent in replacements]
        def resolve(ep):
            index,port=ep
            if not isinstance(index,int) or index<0 or index>=len(ids):raise ValueError('bad local index')
            return ids[index],port
        for x,y in internal:trial.link(resolve(x),resolve(y))
        for old,new in boundary.items():trial.link(resolve(new),old_boundary[old])
        trial.validate()
        self.nodes,self.wires,self.serial=trial.nodes,trial.wires,trial.serial
        return tuple(ids)
