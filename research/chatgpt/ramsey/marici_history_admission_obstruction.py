#!/usr/bin/env python3
"""Exact source-relative no-go and free A4 provenance extension.

Uses the six primitive source occurrences from ActualSeedEndpointTable.agda;
constructs no native Agda proof and does not assert automatic Ramsey admission.
Only Python standard library is required.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import permutations
import json
from pathlib import Path

V = 'ABCD'
E = {
    'AB': ('A','B'), 'BC': ('B','C'), 'CA': ('C','A'),
    'AD': ('A','D'), 'DB': ('D','B'), 'BA': ('B','A')
}
I = tuple(range(4))
def perm(mapping):
    return tuple(V.index(mapping.get(v,v)) for v in V)
def comp(p,q):
    return tuple(p[q[i]] for i in I)
def inv(p):
    return tuple(p.index(i) for i in I)
def sign(p):
    return (-1)**sum(p[i]>p[j] for i in I for j in range(i+1,4))
def vertex(p,v):
    return V[p[V.index(v)]]
def endpoints(p,edge):
    return tuple(vertex(p,v) for v in E[edge])
def trans_edge(p,e):
    ep=endpoints(p,e)
    return next((f for f,ft in E.items() if ep==ft),None)

g=perm({'A':'B','B':'C','C':'A'})
h=perm({'A':'D','D':'B','B':'A'})
s=perm({'A':'B','B':'A','C':'D','D':'C'})
G={I}; frontier=[I]
while frontier:
    p=frontier.pop()
    for q in (g,h,inv(g),inv(h)):
        r=comp(p,q)
        if r not in G: G.add(r);frontier.append(r)
assert len(G)==12 and all(sign(p)==1 for p in G)
H={I,s}
assert H<=G and comp(s,s)==I
assert all(trans_edge(s,e) is not None for e in E)
assert {p for p in G if all(trans_edge(p,e) is not None for e in E)}==H

# Induced edge classes [g,e] in G x_H E, with (g,e)~(gs,s(e)).
def canon(g0,e):
    equiv=(comp(g0,s),trans_edge(s,e))
    assert equiv[1] is not None
    return min((g0,e),equiv)
def action(a,x):
    return canon(comp(a,x[0]),x[1])
def target(x):
    return endpoints(x[0],x[1])
X={canon(p,e) for p in G for e in E}
assert len(X)==36
for x in X:
    assert target(x)==target(action(I,x))
    for a in G:
        assert target(action(a,x))==tuple(vertex(a,v) for v in target(x))
        for b in G:
            assert action(a,action(b,x))==action(comp(a,b),x)

E0={canon(I,e) for e in E}
assert len(E0)==6
sheets={min(p,comp(p,s)) for p in G}
assert len(sheets)==6
sheet_edges={c:{canon(p,e) for e in E} for c in sheets for p in [c]}
assert all(len(es)==6 for es in sheet_edges.values())
assert len(set().union(*sheet_edges.values()))==36
assert all(sheet_edges[min(comp(a,c),comp(comp(a,c),s))]=={action(a,x) for x in edges}
           for c,edges in sheet_edges.items() for a in G)

fibers=defaultdict(list)
for x in sorted(X): fibers[target(x)].append(x)
assert len(fibers)==12 and all(len(es)==3 for es in fibers.values())
assert all(u!=v for u,v in fibers)
# Three action-orbits, one for each original H pair.
orbits=[]
remaining=set(X)
while remaining:
    x=min(remaining)
    orbit={action(a,x) for a in G}
    assert len(orbit)==12
    orbits.append(orbit)
    remaining-=orbit
assert len(orbits)==3
orbit_origins=[sorted(x[1] for x in orb&E0) for orb in orbits]
assert sorted(map(tuple,orbit_origins))==[('AB','BA'),('AD','BC'),('CA','DB')]
assert all(len(orb&E0)==2 for orb in orbits)

# All six complementary unordered Hamiltonian path decompositions of K4.
def undedge(u,v):return ''.join(sorted((u,v)))
all_und={undedge(u,v) for u in V for v in V if u!=v}
assert len(all_und)==6
paths={min(p,p[::-1]) for p in permutations(V)}
assert len(paths)==12
path_edges={p:frozenset(undedge(p[i],p[i+1]) for i in range(3)) for p in paths}
assert len(set(path_edges.values()))==12
pairs=set()
for p,pe in path_edges.items():
    mate=next((q for q,qe in path_edges.items() if qe==all_und-pe),None)
    assert mate is not None and mate!=p
    pairs.add(frozenset((p,mate)))
assert len(pairs)==6
def act_path(a,p):
    t=tuple(vertex(a,v) for v in p)
    return min(t,t[::-1])
def act_pair(a,d):return frozenset(act_path(a,p) for p in d)
assert all(act_pair(a,d) in pairs for a in G for d in pairs)
fixed=sorted((d for d in pairs if act_pair(s,d)==d),key=lambda d: str(sorted(d)))
assert len(fixed)==2
# Both H-fixed choices define equivariant bijections; no others exist.
phi=[]
for base in fixed:
    fmap={c:act_pair(c,base) for c in sheets}
    assert len(set(fmap.values()))==6
    assert all(fmap[min(comp(a,c),comp(comp(a,c),s))]==act_pair(a,fmap[c]) for a in G for c in sheets)
    phi.append(fmap)
assert phi[0]!=phi[1]

# Oriented Hamiltonian-path pairs are fourfold over each unoriented pair.
# Unlike the six unoriented pairs, they have NO H-fixed point.
oriented_pairs=set()
forget_orientation={}
for d in pairs:
    a,b=sorted(d)
    for pa in (a,a[::-1]):
        for pb in (b,b[::-1]):
            z=frozenset((pa,pb))
            oriented_pairs.add(z)
            forget_orientation[z]=d
assert len(oriented_pairs)==24
assert all(len([z for z in oriented_pairs if forget_orientation[z]==d])==4 for d in pairs)
def orient_action(a,z):
    return frozenset(tuple(vertex(a,v) for v in p) for p in z)
assert all(orient_action(g,z) in oriented_pairs for g in G for z in oriented_pairs)
assert all(forget_orientation[orient_action(a,z)]==act_pair(a,forget_orientation[z])
           for a in G for z in oriented_pairs)
H_fixed_oriented={z for z in oriented_pairs if orient_action(s,z)==z}
assert not H_fixed_oriented
orient_orbits=[]
left=set(oriented_pairs)
while left:
    z=next(iter(left))
    orb={orient_action(a,z) for a in G}
    orient_orbits.append(orb)
    left-=orb
assert len(orient_orbits)==2 and all(len(orb)==12 for orb in orient_orbits)
for orb in orient_orbits:
    assert all(sum(forget_orientation[z]==d for z in orb)==2 for d in pairs)

# The two native full-support directed Euler tours, modulo cyclic rotation.
# Their existence uses the declared task "use each original occurrence once".
def cyc(word):
    return min(tuple(word[j:]+word[:j]) for j in range(len(word)))
def admissible_cycle(word):
    return all(E[word[i]][1]==E[word[(i+1)%len(word)]][0]
               for i in range(len(word)))
tours={cyc(t) for t in permutations(tuple(E)) if admissible_cycle(t)}
assert len(tours)==2
assert all(set(t)==set(E) for t in tours)
def sigma_tour(t):
    return cyc(tuple(trans_edge(s,e) for e in t))
assert all(sigma_tour(t) in tours for t in tours)
assert all(sigma_tour(t)!=t and sigma_tour(sigma_tour(t))==t for t in tours)

# The induced tour carrier G x_H Tours is a canonical 12-element G-torsor.
def canon_tour(g0,t):
    return min((g0,t),(comp(g0,s),sigma_tour(t)))
tour_cover={canon_tour(a,t) for a in G for t in tours}
assert len(tour_cover)==12
def deck(z):return canon_tour(z[0],sigma_tour(z[1]))
def tour_action(a,z):return canon_tour(comp(a,z[0]),z[1])
def tour_sheet(z):return min(z[0],comp(z[0],s))
assert set(tour_sheet(z) for z in tour_cover)==sheets
assert all(sum(tour_sheet(z)==sheet for z in tour_cover)==2 for sheet in sheets)
assert all(deck(deck(z))==z and deck(z)!=z for z in tour_cover)
assert all(deck(tour_action(a,z))==tour_action(a,deck(z)) for a in G for z in tour_cover)
assert len({tour_action(a,next(iter(tour_cover))) for a in G})==12
assert all(tour_action(a,tour_action(b,z))==tour_action(comp(a,b),z)
           for z in tour_cover for a in G for b in G)

# For either H-fixed unoriented D and any chosen oriented lift z0 above it,
# there is an equivariant bijection TourCover -> G.orbit(z0) over the sheets.
# There are 2 H-fixed D choices and 4 oriented lifts each: 8 rooted maps,
# none selected by the G-set structure alone.
tour0=min(tours)
def to_oriented(a,base):
    g0,t=a
    effective=g0 if t==tour0 else comp(g0,s)
    return orient_action(effective,base)
rooted_lifts=[]
for base_unoriented in fixed:
    for base in oriented_pairs:
        if forget_orientation[base]!=base_unoriented:continue
        f={z:to_oriented(z,base) for z in tour_cover}
        assert len(set(f.values()))==12
        assert all(f[tour_action(a,z)]==orient_action(a,f[z]) for a in G for z in tour_cover)
        assert all(forget_orientation[f[z]]==act_pair(tour_sheet(z),base_unoriented)
                   for z in tour_cover)
        rooted_lifts.append(f)
assert len(rooted_lifts)==8

# Native resource bound: any complement pair has 6 macro undirected edges,
# one of which is CD. Other five need >=1 source event; CD requires >=2.
primitive_und={undedge(*xy) for xy in E.values()}
assert primitive_und==all_und-{'CD'}
assert len(E)==6 and len(all_und)==6 and 5+2>len(E)

# Unique shortest primitive route for every ordered pair; breadth-first search.
def shortest_native_route(start, stop):
    from collections import deque
    todo=deque([(start,())]);best={start:0};winners=[]
    while todo:
        vertex0, word=todo.popleft()
        if vertex0==stop:
            winners.append(word)
            if len(todo)==0 or (todo and len(todo[0][1])>len(word)):
                break
            continue
        for label,(u,v) in E.items():
            if u!=vertex0:continue
            d=len(word)+1
            if d<=best.get(v,10**9):
                best[v]=d;todo.append((v,word+(label,)))
    assert len(winners)==1,(start,stop,winners)
    return winners[0]

native_macro={(u,v):shortest_native_route(u,v) for u in V for v in V if u!=v}
assert native_macro['C','D']==('CA','AD')
assert native_macro['D','C']==('DB','BC')
def least_primitive_steps(p):
    directions=(p,p[::-1]);return min(sum(len(native_macro[d[i],d[i+1]]) for i in range(3)) for d in directions)
fixed_base_costs=[sum(least_primitive_steps(p) for p in d) for d in fixed]
assert fixed_base_costs==[9,9]

# Concrete conditional history-record lift over the induced-tour cover.
# Choose ONE of the 8 rooted maps; define the output by equivariance and
# expand every macro edge in its transported copy of the six-arrow graph.
def effective_group(z):
    return z[0] if z[1]==tour0 else comp(z[0],s)
def lifted_path_record(z,base):
    eff=effective_group(z)
    records=[]
    for seedpath in base:
        globalpath=tuple(vertex(eff,v) for v in seedpath)
        segments=[]
        for u,v in zip(seedpath,seedpath[1:]):
            primitive=native_macro[u,v]
            segments.append(tuple(canon(eff,e) for e in primitive))
        records.append((globalpath,tuple(segments)))
    return frozenset(records)
def transported_record(a,record):
    p,segs=record
    return tuple(vertex(a,v) for v in p),tuple(tuple(action(a,e) for e in seg) for seg in segs)
whole_history_lengths=set()
whole_history_unique_tokens=set()
for d in fixed:
    for orientation in oriented_pairs:
        if forget_orientation[orientation]!=d:continue
        for z in tour_cover:
            data=lifted_path_record(z,orientation)
            assert len(data)==2
            assert frozenset(p for p,_ in data)==to_oriented(z,orientation)
            all_events=[]
            for path,segs in data:
                assert len(segs)==3
                for (u,v),seg in zip(zip(path,path[1:]),segs):
                    assert seg
                    assert target(seg[0])[0]==u and target(seg[-1])[1]==v
                    assert all(target(seg[j])[1]==target(seg[j+1])[0] for j in range(len(seg)-1))
                    all_events.extend(seg)
            whole_history_lengths.add(len(all_events))
            whole_history_unique_tokens.add(len(set(all_events)))
            for a in G:
                moved=frozenset(transported_record(a,r) for r in data)
                assert moved==lifted_path_record(tour_action(a,z),orientation)
assert whole_history_lengths=={9},whole_history_lengths
assert whole_history_unique_tokens=={6},whole_history_unique_tokens

# History signature in the free noncommutative tensor algebra:
# Sig(w) = prod_{e in w}(1+X_e), truncate at word degree depth.
letters=tuple(E)
number={e:i for i,e in enumerate(letters)}
def signature(word,depth):
    out={():1}
    for e in word:
        i=number[e]
        added=Counter()
        for mon,coeff in out.items():
            if len(mon)<depth:
                added[mon+(i,)]+=coeff
        for mon,coeff in added.items():
            out[mon]=out.get(mon,0)+coeff
    return out
Xloop=('AB','BA')
Yloop=('AD','DB','BA')
def valid_loop(word):
    pos='A'
    for e in word:
        assert E[e][0]==pos,(word,e,pos)
        pos=E[e][1]
    assert pos=='A'
valid_loop(Xloop);valid_loop(Yloop)
# P_0=X, Q_0=Y; P_(k+1)=P_k Q_k, Q_(k+1)=Q_k P_k.
p,q=Xloop,Yloop
rows=[]
for depth in range(0,7):
    valid_loop(p);valid_loop(q)
    assert p!=q and p[0]=='AB' and q[0]=='AD'
    if depth>=1:assert p[-1]=='BA' and q[-1]=='BA'
    sp=signature(p,depth)
    sq=signature(q,depth)
    assert sp==sq
    spp=signature(p,depth+1)
    sqq=signature(q,depth+1)
    difference={str(tuple(letters[i] for i in mon)): spp.get(mon,0)-sqq.get(mon,0)
                for mon in set(spp)|set(sqq) if spp.get(mon,0)!=sqq.get(mon,0)}
    rows.append({'depth':depth,'length_p':len(p),'length_q':len(q),
                 'truncated_signature_equal':True,
                 'difference_at_next_degree':bool(difference),
                 'next_degree_witness':min(difference) if difference else None,
                 'first_p':' '.join(p[:7]),'first_q':' '.join(q[:7]),
                 'last_occurrences':[p[-1],q[-1]]})
    p,q=p+q,q+p
assert all(row['difference_at_next_degree'] for row in rows)
# Sharpness witness: the coefficient of AB^n AD in degree n+1 is nonzero.
# The exact formula follows by projecting away every letter except AB,AD.
p,q=Xloop,Yloop
sharpness=[]
for n in range(0,7):
    if n>=1:
        mon=(number['AB'],)*n+(number['AD'],)
        a,b=signature(p,n+1),signature(q,n+1)
        coeff=a.get(mon,0)-b.get(mon,0)
        expected=(-1)**(n-1)*2**(((n-1)*(n-2))//2)
        assert coeff==expected
        sharpness.append({'degree':n+1,'coefficient_of_AB_power_n_AD':coeff})
    p,q=p+q,q+p
# At depth2 the words are concrete and agree in S1 and S2 but not S3.
p2=Xloop+Yloop+Yloop+Xloop
q2=Yloop+Xloop+Xloop+Yloop
assert p2==('AB','BA','AD','DB','BA','AD','DB','BA','AB','BA')
assert q2==('AD','DB','BA','AB','BA','AB','BA','AD','DB','BA')
assert signature(p2,2)==signature(q2,2)
assert signature(p2,3)!=signature(q2,3)

# Exhaustive finite minimal length of the first quadratic signature collision
# with same start, finish and last primitive occurrence.
def first_degree_two_collision(max_length=10):
    for length in range(1,max_length+1):
        keys={};count=0;example=None
        def explore(start,at,word,counts,pairs):
            nonlocal count,example
            if len(word)==length:
                count+=1
                key=(start,at,word[-1],tuple(counts),tuple(pairs))
                prev=keys.get(key)
                if prev is not None and prev!=word and example is None:
                    example=(prev,word)
                keys[key]=word
                return
            for label,(u,v) in E.items():
                if u!=at: continue
                ix=number[label]
                newcounts=counts.copy();newpairs=pairs.copy()
                for j,n in enumerate(counts):newpairs[6*j+ix]+=n
                newcounts[ix]+=1
                explore(start,v,word+(label,),newcounts,newpairs)
        for st in V:
            explore(st,st,tuple(),[0]*6,[0]*36)
        if example is not None:
            return length,count,example
    raise AssertionError('quadratic collision not found')
first_collision_len,first_collision_paths_at_length,first_collision=first_degree_two_collision()
assert first_collision_len==10

report={
 'source':'ActualSeedEndpointTable.agda: six directed distinct occurrence constructors',
 'group':{'A4_order':len(G),'source_symmetry_order':len(H),
          'native_graph_stabilizer_in_A4':len(H),
          'induced_source_sheets':len(sheets),
          'free_provenance_event_count':len(X),
          'event_count_per_sheet':6,
          'event_multiplicity_per_directed_endpoint_pair':3,
          'free_extension_G_orbits':len(orbits),
          'original_events_per_G_orbit':sorted(len(orb&E0) for orb in orbits),
          'original_source_orbit_pairs':sorted(orbit_origins),
          'single_orbit_contains_all_primitive_events':False},
 'complementary_paths':{
          'K4_undirected_edges':len(all_und),
          'unordered_complementary_path_pairs':len(pairs),
          'H_fixed_basepoints':[[ ''.join(p) for p in sorted(d)] for d in fixed],
          'equivariant_bijections_from_G_over_H':len(phi),
          'oriented_path_pair_count':len(oriented_pairs),
          'oriented_lifts_per_unoriented_pair':4,
          'H_fixed_oriented_lifts':len(H_fixed_oriented),
          'G_orbits_of_oriented_pairs':sorted(len(orb) for orb in orient_orbits),
          'oriented_choices_per_unoriented_pair_in_each_regular_G_orbit':2,
          'G_equivariant_oriented_lift_of_G_over_H_exists':False,
          'G_equivariant_oriented_lift_after_double_cover_G_exists':True,
          'actual_full_support_cyclic_Euler_tours':[[e for e in t] for t in sorted(tours)],
          'seed_reflection_exchanges_Euler_tours':True,
          'induced_Euler_tour_cover_states':len(tour_cover),
          'induced_Euler_tour_cover_deck_involution_fixed_points':0,
          'induced_Euler_tour_cover_is_free_G_torsor':True,
          'rooted_equivariant_maps_to_oriented_path_orbits_over_six_state_base':len(rooted_lifts),
          'verified_full_history_lifts_of_rooted_maps':len(rooted_lifts),
          'primitive_steps_per_lifted_path_pair':list(whole_history_lengths),
          'distinct_provenance_events_per_lifted_path_pair':list(whole_history_unique_tokens),
          'duplicated_event_uses_per_lifted_path_pair':3,
          'history_lift_is_strictly_G_equivariant':True,
          'native_undirected_supports':sorted(primitive_und),
          'missing_undirected_support':['CD'],
          'minimum_primitive_steps_for_occurrence_disjoint_pair':7,
          'minimal_primitive_step_costs_for_two_H_fixed_decompositions':fixed_base_costs,
          'available_primitive_occurrences':len(E),
          'strict_occurrence_disjoint_realization_possible':False},
 'signature_countermodels':{
          'base_loops':{'X':list(Xloop),'Y':list(Yloop)},
          'recursive_family':rows,
          'sharpness_coefficients':sharpness,
          'degree_2_collision_paths':{'P2':list(p2),'Q2':list(q2)},
          'first_degree_2_collision_with_same_terminal':{'minimum_length':first_collision_len,'paths_examined_at_that_length':first_collision_paths_at_length,'example':[list(f) for f in first_collision]},
          'both_final_occurrence_BA':True,
          'finite_degree_complete_on_all_native_histories':False,
          'interpretation':'S1..Sk are compositional observer data, not native path equalities.'},
 'claim_scope':{
          'formalized_by_new_Agda':False,
          'native_six_arrow_rule_set_unchanged':True,
          'free_equivariant_extension_is_conditional_construction':True,
          'complementarity_not_derived_from_WG':True}
 }
result=Path('/mnt/data/marici_history_admission_obstruction_results.json')
result.write_text(json.dumps(report,indent=2)+'\n')
print('PASS: G=A4, six source sheets, 36 free provenance events, 3 orbits, two coset bijections')
print('PASS: oriented pairs: 24 states, no H-fixed points, two free G-orbits of 12')
print('PASS: native 2 Euler tours induce a free 12-state G-cover; 8 rooted maps to oriented paths')
print('PASS: all 8 history lifts G-equivariant; 9 event uses but only 6 distinct events')
print('PASS: strict occurrence-disjoint complementarity impossible (7 > 6)')
print('PASS: length-10 degree-2 collision, all degrees through 6 checked with distinct histories')
print('Report:',result)
