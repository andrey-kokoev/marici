"""Read-only comparison with owning rotor quotient and endpoint charge sectors."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import sys

from check_antiunitary_charge_gate import audit as anti_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,ROOT,BASE
from check_diagonal_spin_networks import CI,S3
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from assemble_endpoint_charging import geometry,block_diagonal

DEST=BASE/'results/source-charge-sector-bridge.v1.json'


def digest(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def conjugate(M):return tuple(tuple(x.flip(8) for x in row) for row in M)
def direct_sum(Aa,Bb):
    n=len(Aa);return tuple(tuple(Aa[i][j] if i<n and j<n else Bb[i-n][j-n] if i>=n and j>=n else ZERO for j in range(2*n)) for i in range(2*n))


def audit():
    previous=anti_audit()
    parent_path='research/strominger/results/common-endpoint-charging.json'
    parent=load(parent_path);spec_path='research/strominger/contracts/common-endpoint-charging.json';spec=load(spec_path)
    assert parent['status']=='passed'
    beta,eta=F(spec['beta']),F(spec['eta'])
    op=parent['source_operators']['electron'];K=tuple(tuple(decode(x) for x in row) for row in op['kinetic_operator'])
    assert len(K)==4 and adj(K)==K and K!=conjugate(K)
    graph=geometry(4,[tuple(e) for e in op['internal_edges']],op['exterior_ports'])
    assert graph['resistance']==[[F(x) for x in row] for row in op['internal_resistance']]
    # Lead sign reversal and endpoint momenta reversal preserve the Gauss basis.
    # Enumerate complete small integer shells, not just the ground fixtures.
    flux_tests=0;witness=None
    for q in (-1,1):
        for flux in product(range(-2,3),repeat=4):
            if sum(flux)!=q:continue
            rev=tuple(-x for x in flux)
            diagonal=block_diagonal(graph,q,flux,beta,eta)
            assert block_diagonal(graph,-q,rev,beta,eta)==diagonal
            for i in range(4):
                n=tuple(q*int(i==j)-flux[j] for j in range(4))
                opposite=tuple(-q*int(i==j)-rev[j] for j in range(4))
                assert opposite==tuple(-x for x in n) and sum(n)==0
            H=add(K,tuple(tuple(A(diagonal[i]) if i==j else ZERO for j in range(4)) for i in range(4)))
            doubled=direct_sum(H,H)
            swap=tuple(tuple(ONE if (i+4)%8==j else ZERO for j in range(8)) for i in range(8))
            charge=direct_sum(scale(A(q),eye(4)),scale(A(-q),eye(4)))
            assert mm(mm(swap,doubled),adj(swap))==doubled
            assert mm(mm(swap,charge),adj(swap))==scale(A(-1),charge)
            # A coefficient-conjugating swap requires a conjugate kinetic
            # partner. Identical K sectors are only a linear charge-sign swap.
            assert mm(mm(swap,conjugate(doubled)),adj(swap))!=doubled
            conjugate_partner=direct_sum(H,conjugate(H))
            assert mm(mm(swap,conjugate(conjugate_partner)),adj(swap))==conjugate_partner
            flux_tests+=1
            if witness is None:witness={'charge':q,'flux':flux,'opposite_flux':rev,'charging_diagonal':diagonal}
    assert flux_tests>0
    phases=[]
    Q=add(eye(4),scale(A(-1),K))
    assert mm(Q,Q)==eye(4)
    for a,b,c in combinations(range(4),3):
        w=(S3*Q[b][a])*(S3*Q[c][b])*(S3*Q[a][c])
        assert w in (CI,-CI);assert w.flip(8)==-w
        phases.append({'face':[a,b,c],'source_loop_phase':w.record(),'conjugate_loop_phase':(-w).record()})
    try:block_diagonal(graph,-1,[0]*4,beta,eta)
    except ValueError:pass
    else:raise AssertionError('Invalid total charge admitted')

    # Owning quotient law: signed integer states |k,n_e>, Q=k-n_e.
    # Its sign involution requires signed states, not a relabelled positive-q
    # scalar doublet. Energy parameters are explicitly declared inertias.
    quotient_tests=[]
    for inverse_collective,inverse_elementary in [(F(1836),F(1)),(F(1944),F(1)),(F(5,2),F(3,2))]:
        for k,ne in product(range(-2,3),repeat=2):
            q=k-ne;energy=(inverse_collective*k*k+inverse_elementary*ne*ne)/2
            assert (-k)-(-ne)==-q
            assert (inverse_collective*(-k)**2+inverse_elementary*(-ne)**2)/2==energy
        quotient_tests.append({'sum_inverse_collective_inertias':str(inverse_collective),
                               'inverse_elementary_inertia':str(inverse_elementary),
                               'integer_states_tested':25,'charge_sign_reversal_energy_even':True})
    assert 1-0==0-(-1)==1  # source neutral mixing preserves Q, not identity

    source_paths=[parent_path,spec_path,'research/strominger/common-endpoint-charging.md',
        'research/strominger/checkers/assemble_endpoint_charging.py',
        'research/nima/mass-primitive-quotient-charge.md','research/nima/mass-rotor-action-and-external-charge.md',
        'research/nima/checkers/check_mass_primitive_quotient_charge.py',
        'research/scattering/seed-composition/check_source_charge_sector_bridge.py']
    dependencies=set(previous['source_sha256'])|set(source_paths)
    freshness=[]
    for p,h in parent['source_hashes'].items():
        dependencies.add(p);freshness.append({'path':p,'matches_owner_receipt':digest(p)==h})
    assert all(row['matches_owner_receipt'] for row in freshness)
    return {
        'schema':'marici.scattering.source-charge-sector-bridge.v1',
        'status':'owning_sources_supply_conditional_signed_sectors_not_seed_derived_charge_conjugation',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'owning_receipt_hash_comparison':freshness,
        'endpoint_bridge':{'selected_electron_face_line_dimension':4,'native_raw_spinor_dimension':8,
                           'native_logical_doublet_dimension':2,
                           'charges_supplied_in_contract':spec['charges'],
                           'sector_involution':'(q,n,ell) -> (-q,-n,-ell), unchanged matter position',
                           'finite_integer_flux_tests':flux_tests,'witness':witness,
                           'charging_energy_even_under_joint_reversal':True,
                           'full_same_K_blocks_related_by_linear_sector_swap':True,
                           'antiunitary_swap_preserves_identical_K_blocks':False,
                           'conjugate_K_partner_makes_antiunitary_swap_covariant':True,
                           'source_Wilson_phases':phases,
                           'conjugate_partner_is_new_coefficient_input':True,
                           'invalid_total_flux_rejected':True},
        'quotient_bridge':{'charge':'Q=k-n_e on signed integer rotor states',
                           'sector_involution':'(k,n_e) -> (-k,-n_e)',
                           'energy':'(k^2*sum(1/C_s)+n_e^2/C_e)/2','tests':quotient_tests,
                           'elementary_opposite_states':'(0,1) and (0,-1) have Q=-1,+1 and equal energy',
                           'rotor_to_native_spinor_adapter_supplied':False,
                           'physical_quotient_identification_is_source_assumption':True,
                           'charge_preserving_mixing':'(1,0) -> (0,-1) preserves Q=+1 but changes sector; charge alone does not protect identity'},
        'comparison_with_previous_doubling':{'within_qN_obstruction_evaded_by_enlarging_sector_domain':True,
                                             'opposite_charge_representations_exist_conditionally':True,
                                             'opposite_charge_forced_by_affine_seed_inverse':False,
                                             'source_hardware_or_physical_sector_swap_derived':False},
        'boundary':{'all_opposite_charge_constructions_absent':False,'physical_charge_conjugation_derived':False,
                    'energy_evenness_is_annihilation_or_mass_prediction':False,'formal_outcome_admitted':False,
                    'shared_sources_or_receipts_rewritten':False},
        'next_gate':'Construct an exact adapter from the native eight-coordinate spinor to the endpoint parent four face-line coordinates, retaining the four forbidden face-polarization directions. Check whether sign/complex conjugation transports its actual kinetic operator and Wilson phases or needs a new sector partner.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=str)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale source charge bridge receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: owning quotient/endpoint models admit conditional opposite charges with retained signed states and fluxes.')
    print('PASS: endpoint charge-sign swap preserves charging energy, but antiunitary covariance needs conjugate kinetic phases.')
    print('Boundary: charge assignments and rotor/spinor adapter remain inputs, not consequences of inverse seeds.')


if __name__=='__main__':main()
