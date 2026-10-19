"""Complete candidate slot tower for the field decoration, before numerical DG binding.

Six state presentations and three horizontal map roles. Histories stay distinct;
semantic route equality never identifies construction histories.
"""
from dataclasses import dataclass
from field_refibration import EDGES,Foliation,encode,recover,present,unpresent,relabel

PHASE={12:'raw',11:'source',10:'target',6:'raw',5:'source',4:'target'}
@dataclass(frozen=True)
class FieldNode:
    rung: int
    reference: tuple
    view: object
    history: tuple

def field_view(field,phase):
    if set(field)!=set(EDGES) or any(len(v)!=3 for v in field.values()):raise ValueError('Expected full field')
    rows=tuple((edge,tuple(field[edge])) for edge in EDGES)
    if phase=='raw':return rows
    if phase not in ('source','target'):raise ValueError('Unknown field phase')
    axis=0 if phase=='source' else 1
    return {vertex:tuple(row for row in rows if row[0][axis]==vertex) for vertex in range(4)}

def field_from_view(view,phase):
    rows=view if phase=='raw' else tuple(row for members in view.values() for row in members)
    field=dict(rows)
    if len(rows)!=12 or view!=field_view(field,phase):raise ValueError('Corrupt field presentation or key')
    return field

def make_node(field,reference,rung,owner,history=()):
    if rung not in PHASE or reference not in EDGES:raise ValueError('Invalid rung/reference')
    view=field_view(field,PHASE[rung]) if rung>=10 else present(encode(field,reference,owner),PHASE[rung])
    return FieldNode(rung,reference,view,tuple(history))

def packet_of(node,owner):
    if node.rung not in (6,5,4):raise ValueError('Not an output slot presentation')
    packet=Foliation(node.reference,unpresent(node.view,PHASE[node.rung]))
    recover(packet,owner)
    if node.view!=present(packet,PHASE[node.rung]):raise ValueError('Noncanonical slot presentation')
    return packet

def recover_field(node,owner):
    if node.rung not in PHASE or node.reference not in EDGES:raise ValueError('Invalid rung/reference')
    if node.rung>=10:return field_from_view(node.view,PHASE[node.rung])
    return recover(packet_of(node,owner),owner)

def vertical(node,owner):
    if node.rung not in (12,11,6,5):raise ValueError('No vertical successor here')
    recover_field(node,owner)
    phase=PHASE[node.rung-1]
    if node.rung>=10:view=field_view(field_from_view(node.view,PHASE[node.rung]),phase)
    else:view=present(packet_of(node,owner),phase)
    return FieldNode(node.rung-1,node.reference,view,node.history+(f'V{node.rung}-{node.rung-1}',))

def horizontal(node,owner):
    if node.rung not in (12,11,10):raise ValueError('Horizontal source must be 12,11,10')
    field=recover_field(node,owner)
    return FieldNode(node.rung-6,node.reference,present(encode(field,node.reference,owner),PHASE[node.rung-6]),node.history+(f'G{node.rung-3}',))

def semantic(node):return node.rung,node.reference,node.view

def geometric_action(node,permutation,vector_action,owner):
    """Geometric action on actual occurrences, independently of horizontal maps."""
    if node.rung>=10:
        moved={tuple(permutation[i] for i in edge):tuple(vector_action(v)) for edge,v in recover_field(node,owner).items()}
        view=field_view(moved,PHASE[node.rung])
    else:
        view=present(relabel(packet_of(node,owner),permutation,vector_action),PHASE[node.rung])
    return FieldNode(node.rung,tuple(permutation[i] for i in node.reference),view,node.history+('geometric-action',))

def induced_action(node,matrix,labels,permutation,zero,owner):
    """Explicit induced global action on the constrained image, NOT a local edge rule."""
    field=recover_field(node,owner)
    coordinates=[(tuple('ABCD'.index(c) for c in label.split(':')[0]),'xyz'.index(label.split(':')[1])) for label in labels]
    values=[field[edge][axis] for edge,axis in coordinates]
    moved=[zero for _ in values]
    for (i,j),coefficient in matrix.items():moved[i]=moved[i]+coefficient*values[j]
    output={edge:[None]*3 for edge in EDGES}
    for (edge,axis),value in zip(coordinates,moved):output[edge][axis]=value
    return make_node(output,tuple(permutation[i] for i in node.reference),node.rung,owner,node.history+('induced-field-action',))
