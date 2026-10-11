"""Positive and hostile tests of the explicit thin-affine cone filler."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from check_merkle_identity_surface import cube, encode, IDENTITY
from check_merkle_torus_holonomy import torus
from merkle_cone_filler import construct, verify, digest
from merkle_gluing_search import face_packet, search, verify_certificate
from check_merkle_gluing_search import detached_cube_faces

BASE=Path(__file__).resolve().parents[1]
MODULE=Path(__file__).with_name('merkle_cone_filler.py')

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError,ZeroDivisionError): return True
    return False

def change(artifact,field,index,mutate):
    out=deepcopy(artifact); root=out['objects'][out['root']]; ref=root[field][index]
    obj=deepcopy(out['objects'][ref]); mutate(obj); new=digest(obj); out['objects'][new]=obj
    root[field][index]=new; out['root']=digest(root); out['objects'][out['root']]=root
    return out

def main():
    surface=encode(cube()); artifact=construct(surface); report=verify(artifact)
    checks={'explicit_cube_cone_verified':report['verified'],
            'twelve_tetrahedra_fill_triangulated_cube':report['tetrahedra']==12 and report['boundary_triangles']==12,
            'eighteen_interior_faces_cancel':report['interior_triangles']==18 and report['interior_faces_cancel'],
            'cone_counts_and_ball_euler_characteristic':(report['vertices'],report['edges'],report['triangles'],report['euler_characteristic'])==(9,26,30,1),
            'exact_original_boundary_root_retained':report['boundary_root']==surface['root'],
            'all_boundary_and_interior_triangle_transports_flat':report['all_triangle_transports_flat'],
            'unfilled_surface_is_not_a_filler':rejected(lambda:verify(surface))}
    missing=deepcopy(artifact); rec=missing['objects'][missing['root']]; rec['tetrahedra'].pop(); missing['root']=digest(rec); missing['objects'][missing['root']]=rec
    checks['honestly_rehashed_missing_tetrahedron_rejected']=rejected(lambda:verify(missing))
    # Reversing four vertices is even; swap two to reverse orientation.
    reversed_tet=change(artifact,'tetrahedra',0,lambda t:t['vertices'].__setitem__(slice(0,2),list(reversed(t['vertices'][:2]))))
    checks['wrong_tetrahedron_orientation_rejected']=rejected(lambda:verify(reversed_tet))
    bad_edge=change(artifact,'edges',0,lambda e:e.__setitem__('map',['1','999']))
    checks['honestly_rehashed_false_transport_rejected']=rejected(lambda:verify(bad_edge))
    missing_edge=deepcopy(artifact); rec=missing_edge['objects'][missing_edge['root']]; rec['edges'].pop(); missing_edge['root']=digest(rec); missing_edge['objects'][missing_edge['root']]=rec
    checks['missing_interior_or_boundary_edge_rejected']=rejected(lambda:verify(missing_edge))
    bad_type=change(artifact,'edges',0,lambda e:e.__setitem__('type','ArbitraryFunction'))
    checks['wrong_transport_type_rejected']=rejected(lambda:verify(bad_type))
    altered=deepcopy(artifact); rec=altered['objects'][altered['root']]; rec['boundary']='0'*64; altered['root']=digest(rec); altered['objects'][altered['root']]=rec
    checks['wrong_boundary_binding_rejected']=rejected(lambda:verify(altered))
    tampered=deepcopy(artifact); tampered['objects'][tampered['root']]['model']='automatic-higher-proof'
    checks['unrehashed_tampering_rejected']=rejected(lambda:verify(tampered))
    altered=deepcopy(artifact); rec=altered['objects'][altered['root']]; rec['triangulation'][0]['triangles'].pop(); altered['root']=digest(rec); altered['objects'][altered['root']]=rec
    checks['boundary_face_restriction_loss_rejected']=rejected(lambda:verify(altered))
    checks['flat_torus_not_filled_by_a_cone_ball']=rejected(lambda:construct(encode(torus(IDENTITY,IDENTITY))))
    checks['nontrivial_holonomy_torus_rejected']=rejected(lambda:construct(encode(torus())))
    opened=cube(); opened['faces'].pop()
    checks['open_surface_rejected']=rejected(lambda:construct(encode(opened)))
    flipped=cube(); flipped['faces'][0].reverse()
    checks['inconsistent_supplied_orientation_requires_transport']=rejected(lambda:construct(encode(flipped)))
    checks['serialized_filler_reverifies']=verify(json.loads(json.dumps(artifact)))==report
    packet=face_packet(detached_cube_faces()); found=search(packet)['solutions'][0]
    verify_certificate(packet,found['certificate'],found['surface'])
    discovered=construct(found['surface'])
    checks['discovered_gluing_also_has_verified_explicit_filler']=verify(discovered)['tetrahedra']==12
    out=BASE/'results'; out.mkdir(exist_ok=True)
    (out/'merkle_discovered_cone_filler.json').write_text(json.dumps(discovered,indent=2)+'\n',encoding='utf-8')
    path=out/'merkle_cube_cone_filler.json'; path.write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    cli=subprocess.run([sys.executable,str(MODULE),str(path)],capture_output=True,text=True)
    checks['fresh_external_filler_verification']=cli.returncode==0 and json.loads(cli.stdout)['verified']
    result={'schema':'marici.merkle-cone-filler-check.v1','passed':all(checks.values()),'checks':checks,'filler':report,
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'module_sha256':sha256(MODULE.read_bytes()).hexdigest()}
    (out/'merkle_cone_filler.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
