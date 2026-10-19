"""Endpoint operator-class obstruction and an explicit conditional gauge-neutral selector."""
from fractions import Fraction as F
from itertools import product,permutations
import argparse
import json

from check_flux_ground_doublets import audit as ground_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,ROOT,BASE
from check_electron_charge_spin_frontier import qm

DEST=BASE/'results/cross-lead-selection.v1.json'


def audit():
    previous=ground_audit();parent=load('research/strominger/results/common-endpoint-charging.json')
    K=tuple(tuple(decode(x) for x in row) for row in parent['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    beta=F(load('research/strominger/contracts/common-endpoint-charging.json')['beta']);v=beta/4
    # Reuse source-bound ground actions, reconstructed by prior audit, rather
    # than treating the owner historical receipt as a fresh scientific replay.
    # Avoid replaying the entire prerequisite chain twice: the character rows
    # bind group elements and the actual T is reconstructed below from exact
    # native data using the same adapter, without calling dressed_audit again.
    from check_native_intrinsic_spinor_adapter import native_decode
    from check_diagonal_spin_networks import S3,CI
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6
    anchor=tuple(face[0][i][0] for i in range(2));w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    assert mm(adj(V),V)==scale(n0,eye(4))
    from check_electron_charge_spin_frontier import spin
    actions={};projector_sum=tuple(tuple(ZERO for _ in range(4)) for _ in range(4));maps=[]
    for item in previous['ground_representation']['character_rows']:
        q=tuple(F(x) for x in item['quaternion']);U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        perm=[face.index(mm(mm(U,p),adj(U))) for p in face]
        raw=tuple(tuple(U[i%2][j%2] if i//2==perm[j//2] else ZERO for j in range(8)) for i in range(8))
        T=mm(mm(D,raw),V);actions[q]=(perm,T)
        assert mm(T,K)==mm(K,T) and mm(adj(T),T)==eye(4)
        chi=decode(item['plus_character']);assert chi==A(2*q[0])
        projector_sum=add(projector_sum,scale(chi.flip(8)/12,T))
        maps.append({'quaternion':item['quaternion'],'permutation':perm})
    assert projector_sum==P
    assert any(P[i][j]!=ZERO for i in range(4) for j in range(4) if i!=j)
    for q,(perm,T) in actions.items():
        for p,(perm2,S) in actions.items():
            target_perm,target_T=actions[qm(q,p)]
            assert [perm[perm2[i]] for i in range(4)]==target_perm and mm(T,S)==target_T
    # Physical basis q=-1: n=-ell-e_k. Hopping changes n, never ell.
    # A separate endpoint/lead shift is gauge neutral but absent from H.
    fluxes=[ell for ell in product(range(-2,3),repeat=4) if sum(ell)==-1]
    hop_tests=0;shift_tests=0;symmetry_tests=0
    for ell in fluxes:
        for k in range(4):
            n=tuple(-ell[i]-int(i==k) for i in range(4))
            assert all(n[i]+ell[i]+int(i==k)==0 for i in range(4))
            for j in range(4):
                moved_n=tuple(n[i]+int(i==k)-int(i==j) for i in range(4))
                assert all(moved_n[i]+ell[i]+int(i==j)==0 for i in range(4))
                hop_tests+=1
            for a,b in permutations(range(4),2):
                # Delta ell=e_a-e_b, Delta n=-Delta ell, unchanged matter.
                dl=tuple(int(i==a)-int(i==b) for i in range(4))
                newell=tuple(x+d for x,d in zip(ell,dl));newn=tuple(x-d for x,d in zip(n,dl))
                assert sum(newell)==-1 and sum(newn)==0
                assert all(newn[i]+newell[i]+int(i==k)==0 for i in range(4))
                shift_tests+=1
            for perm,T in actions.values():
                newell=[0]*4;newn=[0]*4
                for i in range(4):newell[perm[i]]=ell[i];newn[perm[i]]=n[i]
                assert all(newn[i]+newell[i]+int(i==perm[k])==0 for i in range(4))
                assert sum(x*x for x in n)==sum(x*x for x in newn)
                assert sum(x*x for x in ell)==sum(x*x for x in newell)
                symmetry_tests+=1
    assert len(fluxes)==80
    # Bare neutral shift between ground flux i,j leaves the matter vector
    # unchanged. Its squared overlap with destination ground is c²/3.
    overlap_sq=F(4,3)/(v*v+4);leak_sq=1-overlap_sq
    assert 0<overlap_sq<1 and leak_sq>0
    Qabs=lambda x:x.flip(8)*x
    assert all(Qabs(Q[i][j])==A(F(1,3)) for i in range(4) for j in range(4) if i!=j)
    # Conditional group-algebra selector acts on matter and lead together.
    # Adding delta*(I-P_full) leaves the plus ground untouched, raises minus.
    delta=F(1,7);selector_energy=scale(A(delta),Pm)
    assert mm(selector_energy,P)==tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
    assert mm(selector_energy,Pm)==scale(A(delta),Pm)
    assert adj(selector_energy)==selector_energy
    for i in range(4):
        Ei=tuple(tuple(ONE if a==b==i else ZERO for b in range(4)) for a in range(4))
        assert mm(selector_energy,Ei)!=mm(Ei,selector_energy)

    dependencies=set(previous['source_sha256'])|{
        'research/voevodsky/spinor-endpoint-constructor.md',
        'research/voevodsky/checkers/check_spinor_endpoint_constructor.py',
        'research/voevodsky/spinor-quantum-leads.md',
        'research/scattering/seed-composition/check_cross_lead_selection.py'}
    return {
        'schema':'marici.scattering.cross-lead-selection.v1',
        'status':'existing_endpoint_algebra_conserves_flux_conditional_joint_symmetry_selector_is_a_new_interaction',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'endpoint_operator_class':{'generators':['assisted matter hopping at fixed ell','endpoint/lead momentum polynomials','functions of the block-diagonal H'],
                                  'finite_sums_products_adjoint_preserve_each_ell':True,
                                  'cross_lead_ground_projector_in_class':False,
                                  'proof':'Every generator commutes with each lead momentum and its spectral projectors; closure preserves that property, while P_plus has cross-lead ground entries.',
                                  'hopping_basis_tests':hop_tests,'physical_flux_states_tested':len(fluxes),
                                  'scope':'specified endpoint Hamiltonian algebra, not all gauge-compatible controls or devices'},
        'neutral_shift':{'operator':'lead raise_a lower_b together with endpoint lower_a raise_b, unchanged matter',
                          'Gauss_preserved':True,'basis_tests':shift_tests,
                          'included_in_existing_H':False,'preserves_dressed_ground':False,
                          'ground_overlap_squared':'4/(3*(v^2+4))',
                          'ground_overlap_squared_fixture':str(overlap_sq),
                          'excited_record_weight_fixture':str(leak_sq)},
        'joint_symmetry':{'map':'(matter k,n,ell)->(pi(k),pi(n),pi(ell)) with native monomial coefficient',
                           'Gauss_preserved':True,'charging_norms_preserved':True,
                           'source_K_covariance':True,'basis_tests':symmetry_tests,'source_group_maps':maps,
                           'bounded_symmetry_operator_exists_on_full_rotor_lattice':True,
                           'same_as_a_term_in_existing_H':False},
        'conditional_selector':{'formula':'P_full=(2/24)*sum_g conjugate(chi_plus(g))*U_joint(g)',
                                'ground_restriction':'P_plus=(I+Q_label)/2',
                                'projector_restriction_exactly_verified':True,
                                'full_projector_argument':'finite-group central idempotent; the checked native representation extends by rotor-coordinate permutations',
                                'Gauss_and_H_compatible':True,
                                'possible_added_energy':'H_new=H_endpoint+delta*(I-P_full), delta>0',
                                'ground_effect':'keeps plus doublet at old ground energy; raises minus by delta',
                                'ground_energy_witness_delta':str(delta),
                                'commutes_with_each_fixed_lead_momentum':False,
                                'interaction_or_coherent_selection_source_implemented':False,
                                'nonselected_sector_retained':True},
        'boundary':{'all_Gauss_compatible_cross_lead_controls_absent':False,
                    'physical_implementation_or_preparation_derived':False,
                    'symmetry_selector_is_native_H':False,'annihilation_or_photon_outputs_derived':False,
                    'shared_sources_or_receipts_rewritten':False,'formal_outcome_admitted':False},
        'next_gate':'Construct a retained factorization of the added selector into explicit matter/endpoint/lead controls, or test an existing source control library against those operators. Account for flux-changing work and nonselected records; do not treat the group-average existence proof as physical implementation.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale cross-lead selection receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: endpoint Hamiltonian algebra conserves every lead flux and cannot implement the cross-lead doublet projector.')
    print('PASS: neutral flux shifts preserve Gauss but leak from ground; joint native symmetry gives an exact conditional selector.')
    print('Boundary: selector is an added interaction/control, not native dynamics, physical preparation or annihilation.')


if __name__=='__main__':main()
