"""Joint path/cycle tests for four-valued signed conjecture arrows."""
from __future__ import annotations
from dataclasses import dataclass
from math import log2
from typing import Mapping

OUTCOMES=frozenset({'++','+-','-+','--'})

def compose_word(word:tuple[str,...])->str:
    """Compose E_ab arrows, rejecting mismatched adjacent ports."""
    if not word or any(x not in OUTCOMES for x in word):raise ValueError('invalid arrow word')
    for left,right in zip(word,word[1:]):
        if left[1]!=right[0]:raise ValueError('ill-typed arrow composition')
    return word[0][0]+word[-1][1]

@dataclass(frozen=True)
class ArrowPath:
    name:str
    arrows:tuple[str,...]

@dataclass(frozen=True)
class CompositeArrowTest:
    name:str
    paths:tuple[ArrowPath,...]
    individual_costs:Mapping[str,float]
    joint_cost:float
    outcome_probabilities:tuple[float,...]=(0.25,0.25,0.25,0.25)
    def validate(self)->None:
        if len(self.paths)<2:raise ValueError('need alternative paths')
        if self.joint_cost<=0:raise ValueError('joint cost must be positive')
        names=[p.name for p in self.paths]
        if len(names)!=len(set(names)):raise ValueError('duplicate path name')
        arrows={a for p in self.paths for a in p.arrows}
        if arrows-set(self.individual_costs):raise ValueError('missing individual arrow cost')
        if any(self.individual_costs[a]<=0 for a in arrows):raise ValueError('individual costs must be positive')
        if len(self.outcome_probabilities)!=4 or abs(sum(self.outcome_probabilities)-1)>1e-12 or any(p<0 for p in self.outcome_probabilities):raise ValueError('invalid four-way probabilities')
    def evaluate(self,observed:Mapping[str,str])->dict[str,object]:
        self.validate();needed={a for p in self.paths for a in p.arrows}
        if needed-set(observed):return {'status':'incomplete','missing':sorted(needed-set(observed))}
        composites={p.name:compose_word(tuple(observed[a] for a in p.arrows)) for p in self.paths}
        coherent=len(set(composites.values()))==1
        return {'status':'pass' if coherent else 'fail','composites':composites,'suspect_arrows':[] if coherent else sorted(needed)}
    def information_per_cost(self)->float:
        """Prospective entropy touched per joint cost; not a calibrated posterior gain."""
        self.validate();entropy=-sum(p*log2(p) for p in self.outcome_probabilities if p)
        unique={a for p in self.paths for a in p.arrows}
        return entropy*len(unique)/self.joint_cost
    def cost_reduction_percent(self)->float:
        self.validate();separate=sum(self.individual_costs[a] for a in {x for p in self.paths for x in p.arrows})
        return 100*(self.joint_cost-separate)/separate
