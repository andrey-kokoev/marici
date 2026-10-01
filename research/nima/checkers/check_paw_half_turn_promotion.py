"""Retained pi-turn square, promoted identity, and outward-direction gate.

Exact algebra/record experiment; no physical dimension or particle claim.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import count
from pathlib import Path
import json
from check_four_packet_cycle import UNIT, E1, E2, J, multiply, norm2

ZERO=(F(0),)*4
MAX_DEPTH=3

def negate(x): return tuple(-a for a in x)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(x,a): return tuple(a*v for v in x)
def reverse(x): return (x[0],x[1],x[2],-x[3])

def turn_lift(direction):
    if direction not in (-1,1): raise ValueError('A half-turn has direction +/-1')
    # Physical alpha=+pi: exp(-J alpha/2)=-J. Reverse half-turn has lift +J.
    return scale(J,F(-direction))

def act(rotor,x): return multiply(multiply(rotor,x),reverse(rotor))

@dataclass(frozen=True)
class Event:
    occurrence: str
    direction: int
    source: int
    target: int

    def __post_init__(self):
        if self.direction not in (-1,1) or self.source not in (-1,1) or self.target!=-self.source:
            raise ValueError('Invalid typed half-turn')

@dataclass(frozen=True)
class Packet:
    label: str
    source: int
    target: int
    events: tuple
    parents: tuple
    depth: int

    @property
    def angle_in_pi(self): return sum(e.direction for e in self.events)

    @property
    def variation_in_pi(self): return len(self.events)

    @property
    def lift(self):
        result=UNIT
        for e in self.events: result=multiply(turn_lift(e.direction),result)
        return result

    @property
    def endpoint_identity(self): return self.source==self.target

class Ledger:
    def __init__(self): self.serial=count(); self.packets={}

    def remember(self,source,target,events=(),parents=(),depth=0):
        label=f'packet:{next(self.serial)}'
        packet=Packet(label,source,target,events,parents,depth)
        self.packets[label]=packet
        return packet

    def identity(self,source=1): return self.remember(source,source)

    def half_turn(self,source,direction=1):
        occurrence=f'event:{next(self.serial)}'
        event=Event(occurrence,direction,source,-source)
        return self.remember(source,-source,(event,))

    def promote(self,left,right):
        if self.packets.get(left.label) is not left or self.packets.get(right.label) is not right:
            raise ValueError('Parents must be retained in this ledger')
        if left.target!=right.source: raise ValueError('Endpoint mismatch')
        if left.source!=right.target: raise ValueError('Only endpoint-returning composites admitted here')
        depth=max(left.depth,right.depth)+1
        if depth>MAX_DEPTH: raise ValueError('Retained depth limit reached')
        events=left.events+right.events
        if len({e.occurrence for e in events})!=len(events):
            raise ValueError('Replay needs fresh event occurrences, not duplicate event IDs')
        return self.remember(left.source,right.target,events,(left.label,right.label),depth)


def summary(p):
    return {'label':p.label,'source':p.source,'target':p.target,'parents':p.parents,'depth':p.depth,
            'physical_angle_in_pi':p.angle_in_pi,'path_variation_in_pi':p.variation_in_pi,
            'endpoint_identity':p.endpoint_identity,'rotor_lift':[str(v) for v in p.lift],
            'event_occurrences':[e.occurrence for e in p.events]}


def main():
    # Triangle-generated bivector, not a third spatial basis vector.
    # Paw: A=0, B=e2, C=-e1+e2, D=e1; all four vertices are distinct.
    triangle_b=E2;triangle_c=add(negate(E1),E2)
    area=scale(add(multiply(triangle_b,triangle_c),negate(multiply(triangle_c,triangle_b))),F(1,2))
    assert area==J and multiply(area,area)==negate(UNIT)
    assert multiply(J,E1)==negate(E2) and multiply(E1,J)==E2
    assert multiply(E1,E1)==UNIT
    # Naive Euclidean quarter-turn between a leg and its triangle's bivector
    # is not an algebra automorphism: it would send a +1 square to a -1 square.
    mixed=add(E1,J)
    assert norm2(mixed)==2 and multiply(mixed,mixed)==ZERO
    # Normalizing mixed by sqrt(2) cannot remove its square-zero obstruction.
    for direction in (-1,1):
        rotor=turn_lift(direction)
        assert act(rotor,E1)==negate(E1)
        assert act(rotor,E2)==negate(E2)
        assert multiply(rotor,reverse(rotor))==UNIT
    ledger=Ledger();empty=ledger.identity()
    positive=ledger.promote(ledger.half_turn(1,1),ledger.half_turn(-1,1))
    cancel=ledger.promote(ledger.half_turn(1,1),ledger.half_turn(-1,-1))
    another=ledger.promote(ledger.half_turn(1,1),ledger.half_turn(-1,1))
    twice=ledger.promote(positive,another)
    assert positive.endpoint_identity and positive.lift==negate(UNIT)
    assert positive.angle_in_pi==2 and positive.variation_in_pi==2
    assert cancel.lift==UNIT and cancel.angle_in_pi==0 and cancel.variation_in_pi==2
    assert empty.lift==UNIT and empty.variation_in_pi==0
    assert positive.label!=another.label and positive.events!=another.events
    assert twice.lift==UNIT and twice.angle_in_pi==4 and twice.depth==2
    for p in (empty,positive,cancel,another,twice):
        assert act(p.lift,E1)==E1
        for event in p.events:
            assert act(turn_lift(event.direction),scale(E1,F(event.source)))==scale(E1,F(event.target))
    # Fresh parent labels and flattening preserve the actual ordered witnesses.
    for p in (positive,cancel,another,twice):
        assert p.events==tuple(e for parent in p.parents for e in ledger.packets[parent].events)
    try: ledger.promote(positive,positive)
    except ValueError: pass
    else: raise AssertionError('Repeated occurrences silently admitted')
    try: ledger.promote(ledger.half_turn(1),ledger.half_turn(1))
    except ValueError: pass
    else: raise AssertionError('Noncomposable endpoints admitted')
    # Three promotion levels can be tested without erasing ancestry.
    def tree(depth):
        if depth==1: return ledger.promote(ledger.half_turn(1),ledger.half_turn(-1))
        return ledger.promote(tree(depth-1),tree(depth-1))
    deep=tree(3);assert deep.depth==3 and len(deep.events)==8
    try: ledger.promote(deep,ledger.identity())
    except ValueError: pass
    else: raise AssertionError('Depth overflow silently truncated')
    # Outward half-turn requires a supplied spatial normal in this realization.
    # A=(0,0,0), B=(0,1,0), C=(-1,1,0), D=(1,0,0) lie in z=0.
    # N=(0,0,1) is extra input; the leg never hits a body vertex on this path.
    # Exact quarter-turn about -e2 in the e1/e3 plane, keeping triangle as reference.
    def quarter(v): return (-v[2],v[1],v[0])
    path=[(F(1),F(0),F(0))]
    for _ in range(4): path.append(quarter(path[-1]))
    assert path[1]==(0,0,1) and path[2]==(-1,0,0) and path[4]==path[0]
    assert all(sum(v*v for v in point)==1 for point in path)
    assert all(point not in ((0,0,0),(0,1,0),(-1,1,0)) for point in path)
    hull_volumes=tuple(abs(point[2])/6 for point in path)
    assert hull_volumes==(0,F(1,6),0,F(1,6),0)
    # Without N, the intrinsic triangle-plane turn stays in that same plane.
    intrinsic=[E1,E2,negate(E1),negate(E2),E1]
    assert all(v[0]==0 and v[3]==0 for v in intrinsic)
    report={'status':'passed','model':'retained half-turn promotion, not dimension creation',
            'empty':summary(empty),'two_forward_half_turns':summary(positive),
            'forward_then_reverse':summary(cancel),'four_forward_half_turns':summary(twice),
            'depth_three':summary(deep),
            'intrinsic_area':'e1 wedge e2=J; J²=-1; J is a bivector, not a new spatial vector',
            'mixed_grade_control':'(e1+J)²=0: rotating a vector into J is not a Clifford automorphism',
            'outward_path_with_supplied_normal':[[str(v) for v in p] for p in path],
            'convex_hull_volumes_at_quarter_turns':[str(v) for v in hull_volumes],
            'conclusion':'Fresh endpoint-identity records with retained winding are supported; spatial growth and particle properties are not derived.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'paw-half-turn-promotion.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: pi-turn composition, vector versus rotor return, fresh identity promotion, full provenance, depth-3 gate, and bivector/outward-direction distinction.')

if __name__=='__main__': main()
