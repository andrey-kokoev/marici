"""Retained failure and explicit reset receipts for the conditional seed observer.
No native reset authorization or physical execution policy is claimed.
"""
from dataclasses import dataclass, replace
import check_seed_observer_switching as audit
observer=audit.observer
seed=observer.seed
transport=observer.transport

@dataclass(frozen=True)
class Monitor:
    status: str
    history: tuple
    possible: frozenset
    failure_prefix: tuple=()
    parent: object=None
    reset_receipt: str=''


def start(): return Monitor('tracking',(),observer.ALL)

def consume(m,reading):
    history=m.history+(reading,)
    if m.status=='inconsistent':
        return replace(m,history=history)  # sticky failure; no implicit reset
    possible=(observer.initialize(reading) if not m.history
              else observer.advance(m.possible,reading))
    if not possible:
        return replace(m,status='inconsistent',history=history,
                       possible=frozenset(),failure_prefix=history)
    return replace(m,history=history,possible=possible)


def reacquire(m,receipt):
    # receipt is an explicit caller-supplied record, NOT an authorization proof.
    if m.status!='inconsistent' or not receipt:
        raise ValueError('Failed episode and explicit reset receipt required')
    window=m.history[-4:]
    possible=observer.candidates(window)
    if len(window)!=4 or len(possible)!=1:
        raise ValueError('No synchronized four-reading suffix')
    return Monitor('reacquired',window,possible,parent=m,reset_receipt=receipt)

records=[]
for index,(old,replacement,delay) in enumerate(audit.cases):
    m=start()
    for reading in seed.past(old,3): m=consume(m,reading)
    assert m.possible==frozenset((old,))
    actual=replacement; failed=None
    for step in range(1,8):
        actual=seed.next_state[actual]
        m=consume(m,seed.observation[actual])
        if step==delay:
            assert m.status=='inconsistent'
            failed=m.failure_prefix
            assert observer.candidates(failed)==frozenset()
            assert observer.candidates(failed[:-1])
        if step>=delay:
            assert m.status=='inconsistent' and not m.possible
            assert m.failure_prefix==failed
    assert observer.candidates(m.history[-4:])==frozenset((actual,))
    try: reacquire(m,'')
    except ValueError: pass
    else: raise AssertionError('Silent reset accepted')
    reset=reacquire(m,f'caller-reset:{index}')
    assert reset.status=='reacquired' and reset.parent is m
    assert reset.possible==frozenset((actual,))
    actual=seed.next_state[actual]
    continued=consume(reset,seed.observation[actual])
    assert continued.parent is m and continued.reset_receipt==reset.reset_receipt
    assert continued.status=='reacquired' and continued.possible==frozenset((actual,))
    # Even a later failure retains the preceding reset provenance.
    bad=consume(continued,'invalid-vertex')
    assert bad.status=='inconsistent' and bad.parent is m
    records.extend((m,reset,continued,bad))

# Transport full immutable monitor records, not only current candidate counts.
Row=transport['Row']; indexed=transport['indexed']; unindex=transport['unindex']
source=tuple(Row(('monitor',i,m),('episode',i//4),('status',m.status),
                 ((seed.F(len(m.possible)),),)) for i,m in enumerate(records))
for policy in ('inherited','common'):
    def horizontal(rows):
        return transport['incoming_promotion'](transport['incoming_promotion'](rows,1,policy),2,policy)
    left11=indexed(source,'source');left10=indexed(unindex(left11),'target')
    right6=horizontal(source);right5=indexed(right6,'source')
    right4=indexed(unindex(right5),'target')
    assert indexed(horizontal(unindex(left11)),'source')==right5
    assert indexed(horizontal(unindex(left10)),'target')==right4
    recovered=transport['leaves'](unindex(right4))
    assert recovered==source
    assert tuple(r.label[2] for r in recovered)==tuple(records)
    for m in (r.label[2] for r in recovered):
        if m.reset_receipt:
            assert m.parent.status=='inconsistent'
            assert m.parent.failure_prefix
        if m.status=='inconsistent':
            assert not m.possible and m.failure_prefix
    print('PASS:',policy,'retains all',len(records),'failure/reset/continuation records at rung4.')
print('PASS: all 16 switches latch first failure; valid suffixes never reset implicitly.')
print('PASS: explicit reacquisition retains rejected parent episode and reset receipt, including subsequent failure.')
print('BOUNDARY: caller reset receipts are records, not native authorization; model development stops here pending source policy.')
