"""Force-free structural role experiment, exact integer/rational arithmetic."""
from itertools import product
from fractions import Fraction
from hashlib import sha256
from datetime import datetime,timezone
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
SOURCE=ROOT/'research/strominger/demos/dual-tetrahedral-lattices/README.md'
OUT=ROOT/'research/strominger/results/reciprocal-tetrahedral-roles/verification.json'

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def coord(n):
    i,j,k=n;return (2*(j+k),2*(i+k),2*(i+j))
def primitive(v):
    x,y,z=v;nums=(y+z-x,x+z-y,x+y-z)
    assert all(a%4==0 for a in nums)
    return tuple(a//4 for a in nums)
def rz(v):x,y,z=v;return (-y,x,z)


def main():
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    L=4;zero=(0,0,0);ones=(1,1,1)
    unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
    D=[ones,(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    sites=[(family,n) for family in (0,1) for n in product(range(L),repeat=3)]
    index={site:i for i,site in enumerate(sites)}
    def wrapped(n):return tuple(x%L for x in n)
    def neighbors(site):
        family,n=site
        return [(1-family,wrapped(add(n,scale(1 if family else -1,e)))) for e in [zero]+unit]
    adj=[[index[v] for v in neighbors(site)] for site in sites]
    check('128_sites_four_reciprocal_opposite_role_links',len(sites)==128 and all(len(set(row))==4 and all(i in adj[j] and sites[j][0]!=sites[i][0] for j in row) for i,row in enumerate(adj)))
    involution=[index[(1-f,wrapped(scale(-1,n)))] for f,n in sites]
    check('unmarked_centroid_exchange_is_exact_automorphism',all(involution[involution[i]]==i and {involution[j] for j in adj[i]}==set(adj[involution[i]]) for i in range(len(sites))))
    proper=[]
    for family,n in sites:
        x=add(coord(n),scale(family,ones));y=add(rz(x),ones);target_family=1-family
        proper.append(index[(target_family,wrapped(primitive(add(y,scale(-target_family,ones)))) )])
    check('even_proper_rotation_translation_exchanges_roles',len(set(proper))==128 and all(sites[proper[i]][0]!=sites[i][0] and {proper[j] for j in adj[i]}==set(adj[proper[i]]) for i in range(128)))
    # Displacements are unwrapped local geometry, not differences of wrapped representatives.
    stars=[D,[scale(-1,v) for v in D]]
    tensors=[]
    for moves in stars:
        tensors.append([[[sum(v[i]*v[j]*v[k] for v in moves) for k in range(3)] for j in range(3)] for i in range(3)])
    check('zeroth_first_second_moments_cannot_distinguish_roles',all(len(moves)==4 and all(sum(v[i] for v in moves)==0 for i in range(3)) and all(sum(v[i]*v[j] for v in moves)==4*int(i==j) for i in range(3) for j in range(3)) for moves in stars))
    check('third_moment_tensor_is_first_distinguishing_order',all(tensors[f][i][j][k]==(4*(-1)**f if len({i,j,k})==3 else 0) for f in (0,1) for i,j,k in product(range(3),repeat=3)))
    directions=[(1,1,1),(1,1,-1),(1,0,0),(1,1,0),(2,3,5)]
    moments=[]
    for direction in directions:
        values=[sum(dot(direction,v)**3 for v in moves) for moves in stars]
        check('cubic_directional_identity_'+str(direction),values==[24*direction[0]*direction[1]*direction[2],-24*direction[0]*direction[1]*direction[2]])
        moments.append({'normal':direction,'third_moment_A_B':values})
    normal=ones;tau=[1 if family==0 else -1 for family,n in sites]
    marked=[sum(dot(normal,v)**3 for v in stars[family])//24 for family,n in sites]
    check('single_common_oriented_boundary_readout_recovers_role',marked==tau)
    check('reversing_boundary_normal_exchanges_labels',all(sum(dot(scale(-1,normal),v)**3 for v in stars[f])==-sum(dot(normal,v)**3 for v in stars[f]) for f in (0,1)))
    check('exchange_symmetry_does_not_preserve_fixed_boundary_normal',rz(normal)!=normal)
    def step(v):return [sum(v[j] for j in row)/4 for row in adj]
    tau=list(map(Fraction,tau));one=[Fraction(1)]*128
    check('common_barycentric_update_preserves_constant',step(one)==one)
    check('one_step_flips_role_but_two_steps_preserve_it',step(tau)==[-x for x in tau] and step(step(tau))==tau)
    charge=[(1-x)/2 for x in tau]
    check('zero_one_role_score_not_conserved_by_one_step',step(charge)==[1-x for x in charge] and step(charge)!=charge)
    check('two_step_update_preserves_zero_one_role_score',step(step(charge))==charge)
    # Exact diagonal grading anticommutator, including all nonzero source entries.
    check('incidence_update_anticommutes_with_grading',all(tau[i]+tau[j]==0 for i,row in enumerate(adj) for j in row))
    check('compensating_boundary_counter_conserves_total_each_edge',all(charge[j]+(charge[i]-charge[j])==charge[i] for i,row in enumerate(adj) for j in row))
    # A genuine unwrapped six-loop. q_j-q_i is an exact edge coboundary on ANY path.
    loop=[(0,zero),(1,zero),(0,unit[0]),(1,add(unit[0],scale(-1,unit[1]))),(0,add(unit[0],scale(-1,unit[1]))),(1,scale(-1,unit[1])),(0,zero)]
    loop_ids=[index[(f,wrapped(n))] for f,n in loop]
    check('six_loop_counter_has_no_independent_residue',len(set(loop_ids[:-1]))==6 and all(loop_ids[k+1] in adj[loop_ids[k]] for k in range(6)) and sum(charge[loop_ids[k]]-charge[loop_ids[k+1]] for k in range(6))==0)
    # Pyrochlore is the line graph of diamond: its sites are diamond-bond midpoints.
    diamond_edges=[(i,j) for i,row in enumerate(adj) for j in row if i<j]
    incident=[set() for _ in sites]
    for e,(i,j) in enumerate(diamond_edges):incident[i].add(e);incident[j].add(e)
    medial=[(incident[i]|incident[j])-{e} for e,(i,j) in enumerate(diamond_edges)]
    check('midpoint_network_has_256_sites_degree6_corner_sharing_tetrahedra',len(diamond_edges)==256 and all(len(row)==6 for row in medial) and all(len(row)==4 and all(b in medial[a] for a in row for b in row if a!=b) for row in incident))
    check('every_midpoint_belongs_to_exactly_two_coordination_centers',all(sum(e in row for row in incident)==2 for e in range(256)))
    check('center_incidence_C_Ctranspose_equals_4I_plus_diamond_adjacency',all(len(incident[i]&incident[j])==(4 if i==j else int(j in adj[i])) for i in range(128) for j in range(128)))
    check('bond_incidence_Ctranspose_C_equals_2I_plus_pyrochlore_adjacency',all(len(set(diamond_edges[i])&set(diamond_edges[j]))==(2 if i==j else int(j in medial[i])) for i in range(256) for j in range(256)))
    reached={0};queue=[0]
    for i in queue:
        for j in adj[i]:
            if j not in reached:reached.add(j);queue.append(j)
    check('connected_source_certifies_one_dimensional_midpoint_readout_kernel',len(reached)==128 and all(tau[i]+tau[j]==0 for i,j in diamond_edges))
    midpoint_score=[(charge[i]+charge[j])/2 for i,j in diamond_edges]
    exchanged_score=[((1-charge[i])+(1-charge[j]))/2 for i,j in diamond_edges]
    check('symmetric_shared_corner_readout_forgets_role_polarity',midpoint_score==exchanged_score==[Fraction(1,2)]*256)
    midpoint_offsets=[[tuple(Fraction(x,2) for x in v) for v in moves] for moves in stars]
    check('midpoint_tetrahedra_have_quarter_original_squared_edge_length',all(sum(dot(v,v) for v in moves)==3 and all(sum((a[k]-b[k])**2 for k in range(3))==2 for i,a in enumerate(moves) for b in moves[i+1:]) for moves in midpoint_offsets))
    intertwined=True
    for center in range(128):
        lifted=[int(center in edge) for edge in diamond_edges]
        after_midpoint=[6*lifted[e]-sum(lifted[f] for f in row) for e,row in enumerate(medial)]
        after_center=[4*int(i==center)-int(center in adj[i]) for i in range(128)]
        intertwined=intertwined and after_midpoint==[after_center[i]+after_center[j] for i,j in diamond_edges]
    check('full_incidence_laplacian_intertwiner_preserves_operations_not_role_information',intertwined)
    edge_index={edge:e for e,edge in enumerate(diamond_edges)};cycle=[0]*256
    for k in range(6):cycle[edge_index[tuple(sorted((loop_ids[k],loop_ids[k+1])))]]=(-1)**k
    check('actual_six_loop_is_independent_midpoint_mode_invisible_to_centers',any(cycle) and all(sum(cycle[e] for e in row)==0 for row in incident) and [6*cycle[e]-sum(cycle[f] for f in row) for e,row in enumerate(medial)]==[8*x for x in cycle])
    result={'schema':'marici.strominger.reciprocal-tetrahedral-roles.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'status':'pass','checks':checks,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,SOURCE]},
      'site_count':128,'edges':[[i,j] for i,row in enumerate(adj) for j in row if i<j],
      'site_labels':sites,'unmarked_exchange':involution,'proper_exchange':proper,
      'proper_exchange_formula':'g(x)=Rz90(x)+(1,1,1); det(Rz90)=+1; exchanges A/B',
      'unwrapped_stars':stars,'third_moment_tensors':tensors,'directional_tests':moments,
      'role_grading':[int(x) for x in tau],'candidate_zero_one_score':[int(x) for x in charge],
      'counterexample_one_step_score':[int(x) for x in step(charge)],'six_loop':loop,
      'constructor':'A common oriented(111) boundary normal distinguishes roles through the cubic directional moment. Without this mark a proper Euclidean symmetry exchanges the roles.',
      'common_update':'T=adjacency/4, the same mean over four corners for both families. Incidence continuation, NOT asserted physical time evolution.',
      'control_result':'H_A directsum H_B with grading Sigma; Sigma T=-T Sigma; T^2 preserves each sector. One-step role score is not conserved.',
      'diamond_pyrochlore':{'diamond_centers':128,'bond_midpoint_sites':256,'midpoint_degree':6,'incidence_C':'rows=diamond centers, columns=diamond edges; entries1 at endpoints','identities':['C C^T=4I+A_diamond','C^T C=2I+A_pyrochlore'],'midpoint_reader':'r(edge)=(x(endpoint1)+x(endpoint2))/2','reader_kernel':'span(tau), dimension1: edge equations x_i+x_j=0 propagate on the connected bipartite graph','reader_rank':127,'independent_midpoint_cycle_dimension':len(diamond_edges)-len(sites)+1,'cycle_witness':cycle,'laplacian_intertwiner':'L_pyrochlore C^T=C^T L_diamond, with unit-weight combinatorial Laplacians. The erased role mode remains invisible under every continuation through this interface.','lost_role_example':'q and1-q both read as the constant1/2 on every shared corner','boundary_warning':'Recovering the role needs a retained staggered component or endpoint-resolved oriented data; the shared-corner geometry does not supply it automatically.'},
      'boundary_counter':'z_next=z+q(v)-q(u) conserves q+z, but telescopes around every cycle. Pure bookkeeping, not an independent electron or nontrivial holonomy.',
      'physical_validation':False,'formal_outcome':None,
      'enabled_next_test':'Construct a lossless typed boundary/interface state for a one-step role transition; determine whether it has independent reconstructible modes rather than merely an exact-gradient counter.'}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','checks':len(checks),'sites':128,'cubic_A_B':[24,-24],'one_step_preserves_role':False,'two_step_preserves_role':True,'counter_has_independent_cycle_residue':False,'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
