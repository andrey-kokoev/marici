"""History -> compatible states -> next observations through retained transports.
Exact finite observer for the declared fixed-tour dynamics, not a physical reader.
"""
from itertools import product
import check_seed_tour_family_transport as family
seed=family.seed
transport=family.transport
Row=transport['Row']; leaves=transport['leaves']
indexed=transport['indexed']; unindex=transport['unindex']; promote=transport['incoming_promotion']

ALL=frozenset(seed.states)
def candidates(history):
    history=tuple(history)
    if not history: return ALL
    return frozenset(s for s in ALL if seed.past(s,len(history)-1)==history)

def predictions(possible):
    return frozenset(seed.observation[seed.next_state[s]] for s in possible)

def advance(possible,reading):
    return frozenset(seed.next_state[s] for s in possible
                     if seed.observation[seed.next_state[s]]==reading)

# Initial reading filters states without advancing an unobserved time step.
def initialize(reading):
    return frozenset(s for s in ALL if seed.observation[s]==reading)

histories=[()]
for size in range(1,5):
    for history in product(seed.vertices,repeat=size):
        possible=candidates(history)
        if possible:
            histories.append(history)
            assert all(seed.observation[s]==history[-1] for s in possible)
            if size==4: assert len(possible)==1
        else:
            assert not predictions(possible)
assert len(histories)==1+4+6+10+12
assert candidates(('A','A'))==frozenset()
assert candidates(('Z',))==frozenset()
assert candidates(())==ALL
assert initialize('A')==candidates(('A',))
assert any(len(candidates(h))>1 for h in histories if len(h)==3)

# Exact incremental filtering, prediction and four-reading memory on every
# trajectory, including startup and more than one complete return.
for start in seed.states:
    state=start; history=(seed.observation[state],)
    possible=initialize(history[0])
    for step in range(13):
        assert state in possible
        assert possible==candidates(history)==candidates(history[-4:])
        if len(history)>=4: assert possible==frozenset((state,))
        following=seed.next_state[state]; reading=seed.observation[following]
        assert reading in predictions(possible)
        if len(possible)==1: assert predictions(possible)==frozenset((reading,))
        updated=advance(possible,reading)
        history+=reading,
        assert updated==candidates(history)
        possible=updated;state=following

# Histories are the payload available to the reader. No actual hidden state
# or selected tour is attached to these rows. Numeric value is a diagnostic
# cardinality only, never a probability or the authority for reconstruction.
source=tuple(Row(('history',i,h),('length',len(h)),('last',h[-1] if h else 'unobserved'),
                 ((seed.F(len(candidates(h))),),)) for i,h in enumerate(histories))
def read(rows):
    original=leaves(rows)
    assert original==source
    return tuple((r.label[2],candidates(r.label[2]),predictions(candidates(r.label[2])))
                 for r in original)
expected=read(source)
for policy in ('inherited','common'):
    def horizontal(rows): return promote(promote(rows,1,policy),2,policy)
    left11=indexed(source,'source');left10=indexed(unindex(left11),'target')
    right6=horizontal(source);right5=indexed(right6,'source')
    right4=indexed(unindex(right5),'target')
    assert indexed(horizontal(unindex(left11)),'source')==right5
    assert indexed(horizontal(unindex(left10)),'target')==right4
    assert read(unindex(right4))==expected
    for history,possible,predicted in read(unindex(right4)):
        if not history: continue
        for reading in seed.vertices:
            assert advance(possible,reading)==candidates(history+(reading,))
    print('PASS:',policy,'rung4 observer reconstructs all',len(histories),'startup/window records.')
print('PASS: exact filtering and next-reading predictions on all 12 states for 13 updates each.')
print('PASS: four-reading memory suffices; ambiguous startup retains alternatives; impossible readings give empty set.')
print('Scope: fixed-tour model, exact labelled observations; no noise model, tour switching or physical calibration.')
