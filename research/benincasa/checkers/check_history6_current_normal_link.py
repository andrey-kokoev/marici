#!/usr/bin/env python3
"""Lift exceptional direction contours from oriented source normal-link tori."""
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s
ROOT=Path(__file__).resolve().parents[3]
LATTICE='research/benincasa/results/history6_current_contour_lattice.json'
CURRENT='research/benincasa/results/history6_boundary_berezin_current.json'
DIRECTIONS='research/benincasa/results/history6_directional_boundaries.json'
SOURCE='research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'


def main():
    lattice=json.loads((ROOT/LATTICE).read_text());current=json.loads((ROOT/CURRENT).read_text());directions=json.loads((ROOT/DIRECTIONS).read_text())
    for receipt in (lattice,current,directions):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert lattice['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_contour_lattice.py').read_bytes()).hexdigest()
    x,y,B,r,t=s.symbols('b2 b3 b4 rho T',nonzero=True)
    g=y*(x+y+B)/((x+y)*(y+B))
    F=[s.factor(g/(x*y)),s.factor((1-g)/(x*y))]
    assert F==[(B+x+y)/(x*(B+y)*(x+y)),B/(y*(B+y)*(x+y))]
    assert s.factor(sum(F)-1/(x*y))==0
    # Source normal order dx wedge dy is preserved: moving b2,b3 to
    # the front of (b1,b2,b3,b4,...,b8) has two inversions, hence +1.
    source_permutation=[1,2,0,3,4,5,6,7]
    inversions=sum(a>b for i,a in enumerate(source_permutation) for b in source_permutation[i+1:]);assert inversions==2
    blowup=s.Matrix([r*t,t]);cartesian_jac=blowup.jacobian([r,t]);assert cartesian_jac.det()==t
    # dx wedge dy = T drho wedge dT. Radial-first residue has minus sign.
    radial=[s.factor(s.residue(-t*coeff.subs({x:r*t,y:t},simultaneous=True),t,0)) for coeff in F]
    assert radial==[-1/(r*(r+1)),-1/(r+1)]
    R=s.Matrix(lattice['residue_matrix'])
    assert s.Matrix([s.residue(q,r,0) for q in radial])==R[:,0]
    assert s.Matrix([s.residue(q,r,-1) for q in radial])==R[:,1]
    # Ordered torus angles (theta2,theta3) -> (thetaT,thetaR) has det -1.
    angular=s.Matrix([[0,1],[1,-1]]);assert angular.det()==-1
    # Independent two-variable source residues (fixed dx wedge dy torus
    # orientation), and their raw differential-residue order signs.
    inner_x=s.Matrix([s.residue(s.residue(q,x,0),y,0) for q in F])
    inner_y=s.Matrix([s.residue(s.residue(q,y,0),x,0) for q in F])
    assert inner_x==s.Matrix([1,0]) and inner_y==s.Matrix([0,1])
    raw_differential_x_first=inner_x;raw_differential_y_first=-inner_y
    assert raw_differential_x_first==s.Matrix([s.Rational(directions['directional_source_and_decorated_target_routes'][0]['direction_then_exceptional_K0']),s.Rational(directions['directional_source_and_decorated_target_routes'][0]['direction_then_exceptional_B22'])])
    assert raw_differential_y_first==s.Matrix([s.Rational(directions['directional_source_and_decorated_target_routes'][2]['direction_then_exceptional_K0']),s.Rational(directions['directional_source_and_decorated_target_routes'][2]['direction_then_exceptional_B22'])])
    # Holomorphic fermionic/Jacobian prefactors have their center value in
    # either chamber. Polynomial jet controls test that no first/second
    # derivative is silently discarded to fit a selected fermion component.
    h=s.symbols('h0:6');unit=h[0]+h[1]*x+h[2]*y+h[3]*x*y+h[4]*x**2+h[5]*y**2
    jet_x=s.Matrix([s.factor(s.residue(s.residue(q*unit,x,0),y,0)) for q in F])
    jet_y=s.Matrix([s.factor(s.residue(s.residue(q*unit,y,0),x,0)) for q in F])
    assert jet_x==h[0]*inner_x and jet_y==h[0]*inner_y
    chambers=[]
    # All radii are smaller than |b4|; b3+b4 is outside the local torus.
    for rx,ry,b4 in [(s.Rational(1,16),s.Rational(1,8),s.Integer(7)),
                     (s.Rational(1,8),s.Rational(1,16),s.Integer(7))]:
        assert rx>0 and ry>0 and rx!=ry and ry<b4
        ratio=rx/ry;central_winding=1 if ratio>1 else 0
        w=s.Matrix([1,central_winding,0]);period=R*w
        source_period=-period
        expected=inner_x if rx<ry else inner_y
        assert source_period==expected
        lower_bound=abs(rx-ry);assert lower_bound>0
        chambers.append({'radius_b2':str(rx),'radius_b3':str(ry),'b4':str(b4),
            'radius_ratio':str(ratio),'added_divisor_abs_b2_plus_b3_lower_bound':str(lower_bound),
            'rho_circle_winding_about_0':1,'rho_circle_winding_about_minus1':central_winding,
            'direction_cycle_winding':[int(q) for q in w],
            'direction_periods':[int(q) for q in period],
            'ordered_source_torus_periods':[int(q) for q in source_period],
            'source_to_radial_first_orientation':-1,
            'class_description':'C0' if ratio<1 else 'C0+Cminus1=-Cinfinity',
            'physical_admission':'Not selected; radius hierarchy is extra contour data.'})
    wall=s.Matrix(chambers[1]['ordered_source_torus_periods'])-s.Matrix(chambers[0]['ordered_source_torus_periods'])
    assert wall==-R[:,1]==s.Matrix([-1,1])
    # Equal radii put the product torus ON the added pole at antipodal phase.
    epsilon=s.Symbol('epsilon',positive=True)
    wall_point={x:-epsilon,y:epsilon}
    assert (x+y).subs(wall_point)==0 and x.subs(wall_point)!=0 and y.subs(wall_point)!=0
    # b2+b3=0 has a real pole on each split but cancels in their sum.
    central_res=[s.factor(s.residue(q.subs(x,-y+s.Symbol('eta')),s.Symbol('eta'),0)) for q in F]
    assert central_res==[-B/(y*(B+y)),B/(y*(B+y))]
    assert sum(central_res)==0
    # Treating torus order or hierarchy as irrelevant is explicitly hostile.
    assert inner_x-inner_y==s.Matrix([1,-1])
    assert sum(inner_x)==sum(inner_y)==1
    lines=(ROOT/SOURCE).read_text(encoding='utf-8').splitlines()
    needle=r'cell $\Gamma_\sigma\!\in\!G(k,n)$'
    hits=[(i+1,line) for i,line in enumerate(lines) if needle in line];assert len(hits)==1
    source_line,source_text=hits[0]
    paths=[LATTICE,CURRENT,DIRECTIONS,SOURCE,'research/benincasa/checkers/check_history6_current_contour_lattice.py']
    out={'schema':'marici.benincasa.history6-current-normal-link.v1','history_index':6,
        'source_normal_form':'Omega0=(b4+b2+b3)/(b2*(b2+b3)*(b3+b4)) db2 wedge db3; OmegaB=b4/(b3*(b2+b3)*(b3+b4)) db2 wedge db3; sum=dlog b2 wedge dlog b3.',
        'normal_orientation':'db2 wedge db3 with fixed six-base order (b1,b4,b5,b6,b7,b8); source deletion parity+1.',
        'radial_first_coefficients':[str(q) for q in radial],
        'angular_change_matrix':[[int(q) for q in row] for row in angular.tolist()],
        'angular_orientation_determinant':-1,
        'chambers':chambers,
        'fixed_source_orientation_iterated_scalar_residues':{'b2_inner':[int(q) for q in inner_x],'b3_inner':[int(q) for q in inner_y]},
        'raw_differential_residue_order':{'b2_first':[int(q) for q in raw_differential_x_first],'b3_first':[int(q) for q in raw_differential_y_first]},
        'holomorphic_prefactor_jet_controls':'Arbitrary quadratic holomorphic jet contributes only h0; residue argument extends to analytic prefactors on the local complement.',
        'source_wall_crossing':[int(q) for q in wall],
        'wall_origin':'Equal radii intersect b2+b3=0 at b2=-b3 with both coordinate normals nonzero. A complement homotopy between the two product-torus chambers is obstructed; crossing adds the central direction loop.',
        'central_divisor_residues_db3':[str(q) for q in central_res],
        'hostile_hierarchy_ignored_defect':[int(q) for q in inner_x-inner_y],
        'total_source_period_in_both_chambers':1,
        'source_authority_clarification':{'path':SOURCE,'line':source_line,'text':source_text,
            'meaning':'Gamma_sigma denotes the positroid cell in the source, not by itself a prescription for the extra split-pole hierarchy at this exceptional center. The contour symbol/residue representation does not select either radius chamber here.'},
        'passed':True,'claim_boundary':'Explicit oriented local source normal-link lifts and nonzero split wall crossing. This removes arbitrary direction-cycle guesswork but does not select a physical cycle or globally glue the boundary current.',
        'next_action':'Check whether the added b2+b3 divisor and its central direction pole belong to the source positroid boundary or only the weighted split decoration. Track the source canonical divisors and the split divisor under chart changes, then formulate the additional relative-cycle/contour datum required for physical admission.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_normal_link.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'source_torus_chamber_periods':[[int(q) for q in inner_x],[int(q) for q in inner_y]],
        'orientation':-1,'wall_crossing':out['source_wall_crossing'],'equal_radius_torus_hits_added_pole':True,
        'Gamma_source_meaning':'positroid cell, not selected exceptional contour','physical_admission':False},indent=2))

if __name__=='__main__':main()
