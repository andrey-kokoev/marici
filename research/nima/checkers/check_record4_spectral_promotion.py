"""Cycle-five spectral promotion of an explicitly retained nested return.

The operator adapter is cyclic successor on the three original packet slots,
not the already collapsed A->A endpoint. Exact arithmetic in Q(i*sqrt(3)).
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import count
from pathlib import Path
import json
from check_triangle_half_phase import (
    TwoPacket, cycle_from_packets, I, ZERO, mm, transpose,
    zadd, zmul, zscale, zconj, znorm, zmm, zmscale, zreal,
    add, sub, scale,
)

ONE=(F(1),F(0));OMEGA=(F(-1,2),F(1,2))
MODES={'common':ONE,'positive':OMEGA,'negative':zconj(OMEGA)}
MAX_DEPTH=3

def zmadd(a,b): return tuple(tuple(zadd(x,y) for x,y in zip(r,s)) for r,s in zip(a,b))
def dagger(a): return tuple(tuple(zconj(z) for z in row) for row in transpose(a))
def ztrace(a):
    out=(F(0),F(0))
    for i in range(len(a)): out=zadd(out,a[i][i])
    return out

def spectral_projector(T,mode):
    if mode not in MODES: raise ValueError('Explicit common/positive/negative mode required')
    lam=MODES[mode];inverse=zconj(lam)
    E=zmscale(zmadd(zmadd(zreal(I),zmscale(zreal(T),inverse)),
                     zmscale(zreal(mm(T,T)),zmul(inverse,inverse))),(F(1,3),F(0)))
    if zmm(E,E)!=E or dagger(E)!=E or ztrace(E)!=ONE:
        raise ValueError('Operator does not resolve this rank-one mode identity')
    if zmm(zreal(T),E)!=zmscale(E,lam): raise ValueError('Eigenmode sewing failed')
    return lam,E

@dataclass(frozen=True)
class NestedReturn:
    label: str
    entry: TwoPacket
    continuation: tuple
    fold_through_B: tuple
    fold_through_C: tuple
    stage_history: tuple
    depth: int=2

    @property
    def packets(self): return (self.entry,)+self.continuation

@dataclass(frozen=True)
class HistoryWindow:
    root: str
    ordered_occurrences: tuple

@dataclass(frozen=True)
class ModeIdentity:
    label: str
    mode: str
    eigenvalue: tuple
    projector: tuple
    window: HistoryWindow
    depth: int

class SpectralLedger:
    def __init__(self):
        self.serial=count();self.roots={};self.identities={}

    def record4(self,packets):
        packets=tuple(packets);cycle_from_packets(packets)
        a,b,c=packets
        # The nested return retains an entry A->B and a continuation B->C->A.
        if a.target!=b.source or b.target!=c.source or c.target!=a.source:
            raise ValueError('Unsewn nested return')
        label=f'record4:{next(self.serial)}'
        root=NestedReturn(label,a,(b,c),((a,b),(c,)),((a,),(b,c)),
                          ('present-three-segments','fold-through-B','fold-through-C','nest-return-arrow'))
        self.roots[label]=root
        return root

    def validate_root(self,root):
        if self.roots.get(root.label) is not root: raise ValueError('Unknown or substituted retained root')
        p=root.packets;cycle_from_packets(p)
        if tuple(q for part in root.fold_through_B for q in part)!=p:
            raise ValueError('Left fold lost an occurrence')
        if tuple(q for part in root.fold_through_C for q in part)!=p:
            raise ValueError('Right fold lost an occurrence')
        if root.fold_through_B!=((p[0],p[1]),(p[2],)) or root.fold_through_C!=((p[0],),(p[1],p[2])):
            raise ValueError('Incorrect fold structure')
        return cycle_from_packets(p)

    def promote(self,root,mode):
        T=self.validate_root(root)
        if root.depth+1>MAX_DEPTH: raise ValueError('Retained depth limit reached')
        lam,E=spectral_projector(T,mode)
        window=HistoryWindow(root.label,tuple(p.label for p in root.packets))
        label=f'identity:{next(self.serial)}'
        out=ModeIdentity(label,mode,lam,E,window,root.depth+1)
        self.identities[label]=out
        return out

    def resolve(self,identity):
        if self.identities.get(identity.label) is not identity: raise ValueError('Unregistered or modified identity')
        if identity.window.root not in self.roots: raise ValueError('Missing history window')
        root=self.roots[identity.window.root];T=self.validate_root(root)
        if identity.window.ordered_occurrences!=tuple(p.label for p in root.packets):
            raise ValueError('Window is not bound to these ordered occurrences')
        if identity.depth!=root.depth+1 or identity.depth>MAX_DEPTH:
            raise ValueError('Incorrect retained depth')
        lam,E=spectral_projector(T,identity.mode)
        if identity.eigenvalue!=lam or identity.projector!=E:
            raise ValueError('Spectral identity does not belong to its retained mode')
        return root

    def deconstruct(self,identity): return self.resolve(identity).packets


def rejects(fn):
    try: fn()
    except ValueError: return
    raise AssertionError('Invalid promotion was accepted')

def zjson(z): return {'real':str(z[0]),'imaginary_sqrt3_coefficient':str(z[1])}

def main():
    ledger=SpectralLedger()
    packets=(TwoPacket('AB:0','A','B'),TwoPacket('BC:0','B','C'),TwoPacket('CA:0','C','A'))
    root=ledger.record4(packets);T=ledger.validate_root(root)
    promoted={mode:ledger.promote(root,mode) for mode in MODES}
    Q=scale(add(add(I,T),mm(T,T)),F(1,3));P=sub(I,Q);A=sub(T,transpose(T))
    plus=tuple(tuple((P[i][j]/2,-A[i][j]/6) for j in range(3)) for i in range(3))
    assert promoted['positive'].projector==plus
    assert promoted['negative'].projector==tuple(tuple(zconj(z) for z in row) for row in plus)
    assert promoted['common'].projector==zreal(Q)
    total=zreal(ZERO)
    for mode,item in promoted.items():
        assert ledger.resolve(item) is root and ledger.deconstruct(item)==packets
        assert item.depth==3 and zmm(item.projector,item.projector)==item.projector
        total=zmadd(total,item.projector)
        v=(ONE,)*3 if mode=='common' else (ONE,item.eigenvalue,zmul(item.eigenvalue,item.eigenvalue))
        # Projector acts as identity on its selected eigenline.
        vcol=tuple((z,) for z in v)
        assert zmm(item.projector,vcol)==vcol
        for scalar in ((F(1),F(0)),(F(1,2),F(0)),(F(2),F(1)),(F(0),F(1))):
            w=tuple(zmul(scalar,z) for z in v);n=sum(znorm(z) for z in w)
            outer=tuple(tuple(zscale(zmul(x,zconj(y)),1/n) for y in w) for x in w)
            assert outer==item.projector
        for other in promoted.values():
            if other.mode!=mode: assert zmm(item.projector,other.projector)==zreal(ZERO)
    assert total==zreal(I)
    # Inverse cyclic orientation exchanges positive and negative eigenspaces.
    assert spectral_projector(transpose(T),'positive')[1]==promoted['negative'].projector
    # Same endpoint reading or same projector must not merge distinct histories.
    next_packets=tuple(TwoPacket(p.label.replace(':0',':1'),p.source,p.target) for p in packets)
    other_root=ledger.record4(next_packets);other=ledger.promote(other_root,'positive')
    first=promoted['positive']
    assert other.projector==first.projector and other.label!=first.label
    assert other.window!=first.window and ledger.deconstruct(other)!=ledger.deconstruct(first)
    repeat=ledger.promote(root,'positive')
    assert repeat.projector==first.projector and repeat.label!=first.label
    assert ledger.resolve(repeat) is root
    # Collapsing record 4 to its three-step identity destroys simple spectral selection.
    assert mm(mm(T,T),T)==I
    for mode in MODES: rejects(lambda mode=mode:spectral_projector(I,mode))
    rejects(lambda:ledger.promote(root,'unspecified'))
    rejects(lambda:ledger.record4((packets[0],packets[2],packets[1])))
    rejects(lambda:ledger.record4((packets[0],packets[0],packets[2])))
    # Check semantic validation even if an invalid record appears in the registry.
    bad=replace(first,label='identity:bad',window=replace(first.window,ordered_occurrences=tuple(reversed(first.window.ordered_occurrences))))
    ledger.identities[bad.label]=bad;rejects(lambda:ledger.resolve(bad));del ledger.identities[bad.label]
    bad=replace(first,label='identity:bad',eigenvalue=ONE)
    ledger.identities[bad.label]=bad;rejects(lambda:ledger.resolve(bad));del ledger.identities[bad.label]
    bad=replace(first,label='identity:bad',window=HistoryWindow('absent',first.window.ordered_occurrences))
    ledger.identities[bad.label]=bad;rejects(lambda:ledger.resolve(bad));del ledger.identities[bad.label]
    deep=replace(root,label='record4:depth-limit',depth=3)
    ledger.roots[deep.label]=deep;rejects(lambda:ledger.promote(deep,'positive'));del ledger.roots[deep.label]
    # A 1:1 label/record interface, not an injection from histories to projectors.
    assert len({p.label for p in ledger.identities.values()})==len(ledger.identities)
    report={'status':'passed','record4':{'label':root.label,'entry':root.entry.__dict__,
            'returned_arrow':[p.__dict__ for p in root.continuation],
            'folds':[[[p.label for p in part] for part in fold] for fold in (root.fold_through_B,root.fold_through_C)],
            'stage_history':root.stage_history},
            'operator_adapter':'cyclic successor on retained primitive packet slots, counting metric',
            'promoted_modes':{mode:{'label':r.label,'eigenvalue':zjson(r.eigenvalue),
                'projector':[[zjson(z) for z in row] for row in r.projector],
                'window':r.window.__dict__,'retained_depth':r.depth} for mode,r in promoted.items()},
            'checks':['idempotence and Hermitian rank one','eigenline identity and phase retention',
                      'eigenvector scale/phase invariance','mode orthogonality and completeness',
                      'orientation reversal','history-preserving deconstruction','collapsed endpoint degeneracy',
                      'malformed and forged records','depth-three refusal'],
            'scope':'Spectral promotion implemented for a declared packet-slot operator. The nested map is not automatically linearized; mode selection remains explicit. No physical particle claim.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'record4-spectral-promotion.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: nested record 4 -> three exact spectral mode identities, 1:1 labels, recoverable history, phase/scale invariance, degeneracy and depth gates.')

if __name__=='__main__': main()
