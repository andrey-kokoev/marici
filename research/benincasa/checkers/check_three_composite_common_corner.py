#!/usr/bin/env python3
"""Common corner of two internal gluings: pairwise naturality versus chain sum."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_three_composite_internal_gluings import (s,rational,normalize,target_jac,parameters,source_chart,groups_for,boundary_coordinates,source_coefficient,gradient)
from check_paired_composite_corner_residues import sign,raw_bracket
from check_shared_facet_primitive_census import source_key,dimension
PRIOR='research/benincasa/results/three_composite_normalizations.json'
ATLAS='research/benincasa/results/three_composite_primitive_atlas.json'
GLUINGS='research/benincasa/results/three_composite_internal_gluings.json'
NORMALS=[(1,2,6,8),(1,2,3,5)]


def prepare(rows,atlas):
    a,A,_=parameters(rows[8]['target_runs'][0]);reference=A.subs({a[0]:0,a[4]:0});refvars=[a[j] for j in [1,2,3,5,6,7]]
    expected=((1,),(2,),(3,5),(6,8));assert source_key(reference)==expected and dimension(expected)==6
    cases=[]
    for history,identifier,outer_label in [(5,'merge-2-3',4),(8,'delete-7',4),(9,'merge-3-4',7)]:
        face=next(f for f in atlas[history]['faces'] if f['operation']['id']==identifier)
        embedding=rows[history]['superfunction_runs'][0]['matches'][0]
        C,variables,frame=source_chart(groups_for(embedding),face['operation']);t=variables[0]
        outer=s.Symbol(frame['scales'][str(outer_label)]);outer_index=variables.index(outer)
        corner=C.subs({t:0,outer:0});assert source_key(corner)==expected
        order=[0,outer_index] if history!=9 else [outer_index,0]
        parity,free=sign(order);coefficient,logdet=source_coefficient(C,variables,embedding)
        coefficient=rational(coefficient.subs(outer,0));assert coefficient!=0
        boundary=boundary_coordinates(reference,frame,variables);mapping=dict(zip(variables[1:],boundary));mapping[t]=s.Integer(0)
        assert mapping[outer]==0
        transition=[mapping[variables[j]] for j in free]
        L=s.diag(*[1/x for x in transition])*s.Matrix(transition).jacobian(refvars)*s.diag(*refvars)
        logdet6=rational(L.det(method='domain-ge'));assert logdet6!=0
        relative=rational(coefficient.subs(mapping,simultaneous=True)*parity*logdet6)
        assert relative==(1 if history==8 else -1)
        reconstructed=corner.subs(mapping,simultaneous=True).applyfunc(rational)
        assert all(rational(x)==0 for x in normalize(reconstructed,[0,1])-normalize(reference,[0,1]))
        cases.append({'history':history,'C':C,'variables':variables,'frame':frame,'outer':outer,'order':order,
            'parity':parity,'free':free,'coefficient':coefficient,'mapping':mapping,
            'transition':transition,'logdet6':logdet6,'relative':relative,
            'logdet':logdet})
    assert sum(case['relative'] for case in cases)==-1
    return a,reference,refvars,cases


def run(rows,a,reference,refvars,cases,shift):
    Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    _,_,original=parameters(rows[8]['target_runs'][shift]);original[a[0]]=original[a[4]]=0
    Cref=reference.subs(original);N=normalize(Cref*Z,[0,1]);coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    Jr,actual=target_jac(Cref*Z,[reference.diff(z).subs(original)*Z for z in refvars],[0,1]);assert actual==coords
    Fref=Jr*s.diag(*[original[z] for z in refvars]);assert Fref.rank()==6
    selected=next(I for I in itertools.combinations(range(8),6) if Fref[list(I),:].det()!=0)
    reference_density=s.factor(1/Fref[list(selected),:].det())
    grads=s.Matrix.vstack(*[gradient(N,Z,q,coords) for q in NORMALS]);assert grads.rank()==2
    assert all(s.Matrix.vstack(N,*[Z[k-1,:] for k in quad]).det()==0 for quad in NORMALS)
    # The six active source vectors furnish an actual unique boundary fiber.
    support=[0,1,2,4,5,7];L=s.zeros(6,8);left=Z[support,:].inv()
    for j,label in enumerate(support):L[:,label]=left[:,j]
    assert L*Z==s.eye(6) and all(rational(x)==0 for x in reference*Z*L-reference)
    routes=[];density={};reverse={}
    for case in cases:
        history,C,variables=case['history'],case['C'],case['variables'];order=case['order'];free=case['free']
        values={z:rational(x.subs(original)) for z,x in case['mapping'].items()}
        assert all(values[variables[j]]>0 for j in free)
        Cp=C.subs(values);assert normalize(Cp*Z,[0,1])==N
        assert all(Cp[:,list(p)].det()>=0 for p in itertools.combinations(range(8),2))
        J,actual=target_jac(Cp*Z,[C.diff(z).subs(values)*Z for z in variables],[0,1]);assert actual==coords and J.det()!=0
        F=J[:,free]*s.diag(*[values[variables[j]] for j in free]);assert F.rank()==6
        B=grads*J;assert all(B[i,j]==0 for i in range(2) for j in free)
        # Source coordinate order must follow the target normal order. Swapping
        # normal rows without also swapping deleted coordinates would falsely
        # conceal residue anticommutation in a determinant ratio.
        normalminor=B[:,order];assert normalminor.det()!=0
        assert normalminor[0,1]==normalminor[1,0]==0
        pullbacks=[]
        for quad,e in zip(NORMALS,order):
            p=raw_bracket(C,Z,quad);assert p!=0 and p.subs(variables[e],0)==0
            pullbacks.append({'quad':list(quad),'source_deleted_coordinate':str(variables[e]),'raw_pullback':str(p)})
        coefficient=rational(case['coefficient'].subs(values));prod=s.prod(values[variables[j]] for j in free)
        det=s.factor(F[list(selected),:].det());source=s.factor(coefficient*case['parity']/det)
        full=s.Matrix.vstack(B,J[list(selected),:]);top=s.factor(coefficient*normalminor.det()/(prod*full.det()));assert top==source
        remaining=[j for j in range(8) if j!=order[0]]
        D7=s.Matrix.vstack(B[1,remaining],J[list(selected),remaining]);assert D7.det()!=0
        middle=s.factor(coefficient*(-1)**order[0]*B[1,order[1]]/(prod*D7.det()));assert middle==source
        # Reverse both the common target normal order and source deletion order.
        reverse_order=list(reversed(order));reverse_parity,_=sign(reverse_order)
        Brev=s.Matrix.vstack(B[1,:],B[0,:]);revfull=s.Matrix.vstack(Brev,J[list(selected),:])
        revsource=s.factor(coefficient*reverse_parity/det)
        revtop=s.factor(coefficient*Brev[:,reverse_order].det()/(prod*revfull.det()));assert revsource==revtop==-source
        remrev=[j for j in range(8) if j!=reverse_order[0]]
        D7rev=s.Matrix.vstack(Brev[1,remrev],J[list(selected),remrev])
        revmiddle=s.factor(coefficient*(-1)**reverse_order[0]*Brev[1,reverse_order[1]]/(prod*D7rev.det()));assert revmiddle==revsource
        assert source==case['relative']*reference_density
        density[history]=source;reverse[history]=revsource
        routes.append({'history_index':history,'boundary_parameters':{str(z):str(x) for z,x in values.items()},
            'source_deleted_coordinate_order':[str(variables[j]) for j in order],'source_deletion_parity':case['parity'],
            'generic_intrinsic_log_coefficient':str(coefficient),'source_normal_pullbacks':pullbacks,
            'source_corner_residue_then_pushforward':str(source),'first_source_residue_pushforward_then_second_target_residue':str(middle),
            'top_pushforward_then_two_common_target_residues':str(top),
            'reversed_normal_and_source_deletion_order_density':str(revsource),'source_to_common_reference_ratio':str(case['relative'])})
    assert density[5]+density[8]==0 and density[8]+density[9]==0
    assert reverse[8]+reverse[9]==0
    triple=s.factor(sum(density.values()));assert triple==-reference_density and triple!=0
    # Fitting the middle coefficient to2 cancels this corner alone but breaks
    # both already fixed internal facet gluings; retain it as a rejected shortcut.
    fitted=s.factor(density[5]+2*density[8]+density[9]);assert fitted==0
    breaks=s.factor(density[5]+2*density[8]);assert breaks!=0
    return {'positive_Z_moment_shift':shift,'target_normal_order':[list(q) for q in NORMALS],
        'common_source_support':[j+1 for j in support],'common_source_classes':[[1],[2],[3,5],[6,8]],
        'boundary_target_tangent_rank':6,'all_full_target_germ_ranks':8,'common_target_coordinate_indices':list(selected),
        'reference_parameter_order':[str(z) for z in refvars],'reference_log_jacobian_density':str(reference_density),
        'routes':routes,'Y1268_first_pair_H5_A8_sum':'0','Y1235_first_pair_A8_H9_sum':'0',
        'canonical_order_pair_A8_H9_sum':'0','three_composite_canonical_order_sum':str(triple),
        'three_composite_sum_over_reference':'-1','orientation_reversal_pair_residual':str(-density[5]+density[8]),
        'fitted_middle_weight2_corner_sum':str(fitted),'fitted_middle_weight2_internal_pair_residual':str(breaks),
        'residual_disposition':'nonzero selected three-composite corner sum, not weighted-nine-form or complete BCFW refutation'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());atlas=json.loads((ROOT/ATLAS).read_text());gluings=json.loads((ROOT/GLUINGS).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (atlas,'research/benincasa/checkers/check_three_composite_primitive_atlas.py'),
        (gluings,'research/benincasa/checkers/check_three_composite_internal_gluings.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};ar={r['history_index']:r for r in atlas['rows']}
    a,reference,refvars,cases=prepare(rows,ar);runs=[run(rows,a,reference,refvars,cases,shift) for shift in (0,1)]
    witness=[{'history_index':c['history'],'boundary_to_reference_log_determinant':str(c['logdet6']),
        'canonical_deletion_parity':c['parity'],'intrinsic_coefficient':str(c['coefficient']),
        'coefficient_on_common_six_dlog_generator':str(c['relative'])} for c in cases]
    checks={'actual_common_source_corner_key_and_symbolic_frame_reconstruction':True,
        'three_symbolic_reference_log_transitions_and_ordered_signs':True,'two_positive_rank6_common_target_points_and_six_regular_full_germs':True,
        'twelve_three_route_comparisons_in_both_normal_orders':True,'pairwise_gluing_boundary_naturality_sums_zero':True,
        'two_nonzero_selected_three_composite_sums_retained':True,'orientation_and_fitted_middle_coefficient_hostiles_rejected':True,
        'six_active_external_vectors_give_boundary_inverse':True}
    paths=[PRIOR,ATLAS,GLUINGS,'research/benincasa/checkers/check_three_composite_primitive_atlas.py',
        'research/benincasa/checkers/check_three_composite_internal_gluings.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.three-composite-common-corner.v1','histories':[5,8,9],
        'source_witness':{'reference':'A_history8_alpha1=alpha5=0','reference_order':[str(z) for z in refvars],
            'ordered_normal_reference_coefficients':witness,'symbolic_three_composite_source_coefficient_sum':'-1'},
        'runs':runs,'checks':checks,'passed':True,
        'disposition':'pairwise_internal_gluing_naturality_holds_but_selected_three_composite_corner_sum_is_nonzero',
        'claim_boundary':'One actual positive common corner, fixed intrinsic orientations and target normal order Y1268_then_Y1235. A nonzero unit-weight sum of these three forms is retained; it does not refute the unconstructed weighted-nine-form comparison or complete historical BCFW chain.',
        'next_action':'Identify the possible missing fourth six-active-label top cell on support {1,2,3,5,6,8} from the source seed/history matcher, without choosing its sign from the residual. Test whether transported history6 supplies it; derive its intrinsic orientation and common-corner residues. Keep any transported representative distinct from an untransported K0 admission.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/three_composite_common_corner.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'relative_corner_coefficients':[c['relative'].__str__() for c in cases],
        'three_cell_sums':[r['three_composite_canonical_order_sum'] for r in runs]},indent=2))


if __name__=='__main__':main()
