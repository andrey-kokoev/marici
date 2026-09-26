"""Finite resource-indexed rule data, interpreted by the unchanged resolution net."""
from dataclasses import dataclass
from reference import Package,Admission,Rule,Step,unit

@dataclass(frozen=True)
class World:
    owned: frozenset[str]
    spent: frozenset[str] = frozenset()

    def __post_init__(self):
        if type(self.owned) is not frozenset or type(self.spent) is not frozenset:
            raise ValueError('immutable resource sets required')
        if not all(type(x) is str and x for x in self.owned) or not self.spent<=self.owned:
            raise ValueError('invalid resource world')

    def package(self):
        return Package('resource-world',tuple('owned:'+x for x in sorted(self.owned))+
                       tuple('spent:'+x for x in sorted(self.spent)))

    @staticmethod
    def decode(package):
        if package.name!='resource-world':raise ValueError('not a resource-world package')
        if any(not (x.startswith('owned:') or x.startswith('spent:')) for x in package.data):
            raise ValueError('unknown resource field')
        result=World(frozenset(x[6:] for x in package.data if x.startswith('owned:')),
                     frozenset(x[6:] for x in package.data if x.startswith('spent:')))
        if result.package()!=package:raise ValueError('noncanonical resource world')
        return result

def seed(resources,witness):
    return unit(Admission(World(frozenset(resources)).package(),witness))

def consume(history,ticket):
    world=World.decode(history.package)
    if ticket not in world.owned-world.spent:raise ValueError('resource unavailable')
    target=World(world.owned,world.spent|{ticket})
    rule=Rule('consume',(world.package(),),target.package(),'consume:'+ticket)
    return Step(rule,(history,))

def join(left,right):
    a,b=World.decode(left.package),World.decode(right.package)
    if a.owned & b.owned:raise ValueError('overlapping resource footprints')
    target=World(a.owned|b.owned,a.spent|b.spent)
    return Step(Rule('disjoint-join',(a.package(),b.package()),target.package(),'disjoint-owned-union'),(left,right))

def validate_history(history):
    """Domain admission must validate transitions, not just endpoint typing."""
    from reference import Seed
    if isinstance(history,Seed):
        if type(history.evidence) is not Admission:raise ValueError('expect a flattened history')
        world=World.decode(history.package)
        if world.spent:raise ValueError('initial witness cannot pre-spend resources')
        return world
    inputs=[validate_history(h) for h in history.premises]
    target=World.decode(history.package);rule=history.rule
    if rule.name=='consume' and len(inputs)==1 and rule.witness.startswith('consume:'):
        token=rule.witness[len('consume:'):];old=inputs[0]
        if token not in old.owned-old.spent or target!=World(old.owned,old.spent|{token}):
            raise ValueError('invalid consumption transition')
    elif rule.name=='disjoint-join' and len(inputs)==2 and rule.witness=='disjoint-owned-union':
        a,b=inputs
        if a.owned & b.owned or target!=World(a.owned|b.owned,a.spent|b.spent):
            raise ValueError('invalid separation transition')
    else:raise ValueError('rule is not in the resource signature')
    return target
