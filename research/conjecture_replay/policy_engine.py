"""Guarded, provenance-preserving path engine for frozen conjecture quivers."""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,json,math

@dataclass(frozen=True)
class Step:
    action:str; outcome:str; target:str

@dataclass(frozen=True)
class ResolutionPath:
    steps:tuple[Step,...]
    terminal:str
    @property
    def actions(self): return tuple(s.action for s in self.steps if s.action!='O')
    @property
    def outcomes(self): return tuple(s.outcome for s in self.steps if s.action!='O')
    @property
    def provenance_id(self):
        raw=json.dumps([(s.action,s.outcome,s.target) for s in self.steps],separators=(',',':'))
        return hashlib.sha256(raw.encode()).hexdigest()

def enumerate_paths(adjacency:dict,origin='O'):
    found=[]
    def walk(node,used,steps):
        if node.startswith('T_'):
            found.append(ResolutionPath(tuple(steps),node));return
        for outcome,targets in adjacency[node].items():
            for target in targets:
                if target not in used:
                    walk(target,used|{target},steps+[Step(node,outcome,target)])
    walk(origin,{origin},[]);return found

def evaluate(path,costs,probabilities):
    actions=path.actions;outcomes=path.outcomes
    probability=math.prod(probabilities[a][o] for a,o in zip(actions,outcomes))
    return {'provenance_id':path.provenance_id,'terminal':path.terminal,
      'word':[f'{a}:{o}' for a,o in zip(actions,outcomes)],'cost':sum(costs[a] for a in actions),
      'outcome_probability':probability,'surprisal_bits':-math.log2(probability) if probability else math.inf,
      'action_count':len(actions)}

def pareto(rows,axes):
    """axes maps field to 'min' or 'max'; preserve provenance-distinct ties."""
    def dominates(a,b):
        weak=all(a[k]<=b[k] if d=='min' else a[k]>=b[k] for k,d in axes.items())
        strict=any(a[k]<b[k] if d=='min' else a[k]>b[k] for k,d in axes.items())
        return weak and strict
    return [r for r in rows if not any(dominates(q,r) for q in rows)]
