"""Exact K4->K5 closure census and source-policy gap audit.

Inputs: Marici six directed edges AB BC CA AD DB BA, the unique 4-cycle
A-D-B-C-A supplied by its one-in/one-out section, and the primitive reciprocal
seam A-B. CD is a derived (nonprimitive) incidence. No native WG derivations
are asserted by this standalone combinatorial checker.
"""
from itertools import permutations, combinations, product
from collections import Counter
import json

V=tuple('ABCD')
Z='Z'
E=lambda u,v:frozenset((u,v))
K4=frozenset(E(u,v) for u,v in combinations(V,2))
K5=frozenset(E(u,v) for u,v in combinations(V+(Z,),2))
source=[('A','B'),('B','C'),('C','A'),('A','D'),('D','B'),('B','A')]
assert len(source)==6


def is_path(edges):
    if len(edges)!=3: return False
    degree={v:sum(v in e for e in edges) for v in V}
    if sorted(degree.values())!=[1,1,2,2]:return False
    # With four vertices and degree multiset 1,1,2,2, only a P4 is possible
    return True

def endpoints(edges):
    assert is_path(edges)
    return frozenset(v for v in V if sum(v in e for e in edges)==1)

def monochrom_triangles(red,blue):
    return [(''.join(tri), col) for tri in combinations(V+(Z,),3)
           for col,edges in [('P',red),('Q',blue)]
           if all(E(u,v) in edges for u,v in combinations(tri,2))]

def is_c5(edges):
    return len(edges)==5 and all(sum(v in e for e in edges)==2 for v in V+(Z,))

def key_unordered(x,y):
    return tuple(sorted((tuple(sorted(''.join(sorted(e)) for e in x)), tuple(sorted(''.join(sorted(e)) for e in y)))))

raw3={key_unordered(frozenset(e for e in choice),K4-frozenset(choice)) for choice in combinations(K4,3)}
assert len(raw3)==10
allD={key_unordered(frozenset(choice),K4-frozenset(choice)) for choice in combinations(K4,3) if is_path(frozenset(choice)) and is_path(K4-frozenset(choice))}
assert len(allD)==6

# Concretely each partition as unordered immutable pair of edge sets.
Ds={frozenset((frozenset(choice), K4-frozenset(choice))) for choice in combinations(K4,3)
    if is_path(frozenset(choice)) and is_path(K4-frozenset(choice))}
assert len(Ds)==6

# Given an unordered pair, enumerate bit assignments after an arbitrary local
# but retained choice of its first member. Reversing labels just complements bits.
counts=Counter()
rows=[]
for d in Ds:
    p,q=sorted(d,key=lambda a:tuple(sorted(map(lambda e:''.join(sorted(e)),a))))
    e_p,e_q=endpoints(p),endpoints(q)
    assert e_p.isdisjoint(e_q) and e_p|e_q==frozenset(V)
    accepted=[]
    invariants=Counter()
    for bits in product((0,1),repeat=4):
        spokes_p=frozenset(E(Z,v) for v,b in zip(V,bits) if b==0)
        spokes_q=frozenset(E(Z,v) for v,b in zip(V,bits) if b==1)
        pe,qe=p|spokes_p,q|spokes_q
        good_cycles=is_c5(pe) and is_c5(qe)
        triangle_free=len(monochrom_triangles(pe,qe))==0
        assert good_cycles==triangle_free
        assert len(pe|qe)==10 and pe.isdisjoint(qe)
        if good_cycles:
            accepted.append(bits)
            assert spokes_p==frozenset(E(Z,v) for v in e_p)
            assert spokes_q==frozenset(E(Z,v) for v in e_q)
        invariants[(good_cycles, len(spokes_p),len(spokes_q))]+=1
    assert len(accepted)==1
    counts.update({'six_configs':1,'possible_extensions':16,'accepted':1,'rejected':15})
    rows.append(dict(P=sorted(''.join(sorted(e)) for e in p),Q=sorted(''.join(sorted(e)) for e in q),
                     endpoints_P=''.join(sorted(e_p)),endpoints_Q=''.join(sorted(e_q)),
                     unique_bits_P0_Q1=''.join(map(str,accepted[0])),
                     mask_classes={str(k):v for k,v in sorted(invariants.items())}))

# Source cycle and missing diagonal. All original source undirected support is
# a square plus its first diagonal; the second diagonal has path C-A-D.
square=frozenset(E(a,b) for a,b in zip('ADBC','DBCA'))
assert square==frozenset([E('A','D'), E('D','B'),E('B','C'),E('C','A')])
M=K4-square
assert M==frozenset([E('A','B'),E('C','D')])
# 4 path pairs arise from cut one cycle edge and attach it to the two diagonals.
from_cuts={frozenset((square-frozenset([f]),M|frozenset([f]))) for f in square}
assert len(from_cuts)==4 and from_cuts<=Ds
cross_sewn=Ds-from_cuts
assert len(cross_sewn)==2

# Source automorphism s=(AB)(CD) fixes two D, permutes the other four.
s={'A':'B','B':'A','C':'D','D':'C'}
def move_edge(e,p):return frozenset(p[v] for v in e)
def move_d(d,p):return frozenset(frozenset(move_edge(e,p) for e in branch) for branch in d)
fixed=[d for d in Ds if move_d(d,s)==d]
assert len(fixed)==2 and set(fixed)==cross_sewn
# For a fixed unordered D, s preserves its two constituent paths individually.
for d in fixed:
    assert all(frozenset(move_edge(e,s) for e in branch)==branch for branch in d)
# Stabilizer H on sixteen apex assignments: four fixed, three beyond unique rule.
s_fixed_bits=[bits for bits in product((0,1),repeat=4)
             if all(bits[V.index(v)]==bits[V.index(s[v])] for v in V)]
assert len(s_fixed_bits)==4

# Degree-2 closure, before triangle prohibition, can be stated without colors:
# each original vertex must receive a spoke in exactly the branch where it
# presently has degree one, and the new apex receives 2 spokes per branch.

res={
    'scope':'conditional combinatorial K4 to K5 completion; not native WG admission',
    'source_directed_edges':[a+b for a,b in source],
    'derived_shortest_CD':'CA AD',
    'source_unique_routing_cycle':'A D B C A',
    'matching_complement':['AB','CD'],
    'unordered_3_3_partitions_of_K4':len(raw3),
    'unordered_P4_P4_partitions':len(Ds),
    'cycle_cut_partitions':len(from_cuts),
    'additional_cross_sewn_partitions':len(cross_sewn),
    's_fixed_partitions':len(fixed),
    's_fixed_16_spoke_assignments':len(s_fixed_bits),
    'extension_counts':dict(counts),
    'extension_table':rows,
    'tests':{'every_P4_P4_endpoint_split':True,'every_P4_P4_has_unique_dual_C5_extension':True,'C5_C5_equals_no_monochromatic_triangle_for_each_of_96_inputs':True,
             'symmetry_alone_underdetermines_extension':True,'four_cycle_cut_4_plus_cross_sewing_2':True}
}
path='/mnt/data/ramsey_cycle_closure_native_admission_results.json'
with open(path,'w',encoding='utf-8') as f:json.dump(res,f,indent=2,sort_keys=True)
print('PASS: 6 K4 path pairs x 16 extensions = 96; each uniquely closes to two C5.')
print('PASS: 10 unordered 3+3 partitions = 6 paths + 4 nonpath.')
print('PASS: 4 cycle-cut + 2 cross-sewn; two H-fixed decomps; four H-fixed spoke patterns.')
print('result:',path)

# Five-vertex facet holonomy on K6, entirely reconstructed rather than imported.
SIX=tuple('012345')

def complete_edges(vs):
    return frozenset(E(u,v) for u,v in combinations(vs,2))

def pentagon_pairs(vs):
    assert len(vs)==5
    five=complete_edges(vs)
    ans=set()
    for t in permutations(vs[1:]):
        cycle=(vs[0],)+t
        ce=frozenset(E(cycle[k],cycle[(k+1)%5]) for k in range(5))
        rest=five-ce
        if all(sum(v in e for e in rest)==2 for v in vs):
            ans.add(frozenset([ce,rest]))
    assert len(ans)==6
    return ans


def restricted(pair,overlap):
    return frozenset(frozenset(e for e in b if e<=overlap) for b in pair)

facet={i:pentagon_pairs(tuple(v for v in SIX if v!=i)) for i in SIX}
by_overlap={}
for i,j in permutations(SIX,2):
    inter=frozenset(SIX)-{i,j}
    src={restricted(x,inter):x for x in facet[i]}
    dst={restricted(x,inter):x for x in facet[j]}
    assert len(src)==len(dst)==6 and src.keys()==dst.keys()
    by_overlap[i,j]={a:dst[key] for key,a in src.items()}
    assert len(by_overlap[i,j])==6

holonomy_count=0
cycles_by_triangle=[]
for i,j,k in permutations(SIX,3):
    mono={x:by_overlap[k,i][by_overlap[j,k][by_overlap[i,j][x]]] for x in facet[i]}
    # The resulting permutation is exactly the natural action of the
    # transposition (j k) of vertices in W_i.
    flip={j:k,k:j}
    def swapped_pair(x):
        return frozenset(frozenset(frozenset(flip.get(v,v) for v in e) for e in b) for b in x)
    assert all(mono[x]==swapped_pair(x) for x in facet[i])
    assert all(mono[x]!=x for x in facet[i])
    assert all(mono[mono[x]]==x for x in facet[i])
    holonomy_count+=1
    if i<j<k:
        cycles_by_triangle.append(''.join((i,j,k)))
assert holonomy_count==120

res['k6_overlap_holonomy']={
    'K5_facets':len(facet),
    'states_each_K5_facet':6,
    'directed_pairwise_overlap_transports':len(by_overlap),
    'ordered_triangles_checked':holonomy_count,
    'unordered_triangles_checked':len(cycles_by_triangle),
    'all_triangular_holonomies':'transposition (j k) of the other five vertices, permutation cycle type 2+2+2 on the six pentagon pairs',
    'all_holonomies_fixed_point_free':True,
    'global_section_impossible':True,
}
with open(path,'w',encoding='utf-8') as f:json.dump(res,f,indent=2,sort_keys=True)
print('PASS: 30 directed overlap transports; 120 directed triangle loops; all fixed-point-free (2,2,2).')

# Concrete H-equivariant apex-balanced rival. Both have identical uncolored
# incidence and two spokes per bundle at z, but only the first closes the paths.
P=frozenset([E('C','A'),E('A','B'),E('B','D')])
Q=frozenset([E('B','C'),E('C','D'),E('D','A')])
assert frozenset([P,Q]) in Ds
sample={}
for name,chosen in [('endpoint_closure','CD'),('opposite_balanced','AB')]:
    pe=P|frozenset(E('Z',v) for v in chosen)
    qe=Q|frozenset(E('Z',v) for v in V if v not in chosen)
    defects=monochrom_triangles(pe,qe)
    assert sum('Z' in e for e in pe)==sum('Z' in e for e in qe)==2
    assert all(frozenset(s[v] for v in edge) in pe for edge in pe if 'Z' not in edge) # old color graph s-invariant
    sample[name]={'P_spokes':chosen,'Q_spokes':''.join(v for v in V if v not in chosen),
                  'cycle_closure':is_c5(pe) and is_c5(qe),'monochromatic_triangles':defects}
assert sample['endpoint_closure']['cycle_closure'] and not sample['endpoint_closure']['monochromatic_triangles']
assert not sample['opposite_balanced']['cycle_closure']
assert set(x[0] for x in sample['opposite_balanced']['monochromatic_triangles'])=={'ABZ','CDZ'}
res['two_symmetry_invariant_balanced_rivals']=sample
with open(path,'w',encoding='utf-8') as f:json.dump(res,f,indent=2,sort_keys=True)
print('PASS: s-invariant apex-balanced rival preserves source incidences but has triangles ABZ and CDZ.')
