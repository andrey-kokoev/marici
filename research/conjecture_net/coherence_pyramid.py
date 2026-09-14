"""Layered coherence filtering and cheapest survivor-separating query selection."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from math import log2
from typing import Mapping
from composite_arrow_tests import ArrowPath,OUTCOMES,compose_word

@dataclass(frozen=True)
class TypedArrow:
    name:str;domain:str;codomain:str;cost:float

@dataclass(frozen=True)
class PathPattern:
    path:str;pattern:str

@dataclass(frozen=True)
class CoherenceLayer:
    name:str
    equal_paths:tuple[tuple[str,str],...]=()
    patterns:tuple[PathPattern,...]=()
    arrow_domains:tuple[tuple[str,frozenset[str]],...]=()

@dataclass(frozen=True)
class CoherencePyramid:
    arrows:tuple[TypedArrow,...]
    paths:tuple[ArrowPath,...]
    layers:tuple[CoherenceLayer,...]
    max_assignments:int=1_000_000
    def validate(self)->None:
        amap={a.name:a for a in self.arrows};pmap={p.name:p for p in self.paths}
        if len(amap)!=len(self.arrows) or len(pmap)!=len(self.paths):raise ValueError('duplicate names')
        for a in self.arrows:
            if a.cost<=0:raise ValueError('cost must be positive')
        for p in self.paths:
            if not p.arrows or any(x not in amap for x in p.arrows):raise ValueError('unknown path arrow')
            for x,y in zip(p.arrows,p.arrows[1:]):
                if amap[x].codomain!=amap[y].domain:raise ValueError('object-level path type mismatch')
        for layer in self.layers:
            if any(x not in pmap or y not in pmap for x,y in layer.equal_paths):raise ValueError('unknown equality path')
            if any(x.path not in pmap or len(x.pattern)!=2 or any(c not in '+-*' for c in x.pattern) for x in layer.patterns):raise ValueError('bad path pattern')
            domain_names=[x for x,_ in layer.arrow_domains]
            if len(domain_names)!=len(set(domain_names)):raise ValueError('duplicate arrow domain in layer')
            if any(x not in amap or not d or not d<=OUTCOMES for x,d in layer.arrow_domains):raise ValueError('bad arrow domain')
    def run(self)->dict[str,object]:
        self.validate();names=[a.name for a in self.arrows];size=4**len(names)
        if size>self.max_assignments:raise ValueError('assignment bound exceeded')
        survivors=[dict(zip(names,v)) for v in product(sorted(OUTCOMES),repeat=len(names))];rows=[]
        for layer in self.layers:
            before=len(survivors);kept=[]
            domains=dict(layer.arrow_domains)
            for assignment in survivors:
                if any(assignment[a] not in d for a,d in domains.items()):continue
                try:comp={p.name:compose_word(tuple(assignment[x] for x in p.arrows)) for p in self.paths}
                except ValueError:continue
                if any(comp[a]!=comp[b] for a,b in layer.equal_paths):continue
                if any(not all(w=='*' or w==v for w,v in zip(c.pattern,comp[c.path])) for c in layer.patterns):continue
                kept.append(assignment)
            survivors=kept;rows.append({'layer':layer.name,'before':before,'after':len(kept),'marginal_pruning_percent':None if before==0 else 100*(len(kept)-before)/before})
        return {'initial_assignments':size,'layers':rows,'survivor_count':len(survivors),'best_query':self._best_query(survivors)}
    def _best_query(self,survivors:list[dict[str,str]])->dict[str,object]|None:
        if not survivors:return None
        best=None
        for arrow in self.arrows:
            counts={o:sum(x[arrow.name]==o for x in survivors) for o in OUTCOMES};n=len(survivors)
            entropy=-sum((c/n)*log2(c/n) for c in counts.values() if c)
            row={'arrow':arrow.name,'entropy_bits':entropy,'cost':arrow.cost,'bits_per_cost':entropy/arrow.cost,'partition':counts}
            if best is None or row['bits_per_cost']>best['bits_per_cost']:best=row
        return best
