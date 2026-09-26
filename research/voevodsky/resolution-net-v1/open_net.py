"""Open-port extension: absent evidence is an interface, not an agent or seed."""
from copy import copy
from reference import Admission,Seed,Step,unit
from pending import Hole,Pending
from local_net import Agent,Net
from admission import validate,require

class OpenNet(Net):
    def __init__(self,context):
        Pending(context)  # validate unique hole occurrences and rule interfaces
        self.agents={};self.wires={};self.next_id=1;self.boundaries={};self.receipts=()
        def compile_context(c):
            if isinstance(c,Hole):
                boundary=-len(self.boundaries)-1;self.boundaries[boundary]=(c.slot,c.package)
                node=self.allocate(Agent('seed',c.package,1,1))
                self.connect((node,1),(boundary,0));return (node,0)
            node=self.allocate(Agent('step',c.rule,len(c.children),1))
            for k,child in enumerate(c.children,1):self.connect((node,k),compile_context(child))
            return (node,0)
        root=compile_context(context);f=self.allocate(Agent('flatten',None,1,1))
        self.connect((f,0),root);self.connect((0,0),(f,1));self.validate()

    def validate(self):
        require(type(self.receipts) is tuple,'mutable receipts')
        require(len({r[0] for r in self.receipts})==len(self.receipts),'duplicate received slot')
        require(len({r[1] for r in self.receipts})==len(self.receipts),'duplicate received ticket')
        require(not ({slot for slot,_ in self.boundaries.values()} & {r[0] for r in self.receipts}),'received slot still open')
        return validate(self,self.boundaries)

    def arrive(self,slot,ticket,evidence):
        self.validate()
        require(type(ticket) is str and bool(ticket),'invalid ticket')
        require(ticket not in {r[1] for r in self.receipts},'reused ticket')
        matches=[i for i,(s,_) in self.boundaries.items() if s==slot]
        require(len(matches)==1,'unknown or already consumed slot')
        boundary=matches[0]
        history=unit(evidence) if type(evidence) is Admission else evidence
        require(type(history) in (Seed,Step),'pure history evidence required')
        require(history.level==0 and history.package==self.boundaries[boundary][1],'wrong input interface')
        candidate=copy(self);candidate.agents=self.agents.copy();candidate.wires=self.wires.copy();candidate.boundaries=self.boundaries.copy()
        parent=candidate.wires.pop((boundary,0));del candidate.wires[parent];del candidate.boundaries[boundary]
        root=candidate.compile(history);candidate.connect(parent,root)
        candidate.receipts=self.receipts+((slot,ticket,history),)
        candidate.validate()
        self.agents,self.wires,self.next_id,self.boundaries,self.receipts=candidate.agents,candidate.wires,candidate.next_id,candidate.boundaries,candidate.receipts

    def released(self):
        self.validate()
        return not self.boundaries and not any(a.kind=='flatten' for a in self.agents.values())

    def readback(self):
        if not self.released():raise ValueError('unfilled evidence or unfinished structural normalization')
        return super().readback()
