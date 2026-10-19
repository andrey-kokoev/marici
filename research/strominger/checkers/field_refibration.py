"""Candidate lossless field decoration of the existing two-block slot generator.

Four state payloads are source-vertex fibers (three outgoing triples each).
Reference choice and same-kind comparison are declared policies, not derived.
No scalar contraction, new field components, metric or numerical DG legs.
"""
from dataclasses import dataclass

EDGES=tuple((a,b) for a in range(4) for b in range(4) if a!=b)
@dataclass(frozen=True)
class Slot:
    branch: str
    parents: tuple
    source: tuple
    target: tuple
    payloads: tuple

@dataclass(frozen=True)
class Foliation:
    reference: tuple
    slots: tuple

def encode(field,reference,owner):
    if set(field)!=set(EDGES) or any(len(v)!=3 for v in field.values()):
        raise ValueError('Expected twelve endpoint-labelled triples')
    if reference not in EDGES: raise ValueError('Reference must be an existing directed edge')
    field={edge:tuple(field[edge]) for edge in EDGES}
    selected=tuple(edge for edge in EDGES if edge!=reference)
    state={a:tuple((edge,field[edge]) for edge in EDGES if edge[0]==a) for a in range(4)}
    Record=owner['Record']
    initial=owner['Packet'](0,{'reference':reference,'state_policy':'source-fibers'},
        {'arrow':{(i,):Record((a,),(b,)) for i,(a,b) in enumerate(selected)},
         'state':{(i,):Record((i,),(i,)) for i in range(4)}},{})
    generated=owner['advance'](initial)
    slots=[]
    for branch,rows in generated.blocks.items():
        for _,row in sorted(rows.items()):
            left,right=(parent[0] for parent in row.parents)
            if branch=='arrow':
                parents=(selected[left],selected[right])
                payloads=tuple(((edge,field[edge]),) for edge in parents)
            else:
                parents=(left,right);payloads=(state[left],state[right])
            slots.append(Slot(branch,parents,row.source,row.target,payloads))
    return Foliation(reference,tuple(slots))

def recover(packet,owner):
    if not isinstance(packet,Foliation):raise ValueError('Expected a field foliation')
    field={}
    for slot in packet.slots:
        for bundle in slot.payloads:
            for edge,value in bundle:
                if edge in field and field[edge]!=value:raise ValueError('Inconsistent repeated field occurrence')
                field[edge]=value
    # Reconstruct solely from comparison payloads, not a hidden original-field copy.
    if packet!=encode(field,packet.reference,owner):raise ValueError('Slot, endpoint, parent, reference or policy drift')
    return field

def present(packet,phase):
    if phase=='raw':return packet.slots
    if phase not in ('source','target'):raise ValueError('Unknown presentation')
    grouped={}
    for slot in packet.slots:
        key=(slot.branch,getattr(slot,phase))
        grouped.setdefault(key,[]).append(slot)
    return {key:tuple(rows) for key,rows in grouped.items()}

def unpresent(view,phase):
    if phase=='raw':return tuple(view)
    if phase not in ('source','target'):raise ValueError('Unknown presentation')
    for key,rows in view.items():
        if any((s.branch,getattr(s,phase))!=key for s in rows):raise ValueError('Wrong family key')
    return tuple(sorted((slot for rows in view.values() for slot in rows),key=lambda s:(s.branch,s.parents)))

def relabel(packet,permutation,vector_action=lambda v:v):
    """Independent action on each retained occurrence; no decode/re-encode shortcut."""
    if sorted(permutation)!=list(range(4)):raise ValueError('Not a vertex permutation')
    edge_map=lambda edge:tuple(permutation[i] for i in edge)
    slots=[]
    for slot in packet.slots:
        parents=tuple(edge_map(e) for e in slot.parents) if slot.branch=='arrow' else tuple(permutation[a] for a in slot.parents)
        payloads=tuple(tuple(sorted((edge_map(edge),tuple(vector_action(value))) for edge,value in bundle)) for bundle in slot.payloads)
        slots.append(Slot(slot.branch,parents,edge_map(slot.source),edge_map(slot.target),payloads))
    return Foliation(edge_map(packet.reference),tuple(sorted(slots,key=lambda s:(s.branch,s.parents))))
