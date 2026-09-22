"""Residual-only reconstruction on the exact three-forgotten-diamond cube.

No original source capsule, producer lookup, or numerical response model is
available to decode(). The public typed basis is model metadata, not input
coefficients. Uses the existing independent exact ordered-cut recorder.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import runpy,json,copy
ROOT=Path(__file__).resolve().parents[3]
f=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
N=3

def path(bits,n=N,offset=0):
    word=[]
    for i in range(n):
        pair=(2*(offset+i),2*(offset+i)+1)
        word.extend(reversed(pair) if bits&(1<<i) else pair)
    return tuple(word),(0,)*(2*n)

def source(a,n=N,offset=0):
    return {path(bits,n,offset):c for bits,c in enumerate(a) if c}

def moments(a):
    return [sum((a[b] for b in range(len(a)) if b&t==t),Fraction(0)) for t in range(len(a))]

def inverse(m):
    return [sum(((-1)**((t^b).bit_count())*m[t] for t in range(len(m)) if t&b==b),Fraction(0)) for b in range(len(m))]

def mode(t,n=N,offset=0):
    m=[Fraction(int(j==t)) for j in range(1<<n)]
    return source(inverse(m),n,offset)

def selected_row(t):
    return tuple(('e',(1<<(2*i))-1,((1<<(2*i))-1)|(1<<(2*i+1)),0)
                 for i in range(N) if t&(1<<i))

def wire(x):return json.loads(json.dumps(x))

def lower(envelope):
    """Discard one observable order only after moving it into its residual."""
    out=wire(envelope);r=out['observable_order']
    if r<=0:raise ValueError('already terminal')
    keys=[str(t) for t in range(8) if t.bit_count()==r]
    out['residuals'].append({'order':r,'coordinates':{k:out['visible_moments'].pop(k) for k in keys}})
    out['observable_order']=r-1
    return wire(out)

def decode(envelope):
    """Reconstruct exclusively from the received coordinate bundles."""
    if envelope.get('schema')!='diamond-cube-residual-v1':raise ValueError('schema')
    if envelope.get('event_primes')!=[2,3,5,7,11,13] or envelope.get('background')!=2:raise ValueError('source labels')
    r=envelope['observable_order']
    if type(r) is not int or not 0<=r<=3:raise ValueError('order')
    visible=envelope['visible_moments']
    if set(visible)!={str(t) for t in range(8) if t.bit_count()<=r}:raise ValueError('incomplete visible coordinates')
    bundles=envelope['residuals']
    if [b['order'] for b in bundles]!=list(range(3,r,-1)):raise ValueError('missing or reordered residual')
    coordinates=dict(visible)
    for b in bundles:
        if set(b['coordinates'])!={str(t) for t in range(8) if t.bit_count()==b['order']}:raise ValueError('residual labels')
        coordinates.update(b['coordinates'])
    m=[Fraction(coordinates[str(t)]) for t in range(8)]
    return source(inverse(m))

# Each moment is an actual ordered Fox row, not an invented score.
basis=[source([Fraction(int(i==b)) for i in range(8)]) for b in range(8)]
records={r:[f['vacuum_rows'](0,63,col,r) for col in basis] for r in range(4)}
for b,col in enumerate(basis):
    m=moments([Fraction(int(i==b)) for i in range(8)])
    for t in range(8):assert records[t.bit_count()][b].get(selected_row(t),0)==m[t]
ranks=[f['rank'](records[r]) for r in range(4)]
assert ranks==[1,4,7,8]
# Modes are products of H=Q-P in the selected blocks and P elsewhere.
# They lie in I^|T|. Their first nonzero selected moment is at that order,
# proving the ideal-power intersections on this slice, using D_k(I^r)=0.
for t in range(8):
    col=mode(t)
    for r in range(t.bit_count()):assert not f['vacuum_rows'](0,63,col,r)
    assert f['vacuum_rows'](0,63,col,t.bit_count()).get(selected_row(t),0)==1

samples=[[Fraction(int(i==b)) for i in range(8)] for b in range(8)]
samples += [inverse([Fraction(int(i==t)) for i in range(8)]) for t in range(8)]
samples += [[Fraction(x) for x in ('1/2','-2','0','3/7','-1','5/3','2','-4/5')]]
handoffs=0;saved=None
for a in samples:
    original=source(a)
    envelope={'schema':'diamond-cube-residual-v1','background':2,
              'event_primes':[2,3,5,7,11,13],'observable_order':3,
              'visible_moments':{str(t):str(c) for t,c in enumerate(moments(a))},'residuals':[]}
    assert decode(wire(envelope))==original
    for _ in range(3):
        envelope=lower(envelope)
        assert decode(envelope)==original
        handoffs+=1
    # No input path coefficients, original source object or source hash is
    # stored in the final envelope. All data are typed observable/residual coordinates.
    assert set(envelope)=={'schema','background','event_primes','observable_order','visible_moments','residuals'}
    saved=envelope
# Dropping any order identifies an actual nonzero source mode with zero
# in all remaining coordinates. Detect deletion as a protocol violation.
for r in (1,2,3):
    t=next(t for t in range(8) if t.bit_count()==r)
    m=moments(inverse([Fraction(int(j==t)) for j in range(8)]))
    assert all(c==0 for j,c in enumerate(m) if j.bit_count()!=r)
    bad=copy.deepcopy(saved);bad['residuals']=[b for b in bad['residuals'] if b['order']!=r]
    try:decode(bad)
    except ValueError:pass
    else:raise AssertionError('missing residual accepted')

# Actual source multiplication: concatenate compatible block packets.
# Moment modes multiply by union of their block labels; ideal degree adds.
action_checks=0
for n,m in ((1,1),(1,2),(2,1)):
    for t,u in product(range(1<<n),range(1<<m)):
        lhs=f['multiply'](mode(t,n),mode(u,m,n))
        rhs=mode(t|(u<<n),n+m)
        assert lhs==rhs
        assert t.bit_count()+u.bit_count()==(t|(u<<n)).bit_count()
        action_checks+=1

# The owning vacuum row selects the all-P path, not the all-Q moment.
vacuum=(('e',0,1,0),('e',3,7,0),('e',15,31,0))
for a in samples:
    col=source(a);m=moments(a)
    value=f['vacuum_rows'](0,63,col,3).get(vacuum,0)
    assert value==a[0]==sum((-1)**t.bit_count()*m[t] for t in range(8))
    recovered_top=sum((-1)**t.bit_count()*m[t] for t in range(7))-value
    assert recovered_top==m[7]
# Vacuum + terminal has rank 2, whereas all lower-order moments + vacuum
# have rank 8. New acquisition can replace the last residual only when
# the other missing coordinates have already been retained.
terminal_vacuum=[{0:Fraction(1),1:Fraction(int(b==0))} for b in range(8)]
assert f['rank'](terminal_vacuum)==2
k=f['multiply'](f['multiply'](f['relation']((0,1),0),f['relation']((2,3),0)),f['relation']((4,5),0))
assert k=={key:-c for key,c in mode(7).items()}
assert all(not f['vacuum_rows'](0,63,k,r) for r in range(3))
assert f['vacuum_rows'](0,63,k,3).get(vacuum,0)==1
# Identical initial terminal views can make different future predictions.
tail=f['multiply'](f['relation']((2,3),0),f['relation']((4,5),0))
predictions=[]
for first in (source([Fraction(1),Fraction(0)],1),source([Fraction(0),Fraction(1)],1)):
    predictions.append(f['vacuum_rows'](0,63,f['multiply'](first,tail),3).get(vacuum,0))
assert predictions==[1,0]
report={'passed':True,'source_slice':'eight forgotten paths from three ordered two-event blocks',
 'ordered_record_ranks_by_cut_order':ranks,'source_ideal_filtration_dimensions':[8,7,4,1,0],
 'minimal_linear_residual_dimensions_for_D3_to_D2_to_D1_to_D0':[1,3,3],
 'reconstruction_samples':len(samples),'serialized_residual_handoffs':handoffs,
 'typed_source_product_checks':action_checks,'terminal_plus_vacuum_rank':2,
 'missing_dimensions_if_only_terminal_and_vacuum_retained':6,
 'checks':{'no_original_source_capsule':True,'actual_fox_rows_match_moments':True,
 'exact_residual_only_reconstruction':True,'each_deleted_residual_order_has_a_nonzero_blind_witness':True,
 'vacuum_recovers_top_residual_given_all_lower_moments':True,
 'equal_terminal_states_have_different_future_vacuum_predictions':True},
 'scope':'Exact fixed finite forgotten cube and its compatible block concatenations. Not a proof for arbitrary marked sources, complete source-bimodule splitting, noisy acquisition, or completed domains. Rank minimality concerns linear residual coordinates.'}
out=ROOT/'research/voevodsky/results'
(out/'diamond-cube-residual-retention.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'diamond-cube-residual-envelope.json').write_text(json.dumps(saved,indent=2)+'\n')
print(json.dumps(report,indent=2))
