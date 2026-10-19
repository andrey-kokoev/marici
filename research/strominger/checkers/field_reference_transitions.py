"""Reference changes through the complete unanchored operator core.

No original field, phase anchor, physical d, or fixed-2x2 binding is accepted.
The scalar-only subinterface is partial; certified packets plus their required
operator fallback form the total interface on the validated packet domain.
"""
from dataclasses import dataclass, replace
from field_refibration import EDGES
from field_reconstruction import reconstruct, readout
from reconstruction_aware_tower import (audit,verify,operator_packet,recover_operator_packet,
                                        present,data_from_leaves)

@dataclass(frozen=True)
class Change:
    source: object
    target: object
    source_route: str
    target_obligation: str

def operator_core(packet,context,owner,zero,one):
    data=verify(packet,context,owner,zero,one)
    if packet.operator_fallback:return packet.operator_fallback,'retained-operator-data'
    K,ops=context.matrices();decoded=reconstruct(data,K,ops,zero,one)
    rho=decoded['normalization_squared']
    blocks=tuple((key,tuple(tuple(value/rho for value in row) for row in matrix))
                 for key,matrix in operator_packet(decoded['representative']))
    return blocks,'scalar-reconstruction'

def rows_from_data(data,Row):
    reference=data['P']['reference'];selected=tuple(e for e in EDGES if e!=reference);rows=[]
    for branch,tag,vertices in (('arrow','a',selected),('state','s',tuple((i,i) for i in range(4)))):
        for i,e in enumerate(vertices):
            for j,f in enumerate(vertices):
                value=(tuple(data[name]['blocks'][branch][i][j] for name in ('P','Q','C')),)
                rows.append(Row(('leaf',len(rows)),(tag,e[0],f[0]),(tag,e[1],f[1]),value))
    rows=tuple(rows)
    if data_from_leaves(rows,reference)!=data:raise ValueError('Noncanonical comparison data')
    return rows

def change_reference(packet,reference,context,owner,zero,one):
    if reference not in EDGES:raise ValueError('Invalid target reference')
    blocks,route=operator_core(packet,context,owner,zero,one)
    representative,rho=recover_operator_packet(blocks,zero,one)
    K,ops=context.matrices();data=readout(representative,K,ops,reference,zero)
    # Quadratic comparisons normalize by rho; no square root or phase choice.
    for channel in data.values():
        for branch,matrix in channel['blocks'].items():
            channel['blocks'][branch]=tuple(tuple(value/rho for value in row) for row in matrix)
    certificate=audit(data,context,zero,one)
    fallback=blocks if certificate.status!='reconstructible' else ()
    rows=rows_from_data(data,owner['Row'])
    if packet.rung<10:
        for depth in (1,2):rows=owner['incoming_promotion'](rows,depth,packet.policy)
    target=replace(packet,reference=reference,certificate=certificate,operator_fallback=fallback,
                   view=present(rows,packet.rung,owner))
    # The original numerical route history is preserved. Reference-change
    # history is separate, in Change records, not inserted into that route type.
    verify(target,context,owner,zero,one)
    return Change(packet,target,route,'retain-144-operator-blocks' if fallback else 'scalar-packet-suffices')

def verify_change(change,context,owner,zero,one):
    expected=change_reference(change.source,change.target.reference,context,owner,zero,one)
    if change!=expected:raise ValueError('Reference transition or retention obligation drift')
    return change.target

def compose(changes,context,owner,zero,one):
    if not changes:raise ValueError('Empty transition path')
    for i,change in enumerate(changes):
        verify_change(change,context,owner,zero,one)
        if i and changes[i-1].target!=change.source:raise ValueError('Reference transition endpoints do not match')
    direct=change_reference(changes[0].source,changes[-1].target.reference,context,owner,zero,one)
    if direct.target!=changes[-1].target:raise ValueError('Reference cocycle failed')
    # Preserve the path rather than pretending a direct and composite history
    # are identical. Equality here is of their resulting complete packets.
    return direct,tuple(changes)
