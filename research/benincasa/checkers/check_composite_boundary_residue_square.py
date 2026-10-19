#!/usr/bin/env python3
"""History 5 alpha2=0: exact local differential residue/pushforward square.

This constructs one bosonized target boundary map, not its supercomponent map
or the global oriented source chain.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as s
from check_composite_root_normalization import normalize,target_jac,derivative

PRIOR='research/benincasa/results/three_composite_normalizations.json'
QUAD=(1,2,3,4)


def raw_bracket(C,Z,quad):
    # Cauchy-Binet for det([CZ;Z_quad]), with fixed ordered appended rows.
    return s.factor(sum(C[:,[i,j]].det()*s.Matrix.vstack(Z[i,:],Z[j,:],*[Z[k-1,:] for k in quad]).det()
        for i,j in itertools.combinations(range(8),2) if i+1 not in quad and j+1 not in quad))


def boundary_run(sample):
    a=s.symbols('a1:9');e=1;C=s.Matrix([[s.sympify(v) for v in row] for row in sample['source_chart_matrix']])
    Z=s.Matrix([[s.Integer(j+sample['positive_Z_moment_shift'])**k for k in range(6)] for j in range(1,9)])
    vals={v:s.Integer(sample['source_parameters'][str(v)]) for v in a};v=vals|{a[e]:s.Integer(0)}
    Ysym=C*Z;raw=raw_bracket(C,Z,QUAD);pivotdet=s.factor(Ysym[:,[0,1]].det())
    assert raw.subs(a[e],0)==0 and raw!=0
    factor=s.factor(raw/a[e]);assert not factor.has(a[e]) and factor.subs(v)!=0
    assert pivotdet.subs(v)!=0
    b=s.factor(raw/pivotdet)
    # Transverse source normal slope in the normalized target bracket.
    slope=s.factor(s.diff(raw,a[e]).subs(v)/pivotdet.subs(v));assert slope!=0
    Y=Ysym.subs(v);N=normalize(Y,[0,1])
    ordinary_derivs=[C.diff(x).subs(v)*Z for x in a]
    Jall,coords=target_jac(Y,ordinary_derivs,[0,1])
    free=[i for i in range(8) if i!=e]
    Jfree=Jall[:,free]*s.diag(*[vals[a[i]] for i in free])
    assert Jfree.rank()==7
    chosen=next(I for I in itertools.combinations(range(8),7) if Jfree[list(I),:].det()!=0)
    determinant=s.factor(Jfree[list(chosen),:].det());assert determinant!=0
    def target_bracket(T):return s.Matrix.vstack(T,*[Z[i-1,:] for i in QUAD]).det()
    assert target_bracket(N)==0
    # Differentiate target bracket in its eight free coordinate directions.
    gradient=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        gradient.append(s.factor(s.Matrix.vstack(E[0,:],N[1,:],*[Z[k-1,:] for k in QUAD]).det()+
            s.Matrix.vstack(N[0,:],E[1,:],*[Z[k-1,:] for k in QUAD]).det()))
    grad=s.Matrix(1,8,gradient)
    normals=grad*Jall
    assert normals[0,e]==slope and all(normals[0,i]==0 for i in free)
    # Full target coordinates ordered (b, chosen seven free entries).
    D=s.Matrix.vstack(normals,Jall[list(chosen),:]);detD=s.factor(D.det());assert detD!=0
    # Route A: delete alpha2 from ordered source eight-dlog, sign -1.
    sign=(-1)**e
    residue_push=s.factor(sign/determinant)
    # Route B: top density in db wedge dx_selected is 1/(prod(alpha)*det D).
    # b=alpha2*slope+O(alpha2^2), so its b-residue is the following limit.
    pushed_residue=s.factor(slope/(s.prod(vals[a[i]] for i in free)*detD))
    assert pushed_residue==residue_push
    assert s.factor(-residue_push-pushed_residue)!=0
    # Local rank/image screen of this chart's eight coordinate faces.
    faces=[]
    for index,x in enumerate(a):
        w=vals|{x:s.Integer(0)};YY=Ysym.subs(w)
        ds=[C.diff(z).subs(w)*Z for j,z in enumerate(a) if j!=index]
        JJ,_=target_jac(YY,ds,[0,1]);rank=JJ.rank()
        vanishing=[]
        for quad in itertools.combinations(range(1,9),4):
            p=raw_bracket(C,Z,quad)
            if p.subs(x,0)==0:vanishing.append(list(quad))
        physical=[]
        for quad in vanishing:
            q=set(quad)
            if any({i,(i%8)+1,j,(j%8)+1}==q and len({i,(i%8)+1,j,(j%8)+1})==4
                for i in range(1,9) for j in range(i+1,9)):physical.append(quad)
        faces.append({'alpha':index+1,'target_tangent_rank':rank,'identically_vanishing_four_brackets':vanishing,
            'physical_adjacent_pair_brackets':physical,'disposition':('contracted_rank_below_seven' if rank<7 else
                'physical_divisor_local_branch' if physical else 'rank_seven_nonphysical_or_nonlinear_image')})
    return {'positive_Z_moment_shift':sample['positive_Z_moment_shift'],
        'source_boundary_parameters':{str(z):str(w) for z,w in v.items()},
        'raw_Y1234_bracket':str(raw),'raw_bracket_alpha2_quotient':str(factor),
        'normalized_target_bracket':str(b),'target_pivot':[1,2],
        'selected_target_coordinate_indices':list(chosen),
        'selected_target_coordinates':[[coords[i][0]+1,coords[i][1]+1] for i in chosen],
        'target_boundary_log_jacobian':str(determinant),'transverse_normal_slope':str(slope),
        'full_ordinary_normal_chart_jacobian':str(detD),
        'source_residue_sign':sign,'source_residue_then_pushforward':str(residue_push),
        'top_pushforward_then_target_residue':str(pushed_residue),
        'orientation_failure_residual':str(-residue_push-pushed_residue),
        'coordinate_face_screen':faces}


def main():
    prior=json.loads((ROOT/PRIOR).read_text())
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    producer='research/benincasa/checkers/check_three_composite_normalizations.py'
    assert sha256((ROOT/producer).read_bytes()).hexdigest()==prior['checker_sha256']
    row=next(r for r in prior['rows'] if r['history_index']==5)
    runs=[boundary_run(sample) for sample in row['target_runs']]
    checks={'symbolic_alpha2_divisor_identified_both_Z':True,'two_rank_seven_target_tangent_maps':True,
        'two_nonzero_transverse_normals':True,'both_oriented_residue_routes_equal':True,
        'orientation_failure_detected_both_samples':True,'eight_coordinate_faces_screened_each_sample':True}
    paths=[PRIOR,producer,'research/benincasa/checkers/check_composite_root_normalization.py',
        'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex']
    out={'schema':'marici.benincasa.composite-boundary-residue-square.v1','root':[1,2],'history_index':5,
        'source_boundary':'alpha2=0 in the fixed twisted H chart','target_boundary':'normalized <Y1234>=0',
        'runs':runs,'checks':checks,'passed':True,
        'disposition':'constructed_local_bosonized_differential_residue_square_for_one_composite_boundary',
        'scope':'Same source chart, fixed intrinsic orientation and positive external Z samples. Symbolic source divisor relation for each Z, exact differential/algebraic residue limits on regular boundary opens. No global degree, all-atlas facet enumeration, BCFW-chain orientation anchor or supercomponent boundary square.',
        'next_action':'Extend the differential boundary screen and residue squares across all three composite charts, retaining contracted/nonphysical faces; obtain or recover global incidence/transition witnesses separately.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/composite_boundary_residue_square.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'disposition':out['disposition'],
        'face_screen':runs[0]['coordinate_face_screen'],'orientation_sign':runs[0]['source_residue_sign']},indent=2))


if __name__=='__main__':main()
