"""Iteration 2: loss witnesses and exact reconstruction of the actual pullback.
This is a lossless recipe, not a proof of globally minimal description length.
"""
from copy import deepcopy
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

from potential_complex_pullback import digest, depth, factor, project, realization_belt, betti_mod2
from check_potential_complex_pullback import verify_packet, refine_host
from check_proton_face_extension import geometry

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/potential_complex_pullback_store.json'

def canonical(value): return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()

def rebuild(contract):
    """Build from retained factor complexes/maps, not a retained P inventory."""
    c=deepcopy(contract)
    if 'P' in c: raise ValueError('recipe must not smuggle in expanded pullback')
    tz=[v for v,h in c['T_to_I'].items() if h=='0']; cz=[v for v,h in c['C_to_I'].items() if h=='0']
    if len(tz)!=1 or len(cz)!=1: raise ValueError('need unique zero vertices')
    apex='realized-barycenter'; vertices={apex:{'T':tz[0],'C':cz[0],'height':'0'}}
    for a in c['T']['vertices']:
        if a==tz[0]: continue
        for b in c['C']['vertices']:
            if b==cz[0]: continue
            if c['T_to_I'][a]!='1' or c['C_to_I'][b]!='1': raise ValueError('nonbinary vertex interface')
            vertices['T'+a+'_C'+b]={'T':a,'C':b,'height':'1'}
    maximal=[]; provenance=[]
    for tf in c['T']['maximal_simplices']:
        for cf in c['C']['maximal_simplices']:
            if len(tf)!=3 or len(cf)!=4 or tf[-1]!=tz[0] or cf[-1]!=cz[0]: raise ValueError('not the retained cone charts')
            for position in range(3):
                i=j=0; path=['T'+tf[i]+'_C'+cf[j]]
                for step in range(3):
                    if step==position: i+=1
                    else: j+=1
                    path.append('T'+tf[i]+'_C'+cf[j])
                maximal.append([apex]+path)
                provenance.append({'T_flag':tf[:],'C_flag':cf[:],'staircase':position})
    c['P']={'vertices':vertices,'maximal_simplices':maximal,'fold_provenance':provenance}
    return c

def decode(recipe):
    if set(recipe)!={'schema','algorithm','contract_without_P','focus','expected_root'} or recipe['schema']!='marici.pullback-retention.v1' or recipe['algorithm']!='ordered-boundary-product-cone.v1': raise ValueError('recipe schema/algorithm')
    c=rebuild(recipe['contract_without_P']); focus=recipe['focus']; geo=geometry(focus)
    record={'kind':'potential-pullback-realization','contract':c,
            'conforming_host_refinement':refine_host(geo,c['outer_triangle']),
            'realization_belt':realization_belt(c),
            'readout':'retain both projections and every fold flag; do not replace full pullback by its marked zero fiber'}
    packet={'schema':'marici.potential-pullback.v1','root':digest(record),'record':record,'focus':focus}
    if packet['root']!=recipe['expected_root']: raise ValueError('reconstruction root mismatch')
    verify_packet(packet)
    return packet

def encode_point(x,y):
    h=depth(x)
    if h!=depth(y): raise ValueError('incompatible pair')
    if h==0: return {'apex':True}
    return {'host':list(map(str,x)), 'potential_direction':list(map(str,((v-(1-h)/4)/h for v in y)))}

def decode_point(record):
    if record=={'apex':True}: return (Q(1,3),)*3,(Q(1,4),)*4
    if set(record)!={'host','potential_direction'}: raise ValueError('point schema')
    x=tuple(map(Q,record['host'])); v=tuple(map(Q,record['potential_direction']))
    if len(x)!=3 or len(v)!=4 or depth(v)!=1 or depth(x)==0: raise ValueError('direction/depth type')
    h=depth(x)
    return x,tuple((1-h)/4+h*w for w in v)

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    packet=json.loads(SOURCE.read_text(encoding='utf-8')); report=verify_packet(packet); c=packet['record']['contract']
    compressed=deepcopy(c); del compressed['P']
    recipe={'schema':'marici.pullback-retention.v1','algorithm':'ordered-boundary-product-cone.v1',
            'contract_without_P':compressed,'focus':packet['focus'],'expected_root':packet['root']}
    restored=decode(recipe)
    vertices=c['P']['vertices']; th=Counter(v['T'] for v in vertices.values()); ch=Counter(v['C'] for v in vertices.values())
    checks={'source_packet_freshly_reverified':report['verified'],
            'host_projection_has_fourteen_boundary_vertex_preimages':sorted(th.values())==[1]+[14]*6,
            'potential_projection_has_six_boundary_vertex_preimages':sorted(ch.values())==[1]+[6]*14,
            'height_one_has_eighty_four_vertex_preimages':sum(v['height']=='1' for v in vertices.values())==84,
            'both_projections_jointly_separate_all_vertices':len({(v['T'],v['C']) for v in vertices.values()})==85,
            'recipe_contains_no_expanded_pullback':'P' not in recipe['contract_without_P'],
            'decoded_packet_exactly_equals_original':restored==packet,
            'all_fold_provenance_reconstructed':restored['record']['contract']['P']['fold_provenance']==c['P']['fold_provenance']}
    # A concrete equal-host pair whose potential points differ, at positive depth.
    x=(Q(2,3),Q(1,6),Q(1,6)); y1=(Q(5,8),Q(1,8),Q(1,8),Q(1,8)); y2=(Q(1,8),Q(5,8),Q(1,8),Q(1,8))
    p1=factor(x,y1); p2=factor(x,y2)
    checks['host_only_readout_loses_actual_compatible_points']=p1!=p2 and project(c,p1)[0]==project(c,p2)[0] and project(c,p1)[1]!=project(c,p2)[1]
    checks['host_plus_retained_direction_separates_counterexample']=encode_point(x,y1)!=encode_point(x,y2)
    # Retain a point in every full-dimensional cell; no product inventory needed
    # for the point decoder, but the full flag complexes remain in the recipe.
    checks['point_codec_round_trips_all_432_cell_interiors']=all(
        decode_point(encode_point(*project(c,{v:Q(i+1,15) for i,v in enumerate(s)})))==project(c,{v:Q(i+1,15) for i,v in enumerate(s)})
        for s in c['P']['maximal_simplices'])
    checks['apex_codec_does_not_invent_a_direction']=encode_point((Q(1,3),)*3,(Q(1,4),)*4)=={'apex':True}
    checks['apex_codec_round_trip']=decode_point({'apex':True})==((Q(1,3),)*3,(Q(1,4),)*4)
    badpoint={'host':list(map(str,x)),'potential_direction':['1/4']*4}
    checks['interior_point_is_not_accepted_as_boundary_direction']=rejected(lambda:decode_point(badpoint))
    bad=deepcopy(recipe); bad['contract_without_P']['C']['maximal_simplices'].pop()
    checks['dropping_one_inward_fold_breaks_reconstruction']=rejected(lambda:decode(bad))
    bad=deepcopy(recipe); bad['contract_without_P']['C_to_I']['0123']='1'
    checks['forgetting_barycenter_interface_breaks_reconstruction']=rejected(lambda:decode(bad))
    bad=deepcopy(recipe); bad['algorithm']='identity-stage-contraction'
    checks['unspecified_decoder_substitution_rejected']=rejected(lambda:decode(bad))
    # Geometry-only coarsening is not preservation of the flagged realization.
    boundary_c=[s[:-1] for s in c['C']['maximal_simplices']]
    checks['positive_depth_host_fiber_has_sphere_homology']=betti_mod2(boundary_c)==[1,0,1]
    checks['serialized_recipe_reconstructs_same_root']=decode(json.loads(json.dumps(recipe)))['root']==packet['root']
    result={'schema':'marici.pullback-retention-check.v1','passed':all(checks.values()),'checks':checks,
            'root':packet['root'],'recipe_sha256':sha256(canonical(recipe)).hexdigest(),
            'canonical_bytes':{'original_packet_including_focus':len(canonical(packet)),
                               'recipe_including_focus':len(canonical(recipe)),
                               'expanded_contract':len(canonical(c)),
                               'factor_contract_without_P':len(canonical(compressed))},
            'loss_witness':{'same_host':list(map(str,x)),'potential_1':list(map(str,y1)),'potential_2':list(map(str,y2))},
            'fiber_statement':'Over positive-depth host points the fiber is S2; at the center it is one point. A host-only view cannot reconstruct the potential direction.',
            'scope':'Lossless for the fixed flagged PL contract. No global minimality claim, no electron coefficient network or physical identification.',
            'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    out=BASE/'results'
    (out/'pullback_retention_recipe.json').write_text(json.dumps(recipe,indent=2)+'\n',encoding='utf-8')
    (out/'pullback_retention.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
