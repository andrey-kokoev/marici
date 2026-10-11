"""Actual potential complex, PL interface maps and pullback realization checks."""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
from collections import Counter
from hashlib import sha256
import json

from potential_complex_pullback import make_contract, verify, factor, project, depth, digest, complex_cells, betti_mod2, gf2_rank, barycenter, realization_belt
from check_proton_merkle_reassembly import verify as verify_focus, POINTS
from check_proton_face_extension import geometry, mean, det
from check_proton_six_belt import topology

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'

def grid(n,total):
    if n==1: return [(Q(total),)]
    return [(Q(i),)+tail for i in range(total+1) for tail in grid(n-1,total-i)]

def refine_host(geo,host):
    old=[r['triangle'] for r in geo['triangles_and_transports']]
    points={v:tuple(map(Q,p)) for v,p in POINTS.items()}
    for triangle in old: points[triangle[0]]=mean([points[v] for v in triangle[0][2:]])
    center='realized_AB'; points[center]=mean([points[v] for v in host])
    mid={tuple(sorted(e)):'mid_'+'_'.join(sorted(e)) for e in combinations(host,2)}
    for e,name in mid.items(): points[name]=mean([points[v] for v in e])
    faces=[]
    for p in permutations(range(3)):
        v,e=host[p[0]],mid[tuple(sorted((host[p[0]],host[p[1]])))]; triangle=[v,e,center]
        if det(*(points[w] for w in triangle))<0: triangle.reverse()
        faces.append(triangle)
    for triangle in old:
        if triangle==host: continue
        hit=False
        for i,u in enumerate(triangle):
            v,w=triangle[(i+1)%3],triangle[(i+2)%3]; key=tuple(sorted((u,v)))
            if key in mid:
                m=mid[key]; faces.extend([[u,m,w],[m,v,w]]); hit=True; break
        if not hit: faces.append(triangle)
    return {'points':{v:list(map(str,p)) for v,p in points.items()},'faces':faces,'realized_vertex':center,
            'local_projection':'T barycentric coordinates in the ordered original triangle',
            'source_triangle':host}

def affine_rank(points):
    # Rational rank of differences, used to verify genuinely four-dimensional cells.
    rows=[[p[i]-points[0][i] for i in range(len(p))] for p in points[1:]]; rank=0
    for j in range(len(rows[0])):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][j]),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]; d=rows[rank][j]; rows[rank]=[x/d for x in rows[rank]]
        for i in range(len(rows)):
            if i!=rank:
                d=rows[i][j]; rows[i]=[x-d*y for x,y in zip(rows[i],rows[rank])]
        rank+=1
        if rank==len(rows): break
    return rank

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def verify_packet(packet):
    if set(packet)!={'schema','root','record','focus'} or packet['schema']!='marici.potential-pullback.v1': raise ValueError('packet schema')
    focus=packet['focus']; verify_focus(focus); geo=geometry(focus)
    host=next(r['triangle'] for r in geo['triangles_and_transports'] if r['outer_arrow']=='AB')
    record=packet['record']
    if digest(record)!=packet['root']: raise ValueError('record hash')
    expected={'kind':'potential-pullback-realization','contract':make_contract(focus['root'],host),
              'conforming_host_refinement':refine_host(geo,host),'realization_belt':realization_belt(make_contract(focus['root'],host)),
              'readout':'retain both projections and every fold flag; do not replace full pullback by its marked zero fiber'}
    if record!=expected: raise ValueError('source/realization binding')
    return verify(record['contract'])


def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); original,_=verify_focus(focus); geo=geometry(focus)
    host=next(r['triangle'] for r in geo['triangles_and_transports'] if r['outer_arrow']=='AB')
    contract=make_contract(focus['root'],host); report=verify(contract)
    global_mesh=refine_host(geo,host); host_report=topology(global_mesh['faces'])
    # Every four-simplex is an actual nondegenerate affine cell in T x C.
    def pair_point(ref):
        v=contract['P']['vertices'][ref]
        return tuple(map(Q,contract['T']['vertices'][v['T']]+contract['C']['vertices'][v['C']]))
    cells=contract['P']['maximal_simplices']; link=[s[1:] for s in cells]
    checks={'original_proton_witness_retained':original['arrows']==1836,
            'potential_complex_retains_all_24_full_flags':len(contract['C']['maximal_simplices'])==24,
            'all_four_primary_inward_cones_present':len({tuple(sorted(f[-2])) for f in contract['C']['maximal_simplices']})==4,
            'potential_is_triangulated_three_ball':betti_mod2(contract['C']['maximal_simplices'])==[1,0,0,0],
            'host_triangle_has_six_complete_flags':len(contract['T']['maximal_simplices'])==6,
            'all_144_pairs_of_host_and_potential_flags_retained':len({(tuple(r['T_flag']),tuple(r['C_flag'])) for r in contract['P']['fold_provenance']})==144,
            'three_staircases_per_flag_pair':len(cells)==432,
            'all_pullback_cells_have_affine_dimension_four':all(affine_rank([pair_point(v) for v in s])==4 for s in cells),
            'pullback_f_vector_computed':report['pullback_f_vector']==[85,600,1380,1296,432],
            'apex_link_is_not_a_three_sphere':report['apex_link_betti_mod2']==[1,1,1,1],
            'whole_pullback_is_a_cone_not_just_its_vertex':all('realized-barycenter' in s for s in cells) and len(contract['P']['vertices'])==85}
    xs=[tuple(v/6 for v in p) for p in grid(3,6)]; ys=[tuple(v/8 for v in p) for p in grid(4,8)]
    compatible=0; failed=0
    for x in xs:
        for y in ys:
            if depth(x)!=depth(y): continue
            compatible+=1
            weights=factor(x,y)
            if project(contract,weights)!=(x,y): failed+=1
    checks['mediating_map_round_trips_every_compatible_grid_pair']=compatible>2000 and failed==0
    x0=(Q(1,3),)*3; y0=(Q(1,4),)*4
    checks['zero_interface_fiber_is_exactly_barycenter_pair']=factor(x0,y0)=={'realized-barycenter':Q(1)}
    checks['unequal_interface_images_rejected']=rejected(lambda:factor(x0,(Q(1),Q(0),Q(0),Q(0))))
    # Projection reconstructions also verify arbitrary simplex combinations,
    # including interiors rather than only grid vertices.
    reconstruction=True
    for s in cells:
        weights={v:Q(i+1,15) for i,v in enumerate(s)}
        x,y=project(contract,weights)
        reconstruction &= depth(x)==depth(y) and project(contract,factor(x,y))==(x,y)
    checks['all_cell_interiors_factor_and_reconstruct']=reconstruction
    # Inward contractions agree with the interface maps at every flag vertex.
    inward=True
    for part,n in [('T',3),('C',4)]:
        for encoded in contract[part]['vertices'].values():
            point=tuple(map(Q,encoded))
            for amount in (Q(0),Q(1,3),Q(1,2),Q(1)):
                folded=tuple((1-amount)*v+amount/Q(n) for v in point)
                inward &= depth(folded)==(1-amount)*depth(point)
    checks['inward_fold_height_commutes_with_contraction']=inward
    checks['realization_is_a_conforming_vertex_of_proton_surface']=host_report['manifold_with_boundary'] and host_report['boundary_loops']==0 and host_report['euler_characteristic']==2 and host_report['vertices']==12 and host_report['faces']==20
    points={v:tuple(map(Q,p)) for v,p in global_mesh['points'].items()}
    checks['conforming_realization_preserves_original_volume']=sum(det(*(points[v] for v in t))/6 for t in global_mesh['faces'])==Q(8,3)
    # Six edges are the barycentric flag link of the marked host-face center.
    circle=['0','01','1','12','2','02']; boundary_edges=[set(t[:-1]) for t in contract['T']['maximal_simplices']]
    checks['six_belt_directions_follow_from_vertex_edge_flags']=all({a,b} in boundary_edges for a,b in zip(circle,circle[1:]+circle[:1]))
    # The potential-direction fiber remains literally fixed around this circle.
    no_twist=True
    for order in permutations(range(4)):
        boundary=[Q(0)]*4
        for i,w in zip(order,(Q(1,2),Q(1,3),Q(1,6),Q(0))): boundary[i]=w
        y=tuple(Q(1,8)+v/2 for v in boundary)
        for label in circle+[circle[0]]:
            u=tuple(map(Q,contract['T']['vertices'][label])); x=tuple(Q(1,6)+v/2 for v in u)
            no_twist &= project(contract,factor(x,y))[1]==y
    checks['all_potential_fold_charts_return_without_forced_permutation']=no_twist
    # Any flat C2 transport extending over the cone disk has even boundary parity.
    # Unknown radial bits r_i obey r_i XOR r_(i+1) = boundary_i.
    trivial_solutions=[]; twisted_solutions=[]
    for radial in range(64):
        induced=[((radial>>i)&1)^((radial>>((i+1)%6))&1) for i in range(6)]
        if induced==[0]*6: trivial_solutions.append(radial)
        if induced==[1,0,0,0,0,0]: twisted_solutions.append(radial)
    checks['trivial_transport_extends_across_realized_vertex']=len(trivial_solutions)==2
    checks['odd_belt_transport_cannot_extend_flatly_across_vertex']=len(twisted_solutions)==0
    # The topology alone cannot force the number six: the coarser stellar
    # triangle has the same depth map and a three-edge link.
    coarse=[['q','0','1'],['q','1','2'],['q','2','0']]
    checks['three_sector_coarsening_has_same_disk_topology']=betti_mod2(coarse)==[1,0,0]
    belt=realization_belt(contract); belt_report=topology(belt['quadrilaterals'])
    checks['actual_six_panel_belt_derived_at_realized_vertex']=belt_report['annulus'] and (belt_report['vertices'],belt_report['edges'],belt_report['faces'])==(12,18,6)
    checks['belt_cutting_does_not_include_or_collapse_its_center']=rejected(lambda:realization_belt(contract,Q(0),Q(1)))
    checks['belt_geometry_has_declared_depth_levels']=all(depth(tuple(map(Q,p)))==Q(belt['inner_depth'] if name.startswith('inner_') else belt['outer_depth']) for name,p in belt['vertices_in_T'].items())
    corrupted=json.loads(json.dumps(contract)); corrupted['C']['maximal_simplices'].pop()
    checks['missing_potential_fold_not_accepted_as_complete_pullback']=rejected(lambda:verify(corrupted))
    checks['serialized_contract_reverifies']=verify(json.loads(json.dumps(contract)))==report
    record={'kind':'potential-pullback-realization','contract':contract,'conforming_host_refinement':global_mesh,'realization_belt':belt,
            'readout':'retain both projections and every fold flag; do not replace full pullback by its marked zero fiber'}
    packet={'schema':'marici.potential-pullback.v1','root':digest(record),'record':record,'focus':focus}
    checks['complete_source_bound_packet_replays']=verify_packet(json.loads(json.dumps(packet)))==report
    bad=json.loads(json.dumps(packet)); bad['record']['conforming_host_refinement']['points']['realized_AB'][0]='0'; bad['root']=digest(bad['record'])
    checks['honestly_rehashed_wrong_realization_point_rejected']=rejected(lambda:verify_packet(bad))
    bad=json.loads(json.dumps(packet)); bad['record']['contract']['T_to_I']['012']='1'; bad['root']=digest(bad['record'])
    checks['honestly_rehashed_wrong_interface_map_rejected']=rejected(lambda:verify_packet(bad))
    result={'schema':'marici.potential-pullback-check.v1','passed':all(checks.values()),'checks':checks,'pullback':report,
            'compatible_grid_pairs':compatible,'host_surface':host_report,'realization_belt':belt_report,'root':packet['root'],
            'source_file_sha256':sha256(FOCUS.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_module_sha256':sha256(Path(__file__).with_name('potential_complex_pullback.py').read_bytes()).hexdigest(),
            'scope':'A specified PL pullback with full barycentric fold flags. Not all possible folding laws, not an electron identification. Odd C2 monodromy needs branching, curvature or a removed center to extend.'}
    out=BASE/'results'
    (out/'potential_complex_pullback.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (out/'potential_complex_pullback_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
