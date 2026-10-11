"""Separate passive face-chart reversal from active mode conjugation.
Audit ordinary oriented gluing and the proposed alternating piece branches.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,total,encoded

BASE=Path(__file__).resolve().parents[1]
OMEGA=(R(-Q(1,2)),R(Q(1,2)));OMEGA2=mul(OMEGA,OMEGA)
C=(ONE,OMEGA,OMEGA2)

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def volume(t,p):
    a,b,c,d=[p[k] for k in t];return dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6

def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
def physical(face,coeff,p):return tuple(total(scale(p[k][axis],c) for k,c in zip(face,coeff)) for axis in range(3))
def area(v):return cross(tuple(x[0] for x in v),tuple(x[1] for x in v))

def audit(tets,p,selected):
    incidence={}
    for owner,t in enumerate(tets):
        # Use a positively oriented 3-simplex, absorbing any presentation sign.
        t=list(t)
        if volume(t,p)<0:t[-1],t[-2]=t[-2],t[-1]
        assert volume(t,p)>0
        for k in range(4):
            f=t[:k]+t[k+1:]
            if k%2:f[-1],f[-2]=f[-2],f[-1]
            key=tuple(sorted(f));sgn=parity([key.index(x) for x in f])
            incidence.setdefault(key,[]).append({'owner':owner,'order':f,'sign':sgn})
    internal={k:v for k,v in incidence.items() if len(v)==2}
    assert all(len(v) in (1,2) for v in incidence.values())
    rows=[]
    for key,(a,b) in internal.items():
        assert a['sign']==-b['sign']
        # Equal vertex references determine the transition, not a charge rule.
        # Components are permuted inversely to the real geometric chart.
        target_coeff=tuple(C[a['order'].index(v)] for v in b['order'])
        vi=physical(a['order'],C,p);vj=physical(b['order'],target_coeff,p)
        assert vi==vj
        # The source eigencharacter reverses IN COORDINATES under this odd
        # permutation. The physical vector and its bivector do not reverse.
        shifted=target_coeff[1:]+target_coeff[:1]
        assert shifted==tuple(mul(OMEGA2,z) for z in target_coeff)
        assert area(vi)==area(vj)
        fixed_character=physical(b['order'],C,p)
        # Keeping the same numerical cyclic character in the reversed chart
        # is an ACTIVE change, with opposite area (up to a unit cyclic phase).
        assert area(fixed_character)==tuple(-x for x in area(vi))
        opposite=tuple(map(conj,vi))
        assert opposite!=vi
        # Actual conjugation is anti-linear and therefore cannot silently stand
        # in for the complex-linear bridges of the old projector construction.
        zvi=tuple(mul(OMEGA,x) for x in vi)
        assert tuple(map(conj,zvi))!=tuple(mul(OMEGA,x) for x in opposite)
        coefficient=sum(v['sign']*selected[v['owner']] for v in (a,b))
        rows.append({'face':list(key),'left':a,'right':b,
            'passive_target_coefficients':[encoded(z) for z in target_coeff],
            'physical_mode_unchanged_by_passive_gluing':True,
            'selected_signed_chain_boundary_coefficient':coefficient})
    # A single circulation/orientation branch per piece gives an oriented
    # chain. Internal interfaces cancel precisely when adjacent signs AGREE:
    # chi_i epsilon_i + chi_j epsilon_j = epsilon_i(chi_i-chi_j).
    patterns=[]
    for signs in product((-1,1),repeat=len(tets)):
        if all(sum(v['sign']*signs[v['owner']] for v in entries)==0 for entries in internal.values()):patterns.append(signs)
    assert set(patterns)=={(-1,)*len(tets),(1,)*len(tets)}
    return {'internal_faces':len(internal),'outer_boundary_faces':sum(len(v)==1 for v in incidence.values()),
        'seam_free_piece_branch_patterns':[list(p) for p in patterns],
        'selected_pattern':selected,'selected_nonzero_internal_seams':sum(r['selected_signed_chain_boundary_coefficient']!=0 for r in rows),
        'interfaces':rows}

def main():
    geometry_path=BASE/'results/four_six_center_cones.json';flux_path=BASE/'results/mode_flux_charge.json'
    graw=geometry_path.read_bytes();fraw=flux_path.read_bytes();geometry=json.loads(graw);flux=json.loads(fraw)
    assert geometry['verification_passed'] and flux['verification_passed']
    belt_points={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
    proton_points={k:tuple(map(Q,v)) for k,v in geometry['proton_scaled_coordinates'].items()}
    belt=audit(geometry['belt_tetrahedra'],belt_points,flux['belt_face_signs'])
    proton=audit(geometry['proton_tetrahedra'],proton_points,[1]*4)
    checks={
        'both_carriers_have_six_shared_radial_faces':belt['internal_faces']==proton['internal_faces']==6,
        'every_shared_face_has_opposite_induced_boundary_orientations':all(r['left']['sign']==-r['right']['sign'] for a in (belt,proton) for r in a['interfaces']),
        'passive_face_transition_preserves_physical_mode_and_circulation':all(r['physical_mode_unchanged_by_passive_gluing'] for a in (belt,proton) for r in a['interfaces']),
        'ordinary_gluing_allows_only_uniform_piece_orientation_signs':len(belt['seam_free_piece_branch_patterns'])==len(proton['seam_free_piece_branch_patterns'])==2,
        'original_uniform_proton_has_no_internal_orientation_seam':proton['selected_nonzero_internal_seams']==0,
        'alternating_neutral_belt_has_six_signed_internal_seams':belt['selected_nonzero_internal_seams']==6,
        'each_alternating_interface_has_multiplicity_two':all(abs(r['selected_signed_chain_boundary_coefficient'])==2 for r in belt['interfaces']),
        'input_artifacts_unchanged':geometry_path.read_bytes()==graw and flux_path.read_bytes()==fraw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,'proton':proton,'belt':belt,
        'conclusion':'Ordinary shared-face identification reverses local chart orientation, not the physical mode. It does not force the neutral opposite-circulation pattern. With one signed orientation per tetrahedral piece, the alternating pattern leaves six internal signed seams of multiplicity two.',
        'what_survives':'The previously constructed neutral intrinsic operator still has its exact coherent return and 1836 support; this test does not invalidate that algebraic result.',
        'missing_rule':'An active branch-converting interface or additional interface state is required to select and consistently carry the opposite-circulation pattern; passive endpoint matching is insufficient.',
        'complex_linearity_obstruction':'Complex conjugation itself is anti-linear. A linear branch converter must be specified separately; replacing it by conjugation changes the scalar/phase contract.',
        'scope':'The signed-chain test assumes one orientation/circulation sign is extended uniformly over each constituent. The existing outer-mode construction did not specify those internal face modes; the residual seams expose that missing extension, rather than adding them silently.',
        'source_sha256':{'geometry':sha256(graw).hexdigest(),'flux':sha256(fraw).hexdigest()},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/face_gluing_circulation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('belt','proton')},indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
