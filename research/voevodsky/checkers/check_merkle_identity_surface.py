"""Merkle-addressed polygon surfaces with exact invertible affine Q-map identities.
Run without arguments to generate fixtures/tests; --verify FILE verifies a store.
Topology is a finite regular polygon complex, not arbitrary CW attaching maps.
"""
from collections import defaultdict, Counter
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product, permutations
from pathlib import Path
import argparse
import json

BASE = Path(__file__).resolve().parents[1]

def digest(rec):
    return sha256(b'marici.identity-surface.v1\0' + json.dumps(rec, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()

def compose(g, f): return (g[0]*f[0], g[0]*f[1]+g[1])
def inverse(f): return (1/f[0], -f[1]/f[0])
IDENTITY = (Q(1), Q(0))

def cube(prefix=''):
    vertices = {prefix+''.join(map(str, bits)): {'type': 'Q', 'chart': [str(2**sum(bits)), str(sum((i+1)*b for i,b in enumerate(bits)))]}
                for bits in product((0, 1), repeat=3)}
    faces = []
    for axis in range(3):
        others = [i for i in range(3) if i != axis]
        for side in (0, 1):
            cycle = []
            for a,b in ((0,0),(1,0),(1,1),(0,1)):
                v = [0]*3; v[axis] = side; v[others[0]] = a; v[others[1]] = b
                cycle.append(prefix+''.join(map(str,v)))
            # Cross product of the two increasing free axes has sign (-1)^axis.
            if (-1)**axis != (1 if side else -1): cycle.reverse()
            faces.append(cycle)
    edges = {}
    for face in faces:
        for u,v in zip(face, face[1:]+face[:1]):
            a,b = sorted((u,v)); key = a+'>'+b
            ga,gb = (tuple(map(Q,vertices[w]['chart'])) for w in (a,b))
            edges[key] = {'source': a, 'target': b, 'map': list(map(str,compose(gb,inverse(ga))))}
    return {'vertices': vertices, 'edges': edges, 'faces': faces}

def encode(model):
    store = {}
    def put(rec):
        key = digest(rec); store[key] = rec; return key
    vertices = {name: put({'kind':'vertex','name':name,'type':rec['type']}) for name,rec in model['vertices'].items()}
    edges = {}
    for name,e in model['edges'].items():
        edges[name] = put({'kind':'edge','source':vertices[e['source']], 'target':vertices[e['target']],
                           'type':'AffineQIso','map':e['map']})
    faces = []
    for cycle in model['faces']:
        boundary = []
        for u,v in zip(cycle,cycle[1:]+cycle[:1]):
            a,b = sorted((u,v))
            boundary.append({'edge':edges[a+'>'+b], 'direction':1 if u==a else -1})
        witness = put({'kind':'identity-witness','boundary':boundary,'rule':'exact-affine-holonomy-is-identity'})
        faces.append(put({'kind':'face','boundary':boundary,'witness':witness}))
    root = put({'kind':'surface','vertices':sorted(vertices.values()),'edges':sorted(edges.values()),'faces':faces})
    return {'schema':'marici.identity-surface-store.v1','root':root,'objects':store}

def connected(nodes, adjacency):
    if not nodes: return False
    reached=set(); todo=[next(iter(nodes))]
    while todo:
        v=todo.pop()
        if v not in reached: reached.add(v); todo.extend(adjacency[v]-reached)
    return reached == set(nodes)

def global_transport(vertices, edges):
    """A spanning-forest cycle basis tests ALL graph walks, not sampled routes.

    P[v] is the tree transport from a component base to v. Every edge u->v
    must equal P[v] P[u]^-1 for path independence. Its discrepancy is the
    based loop P[v]^-1 E P[u], retained with an explicit signed edge path.
    """
    adjacency = defaultdict(list)
    for ref, edge in sorted(edges.items()):
        u, v = edge['source'], edge['target']
        affine = tuple(map(Q, edge['map']))
        adjacency[u].append((v, ref, 1, affine))
        adjacency[v].append((u, ref, -1, inverse(affine)))
    potential, paths, bases, tree = {}, {}, {}, set()
    components = 0
    for base in sorted(vertices):
        if base in potential: continue
        components += 1
        potential[base], paths[base], bases[base] = IDENTITY, [], base
        todo = [base]
        while todo:
            u = todo.pop()
            for v, ref, direction, affine in adjacency[u]:
                if v in potential: continue
                potential[v] = compose(affine, potential[u])
                paths[v] = paths[u] + [{'edge': ref, 'direction': direction}]
                bases[v] = base
                tree.add(ref)
                todo.append(v)
    cycles = []
    for ref, edge in sorted(edges.items()):
        if ref in tree: continue
        u, v = edge['source'], edge['target']
        hol = compose(inverse(potential[v]), compose(tuple(map(Q, edge['map'])), potential[u]))
        path = paths[u] + [{'edge': ref, 'direction': 1}] + [
            {'edge': step['edge'], 'direction': -step['direction']} for step in reversed(paths[v])]
        cycles.append({'base': bases[u], 'path': path, 'map': list(map(str, hol)), 'identity': hol == IDENTITY})
    return {'components': components, 'cycle_rank': len(cycles),
            'all_graph_cycles_trivial': all(c['identity'] for c in cycles),
            'nontrivial_basis_cycles': sum(not c['identity'] for c in cycles), 'basis_cycles': cycles}

def verify(artifact):
    store=artifact['objects']
    def get(key,kind,fields):
        if key not in store or digest(store[key]) != key: raise ValueError('missing object or hash mismatch')
        rec=store[key]
        if rec.get('kind') != kind or set(rec) != set(fields.split())|{'kind'}: raise ValueError('record schema')
        return rec
    root=get(artifact['root'],'surface','vertices edges faces')
    vs,es,fs=(root[k] for k in ('vertices','edges','faces'))
    if len(set(vs))!=len(vs) or len(set(es))!=len(es): raise ValueError('duplicate vertex/edge declaration')
    vertices={v:get(v,'vertex','name type') for v in vs}
    edges={e:get(e,'edge','source target type map') for e in es}
    adjacency=defaultdict(set); incident=defaultdict(list); links=defaultdict(list)
    typed=all(v['type']=='Q' for v in vertices.values())
    for e in edges.values():
        u,v=e['source'],e['target']
        if u not in vertices or v not in vertices or u==v: raise ValueError('invalid endpoints')
        if len(e['map'])!=2: raise ValueError('affine arity')
        coeff=tuple(map(Q,e['map']))
        if not coeff[0] or list(map(str,coeff))!=e['map']: raise ValueError('noncanonical or noninvertible map')
        typed &= e['type']=='AffineQIso'
        adjacency[u].add(v); adjacency[v].add(u)
    face_equalities=[]; witness_checks=[]
    for i,key in enumerate(fs):
        f=get(key,'face','boundary witness'); boundary=f['boundary']; starts=[]; ends=[]; refs=[]; hol=IDENTITY
        if len(boundary)<3: raise ValueError('degenerate polygon')
        for step in boundary:
            if set(step)!={'edge','direction'} or type(step['direction']) is not int or step['direction'] not in (-1,1): raise ValueError('boundary step')
            ref,d=step['edge'],step['direction']
            if ref not in edges: raise ValueError('undeclared boundary edge')
            e=edges[ref]; u,v=e['source'],e['target']; affine=tuple(map(Q,e['map']))
            if d==-1: u,v=v,u; affine=inverse(affine)
            starts.append(u); ends.append(v); refs.append(ref)
            incident[ref].append((i,d)); hol=compose(affine,hol)
        if ends!=starts[1:]+starts[:1] or len(set(starts))!=len(starts): raise ValueError('non-simple or open attaching polygon')
        for j,v in enumerate(starts): links[v].append((refs[j-1],refs[j]))
        face_equalities.append(hol==IDENTITY)
        w=get(f['witness'],'identity-witness','boundary rule')
        witness_checks.append(w=={'kind':'identity-witness','boundary':boundary,'rule':'exact-affine-holonomy-is-identity'})
    link_ok={}
    for v in vs:
        degrees=Counter(); graph=defaultdict(set)
        expected={e for e,rec in edges.items() if v in (rec['source'],rec['target'])}
        for a,b in links[v]:
            degrees[a]+=1; degrees[b]+=1; graph[a].add(b); graph[b].add(a)
        link_ok[v]=(set(degrees)==expected and bool(expected) and all(n==2 for n in degrees.values()) and connected(expected,graph))
    two_faces=all(len(incident[e])==2 and incident[e][0][0]!=incident[e][1][0] for e in es)
    is_connected=connected(set(vs),adjacency)
    closed=bool(fs) and two_faces and all(link_ok.values())
    # Solve face orientation constraints; distinguish orientability from supplied orientation.
    orientation={}; orientable=True; dual=defaultdict(list)
    if two_faces:
        for rows in incident.values():
            (f,a),(g,b)=rows; dual[f].append((g,-a*b)); dual[g].append((f,-a*b))
        for f in range(len(fs)):
            if f in orientation: continue
            orientation[f]=1; todo=[f]
            while todo:
                a=todo.pop()
                for b,sign in dual[a]:
                    want=orientation[a]*sign
                    if b in orientation: orientable &= orientation[b]==want
                    else: orientation[b]=want; todo.append(b)
    else: orientable=False
    chi=len(vs)-len(es)+len(fs)
    transport = global_transport(vertices, edges) if typed else None
    return {'vertices':len(vs),'edges':len(es),'faces':len(fs),'euler_characteristic':chi,
            'connected':is_connected,'every_edge_has_two_faces':two_faces,
            'vertex_links_are_circles':all(link_ok.values()),'closed_surface':closed,
            'orientable':orientable if closed else None,
            'supplied_orientation_consistent':two_faces and all(a[1]+b[1]==0 for a,b in incident.values()),
            'genus':(2-chi)//2 if closed and is_connected and orientable else None,
            'boundary_edges':sum(len(incident[e])==1 for e in es),
            'nonmanifold_edges':sum(len(incident[e])>2 for e in es),
            'bad_vertex_links':sum(not ok for ok in link_ok.values()),
            'typed':typed,'all_face_identities_hold':all(face_equalities),
            'failed_face_identities':sum(not x for x in face_equalities),
            'witness_attachments_valid':all(witness_checks),
            'coherent_closed_surface':closed and typed and all(face_equalities) and all(witness_checks),
            'globally_path_independent': transport['all_graph_cycles_trivial'] if transport else None,
            'global_transport': transport,
            'three_dimensional_filler':'not supplied or inferred'}

def rejected(action):
    try: action()
    except (ValueError,KeyError): return True
    return False

def run():
    model=cube(); artifact=encode(model); report=verify(artifact)
    checks={'cube_is_coherent_closed_sphere':report['coherent_closed_surface'] and report['connected'] and report['genus']==0 and report['euler_characteristic']==2,
            'cube_has_8_vertices_12_edges_6_faces':(report['vertices'],report['edges'],report['faces'])==(8,12,6),
            'supplied_cube_orientation_consistent':report['supplied_orientation_consistent']}
    controls={}
    missing=deepcopy(model); missing['faces'].pop(); controls['missing_face']=verify(encode(missing))
    checks['missing_face_exposes_four_boundary_edges']=not controls['missing_face']['closed_surface'] and controls['missing_face']['boundary_edges']==4
    duplicate=deepcopy(model); duplicate['faces'].append(duplicate['faces'][0]); controls['duplicate_face']=verify(encode(duplicate))
    checks['extra_face_creates_four_nonmanifold_edges']=controls['duplicate_face']['nonmanifold_edges']==4 and not controls['duplicate_face']['closed_surface']
    pinch=deepcopy(model); other=cube('b'); rename=lambda v:'000' if v=='b000' else v
    for v,rec in other['vertices'].items(): pinch['vertices'][rename(v)]=rec
    for e in other['edges'].values():
        u,v=rename(e['source']),rename(e['target']); pinch['edges'][u+'>'+v]={**e,'source':u,'target':v}
    pinch['faces'] += [[rename(v) for v in face] for face in other['faces']]
    controls['pinched_two_spheres']=verify(encode(pinch))
    checks['edge_pairing_alone_misses_pinched_vertex']=controls['pinched_two_spheres']['every_edge_has_two_faces'] and controls['pinched_two_spheres']['bad_vertex_links']==1 and not controls['pinched_two_spheres']['closed_surface']
    wrong=deepcopy(model); edge=next(iter(wrong['edges'].values())); edge['map'][1]=str(Q(edge['map'][1])+1)
    controls['wrong_identity']=verify(encode(wrong))
    checks['honestly_rehashed_false_identity_keeps_topology_but_fails_coherence']=controls['wrong_identity']['closed_surface'] and controls['wrong_identity']['failed_face_identities']==2 and not controls['wrong_identity']['coherent_closed_surface']
    flipped=deepcopy(model); flipped['faces'][0].reverse(); controls['flipped_orientation']=verify(encode(flipped))
    checks['orientation_choice_not_confused_with_orientability']=controls['flipped_orientation']['orientable'] and not controls['flipped_orientation']['supplied_orientation_consistent'] and controls['flipped_orientation']['closed_surface']
    bad_type=deepcopy(model); bad_type['vertices']['000']['type']='Z'; controls['wrong_port_type']=verify(encode(bad_type))
    checks['port_type_substitution_fails_coherence']=not controls['wrong_port_type']['typed'] and not controls['wrong_port_type']['coherent_closed_surface']
    tamper=deepcopy(artifact); key=next(k for k,r in tamper['objects'].items() if r['kind']=='edge'); tamper['objects'][key]['map'][1]='999'
    checks['unrehashed_tampering_rejected']=rejected(lambda:verify(tamper))
    erase=deepcopy(artifact); key=next(k for k,r in erase['objects'].items() if r['kind']=='identity-witness'); del erase['objects'][key]
    checks['missing_witness_object_rejected']=rejected(lambda:verify(erase))
    routes=[]
    for order in permutations(range(3)):
        bits=[0,0,0]; total=IDENTITY
        for axis in order:
            u=''.join(map(str,bits)); bits[axis]=1; v=''.join(map(str,bits))
            total=compose(tuple(map(Q,model['edges'][u+'>'+v]['map'])),total)
        routes.append(list(map(str,total)))
    checks['all_six_monotone_corner_routes_agree']=all(r==['8','6'] for r in routes)
    checks['serialized_store_reverifies']=verify(json.loads(json.dumps(artifact)))==report
    checks['no_filler_claimed']=report['three_dimensional_filler']=='not supplied or inferred'
    out=BASE/'results'; out.mkdir(exist_ok=True)
    (out/'merkle_identity_surface_store.json').write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    result={'schema':'marici.merkle-identity-surface-check.v1','passed':all(checks.values()),'checks':checks,
            'cube':report,'controls':controls,'corner_route_maps':routes,'root':artifact['root'],
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Regular finite polygon complexes; exact affine rational isomorphisms. Identity witnesses are rechecked, not trusted. No arbitrary symbolic theorem prover or higher filler.'}
    (out/'merkle_identity_surface.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--verify',type=Path)
    parser.add_argument('--require-path-independence', action='store_true', help='With --verify, also reject nontrivial global loop transport')
    args=parser.parse_args()
    if args.require_path_independence and not args.verify: parser.error('--require-path-independence requires --verify')
    if args.verify:
        report=verify(json.loads(args.verify.read_text(encoding='utf-8'))); print(json.dumps(report,indent=2))
        if not report['coherent_closed_surface'] or (args.require_path_independence and not report['globally_path_independent']): raise SystemExit(1)
    else: run()
