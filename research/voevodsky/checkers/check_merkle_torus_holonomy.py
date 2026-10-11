"""A flat Merkle torus need not have globally path-independent transport.
Uses the shared surface verifier, exact rational maps and a 3x3 periodic mesh.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from check_merkle_identity_surface import compose, inverse, IDENTITY, encode, verify, cube, digest

BASE = Path(__file__).resolve().parents[1]
VERIFIER = Path(__file__).with_name('check_merkle_identity_surface.py')

def torus(horizontal=(Q(1), Q(1)), vertical=(Q(1), Q(2)), n=3):
    if n < 3: raise ValueError('Regular mesh needs at least three vertices per direction')
    name = lambda i, j: f'{i%n},{j%n}'
    vertices = {name(i,j): {'type': 'Q'} for i in range(n) for j in range(n)}
    edges, faces = {}, []
    for i in range(n):
        for j in range(n):
            u = name(i,j)
            for v, affine in ((name(i+1,j), horizontal), (name(i,j+1), vertical)):
                a,b = sorted((u,v))
                actual = affine if u == a else inverse(affine)
                edges[a+'>'+b] = {'source':a, 'target':b, 'map':list(map(str,actual))}
            faces.append([u,name(i+1,j),name(i+1,j+1),name(i,j+1)])
    return {'vertices':vertices,'edges':edges,'faces':faces}

def walk(model, names):
    result = IDENTITY
    for u,v in zip(names,names[1:]):
        a,b = sorted((u,v)); affine = tuple(map(Q,model['edges'][a+'>'+b]['map']))
        result = compose(affine if u==a else inverse(affine),result)
    return list(map(str,result))

def replay_cycle(artifact, cycle):
    # Independent replay of the explicit witness; do not trust the report's map.
    root = artifact['objects'][artifact['root']]
    current, value = cycle['base'], IDENTITY
    if current not in root['vertices']: raise ValueError('undeclared loop base')
    for step in cycle['path']:
        ref = step['edge']
        if ref not in root['edges']: raise ValueError('edge outside supplied surface')
        edge = artifact['objects'][ref]
        if digest(edge) != ref: raise ValueError('edge integrity failure')
        u,v = edge['source'],edge['target']; affine = tuple(map(Q,edge['map']))
        if step['direction']==-1: u,v=v,u; affine=inverse(affine)
        elif step['direction']!=1: raise ValueError('bad sign')
        if u!=current: raise ValueError('discontinuous cycle')
        current=v; value=compose(affine,value)
    if current!=cycle['base']: raise ValueError('open cycle')
    return list(map(str,value))

def main():
    model=torus(); artifact=encode(model); report=verify(artifact)
    horizontal=['0,0','1,0','2,0','0,0']
    vertical=['0,0','0,1','0,2','0,0']
    named_loops={'horizontal':walk(model,horizontal), 'vertical':walk(model,vertical),
                 'horizontal_reversed':walk(model,list(reversed(horizontal)))}
    checks={
        'regular_torus_9_vertices_18_edges_9_faces':(report['vertices'],report['edges'],report['faces'])==(9,18,9),
        'closed_connected_orientable_genus_one':report['closed_surface'] and report['connected'] and report['orientable'] and report['genus']==1 and report['euler_characteristic']==0,
        'every_face_identity_holds':report['coherent_closed_surface'],
        'global_path_independence_fails':report['globally_path_independent'] is False,
        'horizontal_holonomy_x_plus_3':named_loops['horizontal']==['1','3'],
        'vertical_holonomy_x_plus_6':named_loops['vertical']==['1','6'],
        'reversed_holonomy_x_minus_3':named_loops['horizontal_reversed']==['1','-3'],
        'graph_cycle_rank_E_minus_V_plus_1':report['global_transport']['cycle_rank']==10,
        'all_reported_cycles_replay':all(replay_cycle(artifact,c)==c['map'] for c in report['global_transport']['basis_cycles']),
    }
    # Holonomy around the commutator is trivial, though the two generators are not.
    h,v=tuple(map(Q,named_loops['horizontal'])),tuple(map(Q,named_loops['vertical']))
    checks['torus_commutator_relation_holds']=compose(inverse(v),compose(inverse(h),compose(v,h)))==IDENTITY
    trivial=verify(encode(torus(IDENTITY,IDENTITY)))
    checks['trivial_torus_passes_global_check']=trivial['coherent_closed_surface'] and trivial['globally_path_independent']
    cube_report=verify(encode(cube()))
    checks['cube_passes_all_cycles_not_only_six_routes']=cube_report['coherent_closed_surface'] and cube_report['globally_path_independent'] and cube_report['global_transport']['cycle_rank']==5
    curved=verify(encode(torus((Q(2),Q(0)),(Q(1),Q(1)))))
    checks['noncommuting_labels_fail_local_and_global_checks']=curved['closed_surface'] and not curved['all_face_identities_hold'] and not curved['globally_path_independent']
    # Nonconstant frame changes conjugate transports; they cannot erase obstruction.
    gauged=deepcopy(model)
    frames={name:(Q(2**((i+j)%3)),Q(i-2*j)) for name in model['vertices'] for i,j in [map(int,name.split(','))]}
    for edge in gauged['edges'].values():
        edge['map']=list(map(str,compose(frames[edge['target']],compose(tuple(map(Q,edge['map'])),inverse(frames[edge['source']])))))
    gauge_report=verify(encode(gauged))
    checks['vertex_frame_changes_preserve_flat_nontrivial_holonomy']=gauge_report['coherent_closed_surface'] and not gauge_report['globally_path_independent']
    gauge_trivial=torus(IDENTITY,IDENTITY)
    for edge in gauge_trivial['edges'].values():
        edge['map']=list(map(str,compose(frames[edge['target']],inverse(frames[edge['source']]))))
    checks['nonidentity_edges_can_still_be_globally_path_independent']=verify(encode(gauge_trivial))['globally_path_independent'] and any(e['map']!=['1','0'] for e in gauge_trivial['edges'].values())
    bigger=verify(encode(torus(n=4)))
    checks['four_by_four_torus_repeats_distinction']=bigger['genus']==1 and bigger['coherent_closed_surface'] and not bigger['globally_path_independent']
    checks['serialized_store_reverifies']=verify(json.loads(json.dumps(artifact)))==report
    out=BASE/'results'; out.mkdir(exist_ok=True)
    store_path=out/'merkle_torus_store.json'
    store_path.write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    # CLI acceptance policies must not conflate local validity and trivial holonomy.
    local=subprocess.run([sys.executable,str(VERIFIER),'--verify',str(store_path)],capture_output=True,text=True)
    global_check=subprocess.run([sys.executable,str(VERIFIER),'--verify',str(store_path),'--require-path-independence'],capture_output=True,text=True)
    checks['cli_accepts_locally_coherent_torus']=local.returncode==0
    checks['cli_global_requirement_rejects_nontrivial_holonomy']=global_check.returncode==1 and json.loads(global_check.stdout)['globally_path_independent'] is False
    result={'schema':'marici.merkle-torus-holonomy.v1','passed':all(checks.values()),'checks':checks,
            'surface_root':artifact['root'],'torus':report,'named_loops':named_loops,
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'verifier_sha256':sha256(VERIFIER.read_bytes()).hexdigest(),
            'scope':'Exact affine rational transport on supplied finite polygon complexes. The spanning-forest criterion tests all graph walks; it does not discover gluing, prove arbitrary symbolic identities, or construct higher fillers.'}
    (out/'merkle_torus_holonomy.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='torus'},indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
