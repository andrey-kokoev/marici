"""Explicit cone-to-ball filler for a coherent oriented sphere boundary.
Semantic model: exact affine Q-isomorphisms with thin equality witnesses.
Not a filler for arbitrary proof-relevant higher cells.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import argparse
import json

from check_merkle_identity_surface import verify as verify_surface, compose, inverse, IDENTITY

DOMAIN=b'marici.affine-cone-filler.v1\0'
def digest(rec): return sha256(DOMAIN+json.dumps(rec,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def boundary_data(surface):
    report=verify_surface(surface)
    if not (report['coherent_closed_surface'] and report['connected'] and report['orientable'] and report['genus']==0 and report['supplied_orientation_consistent'] and report['globally_path_independent']):
        raise ValueError('requires consistently oriented coherent sphere with trivial transport')
    root=surface['objects'][surface['root']]; edges={r:surface['objects'][r] for r in root['edges']}
    triangulation=[]
    for ref in root['faces']:
        face=surface['objects'][ref]; vertices=[]
        for step in face['boundary']:
            edge=edges[step['edge']]; vertices.append(edge['source'] if step['direction']==1 else edge['target'])
        triangles=[[vertices[0],vertices[i],vertices[i+1]] for i in range(1,len(vertices)-1)]
        triangulation.append({'face':ref,'triangles':triangles})
    flat=[t for row in triangulation for t in row['triangles']]
    if len({tuple(sorted(t)) for t in flat})!=len(flat): raise ValueError('fan triangulation not simplicial')
    # Canonical spanning-tree potentials from one boundary vertex.
    adjacency=defaultdict(list)
    for edge in edges.values():
        u,v=edge['source'],edge['target']; m=tuple(map(Q,edge['map']))
        adjacency[u].append((v,m)); adjacency[v].append((u,inverse(m)))
    base=min(root['vertices']); potentials={base:IDENTITY}; todo=[base]
    while todo:
        u=todo.pop()
        for v,m in sorted(adjacency[u]):
            if v not in potentials: potentials[v]=compose(m,potentials[u]); todo.append(v)
    return root,edges,triangulation,potentials

def signed(simplex):
    if len(set(simplex))!=len(simplex): raise ValueError('degenerate simplex')
    inversions=sum(simplex[i]>simplex[j] for i in range(len(simplex)) for j in range(i+1,len(simplex)))
    return tuple(sorted(simplex)),(-1)**inversions

def chain_boundary(tetrahedra):
    result=Counter(); incidence=defaultdict(list)
    for tet in tetrahedra:
        for i in range(4):
            key,sign=signed(tet[:i]+tet[i+1:]); sign*=(-1)**i
            result[key]+=sign; incidence[key].append(sign)
    return {k:v for k,v in result.items() if v},incidence

def construct(surface):
    root,edges,triangulation,potentials=boundary_data(surface)
    objects={}
    def put(rec): key=digest(rec); objects[key]=rec; return key
    apex=put({'kind':'interior-apex','type':'Q'})
    potentials[apex]=IDENTITY
    tetrahedra=[[apex]+t for row in triangulation for t in row['triangles']]
    tet_refs=[put({'kind':'oriented-tetrahedron','vertices':t}) for t in tetrahedra]
    pairs=sorted({tuple(sorted(pair)) for tet in tetrahedra for pair in combinations(tet,2)})
    edge_refs=[]
    for u,v in pairs:
        m=compose(potentials[v],inverse(potentials[u]))
        edge_refs.append(put({'kind':'transport-edge','type':'AffineQIso','source':u,'target':v,'map':list(map(str,m))}))
    ref=put({'kind':'cone-ball-filler','model':'thin-affine-Q-cone-v1','boundary':surface['root'],
             'apex':apex,'triangulation':triangulation,'tetrahedra':tet_refs,'edges':edge_refs})
    return {'schema':'marici.cone-filler-store.v1','boundary':surface,'root':ref,'objects':objects}

def verify(artifact):
    if set(artifact)!={'schema','boundary','root','objects'} or artifact['schema']!='marici.cone-filler-store.v1': raise ValueError('filler schema')
    surface=artifact['boundary']; root,old_edges,expected,_=boundary_data(surface)
    store=artifact['objects']
    def get(ref,kind,fields):
        if ref not in store or digest(store[ref])!=ref: raise ValueError('filler hash mismatch')
        rec=store[ref]
        if rec.get('kind')!=kind or set(rec)!={'kind'}|set(fields.split()): raise ValueError('filler record shape')
        return rec
    rec=get(artifact['root'],'cone-ball-filler','model boundary apex triangulation tetrahedra edges')
    if rec['model']!='thin-affine-Q-cone-v1' or rec['boundary']!=surface['root']: raise ValueError('wrong model or boundary binding')
    if get(rec['apex'],'interior-apex','type')['type']!='Q': raise ValueError('apex type')
    apex=rec['apex']
    if apex in root['vertices'] or rec['triangulation']!=expected: raise ValueError('boundary restriction mismatch')
    triangles=[t for row in expected for t in row['triangles']]
    tetrahedra=[get(ref,'oriented-tetrahedron','vertices')['vertices'] for ref in rec['tetrahedra']]
    expected_sets={tuple(sorted([apex]+t)) for t in triangles}
    if len(tetrahedra)!=len(expected_sets) or {tuple(sorted(t)) for t in tetrahedra}!=expected_sets or any(len(t)!=4 for t in tetrahedra): raise ValueError('wrong or missing cone tetrahedra')
    actual_boundary,incidence=chain_boundary(tetrahedra)
    wanted=Counter()
    for t in triangles:
        key,sign=signed(t); wanted[key]+=sign
    if actual_boundary!=dict(wanted): raise ValueError('oriented tetrahedral boundary does not restrict to original faces')
    for face,signs in incidence.items():
        if apex in face and (len(signs)!=2 or sum(signs)!=0): raise ValueError('uncancelled interior face')
        if apex not in face and len(signs)!=1: raise ValueError('boundary face multiplicity')
    pairs={tuple(sorted(p)) for t in tetrahedra for p in combinations(t,2)}
    maps={}
    for ref in rec['edges']:
        e=get(ref,'transport-edge','type source target map'); pair=(e['source'],e['target'])
        if e['type']!='AffineQIso' or pair not in pairs or pair in maps or len(e['map'])!=2: raise ValueError('edge incidence/type')
        m=tuple(map(Q,e['map']))
        if not m[0] or list(map(str,m))!=e['map']: raise ValueError('canonical invertible map required')
        maps[pair]=m
    if set(maps)!=pairs: raise ValueError('missing interior transport')
    def edge(u,v): return maps[u,v] if u<v else inverse(maps[v,u])
    for e in old_edges.values():
        if edge(e['source'],e['target'])!=tuple(map(Q,e['map'])): raise ValueError('boundary edge transport changed')
    for triangle in incidence:
        a,b,c=triangle
        if compose(edge(c,a),compose(edge(b,c),edge(a,b)))!=IDENTITY: raise ValueError('triangle transport is not flat')
    # Every simplex is explicitly a cone on the supplied sphere triangulation.
    # Cone(S^2) is a 3-ball. This theorem and thin equality are the stated model.
    vertices=set(root['vertices'])|{apex}
    chi=len(vertices)-len(pairs)+len(incidence)-len(tetrahedra)
    if chi!=1: raise ValueError('ball Euler characteristic')
    return {'verified':True,'filler_root':artifact['root'],'boundary_root':surface['root'],
            'model':'thin-affine-Q-cone-v1','vertices':len(vertices),'edges':len(pairs),
            'triangles':len(incidence),'tetrahedra':len(tetrahedra),'boundary_triangles':len(wanted),
            'interior_triangles':sum(apex in t for t in incidence),'euler_characteristic':chi,
            'boundary_restriction_verified':True,'interior_faces_cancel':True,'all_triangle_transports_flat':True,
            'scope':'Explicit simplicial cone 3-ball and flat affine transport extension; not equality of arbitrary boundary proof terms.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('input',type=Path)
    parser.add_argument('--construct',type=Path,help='Construct from a surface store and write the filler')
    args=parser.parse_args()
    try:
        if args.input.stat().st_size>10_000_000: raise ValueError('file size limit')
        artifact=json.loads(args.input.read_text(encoding='utf-8'))
        if args.construct:
            artifact=construct(artifact); result=verify(artifact)
            args.construct.write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
        else: result=verify(artifact)
        print(json.dumps(result,indent=2))
    except (ValueError,KeyError,TypeError,ZeroDivisionError) as error:
        print(json.dumps({'verified':False,'error':str(error)})); raise SystemExit(1)
