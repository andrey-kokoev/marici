#!/usr/bin/env python3
"""Arrow-first seed tests: exact closure, graph kernels, and metric identifiability.
Reuses the source assembly's cycle-isometry convention; no spin/charge input.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import determinant

def rank(matrix):
    a=[list(map(Q,row)) for row in matrix]; r=0
    for j in range(len(a[0]) if a else 0):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; v=a[r][j]; a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def permutation(n,cycle):
    p=list(range(n))
    for a,b in zip(cycle,cycle[1:]+cycle[:1]): p[a]=b
    return tuple(p)
def group(n,gens):
    identity=tuple(range(n)); out={identity};front=[identity]
    while front:
        p=front.pop()
        for g in gens:
            q=tuple(g[p[i]] for i in range(n))
            if q not in out:out.add(q);front.append(q)
    return out

def orbit_edges(edges,grp):
    return {tuple(sorted((p[a],p[b]))) for a,b in edges for p in grp}

def gram(D):
    return [[(D[0][i]+D[0][j]-D[i][j])/2 for j in range(1,len(D))] for i in range(1,len(D))]

def metric_test(n,adjacent_squared,other_squared):
    D=[[Q(0) if i==j else Q(adjacent_squared if (i-j)%n in (1,n-1) else other_squared) for j in range(n)] for i in range(n)]
    G=gram(D)
    minors=[determinant([[G[i][j] for j in s] for i in s]) for k in range(1,n) for s in combinations(range(n-1),k)]
    r=rank(G)
    proper=(n%2==1) if r==n-1 else (n==4 and other_squared==2*adjacent_squared and r==2)
    return {'adjacent_squared':str(adjacent_squared),'other_squared':str(other_squared),'euclidean':all(x>=0 for x in minors),'affine_rank':r,'cycle_orientation_preserving':proper,'gram_determinant':str(determinant(G))}

def main():
    specs=[(1,3,[[0,1,2]],False),(2,3,[[0,2,1]],False),(3,3,[[0,1,2],[0,2,1]],False),(4,5,[[0,1,2],[0,3,4]],False),(5,6,[[0,1,2],[3,4,5]],True),(6,4,[[0,1,2,3]],False),(7,5,[[0,1,2,3,4]],False)]
    rows=[]
    for id,n,cycles,simultaneous in specs:
        directed=[(a,b) for c in cycles for a,b in zip(c,c[1:]+c[:1])]
        gens=[permutation(n,c) for c in cycles]
        if simultaneous:
            gens=[tuple(next((g[i] for g in gens if g[i]!=i),i) for i in range(n))]
        grp=group(n,gens)
        raw={tuple(sorted(e)) for e in directed}; closed=orbit_edges(raw,grp)
        incidence=[[int(v==b)-int(v==a) for a,b in directed] for v in range(n)]
        r=rank(incidence)
        pairs=set(combinations(range(n),2)); unseen=pairs-closed
        pair_orbits=[];left=set(pairs)
        while left:
            orbit=orbit_edges({min(left)},grp);pair_orbits.append(sorted(orbit));left-=orbit
        row={'id':id,'vertices':n,'seed_cycles':[[chr(65+i) for i in c]+[chr(65+c[0])] for c in cycles],'directed_occurrences':len(directed),'undirected_edges':len(raw),'incidence_rank':r,'incidence_kernel_dimension':len(directed)-r,'connected_components':n-r,'undirected_graph_H1_dimension':len(raw)-r,'cycle_action_group_order':len(grp),'action_convention':'simultaneous two-orbit action' if simultaneous else 'each listed cycle fixes unlisted vertices','edge_closure_count':len(closed),'pair_orbit_sizes':[len(x) for x in pair_orbits],'unspecified_pair_count':len(unseen),'unspecified_pairs':[[chr(65+a),chr(65+b)] for a,b in sorted(unseen)],'complete_unit_metric_derived':not unseen}
        if not unseen:
            G=[[Q(8) if i==j else Q(4) for j in range(n-1)] for i in range(n-1)]
            row['derived_gram_rank']=rank(G);row['derived_gram_determinant']=str(determinant(G))
        rows.append(row)
    four=[metric_test(4,8,t) for t in (8,16)]
    five=[metric_test(5,8,t) for t in (4,8,16)]
    assert all(x['euclidean'] for x in four+five)
    assert [x['affine_rank'] for x in four]==[3,2]
    # Existing triangle-coordinate action C(a,b,c)=(b,c,a): derive its
    # characters rather than importing an independent spin representation.
    def mul(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    one=(Q(1),Q(0)); omega=(-Q(1,2),Q(1,2)); omega2=mul(omega,omega)
    vectors=[(one,one,one),(one,omega,omega2),(one,omega2,omega)]
    eigenvalues=[one,omega,omega2]
    character_checks=[tuple(v[1:]+v[:1])==tuple(mul(e,x) for x in v) for v,e in zip(vectors,eigenvalues)]
    checks={
        'single_three_cycle_closes_all_three_distances':rows[0]['complete_unit_metric_derived'],
        'orientation_variants_same_metric_but_different_occurrence_kernel':rows[0]['derived_gram_rank']==rows[2]['derived_gram_rank'] and rows[0]['incidence_kernel_dimension']!=rows[2]['incidence_kernel_dimension'],
        'shared_vertex_cycles_force_five_vertex_simplex_metric':rows[3]['complete_unit_metric_derived'] and rows[3]['derived_gram_rank']==4,
        'disjoint_cycles_do_not_construct_belt_cross_links':rows[4]['connected_components']==2 and rows[4]['unspecified_pair_count']==9,
        'four_cycle_metric_ambiguity_filtered_by_proper_orientation':all(x['euclidean'] for x in four) and not four[0]['cycle_orientation_preserving'] and four[1]['cycle_orientation_preserving'],
        'five_cycle_does_not_select_regular_simplex_metric':all(x['euclidean'] and x['cycle_orientation_preserving'] for x in five) and len({x['other_squared'] for x in five})==3,
        'triangle_characters_derived_from_arrow_cycle':all(character_checks) and mul(omega,omega2)==one,
        'no_spin_charge_or_flavor_decoration':True,
    }
    out={'schema':'marici.strominger.neutrino-arrow-seed-science.v1','status':'passed' if all(checks.values()) else 'failed','frozen_processor_obligations':['registered labelled arrow occurrences','listed cycles act as permutations/isometries','all supplied seed-edge squared lengths use common normalization 8','distance constraints propagate under those isometries','supporting facets and center coning only after a Euclidean realization is established'],'candidates':rows,'counterexamples':{'four_cycle':four,'five_cycle':five},'checks':checks,'interpretation':{'leading_geometric_candidate':'#1: conditional equilateral triangle, rank 2, with the existing coning rule producing a triangular disk','orientation':'#2 reverses the arrow history, not the metric; #3 retains additional directed occurrences without creating a new shape','shared_cycles':'#4 generates a regular four-simplex under the stated isometry convention; geometric overlap with the electron is not particle identity','disjoint_cycles':'#5 alone gives two components; existing neutron assembly additionally supplies relative placement and interface roles','higher_cycles':'#6 admits tetrahedral and square metrics under bare isometry, but the current proper-orientation rule rejects the tetrahedron; #7 retains noncongruent proper-isometry metrics, so the regular pentachoron still needs completion data'},'triangle_mode_analysis':{'action':'C(a,b,c)=(b,c,a)','characteristic_polynomial':'lambda^3-1','characters':['1','omega','omega^2'],'omega':'(-1+sqrt(-3))/2','eigenvectors':['(1,1,1)','(1,omega,omega^2)','(1,omega^2,omega)'],'all_three_selected':False,'selection_rule':None,'three_step_return':'I, not -I','reverse_cycle':'interchanges the omega and omega^2 character labels','physical_spin_derived':False},'next_scientific_gate':'Specify an existing source-admitted selection/attachment rule that distinguishes a triangle character as a neutrino sector; test it against proton face modes. A neutrino-specific selection or interaction witness is still required.','claim_boundary':'Exact arrow and metric-consequence tests under the existing cycle-isometry assembly convention, not a physical neutrino identification.'}
    out['source_hashes']={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/check_common_assembly_constraints.py']}
    target=ROOT/'research/strominger/results/neutrino_arrow_seed_science.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'candidates':rows,'counterexamples':out['counterexamples']},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
