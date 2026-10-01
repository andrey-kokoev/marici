"""Actual seed paths using existing pullback composition and spectral windows.
Finite execution-record adapter, not a native emission law or physical clock.
"""
from itertools import count, permutations
from check_indexed_path_synthesis import compose, source, target
from check_natural_tower_return import PACKETS
from check_record4_spectral_promotion import SpectralLedger, TwoPacket, MODES

registry={label:(s,t) for label,s,t in PACKETS}
serial=count()
emitted={}

def execute(word):
    word=tuple(word)
    if not word or any(label not in registry for label in word):
        raise ValueError('Nonempty seed word required')
    # Validate first: a rejected request emits no partial execution.
    if any(registry[a][1]!=registry[b][0] for a,b in zip(word,word[1:])):
        raise ValueError('Unmatched endpoints')
    path=()
    for label in word:
        s,t=registry[label]
        event=(s,t,f'event:{next(serial)}',label)
        emitted[event[2]]=event
        path=(event,) if not path else next(iter(compose({path},{(event,)})))
    return path

def validate(path):
    if not path or len({e[2] for e in path})!=len(path):
        raise ValueError('Empty or reused execution occurrence')
    for e in path:
        if emitted.get(e[2])!=e or registry.get(e[3])!=e[:2]:
            raise ValueError('Unknown or forged execution occurrence')
    if any(a[1]!=b[0] for a,b in zip(path,path[1:])):
        raise ValueError('Broken execution seam')
    return path

words=(('AB','BC','CA'),('AD','DB','BA'),('AB','BA'))
paths=tuple(validate(execute(word)) for word in words)
assert all(source(p)==target(p)=='A' for p in paths)
assert tuple(map(len,paths))==(3,3,2)
assert len({e[2] for p in paths for e in p})==8
for p in paths:
    assert tuple(e[3] for e in p) in words
# Composition uses the existing function, preserving ordered occurrences.
a,b,c=({p} for p in paths)
assert compose(compose(a,b),c)==compose(a,compose(b,c))
combined=validate(next(iter(compose(compose(a,b),c))))
assert len(combined)==8 and combined==sum(paths,())
repeat=validate(execute(words[0]))
assert tuple(e[3] for e in repeat)==words[0] and repeat!=paths[0]
assert not ({e[2] for e in repeat}&{e[2] for e in paths[0]})

ledger=SpectralLedger()
for p in (paths[0],paths[1],repeat):
    packets=tuple(TwoPacket(e[2],e[0],e[1]) for e in p)
    root=ledger.record4(packets)
    for mode in MODES:
        identity=ledger.promote(root,mode)
        restored=ledger.deconstruct(identity)
        assert restored==packets
        assert tuple(emitted[q.label] for q in restored)==p
# Same mode operator, distinct executions/windows.
roots=tuple(ledger.roots.values())
u=ledger.promote(roots[0],'positive');v=ledger.promote(roots[2],'positive')
assert u.projector==v.projector and u.eigenvalue==v.eigenvalue
assert u.window!=v.window
# AB-BA has two slots: do not feed it to the three-slot spectral adapter.
assert len(paths[2])!=3

def rejects(fn):
    try: fn()
    except ValueError: return
    raise AssertionError('Invalid execution accepted')

before=len(emitted)
rejects(lambda:execute(('AB','AD')))
rejects(lambda:execute(('AC',)))
assert len(emitted)==before
rejects(lambda:validate(paths[2]+paths[2]))
forged=(('A','B','unissued','AB'),paths[2][1])
rejects(lambda:validate(forged))
print('PASS: ABC, ADB and AB-BA coexist as typed seed executions with fresh occurrence IDs.')
print('PASS: existing associative composition retains all eight events; replay creates distinct history.')
print('PASS: existing triangle spectral windows recover execution IDs; equal modes do not identify histories.')
print('PASS: bad seams, absent seed arrows, reused and forged events rejected.')
print('Scope: explicit finite adapter; no assigned edge phase, native emission law, cost calibration or physical clock.')

# Compare two explicit scheduling objectives without selecting either as physics.
cover=('AD','DB','BC','CA')
assert len({registry[e][0] for e in cover})==4
assert len({registry[e][1] for e in cover})==4
assert set(registry)-set(cover)=={'AB','BA'}
# Normalize a full directed Euler tour by its unique AB occurrence. No reversal
# identification: these are directed words, not unoriented polygons.
tours=[]
for rest in permutations(tuple(e for e in registry if e!='AB')):
    word=('AB',)+rest
    if all(registry[a][1]==registry[b][0] for a,b in zip(word,word[1:]+word[:1])):
        tours.append(word)
assert set(tours)=={
    ('AB','BC','CA','AD','DB','BA'),
    ('AB','BA','AD','DB','BC','CA'),
}
assert tours[0]==words[0]+words[1]
assert tours[1]==words[2]+cover
for word in tours:
    path=validate(execute(word))
    assert source(path)==target(path)=='A' and len(path)==6
    assert set(e[3] for e in path)==set(registry)
# Every additive primitive-edge cost gives identical total across these tours,
# since each uses every primitive once. Order/provenance nevertheless differs.
assert len(set(tours))==len(tours)
print('Full six-arrow directed tours modulo cyclic rotation:',len(tours))
for word in tours: print('  ', ' -> '.join(word))
print('PASS: full-support traversal does not uniquely schedule execution; additive edge totals cannot distinguish tours.')

# Reuse the source-symmetry criterion of check_seed_cycle_response_transport:
# automorphisms preserve the actual directed seed, not a completed K4.
vertices='ABCD'
edge_by_endpoints={ends:label for label,ends in registry.items()}
autos=[]
for image in permutations(vertices):
    mapping=dict(zip(vertices,image))
    if {(mapping[s],mapping[t]) for s,t in registry.values()}==set(registry.values()):
        autos.append(mapping)
assert len(autos)==2
swap=next(p for p in autos if p['A']!='A')
assert swap==dict(zip('ABCD','BADC'))
def normalize(word):
    k=word.index('AB')
    return word[k:]+word[:k]
def moved_tour(word,mapping):
    return normalize(tuple(edge_by_endpoints[(mapping[registry[e][0]],mapping[registry[e][1]])]
                           for e in word))
assert moved_tour(tours[0],swap)==tours[1]
assert moved_tour(tours[1],swap)==tours[0]
# No tour is fixed by the full unmarked seed symmetry. A deterministic
# equivariant choice on this seed therefore cannot select a single tour.
assert not any(all(moved_tour(t,p)==t for p in autos) for t in tours)
assert len([p for p in autos if p['A']=='A'])==1
# The second tour is ALSO two triangles when cut at the other shared vertex.
cut_at_B=tours[1][1:]+tours[1][:1]
assert cut_at_B==('BA','AD','DB','BC','CA','AB')
assert registry[cut_at_B[0]][0]==registry[cut_at_B[2]][1]=='B'
assert registry[cut_at_B[3]][0]==registry[cut_at_B[5]][1]=='B'
print('PASS: the seed automorphism A<->B,C<->D exchanges the two cyclic tours.')
print('OBSTRUCTION: no unmarked equivariant deterministic single-tour selector exists.')
print('CORRECTION: both tours split into the two triangles, at different shared endpoints.')

# Minimal seam marking: sew the two supplied triangles at a specified common
# endpoint. This is an explicit CONDITIONAL selection rule, not physical policy.
triangle_sets={frozenset(words[0]),frozenset(words[1])}
def sew_at(vertex):
    selected=[]
    for tour in tours:
        for k in range(6):
            cut=tour[k:]+tour[:k]
            if (registry[cut[0]][0]==vertex and registry[cut[2]][1]==vertex
                and registry[cut[3]][0]==vertex and registry[cut[5]][1]==vertex
                and {frozenset(cut[:3]),frozenset(cut[3:])}==triangle_sets):
                selected.append(tour)
                break
    return tuple(selected)
assert sew_at('A')==(tours[0],)
assert sew_at('B')==(tours[1],)
assert sew_at('C')==sew_at('D')==()
for vertex in 'AB':
    assert tuple(moved_tour(t,swap) for t in sew_at(vertex))==sew_at(swap[vertex])
# The shared support {A,B} is invariant; it does not pick a sewing endpoint.
assert {swap['A'],swap['B']}=={'A','B'}
# Ordered triangle roles remove this swap, but do not themselves declare a
# rule mapping roles to an endpoint. Check only the stabilizer statement.
def moved_edges(edges,mapping):
    return frozenset(edge_by_endpoints[(mapping[registry[e][0]],mapping[registry[e][1]])]
                     for e in edges)
assert moved_edges(words[0],swap)==frozenset(words[1])
assert moved_edges(words[1],swap)==frozenset(words[0])
# Both the full seed incidence and a scalar identity reference are invariant.
from check_natural_tower_return import incidence, I, scale, F
M=incidence(PACKETS)
indices=tuple(vertices.index(swap[v]) for v in vertices)
for matrix in (M,scale(I,F(2))):
    assert tuple(tuple(matrix[indices[i]][indices[j]] for j in range(4))
                 for i in range(4))==matrix
print('PASS: marking A or B selects a unique triangle-sewn tour; selector is equivariant with its marking.')
print('PASS: shared support, seed incidence and scalar identity reference do not break the tour symmetry.')

# The source spectral carrier is packet slots, not original vertices.
# On a specified full tour, successor is defined on its six execution slots.
# This combinatorial operator need not be declared a physical state update.
edge_order=tuple(registry)
def slot_compose(b,a): return tuple(b[a[i]] for i in range(len(a)))
def slot_power(a,n):
    result=tuple(range(len(a)))
    for _ in range(n): result=slot_compose(a,result)
    return result
slot_operators=[]
for tour in tours:
    successor={tour[i]:tour[(i+1)%6] for i in range(6)}
    P=tuple(edge_order.index(successor[e]) for e in edge_order)
    slot_operators.append(P)
    assert all(registry[successor[e]][0]==registry[e][1] for e in edge_order)
    assert slot_power(P,6)==tuple(range(6))
    assert all(slot_power(P,k)!=tuple(range(6)) for k in range(1,6))
    # Descending to a vertex update would require equal successors for all
    # slots projecting to the same source vertex. A and B both violate this.
    images={v:{registry[successor[e]][0] for e in edge_order if registry[e][0]==v}
            for v in vertices}
    assert images['A']=={'B','D'} and images['B']=={'A','C'}
assert slot_operators[0]!=slot_operators[1]
edge_swap=tuple(edge_order.index(edge_by_endpoints[(swap[registry[e][0]],swap[registry[e][1]])])
                for e in edge_order)
assert slot_compose(edge_swap,slot_operators[0])==slot_compose(slot_operators[1],edge_swap)
# A single six-cycle has one fixed coefficient mode. Two independent triangle
# successors would have two; equal return periods do not identify operators.
P=slot_operators[0]
assert len({slot_power(P,k)[0] for k in range(6)})==6
# Characteristic polynomial of a single six-cycle is t^6-1, not the two
# triangle short-half-phase polynomial (t-1)^2*(t^2-t+1)^2.
print('PASS: six-slot tour successor follows endpoints and returns after exactly six steps.')
print('OBSTRUCTION: full-support successor cannot descend to a deterministic four-vertex update.')
print('PASS: seed swap intertwines the two slot successors; six-cycle action is not the joint triangle half-phase.')

# Coarsest forward-stable refinement of the source-vertex observation.
# States include BOTH tour alternatives, not only a silently selected schedule.
states=tuple((t,e) for t in range(2) for e in edge_order)
next_state={(t,e):(t,edge_order[slot_operators[t][edge_order.index(e)]]) for t,e in states}
observation={(t,e):registry[e][0] for t,e in states}
def partition(signatures):
    groups={}
    for state in states: groups.setdefault(signatures[state],[]).append(state)
    return frozenset(frozenset(group) for group in groups.values())
def classes(blocks): return {state:block for block in blocks for state in block}
blocks=partition(observation); sizes=[len(blocks)]
while True:
    cls=classes(blocks)
    refined=partition({s:(cls[s],cls[next_state[s]]) for s in states})
    if refined==blocks: break
    blocks=refined; sizes.append(len(blocks))
assert sizes==[4,6,10,12]
assert all(len(block)==1 for block in blocks)
# Restricted to a fixed tour, current and next vertex distinguish its six slots.
for t in range(2):
    assert len({(observation[s],observation[next_state[s]]) for s in states if s[0]==t})==6
# On the two-tour carrier, three future steps suffice; two do not.
def future(s,steps):
    result=[observation[s]]
    for _ in range(steps):
        s=next_state[s]; result.append(observation[s])
    return tuple(result)
assert len({future(s,3) for s in states})==12
assert len({future(s,2) for s in states})==10
# Invertibility gives the equivalent finite past observer. No future oracle
# is needed once a long enough actual observation history has been retained.
previous={v:k for k,v in next_state.items()}
def past(s,steps):
    result=[observation[s]]
    for _ in range(steps):
        s=previous[s];result.append(observation[s])
    return tuple(reversed(result))
assert len({past(s,3) for s in states})==12
assert len({past(s,2) for s in states})==10
print('PASS: stable observation refinement on both tours:',sizes)
print('RESULT: fixed tour needs six occurrence states; both tours need twelve distinct predictive states.')
print('PASS: four consecutive vertex readings identify tour and slot; three are insufficient in the worst case.')

# Co-constructed reference hypothesis: extract the unique reciprocal support
# from the ORIGINAL rows, not from a preferred tour or a fitted matrix frame.
reciprocal_pairs=frozenset(frozenset((e,f)) for e,(s,t) in registry.items()
                           for f,(u,v) in registry.items() if s==v and t==u and e!=f)
assert reciprocal_pairs==frozenset((frozenset(('AB','BA')),))
seam_occurrences=next(iter(reciprocal_pairs))
assert all(sum(e in triangle for e in seam_occurrences)==1 for triangle in triangle_sets)
assert {registry[e][0] for e in seam_occurrences}=={'A','B'}
# Symmetry preserves the entire seam while exchanging its two directed roles.
assert moved_edges(seam_occurrences,swap)==seam_occurrences
assert all(moved_edges((e,),swap)!=frozenset((e,)) for e in seam_occurrences)
# Recover the seam equivariantly under every vertex renaming, not just autos.
for image in permutations(vertices):
    relabel=dict(zip(vertices,image))
    moved={e:(relabel[s],relabel[t]) for e,(s,t) in registry.items()}
    found=frozenset(frozenset((e,f)) for e,(s,t) in moved.items()
                    for f,(u,v) in moved.items() if s==v and t==u and e!=f)
    assert found==reciprocal_pairs
# Either occurrence is necessary for this bidirectional-interface criterion.
for removed in seam_occurrences:
    remaining={e:ends for e,ends in registry.items() if e!=removed}
    assert not any(s==v and t==u for e,(s,t) in remaining.items()
                   for f,(u,v) in remaining.items() if e!=f)
print('PASS: unique reciprocal seam {AB,BA} is source-extracted and equivariant; neither direction is selected.')
print('SCOPE: retained bidirectional relation, not a single invertible reference map or a derived physical readout.')

# Parallel path ports generated by that seam. Enumerate all vertex-simple
# directed paths between its endpoints, retaining words rather than values.
def simple_paths(start,end):
    found=[]
    def visit(vertex,seen,word):
        if vertex==end:
            found.append(word);return
        for label,(s,t) in registry.items():
            if s==vertex and t not in seen:
                visit(t,seen|{t},word+(label,))
    visit(start,{start},())
    return frozenset(found)
forward=simple_paths('A','B');returns=simple_paths('B','A')
assert forward==frozenset((('AB',),('AD','DB')))
assert returns==frozenset((('BA',),('BC','CA')))
roundtrips=frozenset(p+q for p in forward for q in returns)
assert roundtrips==frozenset((('AB','BA'),('AB','BC','CA'),
                            ('AD','DB','BA'),('AD','DB','BC','CA')))
assert sorted(map(len,roundtrips))==[2,3,3,4]
# Both endpoint orientations are retained. Swap exchanges forward/return
# families rather than selecting one as the physical reference direction.
def rename_word(word):
    return tuple(edge_by_endpoints[(swap[registry[e][0]],swap[registry[e][1]])] for e in word)
assert frozenset(rename_word(p) for p in forward)==returns
assert frozenset(rename_word(p) for p in returns)==forward
print('PASS: seam generates two forward and two return simple-path ports; four products recover the 2,3,3,4 cycles.')
print('BOUNDARY: reference returns are path data, not inverse or weak-unit witnesses; no averaging/readout assigned.')
