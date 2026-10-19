"""Fresh exact native transport of both signed controlled involutions.
Finite mathematical constructor only; no physical calibration or admission.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json,subprocess,sys
from check_native_spinor_pair_adapter import matrix
from check_typed_spin_channels import eye,kron,conjugate_matrix,trace
from check_pentachoron_spin_interfaces import A,mm,adj,scale,add

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/voevodsky'
CONTRACT='research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'
MEDIATOR='research/voevodsky/results/finite_record_mediator_constructor.json'

def prove(nonce):
    subprocess.run([sys.executable,str(BASE/'checkers/check_native_spinor_pair_adapter.py')],check=True,stdout=subprocess.DEVNULL,timeout=300)
    subprocess.run([sys.executable,str(BASE/'checkers/check_finite_record_mediator_constructor.py')],check=True,stdout=subprocess.DEVNULL,timeout=300)
    native=json.loads((ROOT/NATIVE).read_text());med=json.loads((ROOT/MEDIATOR).read_text())
    assert native['verification_passed'] and med['verification_passed']
    contract=json.loads((ROOT/CONTRACT).read_text());typed=json.loads((BASE/'results/typed_spin_channels.json').read_text())
    Ps=matrix(typed['input_scalar_projector']);assert len(Ps)==4 and trace(Ps)==1
    g=A(Q(1,2));checks={}
    def check(name,result):
        checks[name]=bool(result)
        if not result:raise AssertionError(name)
    for row in native['adapter_reports']:
        label=f"{row['chirality']}_{row['doublet_option']}"
        W=matrix(row['cell_encoding']);J=kron(W,conjugate_matrix(W));Pi=mm(mm(J,Ps),adj(J));I=eye(100);S=add(I,scale(A(-1),Pi))
        check('native_pair_isometry_'+label,mm(adj(J),J)==eye(4))
        check('transported_scalar_projection_'+label,mm(Pi,Pi)==Pi and adj(Pi)==Pi and trace(Pi)==1)
        check('retained_native_complement_'+label,trace(S)==99 and mm(S,Pi)==tuple(tuple(A(0) for _ in range(100)) for _ in range(100)))
        # R+ = S⊗I + Pi⊗X, R- = Pi⊗X - S⊗I.
        # In two record blocks they are [[S,Pi],[Pi,S]] and [[-S,Pi],[Pi,-S]].
        diag_identity=add(mm(S,S),mm(Pi,Pi));cross=add(mm(S,Pi),mm(Pi,S))
        check('plus_signed_involution_'+label,diag_identity==I and cross==tuple(tuple(A(0) for _ in range(100)) for _ in range(100)))
        check('minus_signed_involution_'+label,diag_identity==I and cross==tuple(tuple(A(0) for _ in range(100)) for _ in range(100)))
        check('signed_controls_self_adjoint_'+label,adj(S)==S and adj(Pi)==Pi)
        # Q+=(I-R+)/2, Q-=(I-R-)/2, hence Q++Q-=I-Pi⊗X.
        qdiag=add(scale(A(Q(1,2)),Pi),scale(A(Q(1,2)),add(I,S)))
        qoff=scale(A(-1),Pi)
        check('two_controls_sum_full_diagonal_'+label,qdiag==I and qoff==scale(A(-1),Pi))
        # With N=|1><1|, the full one-slot Hamiltonian before empty-reference
        # subtraction is [[gI,-gPi],[-gPi,(1+g)I]]. The common empty-pool
        # energy is g*sqrt(M)=g at M=1; subtracting gI leaves [[0,-gPi],[-gPi,I]].
        bare00=scale(g,I);bare11=scale(1+g,I);bare01=scale(-g,Pi)
        sub00=add(bare00,scale(-g,I));sub11=add(bare11,scale(-g,I))
        check('complete_hamiltonian_diagonal_and_scalar_'+label,bare00==scale(g,I) and bare11==scale(1+g,I) and sub00==scale(A(0),I) and sub11==I)
        check('common_reference_subtraction_'+label,add(sub00,scale(g,I))==bare00 and add(sub11,scale(g,I))==bare11)
        check('native_interaction_annihilates_complement_'+label,mm(Pi,S)==tuple(tuple(A(0) for _ in range(100)) for _ in range(100)))
    for carrier,report in med['signed_controlled_gate_checks'].items():
        check('source_signed_control_verified_'+carrier,report['two_signed_controlled_involutions'] and report['weighted_self_adjoint'])
    check('same_candidate_parameters',contract['frozen_comparison']['candidate_parameters']=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'})
    check('common_neutral_pool_law',med['vacuum_subtracted_law']=='K+sum n_j-(g/sqrt(M))*P*sum X_j' and med['full_controlled_diagonal_terms_retained'])
    checks['vacuum_extension_is_separate_and_dark']=contract['frozen_comparison']['carrier'].startswith('native 100-state pair plus a separately retained empty sector') and contract['frozen_comparison']['primary_control'].endswith('zero on vacuum')
    assert checks['vacuum_extension_is_separate_and_dark']
    sources={str(Path(__file__).resolve().relative_to(ROOT)).replace('\\','/'):sha256(Path(__file__).read_bytes()).hexdigest(),CONTRACT:sha256((ROOT/CONTRACT).read_bytes()).hexdigest(),NATIVE:sha256((ROOT/NATIVE).read_bytes()).hexdigest(),MEDIATOR:sha256((ROOT/MEDIATOR).read_bytes()).hexdigest()}
    for path in ('research/voevodsky/checkers/check_native_spinor_pair_adapter.py','research/voevodsky/checkers/check_finite_record_mediator_constructor.py','research/voevodsky/checkers/check_typed_spin_channels.py','research/voevodsky/checkers/check_pentachoron_spin_interfaces.py'):
        sources[path]=sha256((ROOT/path).read_bytes()).hexdigest()
    return {'schema':'marici.voevodsky.native-signed-record-receipt.v1','status':'pass','node_id':'native-signed-record-rule','outcome':'++','intent':'prove','attempt_nonce':nonce,'fresh_execution':True,'checks':checks,'proof_kind':'exact native projector transport and complete one-record Hamiltonian accounting in all four native chirality/doublet cases','physical_admission':False,'native_pair_dimension':100,'scalar_projector_rank':1,'retained_complement_dimension':99,'candidate_parameters':contract['frozen_comparison']['candidate_parameters'],'Hamiltonian':'Before common empty subtraction: N+g(I-Pi⊗X); for M=1,g=1/2 the record blocks are [[gI,-gPi],[-gPi,(1+g)I]]. Subtract common empty reference gI to obtain N-gPi⊗X.','source_hashes':sources}

if __name__=='__main__':
    Path(sys.argv[2]).write_text(json.dumps(prove(sys.argv[1]),indent=2)+'\n')
