#!/usr/bin/env python3
"""Two actual invariant internal source gluings, not equal-divisor pairing."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_three_composite_primitive_atlas import (s,rational,normalize,target_jac,parameters,source_chart,groups_for,extract,gradient)
PRIOR='research/benincasa/results/three_composite_normalizations.json'
ATLAS='research/benincasa/results/three_composite_primitive_atlas.json'
PREVIOUS='research/benincasa/results/shared_internal_composite_facet.json'


def boundary_coordinates(R,frame,coordinates):
    cut=frame['cut_label']
    def signed(label):return (-1 if label<cut else 1)*R[:,label-1]
    W=s.Matrix.hstack(signed(frame['first_anchor']),signed(frame['last_anchor']));assert W.det()!=0
    B=(W.inv()*R).applyfunc(rational)
    def col(label):return (-1 if label<cut else 1)*B[:,label-1]
    classes=frame['cyclic_classes'];slopes=[]
    for group in classes[1:-1]:
        representative=next(x for x in group if any(rational(v)!=0 for v in col(x)))
        c=col(representative);assert c[1]!=0;slopes.append(rational(c[0]/c[1]))
    slopes.append(s.Integer(0));mapping={s.Symbol(name):rational(slopes[i]-slopes[i+1]) for i,name in enumerate(frame['ordered_gaps'])}
    for label,name in frame['scales'].items():
        label=int(label);group=next(i for i,g in enumerate(classes) if label in g)
        mapping[s.Symbol(name)]=rational(col(label)[0] if group==0 else col(label)[1])
    return [mapping[z] for z in coordinates[1:]]


def source_coefficient(C,coordinates,embedding):
    alpha,_,_=extract(C,embedding)
    logJ=s.diag(*[1/x for x in alpha])*s.Matrix(alpha).jacobian(coordinates)*s.diag(*coordinates)
    det=rational(logJ.det(method='domain-ge'));t=coordinates[0]
    num,den=s.fraction(det);assert den.subs(t,0)!=0
    coefficient=rational(det.subs(t,0));assert coefficient!=0
    return coefficient,det


def measure(C,coordinates,values,Z,selected=None):
    t=coordinates[0];C0=C.subs(t,0);Cp=C0.subs(values)
    assert all(Cp[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
    J,coords=target_jac(Cp*Z,[C.diff(z).subs(t,0).subs(values)*Z for z in coordinates],[0,1]);assert J.det()!=0
    F=J[:,1:]*s.diag(*[values[z] for z in coordinates[1:]]);assert F.rank()==7
    if selected is None:selected=next(I for I in itertools.combinations(range(8),7) if F[list(I),:].det()!=0)
    return normalize(Cp*Z,[0,1]),J,F,coords,list(selected)


def pair(rows,atlasrows,donor,donorid,receiver,receiverid,quad):
    Dface=next(f for f in atlasrows[donor]['faces'] if f['operation']['id']==donorid)
    Rface=next(f for f in atlasrows[receiver]['faces'] if f['operation']['id']==receiverid)
    assert Dface['source_boundary_class_key']==Rface['source_boundary_class_key']
    de=rows[donor]['superfunction_runs'][0]['matches'][0];re=rows[receiver]['superfunction_runs'][0]['matches'][0]
    D,dcoords,df=source_chart(groups_for(de),Dface['operation']);R,rcoords,rf=source_chart(groups_for(re),Rface['operation'])
    td,tr=dcoords[0],rcoords[0];D0=D.subs(td,0);R0=R.subs(tr,0)
    transition=boundary_coordinates(D0,rf,rcoords);sub=dict(zip(rcoords[1:],transition))
    reconstructed=R0.subs(sub,simultaneous=True).applyfunc(rational)
    pd=next(p for p in itertools.combinations(range(8),2) if rational(D0[:,list(p)].det())!=0)
    assert all(rational(x)==0 for x in normalize(reconstructed,list(pd))-normalize(D0,list(pd)))
    back=boundary_coordinates(reconstructed,df,dcoords)
    assert all(rational(x-y)==0 for x,y in zip(back,dcoords[1:]))
    logT=s.diag(*[1/x for x in transition])*s.Matrix(transition).jacobian(dcoords[1:])*s.diag(*dcoords[1:])
    determinant=rational(logT.det(method='domain-ge'));assert determinant!=0
    cd,ld=source_coefficient(D,dcoords,de);cr,lr=source_coefficient(R,rcoords,re)
    paired=rational(cd+cr.subs(sub,simultaneous=True)*determinant);assert paired==0
    assert rational(-cd+cr.subs(sub,simultaneous=True)*determinant)!=0
    runs=[]
    for shift,numbers in [(0,[2,3,5,7,11,13,17]),(1,[3,5,7,11,13,17,19])]:
        dv=dict(zip(dcoords[1:],[s.Integer(x) for x in numbers]));rv={z:rational(x.subs(dv)) for z,x in zip(rcoords[1:],transition)}
        assert all(x>0 for x in rv.values())
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        N,Jd,Fd,coords,selected=measure(D,dcoords,dv,Z);Nr,Jr,Fr,_,_=measure(R,rcoords,rv,Z,selected)
        assert N==Nr and Fr*logT.subs(dv)==Fd
        assert s.Matrix.vstack(N,*[Z[k-1,:] for k in quad]).det()==0
        grad=gradient(N,Z,quad,coords);routes=[];densities=[]
        for history,C,vars,values,J,F,c in [(donor,D,dcoords,dv,Jd,Fd,cd),(receiver,R,rcoords,rv,Jr,Fr,cr)]:
            coefficient=rational(c.subs(values));det=s.factor(F[selected,:].det());source=s.factor(coefficient/det)
            normals=grad*J;assert normals[0]!=0 and all(normals[j]==0 for j in range(1,8))
            full=s.Matrix.vstack(normals,J[selected,:]);assert full.det()!=0
            target=s.factor(coefficient*normals[0]/(s.prod(values[z] for z in vars[1:])*full.det()));assert source==target
            densities.append(source);routes.append({'history_index':history,'boundary_parameters':{str(z):str(x) for z,x in values.items()},
                'intrinsic_boundary_coefficient':str(coefficient),'source_residue_then_pushforward':str(source),
                'top_pushforward_then_common_bracket_residue':str(target),'boundary_log_jacobian':str(det)})
        assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
        # Reproduce orientation coefficients in each atlas at its own named point
        # by the generic circuit, not by reusing them at a different target point.
        for face,c in [(Dface,cd),(Rface,cr)]:
            fixture={s.Symbol(z):s.Rational(x) for z,x in face['positive_source_fixture'].items()}
            assert str(rational(c.subs(fixture)))==face['runs'][shift]['source_boundary_coefficient']
        runs.append({'positive_Z_moment_shift':shift,'common_target_coordinate_indices':selected,
            'source_log_transition_determinant':str(rational(determinant.subs(dv))),
            'common_target_point':[str(N[i,j]) for i,j in coords],'routes':routes,
            'paired_seven_form_sum':'0','orientation_reversal_residual':str(hostile)})
    return {'histories':[donor,receiver],'primitive_ids':[donorid,receiverid],'target_internal_bracket':list(quad),
        'common_source_boundary_key':Dface['source_boundary_class_key'],
        'donor_boundary_order':[str(z) for z in dcoords[1:]],'receiver_boundary_order':[str(z) for z in rcoords[1:]],
        'symbolic_boundary_transition':[str(x) for x in transition],'symbolic_inverse_transition_identity':True,
        'symbolic_log_transition_determinant':str(determinant),
        'intrinsic_donor_log_transition':str(ld),'intrinsic_receiver_log_transition':str(lr),
        'intrinsic_boundary_coefficients':[str(cd),str(cr)],'symbolic_paired_source_seven_form_coefficient':'0',
        'runs':runs},(D,dcoords,df,cd,R,rcoords,rf,cr)


def previous_regression(rows,previous,context):
    D,dcoords,df,cd,R,rcoords,rf,cr=context;out=[]
    a,A,_=parameters(rows[8]['target_runs'][0])
    for old in previous['runs']:
        shift=old['positive_Z_moment_shift'];_,_,oldvalues=parameters(rows[8]['target_runs'][shift]);oldvalues[a[0]]=0
        C=A.subs(oldvalues);Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        dv=dict(zip(dcoords[1:],boundary_coordinates(C,df,dcoords)));rv=dict(zip(rcoords[1:],boundary_coordinates(C,rf,rcoords)))
        assert all(x>0 for x in list(dv.values())+list(rv.values()))
        selected=old['selected_common_target_coordinate_indices'];original={r['history_index']:r for r in old['routes']}
        densities=[]
        for history,chart,vars,values,c in [(8,D,dcoords,dv,cd),(9,R,rcoords,rv,cr)]:
            _,_,F,_,_=measure(chart,vars,values,Z,selected)
            density=s.factor(c.subs(values)/F[selected,:].det())
            assert str(density)==original[history]['source_residue_then_pushforward'];densities.append(str(density))
        out.append({'positive_Z_moment_shift':shift,'target_coordinate_frame_preserved':True,'original_history8_and9_densities':densities,'passed':True})
    return out


def main():
    prior=json.loads((ROOT/PRIOR).read_text());atlas=json.loads((ROOT/ATLAS).read_text());previous=json.loads((ROOT/PREVIOUS).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (atlas,'research/benincasa/checkers/check_three_composite_primitive_atlas.py'),
        (previous,'research/benincasa/checkers/check_shared_internal_composite_facet.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};ar={r['history_index']:r for r in atlas['rows']}
    # Exhaust all equal source keys among distinct parents; physical labels alone
    # do not authorize a gluing candidate.
    actual=[]
    for first,second in itertools.combinations(ar.values(),2):
        for f in first['faces']:
            for g in second['faces']:
                if f['source_boundary_class_key']==g['source_boundary_class_key']:actual.append((first['history_index'],f['operation']['id'],second['history_index'],g['operation']['id']))
    expected=[(5,'merge-2-3',8,'delete-7'),(8,'delete-4',9,'merge-3-4')];assert actual==expected
    pair1,_=pair(rows,ar,*expected[0],(1,2,6,8));pair2,context=pair(rows,ar,*expected[1],(1,2,3,5))
    regressions=previous_regression(rows,previous,context)
    checks={'exactly_two_equal_invariant_source_boundary_keys':True,'two_symbolic_positive_chart_inverse_transitions':True,
        'derived_generic_intrinsic_source_log_coefficients_and_boundary_log_jacobians':True,
        'two_symbolic_paired_source_seven_form_identities':True,'four_same_positive_source_target_point_comparisons':True,
        'eight_common_normal_local_residue_squares_four_paired_sums_zero':True,
        'four_orientation_reversal_residuals_nonzero':True,'four_old_Y1235_target_density_regressions_preserved':True}
    paths=[PRIOR,ATLAS,PREVIOUS,'research/benincasa/checkers/check_three_composite_primitive_atlas.py',
        'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.three-composite-internal-gluings.v1','pairs':[pair1,pair2],
        'previous_Y1235_regressions':regressions,'checks':checks,'passed':True,
        'disposition':'both_actual_internal_source_gluings_have_symbolic_unweighted_orientation_cancellation_and_local_target_squares',
        'claim_boundary':'Two invariant common source facets among three matched intrinsic cells, generic source transition identities and local target seven-form cancellations at named positive points/two fixed Z. No historical full-chain orientation, weighted sector map or supercomponent boundary extraction theorem.',
        'next_action':'Test the common corner of these two internal gluings: A_history8 zero columns4_and7 (alpha1=alpha5=0), with the corresponding H5/H9 boundary closures. Fix common target normal order Y1268 then Y1235, derive iterated deletion/transition signs for all three routes, retain their exact sums and distinguish pairwise gluing naturality from any unsupported three-cell or weighted cancellation claim.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/three_composite_internal_gluings.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'paired_sums':[[r['paired_seven_form_sum'] for r in p['runs']] for p in out['pairs']]},indent=2))


if __name__=='__main__':main()
