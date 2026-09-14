"""Existential and forced wildcard-polarity analysis over signed arrow paths."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations,product
from typing import Mapping
from composite_arrow_tests import ArrowPath,OUTCOMES,compose_word

@dataclass(frozen=True)
class PathPolarityConstraint:
    path:str
    pattern:str
    def __post_init__(self):
        if len(self.pattern)!=2 or any(x not in '+-*' for x in self.pattern):raise ValueError('pattern must be two characters over +,-,*')
    def accepts(self,value:str)->bool:return all(w=='*' or w==v for w,v in zip(self.pattern,value))

@dataclass(frozen=True)
class PolarityExistenceProblem:
    paths:tuple[ArrowPath,...]
    constraints:tuple[PathPolarityConstraint,...]
    require_coherence:bool=False
    max_assignments:int=1_000_000
    def _counts(self,domains:Mapping[str,frozenset[str]])->tuple[int,int,list[dict[str,str]]]:
        pnames={p.name for p in self.paths};
        if any(c.path not in pnames for c in self.constraints):raise ValueError('constraint names unknown path')
        arrows=sorted({a for p in self.paths for a in p.arrows});ds=[domains.get(a,OUTCOMES) for a in arrows]
        if any(not d or not d<=OUTCOMES for d in ds):raise ValueError('invalid arrow domain')
        size=1
        for d in ds:size*=len(d)
        if size>self.max_assignments:raise ValueError('assignment bound exceeded')
        typed=sat=0;witness=[]
        for vals in product(*[sorted(d) for d in ds]):
            assignment=dict(zip(arrows,vals))
            try:comp={p.name:compose_word(tuple(assignment[a] for a in p.arrows)) for p in self.paths}
            except ValueError:continue
            if self.require_coherence and len(set(comp.values()))!=1:continue
            typed+=1
            if all(c.accepts(comp[c.path]) for c in self.constraints):
                sat+=1
                if len(witness)<2:witness.append({'assignment':assignment,'composites':comp})
        return typed,sat,witness
    def analyze(self,domains:Mapping[str,frozenset[str]])->dict[str,object]:
        typed,sat,witness=self._counts(domains)
        status='typing-impossible' if typed==0 else 'impossible' if sat==0 else 'forced' if sat==typed else 'possible'
        result={'status':status,'typed_assignments':typed,'satisfying_assignments':sat,'witnesses':witness}
        if status=='impossible':result['minimal_unsat_core']=self._minimal_unsat_core(domains)
        return result
    def _minimal_unsat_core(self,domains:Mapping[str,frozenset[str]])->list[str]:
        constrained=sorted(a for a,d in domains.items() if d!=OUTCOMES)
        for n in range(1,len(constrained)+1):
            for subset in combinations(constrained,n):
                trial={a:(domains[a] if a in subset else OUTCOMES) for a in constrained}
                typed,sat,_=self._counts(trial)
                if typed and not sat:return list(subset)
        return constrained
