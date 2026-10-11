"""Discovery controls: unique cube, ambiguous squares, missing faces and limits."""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from check_merkle_identity_surface import cube
from merkle_gluing_search import face_packet, search, verify_certificate, digest, read_faces

BASE=Path(__file__).resolve().parents[1]
SEARCH=Path(__file__).with_name('merkle_gluing_search.py')

def detached_cube_faces():
    # Distinct endpoint-potential differences make each oriented map's inverse
    # unique. No endpoint IDs, coordinates or original adjacency enter the input.
    faces=[]
    for cycle in cube()['faces']:
        potential=lambda name:2**int(name,2)
        faces.append([['1',str(potential(v)-potential(u))] for u,v in zip(cycle,cycle[1:]+cycle[:1])])
    return faces

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    maps=detached_cube_faces(); packet=face_packet(maps); result=search(packet)
    checks={'unique_discovery_search_exhausted':result['status']=='unique_labelled_gluing' and result['exhaustive'],
            'one_connected_sphere_found':len(result['solutions'])==1 and result['solutions'][0]['summary']=={'vertices':8,'edges':12,'faces':6,'genus':0,'globally_path_independent':True}}
    solution=result['solutions'][0]
    checks['certificate_reconstructs_and_verifies_surface']=verify_certificate(packet,solution['certificate'],solution['surface'])['coherent_closed_surface']
    checks['source_contains_only_local_corners_and_proofs']=all(set(face)=={'kind','occurrence','types','maps','proof'} for face in read_faces(packet))
    checks['all_24_ports_paired_once']=len(solution['certificate']['record']['pairings'])==12
    rotated=[f[1:]+f[:1] for f in reversed(maps)]
    reordered=search(face_packet(rotated))
    checks['face_order_and_corner_origin_do_not_prevent_discovery']=reordered['status']=='unique_labelled_gluing' and reordered['solutions'][0]['summary']['genus']==0
    missing=search(face_packet(maps[:-1]))
    checks['missing_face_reports_four_unmatched_ports']=missing['status']=='no_gluing_in_supported_grammar' and missing['exhaustive'] and len(missing['unmatched_ports'])==4
    one=search(face_packet([[['1','0']]*4]))
    checks['self_pairing_not_invented']=one['status']=='no_gluing_in_supported_grammar' and len(one['unmatched_ports'])==4
    ambiguous_packet=face_packet([[['1','0']]*4,[['1','0']]*4])
    ambiguous=search(ambiguous_packet)
    checks['multiple_labelled_gluings_reported']=ambiguous['status']=='ambiguous' and len(ambiguous['solutions'])==2 and not ambiguous['exhaustive']
    checks['ambiguous_solutions_have_distinct_pairings']=ambiguous['solutions'][0]['certificate']['record']['pairings']!=ambiguous['solutions'][1]['certificate']['record']['pairings']
    checks['each_ambiguous_solution_is_independently_valid']=all(verify_certificate(ambiguous_packet,s['certificate'],s['surface'])['genus']==0 for s in ambiguous['solutions'])
    bounded=search(packet,max_nodes=1)
    checks['budget_exhaustion_not_reported_as_impossibility']=bounded['status']=='search_limit' and not bounded['exhaustive']
    false=deepcopy(maps); false[0][0][1]=str(Q(false[0][0][1])+1)
    checks['false_local_identity_rejected_before_search']=rejected(lambda:search(face_packet(false)))
    broken=deepcopy(packet); ref=broken['objects'][broken['root']]['faces'][0]; broken['objects'][ref]['types'][0]='Z'
    checks['source_tampering_rejected']=rejected(lambda:search(broken))
    rebound=deepcopy(solution['certificate']); rebound['record']['source']='0'*64; rebound['hash']=digest(rebound['record'])
    checks['honestly_rehashed_wrong_source_rejected']=rejected(lambda:verify_certificate(packet,rebound,solution['surface']))
    repeat=deepcopy(solution['certificate']); repeat['record']['pairings'][-1]=repeat['record']['pairings'][0]; repeat['hash']=digest(repeat['record'])
    checks['reused_boundary_port_rejected']=rejected(lambda:verify_certificate(packet,repeat,solution['surface']))
    incompatible=deepcopy(solution['certificate']); p=incompatible['record']['pairings']; p[0][1],p[1][1]=p[1][1],p[0][1]; incompatible['hash']=digest(incompatible['record'])
    checks['incompatible_edge_attachment_rejected']=rejected(lambda:verify_certificate(packet,incompatible,solution['surface']))
    checks['serialized_certificate_replays']=verify_certificate(json.loads(json.dumps(packet)),json.loads(json.dumps(solution['certificate'])),json.loads(json.dumps(solution['surface'])))['genus']==0
    out=BASE/'results'; out.mkdir(exist_ok=True)
    source=out/'merkle_unglued_cube_faces.json'; source.write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    discovered=out/'merkle_discovered_cube.json'
    cli=subprocess.run([sys.executable,str(SEARCH),str(source),'--output',str(discovered)],capture_output=True,text=True)
    checks['external_input_cli_discovers_surface']=cli.returncode==0 and json.loads(cli.stdout)['status']=='unique_labelled_gluing'
    external=json.loads(discovered.read_text(encoding='utf-8'))['solutions'][0]
    checks['external_cli_certificate_reverifies']=verify_certificate(packet,external['certificate'],external['surface'])['coherent_closed_surface']
    receipt={'schema':'marici.merkle-gluing-search-check.v1','passed':all(checks.values()),'checks':checks,
             'source_root':packet['root'],'discovered_surface_root':solution['surface']['root'],
             'unique_search_nodes':result['visited_nodes'],'ambiguous_search_nodes':ambiguous['visited_nodes'],
             'search_sha256':sha256(SEARCH.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'scope':'Bounded labelled-port matching with exact inverse affine labels. Simple-edge connected regular polygon surfaces only; no uniqueness claim modulo isomorphism or beyond search budget.'}
    (out/'merkle_gluing_search.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    (out/'merkle_ambiguous_gluing.json').write_text(json.dumps({'source':ambiguous_packet,'search':ambiguous},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if not receipt['passed']: raise SystemExit(1)

if __name__=='__main__': main()
