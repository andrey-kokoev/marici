"""Exact geometric attachment to one retained proton-like boundary triangle.
Adds a tetrahedron with specified barycenter, not a particle or interaction law.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from copy import deepcopy
import json

from check_proton_merkle_reassembly import verify as verify_focus, POINTS

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,s): return tuple(x*s for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mean(points): return tuple(sum(p[i] for p in points)/len(points) for i in range(3))
def encoded(p): return list(map(str,p))
def digest(r): return sha256(b'marici.proton-face-extension.v1\0'+json.dumps(r,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def geometry(focus):
    store=focus['objects']; root=store[focus['root']]
    return store[root['geometry']]['payload']

def derive(geo,label,center):
    records=geo['triangles_and_transports']; triangles=[r['triangle'] for r in records]
    selected=next(r['triangle'] for r in records if r['outer_arrow']==label)
    points={k:tuple(map(Q,v)) for k,v in POINTS.items()}
    for tri in triangles:
        face=tri[0][2:]; points[tri[0]]=mean([points[v] for v in face])
    a,b,c=[points[v] for v in selected]; q=mean([a,b,c])
    normal=cross(sub(b,a),sub(c,a)); plane=dot(normal,a)
    if plane<=0 or any(dot(normal,p)>plane for p in points.values()): raise ValueError('not a supporting outward face')
    d=sub(scale(center,4),add(add(a,b),c))
    if dot(normal,d)<=plane: raise ValueError('new apex is not strictly outside the supporting plane')
    # Original body is in the inward half-space, new cell in the outward one:
    # their intersection is precisely the selected triangular base.
    points['E']=d
    cell=['E',selected[0],selected[2],selected[1]]
    tetra=[points[v] for v in cell]
    volume=det(sub(tetra[1],tetra[0]),sub(tetra[2],tetra[0]),sub(tetra[3],tetra[0]))/6
    if volume<=0 or mean(tetra)!=center: raise ValueError('wrong oriented volume or barycenter')
    A,B,C=selected
    boundary=[t for t in triangles if t!=selected]+[['E',B,C],['E',A,B],['E',C,A]]
    edge_counts=Counter(); signs=Counter(); links=defaultdict(list)
    for tri in boundary:
        for u,v in zip(tri,tri[1:]+tri[:1]):
            key=tuple(sorted((u,v))); edge_counts[key]+=1; signs[key]+=1 if u<v else -1
        for i,v in enumerate(tri): links[v].append((tri[i-1],tri[(i+1)%3]))
    link_cycles=True
    for v,pairs in links.items():
        degrees=Counter(); adjacent=defaultdict(set)
        for u,w in pairs: degrees[u]+=1; degrees[w]+=1; adjacent[u].add(w); adjacent[w].add(u)
        seen=set(); todo=[next(iter(degrees))]
        while todo:
            u=todo.pop()
            if u not in seen: seen.add(u); todo.extend(adjacent[u]-seen)
        link_cycles &= all(x==2 for x in degrees.values()) and seen==set(degrees)
    if not all(n==2 for n in edge_counts.values()) or any(signs.values()) or not link_cycles: raise ValueError('boundary not an oriented surface')
    boundary_volume=sum(det(*(points[v] for v in tri))/6 for tri in boundary)
    original_volume=sum(det(*(points[v] for v in tri))/6 for tri in triangles)
    if boundary_volume!=original_volume+volume: raise ValueError('volume does not add')
    # Segment O -> center must actually pass through the selected triangular face.
    denominator=dot(normal,center)
    parameter=plane/denominator; crossing=scale(center,parameter)
    u,v,w=sub(b,a),sub(c,a),sub(crossing,a)
    gram=dot(u,u)*dot(v,v)-dot(u,v)**2
    beta=(dot(w,u)*dot(v,v)-dot(w,v)*dot(u,v))/gram
    gamma=(dot(w,v)*dot(u,u)-dot(w,u)*dot(u,v))/gram
    bary=(1-beta-gamma,beta,gamma)
    if not 0<parameter<1 or any(x<0 for x in bary): raise ValueError('center segment misses the selected face')
    return {'kind':'geometric-face-extension','selected_outer_arrow':label,'shared_triangle':selected,
            'target_barycenter':encoded(center),'new_apex':encoded(d),'oriented_cell':cell,
            'points':{k:encoded(v) for k,v in points.items()},'boundary_triangles':boundary,
            'added_volume':str(volume),'original_volume':str(original_volume),'total_volume':str(boundary_volume),
            'segment_crossing_parameter':str(parameter),'segment_face_coordinates':encoded(bary),
            'surface_counts':{'vertices':len(points),'edges':len(edge_counts),'triangles':len(boundary),'euler_characteristic':len(points)-len(edge_counts)+len(boundary)},
            'new_interaction_map':'not supplied','new_particle_identity':'not inferred'}

def construct(focus,label='AB',radial_scale=Q(5,4)):
    geo=geometry(focus); tri=next(r['triangle'] for r in geo['triangles_and_transports'] if r['outer_arrow']==label)
    points={k:tuple(map(Q,v)) for k,v in POINTS.items()}; points[tri[0]]=mean([points[k] for k in tri[0][2:]])
    center=scale(mean([points[v] for v in tri]),radial_scale)
    cell=derive(geo,label,center); cref=digest(cell)
    root={'kind':'attached-proton-geometry','focus':focus['root'],'extension':cref,'transport_segment':{'source':['0','0','0'],'target':encoded(center)}}
    return {'schema':'marici.proton-face-extension.v1','focus':focus,'root':digest(root),'objects':{cref:cell,digest(root):root}}

def verify(packet):
    if set(packet)!={'schema','focus','root','objects'} or packet['schema']!='marici.proton-face-extension.v1': raise ValueError('packet schema')
    base,_=verify_focus(packet['focus']); store=packet['objects']
    root=store[packet['root']]
    if digest(root)!=packet['root'] or set(root)!={'kind','focus','extension','transport_segment'} or root['kind']!='attached-proton-geometry' or root['focus']!=base['root']: raise ValueError('root binding')
    cell=store[root['extension']]
    if digest(cell)!=root['extension']: raise ValueError('extension hash')
    expected=derive(geometry(packet['focus']),cell['selected_outer_arrow'],tuple(map(Q,cell['target_barycenter'])))
    if cell!=expected or root['transport_segment']!={'source':['0','0','0'],'target':cell['target_barycenter']}: raise ValueError('attachment or segment mismatch')
    return {'verified':True,'root':packet['root'],'retained_internal_arrows':base['arrows'],**{k:cell[k] for k in ('shared_triangle','target_barycenter','new_apex','added_volume','total_volume','surface_counts','segment_crossing_parameter','segment_face_coordinates','new_interaction_map','new_particle_identity')}}

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError,ZeroDivisionError): return True
    return False

def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); packet=construct(focus); report=verify(packet)
    checks={'original_1836_arrow_package_retained':report['retained_internal_arrows']==1836,
            'barycenter_reconstructs_outward_tetrahedron':report['target_barycenter']==['35/36','5/36','-5/36'] and report['new_apex']==['14/9','2/9','-2/9'],
            'closed_surface_with_14_triangles':report['surface_counts']=={'vertices':9,'edges':21,'triangles':14,'euler_characteristic':2},
            'added_volume_2_over_9_total_26_over_9':report['added_volume']=='2/9' and report['total_volume']=='26/9',
            'center_segment_crosses_inside_selected_face':report['segment_crossing_parameter']=='4/5' and report['segment_face_coordinates']==['1/3']*3,
            'degenerate_face_center_rejected':rejected(lambda:construct(focus,radial_scale=Q(1))),
            'inward_attachment_rejected':rejected(lambda:construct(focus,radial_scale=Q(3,4)))}
    geo=geometry(focus)
    checks['all_twelve_source_faces_admit_radial_extensions']=all(construct(focus,r['outer_arrow'])['root'] for r in geo['triangles_and_transports'])
    bigger=construct(focus,radial_scale=Q(3,2)); cell=bigger['objects'][bigger['objects'][bigger['root']]['extension']]
    checks['barycenter_position_changes_volume_not_particle_label']=cell['added_volume']=='4/9'
    bad=deepcopy(packet); root=deepcopy(bad['objects'][bad['root']]); cell=deepcopy(bad['objects'][root['extension']]); cell['new_apex'][0]='0'; new=digest(cell); bad['objects'][new]=cell; root['extension']=new; bad['root']=digest(root); bad['objects'][bad['root']]=root
    checks['rehashed_wrong_apex_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); root=deepcopy(bad['objects'][bad['root']]); root['transport_segment']['source']=['1','0','0']; bad['root']=digest(root); bad['objects'][bad['root']]=root
    checks['rehashed_wrong_starting_center_rejected']=rejected(lambda:verify(bad))
    checks['serialized_attachment_reverifies']=verify(json.loads(json.dumps(packet)))==report
    out=BASE/'results'
    (out/'proton_face_extension_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    result={'schema':'marici.proton-face-extension-check.v1','passed':all(checks.values()),'checks':checks,'extension':report,
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'focus_file_sha256':sha256(FOCUS.read_bytes()).hexdigest()}
    (out/'proton_face_extension.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    cell=packet['objects'][packet['objects'][packet['root']]['extension']]; names=list(cell['points']); indices={v:i+1 for i,v in enumerate(names)}
    obj=['# One outward tetrahedral attachment; no physical particle interpretation']
    obj+=['v '+' '.join(str(float(Q(x))) for x in cell['points'][v]) for v in names]
    obj+=['f '+' '.join(str(indices[v]) for v in tri) for tri in cell['boundary_triangles']]
    (out/'proton_face_extension.obj').write_text('\n'.join(obj)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
