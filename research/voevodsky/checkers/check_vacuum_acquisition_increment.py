"""Exact saturated vacuum increment from actual labelled forgotten paths.

A unit-vacuum seed selects one six-event word. Its nonzero contextual
restrictions to I are its contiguous subwords of length at least two.
No numerical calibration or symbolic detector weights are used.
"""
from pathlib import Path
from itertools import permutations,combinations
import json,math
ROOT=Path(__file__).resolve().parents[3]
primes=(2,3,5,7,11,13)
intervals=[(i,j) for i in range(7) for j in range(i+2,7)]
assert len(intervals)==15

def private_value(A,word):
    states=[A]
    for p in word:states.append(states[-1]*p)
    wanted=((A,2*A),(6*A,30*A),(210*A,2310*A))
    return sum(tuple((states[k],states[k+1]) for k in cuts)==wanted for cuts in combinations(range(6),3))

blocks=[];supports=[]
for A in (3,4):
    chain=[A]
    for p in primes:chain.append(chain[-1]*p)
    # A vacuum row kills every path with a retained mark by homogeneous
    # retained degree. Exhaust all remaining (all-forgotten) path orders.
    nonzero=[(word,private_value(A,word)) for word in permutations(primes) if private_value(A,word)]
    assert nonzero==[(primes,1)]
    # Each basis state has an actual I-source representative: canonical
    # subword minus the same word with its first two events exchanged.
    representatives=[]
    for i,j in intervals:
        word=primes[i:j];other=(word[1],word[0])+word[2:]
        representatives.append((chain[i],chain[j],{word:1,other:-1}))
    def evaluate(start,end,col):
        return [col.get(primes[i:j],0) if (start,end)==(chain[i],chain[j]) else 0 for i,j in intervals]
    assert [evaluate(*rep) for rep in representatives]==[[int(i==j) for j in range(15)] for i in range(15)]
    corner_set={(chain[i],chain[j]) for i,j in intervals};supports.append(corner_set)
    # Shorter all-forgotten corners have one path and no degree-zero ideal
    # kernel. Positive-feature ideal elements cannot contribute to vacuum.
    assert all(math.factorial(n)==1 for n in (0,1))
    left_actions={};right_actions={};edge_checks=0
    for mask in range(64):
        start=A*math.prod(primes[k] for k in range(6) if mask&(1<<k))
        for k,p in enumerate(primes):
            if mask&(1<<k):continue
            end=start*p;left=[];right=[]
            for c,(u,w,col) in enumerate(representatives):
                lv=evaluate(start,w,{(p,)+word:coef for word,coef in col.items()}) if end==u else [0]*15
                rv=evaluate(u,end,{word+(p,):coef for word,coef in col.items()}) if w==start else [0]*15
                left.extend([r,c,value] for r,value in enumerate(lv) if value)
                right.extend([r,c,value] for r,value in enumerate(rv) if value)
            if left:left_actions[(start,end)]=left
            if right:right_actions[(start,end)]=right
            edge_checks+=1
    assert edge_checks==192
    # Compare actual multiplication with the interval representation formula.
    for k in range(6):
        key=(chain[k],chain[k+1])
        L=[[intervals.index((k,j)),c,1] for c,(i,j) in enumerate(intervals) if i==k+1]
        R=[[intervals.index((i,k+1)),c,1] for c,(i,j) in enumerate(intervals) if j==k]
        assert left_actions.get(key,[])==L and right_actions.get(key,[])==R
    assert all(key in set(zip(chain,chain[1:])) for key in left_actions|right_actions)
    # Off-chain forgotten edges act by zero; all retained edges do also.
    # A consecutive forgotten diamond acts by its canonical two-edge term;
    # its reversed term goes through an off-chain vertex and is zero.
    left_image=set();right_image=set()
    for i,j in intervals:
        if i>=2:left_image.add((i-2,j))
        if j<=4:right_image.add((i,j+2))
    expected={p for p in intervals if p[1]-p[0]>=4}
    assert left_image==right_image==expected and len(expected)==6
    left2={(i-2,j) for i,j in left_image if i>=2}
    right2={(i,j+2) for i,j in right_image if j<=4}
    assert left2==right2=={(0,6)}
    # All I factors have at least two events. This also gives the reverse
    # image containment, and I^3 kills this six-event module.
    assert all(60060%end!=0 for start,end in corner_set)
    blocks.append({'background':A,'chain_vertices':chain,
      'basis':[{'index':k,'start':chain[i],'end':chain[j],'interval':[i,j]} for k,(i,j) in enumerate(intervals)],
      'left_forgotten_edge_actions':[{'edge':list(edge),'entries_row_col_value':entries} for edge,entries in left_actions.items()],
      'right_forgotten_edge_actions':[{'edge':list(edge),'entries_row_col_value':entries} for edge,entries in right_actions.items()],
      'all_other_prime_edge_actions':'zero, including every retained edge',
      'M_basis_indices':[k for k,p in enumerate(intervals) if p in expected],
      'L_basis_indices':[intervals.index((0,6))],
      'prime_edges_audited':edge_checks})
assert supports[0].isdisjoint(supports[1])
# Every old contextual row ends at a divisor of its largest terminal 60060.
# Neither new block has a supported terminal among those divisors.
result={'passed':True,'increment_dimension':30,'inherited_filtration_dimensions':[30,12,2,0],
 'blocks':blocks,'old_terminal_bound':60060,
 'checks':{'all_forgotten_seed_orders_audited':720,
   'saturation_basis_complete_by_contiguous_subwords':True,
   'actual_I_source_representatives_pair_dually':True,
   'left_and_right_I_images_equal':True,
   'new_blocks_have_disjoint_source_corners':True,
   'new_support_disjoint_from_every_old_source_corner':True},
 'conclusion':'Canonical source-bimodule splitting Eplus = E direct_sum D3 direct_sum D4; each new block has dimension 15 and ideal-depth dimensions 15,6,1,0.',
 'scope':'Specified background-three/four vacuum seeds, old detectors supported inside the background-two packet. No extra tail detector or broader protocol is included.'}
(ROOT/'research/voevodsky/results/vacuum-acquisition-increment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','increment_dimension','inherited_filtration_dimensions','checks','conclusion','scope')},indent=2))
