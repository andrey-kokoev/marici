"""Audit the actual six-panel belt against the existing operator theorem.
Uses the original proton's monomial Cartesian frame, not a new sparsifying
basis. Does not invent transport between distinct geometric seed orbits.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import permutations, product
from hashlib import sha256
import json
from check_three_arrow_receiver_geometry import sub, dot, cross, mean

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/four_six_center_cones.json'

def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qm(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qs(s,x): return (s*x[0],s*x[1])
def sum_q(values):
    out=(Q(0),Q(0))
    for value in values: out=qa(out,value)
    return out
def frame(v):
    # Inverse of the displayed proton's rotation and scale: A -> (1,1,1),
    # B -> (1,-1,-1), C -> (-1,1,-1), D -> (-1,-1,1).
    # Input physical coordinates are (sqrt(3) X,Y,Z); output lives in Q(sqrt(2)).
    x,y,z=v
    return ((4*z/3,2*y/3),(-2*z/3-2*x,2*y/3),(-2*z/3+2*x,2*y/3))
def action(r,v):
    return tuple(qa(qa(qs(row[0],v[0]),qs(row[1],v[1])),qs(row[2],v[2])) for row in r)
def det(r): return dot(r[0],cross(r[1],r[2]))
def mm(a,b): return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def mode(triangle,points):
    f,a,b=[frame(points[k]) for k in triangle]
    re=tuple(qa(x,qs(-Q(1,2),qa(y,z))) for x,y,z in zip(f,a,b))
    im=tuple(qs(Q(1,2),qa(y,qs(-1,z))) for y,z in zip(a,b))
    return re,im  # re + i*sqrt(3)*im

def main():
    raw=SOURCE.read_bytes(); source=json.loads(raw)
    if not source['verification_passed']: raise ValueError('unverified geometry')
    points={k:tuple(map(Q,v)) for k,v in source['belt_scaled_coordinates'].items() if k!='O'}
    triangles=[]
    for f in source['belt_faces']:
        center='F_'+'_'.join(sorted(f));points[center]=mean([points[k] for k in f])
        triangles.extend((center,f[i],f[(i+1)%3]) for i in range(3))
    coords={k:frame(v) for k,v in points.items()}
    inverse={v:k for k,v in coords.items()}
    group=[]; names=[]
    for p in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            r=tuple(tuple(Q(signs[i] if j==p[i] else 0) for j in range(3)) for i in range(3))
            if det(r)!=1: continue
            transformed={k:action(r,v) for k,v in coords.items()}
            if not all(v in inverse for v in transformed.values()):continue
            rename={k:inverse[v] for k,v in transformed.items()}
            if {tuple(rename[k] for k in t) for t in triangles}!=set(triangles):continue
            group.append(r);names.append(rename)
    seen=set();orbits=[]
    for triangle in triangles:
        if triangle in seen:continue
        orbit=sorted({tuple(rename[k] for k in triangle) for rename in names})
        seen.update(orbit);orbits.append(orbit)
    all_nonzero=True;generated=True;norms=[];reports=[]
    for orbit in orbits:
        ref=mode(orbit[0],points)
        generated_modes={(action(r,ref[0]),action(r,ref[1])) for r in group}
        actual_modes={mode(t,points) for t in orbit}
        generated &= generated_modes==actual_modes
        ns=[]
        for t in orbit:
            re,im=mode(t,points); n=(Q(0),Q(0))
            for a,b in zip(re,im):
                all_nonzero &= a!=(0,0) or b!=(0,0)
                n=qa(n,qa(qm(a,a),qs(3,qm(b,b))))
            ns.append(n)
        norms.extend(ns)
        g=len(orbit);m=3
        reports.append({'triangles':orbit,'norm_squared_in_proton_frame':[[str(x) for x in n] for n in sorted(set(ns))],
                        'theorem_stage_supports':{'L':g*m*m,'G':g*g*m,'N':g*g*m*m},
                        'separately_closed_support':g*m*m+g*g*m+g*g*m*m})
    gap=Q(source['gap']); b=(4*gap*gap-8)/3
    rim_coords=[coords[k] for k in coords if not k.startswith('F_')]
    covariance=tuple(tuple(sum_q(qm(v[i],v[j]) for v in rim_coords) for j in range(3)) for i in range(3))
    checks={
        'eighteen_face_generated_triangles':len(triangles)==len(set(triangles))==18,
        'six_proper_monomial_symmetries_preserve_actual_source':len(group)==6,
        'distinct_covariance_axis_forces_rotations_to_preserve_rim_axis':covariance==tuple(tuple((8*Q(i==j)+b,Q(0)) for j in range(3)) for i in range(3)) and 4*gap*gap!=8,
        'group_is_closed':all(mm(a,b) in group for a in group for b in group),
        'three_disjoint_six_triangle_orbits':len(orbits)==3 and all(len(o)==6 for o in orbits) and len(seen)==18,
        'each_orbit_matches_rotated_reference_constructor':generated,
        'all_spatial_mode_coordinates_nonzero_in_original_frame':all_nonzero,
        'geometric_modes_have_two_distinct_positive_norms':len(set(norms))==2 and all(n[0]>0 and n[1]==0 for n in norms),
        'not_one_eighteen_triangle_rotation_orbit':all(len(o)!=18 for o in orbits),
        'one_orbit_formula_is_486':all(r['separately_closed_support']==486 for r in reports),
        'three_independent_returns_count_1458_not_one_collective_mode':sum(r['separately_closed_support'] for r in reports)==1458,
        'geometry_input_unchanged':SOURCE.read_bytes()==raw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,'orbits':reports,
        'group_matrices':[[list(map(str,row)) for row in r] for r in group],
        'separately_closed_total':1458,'separately_closed_collective_rank':3,
        'conditional_eighteen_position_monomial_total':4050,
        'outcome':'The existing constructor applies separately to three six-placement seed orbits. The source does not provide a single 18-placement rotation family. Three independent closures have rank three; a one-mode belt requires additional inter-orbit transport, which is not supplied by substituting 18 into the proton formula.',
        'scope':'theorem-hypothesis audit; no new joint belt compiler or physical mass assignment',
        'source_sha256':sha256(raw).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/belt_operator_inputs.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
