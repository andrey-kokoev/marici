"""Exact common-process regression and hostile controls for mixed arrows."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as Q
import hashlib,json
from assemble_real_complex_arrows import ROOT,run,decode,assemble,evolve


def main():
    source_path=ROOT/'research/strominger/inputs/neutron-real-complex-arrows.json'
    legacy_path=ROOT/'research/voevodsky/inputs/mode-neutron.json'
    source=json.loads(source_path.read_text());legacy=json.loads(legacy_path.read_text());result=run(source)
    # Exact coordinate permutation (X,Y,Z) -> (Y,Z,X), no projection.
    order=[1,2,0]
    rebased={'metric':[[str(Q(legacy['metric'][i][j])) for j in order] for i in order],
             'generators':[{'matrix':[[str(Q(g['matrix'][i][j])) for j in order] for i in order],
                            'translation':[str(Q(g['translation'][i])) for i in order]} for g in legacy['generators']],
             'seeds':[{'point':[str(Q(s['point'][i])) for i in order],'role':s['role']} for s in legacy['seeds']]}
    checks={'arrows_recover_existing_neutron_action_exactly':result['decoded_source']==rebased,
            'same_full_geometry_in_same_basis':result['geometry']==assemble(rebased),
            'same_complete_cycle_in_same_basis':result['cycle']==evolve(rebased),
            'input_arrows_retained_exactly':result['arrow_source']==source,
            'six_vertices_eight_facets':len(result['geometry']['vertices'])==6 and len(result['geometry']['supporting_facets'])==8,
            'six_moving_two_fixed':result['cycle']['geometry']['counts']['carrier_facets']==6 and result['cycle']['geometry']['counts']['external_interfaces']==2,
            'three_step_return':result['cycle']['scheduled_atomic_steps_to_word_return']==3}
    caps=[p for p in result['coordinates']['facet_centroids'] if p['complex']==[['0','0']]]
    checks['coincident_planar_caps_retain_real_separation']=len(caps)==2 and {p['real'][0] for p in caps}=={'7/20','-7/20'}
    # Recover every geometry vertex and centroid from typed coordinates.
    checks['all_vertices_recover']=[[str(Q(x)) for x in p['real']]+[str(Q(x)) for z in p['complex'] for x in z] for p in result['coordinates']['vertices']]==result['geometry']['vertices']
    reverse=deepcopy(source);reverse['arrow_families']=[[[b,a] for a,b in family] for family in reverse['arrow_families']]
    back=run(reverse)
    checks['direction_retained']=back['geometry']==result['geometry'] and back['cycle']['centroid_motion_trace']!=result['cycle']['centroid_motion_trace']
    tall=deepcopy(source)
    for v in tall['vertices'].values():v['real']=[str(Q(v['real'][0])*2)]
    changed=run(tall)
    checks['real_scale_changes_metric']=changed['geometry']['squared_distances']!=result['geometry']['squared_distances']
    planar=deepcopy(source)
    for v in planar['vertices'].values():v['real']=[]
    flat=run(planar)
    checks['same_frontend_planar_control_is_hexagon']=len(flat['geometry']['supporting_facets'])==6
    # A pure-real 3D input follows exactly the same frontend and backend.
    tetra={'schema':source['schema'],'imaginary_square':'1','vertices':{k:{'real':v,'complex':[]} for k,v in zip('ABCD',[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])},
           'arrow_families':[[['A','B'],['B','C'],['C','A'],['D','D']]],'seeds':[{'vertex':'A','role':'carrier'},{'vertex':'D','role':'carrier'}]}
    solid=run(tetra)
    checks['same_frontend_pure_real_control_is_tetrahedron']=len(solid['geometry']['vertices'])==4 and len(solid['geometry']['supporting_facets'])==4
    def reject(label,bad,text):
        try:run(bad)
        except ValueError as e:checks[label]=text in str(e)
        else:checks[label]=False
    bad=deepcopy(source);bad['faces']=[];reject('finished_cells_rejected',bad,'fields only')
    bad=deepcopy(source);bad['arrow_families'][0][0][1]='A';reject('nonpermutation_rejected',bad,'permute')
    bad=deepcopy(source);bad['arrow_families'][0][0][1],bad['arrow_families'][0][1][1]=bad['arrow_families'][0][1][1],bad['arrow_families'][0][0][1];reject('inconsistent_arrow_action_rejected',bad,'inconsistent')
    bad=deepcopy(source);bad['arrow_families']=[[['A','A'],['B','C'],['C','B'],['D','D'],['E','F'],['F','E']]];reject('improper_reflection_rejected',bad,'orientation preserving')
    bad=deepcopy(source);bad['vertices']={k:v for k,v in bad['vertices'].items() if k in 'ABC'};bad['arrow_families']=[bad['arrow_families'][0][:3]];bad['seeds']=bad['seeds'][:1];reject('underdetermined_single_rim_rejected',bad,'unique affine')
    bad=deepcopy(source);bad['seeds']=bad['seeds'][:1];reject('missing_orbit_rejected',bad,'do not span')
    bad=deepcopy(source);bad['imaginary_square']='0';reject('degenerate_metric_rejected',bad,'positive')
    paths=[source_path,legacy_path,Path(__file__).resolve(),ROOT/'research/strominger/checkers/assemble_real_complex_arrows.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,'counts':result['cycle']['geometry']['counts'],
            'coordinate_comparison':'Exact permutation (X,Y,Z)->(Y,Z,X); metric and generators conjugated before complete output comparison',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/neutron-real-complex-checks.json';out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
