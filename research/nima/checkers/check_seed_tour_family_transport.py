"""Retained two-tour orbit through existing rung transports; no probabilities."""
from pathlib import Path
import runpy
import check_seed_typed_execution as seed

transport=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
Row=transport['Row']; indexed=transport['indexed']; unindex=transport['unindex']
leaves=transport['leaves']; promote=transport['incoming_promotion']

# Ordering below is a storage enumeration, not a preferred tour or execution order
# between the alternatives. Each alternative has its own fresh execution receipt.
receipts=tuple(seed.validate(seed.execute(word)) for word in seed.tours)
assert not ({e[2] for e in receipts[0]} & {e[2] for e in receipts[1]})
seams=tuple(next(v for v in 'AB' if word in seed.sew_at(v)) for word in seed.tours)
# Split at the tour's triangle-sewing endpoint, retaining the rotation offset.
# This is a view of a cyclic tour, not a reordering of its original execution.
spectral_ledger=seed.SpectralLedger()
spectral_bundles=[]
for i,receipt in enumerate(receipts):
    offset=next(k for k,e in enumerate(receipt) if e[0]==seams[i])
    cut=receipt[offset:]+receipt[:offset]
    roots=[]; modes=[]
    for triangle in (cut[:3],cut[3:]):
        packets=tuple(seed.TwoPacket(e[2],e[0],e[1]) for e in triangle)
        root=spectral_ledger.record4(packets)
        roots.append(root)
        modes.append(tuple(spectral_ledger.promote(root,mode) for mode in seed.MODES))
    spectral_bundles.append((offset,tuple(roots),tuple(modes)))
spectral_bundles=tuple(spectral_bundles)

def recover_spectral(bundle):
    offset,roots,modes=bundle
    cut=()
    for root,identities in zip(roots,modes):
        for identity in identities:
            assert spectral_ledger.resolve(identity) is root
        packets=spectral_ledger.deconstruct(identities[0])
        cut+=tuple(seed.emitted[p.label] for p in packets)
    return cut[-offset:]+cut[:-offset] if offset else cut

def spectral_reading(bundle):
    return tuple(tuple((m.mode,m.eigenvalue,m.projector) for m in modes) for modes in bundle[2])

assert tuple(map(recover_spectral,spectral_bundles))==receipts
assert spectral_reading(spectral_bundles[0])==spectral_reading(spectral_bundles[1])
assert spectral_bundles[0][2][0][0].window!=spectral_bundles[1][2][0][0].window
source=tuple(Row(('tour',i,receipt,spectral_bundles[i]),('seed-family',),('seam',seams[i]),((seed.F(6),),))
             for i,receipt in enumerate(receipts))

def recover(rows):
    original=leaves(rows)
    assert original==source
    result=tuple(seed.validate(row.label[2]) for row in original)
    assert result==receipts
    assert tuple(recover_spectral(row.label[3]) for row in original)==result
    assert tuple(spectral_reading(row.label[3]) for row in original)==tuple(map(spectral_reading,spectral_bundles))
    return result

def word(receipt): return tuple(e[3] for e in receipt)
def seam(receipt):
    return next(v for v in 'AB' if seed.normalize(word(receipt)) in seed.sew_at(v))
def marked_reader(receipt,mark):
    assert mark in 'AB'
    return int(seam(receipt)==mark)

for policy in ('inherited','common'):
    def horizontal(rows): return promote(promote(rows,1,policy),2,policy)
    left11=indexed(source,'source'); left10=indexed(unindex(left11),'target')
    right6=horizontal(source)
    right5=indexed(right6,'source'); right4=indexed(unindex(right5),'target')
    assert indexed(horizontal(unindex(left11)),'source')==right5
    assert indexed(horizontal(unindex(left10)),'target')==right4
    recovered=recover(unindex(right4))
    assert tuple(map(len,recovered))==(6,6)
    assert tuple(marked_reader(p,'A') for p in recovered)==(1,0)
    assert tuple(marked_reader(p,'B') for p in recovered)==(0,1)
    # The generic transport computes means internally, but the observer returns
    # the full family of readings and receipts, never an average over alternatives.
    assert sum(len(p) for p in recovered)==12  # retained alternative events only
    print('PASS:',policy,'rung4 retains both six-event alternatives; outer families',len(right6))

# Scalar observation space on a two-point orbit: invariant line (1,1),
# anti-invariant line (1,-1). This is linear algebra, not probabilistic mixing.
exchange=((0,1),(1,0))
for values in ((0,0),(1,1),(1,0),(0,1),(2,-3)):
    a,b=map(seed.F,values)
    even=(a+b)/2; odd=(a-b)/2
    assert (even+odd,even-odd)==(a,b)
    assert ((b+a)/2,(b-a)/2)==(even,-odd)
    assert ((a,b)==(b,a))==(odd==0)
# A marked reading is covariant if the marking is moved too; fixing it breaks
# the exchange symmetry and distinguishes the alternatives.
for i,p in enumerate(receipts):
    moved_word=seed.moved_tour(word(p),seed.swap)
    j=seed.tours.index(moved_word)
    assert j==1-i
    for mark in 'AB':
        assert marked_reader(p,mark)==marked_reader(receipts[j],seed.swap[mark])
        assert marked_reader(p,mark)!=marked_reader(receipts[j],mark)
# No assumption that relabelling re-executes events: the index permutation
# acts on alternatives; original execution receipts stay explicitly retained.
print('PASS: invariant scalar readers are constant on the orbit; distinguishing scalar readers need symmetry-breaking data.')
print('PASS: seam-marked reader is covariant under simultaneous tour/mark exchange.')
# Relabelling matches triangle slot positions and descriptors, but not issued
# occurrence IDs. Verify the supplied correspondence without equating histories.
for left_root,right_root in zip(spectral_bundles[0][1],spectral_bundles[1][1]):
    for p,q in zip(left_root.packets,right_root.packets):
        assert (seed.swap[p.source],seed.swap[p.target])==(q.source,q.target)
        assert p.label!=q.label
print('PASS: complete triangle spectra agree across tours; exact execution windows remain distinct at rung4.')
print('PASS: seed symmetry aligns triangle slots and spectral descriptors without identifying event IDs.')

# Reuse the separately declared order-sensitive vertex-action adapter.
response=runpy.run_path(str(Path(__file__).with_name('check_seed_cycle_response_transport.py')))
def vertex_action(root):
    action=list(range(4))
    for p in root.packets:
        action[seed.vertices.index(p.source)]=seed.vertices.index(p.target)
    return tuple(action)
actions=tuple(tuple(vertex_action(root) for root in bundle[1]) for bundle in spectral_bundles)
assert actions==((response['g'],response['h']),(response['h'],response['g']))
operators=tuple(response['compose'](b,a) for a,b in actions)
assert operators==(response['left'],response['right'])
assert operators[0]!=operators[1]
print('PASS: existing vertex-action composite distinguishes the two sewn orders, unlike bare triangle spectra.')
print('Scope: composite action is a declared adapter, not derived edge phase evolution or calibrated physical reading.')

# Exhaust all cuts, respecting the DOMAIN of the existing triangle-block adapter.
def cut_actions(receipt,offset):
    cut=receipt[offset:]+receipt[:offset]
    blocks=(cut[:3],cut[3:])
    if any(block[0][0]!=block[-1][1] for block in blocks):
        raise ValueError('Cut does not split into closed triangle blocks')
    if {frozenset(e[3] for e in block) for block in blocks}!=seed.triangle_sets:
        raise ValueError('Blocks are not the two supplied triangles')
    result=[]
    for block in blocks:
        action=list(range(4))
        for s,t,_,_ in block:
            action[seed.vertices.index(s)]=seed.vertices.index(t)
        result.append(tuple(action))
    return tuple(result)

def inverse(p): return tuple(p.index(i) for i in range(4))
compose=response['compose']
for number,receipt in enumerate(receipts):
    valid={}
    for offset in range(6):
        try: a,b=cut_actions(receipt,offset)
        except ValueError: continue
        valid[offset]=(a,b,compose(b,a))
    assert set(valid)==({0,3} if number==0 else {1,4})
    assert {data[2] for data in valid.values()}==set(operators)
    for offset,(a,b,L) in valid.items():
        other=(offset+3)%6
        R=valid[other][2]
        # Moving a complete leading block to the end changes base frame by a.
        assert R==compose(compose(a,L),inverse(a))
        ML=response['matrix'](L); MR=response['matrix'](R)
        assert MR==tuple(tuple(ML[inverse(a)[i]][inverse(a)[j]] for j in range(4))
                        for i in range(4))
        # All named matrix probes, not just one sample, transport covariantly.
        for i in range(4):
            for j in range(4):
                assert ML[i][j]==MR[a[i]][a[j]]
        # The shared scalar-identity reference transports unchanged as well.
        fixed=response['fixed'].value
        DL=response['subtract'](ML,fixed); DR=response['subtract'](MR,fixed)
        assert all(DL[i][j]==DR[a[i]][a[j]] for i in range(4) for j in range(4))
    print('Cut-domain audit: tour',number,'valid',tuple(valid),'other four cuts outside triangle-block adapter')
# The two responses have the same conjugacy class; a fixed named probe is not
# a conjugacy-invariant reader. The old A-to-A distinction is frame-dependent.
assert response['L'][0][0]!=response['R'][0][0]
assert sorted(sum(int(p[i]==i) for i in range(4)) for p in operators)==[1,1]
print('PASS: valid cut changes conjugate the response; all transported matrix probes preserve their readings.')
print('RESULT: no distinction under conjugacy-invariant readers; fixed named probes retain a frame/cut witness.')
print('BOUNDARY: four of six cuts per tour require an edge-level adapter not supplied by existing triangle actions.')
