"""Lossless interface-state rival on unchanged diamond; force-free incidence tests."""
from collections import deque
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/tetrahedral-interface-state-v1.json'
OUT=ROOT/'research/strominger/results/tetrahedral-interface-state/verification.json'


def main():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'));source=json.loads((ROOT/f['source']).read_text(encoding='utf-8'));checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    check('prior_exact_source_and_all_source_pins_current',source['status']=='pass' and all(source['checks'].values()) and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in source['source_sha256'].items()))
    sites=source['site_labels'];V=len(sites);edges=[tuple(e) for e in source['edges']];E=len(edges)
    lookup={(family,tuple(n)):i for i,(family,n) in enumerate(sites)}
    check('same_source_geometry_not_new_particle_positions',V==128 and E==256 and all(sites[a][0]==0 and sites[b][0]==1 for a,b in edges))
    incident=[[] for _ in sites]
    for e,(a,b) in enumerate(edges):incident[a].append((b,e));incident[b].append((a,e))
    def boundary(j):
        q=[0]*V
        for x,(a,b) in zip(j,edges):q[a]-=x;q[b]+=x
        return q
    def gradient(q):return [q[b]-q[a] for a,b in edges]
    def H1(j):return gradient(boundary(j))
    def U1(j):return [x-y for x,y in zip(j,H1(j))]
    def U0(q):return [x-y for x,y in zip(q,boundary(gradient(q)))]
    parent=[None]*V;parent_edge=[None]*V;parent[0]=0;order=[0]
    for a in order:
        for b,e in sorted(incident[a]):
            if parent[b] is None:parent[b]=a;parent_edge[b]=e;order.append(b)
    check('connected_source_tree_rank_Vminus1',len(order)==V)
    tree={parent_edge[v] for v in order[1:]};chords=[e for e in range(E) if e not in tree]
    def encode(j):return boundary(j),[j[e] for e in chords]
    def decode(q,z):
        result=[0]*E
        for e,x in zip(chords,z):result[e]=x
        residual=[x-y for x,y in zip(q,boundary(result))]
        for v in order[:0:-1]:
            e=parent_edge[v];a,b=edges[e];sgn=1 if v==b else -1
            result[e]=sgn*residual[v];residual[parent[v]]+=residual[v];residual[v]=0
        assert residual[0]==0
        return result
    def packet_update(packet):
        q,z=packet;g=gradient(q)
        return U0(q),[x-g[e] for x,e in zip(z,chords)]
    basis=[]
    for k in range(len(chords)):
        z=[int(i==k) for i in range(len(chords))];c=decode([0]*V,z);basis.append(c)
    check('all129_fundamental_cycles_explicit_independent_and_closed',len(chords)==129 and all(not any(boundary(c)) and [c[e] for e in chords]==[int(i==k) for i in range(len(chords))] for k,c in enumerate(basis)))
    full_reconstruction=full_one=full_two=conserved=True
    for k in range(E):
        j=[int(i==k) for i in range(E)];packet=encode(j);next_j=U1(j);next_packet=packet_update(packet)
        full_reconstruction=full_reconstruction and decode(*packet)==j
        full_one=full_one and next_packet==encode(next_j) and decode(*next_packet)==next_j
        full_two=full_two and packet_update(next_packet)==encode(U1(next_j)) and decode(*packet_update(next_packet))==U1(next_j)
        delta=[a-b for a,b in zip(next_j,j)]
        conserved=conserved and all(sum(a*b for a,b in zip(c,delta))==0 for c in basis)
    check('all256_source_basis_states_reconstruct_without_loss',full_reconstruction)
    check('whole_packet_intertwines_one_application',full_one)
    check('whole_packet_preserves_two_application_composition',full_two)
    check('all129_cycle_readouts_conserved_on_every_source_basis',conserved)
    edge_index={tuple(sorted(e)):i for i,e in enumerate(edges)}
    def wrap(n):return tuple(x%4 for x in n)
    def vertex(site):family,n=site;return lookup[family,wrap(n)]
    def chain(walk):
        j=[0]*E
        for raw_a,raw_b in zip(walk,walk[1:]):
            a,b=vertex(raw_a),vertex(raw_b);e=edge_index[tuple(sorted((a,b)))];j[e]+=1 if edges[e]==(a,b) else -1
        return j
    loop=source['six_loop'];c=chain(loop)
    check('genuine_unwrapped_six_loop_not_wrapping_or_backtracking_artifact',len({vertex(v) for v in loop[:-1]})==6 and sum(x*x for x in c)==6 and not any(boundary(c)) and U1(c)==c)
    mplus=[int(x==1) for x in c];mminus=[int(x==-1) for x in c]
    def occupancy(m):
        result=[0]*V
        for x,(a,b) in zip(m,edges):result[a]+=x;result[b]+=x
        return result
    check('two_valid_pair_matchings_have_same_endpoints_and_same_boundary',sum(mplus)==sum(mminus)==3 and max(occupancy(mplus))==1 and occupancy(mplus)==occupancy(mminus) and boundary(mplus)==boundary(mminus) and [a-b for a,b in zip(mplus,mminus)]==c)
    eta=lambda j:sum(a*b for a,b in zip(c,j))
    check('actual_internal_reader_distinguishes_matchings',eta(mplus)==3 and eta(mminus)==-3)
    check('boundary_only_reader_cannot_reconstruct_internal_states',boundary(c)==boundary([0]*E) and encode(c)!=encode([0]*E) and decode(*encode(c))==c)
    check('adding_any_test_cycle_changes_internal_state_without_changing_boundary',all(boundary([a+b for a,b in zip(mminus,z)])==boundary(mminus) for z in basis))
    # An alternating cycle flip is a legal matching move under endpoint-exclusion alone.
    flipped=[1-x if c[e] else x for e,x in enumerate(mplus)]
    check('matching_flip_preserves_pairing_constraints_but_changes_role_candidate',flipped==mminus and occupancy(flipped)==occupancy(mplus) and eta(flipped)!=eta(mplus))
    check('declared_linear_update_does_not_preserve_binary_matching_domain',any(x not in (0,1) for x in U1(mplus)))
    # Center-star corner triangle, each corner step routed through that same center.
    root=(0,(0,0,0));corner0=(1,(0,0,0));corner1=(1,(-1,0,0));corner2=(1,(0,-1,0))
    fake_walk=[corner0,root,corner1,root,corner2,root,corner0]
    check('compressed_corner_triangle_has_no_independent_loop_chain',chain(fake_walk)==[0]*E)
    star_edges=[e for v,e in incident[0]]
    check('isolated_coordination_tetrahedral_star_cannot_support_circulation',len(star_edges)==4 and all(sum(1 for e in star_edges if v in edges[e])==1 for v,e in incident[0]))
    # New rival: fill this six-loop with one2-cell. Boundary-of-boundary remains zero.
    with_face=lambda j:[a+sum(x*y for x,y in zip(c,j))*b for a,b in zip(H1(j),c)]
    check('valid_higher_cell_filling_changes_loop_protection',not any(boundary(c)) and with_face(c)==[6*x for x in c] and [a-b for a,b in zip(c,with_face(c))]==[-5*x for x in c])
    # Compare against OLD source operator rather than silently calling the new one unchanged.
    medial=[{f for v in edge for w,f in incident[v]}-{e} for e,edge in enumerate(edges)]
    oldL=lambda j:[6*j[e]-sum(j[f] for f in row) for e,row in enumerate(medial)]
    relation=True
    for k in range(E):
        j=[int(i==k) for i in range(E)]
        relation=relation and H1(j)==[8*x-y for x,y in zip(j,oldL(j))]
    check('explicit_operator_change_Hodge_equals_8I_minus_old_linegraph_Laplacian',relation and oldL(c)==[8*x for x in c])
    # Half-turn of the hexagon is a translated source inversion; it swaps matchings.
    unwrapped_index_shift=(1,-1,0)
    def exchange(site):
        family,n=site;return (1-family,wrap(tuple(a-b for a,b in zip(unwrapped_index_shift,n))))
    permutation=[lookup[exchange(s)] for s in sites]
    edge_permutation=[edge_index[tuple(sorted((permutation[a],permutation[b])))] for a,b in edges]
    exchanged=[0]*E
    for e,x in enumerate(mplus):exchanged[edge_permutation[e]]=x
    check('unmarked_source_symmetry_still_exchanges_two_pairing_patterns',len(set(permutation))==V and exchanged==mminus)
    for integer_scale in (-2,-1,0,1,2):
        j=[integer_scale*x for x in c]
        check('loop_sector_not_automatically_two_states_'+str(integer_scale),not any(boundary(j)) and U1(j)==j and eta(j)==6*integer_scale)
    # Separate higher-incidence control: an actual isolated tetrahedron with all faces.
    tedges=list(combinations(range(4),2));faces=list(combinations(range(4),3));teindex={e:i for i,e in enumerate(tedges)}
    d1=[[int(v==b)-int(v==a) for a,b in tedges] for v in range(4)]
    d2=[[0]*4 for _ in tedges]
    for k,(a,b,c0) in enumerate(faces):
        for edge,sgn in [((a,b),1),((b,c0),1),((a,c0),-1)]:d2[teindex[edge]][k]=sgn
    def transpose(a):return list(map(list,zip(*a)))
    def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
    lower=mm(transpose(d1),d1);upper=mm(d2,transpose(d2))
    check('local_tetrahedron_full_face_boundary_of_boundary_zero',mm(d1,d2)==[[0]*4 for _ in range(4)])
    check('local_tetrahedron_with_all_faces_has_no_harmonic_edge_loop',[[x+y for x,y in zip(a,b)] for a,b in zip(lower,upper)]==[[4*int(i==j) for j in range(6)] for i in range(6)])
    check('tetrahedral_face_cycle_is_graph_closed_but_not_higher_cell_protected',mm(d1,[[row[0]] for row in d2])==[[0] for _ in range(4)] and any(mm(upper,[[row[0]] for row in d2])[i][0] for i in range(6)))
    paths=[HERE,FIXTURE,ROOT/f['source'],ROOT/f['source_note'],ROOT/f['literature_context']]
    report={'schema':'marici.strominger.tetrahedral-interface-state.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'status':'pass',
      'classification':'faithful_internal_loop_fiber_constructed_particle_identity_not_derived','checks':checks,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths},
      'source_sites':sites,'source_edges':edges,'source_state_dimension':E,'boundary_rank':V-1,'internal_cycle_rank':len(chords),
      'packet_displayed_coordinates':V+len(chords),'packet_independent_dimension':E,
      'tree_edges':sorted(tree),'chord_edges':chords,'fundamental_cycles_sparse':[[[e,x] for e,x in enumerate(z) if x] for z in basis],
      'true_unwrapped_loop':loop,'loop_state':c,'fake_triangle_walk':fake_walk,
      'two_pairing_patterns':{'plus':mplus,'minus':mminus,'identical_boundary':boundary(mplus),'loop_readouts':[eta(mplus),eta(mminus)],'vertex_occupancy':occupancy(mplus)},
      'lossless_packet':{'encoder':'(partial*j, j_on_chords)','decoder':'Subtract chord divergence; solve remaining tree flows by leaf elimination. All256 original basis vectors verified, plus one/two-step composition.','constraint':'sum(boundary)=0','cycle_readouts':'For every fundamental c, eta_c=c^T*j. These are conserved by U1, not generally by matching flips or filled-face continuation.'},
      'local_full_tetrahedron_control':{'edges':tedges,'faces':faces,'boundary_d1':d1,'boundary_d2':d2,'full_edge_Hodge_operator':[[x+y for x,y in zip(a,b)] for a,b in zip(lower,upper)],'result':'With all triangular faces present the edge Hodge operator is4I6: no nonzero harmonic edge circulation. Graph-only cycles are not automatically protected modes of a solid tetrahedron.'},
      'operator_boundary':{'new':'H1=partial^T*partial; U1=I-H1; U0=I-partial*partial^T','old':'L_pyrochlore=8I-H1','face_rival':'Add one2-cell with boundary c; H1_full=H1+c*c^T, so H1_full*c=6c. Geometry of vertices/edges unchanged; higher incidence is a separate changed source.'},
      'disposition':{'constructed':'Distinct internal states with identical boundary data and an exact complete interface encoding. No forces or fitted parameters.','not_constructed':['A unique binary P/N state set','Physical electric charge, spin or masses','Protection under every compatible control','A circulation confined to one tetrahedral star','Selection of no2-cell fillings or forbidden loop flips']},
      'enabled_next_test':'Classify minimal six-loop patterns modulo actual diamond symmetries, separating distinguishable invariants from merely relabeled orientations; retain full interface data and declare which higher-cell controls are admitted.',
      'physical_validation':False,'formal_outcome':None}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','classification':report['classification'],'checks':len(checks),'boundary_rank':V-1,'internal_cycle_rank':len(chords),'faithful_packet_dimension':E,'displayed_packet_coordinates':V+len(chords),'all_basis_composition_verified':E,'binary_PN_or_charge_derived':False,'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
