#!/usr/bin/env python3
"""Intrinsic ordered F-chart corner calculation; sign derived, not fitted."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_common_corner import prepare, NORMALS
from check_three_composite_internal_gluings import s, rational, normalize, target_jac, parameters, gradient
from check_paired_composite_corner_residues import sign, raw_bracket
ROOT=Path(__file__).resolve().parents[3]
PRIOR='research/benincasa/results/three_composite_normalizations.json'
ATLAS='research/benincasa/results/three_composite_primitive_atlas.json'
CORNER='research/benincasa/results/three_composite_common_corner.json'
MATCH='research/benincasa/results/history6_seed_admission.json'


def main():
    prior=json.loads((ROOT/PRIOR).read_text()); atlas=json.loads((ROOT/ATLAS).read_text())
    previous=json.loads((ROOT/CORNER).read_text()); admission=json.loads((ROOT/MATCH).read_text())
    assert admission['passed'] and all(f['distinct_matched_cell_keys']==1 for f in admission['fixtures'])
    assert admission['owning_matcher_sha256']==sha256((ROOT/admission['owning_matcher']).read_bytes()).hexdigest()
    for receipt in (prior,atlas,previous):
        for p,h in receipt['source_sha256'].items():
            assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    rows={r['history_index']:r for r in prior['rows']}; ar={r['history_index']:r for r in atlas['rows']}
    a,reference,refvars,_=prepare(rows,ar)
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    F=s.Matrix([[1,b1+b2+b3+b4,(b2+b3+b4)*b5,(b3+b4)*b6,b4*b7,0],
                [0,1,b5,b6,b7,b8]])
    support=[0,1,2,4,5,7];C=s.zeros(2,8)
    for j,k in enumerate(support):C[:,k]=F[:,j]
    Nref=normalize(reference,[0,1]);v=[Nref[1,k] for k in support[2:]]
    slopes=[-Nref[0,k]/Nref[1,k] for k in support[2:]]
    inverse=[slopes[0]]+[slopes[j]-slopes[j-1] for j in range(1,4)]+v
    mapping={z:rational(x) for z,x in zip(b,inverse)}
    assert mapping[b2]==mapping[b4]==0
    assert all(rational(x)==0 for x in normalize(C.subs(mapping,simultaneous=True),[0,1])-Nref)
    order=[1,3];parity,free=sign(order)
    transition=[mapping[b[j]] for j in free]
    logJ=s.diag(*[1/x for x in transition])*s.Matrix(transition).jacobian(refvars)*s.diag(*refvars)
    determinant=rational(logJ.det(method='domain-ge'))
    relative=rational(parity*determinant)
    runs=[]
    for shift,old in enumerate(previous['runs']):
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        _,_,sample=parameters(rows[8]['target_runs'][shift]);sample[a[0]]=sample[a[4]]=0
        values={z:rational(x.subs(sample)) for z,x in mapping.items()}
        assert all(values[b[j]]>0 for j in free)
        Cp=C.subs(values);Y=Cp*Z;N=normalize(Y,[0,1])
        assert N==normalize(reference.subs(sample)*Z,[0,1])
        assert all(Cp[:,list(I)].det()>=0 for I in itertools.combinations(range(8),2))
        J,coords=target_jac(Y,[C.diff(z).subs(values)*Z for z in b],[0,1])
        assert J.det()!=0
        grads=s.Matrix.vstack(*[gradient(N,Z,q,coords) for q in NORMALS]);B=grads*J
        assert all(B[i,j]==0 for i in range(2) for j in free)
        assert B[:,order].det()!=0 and B[0,3]==B[1,1]==0
        pulls=[]
        for quad,e in zip(NORMALS,order):
            p=raw_bracket(C,Z,quad)
            assert p!=0 and p.subs(b[e],0)==0
            pulls.append(str(p))
        selected=old['common_target_coordinate_indices']
        tangent=J[:,free]*s.diag(*[values[b[j]] for j in free]);assert tangent.rank()==6
        density=s.factor(parity/tangent[selected,:].det())
        prod=s.prod(values[b[j]] for j in free)
        full=s.Matrix.vstack(B,J[selected,:])
        target=s.factor(B[:,order].det()/(prod*full.det()));assert target==density
        remaining=[j for j in range(8) if j!=order[0]]
        middle=s.factor((-1)**order[0]*B[1,order[1]]/(prod*s.Matrix.vstack(B[1,remaining],J[selected,remaining]).det()))
        assert middle==density
        assert density==relative*s.Rational(old['reference_log_jacobian_density'])
        total=s.factor(density+s.Rational(old['three_composite_canonical_order_sum']))
        assert total==(relative-1)*s.Rational(old['reference_log_jacobian_density'])
        assert -2*density!=0
        runs.append({'positive_Z_moment_shift':shift,'parameters':{str(z):str(x) for z,x in values.items()},
            'target_normal_order':[list(q) for q in NORMALS],'raw_normal_pullbacks':pulls,
            'ambient_target_rank':8,'corner_tangent_rank':6,
            'source_corner_then_pushforward':str(density),'top_pushforward_then_target_residues':str(target),
            'first_source_residue_then_target_residue':str(middle),
            'four_transported_cell_corner_sum':str(total),'orientation_flip_defect':str(-2*density)})
    paths=[PRIOR,ATLAS,CORNER,MATCH,'research/benincasa/checkers/check_first_simple_root_boundary_localization.py',
           'research/benincasa/checkers/check_history6_seed_admission.py','research/benincasa/checkers/check_three_composite_common_corner.py',
           admission['owning_matcher']]
    out={'schema':'marici.benincasa.history6-common-corner.v1','history_index':6,'seed':'F',
         'support':[j+1 for j in support],'rotation':0,'source_orientation':'dlog b1 wedge ... wedge dlog b8',
         'source_chart':[[str(x) for x in row] for row in C.tolist()],
         'corner_equations':['b2=0','b4=0'],'boundary_to_reference':{str(z):str(x) for z,x in mapping.items()},
         'deletion_parity':parity,'six_log_transition_determinant':str(determinant),
         'derived_reference_coefficient':str(relative),'runs':runs,'passed':True,
         'scope':'Intrinsic local transported F chart, frozen increasing eight-dlog convention; no global BCFW sign anchor or untransported K0 admission.',
         'next_action':'Derive the history6 endpoint-switch coefficient and its boundary/component extraction before attempting the weighted nine-form map. Attach global BCFW orientation/covering evidence independently.',
         'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
         'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_common_corner.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'passed':True,'relative':str(relative),'runs':runs},indent=2))

if __name__=='__main__':main()
