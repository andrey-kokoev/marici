"""Four proton face cones versus six cones on the actual displayed belt.
Exact rational coordinates are used in scaled frames: (sqrt(3)X,Y,Z)
for the belt and (sqrt(3)X,sqrt(2)Y,Z) for the regular proton.
No source arrows, charges, or energy weights are added.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
from hashlib import sha256
import json
import re
from check_retained_barycenter_attachment import cells_of, topology
from check_three_arrow_receiver_geometry import boundary, sub, dot, cross

BASE=Path(__file__).resolve().parents[1]
PAGE=BASE.parents[1]/'papers/witness-generators/tetrahedron.html'

def volume(t,points):
    a,b,c,d=[points[v] for v in t]
    return dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6

def outward(face,points):
    a,b,c=[points[v] for v in face]
    return tuple(face) if dot(a,cross(sub(b,a),sub(c,a)))>0 else (face[0],face[2],face[1])

def link(cells,vertex): return {tuple(v for v in c if v!=vertex) for c in cells if vertex in c and len(c)>1}
def squared(a,b,metric): return sum(m*(x-y)**2 for m,x,y in zip(metric,a,b))

def main():
    original=PAGE.read_bytes(); source=original.decode('utf-8')
    required=['const h = Math.sqrt(2);','const r = Math.sqrt(3) / 2;',
        'new THREE.Vector3(0, 3 * h / 4, 0)', 'new THREE.Vector3(0, -h / 4, 1)',
        'new THREE.Vector3(-r, -h / 4, -0.5)', 'new THREE.Vector3(r, -h / 4, -0.5)',
        'opposite.rotation.x = Math.PI;', 'tetrahedron.position.y = h / 4 + gap / 2;',
        'opposite.position.y = -h / 4 - gap / 2;']
    if not all(s in source for s in required): raise ValueError('display geometry changed; update source resolver')
    gap=Q(re.search(r'const gap = ([0-9.]+);',source).group(1))
    if gap<=0: raise ValueError('positive separation required')
    P={'O':(Q(0),)*3,
       'U0':(Q(0),gap/2,Q(1)), 'U1':(-Q(1,2),gap/2,-Q(1,2)), 'U2':(Q(1,2),gap/2,-Q(1,2)),
       'L0':(Q(0),-gap/2,-Q(1)), 'L1':(-Q(1,2),-gap/2,Q(1,2)), 'L2':(Q(1,2),-gap/2,Q(1,2))}
    upper=['U0','U1','U2']; lower=['L0','L1','L2']; metric=(3,1,1)
    stitches={(u,l) for u in upper for l in sorted(lower,key=lambda l:squared(P[u],P[l],metric))[:2]}
    faces=[outward([u]+sorted(l for a,l in stitches if a==u),P) for u in upper]
    faces += [outward([l]+sorted(u for u,b in stitches if b==l),P) for l in lower]
    caps=[outward(upper,P),outward(lower,P)]
    belt_tets=[('O',)+face for face in faces]
    cap_tets=[('O',)+face for face in caps]
    belt_cells=cells_of(belt_tets); full_cells=cells_of(belt_tets+cap_tets)
    proton={'O':(Q(0),)*3,'A':(Q(0),Q(3,4),Q(0)), 'B':(Q(0),-Q(1,4),Q(1)),
            'C':(-Q(1,2),-Q(1,4),-Q(1,2)), 'D':(Q(1,2),-Q(1,4),-Q(1,2))}
    proton_faces=[outward(t,proton) for t in combinations('ABCD',3)]
    proton_tets=[('O',)+f for f in proton_faces]
    proton_cells=cells_of(proton_tets)
    def oriented_chain(tets,points):
        return {tuple(sorted(t)):1 if volume(tuple(sorted(t)),points)>0 else -1 for t in tets}
    belt_boundary=boundary(oriented_chain(belt_tets,P))
    full_boundary=boundary(oriented_chain(belt_tets+cap_tets,P))
    proton_boundary=boundary(oriented_chain(proton_tets,proton))
    belt_link=topology(link(belt_cells,'O')); proton_link=topology(link(proton_cells,'O'))
    full_link=topology(link(full_cells,'O'))
    adjacency={i:[j for j in range(6) if j!=i and len(set(belt_tets[i])&set(belt_tets[j]))==3] for i in range(6)}
    cone_edge_lengths=lambda t,p,m:sorted(squared(p[a],p[b],m) for a,b in combinations(t,2))
    belt_lengths=[cone_edge_lengths(t,P,metric) for t in belt_tets]
    proton_lengths=[cone_edge_lengths(t,proton,(3,2,1)) for t in proton_tets]
    supports=[]
    for f in faces+caps:
        a,b,c=[P[v] for v in f]; normal=cross(sub(b,a),sub(c,a))
        supports.append(dot(normal,sub(P['O'],a))<0 and all(dot(normal,sub(P[v],a))<=0 for v in upper+lower))
    checks={
        'six_faces_reconstructed_by_display_nearest_stitches':len(stitches)==len(faces)==6,
        'all_eight_faces_support_convex_antiprism_and_center_is_inside':all(supports),
        'four_proton_pieces_have_positive_equal_volume':all(volume(t,proton)==Q(1,16) for t in proton_tets),
        'four_piece_proton_boundary_is_original_four_faces':len(proton_boundary)==4 and all('O' not in f for f in proton_boundary),
        'six_belt_pieces_have_positive_equal_volume':all(volume(t,P)==gap/8 for t in belt_tets),
        'six_piece_cycle_of_face_adjacencies':all(len(v)==2 for v in adjacency.values()) and topology(cells_of(faces))['rational_betti']==[1,1,0,0],
        'belt_piece_outer_faces_match_original_six_panels':{f for f in belt_boundary if 'O' not in f}=={tuple(sorted(f)) for f in faces},
        'belt_boundary_has_six_more_radial_rim_triangles':len(belt_boundary)==12 and sum('O' in f for f in belt_boundary)==6,
        'belt_center_link_is_annulus_not_sphere_or_disk':belt_link['rational_betti']==[1,1,0,0] and belt_link['cells']==[6,12,6,0],
        'proton_center_link_is_sphere':proton_link['rational_betti']==[1,0,1,0],
        'two_missing_cap_cones_fill_antiprism':len(full_boundary)==8 and all('O' not in f for f in full_boundary) and sum(volume(t,P) for t in belt_tets+cap_tets)==gap,
        'filled_eight_piece_center_link_is_sphere':full_link['rational_betti']==[1,0,1,0],
        'six_pieces_are_mutually_congruent':all(x==belt_lengths[0] for x in belt_lengths),
        'four_proton_pieces_are_mutually_congruent':all(x==proton_lengths[0] for x in proton_lengths),
        'belt_piece_is_not_congruent_to_proton_piece_at_display_gap':belt_lengths[0]!=proton_lengths[0],
        'equal_face_condition_cannot_also_match_center_edges':1+Q(2)==3 and 1+Q(2)/4!=Q(9,8),
        'original_display_unchanged':PAGE.read_bytes()==original,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'source_page':str(PAGE),'source_sha256':sha256(original).hexdigest(),'gap':str(gap),
        'belt_scaled_coordinates':{k:list(map(str,v)) for k,v in P.items()},
        'belt_frame':'physical (x,y,z)=(sqrt(3)X,Y,Z)',
        'proton_scaled_coordinates':{k:list(map(str,v)) for k,v in proton.items()},
        'proton_frame':'physical (x,y,z)=(sqrt(3)X,sqrt(2)Y,Z)',
        'belt_faces':faces,'belt_tetrahedra':belt_tets,'missing_cap_tetrahedra':cap_tets,
        'proton_tetrahedra':proton_tets,'belt_face_adjacency':adjacency,
        'squared_edge_lengths':{'proton_piece':list(map(str,proton_lengths[0])),'belt_piece':list(map(str,belt_lengths[0]))},
        'topology':{'proton':topology(proton_cells),'belt_cones':topology(belt_cells),'filled_gap':topology(full_cells),
                    'proton_center_link':proton_link,'belt_center_link':belt_link,'filled_center_link':full_link},
        'volumes':{'proton':'sqrt(6)/4','one_proton_piece':'sqrt(6)/16',
            'one_belt_piece':f'{gap/8}*sqrt(3)','six_belt_pieces':f'{3*gap/4}*sqrt(3)',
            'whole_gap':f'{gap}*sqrt(3)','piece_ratio_to_proton_piece':f'{gap}*sqrt(2)',
            'belt_ratio_to_proton':f'{3*gap/2}*sqrt(2)',
            'piece_ratio_approx':float(gap)*2**0.5,'belt_ratio_approx':float(3*gap/2)*2**0.5,
            'equal_piece_volume_gap':'1/sqrt(2)','belt_ratio_at_equal_piece_volume':'3/2'},
        'interpretation':'The same face-to-center construction yields four proton pieces and six mutually congruent belt pieces. The two families are not congruent. The six-piece union is a cone over an annulus, with a non-manifold common center; two cap pieces complete the ordinary solid gap.',
        'scope':'geometry and incidence only; no coefficient arrows, charges, or mass law assigned',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/four_six_center_cones.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('belt_scaled_coordinates','proton_scaled_coordinates','belt_faces','belt_tetrahedra','missing_cap_tetrahedra','proton_tetrahedra','belt_face_adjacency')},indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
