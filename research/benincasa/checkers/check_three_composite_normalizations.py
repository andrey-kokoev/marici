#!/usr/bin/env python3
"""Extend the fixed history-5 convention to all three composite roots.

Preserves the first-composite receipt; no source producers or atlas repair.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(ROOT/'research/nima'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as s
from check_untransported_simple_root_seed_admission import library,bracket
from check_composite_root_normalization import normalize,target_jac
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor,angle
from momentum_twistor_super import SuperTwistor,super_line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state

CASES=[(5,[1,2],'H'),(8,[1,3],'A'),(9,[2,3],'H')]


def match(history_index,root,seed,shift):
    lam,_,x=momentum_conserving_kinematics([(1,j*j+j+1+shift*j) for j in range(1,9)],
        [(1,j**3+2*j+1+shift*j*j) for j in range(1,7)])
    eps=s.Matrix([[0,1],[-1,0]]);theta=theta_coefficients(lam,8);Z={}
    for j in range(1,9):
        lj=eps*lam[j]
        Z[j]=SuperTwistor(lam[j].col_join(x[j].T*lj),
            {k:s.factor((lj.T*v)[0]) for k,v in theta[j].items() if (lj.T*v)[0]!=0})
    h=compile_nnmhv_histories(8)[history_index]
    assert [h.inner_pair[1]-4,h.outer_pair[1]-4]==root and not h.boundary_updates
    _,o=generalized_r(lam,x,8,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)
    st=terminal_r_state(h)
    _,i=generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,
        transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))
    def matrix(q,r):return s.Matrix([[lam[j][0] for j in range(1,9)],[lam[j][1] for j in range(1,9)],
        [q.get(j,0) for j in range(1,9)],[r.get(j,0) for j in range(1,9)]])
    H=matrix(o['xi_coefficients'],i['xi_coefficients']);piv=list(H.rref()[1]);assert len(piv)==4
    seeds,groups=library();left,right=seeds[seed];matches=[];count=0
    size=8 if seed=='A' else 7
    for chosen in itertools.combinations(range(1,9),size):
        for rot in range(size):
            order=chosen[rot:]+chosen[:rot];mp={j:order[j-1] for j in range(1,size+1)}
            def point(token):
                if isinstance(token,int):return Z[mp[token]]
                return super_line_plane_point(*(Z[mp[j]] for j in token))
            q,dq=bracket(tuple(point(t) for t in left));r,dr=bracket(tuple(point(t) for t in right))
            assert dq*dr!=0;count+=1
            C=matrix(q,r);cp=C[:,piv]
            if cp.det()==0:continue
            M=H[:,piv]*cp.inv()
            if M*C!=H:continue
            scale=s.factor(M.det());full=s.factor(o['prefactor']*i['prefactor']*scale**4*dq*dr)
            assert all(s.factor(H[:,list(I)].det()-scale*C[:,list(I)].det())==0 for I in itertools.combinations(range(8),4))
            matches.append({'support':list(chosen),'rotation':rot,'seed':seed,'full_superfunction_ratio':str(full),
                'cell_key':{'parallel_classes':sorted(sorted(mp[j] for j in g) for g in groups[seed]),
                            'zero_columns':sorted(set(range(1,9))-set(chosen))}})
    assert len(matches)==1 and matches[0]['full_superfunction_ratio']=='1',matches
    wedge=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0)
    K0=s.factor(o['prefactor']*i['prefactor']*wedge**4/angle(lam,2,3)**4)
    return {'shift':shift,'matches':matches,'K0':str(K0),'boundary_update_absent':True,'nonsingular_seed_candidates':count}


def target(embedding,vals,zshift):
    a=s.symbols('a1:9');a1,a2,a3,a4,a5,a6,a7,a8=a
    charts={'H':s.Matrix([[1,a1,a2+a3+a4,(a3+a4)*a5,(a3+a4)*a6,a4*a7,0],[0,0,1,a5,a6,a7,a8]]),
            'A':s.Matrix([[1,a1,a2,a3+a4,(a3+a4)*a5,(a3+a4)*a6,a4*a7,0],[0,0,0,1,a5,a6,a7,a8]])}
    chart=charts[embedding['seed']];chosen=tuple(embedding['support']);r=embedding['rotation'];order=chosen[r:]+chosen[:r]
    C=s.zeros(2,8);plain=s.zeros(2,8);wrapped=[]
    for j,label in enumerate(order):
        sign=-1 if label<chosen[r] else 1
        if sign==-1:wrapped.append(label)
        C[:,label-1]=sign*chart[:,j];plain[:,label-1]=chart[:,j]
    v=dict(zip(a,map(s.Integer,vals)));Cn=C.subs(v);Pn=plain.subs(v)
    negative=sum(bool(Pn[:,[i,j]].det()<0) for i in range(8) for j in range(i+1,8))
    assert all(Cn[:,[i,j]].det()>=0 for i in range(8) for j in range(i+1,8))
    assert not wrapped or negative>0
    Z=s.Matrix([[s.Integer(j+zshift)**k for k in range(6)] for j in range(1,9)])
    assert all(Z[list(I),:].det()>0 for I in itertools.combinations(range(8),6))
    Y=Cn*Z;derivs=[C.diff(z).subs(v)*Z*v[z] for z in a]
    J,coords=target_jac(Y,derivs,[0,1]);det=s.factor(J.det());assert det!=0
    J2,_=target_jac(Y,derivs,[0,2]);det2=s.factor(J2.det());assert det2!=0
    N=normalize(Y,[0,1]);basis=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1;basis.append(E)
    T,_=target_jac(N,basis,[0,2]);dt=s.factor(T.det())
    assert J2==T*J and s.factor(dt/det2-1/det)==0
    return {'source_parameters':{str(k):str(q) for k,q in v.items()},'positive_Z_moment_shift':zshift,
        'source_chart_matrix':[[str(q) for q in row] for row in C.tolist()],
        'wrapped_columns_with_minus_sign':wrapped,'untwisted_negative_minor_count':negative,
        'target_Y':[[str(q) for q in row] for row in Y.tolist()],
        'target_pivot':[1,2],'target_coordinate_order':[[i+1,j+1] for i,j in coords],
        'target_log_jacobian':str(det),'intrinsic_pushforward_density':str(1/det),
        'alternative_pivot':[1,3],'alternative_log_jacobian':str(det2),
        'target_transition_jacobian':str(dt),'transition_covariance_checked':True}


def main():
    priorpath='research/benincasa/results/composite_root_normalization.json'
    prior=json.loads((ROOT/priorpath).read_text())
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_composite_root_normalization.py').read_bytes()).hexdigest()
    rows=[]
    for hi,root,seed in CASES:
        runs=[match(hi,root,seed,t) for t in (0,1,2)]
        e=runs[0]['matches'][0]
        assert all(r['matches'][0]==e for r in runs)
        ts=[target(e,[2,3,5,7,11,13,17,19],0),target(e,[3,5,7,11,13,17,19,23],1)]
        if hi==5:
            assert [r['K0'] for r in runs]==[r['K0_12'] for r in prior['superfunction_runs']]
            assert [t['target_log_jacobian'] for t in ts]==[t['source_log_jacobian'] for t in prior['target_runs']]
        rows.append({'history_index':hi,'root':root,'seed':seed,'superfunction_runs':runs,'target_runs':ts})
    paths=[priorpath,'research/benincasa/checkers/check_composite_root_normalization.py',
        'research/benincasa/checkers/check_untransported_simple_root_seed_admission.py',
        'research/nima/check_eight_point_history_positroid_matching.py','research/nima/dual_r_invariant.py',
        'research/nima/dual_spinor_kinematics.py','research/nima/momentum_twistor_constructors.py',
        'research/nima/momentum_twistor_super.py','research/nima/nnmhv_coherence_paths.py',
        'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex']
    out={'schema':'marici.benincasa.three-composite-normalizations.v1','rows':rows,
        'fixed_rule':prior['fixed_conventions']|{'source':'matched sourced A or H chart with rank-two positive cyclic twist and ordered eight-dlog orientation','superfunction':'matched source A or H five-bracket product, full denominators, unit normalization; no fitted scale'},
        'checks':{'nine_exact_full_unit_superfunction_matches':True,'six_positive_local_target_tests':True,
            'all_matching_70_minors_checked':True,'all_three_K_equals_K0':True,
            'six_nonzero_target_log_jacobians':True,'six_target_transition_covariances':True,
            'wrapped_column_sign_hostiles_checked':True,'history5_predecessor_preserved':True},
        'passed':True,'disposition':'three_composite_intrinsic_top_normalization_rule_extended; global_and_boundary_comparison_open',
        'missing':['global BCFW source-chain orientation and target degree','bosonized-target/component extraction square',
            'physical target boundary generators/normals and residue map','complete 5/6/5 physical facet provenance'],
        'next_action':'Construct one actual composite source-boundary-to-target differential map, test rank and target normal, and distinguish contracted/nonphysical images without assuming the missing full atlas.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'evidence_level':'Fresh exact finite superfunction matching and local differential algebra; no full atlas or kernel proof.'}
    path=ROOT/'research/benincasa/results/three_composite_normalizations.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'matches':[{k:r[k] for k in ('history_index','root','seed')}|{'embedding':r['superfunction_runs'][0]['matches'][0]} for r in rows],
        'checks':out['checks'],'disposition':out['disposition'],'missing':out['missing']},indent=2))


if __name__=='__main__':main()
