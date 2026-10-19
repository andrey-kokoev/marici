"""Exact-retention adapter; the old packet contract is expanded, never weakened."""
from dataclasses import dataclass
from field_refibration import EDGES
from reconstruction_aware_tower import Packet,Certificate,audit,verify,raw_rows,data_from_leaves,operator_packet
from field_reference_transitions import operator_core,change_reference
from reference_quadratic_fibers import constraints,fiber,validate_completion

@dataclass(frozen=True)
class Carrier:
    rung:int
    reference:tuple
    context:object
    policy:str
    view:object
    history:tuple

@dataclass(frozen=True)
class CompletionColumn:
    anchor_edge:tuple
    anchor_component:int
    values:tuple

@dataclass(frozen=True)
class FiberCertificate:
    kind:str
    linear_rank:int
    complex_nullity:int
    reason:str

@dataclass(frozen=True)
class SharpPacket:
    carrier:Carrier
    certificate:FiberCertificate
    prior_probe_certificate:object
    completion:object=None
    full_operator_fallback:tuple=()
    retention_policy:str='exact-uniqueness-plus-completion-v1'

SPAN_FAILURE='Selected arrow fields do not span three dimensions'
UNSUPPORTED=FiberCertificate('selected-span-fallback',-1,-1,SPAN_FAILURE)

def anchor(selected,zero):
    field=selected['representative']
    return next((e,i) for e in EDGES if e in field for i in range(3) if field[e][i]!=zero)

def column_from_core(core,reference,selected,zero):
    e,j=anchor(selected,zero);matrix=dict(core)[reference,e]
    return CompletionColumn(e,j,tuple(matrix[i][j] for i in range(3)))

def missing_from_column(column,selected,zero):
    if (column.anchor_edge,column.anchor_component)!=anchor(selected,zero) or len(column.values)!=3:
        raise ValueError('Completion-column anchor drift')
    divisor=selected['representative'][column.anchor_edge][column.anchor_component].flip(8)
    return tuple(selected['normalization_squared']*v/divisor for v in column.values)

def analyze(data,context,zero,one,column=None):
    K,ops=context.matrices();selected,rows,values,desired=constraints(data,K,ops,zero,one)
    witness=missing_from_column(column,selected,zero) if column is not None else None
    result=fiber(rows,values,desired,K,ops,zero,one,witness)
    certificate=FiberCertificate(result['kind'],result['linear_rank'],result['complex_nullity'],result['reason'])
    missing=result['solution'] if result['kind']=='unique' else witness
    completed=validate_completion(data,selected,missing,K,ops,zero) if missing is not None else None
    return certificate,completed,selected

def compact(packet,context,owner,zero,one):
    core,_=operator_core(packet,context,owner,zero,one)
    data=data_from_leaves(owner['leaves'](raw_rows(packet,owner)),packet.reference)
    carrier=Carrier(packet.rung,packet.reference,packet.context,packet.policy,packet.view,packet.history)
    K,ops=context.matrices()
    try:selected,_,_,_=constraints(data,K,ops,zero,one)
    except ValueError as error:
        if str(error)!=SPAN_FAILURE:raise
        return SharpPacket(carrier,UNSUPPORTED,packet.certificate,full_operator_fallback=core)
    column=column_from_core(core,packet.reference,selected,zero)
    certificate,_,_=analyze(data,context,zero,one,column)
    return SharpPacket(carrier,certificate,packet.certificate,None if certificate.kind=='unique' else column)

def expand(sharp,context,owner,zero,one):
    if sharp.retention_policy!='exact-uniqueness-plus-completion-v1':raise ValueError('Unknown sharp retention policy')
    c=sharp.carrier
    if c.context!=context:raise ValueError('Sharp packet context mismatch')
    data=data_from_leaves(owner['leaves'](raw_rows(c,owner)),c.reference)
    K,ops=context.matrices()
    try:certificate,completed,_=analyze(data,context,zero,one,sharp.completion)
    except ValueError as error:
        if str(error)!=SPAN_FAILURE:raise
        if sharp.certificate!=UNSUPPORTED or sharp.completion is not None or not sharp.full_operator_fallback:
            raise ValueError('Missing full fallback for selected-span failure')
        core=sharp.full_operator_fallback
    else:
        if certificate!=sharp.certificate:raise ValueError('Stale quadratic-fiber certificate')
        if sharp.full_operator_fallback:raise ValueError('Unneeded full fallback in sharp domain')
        if (certificate.kind=='unique')!=(sharp.completion is None):raise ValueError('Completion-column retention obligation violated')
        if completed is None:raise ValueError('Unresolved fiber has no retained completion')
        field,rho=completed
        core=tuple((key,tuple(tuple(v/rho for v in row) for row in matrix)) for key,matrix in operator_packet(field))
    old_certificate=audit(data,context,zero,one)
    if old_certificate!=sharp.prior_probe_certificate:raise ValueError('Prior conditioning certificate drift')
    fallback=core if old_certificate.status!='reconstructible' else ()
    packet=Packet(c.rung,c.reference,c.context,old_certificate,fallback,c.policy,c.view,c.history)
    verify(packet,context,owner,zero,one)
    return packet

def change_sharp_reference(sharp,reference,context,owner,zero,one):
    source=expand(sharp,context,owner,zero,one)
    changed=change_reference(source,reference,context,owner,zero,one)
    return compact(changed.target,context,owner,zero,one)
