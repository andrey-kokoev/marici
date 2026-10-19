"""Retained comparison transport with explicit reconstruction/fallback contracts.

Numeric family means are computed only AFTER leaf comparisons. Field families
retain occurrences; they never average fields before the quadratic readout.
"""
from dataclasses import dataclass, replace
from fractions import Fraction
from field_refibration import EDGES
from field_metric_comparisons import pairing
from field_reconstruction import readout, reconstruct, positive_real, solve

PHASE={12:'raw',11:'source',10:'target',6:'raw',5:'source',4:'target'}

@dataclass(frozen=True)
class Context:
    metric: tuple
    operators: tuple
    coframes: tuple
    source_provenance: tuple
    reference_margin_threshold_squared: object
    coordinates: str='existing-corner-coframes'
    tester_norm: str='Euclidean norm on the four P/Q reference equations'
    phase_policy: str='common phase is not anchored'

    def matrices(self):
        K={(i,j):v for i,row in enumerate(self.metric) for j,v in enumerate(row)}
        ops={name:{(i,j):v for i,row in enumerate(matrix) for j,v in enumerate(row)} for name,matrix in self.operators}
        return K,ops

@dataclass(frozen=True)
class FieldRow:
    label: tuple
    source: tuple
    target: tuple
    slot: object=None
    mass: int=1
    members: tuple=()

@dataclass(frozen=True)
class Certificate:
    status: str
    reason: str
    reference_margin_lower_squared: object=None
    reference_margin_upper_squared: object=None
    probe_ranks: tuple=()

@dataclass(frozen=True)
class Packet:
    rung: int
    reference: tuple
    context: Context
    certificate: Certificate
    operator_fallback: tuple
    policy: str
    view: object
    history: tuple=()

def field_rows(foliation):
    return tuple(FieldRow(('leaf',i),('a' if slot.branch=='arrow' else 's',)+slot.source,
                          ('a' if slot.branch=='arrow' else 's',)+slot.target,slot)
                 for i,slot in enumerate(foliation.slots))

def retain_field_families(rows,depth,policy):
    if policy not in ('inherited','common'):raise ValueError('Unknown retention policy')
    grouped={}
    for row in rows:grouped.setdefault(row.target,[]).append(row)
    return tuple(FieldRow((f'family:{depth}',i),('assembly',depth,i),
                          ('retained-key',depth,key) if policy=='inherited' else ('common-target',depth),
                          mass=sum(r.mass for r in members),members=tuple(members))
                 for i,(key,members) in enumerate(grouped.items()))

def observe_field_rows(rows,context,Row,mean,zero):
    K,ops=context.matrices();result=[]
    for row in rows:
        if row.members:
            children=observe_field_rows(row.members,context,Row,mean,zero)
            result.append(Row(row.label,row.source,row.target,mean(children),row.mass,children))
            continue
        if row.slot is None or row.mass!=1:raise ValueError('Missing field occurrence')
        slot=row.slot;left,right=slot.payloads
        values=[]
        for name in ('P','Q','C'):
            operator=ops[name];total=zero
            for edge,x in left:
                for other,y in right:
                    if slot.branch=='state' and edge[1]!=other[1]:continue
                    transformed=tuple(sum((operator[i,j]*x[j] for j in range(3)),zero) for i in range(3))
                    total+=pairing(y,transformed,K,zero)
            values.append(total)
        result.append(Row(row.label,row.source,row.target,(tuple(values),),1))
    return tuple(result)

def data_from_leaves(rows,reference):
    if reference not in EDGES:raise ValueError('Invalid directed reference')
    selected=tuple(e for e in EDGES if e!=reference);index=0
    data={name:{'reference':reference,'selected_edges':selected,'blocks':{}} for name in ('P','Q','C')}
    for branch,tag,vertices in (('arrow','a',selected),('state','s',tuple((a,a) for a in range(4)))):
        matrices={name:[] for name in data}
        for i,e in enumerate(vertices):
            lines={name:[] for name in data}
            for j,f in enumerate(vertices):
                if index>=len(rows):raise ValueError('Missing comparison leaves')
                row=rows[index]
                if (row.label,row.source,row.target,row.mass,row.members)!=(('leaf',index),(tag,e[0],f[0]),(tag,e[1],f[1]),1,()):
                    raise ValueError('Leaf label, parent endpoint, mass or membership drift')
                if len(row.value)!=1 or len(row.value[0])!=3:raise ValueError('Expected three comparison channels')
                for k,name in enumerate(data):lines[name].append(row.value[0][k])
                index+=1
            for name in data:matrices[name].append(tuple(lines[name]))
        for name in data:data[name]['blocks'][branch]=tuple(matrices[name])
    if index!=len(rows):raise ValueError('Extra comparison leaves')
    return data

def determinant3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def audit(data,context,zero,one):
    K,ops=context.matrices();threshold=context.reference_margin_threshold_squared
    if not positive_real(threshold):raise ValueError('Nonpositive diagnostic threshold')
    try:decoded=reconstruct(data,K,ops,zero,one)
    except ValueError as error:
        if str(error) not in ('Selected arrow fields do not span three dimensions','Reference probes do not span the missing field triple'):raise
        return Certificate('requires-retained-operator-data',str(error))
    field=decoded['representative'];rho=decoded['normalization_squared'];a,t=data['P']['reference']
    equations=[]
    for name in ('P','Q'):
        for b in range(4):
            if b in (a,t):continue
            equations.append(tuple(sum((field[b,t][i].flip(8)*K[i,k]*ops[name][k,j] for i in range(3) for k in range(3)),zero) for j in range(3)))
    N=tuple(tuple(sum((r[i].flip(8)*r[j] for r in equations),zero)/rho for j in range(3)) for i in range(3))
    metric=tuple(tuple(K[i,j] for j in range(3)) for i in range(3))
    columns=[solve(metric,tuple(N[i][j] for i in range(3)),zero) for j in range(3)]
    H=tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
    trace=sum((H[i][i] for i in range(3)),zero)
    lower=determinant3(H)/(trace*trace)
    upper=N[0][0]/K[0,0]
    for j in (1,2):
        candidate=N[j][j]/K[j,j]
        if positive_real(upper-candidate):upper=candidate
    if not positive_real(lower) or positive_real(lower-upper):raise ValueError('Invalid reference-margin bounds')
    if lower==threshold or positive_real(lower-threshold):status='reconstructible'
    elif positive_real(threshold-upper):status='reconstructible-weak-reference-probes'
    else:status='reconstructible-margin-unresolved'
    return Certificate(status,'Reference-equation margin only; not a full nonlinear inverse condition number',lower,upper,tuple(sorted(decoded['reference_probe_ranks'].items())))

def operator_packet(field):
    return tuple(((e,f),tuple(tuple(field[e][i]*field[f][j].flip(8) for j in range(3)) for i in range(3))) for e in EDGES for f in EDGES)

def recover_operator_packet(blocks,zero,one):
    if tuple(key for key,_ in blocks)!=tuple((e,f) for e in EDGES for f in EDGES):raise ValueError('Missing or mislabelled fallback blocks')
    B=dict(blocks)
    if any(len(m)!=3 or any(len(row)!=3 for row in m) for m in B.values()):raise ValueError('Wrong fallback matrix shape')
    pivot=next(((e,i) for e in EDGES for i in range(3) if B[e,e][i][i]!=zero),None)
    if pivot is None:
        field={e:(zero,zero,zero) for e in EDGES};rho=one
    else:
        e,j=pivot;rho=B[e,e][j][j]
        if not positive_real(rho):raise ValueError('Nonpositive fallback pivot')
        field={f:tuple(B[f,e][i][j] for i in range(3)) for f in EDGES}
    rebuilt=operator_packet(field)
    if any(v!=rho*B[key][i][j] for key,m in rebuilt for i,row in enumerate(m) for j,v in enumerate(row)):
        raise ValueError('Fallback is not a consistent rank-one outer-product packet')
    return field,rho

def raw_rows(packet,owner):
    if packet.rung not in PHASE:raise ValueError('Invalid rung')
    return packet.view if PHASE[packet.rung]=='raw' else owner['unindex'](packet.view)

def present(rows,rung,owner):
    return rows if PHASE[rung]=='raw' else owner['indexed'](rows,PHASE[rung])

def make_packet(rows,field,reference,context,policy,owner,zero,one):
    if policy not in ('inherited','common'):raise ValueError('Unknown retention policy')
    data=data_from_leaves(rows,reference);K,ops=context.matrices()
    if data!=readout(field,K,ops,reference,zero):raise ValueError('Field and leaf observations disagree')
    certificate=audit(data,context,zero,one)
    fallback=operator_packet(field) if certificate.status!='reconstructible' else ()
    return Packet(12,reference,context,certificate,fallback,policy,rows)

def vertical(packet,owner):
    if packet.rung not in (12,11,6,5):raise ValueError('No vertical successor')
    rung=packet.rung-1
    return replace(packet,rung=rung,view=present(raw_rows(packet,owner),rung,owner),history=packet.history+(f'V{packet.rung}-{rung}',))

def horizontal(packet,owner):
    if packet.rung not in (12,11,10):raise ValueError('Invalid horizontal source')
    rows=raw_rows(packet,owner)
    for depth in (1,2):rows=owner['incoming_promotion'](rows,depth,packet.policy)
    rung=packet.rung-6
    return replace(packet,rung=rung,view=present(rows,rung,owner),history=packet.history+(f'G{packet.rung-3}',))

def semantic(packet):return replace(packet,history=())

def verify_carrier(packet,expected_context,owner):
    if packet.context!=expected_context:raise ValueError('Metric, coframe, operator or policy provenance mismatch')
    if packet.policy not in ('inherited','common'):raise ValueError('Unknown retention policy')
    transitions={12:{'V12-11':11,'G9':6},11:{'V11-10':10,'G8':5},10:{'G7':4},6:{'V6-5':5},5:{'V5-4':4},4:{}}
    at=12
    for step in packet.history:
        if step not in transitions[at]:raise ValueError('Invalid retained route history')
        at=transitions[at][step]
    if at!=packet.rung:raise ValueError('Route history terminates at another rung')
    rows=raw_rows(packet,owner)
    leaves=owner['leaves'](rows);data=data_from_leaves(leaves,packet.reference)
    expected=leaves
    if packet.rung<10:
        for depth in (1,2):expected=owner['incoming_promotion'](expected,depth,packet.policy)
    if rows!=expected or packet.view!=present(expected,packet.rung,owner):raise ValueError('Retained tree, family mass, mean or presentation drift')
    return data

def verify(packet,expected_context,owner,zero,one):
    data=verify_carrier(packet,expected_context,owner)
    certificate=audit(data,expected_context,zero,one)
    if certificate!=packet.certificate:raise ValueError('Stale reconstruction certificate')
    required=certificate.status!='reconstructible'
    if bool(packet.operator_fallback)!=required:raise ValueError('Fallback retention policy violated')
    if required:
        field,rho=recover_operator_packet(packet.operator_fallback,zero,one)
        K,ops=expected_context.matrices();test=readout(field,K,ops,packet.reference,zero)
        if any(test[name]['blocks'][branch][i][j]!=rho*v for name in data for branch,m in data[name]['blocks'].items() for i,row in enumerate(m) for j,v in enumerate(row)):
            raise ValueError('Fallback disagrees with comparison observations')
    return data
