"""Retained nine-record ideal radar protocol; no physical realization oracle.
Directions are (3,0), (0,4), (3,4) times epsilon in a declared transverse chart.
Clock values are proper times, c=1. Output is a finite-difference radar shape,
not an unconditional estimator of pointwise curvature.
"""
from dataclasses import dataclass
from fractions import Fraction as F

TIMES=(-1,0,1)
DIRECTIONS=('x3','y4','xy5')
WEIGHTS={-1:F(1),0:F(-2),1:F(1)}

@dataclass(frozen=True)
class Protocol:
    epsilon:F
    step:F
    center:F
    frame_label:str
    clock_label:str
    reflection:str='instantaneous-null-return'
    def __post_init__(self):
        if self.epsilon<=0 or self.step<=0:raise ValueError('positive baseline and proper-time step required')
        if not self.frame_label or not self.clock_label:raise ValueError('frame and clock provenance required')
        if self.reflection!='instantaneous-null-return':raise ValueError('unmodeled reflection delay')

@dataclass(frozen=True)
class Row:
    time:int
    direction:str
    emission:F
    reception:F

@dataclass(frozen=True)
class Packet:
    protocol:Protocol
    rows:tuple
    source_reference:str
    def index(self):
        if not self.source_reference:raise ValueError('source reference or explicit synthetic designation required')
        out={}
        for row in self.rows:
            key=(row.time,row.direction)
            if row.time not in TIMES or row.direction not in DIRECTIONS:raise ValueError('unknown active-domain label')
            if key in out:raise ValueError('duplicate labelled row')
            if row.emission!=self.protocol.center+row.time*self.protocol.step:raise ValueError('emission/clock-grid mismatch')
            if row.reception<=row.emission:raise ValueError('future reception required')
            out[key]=row
        if set(out)!={(t,d) for t in TIMES for d in DIRECTIONS}:raise ValueError('complete nine-record domain required')
        return out

def distances(packet):
    return {k:(r.reception-r.emission)/2 for k,r in packet.index().items()}

def normalized_squares(packet):
    return {k:(v/packet.protocol.epsilon)**2 for k,v in distances(packet).items()}

def polarize(q):
    # Symmetric matrix stored as (11,12,22), with the calibrated 3-4-5 factors.
    return (q['x3']/9,(q['xy5']-q['x3']-q['y4'])/24,q['y4']/16)

def by_time(packet):
    q=normalized_squares(packet)
    shapes={t:polarize({d:q[t,d] for d in DIRECTIONS}) for t in TIMES}
    return tuple(-sum(WEIGHTS[t]*shapes[t][i] for t in TIMES)/(2*packet.protocol.step**2) for i in range(3))

def by_direction(packet):
    q=normalized_squares(packet)
    temporal={d:-sum(WEIGHTS[t]*q[t,d] for t in TIMES)/(2*packet.protocol.step**2) for d in DIRECTIONS}
    return polarize(temporal)

@dataclass(frozen=True)
class NativeSection:
    protocol:Protocol
    choices:tuple # (fiber index, selected row), retaining membership labels
    source_reference:str

def encode_section(packet):
    return NativeSection(packet.protocol,tuple(packet.index().items()),packet.source_reference)

def on_native_section(section):
    # Direct reading of selected fiber rows: no Packet reconstruction or decode.
    if not section.source_reference:raise ValueError('source provenance required')
    seen=set();temporal={d:F(0) for d in DIRECTIONS}
    for index,row in section.choices:
        if index!=(row.time,row.direction):raise ValueError('fiber membership mismatch')
        if index in seen or row.time not in TIMES or row.direction not in DIRECTIONS:raise ValueError('invalid section domain')
        seen.add(index)
        if row.emission!=section.protocol.center+row.time*section.protocol.step:raise ValueError('clock grid mismatch')
        if row.reception<=row.emission:raise ValueError('future reception required')
        value=((row.reception-row.emission)/(2*section.protocol.epsilon))**2
        temporal[row.direction]+=WEIGHTS[row.time]*value
    if seen!={(t,d) for t in TIMES for d in DIRECTIONS}:raise ValueError('incomplete section')
    scale=-1/(2*section.protocol.step**2)
    return (scale*temporal['x3']/9,
            scale*(temporal['xy5']-temporal['x3']-temporal['y4'])/24,
            scale*temporal['y4']/16)

def error_bound(protocol,max_true_distance,distance_error):
    if max_true_distance<0 or distance_error<0:raise ValueError('nonnegative error envelope required')
    return (2*max_true_distance*distance_error+distance_error**2)/(4*protocol.epsilon**2*protocol.step**2)

def flat_packet(protocol):
    lengths={'x3':F(3),'y4':F(4),'xy5':F(5)}
    rows=tuple(Row(t,d,protocol.center+t*protocol.step,
                   protocol.center+t*protocol.step+2*protocol.epsilon*lengths[d])
               for t in TIMES for d in DIRECTIONS)
    return Packet(protocol,rows,'analytic:flat-Minkowski-static-reflectors')
