"""FCC-first labelled transport and equivariant esd7 presentation audit.
Read prior geometry; do not change native particle/window rules.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
SOURCE='research/voevodsky/results/esd7_explicit_analytical_census.json'


def key(vs):return tuple(sorted(vs))
def norm2(v):return sum(x*x for x in v)
def delta(a,b):return tuple(y-x for x,y in zip(a,b))
def fcc(x):return (x[0]+x[1],x[0]+x[2],x[1]+x[2])
def inverse(y):
    a,b,c=y
    return ((a+b-c)/2,(a+c-b)/2,(b+c-a)/2,7-(a+b+c)/2)
def act(x,p):
    out=[0]*4
    for i in range(4):out[p[i]]=x[i]
    return tuple(out)
def step(x,i,j):
    y=list(x);y[i]-=1;y[j]+=1
    return tuple(y)
def face_set(vs):return {key(f) for f in combinations(vs,3) if all(norm2(delta(a,b))==2 for a,b in combinations(f,2))}
def determinant(m):
    return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))*m[0][p[0]]*m[1][p[1]]*m[2][p[2]] for p in permutations(range(3)))


def main():
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    data=json.loads((ROOT/SOURCE).read_text(encoding='utf-8'))
    verts={r['id']:tuple(r['barycentric']) for r in data['vertices']}
    vertex_ids={v:id for id,v in verts.items()};V=set(verts.values())
    fine={r['id']:key(verts[id] for id in r['vertices']) for r in data['tetrahedra']}
    fine_set=set(fine.values())
    edges={r['id']:key(verts[id] for id in r['vertices']) for r in data['edges']}
    root_edges={e for e in edges.values() if norm2(delta(*e))==2}
    diagonals={e for e in edges.values() if norm2(delta(*e))==4}
    check('all source vertices are in the affine A3 lattice',len(V)==120 and all(sum(v)==7 and min(v)>=0 for v in V))
    check('FCC chart is integral even-sum and exactly invertible',all(sum(fcc(v))%2==0 and inverse(tuple(map(F,fcc(v))))==v for v in V))
    check('FCC chart preserves all displacement norms',all(norm2(delta(a,b))==norm2(delta(fcc(a),fcc(b))) for a,b in combinations(V,2)))
    sectors=[(i,j) for i in range(4) for j in range(4) if i!=j]
    moves=[(x,i,j,step(x,i,j)) for x in sorted(V) for i,j in sectors if x[i]>0]
    check('twelve directed sector types give every FCC nearest edge',len(sectors)==12 and {key((x,y)) for x,i,j,y in moves}==root_edges and len(moves)==1008)
    check('source subdivision has 504 root edges and 56 diagonals',len(root_edges)==504 and len(diagonals)==56 and len(edges)==560)
    face_ids={key(verts[id] for id in r['vertices']):r['id'] for r in data['triangles']}
    elementary=[];octa=[];assigned=[]
    for id,t in fine.items():
        ds=[e for e in combinations(t,2) if norm2(delta(*e))==4]
        if not ds:elementary.append({'id':'tet-'+id,'vertices':t,'refinement':[id]})
        else:assert len(ds)==1
    for n,d in enumerate(sorted(diagonals)):
        common=sorted(x for x in V if all(norm2(delta(x,end))==2 for end in d))
        assert len(common)==4
        vs=key((*d,*common))
        pieces=[id for id,t in fine.items() if set(d)<=set(t)]
        assert len(pieces)==4 and set().union(*(set(fine[id]) for id in pieces))==set(vs)
        assert all(norm2(delta(a,b)) in (2,4) for a,b in combinations(vs,2))
        assert len(face_set(vs))==8
        paths=[]
        for mid in common:
            legs=[]
            for a,b in [(d[0],mid),(mid,d[1])]:
                dv=delta(a,b);legs.append([dv.index(-1),dv.index(1)])
            assert step(step(d[0],*legs[0]),*legs[1])==d[1]
            paths.append({'middle':vertex_ids[mid],'sector_word':legs,'comparison_face':face_ids[key((*d,mid))]})
        octa.append({'id':f'oct-{n:03d}','vertices':vs,'selected_diagonal':d,'refinement':pieces,'diagonal_root_paths':paths})
        assigned.extend(pieces)
    assigned.extend(r['refinement'][0] for r in elementary)
    check('coarsening uniquely recovers 119 tetrahedra and 56 octahedra',len(elementary)==119 and len(octa)==56 and len(assigned)==len(set(assigned))==343)
    check('every presentation diagonal has four retained two-root routes',all(len(c['diagonal_root_paths'])==4 for c in octa))
    check('all224 diagonal-to-route comparisons name existing source faces',len({p['comparison_face'] for c in octa for p in c['diagonal_root_paths']})==224)
    coarse=elementary+octa
    coarse_set={r['vertices'] for r in coarse}
    face_incidence=defaultdict(list)
    for c in coarse:
        for face in face_set(c['vertices']):face_incidence[face].append(c['id'])
    check('coarse cellular counts and boundary are consistent',len(coarse)==175 and len(face_incidence)==560 and set(map(len,face_incidence.values()))=={1,2} and sum(len(v)==1 for v in face_incidence.values())==196)
    for cell in coarse:
        boundary=defaultdict(int)
        for id in cell['refinement']:
            t=fine[id];points=list(map(fcc,t))
            columns=[delta(points[0],points[j]) for j in (1,2,3)]
            signed_volume=determinant(tuple(tuple(columns[j][i] for j in range(3)) for i in range(3)))
            assert abs(signed_volume)==2
            orientation=1 if signed_volume>0 else -1
            for i in range(4):boundary[t[:i]+t[i+1:]]+=orientation*((-1)**i)
        nonzero={f:s for f,s in boundary.items() if s}
        assert set(nonzero)==face_set(cell['vertices']) and all(abs(s)==1 for s in nonzero.values())
    checks.append('refinement preserves every coarse boundary and cancels internal diagonal faces')
    # Full S4 acts on sites, sectors and unsubdivided cells. The chosen split is
    # carried along with its frame, not demanded invariant under every action.
    Ps=list(permutations(range(4)));variants={};frames=[]
    for p in Ps:
        assert {act(x,p) for x in V}==V
        assert {key(act(x,p) for x in c) for c in coarse_set}==coarse_set
        assert {key(act(x,p) for x in e) for e in root_edges}==root_edges
        for x,i,j,y in moves:assert act(y,p)==step(act(x,p),p[i],p[j])
        transformed=frozenset(key(act(x,p) for x in t) for t in fine_set)
        if transformed not in variants:variants[transformed]=len(variants)
        origin=fcc(act((0,0,0,7),p))
        columns=[]
        for j in range(3):
            unit=tuple(F(int(i==j)) for i in range(3))
            image=fcc(act(inverse(unit),p));columns.append(tuple(image[i]-origin[i] for i in range(3)))
        matrix=tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
        assert all(sum(matrix[k][i]*matrix[k][j] for k in range(3))==int(i==j) for i,j in product(range(3),repeat=2))
        frames.append({'permutation':p,'fcc_linear':matrix,'fcc_translation':origin,'determinant':determinant(matrix),'subdivision_variant':variants[transformed],'preserves_selected_subdivision':transformed==fine_set})
    checks.append('all24 frames preserve FCC cells and intertwine all1008 labelled moves')
    check('all24 frame maps are affine isometries with12 proper and12 improper',sum(f['determinant']==1 for f in frames)==12 and sum(f['determinant']==-1 for f in frames)==12)
    check('chosen subdivision has eight symmetries and three transported presentations',sum(f['preserves_selected_subdivision'] for f in frames)==8 and len(variants)==3)
    for p,q in product(Ps,repeat=2):
        pq=tuple(p[q[i]] for i in range(4))
        for x in [(7,0,0,0),(0,7,0,0),(0,0,7,0),(0,0,0,7)]:assert act(act(x,q),p)==act(x,pq)
        assert {key(act(act(x,q),p) for x in t) for t in fine_set}=={key(act(x,pq) for x in t) for t in fine_set}
    checks.append('all576 frame compositions carry the complete subdivision consistently')
    # Test geometric route squares with both intermediate states inside the region.
    squares=0
    for x in V:
        for (i,j),(k,l) in product(sectors,repeat=2):
            a=step(x,i,j);b=step(x,k,l);end=step(a,k,l)
            if a in V and b in V and end in V:
                assert end==step(b,i,j);squares+=1
    check('all admitted two-move endpoint squares close',squares>0)
    # A retained route is not identified by endpoint equality.
    witness=octa[0]
    check('diagonal alternatives retain distinct histories at equal endpoints',len({tuple(map(tuple,p['sector_word'])) for p in witness['diagonal_root_paths']})==4)
    bad_frame=next(p for p in Ps if {key(act(x,p) for x in t) for t in fine_set}!=fine_set)
    check('fixed-triangulation control rejects a valid ambient frame',any(key(act(x,bad_frame) for x in t) not in fine_set for t in fine_set))
    check('a presentation diagonal is not an elementary root move',all(sorted(delta(*d))!=[-1,0,0,1] for d in diagonals))
    mids=[verts[p['middle']] for p in witness['diagonal_root_paths']]
    selection_failure=next((p for p in Ps if act(min(mids),p)!=min(act(m,p) for m in mids)),None)
    check('lexicographic shortest-route selection is not S4 equivariant',selection_failure is not None)
    inputs=[SOURCE,'research/strominger/checkers/check_fcc_first_transport.py']
    report={'status':'passed','checks':checks,'check_count':len(checks),'fcc_chart':'(a,b,c,d) -> (a+b,a+c,b+c), a+b+c+d=7',
      'counts':{'vertices':len(V),'root_edges':len(root_edges),'directed_moves':len(moves),'presentation_diagonals':len(diagonals),'coarse_faces':len(face_incidence),'tetrahedra':len(elementary),'octahedra':len(octa),'fine_tetrahedra':len(fine),'admitted_geometric_squares':squares,'frames':24,'subdivision_variants':len(variants)},
      'vertices':[{'id':id,'barycentric':v,'fcc':fcc(v)} for id,v in verts.items()],
      'directed_moves':[{'source':vertex_ids[x],'sector':[i,j],'target':vertex_ids[y]} for x,i,j,y in moves],
      'coarse_cells':coarse,'coarse_faces':[{'vertices':face,'incident_cells':ids} for face,ids in sorted(face_incidence.items())],
      'frame_actions':frames,'negative_controls':{'fixed_subdivision_breaking_frame':bad_frame,'lexicographic_route_breaking_frame':selection_failure},'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
      'scope':'Exact spatial and labelled-incidence adapter. FCC endpoint commutation is not analytical face-homotopy data. All four diagonal routes remain distinct; none is chosen as a field-transfer law. No C3 coefficient action, P/N/E role binding, convolution-depth selector, global28-stage evolution or physical dynamics is inferred. S4 includes improper spatial isometries; chart quarter-cycle is not automatically a proper spatial quarter-turn.'}
    dest=ROOT/'research/strominger/results/fcc-first-transport.json'
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(report,indent=2,default=str)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'counts':report['counts'],'result':str(dest)}))


if __name__=='__main__':main()
