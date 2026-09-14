"""Finite hypothesis/interface planner with partial observation decoders."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from typing import Callable,Mapping

OUTCOMES=("++","+-","-+","--")

@dataclass(frozen=True,order=True)
class Proposition:
    name:str
    args:tuple[str,...]=()
    positive:bool=True
    scope:str="global"
    def negate(self)->Proposition:return Proposition(self.name,self.args,not self.positive,self.scope)
    @property
    def atom(self)->tuple[str,tuple[str,...],str]:return (self.name,self.args,self.scope)

@dataclass(frozen=True)
class Justification:
    conclusion:Proposition
    premises:frozenset[Proposition]
    relation:str
    @property
    def path_id(self)->str:
        payload=repr((self.conclusion,tuple(sorted(self.premises)),self.relation))
        return sha256(payload.encode()).hexdigest()

@dataclass(frozen=True)
class Coherence:
    left_path_id:str
    right_path_id:str
    relation:str
    witness:str
    def __post_init__(self)->None:
        if self.relation not in {"equal","equivalent","incompatible"}:raise ValueError("invalid path coherence relation")
        if self.left_path_id==self.right_path_id:raise ValueError("coherence requires distinct paths")
    @property
    def pair(self)->frozenset[str]:return frozenset({self.left_path_id,self.right_path_id})

@dataclass(frozen=True)
class Resolution:
    action:str
    starting_state_id:str
    selected_outcome:str
    alternatives:tuple[str,...]=OUTCOMES
    relation:str="exactly_one"
    def __post_init__(self)->None:
        if self.selected_outcome not in self.alternatives:raise ValueError("selected outcome is not an alternative")
        if len(set(self.alternatives))!=len(self.alternatives):raise ValueError("resolution alternatives must be distinct")
        if self.relation!="exactly_one":raise ValueError("only exactly_one resolutions are supported")
    @property
    def excluded_outcomes(self)->tuple[str,...]:return tuple(o for o in self.alternatives if o!=self.selected_outcome)

@dataclass(frozen=True)
class State:
    hypotheses:frozenset[str]
    interfaces:frozenset[str]=frozenset()
    resolutions:frozenset[Resolution]=frozenset()
    facts:frozenset[Proposition]=frozenset()
    justifications:frozenset[Justification]=frozenset()
    coherences:frozenset[Coherence]=frozenset()
    def __post_init__(self)->None:
        by_atom:dict[tuple[str,tuple[str,...],str],bool]={}
        for fact in self.facts:
            if fact.atom in by_atom and by_atom[fact.atom]!=fact.positive:raise ValueError(f"contradictory fact: {fact.atom}")
            by_atom[fact.atom]=fact.positive
        by_event:dict[tuple[str,str],str]={}
        for resolution in self.resolutions:
            key=(resolution.action,resolution.starting_state_id)
            if key in by_event and by_event[key]!=resolution.selected_outcome:raise ValueError(f"conflicting resolution: {key}")
            by_event[key]=resolution.selected_outcome
    def identity(self)->str:
        payload=repr((sorted(self.hypotheses),sorted(self.interfaces),sorted((r.action,r.starting_state_id,r.selected_outcome) for r in self.resolutions),sorted(self.facts),sorted((j.conclusion,tuple(sorted(j.premises)),j.relation) for j in self.justifications)))
        return sha256(payload.encode()).hexdigest()
    def resolve(self,action:str,outcome:str)->State:
        start=self.identity();resolution=Resolution(action,start,outcome)
        outcome_facts=frozenset(Proposition("outcome",(action,start,o),o==outcome,"action-resolution") for o in OUTCOMES)
        return State(self.hypotheses,self.interfaces,self.resolutions|{resolution},self.facts|outcome_facts,self.justifications,self.coherences)
    def merge(self,other:State)->State:
        return State(self.hypotheses|other.hypotheses,self.interfaces|other.interfaces,self.resolutions|other.resolutions,self.facts|other.facts,self.justifications|other.justifications,self.coherences|other.coherences)
    def derive(self,implications:tuple[Implication,...],assume_branch_premises:bool=False,coherences:frozenset[Coherence]=frozenset(),require_path_coherence:bool=False)->State:
        facts=set(self.facts);justifications=set(self.justifications);all_coherences=self.coherences|coherences
        if assume_branch_premises:
            for implication in implications:
                premises=implication.premises
                facts.update(premises)
        changed=True
        while changed:
            changed=False
            for implication in implications:
                conclusion=implication.conclusion
                if isinstance(conclusion,Proposition) and all(p in facts for p in implication.premises):
                    justification=Justification(conclusion,frozenset(implication.premises),implication.relation)
                    alternatives=[j for j in justifications if j.conclusion==conclusion and j.path_id!=justification.path_id]
                    for prior in alternatives:
                        matches=[c for c in all_coherences if c.pair==frozenset({prior.path_id,justification.path_id})]
                        if any(c.relation=="incompatible" for c in matches):raise ValueError(f"incompatible paths to {conclusion}")
                        if require_path_coherence and not any(c.relation in {"equal","equivalent"} for c in matches):raise ValueError(f"missing coherence for parallel paths to {conclusion}")
                    if conclusion not in facts:facts.add(conclusion);changed=True
                    justifications.add(justification)
        return State(self.hypotheses,self.interfaces,self.resolutions,frozenset(facts),frozenset(justifications),all_coherences)
    def invalidate(self,fact:Proposition)->State:
        facts=set(self.facts);facts.discard(fact);facts.add(fact.negate())
        changed=True
        while changed:
            changed=False
            conclusions={j.conclusion for j in self.justifications}
            for conclusion in conclusions:
                supports=[j for j in self.justifications if j.conclusion==conclusion and j.premises<=facts]
                if conclusion in facts and not supports:
                    facts.remove(conclusion);changed=True
        live=frozenset(j for j in self.justifications if j.conclusion in facts and j.premises<=facts)
        return State(self.hypotheses,self.interfaces,self.resolutions,frozenset(facts),live,self.coherences)

@dataclass(frozen=True)
class Effect:
    retain:frozenset[str]|None=None
    add:frozenset[str]=frozenset()
    remove:frozenset[str]=frozenset()
    raw:str|None=None
    def apply(self,s:State)->State:
        hs=s.hypotheses if self.retain is None else s.hypotheses & self.retain
        return State(hs,(s.interfaces-self.remove)|self.add,s.resolutions,s.facts,s.justifications,s.coherences)

@dataclass(frozen=True)
class Implication:
    premise:Proposition|tuple[Proposition,...]|str
    relation:str
    conclusion:Proposition|str
    evidence_requirement:str|None=None
    def __post_init__(self)->None:
        if self.relation not in {"entails","blocks","invalidates"}:raise ValueError(f"unsupported implication relation: {self.relation}")
        if isinstance(self.premise,tuple) and not self.premise:raise ValueError("implication requires at least one premise")
    @property
    def premises(self)->tuple[Proposition,...]:
        if isinstance(self.premise,Proposition):return (self.premise,)
        if isinstance(self.premise,tuple):return self.premise
        return ()

@dataclass(frozen=True)
class Branch:
    probability:float
    effect:Effect
    implications:tuple[Implication,...]=()

@dataclass(frozen=True)
class Action:
    name:str
    cost:float
    requires:frozenset[str]
    branches:Mapping[str,Branch]
    def available(self,s:State)->bool:return self.requires<=s.interfaces

@dataclass(frozen=True)
class Decoder:
    experiment:str
    raw:str
    requires:frozenset[str]
    target:str
    def decode(self,action:str,raw:str|None,state:State)->str|None:
        return self.target if action==self.experiment and raw==self.raw and self.requires<=state.interfaces else None

@dataclass(frozen=True)
class Value:
    success:float
    expected_cost:float
    first_action:str|None

class Planner:
    def __init__(self,actions:list[Action],decoders:list[Decoder],target:str,require_implications:bool=False):
        self.actions={a.name:a for a in actions};self.decoders=decoders;self.target=target
        for a in actions:
            if set(a.branches)!=set(OUTCOMES):raise ValueError(f"{a.name}: four branches required")
            if abs(sum(b.probability for b in a.branches.values())-1)>1e-12:raise ValueError(f"{a.name}: probabilities do not sum to one")
            if require_implications:
                missing=[o for o,b in a.branches.items() if not b.implications]
                if missing:raise ValueError(f"{a.name}: implication relation required for {missing}")
                for outcome,branch in a.branches.items():
                    for implication in branch.implications:
                        conclusion=implication.conclusion
                        if isinstance(conclusion,Proposition):
                            expected=branch.effect.add if conclusion.positive else branch.effect.remove
                            if conclusion.name not in expected:raise ValueError(f"{a.name}/{outcome}: implication conclusion disagrees with effect")
    def solve_expected(self,initial:State)->Value:
        @lru_cache(None)
        def go(state:State,unused:frozenset[str])->Value:
            candidates=[Value(0.,0.,None)]  # abandonment option
            for name in sorted(unused):
                a=self.actions[name]
                if not a.available(state):continue
                success=0.;future_cost=0.
                for outcome in OUTCOMES:
                    branch=a.branches[outcome];ns=branch.effect.apply(state.resolve(name,outcome)).derive(branch.implications,assume_branch_premises=True)
                    decoded=any(d.decode(name,branch.effect.raw,ns)==self.target for d in self.decoders)
                    child=Value(1.,0.,None) if decoded else go(ns,unused-{name})
                    success+=branch.probability*child.success
                    future_cost+=branch.probability*child.expected_cost
                candidates.append(Value(success,a.cost+future_cost,name))
            if not candidates:return Value(0.,0.,None)
            return max(candidates,key=lambda v:(v.success,-v.expected_cost,v.first_action or ''))
        return go(initial,frozenset(self.actions))
