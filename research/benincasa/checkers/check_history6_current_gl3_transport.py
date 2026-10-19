#!/usr/bin/env python3
"""Triple normal-current GL3 covariance, marked arrangement and integral tubes."""
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s, normalize, berezin_pair
ROOT=Path(__file__).resolve().parents[3]
LATTICE='research/benincasa/results/history6_current_projective_lattice.json'
CHART='research/benincasa/results/history6_common_corner.json'


def main():
    prior=json.loads((ROOT/LATTICE).read_text());chart=json.loads((ROOT/CHART).read_text())
    for receipt in (prior,chart):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_projective_lattice.py').read_bytes()).hexdigest()
    r,z,R,S,u,v,t,k=s.symbols('r s R S u v T rho')
    basis=[1/(r*z),1/(r*(r+z)),1/(r*(z+1)),1/((r+z)*(z+1))]
    F=[basis[1]+basis[3],basis[0]-basis[1]-basis[3]]
    pairing=s.Matrix([item['basis_periods'] for item in prior['cycles']])
    periods=s.Matrix(prior['split_period_matrix'])
    def res(q,word):
        for normal in word:q=s.factor(s.residue(q,normal,0))
        return q
    # Universal projective Jacobian, with a genuine normal-frame matrix.
    entries=s.symbols('a0:9');general=s.Matrix(3,3,entries);image=general*s.Matrix([r,z,1]);scale=image[2]
    forward=s.Matrix([image[0]/scale,image[1]/scale])
    assert s.factor(forward.jacobian([r,z]).det()-general.det()/scale**3)==0
    lines=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1]])
    vertices=[s.Matrix(q) for q in ([0,0,1],[1,0,0],[0,1,0],[0,-1,1],[1,-1,0],[1,-1,1])]
    b=s.symbols('b1:9');C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])[:,[0,1,2,4,5,7]]
    D=normalize(C,[0,1]).applyfunc(s.factor);values=dict(zip(b,map(s.Integer,[2,0,0,0,5,7,11,13])))
    M=s.diag(2,3,5,7);Dn=D.subs(values);external=M*(-Dn[:,2:].T).row_join(s.eye(4));G=D*external.T
    coords=[(i,j) for i in range(2) for j in range(4)]
    J=s.Matrix([[s.diff(G[i,j],q).subs(values) for q in b] for i,j in coords]);assert J.det()!=0
    numerator=berezin_pair(Dn[:,[0,5]]);assert numerator==s.Integer(13)**4
    runs=[]
    for A in (s.Matrix([[2,1,0],[0,3,1],[1,0,2]]),s.Matrix([[0,1,0],[1,0,0],[0,0,1]]),
              s.Matrix([[1,0,0],[0,2,0],[1,1,3]]),2*s.eye(3)):
        det=A.det();inv=A.inv();image=A*s.Matrix([r,z,1]);h=image[2]
        mapped={R:s.factor(image[0]/h),S:s.factor(image[1]/h)}
        original=inv*s.Matrix([R,S,1]);back={r:s.factor(original[0]/original[2]),z:s.factor(original[1]/original[2])}
        jf=s.factor(s.Matrix([mapped[R],mapped[S]]).jacobian([r,z]).det())
        ji=s.factor(s.Matrix([back[r],back[z]]).jacobian([R,S]).det())
        assert s.factor(jf-det/h**3)==0
        assert s.factor(jf*ji.subs(mapped,simultaneous=True)-1)==0
        # ACTUAL incidence derivative after source normal-coordinate change,
        # independent of the declared current coefficient transformation.
        w=s.Matrix([b[1],b[2],b[3]]);old=inv*w
        replacement={b[i+1]:old[i] for i in range(3)}
        Gnew=G.subs(replacement,simultaneous=True)
        Jnew=s.Matrix([[s.diff(Gnew[i,j],q).subs(values) for q in b] for i,j in coords])
        assert Jnew.det()==J.det()/det
        assert numerator/Jnew.det()==det*numerator/J.det()
        current_coeff=[s.factor(det*q.subs(back,simultaneous=True)*ji) for q in F]
        current_pullback=[s.factor(q.subs(mapped,simultaneous=True)*jf/det) for q in current_coeff]
        assert all(s.factor(a-b)==0 for a,b in zip(current_pullback,F))
        # Transport MARKED homogeneous divisors; do not replace them by
        # arbitrary receiving coordinate hyperplanes or a new round torus.
        transported_lines=lines*inv
        assert transported_lines*A==lines
        for point in vertices:
            assert transported_lines*(A*point)==lines*point
        transported_basis=[s.factor(q.subs(back,simultaneous=True)*ji) for q in basis]
        pulled=[s.factor(q.subs(mapped,simultaneous=True)*jf) for q in transported_basis]
        assert all(s.factor(a-b)==0 for a,b in zip(pulled,basis))
        observed=[]
        for cycle in prior['cycles']:
            sub={r:s.sympify(cycle['normals']['r'],locals={'u':u,'v':v}),z:s.sympify(cycle['normals']['s'],locals={'u':u,'v':v})}
            jac=s.Matrix([sub[r],sub[z]]).jacobian([u,v]).det()
            order=tuple({'u':u,'v':v}[q] for q in cycle['inner_outer_order'])
            observed.append([res(q.subs(sub,simultaneous=True)*jac,order) for q in pulled])
        assert s.Matrix(observed)==pairing
        # Unimodular full pairing retains all integral cycle coordinates,
        # including both directions invisible to the split-only screen.
        assert pairing.det()==1
        hostile=[s.factor(q/det-q) for q in F]
        assert any(q!=0 for q in hostile)
        runs.append({'normal_matrix':[[str(q) for q in row] for row in A.tolist()],
            'normal_det':str(det),'forward_projective_coordinates':[str(mapped[R]),str(mapped[S])],
            'forward_Jacobian':str(jf),'transformed_current_coefficients':[str(q) for q in current_coeff],
            'actual_incidence_Jacobian_new_over_old':str(s.factor(Jnew.det()/J.det())),
            'marked_five_line_covectors':[[str(q) for q in row] for row in transported_lines.tolist()],
            'all_six_vertex_incidences_preserved':True,'full_four_cycle_pairing_preserved':True,
            'transported_cycle_coordinates':'Identity in the transported marked integral basis, including invisible classes.',
            'omitted_delta_normal_det_defects':[str(q) for q in hostile]})
    # The receiving affine horizon need not be a canonical boundary.
    horizon_A=s.Matrix([[1,0,0],[0,2,0],[1,1,3]])
    horizon_point=s.Matrix([1,-4,1])
    assert (horizon_A*horizon_point)[2]==0
    assert all(q!=0 for q in lines*horizon_point)
    # Two P1 boundary maps: radial-first residue of the ordinary projective
    # logarithmic forms. These are arrangement residue/tube maps, not a
    # silently identified external codim2 versus codim3 physical current.
    boundaries=[]
    for label,sub in [('p36_center',{r:k*t,z:t}),('p58_center',{r:1/t,z:k})]:
        # For p58 use p=y/x=rho*T,q=z/x=T, hence s=p/q=rho.
        jac=s.factor(s.Matrix([sub[r],sub[z]]).jacobian([k,t]).det())
        boundary=[s.factor(s.residue(-jac*q.subs(sub,simultaneous=True),t,0)) for q in basis]
        local=s.Matrix([[s.residue(q,k,p) for q in boundary] for p in (0,-1)])
        tubes=pairing.T.inv()*local.T
        assert all(q.is_Integer for q in tubes)
        split=periods*tubes
        expected=s.Matrix([[-1,1],[0,-1]]) if label=='p36_center' else s.Matrix([[0,-1],[-1,1]])
        assert split==expected
        boundaries.append({'center':label,'boundary_one_form_coefficients':[str(q) for q in boundary],
            'tube_columns_local_loop_zero_minus1':[[int(q) for q in row] for row in tubes.tolist()],
            'split_boundary_periods':[[int(q) for q in row] for row in split.tolist()],
            'scope':'Integral arrangement residue/tube map; external normal/current degree-changing gluing remains separately typed.'})
    paths=[LATTICE,CHART,'research/benincasa/checkers/check_history6_current_projective_lattice.py']
    out={'schema':'marici.benincasa.history6-current-gl3-transport.v1','history_index':6,
        'universal_projective_Jacobian':'For w=A nu, h=(A*(r,s,1))_3, det(d(R,S)/d(r,s))=det(A)/h^3.',
        'current_normal_law':'Ordinary source radial two-form is pulled back as a two-form; actual constraint Jacobian in new normal coordinates is Jnew=Jold/det(A). Thus density coefficient is det(A)*F(inverse)*Jac_inverse and ordered delta(w)=delta(nu)/det(A); both together restore E7.',
        'runs':runs,'four_frame_current_and_full_lattice_checks':True,
        'receiving_horizon_hostile':{'source_regular_point':[1,-4,1],'receiving_last_coordinate':0,
            'all_five_source_arrangement_equations_nonzero':True,
            'meaning':'Receiving coordinate horizon cuts the regular complement. Use a projective chart cover and transported canonical infinity divisor, not a fabricated new canonical boundary.'},
        'both_P1_boundary_maps':boundaries,
        'passed':True,'claim_boundary':'Local GL3 normal/current covariance with independently evaluated incidence Jacobians, marked arrangement/full integral cycle transport, and both integral P1 tube maps. No physical lift selection or external codim2/codim3 current identification by fiat.',
        'next_action':'Materialize a conditional contour-admission contract requiring a full integral lift class, owning-source selection/word, normal/constraint prescription and chart-compatible cycle transport. Evaluate the stored regular corner word versus its possible completions, including invisible cycle differences, before any physical promotion.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_gl3_transport.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'GL3_frames':len(runs),'actual_incidence_Jacobians':True,
        'full_integral_cycle_pairings':True,'P1_boundary_maps':2,'receiving_horizon_not_canonical':True,
        'physical_admission':False},indent=2))

if __name__=='__main__':main()
