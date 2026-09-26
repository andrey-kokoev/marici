"""Theory-neutral finite dependent Sigma/Pi normalization.
Branches retain the instantiated dependencies of prior finite indices.
Leaves carry type labels; payloads are opaque. Universally quantified type
arguments are given in the companion proof, rather than encoded as Python.
"""
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Atom:
    type_label: str

@dataclass(frozen=True)
class Binder:
    kind: str
    branches: tuple
    def __post_init__(self):
        if self.kind not in ('Sigma','Pi'):raise ValueError('unknown binder')
        if not isinstance(self.branches,tuple):raise TypeError('tuple branches required')
        labels=[label for label,_ in self.branches]
        if len(set(labels))!=len(labels):raise ValueError('duplicate index')

@dataclass(frozen=True)
class Case:
    shape: object
    # Each position retains its entire source path and its leaf type.
    positions: tuple

@dataclass(frozen=True)
class Normal:
    source: object
    cases: tuple
    children: tuple
    rule: str


def normalize(tree,reverse_schedule=False):
    if isinstance(tree,Atom):
        return Normal(tree,(Case(None,(((),tree.type_label),)),),(),'atom')
    if not isinstance(tree,Binder):raise TypeError('Atom or Binder required')
    work=tree.branches[::-1] if reverse_schedule else tree.branches
    computed={label:normalize(child,reverse_schedule) for label,child in work}
    children=tuple((label,computed[label]) for label,_ in tree.branches)
    cases=[]
    if tree.kind=='Sigma':
        for label,child in children:
            for case in child.cases:
                positions=tuple((((tree.kind,label),)+path,typ) for path,typ in case.positions)
                cases.append(Case((label,case.shape),positions))
        rule='Sigma reassociation with retained index'
    else:
        for selection in product(*(child.cases for _,child in children)):
            shape=tuple((label,case.shape) for (label,_),case in zip(children,selection))
            positions=tuple((((tree.kind,label),)+path,typ)
                            for (label,_),case in zip(children,selection) for path,typ in case.positions)
            cases.append(Case(shape,positions))
        rule='dependent Pi-Sigma distributivity; positions are dependent sum'
    return Normal(tree,tuple(cases),children,rule)


def encode(normal,value):
    tree=normal.source
    if isinstance(tree,Atom):return None,(value,)
    if tree.kind=='Sigma':
        label,v=value
        choices=dict(normal.children)
        if label not in choices:raise ValueError('wrong dependent index')
        shape,values=encode(choices[label],v)
        return (label,shape),values
    if not isinstance(value,tuple) or len(value)!=len(normal.children):
        raise ValueError('wrong product arity')
    parts=[encode(child,v) for (_,child),v in zip(normal.children,value)]
    return (tuple((label,shape) for (label,_),(shape,_) in zip(normal.children,parts)),
            tuple(v for _,values in parts for v in values))


def case_for(normal,shape):
    for case in normal.cases:
        if case.shape==shape:return case
    raise ValueError('invalid dependent shape')


def decode(normal,shape,values):
    case=case_for(normal,shape)
    if len(values)!=len(case.positions):raise ValueError('wrong witness arity')
    if isinstance(normal.source,Atom):return values[0]
    if normal.source.kind=='Sigma':
        label,child_shape=shape
        return label,decode(dict(normal.children)[label],child_shape,values)
    result=[];offset=0
    for (label,child),(label2,child_shape) in zip(normal.children,shape):
        if label!=label2:raise ValueError('misaligned selection function')
        size=len(case_for(child,child_shape).positions)
        result.append(decode(child,child_shape,values[offset:offset+size]));offset+=size
    return tuple(result)


def as_expression(normal):
    """The normal form itself belongs to the same grammar.
    Original source and rule evidence remain in the Normal record.
    """
    return Binder('Sigma',tuple((case.shape,Binder('Pi',tuple((path,Atom(typ))
                   for path,typ in case.positions))) for case in normal.cases))
