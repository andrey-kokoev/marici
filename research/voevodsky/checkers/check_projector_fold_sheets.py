"""Iteration 5: exact fibers and seam of the actual projector-induced fold.
Two sheets are derived from the tetrahedron inequalities, not postulated as
conjugate coefficient states. They have equal selected coefficient readouts.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_fold_coefficient_attachment import verify as verify_attachment, mode, direction, dot
from check_proton_merkle_reassembly import POINTS, ZERO
from check_proton_face_extension import det
from potential_complex_pullback import digest, depth, complex_cells, betti_mod2
from check_proton_six_belt import topology

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/fold_coefficient_attachment_store.json'


def parameters(source):
    r=source['record']
    if r['declared_alignment']!=list('ABCD'): raise ValueError('this atlas binds the declared ABCD alignment')
    p=[[tuple(map(Q,z)) for z in row] for row in r['mode_matrix']]
    n=tuple(map(Q,r['normal'])); recovery=[[Q(x) for x in row] for row in r['real_recovery_matrix']]
    if n!=(Q(1),Q(1),Q(-1)): raise ValueError('host normal differs')
    return p,n,recovery


def fiber(z,p,n,recovery):
    """Exact entire fiber on the REAL tetrahedron boundary; reject bad modes."""
    if len(z)!=3 or any(len(a)!=2 for a in z): raise ValueError('mode type')
    w=tuple(dot(row,[a[0] for a in z]) for row in recovery)
    if dot(w,n)!=0 or mode(p,w)!=list(z): raise ValueError('not in the real selected-mode plane')
    lower=-1-min(dot(POINTS[a],w) for a in 'ABC'); upper=Q(1,3)
    if lower>upper: raise ValueError('outside triangular mode image')
    result=[]
    for height in (lower,upper):
        d=tuple(a+height*b for a,b in zip(w,n))
        v=tuple((1+dot(POINTS[a],d))/4 for a in 'ABCD')
        if depth(v)!=1 or mode(p,d)!=list(z): raise ValueError('invalid endpoint reconstruction')
        if v not in result: result.append(v)
    return result


def deck(v,p,n,recovery):
    pair=fiber(mode(p,direction(v)),p,n,recovery)
    if v not in pair: raise ValueError('point not on its endpoint fiber')
    return pair[-1] if v==pair[0] else pair[0]


def encode(v,p,n,recovery):
    z=mode(p,direction(v)); endpoints=fiber(z,p,n,recovery)
    sheet='seam' if len(endpoints)==1 else ('upper' if v==endpoints[1] else 'lower')
    if v not in endpoints: raise ValueError('not a boundary endpoint')
    return {'mode':[list(map(str,a)) for a in z],'sheet':sheet}


def decode(record,p,n,recovery):
    if set(record)!={'mode','sheet'}: raise ValueError('point codec schema')
    endpoints=fiber([tuple(map(Q,a)) for a in record['mode']],p,n,recovery)
    if len(endpoints)==1:
        if record['sheet']!='seam': raise ValueError('seam has one point, not two tagged points')
        return endpoints[0]
    if record['sheet'] not in ('upper','lower'): raise ValueError('interior needs a sheet choice')
    return endpoints[1 if record['sheet']=='upper' else 0]


def contains_flag(point,flag):
    order=[]; seen=set()
    for label in flag:
        new=set(map(int,label))-seen
        if len(new)!=1: raise ValueError('not a maximal boundary flag')
        order.append(next(iter(new))); seen|=new
    missing=next(i for i in range(4) if i not in seen)
    return point[missing]==0 and point[order[0]]>=point[order[1]]>=point[order[2]]>=0


def build(source):
    p,n,recovery=parameters(source)
    original=source['source']['record']['directions']; vertices={}; faces=[]; owners=[]
    def put(v):
        record={'kind':'retained-direction','barycentric':list(map(str,v))}; ref=digest(record); vertices[ref]=record
        return ref
    # The lower disk already has 18 flagged triangles. Reflect its actual
    # coefficient fibers to obtain a matching 18-triangle upper disk.
    for triangle in original['maximal_simplices']:
        if triangle[-1]=='012': continue
        lower=[tuple(map(Q,original['vertices'][v])) for v in triangle]
        for points in (lower,[deck(v,p,n,recovery) for v in lower]):
            if det(*(direction(v) for v in points))<0: points=[points[0],points[2],points[1]]
            refs=[put(v) for v in points]; faces.append(refs)
            matching=[flag for flag in original['maximal_simplices'] if all(contains_flag(v,flag) for v in points)]
            if len(matching)!=1: raise ValueError('refinement crosses or loses an original fold chart')
            owners.append(matching[0]+['0123'])
    swap={ref:put(deck(tuple(map(Q,r['barycentric'])),p,n,recovery)) for ref,r in list(vertices.items())}
    image_vertices={}; projection={}
    for ref,r in vertices.items():
        z=mode(p,direction(tuple(map(Q,r['barycentric']))))
        value={'kind':'selected-mode','value':[list(map(str,a)) for a in z]}; key=digest(value)
        image_vertices[key]=value; projection[ref]=key
    # Unoriented image cells: duplicates from the two hemispheres are identified.
    image_faces=[]
    for triple in sorted({tuple(sorted(projection[v] for v in face)) for face in faces}):
        points=[tuple(Q(a[0]) for a in image_vertices[v]['value']) for v in triple]
        signed=det(n,tuple(b-a for a,b in zip(points[0],points[1])),tuple(b-a for a,b in zip(points[0],points[2])))
        if signed==0: raise ValueError('degenerate image triangle')
        image_faces.append(list(triple) if signed>0 else [triple[0],triple[2],triple[1]])
    return {'kind':'projector-induced-fold-atlas','source_root':source['root'],
            'input_scope':'real boundary directions in the declared ABCD coordinate bridge',
            'fiber_rule':'d=w+alpha*n; alpha_lower=-1-min(A.w,B.w,C.w), alpha_upper=1/3',
            'vertices':vertices,'oriented_faces':faces,'original_fold_owners':owners,'deck_vertex_map':swap,
            'image':{'vertices':image_vertices,'faces':[list(s) for s in image_faces]},'projection':projection,
            'seam_vertices':sorted(v for v in vertices if swap[v]==v),
            'sheet_interpretation':'two points over the image interior, identified on its boundary; not two conjugate coefficient states'}


def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.projector-fold-sheets.v1': raise ValueError('schema')
    verify_attachment(packet['source']); r=packet['record']
    if digest(r)!=packet['root'] or r!=build(packet['source']): raise ValueError('source-bound fold atlas mismatch')
    return {'sphere':topology(r['oriented_faces']), 'image':topology(r['image']['faces']),
            'sphere_betti_mod2':betti_mod2(r['oriented_faces']), 'image_betti_mod2':betti_mod2(r['image']['faces'])}


def grid4(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                d=total-a-b-c
                if min(a,b,c,d)==0: yield tuple(Q(x,total) for x in (a,b,c,d))


def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False


def cyclic(face): return min(tuple(face[i:]+face[:i]) for i in range(3))


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_attachment(source); p,n,recovery=parameters(source)
    record=build(source); packet={'schema':'marici.projector-fold-sheets.v1','source':source,'record':record,'root':digest(record)}
    report=verify(packet); sphere=report['sphere']; image=report['image']; verts=record['vertices']; swap=record['deck_vertex_map']
    checks={'source_and_atlas_freshly_reverified':True,
            'refinement_is_closed_oriented_sphere':sphere['manifold_with_boundary'] and sphere['supplied_orientation_consistent'] and sphere['boundary_loops']==0 and (sphere['vertices'],sphere['edges'],sphere['faces'])==(20,54,36),
            'mode_image_is_a_disk':image['disk'] and (image['vertices'],image['edges'],image['faces'])==(13,30,18),
            'six_edge_boundary_is_actual_identification_seam':image['boundary_lengths']==[6] and len(record['seam_vertices'])==6,
            'deck_is_an_involution':all(swap[swap[v]]==v for v in verts),
            'deck_preserves_actual_coefficient_readout':all(record['projection'][swap[v]]==record['projection'][v] for v in verts),
            'deck_fixes_only_seam_vertices':sum(swap[v]==v for v in verts)==6}
    oriented={cyclic(face) for face in record['oriented_faces']}
    checks['deck_reverses_sphere_orientation_on_every_face']=all(cyclic([swap[v] for v in reversed(face)]) in oriented for face in record['oriented_faces'])
    counts=Counter(tuple(v) for v in record['original_fold_owners'])
    checks['all_24_original_inward_flags_retained']=len(counts)==24
    checks['upper_six_flags_refined_threefold_lower_eighteen_unchanged']=Counter(counts.values())=={1:18,3:6}
    original=source['source']['record']['directions']
    checks['every_original_direction_vertex_is_still_present']=all(any(r['barycentric']==point for r in verts.values()) for point in original['vertices'].values())
    grid=list(grid4(12)); exact=True; involution=True
    for v in grid:
        exact &= decode(encode(v,p,n,recovery),p,n,recovery)==v
        involution &= deck(deck(v,p,n,recovery),p,n,recovery)==v
    checks['sheet_codec_round_trips_all_290_boundary_grid_points']=len(grid)==290 and exact
    checks['deck_involution_on_complete_boundary_grid']=involution
    census=Counter(); image_ok=True
    for a in range(13):
        for b in range(13-a):
            c=12-a-b; upper=(Q(a,12),Q(b,12),Q(c,12),Q(0))
            endpoints=fiber(mode(p,direction(upper)),p,n,recovery)
            expected=1 if min(a,b,c)==0 else 2
            image_ok &= len(endpoints)==expected and upper in endpoints
            census[len(endpoints)]+=1
    checks['image_grid_has_55_double_and_36_single_fibers']=image_ok and dict(census)=={1:36,2:55}
    outside=[Q(2)*a for a in direction((Q(1),Q(0),Q(0),Q(0)))]
    checks['mode_outside_image_rejected']=rejected(lambda:fiber(mode(p,outside),p,n,recovery))
    seam=encode((Q(1),Q(0),Q(0),Q(0)),p,n,recovery); seam['sheet']='upper'
    checks['spurious_second_seam_point_rejected']=rejected(lambda:decode(seam,p,n,recovery))
    # A closed six-step interior loop has two independently closing lifts.
    circle=[(Q(1),Q(0),Q(0)),(Q(1,2),Q(1,2),Q(0)),(Q(0),Q(1),Q(0)),
            (Q(0),Q(1,2),Q(1,2)),(Q(0),Q(0),Q(1)),(Q(1,2),Q(0),Q(1,2))]
    loops={'upper':[],'lower':[]}
    for u in circle+[circle[0]]:
        point=tuple(Q(1,6)+a/2 for a in u)+(Q(0),)
        ends=fiber(mode(p,direction(point)),p,n,recovery)
        for label,index in [('lower',0),('upper',1)]: loops[label].append(list(map(str,ends[index])))
    checks['interior_loop_closes_on_each_sheet_without_swap']=all(path[0]==path[-1] for path in loops.values()) and loops['upper']!=loops['lower']
    bad=deepcopy(packet); bad['record']['deck_vertex_map'][next(v for v in swap if swap[v]!=v)]=next(iter(verts)); bad['root']=digest(bad['record'])
    checks['honestly_rehashed_wrong_sheet_map_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); bad['record']['original_fold_owners'].pop(); bad['root']=digest(bad['record'])
    checks['honestly_rehashed_missing_fold_provenance_rejected']=rejected(lambda:verify(bad))
    checks['complete_serialized_atlas_reverifies']=verify(json.loads(json.dumps(packet)))==report
    result={'schema':'marici.projector-fold-sheets-check.v1','passed':all(checks.values()),'checks':checks,'topology':report,
            'boundary_grid_points':len(grid),'image_grid_fiber_census':dict(census),'closed_lifts':loops,
            'root':packet['root'],'source_root':source['root'],'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Two geometric sheets follow from the actual projector on the declared real tetrahedral directions. The cover of the interior is trivial; sheets meet at the boundary. No neutron or charge identification.'}
    out=BASE/'results'
    (out/'projector_fold_sheets_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'projector_fold_sheets.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
