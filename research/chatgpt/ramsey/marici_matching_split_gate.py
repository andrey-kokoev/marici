"""Finite control: K4 complementary-path partitions versus actual Marici seed direction.
Macro edges CD and DC retain their two-letter primitive word provenance.
No Ramsey or native color-generation law is assumed.
"""
from itertools import permutations, combinations
import json
V='ABCD'
seed={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),
      'AD':('A','D'),'DB':('D','B'),'BA':('B','A')}
macro={'CD':('C','D'),'DC':('D','C')}
lineage={'CD':('CA','AD'),'DC':('DB','BC')}
arcs={**seed,**macro}
swap=dict(zip(V,'BADC'))
def ed(a,b): return ''.join(sorted((a,b)))
def edges(path): return frozenset(ed(a,b) for a,b in zip(path,path[1:]))
def pathstr(path): return '-'.join(path)
def support_pair(paths): return tuple(sorted(tuple(pathstr(p) for p in paths)))
matchings=[frozenset([ed('A','B'),ed('C','D')]),frozenset([ed('A','C'),ed('B','D')]),frozenset([ed('A','D'),ed('B','C')])]
# Each opposite-edge pair contributes either monochromatic two edges or one of each.
all_undirected={frozenset([edges(p),edges(q)]):tuple(sorted((p,q)))
  for p in permutations(V) for q in permutations(V)
  if edges(p).isdisjoint(edges(q))}
assert len(all_undirected)==6
# Directed Hamiltonian paths built from native occurrence directions, plus two composites.
directed=[]
for p in permutations(V):
  words=[]
  for a,b in zip(p,p[1:]):
    candidates=[k for k,e in arcs.items() if e==(a,b)]
    if not candidates: break
    words.append(candidates[0])
  else: directed.append((p,tuple(words),edges(p)))
assert len(directed)==8
native=[]
for i,p in enumerate(directed):
  for q in directed[i+1:]:
    if not p[2].isdisjoint(q[2]): continue
    classified=next(j for j,matching in enumerate(matchings) if len(matching & p[2])==1)
    words=p[1]+q[1]
    assert sum(arc in lineage for arc in words)==1
    macro_edge=next(arc for arc in words if arc in lineage)
    owning_path=p if macro_edge in p[1] else q
    other_path=q if owning_path is p else p
    factors=lineage[macro_edge]
    # Both factors are in opposite-colored path, not in macro's path.
    assert all(arc in other_path[1] for arc in factors)
    native.append(dict(paths=[pathstr(p[0]),pathstr(q[0])],
                       words=[list(p[1]),list(q[1])],
                       split_matching=classified+1,macro=macro_edge,
                       macro_lineage=list(factors),
                       factors_in_other_path=True))
assert len(native)==4
native_sets=set(frozenset([p[2],q[2]]) for i,p in enumerate(directed) for q in directed[i+1:] if p[2].isdisjoint(q[2]))
missing=all_undirected.keys()-native_sets
assert len(missing)==2
# A seed automorphism acts on edge supports, not its arbitrary color labels.
def image_edges(es): return frozenset(ed(swap[e[0]],swap[e[1]]) for e in es)
def image_pair(ps): return frozenset(image_edges(p) for p in ps)
fixed=[p for p in all_undirected if image_pair(p)==p]
assert len(fixed)==2
assert missing==set(fixed)
assert {v['split_matching'] for v in native}=={2,3}
assert len([p for p in all_undirected if p not in native_sets])==2
# Derived macros carry no novel primitive occurrence; direct route equality is purely definitional.
for lab,word in lineage.items():
  assert seed[word[0]][1]==seed[word[1]][0]
  assert seed[word[0]][0]==macro[lab][0] and seed[word[-1]][1]==macro[lab][1]
# Derived unique native-directed length-four vertex cycle, up to rotation.
all_cycle_words=[]
for p in permutations(V):
  w=[]
  for a,b in zip(p,p[1:]+p[:1]):
    choice=[k for k,e in seed.items() if e==(a,b)]
    if not choice:break
    w.append(choice[0])
  else: all_cycle_words.append(tuple(w))
assert len(all_cycle_words)==4
assert {tuple(all_cycle_words[0][i:]+all_cycle_words[0][:i]) for i in range(4)}==set(all_cycle_words)
# signed 1-cycle identity w=t1+t2-h as integer vector over occurrence basis
T1={'AB':1,'BC':1,'CA':1}
T2={'AD':1,'DB':1,'BA':1}
H={'AB':1,'BA':1}
W={'BC':1,'CA':1,'AD':1,'DB':1}
assert all(T1.get(x,0)+T2.get(x,0)-H.get(x,0)==W.get(x,0) for x in seed)
result={'original_seed':seed,'directed_hamiltonian_cycle_count':len(all_cycle_words),
        'unique_cycle_up_to_rotation':list(all_cycle_words[0]),
        'derived_macro_edges':lineage,
        'total_unordered_complementary_hamiltonian_path_partitions':len(all_undirected),
        'directed_hamiltonian_paths_with_macros':len(directed),
        'directed_complementary_path_partitions':len(native),
        'all_directed_partitions':native,
        'original_seed_symmetry_fixed_undirected_partitions':len(fixed),
        'fixed_partitions_not_directed':sorted([sorted([sorted(list(a)),sorted(list(b))]) for a,b in fixed]),
        'directed_partitions_are_all_nonfixed':True,
        'each_macro_has_both_primitive_factors_in_opposite_path':True,
        'caveat':'Macro shortcuts denote two-step words; they are NOT new primitive occurrences and cannot inherit one of two Ramsey colors under the checked complementary decomposition.'}
with open('/mnt/data/marici_matching_split_gate_results.json','w') as f:json.dump(result,f,indent=2)
print('PASS: original seed directed 4-cycles',len(all_cycle_words),'up to rotation 1')
print('PASS: K4 unordered complementary path partitions',len(all_undirected))
print('PASS: with directed seed+macros, directed Hamiltonian paths',len(directed),'complementary partitions',len(native))
print('PASS: two seed-symmetry-fixed partitions cannot be realized fully directed')
print('PASS: every directed partition puts macro edge opposite its two primitive factors')
for x in native: print('   ',x['paths'],'split M'+str(x['split_matching']),'macro '+x['macro']+' factors '+','.join(x['macro_lineage']))
