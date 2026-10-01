"""Deconstructed arrows with typed windows into retained half-turn histories.

A finite adapter of the table-fibration regroup/reverse cycle. No claim that
ordinary imaginary coefficients encode provenance or that views execute turns.
"""
from dataclasses import dataclass, replace
from pathlib import Path
import json
from check_paw_half_turn_promotion import Ledger, UNIT, negate, turn_lift, multiply

@dataclass(frozen=True)
class Window:
    root: str
    parent_path: tuple
    occurrence: str

@dataclass(frozen=True)
class Arrow:
    occurrence: str
    source: int
    target: int
    reversed: bool
    window: Window

@dataclass(frozen=True)
class Presentation:
    origin: str
    arrows: tuple
    operations: tuple=()


def leaves(ledger,root):
    """Recover ordered primitive leaves by parent links, checking cached members."""
    if root not in ledger.packets: raise ValueError('Unknown retained root')
    def visit(label,path,ancestors):
        if label in ancestors: raise ValueError('Cyclic parent history')
        if label not in ledger.packets: raise ValueError('Missing retained parent')
        p=ledger.packets[label]
        if p.depth>3: raise ValueError('Retained depth exceeds bound')
        if p.parents:
            if len(p.parents)!=2: raise ValueError('Expected ordered binary parents')
            a,b=(ledger.packets[k] for k in p.parents)
            if a.target!=b.source or (p.source,p.target)!=(a.source,b.target):
                raise ValueError('Parent endpoint mismatch')
            if p.depth!=1+max(a.depth,b.depth): raise ValueError('Wrong retained depth')
            out=visit(a.label,path+(0,),ancestors+(label,))+visit(b.label,path+(1,),ancestors+(label,))
        else:
            if p.depth!=0 or len(p.events)>1: raise ValueError('Malformed primitive')
            out=[] if not p.events else [(path,p.events[0])]
            if p.events and (p.source,p.target)!=(p.events[0].source,p.events[0].target):
                raise ValueError('Leaf endpoint mismatch')
            if not p.events and p.source!=p.target: raise ValueError('Empty nonidentity leaf')
        if tuple(e for _,e in out)!=p.events: raise ValueError('Cached history differs from parent history')
        return out
    out=visit(root,(),())
    if len({e.occurrence for _,e in out})!=len(out): raise ValueError('Reused primitive occurrence')
    return tuple(out)


def deconstruct(ledger,packet):
    if ledger.packets.get(packet.label) is not packet: raise ValueError('Foreign packet')
    arrows=tuple(Arrow(e.occurrence,e.source,e.target,False,Window(packet.label,path,e.occurrence))
                 for path,e in leaves(ledger,packet.label))
    return Presentation(packet.label,arrows,('deconstruct',))


def resolve(ledger,presentation,arrow):
    w=arrow.window
    if w.root!=presentation.origin: raise ValueError('Window rooted in another identity')
    candidates=dict(leaves(ledger,w.root))
    if w.parent_path not in candidates: raise ValueError('Invalid parent path')
    event=candidates[w.parent_path]
    if event.occurrence!=w.occurrence or arrow.occurrence!=w.occurrence:
        raise ValueError('Window does not bind this arrow occurrence')
    source,target=(event.target,event.source) if arrow.reversed else (event.source,event.target)
    if (arrow.source,arrow.target)!=(source,target): raise ValueError('Untransported history window')
    direction=-event.direction if arrow.reversed else event.direction
    return event,direction


def validate(ledger,p):
    expected=[e.occurrence for _,e in leaves(ledger,p.origin)]
    actual=[a.occurrence for a in p.arrows]
    if len(actual)!=len(set(actual)) or set(actual)!=set(expected):
        raise ValueError('Omitted, duplicated or foreign retained occurrence')
    for a in p.arrows: resolve(ledger,p,a)


def group_by_source(ledger,p):
    validate(ledger,p)
    groups={}
    for a in p.arrows: groups.setdefault(a.source,[]).append(a)
    return tuple((key,tuple(groups[key])) for key in sorted(groups))


def transpose_view(ledger,p):
    groups=group_by_source(ledger,p)
    arrows=tuple(replace(a,source=a.target,target=a.source,reversed=not a.reversed)
                 for _,members in groups for a in members)
    out=Presentation(p.origin,arrows,p.operations+('group-by-source','reversed-unpack'))
    validate(ledger,out)
    return out


def ordered(ledger,p):
    # Display grouping may reorder rows; original event positions remain in windows.
    validate(ledger,p)
    order={e.occurrence:i for i,(_,e) in enumerate(leaves(ledger,p.origin))}
    return tuple(sorted(p.arrows,key=lambda a:order[a.occurrence]))


def recover(ledger,p):
    validate(ledger,p)
    if any(a.reversed for a in p.arrows):
        raise ValueError('Return to the original endpoint presentation before reassembly')
    return ledger.packets[p.origin]


def original_phase(ledger,p):
    validate(ledger,p)
    rotor=UNIT
    for a in ordered(ledger,p):
        event,_=resolve(ledger,p,a)
        rotor=multiply(turn_lift(event.direction),rotor)
    return rotor


def rejects(fn):
    try: fn()
    except ValueError: return
    raise AssertionError('Invalid history view was accepted')


def main():
    ledger=Ledger()
    def loop(directions=(1,1)):
        return ledger.promote(ledger.half_turn(1,directions[0]),ledger.half_turn(-1,directions[1]))
    full=ledger.promote(loop(),loop())
    empty=ledger.identity()
    cancel=loop((1,-1))
    another_full=ledger.promote(loop(),loop())
    assert full.lift==empty.lift==cancel.lift==UNIT
    views={name:deconstruct(ledger,p) for name,p in
           [('four_turns',full),('empty',empty),('out_and_back',cancel),('another_four_turns',another_full)]}
    root_snapshot=dict(ledger.packets)
    traces={}
    for name,initial in views.items():
        p=initial
        for cycle in range(3):
            middle=transpose_view(ledger,p)
            for a in middle.arrows:
                event,direction=resolve(ledger,middle,a)
                assert direction==-event.direction
            if middle.arrows: rejects(lambda:recover(ledger,middle))
            p=transpose_view(ledger,middle)
            assert ordered(ledger,p)==ordered(ledger,initial)
            assert recover(ledger,p) is recover(ledger,initial)
            assert original_phase(ledger,p)==ledger.packets[p.origin].lift
            assert p.operations!=initial.operations
        traces[name]={'origin':p.origin,'active_arrow_count':len(p.arrows),
                      'retained_angle_in_pi':ledger.packets[p.origin].angle_in_pi,
                      'retained_variation_in_pi':ledger.packets[p.origin].variation_in_pi,
                      'retained_rotor_lift':[str(v) for v in original_phase(ledger,p)],
                      'presentation_cycles':3,'operation_history':p.operations,
                      'windows':[{'occurrence':a.occurrence,'root':a.window.root,
                                  'parent_path':a.window.parent_path} for a in ordered(ledger,p)]}
    assert ledger.packets==root_snapshot # Views do not execute new physical turns.
    v=views['four_turns'];a=v.arrows[0]
    # Different provenance with identical visible endpoints must not be substituted.
    other=views['another_four_turns'].arrows[0]
    assert (a.source,a.target)==(other.source,other.target)
    rejects(lambda:resolve(ledger,v,replace(a,window=other.window)))
    rejects(lambda:resolve(ledger,v,replace(a,source=a.target,target=a.source)))
    rejects(lambda:resolve(ledger,v,replace(a,window=replace(a.window,parent_path=(9,)))))
    rejects(lambda:resolve(ledger,v,replace(a,window=replace(a.window,occurrence='forged'))))
    rejects(lambda:validate(ledger,replace(v,arrows=v.arrows[:-1])))
    rejects(lambda:validate(ledger,replace(v,arrows=v.arrows+(a,))))
    # r^4 and the empty identity share Re/Im, yet their retained windows differ.
    assert full.events!=empty.events and v.origin!=views['empty'].origin
    assert len(v.arrows)==4 and len(views['empty'].arrows)==0
    assert len({a.occurrence for a in v.arrows})==4
    assert all(len(a.window.parent_path)==2 for a in v.arrows)
    # +pi and -pi arrows look identical at the endpoint but replay differently.
    plus=deconstruct(ledger,ledger.half_turn(1,1))
    minus=deconstruct(ledger,ledger.half_turn(1,-1))
    assert (plus.arrows[0].source,plus.arrows[0].target)==(minus.arrows[0].source,minus.arrows[0].target)
    assert resolve(ledger,plus,plus.arrows[0])[1]==-resolve(ledger,minus,minus.arrows[0])[1]
    report={'status':'passed','model':'arrow presentation with root-bound retained-history windows',
            'active_law':'group-by-source / reversed-unpack, repeated twice',
            'window':'root label + ordered parent path + primitive occurrence; view reversal transported separately',
            'tested_presentation_cycles':3,'traces':traces,
            'hostile_controls':6,'same_endpoint_opposite_half_turns_distinguished':True,
            'scope':'Finite presentation adapter, not new physical dynamics, literal Re/Im decomposition, or automatic arity growth.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'arrow-history-window.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: arity-4 deconstruction, typed history windows, three regroup/reverse cycles, exact reassembly, retained winding and rejection controls.')

if __name__=='__main__': main()
