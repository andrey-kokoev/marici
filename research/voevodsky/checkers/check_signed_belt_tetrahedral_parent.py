"""Exact test: regular R4 tetrahedron -> medial octahedron -> signed belt.
The projection is orthogonal in the declared diagonal metric. This is NOT a
projection of the entire tetrahedron onto the belt, nor unitary spin transport.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
from hashlib import sha256
import json
from check_particle_construction_routes import (R,cast,ident,scale,plus,adj,trace,
    cross,sub,dot,projector,sum_m,return_matrix,supports,encode)
from check_electron_charge_spin_frontier import ga,gs,gm,gmm,G0

BASE=Path(__file__).resolve().parents[1]
def qsqrt(q):
    if q<0:return None
    a,b=isqrt(q.numerator),isqrt(q.denominator)
    return F(a,b) if a*a==q.numerator and b*b==q.denominator else None
def norminv(q):
    for d,root in [(1,cast(1)),(3,R((0,1,0,0))),(222,R((0,0,0,1)))]:
        r=qsqrt(q/F(d))
        if r:return root/(d*r)
    raise AssertionError(('unsupported squared norm',q))
def average(ps):return tuple(sum(p[j] for p in ps)/len(ps) for j in range(len(ps[0])))
def physical(p):return (R((0,p[0],0,0)),cast(p[1]),cast(p[2]))
def outward(points,face):
    ps=[physical(points[k]) for k in face]
    n=cross(sub(ps[1],ps[0]),sub(ps[2],ps[0]))
    c=average([points[k] for k in face])
    # Sign can be checked rationally in scaled coordinates.
    r=cross(sub(points[face[1]],points[face[0]]),sub(points[face[2]],points[face[0]]))
    if dot(r,c)<0:n=tuple(-v for v in n)
    q=dot(n,n);assert all(v==0 for v in q.c[1:]) and q.c[0]>0
    return tuple(v*norminv(q.c[0]) for v in n)
def dist2(a,b,metric):return sum(w*(x-y)**2 for x,y,w in zip(a,b,metric))
def mprod(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def matrix_token(m):return sha256(json.dumps([[str(x) for x in row] for row in m],separators=(',',':')).encode()).hexdigest()
def encode_points(p):return {k:list(map(str,v)) for k,v in p.items()}
def decode(z):return tuple(R(tuple(map(F,v))) for v in z)

def main():
    paths={'geometry':BASE/'results/four_six_center_cones.json',
           'fourth':BASE/'results/conditional_fourth_spinor_store.json',
           'paired_belt':BASE/'results/opposite_branch_belt_store.json'}
    raw={k:p.read_bytes() for k,p in paths.items()};data={k:json.loads(v) for k,v in raw.items()}
    geo,x,paired=(data[k] for k in ('geometry','fourth','paired_belt'))
    assert geo['verification_passed']
    for k in ('geometry','paired_belt'):assert x['source_sha256'][k]==sha256(raw[k]).hexdigest()
    g=F(geo['gap']);assert g==F(7,10)
    # Source recipe, independent of the target arrow coefficients.
    # Physical coordinates: (sqrt(3) X,Y,Z,sqrt(2-g^2) H).
    t4={'A':(F(0),3*g/2,F(0),F(3,2)),
        'B':(F(0),-g/2,F(2),F(-1,2)),
        'C':(F(-1),-g/2,F(-1),F(-1,2)),
        'D':(F(1),-g/2,F(-1),F(-1,2))}
    metric4=(F(3),F(1),F(1),2-g*g);assert metric4[-1]>0
    edges=list(combinations('ABCD',2))
    lifted_lengths={dist2(t4[a],t4[b],metric4) for a,b in edges};assert lifted_lengths=={12}
    t3={k:v[:3] for k,v in t4.items()}
    projected_lengths={dist2(t3[a],t3[b],(3,1,1)) for a,b in edges}
    assert projected_lengths=={F(12),F(149,25)}
    # Finite falsifier: keeping all vertices but perturbing the hidden metric
    # destroys regularity; projecting the full tetrahedron stays four-vertex.
    bad_metric=(3,1,1,metric4[-1]-F(1,100))
    bad_lengths={dist2(t4[a],t4[b],bad_metric) for a,b in edges}
    assert bad_lengths=={F(12),F(299,25)}
    names={'AB':'U0','AC':'U1','AD':'U2','BC':'L1','BD':'L2','CD':'L0'}
    edge_for={name:set(edge) for edge,name in names.items()}
    mids4={names[a+b]:average([t4[a],t4[b]]) for a,b in edges}
    mids={k:v[:3] for k,v in mids4.items()}
    target={k:tuple(map(F,v)) for k,v in geo['belt_scaled_coordinates'].items() if k!='O'}
    assert mids==target
    # Midpoint subdivision has four corner tetrahedra and a medial octahedron.
    faces=[]
    for f in combinations(mids,3):
        shared=set.intersection(*(edge_for[k] for k in f))
        union=set.union(*(edge_for[k] for k in f))
        if len(shared)==1 or len(union)==3:faces.append(frozenset(f))
    assert len(faces)==8
    caps={frozenset(('U0','U1','U2')),frozenset(('L0','L1','L2'))}
    belt=set(faces)-caps
    ordered_faces=geo['belt_faces'];assert belt=={frozenset(f) for f in ordered_faces}
    normal=[outward(mids,f) for f in ordered_faces]
    parent_normals={''.join(f):outward(t3,f) for f in combinations('ABCD',3)}
    records=[];ps=[];signs=[]
    for f,n in zip(ordered_faces,normal):
        shared=set.intersection(*(edge_for[k] for k in f))
        union=set.union(*(edge_for[k] for k in f))
        if len(shared)==1:
            parent=''.join(sorted(set('ABCD')-shared));chi=-1;kind='corner_cut'
        else:
            assert len(union)==3
            parent=''.join(sorted(union));chi=1;kind='central_parent_face'
        m=parent_normals[parent]
        assert tuple(chi*v for v in n)==m
        p=projector(n,chi);assert p==projector(m,1)
        ps.append(p);signs.append(chi)
        records.append({'panel':f,'kind':kind,'parent_face':parent,'chi':chi})
    assert signs==x['face_signs']==paired['face_signs']==[-1,-1,-1,1,1,1]
    duplicates=[[0,3],[1,5],[2,4]]
    assert all(ps[i]==ps[j] for i,j in duplicates) and len(set(ps))==3
    # Compute the inverse from the NEW frame, not from the old stored inverse.
    S=sum_m(ps);det=ga(gm(S[0][0],S[1][1]),gs(-1,gm(S[0][1],S[1][0])))
    assert det[1]==0 and all(v==0 for v in det[0].c[1:]) and det[0].c[0]==F(441,74)
    inv=scale(1/det[0].c[0],((S[1][1],gs(-1,S[0][1])),(gs(-1,S[1][0]),S[0][0])))
    assert gmm(S,inv)==ident(2)
    N=return_matrix(ps,inv)
    L=tuple(tuple(ps[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(12)) for i in range(12))
    arrows=[{'stage':stage,'target':i,'source':j,'weight':encode(m[i][j])} for stage,m in [('L',L),('G',N),('N',N)] for i in range(12) for j in range(12) if m[i][j]!=G0]
    assert arrows==x['arrows'] and len(arrows)==312
    assert adj(N)==N and gmm(N,N)==N and trace(N)==(cast(2),cast(0))
    wrong=[projector(n,1) for n in normal]
    wrongN=return_matrix(wrong,scale(F(1,3),ident(2)))
    assert wrongN!=N and sum(supports(wrong,wrongN).values())==264
    # Six exposed extreme points: duals to independent U0,U1,U2 single out
    # the six antipodal vertices. No affine image of four vertices has six.
    p,q,r=(mids[k] for k in ('U0','U1','U2'))
    determinant=dot(p,cross(q,r));assert determinant==-F(21,40)
    duals=[tuple(v/determinant for v in row) for row in (cross(q,r),cross(r,p),cross(p,q))]
    support_certificates=[]
    for d in duals:
        for s in (-1,1):
            values={k:s*dot(d,v) for k,v in mids.items()}
            assert sorted(values.values())==[-1,0,0,0,0,1]
            support_certificates.append({k:str(v) for k,v in values.items()})
    edgecounts={}
    for f in belt:
        for e in combinations(sorted(f),2):edgecounts[e]=edgecounts.get(e,0)+1
    boundary={frozenset(e) for e,count in edgecounts.items() if count==1}
    assert len(edgecounts)==12 and len(boundary)==6 and 6-12+6==0
    assert boundary=={frozenset(e) for cap in caps for e in combinations(cap,2)}
    # The regular parent's face normals are equiangular in its intrinsic
    # (sqrt(3)X,sqrt(2)H,Z) coordinates. Projection changes their angles.
    intrinsic={k:(v[0],v[3],v[2]) for k,v in t4.items()}
    normals0=[]
    for f in combinations('ABCD',3):
        a,b,c=[intrinsic[k] for k in f];n=cross(sub(b,a),sub(c,a))
        if dot(n,average([a,b,c]))<0:n=tuple(-v for v in n)
        assert sum(n[i]*n[i]/F((3,2,1)[i]) for i in range(3))==18
        a3,b3,c3=[t3[k] for k in f]
        projected_covector=cross(sub(b3,a3),sub(c3,a3))
        if dot(projected_covector,average([a3,b3,c3]))<0:projected_covector=tuple(-v for v in projected_covector)
        assert projected_covector==(g*n[0],n[1],g*n[2])
        normals0.append(n)
    old_dots={sum(a[i]*b[i]/F((3,2,1)[i]) for i in range(3))/18 for a,b in combinations(normals0,2)}
    assert old_dots=={-F(1,3)}
    new_dots={dot(normal[i],normal[j]) for i,j in combinations(range(3),2)}
    assert new_dots=={cast(F(1,148))}
    overlaps={trace(gmm(ps[i],ps[j])) for i,j in combinations(range(3),2)}
    assert overlaps=={(cast(F(149,296)),cast(0))}
    # Linear midpoint/projection square on arbitrary labelled configurations.
    def project_matrix(count):return [[F(int(j==4*(i//3)+i%3)) for j in range(4*count)] for i in range(3*count)]
    def midpoint_matrix(dim):
        return [[F(1,2) if j//dim in ('ABCD'.index(edges[i//dim][0]),'ABCD'.index(edges[i//dim][1])) and j%dim==i%dim else F(0) for j in range(4*dim)] for i in range(6*dim)]
    pt,pm=project_matrix(4),project_matrix(6);m4,m3=midpoint_matrix(4),midpoint_matrix(3)
    first_project=mprod(m3,pt);first_midpoint=mprod(pm,m4);assert first_project==first_midpoint
    matrices={'project_vertices':pt,'midpoint_4d':m4,'midpoint_3d':m3,'project_midpoints':pm,'via_projection':first_project,'via_midpoints':first_midpoint}
    diagram={'id':'voevodsky-belt-tetrahedral-parent-square','objects':[{'id':k,'dimension':v,'type':'rational_scaled_labelled_coordinate_packet'} for k,v in [('T4',16),('T3',12),('M4',24),('M3',18)]],
        'arrows':[{'id':k,'source':s,'target':t,'map_token':matrix_token(matrices[k])} for k,s,t in [('project_vertices','T4','T3'),('midpoint_4d','T4','M4'),('midpoint_3d','T3','M3'),('project_midpoints','M4','M3'),('via_projection','T4','M3'),('via_midpoints','T4','M3')]],
        'cells':[{'id':'midpoints_commute_with_projection','routes':[['via_projection'],['via_midpoints']],'witness':'check_signed_belt_tetrahedral_parent.py computes both exact composite matrices independently.'}],
        'obstructions':[{'id':'unmodified_spinor_transport','reason':'Regular face overlap 1/3 differs from projected side-face overlap 149/296.'}],
        'claims':[{'id':'signed_subdivision_assembly','requires':['midpoint_square','312_coefficient_equality']},{'id':'positron_identification','requires':['charge_conjugation_map','mass_and_charge_readouts']}],
        'available_witnesses':['midpoint_square','312_coefficient_equality'],
        'higher_coherence':[{'id':'physical_antiparticle_comparison','degree':3,'state':'unsupported'}]}
    (BASE/'contracts').mkdir(exist_ok=True)
    (BASE/'contracts/signed-belt-tetrahedral-parent.json').write_text(json.dumps(diagram,indent=2)+'\n',encoding='utf-8')
    checks={
        'regular_tetrahedron_in_R4_all_six_squared_edges_12':lifted_lengths=={12},
        'perturbed_hidden_metric_fails_regularity':len(bad_lengths)==2,
        'projected_midpoints_match_all_six_retained_vertices':mids==target,
        'medial_octahedron_minus_two_caps_matches_exact_six_panels':belt=={frozenset(f) for f in ordered_faces},
        'corner_vs_parent_orientation_derives_retained_signs':signs==x['face_signs'],
        'parent_projectors_match_all_signed_belt_projectors':all(projector(parent_normals[r['parent_face']],1)==p for r,p in zip(records,ps)),
        'all_312_retained_coefficients_reconstructed':arrows==x['arrows'],
        'return_remains_Hermitian_rank_two_projector':adj(N)==N and gmm(N,N)==N and trace(N)==(cast(2),cast(0)),
        'erasing_orientation_signs_fails_coefficient_match':wrongN!=N,
        'six_extreme_points_exclude_whole_tetrahedron_affine_projection':len(support_certificates)==6,
        'two_boundary_loops_exclude_closed_tetrahedral_surface':len(boundary)==6 and 6-12+6==0,
        'only_three_distinct_parent_face_projectors_retained':len(set(ps))==3,
        'all_four_parent_normals_transport_by_projection_cofactor':True,
        'projected_overlap_excludes_global_unitary_or_antiunitary_face_transport':F(149,296)!=F(1,3),
        'midpoint_projection_square_commutes_for_every_coordinate_packet':first_project==first_midpoint,
        'all_source_artifacts_unchanged':all(p.read_bytes()==raw[k] for k,p in paths.items())}
    report={'verification_passed':all(checks.values()),'checks':checks,
        'classification':'exact_regular_R4_parent_with_signed_medial_subassembly_not_whole_tetrahedral_projection',
        'gap':str(g),'lifted_scaled_vertices':encode_points(t4),'physical_coordinate_frame':['sqrt(3) X','Y','Z','sqrt(151)/10 H'],
        'projected_scaled_vertices':encode_points(t3),'midpoint_labels':names,'panel_inheritance':records,
        'duplicate_projector_face_indices_zero_based':duplicates,'omitted_parent_face':'BCD',
        'regular_squared_edges':['12'],'projected_squared_edges':list(map(str,sorted(projected_lengths))),
        'normal_overlap_residual':{'regular_projector_overlap':'1/3','projected_side_projector_overlap':'149/296'},
        'six_extreme_point_certificates':support_certificates,
        'normalization':'Recompute projections from projected Euclidean normals, then recompute S and S^-1. Not unitary transport of the unmodified regular parent projectors.',
        'disposition':'A regular tetrahedron embedded in R4 generates the current signed belt by midpoint subdivision, two-cap omission and orthogonal projection. Matching all 312 coefficients requires the existing spinor rule on projected geometry and its frame normalization. The belt is a proper subassembly, not the entire tetrahedron in disguise. No positron identification is established.',
        'source_sha256':{k:sha256(v).hexdigest() for k,v in raw.items()},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/signed_belt_tetrahedral_parent.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/signed_belt_tetrahedral_parent_maps.json').write_text(json.dumps({k:[[str(v) for v in row] for row in m] for k,m in matrices.items()},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)
if __name__=='__main__':main()
