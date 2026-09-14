"""Deterministic conjecture-net metrics derived from an explicit graph/state snapshot."""
from __future__ import annotations
from dataclasses import dataclass,replace
from math import log2

@dataclass(frozen=True)
class MetricAction:
    name:str
    dependencies:frozenset[str]=frozenset()
    requires:frozenset[str]=frozenset()
    outcome_domain:frozenset[str]=frozenset({'++','+-','-+','--'})
    status:str='active'  # active, resolved, pruned
    terminal:bool=False

@dataclass(frozen=True)
class MetricGraph:
    actions:tuple[MetricAction,...]
    interfaces:frozenset[str]=frozenset()
    coherence_constraints:tuple[frozenset[str],...]=()
    def validate(self)->None:
        amap={a.name:a for a in self.actions}
        if len(amap)!=len(self.actions):raise ValueError('duplicate action')
        if any(a.status not in {'active','resolved','pruned'} for a in self.actions):raise ValueError('invalid status')
        if any(not a.outcome_domain or not a.outcome_domain<={'++','+-','-+','--'} for a in self.actions):raise ValueError('invalid outcome domain')
        if any(not a.dependencies<=set(amap) for a in self.actions):raise ValueError('unknown dependency')
        if any(not c<=set(amap) for c in self.coherence_constraints):raise ValueError('unknown coherence action')
        visiting=set();done=set()
        def visit(n):
            if n in visiting:raise ValueError('dependency cycle')
            if n not in done:
                visiting.add(n)
                for d in amap[n].dependencies:visit(d)
                visiting.remove(n);done.add(n)
        for n in amap:visit(n)
    def metrics(self)->dict[str,float]:
        self.validate();amap={a.name:a for a in self.actions};active=[a for a in self.actions if a.status=='active']
        frontier=[a for a in active if a.requires<=self.interfaces and all(amap[d].status=='resolved' for d in a.dependencies)]
        missing={x for a in active for x in a.requires-self.interfaces}
        unresolved={a.name for a in active}
        burden=sum(bool(c&unresolved) for c in self.coherence_constraints)
        entropy=sum(log2(len(a.outcome_domain)) for a in active)
        # Shortest directed action count from an executable frontier node to an active terminal.
        successors={n:set() for n in amap}
        for a in self.actions:
            for d in a.dependencies:successors[d].add(a.name)
        distances=[]
        for start in (a.name for a in frontier):
            queue=[(start,1)];seen=set()
            while queue:
                n,k=queue.pop(0)
                if n in seen:continue
                seen.add(n)
                if amap[n].terminal and amap[n].status=='active':distances.append(k);break
                queue.extend((z,k+1) for z in successors[n] if amap[z].status=='active')
        return {'active_action_count':float(len(active)),'frontier_width':float(len(frontier)),'interface_deficit':float(len(missing)),'coherence_burden':float(burden),'formal_outcome_entropy_bits':float(entropy),'minimum_declared_terminal_depth':float(min(distances)) if distances else 0.0}

def percent_change(before:dict[str,float],after:dict[str,float])->dict[str,float|None]:
    if before.keys()!=after.keys():raise ValueError('metric keys differ')
    return {k:(100*(after[k]-before[k])/before[k] if before[k]!=0 else None) for k in before}
