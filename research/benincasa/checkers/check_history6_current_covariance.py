#!/usr/bin/env python3
"""Kernel/pivot and external normal/direction covariance of local currents."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s, normalize, berezin_pair
ROOT=Path(__file__).resolve().parents[3]
CURRENT='research/benincasa/results/history6_boundary_berezin_current.json'
CHART='research/benincasa/results/history6_common_corner.json'


def main():
    current=json.loads((ROOT/CURRENT).read_text());chart=json.loads((ROOT/CHART).read_text())
    for receipt in (current,chart):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert current['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_boundary_berezin_current.py').read_bytes()).hexdigest()
    b=s.symbols('b1:9');C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])[:,[0,1,2,4,5,7]]
    D=normalize(C,[0,1]).applyfunc(s.factor)
    h11,h12,h21,h22=s.symbols('h11 h12 h21 h22');H=s.Matrix([[h11,h12],[h21,h22]])
    dh=s.factor(H.det())
    # All components: each sector wedge scales by detH, so the full
    # fermionic numerator scales by detH^4, precisely like eight constraints.
    HD=H*D
    assert all(s.factor(HD[:,list(p)].det()-dh*D[:,list(p)].det())==0 for p in itertools.combinations(range(6),2))
    row_constraint_change=s.kronecker_product(H,s.eye(4))
    assert s.factor(row_constraint_change.det()-dh**4)==0
    coords=[(i,j) for i in range(2) for j in range(4)]
    labels=[1,2,3,5,6,8];runs=[]
    for kind,values in [('regular_b3',[2,3,0,7,11,13,17,19]),('exceptional_center',[3,0,0,11,13,17,19,23])]:
        v=dict(zip(b,map(s.Integer,values)));Dn=D.subs(v)
        M=s.diag(2,3,5,7);z=M*(-Dn[:,2:].T).row_join(s.eye(4))
        G=D*z.T;assert G.subs(v)==s.zeros(2,4)
        J=s.Matrix([[s.diff(G[i,j],u).subs(v) for u in b] for i,j in coords]);detJ=s.factor(J.det());assert detJ!=0
        sector_ref={p:s.factor(Dn[:,list(p)].det()) for p in itertools.combinations(range(6),2)}
        n0=berezin_pair(Dn[:,[0,5]])
        admitted=[];excluded=[]
        for p in itertools.combinations(range(6),2):
            detp=sector_ref[p]
            if detp==0:
                excluded.append({'labels':[labels[j] for j in p],'disposition':'singular_gauge_patch_not_zero_current'});continue
            # H depends on b. At G=0, d(HG)=H dG because dH G vanishes.
            Hp=D[:,list(p)].inv();Hp0=Hp.subs(v)
            Jprime=s.kronecker_product(Hp0,s.eye(4))*J
            detprime=s.factor(Jprime.det());assert detprime==Hp0.det()**4*detJ
            P=Hp0*Dn
            assert all(s.factor(P[:,list(q)].det()-Hp0.det()*sector_ref[q])==0 for q in sector_ref)
            nprime=berezin_pair(P[:,[0,5]])
            assert s.factor(nprime/detprime-n0/detJ)==0
            admitted.append({'labels':[labels[j] for j in p],'gauge_det':str(s.factor(Hp0.det())),
                'bosonic_constraint_Jacobian':str(detprime),'fermion_over_constraint_ratio':str(s.factor(nprime/detprime))})
        assert len(admitted)==(14 if kind=='regular_b3' else 12)
        # Independently differentiate varying pivot gauges at nontrivial and
        # orientation-reversing representatives, not just the frozen H law.
        for p in ((0,5),(1,4),(5,0)):
            Hp=D[:,list(p)].inv();P=(Hp*D).applyfunc(s.factor);Gp=P*z.T
            direct=s.Matrix([[s.diff(Gp[i,j],u).subs(v) for u in b] for i,j in coords])
            expected=s.kronecker_product(Hp.subs(v),s.eye(4))*J
            assert direct==expected
        negative=s.Matrix([[0,1],[2,3]]);assert negative.det()==-2
        nneg=berezin_pair((negative*Dn)[:,[0,5]])
        assert s.factor(nneg/(negative.det()**4*detJ)-n0/detJ)==0
        # Dropping the fermionic frame factor is a retained hostile defect.
        hostile=s.factor(n0/(negative.det()**4*detJ)-n0/detJ);assert hostile!=0
        runs.append({'source_open':kind,'regular_pivots':admitted,'excluded_pivots':excluded,
            'three_actual_pivot_derivative_checks':True,'negative_det_frame_covariance':True,
            'omitted_fermionic_gauge_factor_defect':str(hostile)})
    # Normal-frame covariance is density-valued, not a scalar invariance.
    # w=A nu, delta(w)=delta(nu)/detA. On the blowup direction the induced
    # projective transformation is x=(a*r+b)/(c*r+d).
    r,x=s.symbols('rho rho_prime');amplitude=s.Symbol('A_current')
    fiber=[-amplitude/(r*(r+1)),-amplitude/(r+1)]
    frames=[]
    for A in (s.Matrix([[2,1],[1,3]]),s.Matrix([[0,1],[1,0]]),s.Matrix([[3,0],[0,-2]])):
        a,bb,c,d=A[0,0],A[0,1],A[1,0],A[1,1];det=s.factor(A.det());assert det!=0
        forward=(a*r+bb)/(c*r+d);inverse=(d*x-bb)/(a-c*x)
        derivative=s.factor(s.diff(inverse,x));change=s.factor(s.diff(forward,r))
        assert s.factor(derivative.subs(x,forward)*change)==1
        converted=[]
        for F in fiber:
            # Multiply coefficient by detA for the changed delta-frame,
            # then change the one-form coordinate. Pulling both factors
            # back restores exactly the original current.
            transformed=s.factor(det*F.subs(r,inverse)*derivative)
            assert s.factor(transformed.subs(x,forward)*change/det-F)==0
            converted.append(str(transformed))
        hostile=s.factor(fiber[0]/det-fiber[0]);assert hostile!=0
        frames.append({'normal_change_matrix':[[str(q) for q in row] for row in A.tolist()],
            'normal_det':str(det),'direction_change':str(forward),
            'new_frame_K0_one_form_coefficient':converted[0],'new_frame_B22_one_form_coefficient':converted[1],
            'pullback_with_delta_factor_defects':['0','0'],'omitted_delta_frame_factor_defect':str(hostile),
            'positivity_scope':'Normal/direction frame changes are coordinate changes, not admission of a new positive or physical contour.'})
    # Scalar regular normal w=a*nu+O(nu^2) has delta(w)=delta(nu)/a|support.
    scalar=[]
    for scale in (s.Integer(2),s.Integer(-3),1+b[0]**2):
        transformed=scale*amplitude
        assert s.factor(transformed/scale-amplitude)==0
        defect=s.factor(amplitude/scale-amplitude);assert defect!=0
        scalar.append({'normal_scale_on_support':str(scale),'new_coefficient':str(transformed),
            'covariance_defect':'0','omitted_normal_scale_defect':str(defect)})
    paths=[CURRENT,CHART,'research/benincasa/checkers/check_history6_boundary_berezin_current.py',
        'research/benincasa/checkers/check_history6_bosonization_bridge.py']
    out={'schema':'marici.benincasa.history6-current-covariance.v1','history_index':6,
        'universal_kernel_frame_law':'Cprime=H C; fermionic degree8 numerator Nprime=det(H)^4 N; ordered eight-constraint Jacobian Jprime=det(H)^4 J at incidence support, including varying H. Therefore Nprime/Jprime=N/J.',
        'pivot_runs':runs,'scalar_normal_tests':scalar,'exceptional_normal_direction_tests':frames,
        'normal_current_transition':'For w=A nu use coefficient det(A)*f(rho(rho_prime))*d rho/d rho_prime and delta(w)=delta(nu)/det(A). This preserves the current; coefficient alone is not invariant.',
        'passed':True,'scope':'Local algebraic kernel-gauge/pivot and normal-frame covariance with preserved orientation factors. No global atlas/current cycle or physical contour has been admitted.',
        'physical_contour_gate':'A physical contour needs a sourced cycle with winding/orientation at rho0,rho-1,rho-infinity and compatibility with the external constraint prescription. Pivot covariance cannot pick it. Added pole remains nonpositive and cannot be silently added to positive endpoint closure.',
        'next_action':'Construct the punctured-direction contour/winding lattice and test which contour choices give the retained split residues, then compare admission conditions with the owning source prescription without fitting a physical cycle from a desired cancellation.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_covariance.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'regular_pivot_counts':[len(r['regular_pivots']) for r in runs],
        'excluded_pivot_counts':[len(r['excluded_pivots']) for r in runs],'normal_frames':len(frames),
        'physical_contour_gate':out['physical_contour_gate']},indent=2))

if __name__=='__main__':main()
