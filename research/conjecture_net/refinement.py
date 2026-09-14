"""Typed next-rung refinement and cheap-information gate scheduling."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping

OUTCOMES=frozenset({'++','+-','-+','--'})

@dataclass(frozen=True)
class InterfaceType:
    name:str
    domain:str
    codomain:str

@dataclass(frozen=True)
class Gate:
    name:str
    requires:frozenset[str]
    produces:tuple[InterfaceType,...]
    estimated_cost:float
    branch_elimination:float
    interface_tightening:float
    falsification_power:float=0.0
    hard_type_gate:bool=False
    def score(self)->float:
        if self.estimated_cost<=0:raise ValueError('gate cost must be positive')
        priority=2.0 if self.hard_type_gate else 1.0
        return priority*(self.branch_elimination+self.interface_tightening+self.falsification_power)/self.estimated_cost

@dataclass(frozen=True)
class AggregationRule:
    """Frozen parent semantics. No parent outcome exists until every child resolves."""
    all_success_parent:str='++'
    soft_failure_parent:str='+-'
    hard_failure_parent:str='-+'
    invalid_parent:str='--'
    def aggregate(self,children:tuple[str,...],resolved:Mapping[str,str])->str|None:
        if any(x not in OUTCOMES for x in resolved.values()):raise ValueError('invalid child outcome')
        values=[resolved[x] for x in children if x in resolved]
        # Invalid or hard-failure children short-circuit: no descendant can repair them.
        if '--' in values:return self.invalid_parent
        if '-+' in values:return self.hard_failure_parent
        if any(x not in resolved for x in children):return None
        if '+-' in values:return self.soft_failure_parent
        return self.all_success_parent

@dataclass(frozen=True)
class ExistentialAggregationRule:
    """Aggregate branches when existence requires at least one terminal `*+`."""
    success_pattern:str='*+'
    def aggregate(self,children:tuple[str,...],resolved:Mapping[str,str])->str|None:
        if self.success_pattern not in {'*+','*-'}:raise ValueError('existential pattern must constrain terminal polarity')
        if any(x not in OUTCOMES for x in resolved.values()):raise ValueError('invalid child outcome')
        wanted=self.success_pattern[1]
        values=[resolved[x] for x in children if x in resolved]
        if any(v[1]==wanted for v in values):return '++'
        if any(x not in resolved for x in children):return None
        return '-+'

@dataclass(frozen=True)
class RefinementPlan:
    parent_action:str
    gates:tuple[Gate,...]
    dependencies:tuple[tuple[str,str],...]
    aggregation:AggregationRule|ExistentialAggregationRule=AggregationRule()
    def validate(self)->None:
        names={g.name for g in self.gates}
        if not names or len(names)!=len(self.gates):raise ValueError('child gate names must be nonempty and unique')
        if self.parent_action in names:raise ValueError('parent cannot be its own child')
        if any(a not in names or b not in names for a,b in self.dependencies):raise ValueError('dependency names unknown gate')
        # Kahn cycle check.
        done=set()
        while len(done)<len(names):
            ready={n for n in names-done if all(a in done for a,b in self.dependencies if b==n)}
            if not ready:raise ValueError('cyclic refinement dependencies')
            done|=ready
        produced=[x.name for g in self.gates for x in g.produces]
        if len(produced)!=len(set(produced)):raise ValueError('duplicate produced interface')
        for g in self.gates:g.score()
    def next_gate(self,available_interfaces:frozenset[str],resolved:frozenset[str]=frozenset())->Gate|None:
        self.validate();names={g.name for g in self.gates};candidates=[]
        for g in self.gates:
            predecessors={a for a,b in self.dependencies if b==g.name}
            if g.name not in resolved and predecessors<=resolved and g.requires<=available_interfaces:candidates.append(g)
        return max(candidates,key=lambda g:(g.score(),-g.estimated_cost,g.name),default=None)
