#!/usr/bin/env python3
"""First composite: source-fixed top normalization and local target pushforward.

No global facet atlas, degree certificate or target boundary selector is inferred.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(ROOT/'research/nima'))
sys.path.insert(0,str(HERE))
import sympy as s
from check_untransported_simple_root_seed_admission import library, bracket
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor,angle
from momentum_twistor_super import SuperTwistor,super_line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state


def super_match(shift):
    lam,_,x=momentum_conserving_kinematics([(1,j*j+j+1+shift*j) for j in range(1,9)],
        [(1,j**3+2*j+1+shift*j*j) for j in range(1,7)])
    eps=s.Matrix([[0,1],[-1,0]]);theta=theta_coefficients(lam,8);Z={}
    for j in range(1,9):
        lj=eps*lam[j]
        Z[j]=SuperTwistor(lam[j].col_join(x[j].T*lj),
            {k:s.factor((lj.T*v)[0]) for k,v in theta[j].items() if (lj.T*v)[0]!=0})
    h=compile_nnmhv_histories(8)[5]
    assert h.outer_pair==(2,6) and h.inner_pair==(3,5) and not h.boundary_updates
    _,o=generalized_r(lam,x,8,(),h.outer_pair,lam[1].T*eps,lam[6].T*eps)
    st=terminal_r_state(h)
    _,i=generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,
        transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))
    def matrix(q,r):return s.Matrix([[lam[j][0] for j in range(1,9)],[lam[j][1] for j in range(1,9)],
        [q.get(j,0) for j in range(1,9)],[r.get(j,0) for j in range(1,9)]])
    H=matrix(o['xi_coefficients'],i['xi_coefficients']);piv=list(H.rref()[1]);assert len(piv)==4
    seeds,groups=library();left,right=seeds['H'];matches=[]
    for chosen in itertools.combinations(range(1,9),7):
        for rot in range(7):
            order=chosen[rot:]+chosen[:rot];mp={j:order[j-1] for j in range(1,8)}
            def point(token):
                if isinstance(token,int):return Z[mp[token]]
                return super_line_plane_point(*(Z[mp[j]] for j in token))
            q,dq=bracket(tuple(point(t) for t in left));r,dr=bracket(tuple(point(t) for t in right))
            assert dq*dr!=0
            C=matrix(q,r);cp=C[:,piv]
            if cp.det()==0:continue
            M=H[:,piv]*cp.inv()
            if M*C!=H:continue
            scale=s.factor(M.det());full=s.factor(o['prefactor']*i['prefactor']*scale**4*dq*dr)
            assert all(s.factor(H[:,list(I)].det()-scale*C[:,list(I)].det())==0 for I in itertools.combinations(range(8),4))
            matches.append({'support':list(chosen),'rotation':rot,'full_superfunction_ratio':str(full),
                'cell_key':{'parallel_classes':sorted(sorted(mp[j] for j in g) for g in groups['H']),
                            'zero_columns':sorted(set(range(1,9))-set(chosen))}})
    assert len(matches)==1 and matches[0]['full_superfunction_ratio']=='1'
    wedge=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0)
    K0=s.factor(o['prefactor']*i['prefactor']*wedge**4/angle(lam,2,3)**4)
    return {'shift':shift,'matches':matches,'K0_12':str(K0),'boundary_update_absent':True}


def normalize(Y,piv):return Y[:,piv].inv()*Y


def derivative(Y,dY,piv):
    inv=Y[:,piv].inv();N=inv*Y
    return inv*dY-inv*dY[:,piv]*N


def target_jac(Y,derivs,piv):
    coords=[(i,j) for i in range(2) for j in range(6) if j not in piv]
    ds=[derivative(Y,d,piv) for d in derivs]
    return s.Matrix([[d[i,j] for d in ds] for i,j in coords]),coords


def target_run(embedding,parameter_values,zshift):
    a=s.symbols('a1:9');a1,a2,a3,a4,a5,a6,a7,a8=a
    H=s.Matrix([[1,a1,a2+a3+a4,(a3+a4)*a5,(a3+a4)*a6,a4*a7,0],
                [0,0,1,a5,a6,a7,a8]])
    chosen=tuple(embedding['support']);r=embedding['rotation'];order=chosen[r:]+chosen[:r]
    C=s.zeros(2,8);plain=s.zeros(2,8)
    # Positive cyclic rotation in rank two twists each wrapped column by
    # (-1)^(k-1)=-1. Plain relabeling preserves cell keys, not positivity.
    for j in range(7):
        sign=-1 if order[j]<chosen[r] else 1
        C[:,order[j]-1]=sign*H[:,j]
        plain[:,order[j]-1]=H[:,j]
    values=dict(zip(a,map(s.Integer,parameter_values)));Cn=C.subs(values)
    plain_n=plain.subs(values)
    negative_plain=sum(bool(plain_n[:,[i,j]].det()<0) for i in range(8) for j in range(i+1,8))
    assert negative_plain>0, 'Untwisted cyclic embedding hostile did not discriminate'
    minors=[Cn[:,[i,j]].det() for i in range(8) for j in range(i+1,8)]
    assert all(v>=0 for v in minors) and Cn.rank()==2
    Z=s.Matrix([[s.Integer(j+zshift)**k for k in range(6)] for j in range(1,9)])
    assert all(Z[list(rows),:].det()>0 for rows in itertools.combinations(range(8),6))
    Y=Cn*Z
    ds=[C.diff(var).subs(values)*Z*values[var] for var in a]
    J,coords=target_jac(Y,ds,[0,1]);d=s.factor(J.det());assert d!=0
    J2,_=target_jac(Y,ds,[0,2]);d2=s.factor(J2.det());assert d2!=0
    N=normalize(Y,[0,1]);basis=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1;basis.append(E)
    transition,_=target_jac(N,basis,[0,2]);dt=s.factor(transition.det())
    assert J2==transition*J and s.factor(dt/d2-1/d)==0
    return {'positive_source_parameters':{str(k):str(v) for k,v in values.items()},'positive_Z_moment_shift':zshift,
        'target_Y':[[str(v) for v in row] for row in Y.tolist()],
        'target_pivot':[1,2],'target_coordinate_order':[[i+1,j+1] for i,j in coords],
        'source_log_jacobian':str(d),'intrinsic_oriented_pushforward_density':str(1/d),
        'alternative_target_pivot':[1,3],'alternative_log_jacobian':str(d2),'target_transition_jacobian':str(dt),
        'transition_covariance_checked':True,'untwisted_cyclic_embedding_negative_minor_count':int(negative_plain)}


def main():
    super_runs=[super_match(j) for j in (0,1,2)]
    embedding=super_runs[0]['matches'][0]
    assert all(r['matches'][0]['support']==embedding['support'] and r['matches'][0]['rotation']==embedding['rotation'] for r in super_runs)
    targets=[target_run(embedding,[2,3,5,7,11,13,17,19],0),
             target_run(embedding,[3,5,7,11,13,17,19,23],1)]
    paths=['research/benincasa/checkers/check_untransported_simple_root_seed_admission.py',
        'research/nima/check_eight_point_history_positroid_matching.py','research/nima/dual_r_invariant.py',
        'research/nima/dual_spinor_kinematics.py','research/nima/momentum_twistor_constructors.py',
        'research/nima/momentum_twistor_super.py','research/nima/nnmhv_coherence_paths.py',
        'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex']
    out={'schema':'marici.benincasa.composite-root-normalization.v1','root':[1,2],'history_index':5,
        'fixed_conventions':{
            'source':'sourced H chart on the matched support, rank-two twisted cyclic embedding (wrapped columns multiplied by -1), ordered dlog a1 wedge ... wedge dlog a8',
            'superfunction':'source H five-bracket product with complete denominators; no independent per-history scale',
            'component':'eta2/eta3 wedge to fourth power times outer/inner prefactors divided by <23>^4',
            'top_target_map':'Phi_Z(C)=C Z with positive rank-six bosonized external Z',
            'target_coordinates':'normalize target columns 1,2 to identity; free entries in row-major order',
            'local_pushforward':'at a regular locally invertible branch, density = 1/det(d target_coords / d log alpha) with declared intrinsic source orientation',
            'boundary_extension':'Not constructed. Retain source residue deletion parity, exposing chart and transition Jacobian; specify target normal and boundary map before comparison.'},
        'superfunction_runs':super_runs,'target_runs':targets,
        'checks':{'three_full_superfunction_unit_matches':True,'all_matching_70_minors_checked':True,
            'uncorrected_history_K_equals_K0':True,'same_H_embedding_at_three_fixtures':True,
            'two_positive_source_and_target_fixtures':True,'nonzero_eight_dimensional_target_log_jacobians':True,
            'target_chart_transition_covariance':True,'untwisted_cyclic_embedding_rejected':True},
        'passed':True,'disposition':'first_composite_top_level_convention_and_local_branch_normalization_constructed; three-composite_and_boundary_comparison_open',
        'claim_boundary':'Exact finite superfunction matching and local target differential controls. Four-dimensional supertwistor kinematics and six-dimensional bosonized target samples are distinct typed domains; no commuting bosonization/component square is inferred. No global degree, five-facet coverage, BCFW-chain orientation anchor, physical boundary residue map or nine-to-twenty image supplied.',
        'next_action':'Extend the same frozen intrinsic conventions to histories 8 and 9 without fitting scales, and retain the independent missing boundary/bosonization comparison square.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/composite_root_normalization.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'embedding':embedding,'checks':out['checks'],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
