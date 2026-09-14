"""Dependency-derived centrality metrics for planner interfaces."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations

@dataclass(frozen=True)
class InterfaceAction:
    name:str
    requires:frozenset[str]
    adds:frozenset[str]
    cost:float

@dataclass(frozen=True)
class InterfaceScore:
    interface:str
    immediate_unlocks:int
    closure_unlocks:int
    target_reachable:bool
    target_critical:bool
    cost:float
    score:float

def closure(actions:list[InterfaceAction],initial:frozenset[str])->tuple[frozenset[str],frozenset[str]]:
 interfaces=set(initial);used=set();changed=True
 while changed:
  changed=False
  for a in actions:
   if a.name not in used and a.requires<=interfaces:
    used.add(a.name);interfaces.update(a.adds);changed=True
 return frozenset(interfaces),frozenset(used)

def shapley_interface_values(actions:list[InterfaceAction],current:frozenset[str],target:str,candidates:tuple[str,...])->dict[str,float]:
    """Allocate complementary unlock value across candidate interfaces."""
    values={x:0.0 for x in candidates};orders=list(permutations(candidates))
    def utility(seed:frozenset[str])->float:
        interfaces,used=closure(actions,current|seed)
        return float(len(used)+5*int(target in interfaces))
    for order in orders:
        seed=frozenset()
        for interface in order:
            before=utility(seed);seed=seed|{interface};values[interface]+=utility(seed)-before
    return {x:v/len(orders) for x,v in values.items()}

def score_interfaces(actions:list[InterfaceAction],current:frozenset[str],target:str,candidate_costs:dict[str,float])->list[InterfaceScore]:
 base_i,base_a=closure(actions,current);scores=[]
 for interface,cost in candidate_costs.items():
  immediate=sum(a.requires<=current|{interface} and not a.requires<=current for a in actions)
  full_i,full_a=closure(actions,current|{interface});reachable=target in full_i
  # Critical means target is lost when this candidate interface is removed from its augmented closure seed.
  without_i,_=closure(actions,current-{interface});critical=reachable and target not in without_i
  gain=len(full_a-base_a);value=immediate+gain+5*int(reachable)+5*int(critical)
  scores.append(InterfaceScore(interface,immediate,gain,reachable,critical,cost,value/max(cost,1e-12)))
 return sorted(scores,key=lambda x:(x.score,x.interface),reverse=True)
