"""Append-only event sourcing for conjecture-net resolutions and topology changes."""
from __future__ import annotations
from dataclasses import asdict,dataclass
from hashlib import sha256
import json
from typing import Callable,Mapping


def digest(value:object)->str:
    return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

@dataclass(frozen=True)
class StateDelta:
    add_interfaces:tuple[str,...]=()
    remove_interfaces:tuple[str,...]=()
    add_facts:tuple[str,...]=()
    remove_facts:tuple[str,...]=()

@dataclass(frozen=True)
class ResolutionEvent:
    action_id:str
    action_contract_digest:str
    graph_before_digest:str
    state_before_id:str
    selected_outcome:str
    excluded_outcomes:tuple[str,...]
    evidence_refs:tuple[str,...]
    execution_cost:float
    execution_telemetry:tuple[tuple[str,str],...]
    applied_effect:StateDelta
    implications:tuple[tuple[str,str,str],...]
    invalidations:tuple[str,...]
    state_after_id:str
    timestamp:str
    kind:str="resolution"
    @property
    def event_id(self)->str:return digest(asdict(self))

@dataclass(frozen=True)
class CorrectionEvent:
    action_id:str
    superseded_event_id:str
    graph_before_digest:str
    state_before_id:str
    old_outcome:str
    corrected_outcome:str
    evidence_refs:tuple[str,...]
    applied_effect:StateDelta
    state_after_id:str
    timestamp:str
    kind:str="correction"
    @property
    def event_id(self)->str:return digest(asdict(self))

@dataclass(frozen=True)
class RefinementEvent:
    """Replace one coarse action by typed child gates with a frozen aggregation rule."""
    old_graph_digest:str
    parent_action:str
    child_actions:tuple[str,...]
    contracts_digest:str
    dependency_order:tuple[tuple[str,str],...]
    aggregation_rule_digest:str
    new_graph_digest:str
    reason:str
    evidence_refs:tuple[str,...]
    timestamp:str
    kind:str="refinement"
    @property
    def event_id(self)->str:return digest(asdict(self))

@dataclass(frozen=True)
class TopologyEvent:
    old_graph_digest:str
    operation:str
    added_actions:tuple[str,...]
    removed_actions:tuple[str,...]
    split_actions:tuple[tuple[str,tuple[str,...]],...]
    dependency_changes:tuple[str,...]
    new_graph_digest:str
    reason:str
    evidence_refs:tuple[str,...]
    timestamp:str
    kind:str="topology"
    @property
    def event_id(self)->str:return digest(asdict(self))

Event=ResolutionEvent|CorrectionEvent|TopologyEvent|RefinementEvent

@dataclass(frozen=True)
class Projection:
    graph_digest:str
    state_id:str
    interfaces:frozenset[str]=frozenset()
    facts:frozenset[str]=frozenset()
    sunk_cost:float=0.0
    resolved_actions:frozenset[tuple[str,str]]=frozenset()
    event_ids:tuple[str,...]=()

@dataclass(frozen=True)
class EventLog:
    initial_graph_digest:str
    initial_state_id:str
    events:tuple[Event,...]=()
    initial_interfaces:frozenset[str]=frozenset()
    initial_facts:frozenset[str]=frozenset()
    initial_sunk_cost:float=0.0
    initial_resolved_actions:frozenset[tuple[str,str]]=frozenset()
    initial_event_ids:tuple[str,...]=()
    @classmethod
    def resume(cls,projection:Projection)->EventLog:
        """Continue from a complete projection without resetting cumulative state."""
        return cls(projection.graph_digest,projection.state_id,(),projection.interfaces,projection.facts,projection.sunk_cost,projection.resolved_actions,projection.event_ids)
    def project(self,through:int|None=None)->Projection:
        if through is not None and not 0<=through<=len(self.events):raise IndexError("through is an event count in [0,len(events)]")
        p=Projection(self.initial_graph_digest,self.initial_state_id,self.initial_interfaces,self.initial_facts,self.initial_sunk_cost,self.initial_resolved_actions,self.initial_event_ids)
        selected=self.events if through is None else self.events[:through]
        for event in selected:
            if isinstance(event,(TopologyEvent,RefinementEvent)):
                if event.old_graph_digest!=p.graph_digest:raise ValueError("topology graph-chain mismatch")
                if isinstance(event,RefinementEvent):
                    if not event.child_actions:raise ValueError("refinement has no child gates")
                    if len(set(event.child_actions))!=len(event.child_actions):raise ValueError("duplicate refinement child gate")
                    if event.parent_action in event.child_actions:raise ValueError("refinement child equals parent")
                p=Projection(event.new_graph_digest,p.state_id,p.interfaces,p.facts,p.sunk_cost,p.resolved_actions,p.event_ids+(event.event_id,))
            elif isinstance(event,CorrectionEvent):
                if event.graph_before_digest!=p.graph_digest:raise ValueError("correction graph mismatch")
                if event.state_before_id!=p.state_id:raise ValueError("correction state-chain mismatch")
                if event.superseded_event_id not in p.event_ids:raise ValueError("correction does not reference prior event")
                if (event.action_id,event.old_outcome) not in p.resolved_actions:raise ValueError("corrected old outcome is not projected")
                if event.old_outcome==event.corrected_outcome or event.corrected_outcome not in {"++","+-","-+","--"}:raise ValueError("invalid corrected outcome")
                d=event.applied_effect;interfaces=(p.interfaces-set(d.remove_interfaces))|set(d.add_interfaces);facts=(p.facts-set(d.remove_facts))|set(d.add_facts)
                resolved=(set(p.resolved_actions)-{(event.action_id,event.old_outcome)})|{(event.action_id,event.corrected_outcome)}
                p=Projection(p.graph_digest,event.state_after_id,frozenset(interfaces),frozenset(facts),p.sunk_cost,frozenset(resolved),p.event_ids+(event.event_id,))
            else:
                if event.graph_before_digest!=p.graph_digest:raise ValueError("resolution graph mismatch")
                if event.state_before_id!=p.state_id:raise ValueError("resolution state-chain mismatch")
                if set(event.excluded_outcomes)|{event.selected_outcome}!={"++","+-","-+","--"}:raise ValueError("outcome partition is not exhaustive")
                if event.selected_outcome in event.excluded_outcomes:raise ValueError("selected outcome is excluded")
                d=event.applied_effect
                interfaces=(p.interfaces-set(d.remove_interfaces))|set(d.add_interfaces)
                facts=(p.facts-set(d.remove_facts))|set(d.add_facts)
                p=Projection(p.graph_digest,event.state_after_id,frozenset(interfaces),frozenset(facts),p.sunk_cost+event.execution_cost,p.resolved_actions|{(event.action_id,event.selected_outcome)},p.event_ids+(event.event_id,))
        return p
    def append(self,event:Event)->EventLog:
        # Full replay validates hash-chain continuity before admitting the event.
        EventLog(self.initial_graph_digest,self.initial_state_id,self.events+(event,),self.initial_interfaces,self.initial_facts,self.initial_sunk_cost,self.initial_resolved_actions,self.initial_event_ids).project()
        return EventLog(self.initial_graph_digest,self.initial_state_id,self.events+(event,),self.initial_interfaces,self.initial_facts,self.initial_sunk_cost,self.initial_resolved_actions,self.initial_event_ids)
    def metric_snapshot(self,metric:Callable[[Projection],Mapping[str,float]],through:int|None=None)->dict[str,float]:
        return dict(metric(self.project(through)))
    def metric_delta(self,metric:Callable[[Projection],Mapping[str,float]],before:int,after:int)->dict[str,float]:
        left=self.metric_snapshot(metric,before);right=self.metric_snapshot(metric,after)
        return {key:right.get(key,0.0)-left.get(key,0.0) for key in left.keys()|right.keys()}
    def metric_percent_delta(self,metric:Callable[[Projection],Mapping[str,float]],before:int,after:int)->dict[str,float|None]:
        """Percentage change from the previous snapshot; zero bases are explicitly undefined."""
        left=self.metric_snapshot(metric,before);right=self.metric_snapshot(metric,after)
        return {key:(100.0*(right.get(key,0.0)-left.get(key,0.0))/left[key] if left.get(key,0.0)!=0 else None) for key in left.keys()|right.keys()}
