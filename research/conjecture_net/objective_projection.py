"""Objective-indexed recommendation projections over immutable action assessments."""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class ObjectiveKind(Enum):
    SCIENTIFIC_TARGET="scientific_target"
    INTERFACE_CONSTRUCTION="interface_construction"
    FALSIFICATION="falsification"
    COST="cost"
    INFORMATION="information"
    ROBUSTNESS="robustness"
    PROOF_QUALITY="proof_quality"
    GRAPH_MAINTENANCE="graph_maintenance"
    PORTFOLIO="portfolio"

@dataclass(frozen=True)
class Objective:
    name:str
    kind:ObjectiveKind
    target:str
    functional:str
    risk_attitude:str="neutral"
    budget:float|None=None
    horizon:int|None=None
    required_certificate:int=0

@dataclass(frozen=True)
class ActionAssessment:
    action:str
    reaches:frozenset[str]
    expected_cost:float
    worst_cost:float
    success_probability:float
    falsification_value:float=0.0
    information_gain:float=0.0
    robustness:float=0.0
    certificate_strength:int=0
    graph_repair_value:float=0.0

@dataclass(frozen=True)
class Recommendation:
    objective:str
    action:str|None
    reason:str


def recommend(objective:Objective,actions:list[ActionAssessment])->Recommendation:
    xs=[a for a in actions if objective.target in a.reaches and a.certificate_strength>=objective.required_certificate]
    if objective.budget is not None:xs=[a for a in xs if a.worst_cost<=objective.budget]
    if not xs:return Recommendation(objective.name,None,"no admissible action reaches the target under the declared constraints")
    keys={
      "reachability_then_expected_cost":lambda a:(a.success_probability,-a.expected_cost),
      "minimum_expected_cost":lambda a:(-a.expected_cost,a.success_probability),
      "minimum_worst_case_cost":lambda a:(-a.worst_cost,a.success_probability),
      "maximum_falsification_value":lambda a:(a.falsification_value,-a.expected_cost),
      "maximum_information_gain":lambda a:(a.information_gain,-a.expected_cost),
      "maximum_robustness":lambda a:(a.robustness,a.certificate_strength,-a.expected_cost),
      "maximum_certificate_strength":lambda a:(a.certificate_strength,a.robustness,-a.expected_cost),
      "maximum_graph_repair":lambda a:(a.graph_repair_value,-a.expected_cost),
    }
    if objective.functional not in keys:raise ValueError(f"unsupported objective functional: {objective.functional}")
    winner=max(xs,key=lambda a:(keys[objective.functional](a),a.action))
    return Recommendation(objective.name,winner.action,f"maximizes {objective.functional} among {len(xs)} admissible actions")
