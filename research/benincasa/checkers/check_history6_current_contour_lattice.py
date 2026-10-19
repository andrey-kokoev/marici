#!/usr/bin/env python3
"""Integral contour lattice of the retained exceptional direction; no cycle admission."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s
ROOT=Path(__file__).resolve().parents[3]
COVARIANCE='research/benincasa/results/history6_current_covariance.json'
DIRECTIONS='research/benincasa/results/history6_directional_boundaries.json'
SOURCE='research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'


def main():
    cov=json.loads((ROOT/COVARIANCE).read_text());directions=json.loads((ROOT/DIRECTIONS).read_text())
    for receipt in (cov,directions):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert cov['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_covariance.py').read_bytes()).hexdigest()
    text=(ROOT/SOURCE).read_text(encoding='utf-8');lines=text.splitlines()
    anchors={
        'sourced_kernel_cycle':r'\label{general_on_shell_function_momentum_twistors}',
        'residue_identity_scope':r'any $(4k\pl1)$-dimensional cell',
        'excess_constraints_singular_support':'left-over constraints will impose conditions on the external momenta',
        'physical_loop_real_contour':r'restricts each loop-momentum to be {\it real}',
    }
    source_anchors=[]
    for name,needle in anchors.items():
        matches=[(i+1,line) for i,line in enumerate(lines) if needle in line];assert len(matches)==1,(name,matches)
        number,line=matches[0];source_anchors.append({'role':name,'line':number,'text':line})
    r,u=s.symbols('rho inverse_rho');f=[-1/(r*(1+r)),-1/(1+r)]
    poles=[s.Integer(0),s.Integer(-1),s.oo]
    R=s.Matrix([[s.residue(F,r,p) if p!=s.oo else s.residue(F.subs(r,1/u)*(-1/u**2),u,0) for p in poles] for F in f])
    assert R==s.Matrix([[-1,1,0],[0,-1,1]])
    for col,item in enumerate(directions['directional_source_and_decorated_target_routes']):
        assert R[:,col]==s.Matrix([s.Rational(item['exceptional_then_direction_K0']),s.Rational(item['exceptional_then_direction_B22'])])
    relation=s.ones(3,1);assert R*relation==s.zeros(2,1)
    assert R.rank()==2 and R.nullspace()==[relation]
    # H1(P1 minus three marked points,Z)=Z3/<(1,1,1)>.
    # Choose coordinates q=(w0-winfinity,wminus1-winfinity).
    Q=s.Matrix([[1,0,-1],[0,1,-1]])
    reduced=s.Matrix([[-1,1],[0,-1]])
    assert R==reduced*Q and reduced.det()==1
    # The period map on H1 is unimodular. No nonzero homology class can
    # annihilate both split periods for generic nonzero shared amplitude.
    scans=[];zero_count=0
    for winding in itertools.product(range(-2,3),repeat=3):
        w=s.Matrix(winding);period=R*w;class_coordinates=Q*w
        assert (period==s.zeros(2,1))==(class_coordinates==s.zeros(2,1))
        zero_count+=int(period==s.zeros(2,1))
        assert R*(w+7*relation)==period
        scans.append({'winding':list(winding),'class':[int(q) for q in class_coordinates],'period':[int(q) for q in period]})
    assert zero_count==5
    controls=[]
    for label,winding in [('loop_0',[1,0,0]),('loop_minus1',[0,1,0]),('loop_infinity',[0,0,1]),
            ('positive_endpoint_loop_sum',[1,0,1]),('full_three_loop_relation',[1,1,1])]:
        w=s.Matrix(winding);p=R*w
        controls.append({'label':label,'winding':winding,'class':[int(q) for q in Q*w],
            'split_periods_over_2pi_i_shared_current':[int(q) for q in p],
            'total_period':int(sum(p)),'physical_admission':'not_selected_by_this_check'})
    # The total form can have a vanishing period on a NONZERO split class:
    # C0+Cinfinity=-Cminus1, giving (-1,+1), not zero for either split.
    positive=s.Matrix([1,0,1]);central=s.Matrix([0,-1,0])
    assert Q*positive==Q*central and R*positive==s.Matrix([-1,1])
    total=s.ones(1,2)*R;assert total==s.Matrix([[-1,0,1]])
    assert (s.ones(1,2)*reduced).nullspace()==[s.Matrix([0,1])]
    # Verify residue periods in each covariance-tested normal/direction
    # frame. Divide by detA to put the external delta-frame back in the
    # original convention; do not drop the normal orientation factor.
    converted=[]
    x=s.Symbol('rho_prime');amplitude=s.Symbol('A_current')
    for frame in cov['exceptional_normal_direction_tests']:
        A=s.Matrix([[s.sympify(q) for q in row] for row in frame['normal_change_matrix']]);det=A.det()
        a,bb,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
        targets=[s.oo if (p==s.oo and c==0) or (p!=s.oo and c*p+d==0) else
            s.factor(a/c if p==s.oo else (a*p+bb)/(c*p+d)) for p in poles]
        assert len(set(targets))==3
        coeff=[s.sympify(frame[key],locals={'rho_prime':x,'A_current':amplitude})/amplitude/det for key in
            ('new_frame_K0_one_form_coefficient','new_frame_B22_one_form_coefficient')]
        Rp=s.Matrix([[s.residue(F,x,p) if p!=s.oo else s.residue(F.subs(x,1/u)*(-1/u**2),u,0) for p in targets] for F in coeff])
        assert Rp==R
        converted.append({'normal_det':str(det),'ordered_mapped_poles':[str(p) for p in targets],
            'period_matrix_back_in_original_normal_frame':[[str(q) for q in row] for row in Rp.tolist()]})
    # A positive interval is a relative chain, not one of the closed loops.
    # Its unregularized periods have independent endpoint divergences.
    eps,L=s.symbols('epsilon L',positive=True)
    primitives=[s.log(1+r)-s.log(r),-s.log(1+r)]
    for F,P in zip(f,primitives):assert s.factor(s.diff(P,r)-F)==0
    intervals=[s.expand_log(P.subs(r,L)-P.subs(r,eps),force=True) for P in primitives]
    assert s.simplify(sum(intervals)-s.log(eps/L))==0
    assert s.limit(s.limit(intervals[0],L,s.oo),eps,0,dir='+')==-s.oo
    assert s.limit(s.limit(intervals[1],eps,0,dir='+'),L,s.oo)==-s.oo
    paths=[COVARIANCE,DIRECTIONS,SOURCE,'research/benincasa/checkers/check_history6_current_covariance.py']
    out={'schema':'marici.benincasa.history6-current-contour-lattice.v1','history_index':6,
        'normalization':'Periods divided by 2*pi*i times the common nonzero external fermionic constraint current A*delta(nu2)*delta(nu3). Ordered normal frame fixed.',
        'space':'P1_rho minus {0,-1,infinity}; H1=Z3/<(1,1,1)>; positive local loops use rho at finite poles and inverse_rho at infinity.',
        'residue_matrix':[[int(q) for q in row] for row in R.tolist()],
        'quotient_coordinates':'(w0-winfinity,wminus1-winfinity)',
        'quotient_period_matrix':[[int(q) for q in row] for row in reduced.tolist()],
        'quotient_determinant':1,'generic_split_zero_kernel':'Only the zero homology class; common amplitude assumed nonzero, not every fermion component required nonzero.',
        'total_zero_kernel':'The nonzero central-loop class is invisible to K0+B22, but not to either split separately.',
        'controls':controls,'finite_winding_checks':len(scans),'split_zero_winding_count':zero_count,
        'covariant_marked_pole_period_tests':converted,
        'positive_interval':{'relative_chain':'[epsilon,L] on rho>0; not a closed homology cycle',
            'K0_integral_over_shared_current':str(intervals[0]),'B22_integral_over_shared_current':str(intervals[1]),
            'total':str(s.log(eps/L)),'unregularized_limit':'Each split coefficient diverges; endpoint/branch/regularization prescription is additional data, not supplied here.'},
        'source_anchors':source_anchors,
        'source_scope':'The source specifies Gamma_hat_sigma in the delta-integral, singular support for excess constraints, and oriented Cauchy identities for generic dimension4k_plus1 cells. Here source dimension7 has8 constraints and retained exceptional fiber over external codim2 support. No identification of its physical cycle with these generic one-form cells or real loop-momentum contours has been constructed.',
        'rejected_shortcuts':['Full three-loop zero is the null homology relation, not a nontrivial physical cycle annihilating both split periods.',
            'Positive endpoint loop sum has total zero but split periods(-1,+1); it is homologous to minus the nonpositive central loop, not an ordinary positive integration interval.',
            'Dropping the central pole or omitting changed normal determinant fails the retained split residue pairing.',
            'The positive open interval needs endpoint regularization and does not supply a finite canonically selected closed contour.'],
        'passed':True,'claim_boundary':'Exact local integral contour lattice and covariance of marked-pole periods; not physical cycle admission or global weighted cancellation.',
        'next_action':'Lift candidate direction cycles from ordered small normal-link tori in (b2,b3), track rho=b2/b3 and the b2+b3 pole, radius hierarchy and source orientation. Compare the induced classes and wall crossing with the owning Gamma prescription before choosing a physical contour.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_contour_lattice.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'residue_matrix':out['residue_matrix'],'quotient_determinant':1,
        'split_zero_kernel':out['generic_split_zero_kernel'],'positive_endpoint_periods':[-1,1],
        'covariant_period_frames':len(converted),'physical_admission':False},indent=2))

if __name__=='__main__':main()
