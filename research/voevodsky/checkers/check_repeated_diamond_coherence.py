"""Pairwise filling bijections need not satisfy three-direction coherence.

Finite tagged coordinate source and independently fixed swap rules. Each swap
preserves outside endpoints and is involutive. Compare the two braid routes.
"""
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/voevodsky/results'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
# A path changes three independent binary coordinates, once each. At the
# interior cuts retain witness tags in Z/2. Adjacent interchange changes
# the shared intermediate coordinate state and transports its tag.
contract={'source':'Three binary coordinate directions, with a Z/2 witness tag at each cut.',
 'paths':'Each direction changes its own coordinate to a specified target. Tags are independent source witness coordinates; initial/final tags fixed.',
 'elementary_diamond':'Swap adjacent distinct directions. Unique swapped intermediate coordinate is reconstructed from outer endpoints. Transport its tag by XOR with the tag at the preceding outer cut.',
 'prediction':'Boundary-preserving involutive diamond bijections satisfy the three-direction braid coherence.',
 'scope':'Independent finite proof-relevant fixture; not an assertion that the owning operational source already supplies these swaps.'}
save(OUT/'repeated-diamond-coherence-contract.json',contract)

def states(start,target,order):
 out=[tuple(start)];current=list(start)
 for direction in order:
  current[direction]=target[direction];out.append(tuple(current))
 return out

def swap(order,tags,index,twisted):
 order=list(order); tags=list(tags)
 assert order[index]!=order[index+1]
 order[index],order[index+1]=order[index+1],order[index]
 if twisted: tags[index+1]^=tags[index]
 return tuple(order),tuple(tags)

def route(order,tags,indices,twisted):
 for i in indices:order,tags=swap(order,tags,i,twisted)
 return order,tags

bijections=0;braid_checks=0;twisted_failures=0;counterexample=None
from itertools import permutations
for start in product((0,1),repeat=3):
 for target in product((0,1),repeat=3):
  for order in permutations(range(3)):
   for tags in product((0,1),repeat=4):
    old_states=states(start,target,order)
    for i in (0,1):
     for twisted in (False,True):
      new_order,new_tags=swap(order,tags,i,twisted)
      new_states=states(start,target,new_order)
      assert new_states[i]==old_states[i] and new_states[i+2]==old_states[i+2]
      assert new_tags[i]==tags[i] and new_tags[i+2]==tags[i+2]
      assert swap(new_order,new_tags,i,twisted)==(order,tags)
      bijections+=1
    good_left=route(order,tags,(0,1,0),False)
    good_right=route(order,tags,(1,0,1),False)
    assert good_left==good_right
    bad_left=route(order,tags,(0,1,0),True)
    bad_right=route(order,tags,(1,0,1),True)
    assert bad_left[0]==bad_right[0]
    assert bad_left[1][0]==bad_right[1][0] and bad_left[1][-1]==bad_right[1][-1]
    if bad_left!=bad_right:
     twisted_failures+=1
     if counterexample is None and start==(0,0,0) and target==(1,1,1):
      counterexample={'initial_order':order,'initial_tags':tags,
       'route_010':{'order':bad_left[0],'tags':bad_left[1]},
       'route_101':{'order':bad_right[0],'tags':bad_right[1]}}
    braid_checks+=1
assert counterexample is not None
# Four directions: distant swaps commute for both transports. Together with
# involutions and braid laws these are the symmetric-group presentation.
distant_checks=0
for order in permutations(range(4)):
 for tags in product((0,1),repeat=5):
  for twisted in (False,True):
   assert route(order,tags,(0,2),twisted)==route(order,tags,(2,0),twisted)
   distant_checks+=1
report={'passed':True,'independent_fixture':True,
 'elementary_involution_and_boundary_checks':bijections,
 'three_direction_paths_tested':braid_checks,
 'twisted_braid_failures':twisted_failures,
 'distant_swap_checks':distant_checks,
 'counterexample':counterexample,
 'verdict':'PAIRWISE_EQUIVALENCE_DOES_NOT_IMPLY_HIGHER_COHERENCE',
 'positive_control':'Tag-preserving swaps satisfy involution, distant commutation and braid relations; these generate coherent permutation transport for any finite number of independent directions.',
 'negative_control':'The tag-twisted swaps are individually invertible, source-typed and boundary-preserving, but the two three-swap routes differ at an internal witness tag.',
 'identity_scope':'Tags have discrete identity. No higher identification is supplied to erase the defect. An extra homotopy would need an independently justified witness-equivalence structure.',
 'scope':'Concrete structural adversary and coherent product control, not a newly discovered defect or repair in the actual assembled observer.'}
save(OUT/'repeated-diamond-coherence.json',report)
print(json.dumps(report,indent=2))
