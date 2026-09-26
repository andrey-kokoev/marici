"""Compare full-chain observer products and their coherent attachment fibres.
Uses the independently enumerated 18-element dependent source family.
"""
import contextlib,io,json
from itertools import product
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    import check_dependent_sigma_pi_full_chains as ground
Q=ground.sources()
A={q:ground.outer_first(q) for q in Q}
B={q:ground.inner_first(q) for q in Q}
# A free observer retains two full chains, including their source entries.
def encode_observer(x,y):return A[x],B[y]
def decode_observer(o):return o[0][0],o[1][0]
def compatible(o):return o[0][-1]==o[1][-1]
observers=tuple(encode_observer(x,y) for x,y in product(Q,repeat=2))
assert all(encode_observer(*decode_observer(o))==o for o in observers)
coherent=tuple(o for o in observers if compatible(o))
assert len(coherent)==len(Q)
assert all(decode_observer(o)[0]==decode_observer(o)[1] for o in coherent)
# O x Q <-> Q^3, retaining both intermediate chains.
triples=0
for x,y,z in product(Q,repeat=3):
    left=(encode_observer(x,y),z)
    unpacked=(*decode_observer(left[0]),left[1])
    assert unpacked==(x,y,z)
    assert (encode_observer(*unpacked[:2]),unpacked[2])==left
    triples+=1
# O x O <-> Q^4: two orders of expanding the observer pairs.
quadruples=0
for x,y,z,w in product(Q,repeat=4):
    start=(encode_observer(x,y),encode_observer(z,w))
    # Q1=O x O; Q2=(Q x Q) x O; Q3=O x (Q x Q); Q4=Q^4.
    via2=(decode_observer(start[0]),start[1])
    via3=(start[0],decode_observer(start[1]))
    end2=(*via2[0],*decode_observer(via2[1]))
    end3=(*decode_observer(via3[0]),*via3[1])
    assert end2==end3==(x,y,z,w)
    assert (encode_observer(*end2[:2]),encode_observer(*end2[2:]))==start
    # Retain the compatibility conditions alongside the power coordinates.
    assert compatible(start[0])==(x==y)
    assert compatible(start[1])==(z==w)
    quadruples+=1
report={'passed':True,'ground_source_count':len(Q),
 'free_full_chain_observers':len(observers),'coherently_attached_observers':len(coherent),
 'observer_times_source_bijection_cases':triples,
 'observer_times_observer_two_route_cases':quadruples,
 'coherent_observer_times_source_count':len(coherent)*len(Q),
 'coherent_observer_times_coherent_observer_count':len(coherent)**2,
 'power_coordinate_attachment_conditions':['x=y','z=w'],
 'scope':'Finite set-valued full-chain presentations with fixed route constructions. Written general equivalence argument accompanies this check; higher identity witnesses are not represented by Boolean equality in general HoTT.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/observer-source-power-comparisons.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
