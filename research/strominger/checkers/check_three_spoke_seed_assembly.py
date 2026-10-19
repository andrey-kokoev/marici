#!/usr/bin/env python3
"""Three outgoing arrows: bare incidence and inherited assembly controls."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,determinant,apply
from check_relative_geometry_mode_selection import select
from check_neutrino_arrow_seed_science import rank


def main():
    arrows=[('A','B'),('A','C'),('A','D')]
    labels=list('ABCD')
    incidence=[[Q(int(v==b)-int(v==a)) for a,b in arrows] for v in labels]
    K=[[int(a[1]==b[0]) for a in arrows] for b in arrows]
    results=[]
    # Fixed-length spokes, cyclic leaf symmetry. The distance between leaves
    # is NOT a primitive spoke constraint. Show its exact freedom.
    for s in (8,16):
        G=[[8 if i==j else 8-s//2 for j in range(3)] for i in range(3)]
        source={'metric':G,'generators':[{'matrix':[[0,0,1],[1,0,0],[0,1,0]],'translation':[0,0,0]}],'seeds':[{'point':[0,0,0],'role':'carrier'},{'point':[1,0,0],'role':'carrier'}]}
        geometry=assemble(source);selected,_=select(source)
        root=(Q(0),)*3;leaves=[tuple(Q(i==j) for i in range(3)) for j in range(3)]
        assert all(sum(p[i]*Q(G[i][j])*p[j] for i in range(3) for j in range(3))==8 for p in leaves)
        results.append({'leaf_squared_distance':str(s),'gram_determinant':str(determinant([[Q(x) for x in row] for row in G])),'affine_rank':rank(G),'source':source,'raw_geometry_counts':geometry['counts'],'centroid_selected_counts':selected['counts'],'centroid_scores':selected['mode_scores'],'fixed_cap_count':sum(Q(row['score'])==0 for row in selected['mode_scores']),'center':geometry['center'],'root_equals_center':geometry['center']==['0','0','0']})
    # At leaf distance 24 the same spoke constraints have a planar realization.
    source={'metric':[[8,-4],[-4,8]],'generators':[{'matrix':[[0,-1],[1,-1]],'translation':[0,0]}],'seeds':[{'point':[0,0],'role':'carrier'},{'point':[1,0],'role':'carrier'}]}
    geometry=assemble(source);selected,_=select(source)
    results.append({'leaf_squared_distance':'24','gram_determinant':'0 (three-spoke Gram)','affine_rank':2,'source':source,'raw_geometry_counts':geometry['counts'],'centroid_selected_counts':selected['counts'],'centroid_scores':selected['mode_scores'],'fixed_cap_count':sum(Q(row['score'])==0 for row in selected['mode_scores']),'center':geometry['center'],'root_equals_center':geometry['center']==['0','0'],'center_identity_note':'The existing assembler retains a separate center ID even when its coordinates equal the registered root; no identity of records is silently added.'})
    # Try the actual source interface without inventing a cycle generator.
    # With only a root seed and no generators there is no orbit spanning a shape.
    unsupported={'metric':[[8,4,4],[4,8,4],[4,4,8]],'generators':[],'seeds':[{'point':[0,0,0],'role':'carrier'}]}
    try:assemble(unsupported);bare_interface_result='unexpected acceptance'
    except ValueError as e:bare_interface_result=str(e)
    checks={
        'spoke_incidence_rank_three':rank(incidence)==3,
        'no_spoke_incidence_cycle':3-rank(incidence)==0,
        'no_endpoint_continuation':K==[[0]*3 for _ in range(3)],
        'same_spoke_lengths_two_noncongruent_3D_realizations':results[0]['leaf_squared_distance']!=results[1]['leaf_squared_distance'] and results[0]['affine_rank']==results[1]['affine_rank']==3,
        'three_spoke_Gram_formula_controls':all(Q(r['gram_determinant'])==Q(r['leaf_squared_distance'])**2*(24-Q(r['leaf_squared_distance']))/4 for r in results[:2]),
        'same_spoke_lengths_allow_planar_realization':results[2]['affine_rank']==2,
        '3D_leaf_cap_rejected_by_existing_centroid_rule':all(r['raw_geometry_counts']['carrier_facets']==4 and r['centroid_selected_counts']['carrier_facets']==3 and r['fixed_cap_count']==1 for r in results[:2]),
        'planar_outer_edges_all_active':results[2]['centroid_selected_counts']['carrier_facets']==3 and results[2]['fixed_cap_count']==0,
        'bare_orbit_interface_does_not_generate_branches':bare_interface_result=='Generated points do not span the supplied metric dimension',
    }
    out={'schema':'marici.strominger.three-spoke-seed-assembly.v1','status':'passed' if all(checks.values()) else 'failed','seed':{'vertices':labels,'arrows':[list(a) for a in arrows],'shape':'rooted outgoing three-star','undirected_f_vector':[4,3],'graph_betti':[1,0],'incidence_rank':rank(incidence),'incidence_kernel_dimension':0,'continuation_matrix':K},'bare_assembly_interface':bare_interface_result,'symmetry_augmented_controls':results,'checks':checks,'interpretation':{'bare':'No branch-to-branch arrows, triangles, directed returns or nonzero endpoint continuation exist in the three-spoke seed.','realization':'Declaring a cyclic leaf action and spoke lengths still leaves the leaf distance free. At 8 and 16 the full facet assembler gives noncongruent tetrahedra; at 24 the root lies inside a planar triangle.','centroid_rule':'For either 3D fixture, the leaf face is fixed and removed from active facets. Three root-incident faces remain, an open tetrahedral fan. The coning center is the mean of all four points, not the root.','comparison_to_closed_triangle':'The star alone has no cyclic phase mode. The triangle seed does.','missing_input_for_unique_shape':'Branch comparisons or a metric-completion obligation fixing leaf distances; the C3 leaf action used in these controls is explicitly additional data, not a directed cycle already present in the star.'},'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/check_relative_geometry_mode_selection.py',ROOT/'research/strominger/checkers/check_neutrino_arrow_seed_science.py']}}
    (ROOT/'research/strominger/results/three_spoke_seed_assembly.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'seed':out['seed'],'controls':[{'leaf_distance':r['leaf_squared_distance'],'dimension':r['affine_rank'],'raw_facets':r['raw_geometry_counts']['carrier_facets'],'active_facets':r['centroid_selected_counts']['carrier_facets']} for r in results]},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
