"""Seed relabelling induces a comparison of spectral ports, not an interaction."""
from itertools import permutations
import check_record4_spectral_promotion as p

edges=('AB','BC','CA','BA','AD','DB')
automorphisms=[]
for image in permutations('ABCD'):
    rename=dict(zip('ABCD',image))
    if {rename[e[0]]+rename[e[1]] for e in edges}==set(edges):
        automorphisms.append(rename)
assert len(automorphisms)==2
swap=next(s for s in automorphisms if s['A']!='A')
assert swap==dict(zip('ABCD','BADC'))
left=('AB','BC','CA');right=('BA','AD','DB')
def transport(word): return tuple(swap[e[0]]+swap[e[1]] for e in word)
assert transport(left)==right and transport(right)==left
ledger=p.SpectralLedger()
roots=[ledger.record4(tuple(p.TwoPacket(e,e[0],e[1]) for e in word)) for word in (left,right)]
# Slot correspondence is the identity matrix in these transported ordered bases,
# but has different labelled occurrence spaces as source and target.
T0,T1=map(ledger.validate_root,roots)
J=p.I
assert p.mm(J,T0)==p.mm(T1,J)
assert p.mm(p.transpose(J),J)==p.I
for mode in p.MODES:
    a,b=(ledger.promote(root,mode) for root in roots)
    assert a.label!=b.label and a.window.root!=b.window.root
    assert a.window.ordered_occurrences!=b.window.ordered_occurrences
    assert transport(a.window.ordered_occurrences)==b.window.ordered_occurrences
    assert a.eigenvalue==b.eigenvalue
    assert p.zmm(p.zreal(J),a.projector)==p.zmm(b.projector,p.zreal(J))
    assert tuple(q.label for q in ledger.deconstruct(a))==left
    assert tuple(q.label for q in ledger.deconstruct(b))==right
# Cross-mode products vanish after transporting into the same comparison basis.
for mode in p.MODES:
    for other in p.MODES:
        _,E=p.spectral_projector(T0,mode)
        _,F=p.spectral_projector(T1,other)
        overlap=p.zmm(F,p.zmm(p.zreal(J),E))
        assert overlap==(E if mode==other else p.zreal(p.ZERO))
print('PASS: unique nonidentity seed symmetry transports every promoted mode with occurrence provenance intact.')
print('PASS: corresponding modes intertwine; unequal modes have zero transported overlap.')
print('BOUNDARY: relabelling comparison is not a primitive arrow action, physical coupling, or native admission proof.')
