"""Compact chart transitions without constructing a complete operator core.

A temporary normalized field representative (36 complex coordinates) is used.
The selected-spanning domain is explicit; no full-core fallback is hidden here.
"""
from dataclasses import dataclass,replace
from field_refibration import EDGES
from field_reconstruction import readout,positive_real
from reconstruction_aware_tower import verify_carrier,audit,present
from field_reference_transitions import rows_from_data
from reference_quadratic_fibers import constraints,fiber,validate_completion
from sharp_reference_packets import (Carrier,CompletionColumn,FiberCertificate,SharpPacket,SPAN_FAILURE)

class FullFallbackRequired(ValueError):
    pass

@dataclass(frozen=True)
class AnchorCertificate:
    strength_squared:object
    status:str

@dataclass(frozen=True)
class DirectPacket:
    carrier:Carrier
    certificate:FiberCertificate
    prior_probe_certificate:object
    completion:object
    anchor_certificate:object
    anchor_threshold_squared:object
    policy:str='direct-compact-charts-v1'

def _anchor_ok(anchor,field,reference,zero):
    if not isinstance(anchor,tuple) or len(anchor)!=2:raise ValueError('Invalid anchor label')
    e,j=anchor
    if e==reference or e not in field or type(j)!=int or j not in range(3):raise ValueError('Anchor is not a selected coordinate')
    if field[e][j]==zero:raise ValueError('Zero anchor; select another chart')

def choose_anchor(field,reference,rho,zero,strongest=True):
    choices=[(e,j) for e in EDGES if e!=reference for j in range(3) if field[e][j]!=zero]
    if not choices:raise FullFallbackRequired('No selected anchor; use the verified full fallback')
    best=choices[0]
    if strongest:
        strength=lambda key:field[key[0]][key[1]].flip(8)*field[key[0]][key[1]]/rho
        for candidate in choices[1:]:
            if positive_real(strength(candidate)-strength(best)):best=candidate
    return best

def _anchor_certificate(anchor,field,rho,threshold,zero):
    value=field[anchor[0]][anchor[1]];strength=value.flip(8)*value/rho
    status='above-threshold' if strength==threshold or positive_real(strength-threshold) else 'weak'
    return AnchorCertificate(strength,status)

def _fiber(data,context,column,zero,one):
    K,ops=context.matrices()
    try:selected,rows,values,desired=constraints(data,K,ops,zero,one)
    except ValueError as error:
        if str(error)==SPAN_FAILURE:raise FullFallbackRequired('Target selected span failed; retain the source and use the verified full fallback') from error
        raise
    witness=None
    if column is not None:
        field=selected['representative'];reference=data['P']['reference']
        key=(column.anchor_edge,column.anchor_component);_anchor_ok(key,field,reference,zero)
        if len(column.values)!=3:raise ValueError('Wrong completion-column size')
        divisor=field[key[0]][key[1]].flip(8)
        witness=tuple(selected['normalization_squared']*v/divisor for v in column.values)
    result=fiber(rows,values,desired,K,ops,zero,one,witness)
    certificate=FiberCertificate(result['kind'],result['linear_rank'],result['complex_nullity'],result['reason'])
    missing=result['solution'] if certificate.kind=='unique' else witness
    if missing is None:raise ValueError('Missing completion for a nonunique or unresolved fiber')
    completed=validate_completion(data,selected,missing,K,ops,zero)
    return certificate,completed

def decode(packet,context,owner,zero,one):
    if packet.policy!='direct-compact-charts-v1':raise ValueError('Unknown direct-chart policy')
    if not positive_real(packet.anchor_threshold_squared):raise ValueError('Nonpositive anchor diagnostic threshold')
    data=verify_carrier(packet.carrier,context,owner)
    certificate,(field,rho)=_fiber(data,context,packet.completion,zero,one)
    if certificate!=packet.certificate:raise ValueError('Direct fiber certificate drift')
    if (certificate.kind=='unique')!=(packet.completion is None):raise ValueError('Direct completion retention violation')
    if packet.completion is None:
        if packet.anchor_certificate is not None:raise ValueError('Unique packet has a spurious anchor certificate')
    else:
        key=(packet.completion.anchor_edge,packet.completion.anchor_component)
        expected=_anchor_certificate(key,field,rho,packet.anchor_threshold_squared,zero)
        if expected!=packet.anchor_certificate:raise ValueError('Anchor strength certificate drift')
    if audit(data,context,zero,one)!=packet.prior_probe_certificate:raise ValueError('Prior conditioning certificate drift')
    return field,rho,data

def from_sharp(sharp,context,owner,zero,one,threshold,strongest=True):
    if sharp.retention_policy!='exact-uniqueness-plus-completion-v1':raise ValueError('Unknown sharp retention policy')
    if sharp.full_operator_fallback:raise FullFallbackRequired('Source retains a full fallback; keep using that interface')
    data=verify_carrier(sharp.carrier,context,owner)
    certificate,(field,rho)=_fiber(data,context,sharp.completion,zero,one)
    if certificate!=sharp.certificate:raise ValueError('Sharp fiber certificate drift')
    info=None
    if sharp.completion is not None:
        key=(sharp.completion.anchor_edge,sharp.completion.anchor_component)
        if key!=choose_anchor(field,sharp.carrier.reference,rho,zero,False):raise ValueError('Noncanonical incoming SharpPacket anchor')
        info=_anchor_certificate(key,field,rho,threshold,zero)
    packet=DirectPacket(sharp.carrier,certificate,sharp.prior_probe_certificate,sharp.completion,info,threshold)
    decode(packet,context,owner,zero,one)
    return reanchor(packet,choose_anchor(field,sharp.carrier.reference,rho,zero),context,owner,zero,one) if strongest and packet.completion else packet

def to_sharp(packet,context,owner,zero,one):
    field,rho,_=decode(packet,context,owner,zero,one)
    column=None
    if packet.completion:
        e,j=choose_anchor(field,packet.carrier.reference,rho,zero,False)
        column=CompletionColumn(e,j,tuple(field[packet.carrier.reference][i]*field[e][j].flip(8)/rho for i in range(3)))
    return SharpPacket(packet.carrier,packet.certificate,packet.prior_probe_certificate,column)

def reanchor(packet,target,context,owner,zero,one):
    field,rho,_=decode(packet,context,owner,zero,one)
    if packet.completion is None:raise ValueError('Unique packet needs no completion anchor')
    _anchor_ok(target,field,packet.carrier.reference,zero)
    old=packet.completion
    ratio=field[target[0]][target[1]].flip(8)/field[old.anchor_edge][old.anchor_component].flip(8)
    column=CompletionColumn(target[0],target[1],tuple(value*ratio for value in old.values))
    info=_anchor_certificate(target,field,rho,packet.anchor_threshold_squared,zero)
    return replace(packet,completion=column,anchor_certificate=info)

def change_reference(packet,reference,context,owner,zero,one,target_anchor=None):
    if reference not in EDGES:raise ValueError('Invalid target reference')
    field,rho,_=decode(packet,context,owner,zero,one)
    K,ops=context.matrices();data=readout(field,K,ops,reference,zero)
    for channel in data.values():
        for branch,matrix in channel['blocks'].items():
            channel['blocks'][branch]=tuple(tuple(value/rho for value in row) for row in matrix)
    # This provisional column is just three products, not a 144-block core.
    key=choose_anchor(field,reference,rho,zero) if target_anchor is None else target_anchor
    _anchor_ok(key,field,reference,zero)
    column=CompletionColumn(key[0],key[1],tuple(field[reference][i]*field[key[0]][key[1]].flip(8)/rho for i in range(3)))
    certificate,_=_fiber(data,context,column,zero,one)
    if certificate.kind=='unique':
        if target_anchor is not None:raise ValueError('Unique target needs no completion anchor')
        column=None;info=None
    else:info=_anchor_certificate(key,field,rho,packet.anchor_threshold_squared,zero)
    rows=rows_from_data(data,owner['Row'])
    if packet.carrier.rung<10:
        for depth in (1,2):rows=owner['incoming_promotion'](rows,depth,packet.carrier.policy)
    carrier=replace(packet.carrier,reference=reference,view=present(rows,packet.carrier.rung,owner))
    return DirectPacket(carrier,certificate,audit(data,context,zero,one),column,info,packet.anchor_threshold_squared)

def transport(packet,operation,context,owner,zero,one):
    """Lift an existing retained-carrier map; its resulting carrier is validated."""
    decode(packet,context,owner,zero,one)
    carrier=operation(packet.carrier,owner)
    moved=replace(packet,carrier=carrier)
    decode(moved,context,owner,zero,one)
    return moved
