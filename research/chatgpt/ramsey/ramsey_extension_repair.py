#!/usr/bin/env python3
"""Exact deletion obstructions and a constructive extension-and-repair packet.
Standard library only. SAT search/proof generation live in separate scripts.
"""
from collections import Counter, deque
from itertools import combinations
import json
from pathlib import Path
from heptagon_near_extremal_counterexample import graph, independent_levels
from pauli_realization_audit import triangle_free, independent_witness, decode_graph6, encode_graph6, binary_rank
from pauli_low_cost_structure import parity_closed_heptagons
HERE=Path(__file__).resolve().parent

def add_vertex(rows,neighbors):
    n=len(rows);result=rows[:]+[neighbors]
    for v in range(n):
        if neighbors>>v&1:result[v]|=1<<n
    return result

def toggle(rows,edge):
    i,j=edge;result=rows[:];result[i]^=1<<j;result[j]^=1<<i
    return result

def independent_masks(rows,size):return independent_levels(rows,size)[size]

def deletion_obstruction():
    rows=graph();frozen=[];flexible=[]
    for i,j in combinations(range(21),2):
        if not(rows[i]>>j&1):continue
        changed=toggle(rows,(i,j));witness=independent_witness(changed,7)
        if witness is None:flexible.append((i,j))
        else:frozen.append({'edge_0based':[i,j],'independent_seven_after_deletion_0based':witness})
    assert len(flexible)==21 and len(frozen)==42
    assert all(min(j-i,21-j+i)==1 for i,j in flexible)
    core=rows[:]
    for edge in flexible:core=toggle(core,edge)
    sixes=independent_masks(rows,6);core_sevens=independent_masks(core,7)
    assert len(sixes)==112 and len(core_sevens)==210
    minimal={sum(1<<j for j in(i,(i+10)%21))for i in range(21)}
    supports={}
    for seven in core_sevens:
        deletion_support=sum(1<<i for i in range(21)if seven>>i&1 and seven>>((i+1)%21)&1)
        supports[seven]=deletion_support
        assert any(pair&deletion_support==pair for pair in minimal)
    assert minimal<=set(supports.values())
    # A valid deletion set contains no conflicting pair (i,i+10) of cycle edges.
    # The conflict graph is itself a C21, since gcd(10,21)=1.
    conflict=[(1<<((i+10)%21))|(1<<((i-10)%21))for i in range(21)]
    valid_deletion_levels=independent_levels(conflict,10)
    assert sum(map(len,valid_deletion_levels))==24476
    levels=independent_levels(core,6);neighborhood_witnesses=[];min_missed={}
    for size,level in enumerate(levels):
        minimum=112
        for neighbors in level:
            missed=[s for s in sixes if not(s&neighbors)];assert missed
            minimum=min(minimum,len(missed))
            neighborhood_witnesses.append({'neighbor_mask':neighbors,'disjoint_old_independent_six_mask':missed[0],
                                           'missed_old_sixes':len(missed)})
        min_missed[size]=minimum
    assert len(neighborhood_witnesses)==4572
    assert list(min_missed.values())==[112,80,48,29,16,7,2]
    return {'frozen_edges':frozen,'flexible_edges_0based':flexible,'frozen_core_graph6':encode_graph6(core),
            'original_independent_six_masks':sixes,'core_independent_seven_masks':core_sevens,
            'cycle_edge_deletion_supports':[{ 'independent_seven_mask':s,'required_deletion_mask':d}for s,d in sorted(supports.items())],
            'minimal_forbidden_deletion_masks':sorted(minimal),'valid_deletion_set_count':24476,
            'candidate_neighborhood_count':4572,'minimum_missed_sixes_by_size':min_missed,
            'candidate_neighborhood_witnesses':neighborhood_witnesses,
            'conclusion':'No edge-deletion-only repair can enable a Ramsey-preserving one-vertex extension, regardless of deletion count.'}

def constructive_repair():
    recipe=json.loads((HERE/'ramsey-unrestricted-repair-11.json').read_text());assert recipe['status']=='SAT'
    rows=graph();path=[];neighbors=sum(1<<v for v in recipe['new_vertex_neighbors_0based'])
    for edge in recipe['removed_old_edges_0based']:
        assert rows[edge[0]]>>edge[1]&1
        rows=toggle(rows,edge);assert triangle_free(rows)and independent_witness(rows,7)is None
        path.append({'operation':'delete','edge_0based':edge,'graph6':encode_graph6(rows)})
    assert not any(rows[v]&neighbors for v in range(21)if neighbors>>v&1)
    blockers=[s for s in independent_masks(rows,6)if not(s&neighbors)];assert len(blockers)==17
    coverage=[];remaining_counts=[len(blockers)]
    for edge in recipe['added_old_edges_0based']:
        i,j=edge;assert not(rows[i]>>j&1)
        rows=toggle(rows,edge);assert triangle_free(rows)and independent_witness(rows,7)is None
        path.append({'operation':'add','edge_0based':edge,'graph6':encode_graph6(rows)})
        coverage.append({'edge_0based':edge,'covered_blocker_masks':[s for s in blockers if s>>i&1 and s>>j&1]})
        remaining_counts.append(sum(not any(rows[v]&s for v in range(21)if s>>v&1)for s in blockers))
    assert remaining_counts==[17,10,4,0]
    assert independent_witness(rows,6,((1<<21)-1)^neighbors)is None
    extended=add_vertex(rows,neighbors)
    assert encode_graph6(extended)==recipe['graph6']
    assert triangle_free(extended)and independent_witness(extended,7)is None
    assert binary_rank(extended)==18 and not parity_closed_heptagons(extended)[0]
    return {'old_edge_edit_count':len(path),'path':path,'new_vertex_neighbors_0based':recipe['new_vertex_neighbors_0based'],
            'blockers_after_deletions':blockers,'added_edge_blocker_coverage':coverage,'remaining_blocker_counts':remaining_counts,
            'final_graph6':encode_graph6(extended),'final_degrees':[r.bit_count()for r in extended],
            'final_binary_rank':18,'final_minimum_qubits':9,'parity_closed_heptagons':0,
            'degree_four_vertices_0based':[v for v,r in enumerate(extended)if r.bit_count()==4]}

def regular_repair_path():
    recipe=json.loads((HERE/'ramsey-regular-repair-5-addition.json').read_text());assert recipe['status']=='SAT'
    moves=recipe['removed_old_edges_0based']+recipe['added_old_edges_0based'];assert len(moves)==13
    base=graph();valid={}
    for mask in range(1<<13):
        rows=base[:]
        for k,edge in enumerate(moves):
            if mask>>k&1:rows=toggle(rows,edge)
        if triangle_free(rows)and independent_witness(rows,7)is None:valid[mask]=rows
    queue=deque([0]);previous={0:None};end=(1<<13)-1
    while queue:
        mask=queue.popleft()
        if mask==end:break
        for k in range(13):
            if mask>>k&1:continue
            next_mask=mask|(1<<k)
            if next_mask in valid and next_mask not in previous:previous[next_mask]=mask;queue.append(next_mask)
    assert end in previous
    steps=[];current=end
    while previous[current]is not None:
        old=previous[current];k=(current^old).bit_length()-1
        steps.append({'operation':'delete'if k<len(recipe['removed_old_edges_0based'])else'add',
                      'edge_0based':moves[k],'graph6':encode_graph6(valid[current])});current=old
    steps.reverse();neighbors=sum(1<<v for v in recipe['new_vertex_neighbors_0based'])
    result=add_vertex(valid[end],neighbors)
    assert encode_graph6(result)==recipe['graph6']and [r.bit_count()for r in result]==[6]*22
    assert triangle_free(result)and independent_witness(result,7)is None
    return {'old_edge_edit_count':13,'valid_states_within_this_monotone_patch':len(valid),
            'path':steps,'new_vertex_neighbors_0based':recipe['new_vertex_neighbors_0based'],
            'final_graph6':recipe['graph6'],'final_binary_rank':binary_rank(result)}

def main():
    result={'schema':'marici.ramsey-extension-repair.v1','source_graph6':encode_graph6(graph()),
            'scope':'Exact growth/repair statements for the Z21 circulant with jumps ±1,±4,±6; not universal numerical edit costs.',
            'deletion_obstruction':deletion_obstruction(),'unrestricted_repair':constructive_repair(),
            'regular_repair':regular_repair_path(),
            'minimum_edit_costs':{'arbitrary_destination':11,'six_regular_destination':13},
            'lower_bound_receipts':['ramsey-unrestricted-repair-10.json','ramsey-regular-repair-4-addition-at-most.json']}
    for name in result['lower_bound_receipts']:
        receipt=json.loads((HERE/name).read_text());assert receipt['status']=='UNSAT'and receipt['proof_independently_checked']
    (HERE/'ramsey-extension-repair.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Frozen edges:',len(result['deletion_obstruction']['frozen_edges']))
    print('Safe deletion configurations:',result['deletion_obstruction']['valid_deletion_set_count'])
    print('Blockers eliminated:',result['unrestricted_repair']['remaining_blocker_counts'])
    print('Certified minimum old-edge edits:',result['minimum_edit_costs'])

if __name__=='__main__':main()
