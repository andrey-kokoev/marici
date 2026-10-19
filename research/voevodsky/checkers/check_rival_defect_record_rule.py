"""Fresh exact check of the vacuum-safe rival control c-Pi.
The same carrier, scalar preparation, record, parameters and empty reference are
used. This proves a finite conditional constructor, not physical selection.
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
REFINEMENTS='research/voevodsky/contracts/retained-reaggregation-rule-refinements.v1.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'

def vacuum_extend(m):
    """Direct sum with the zero operator on the separate empty sector."""
    return tuple(row+(A(0),) for row in m)+(tuple(A(0) for _ in range(len(m)+1)),)

def generator_blocks(p,g):
    """Derive N+g[(I-R+)/2+(I-R-)/2] from the signed controls."""
    i=eye(len(p));s=add(i,scale(A(-1),p));half=A(Q(1,2))
    diagonal=add(scale(half,add(i,scale(A(-1),s))),scale(half,add(i,s)))
    off_diagonal=add(scale(-half,p),scale(-half,p))
    return scale(g,diagonal),scale(g,off_diagonal),add(i,scale(g,diagonal))

def prove(nonce):
    subprocess.run([sys.executable,str(BASE/'checkers/check_native_spinor_pair_adapter.py')],check=True,stdout=subprocess.DEVNULL,timeout=300)
    native=json.loads((ROOT/NATIVE).read_text());typed=json.loads((BASE/'results/typed_spin_channels.json').read_text())
    assert native['verification_passed']
    contract=json.loads((ROOT/CONTRACT).read_text());refinements=json.loads((ROOT/REFINEMENTS).read_text())
    Ps=matrix(typed['input_scalar_projector']);g=A(Q(1,2))
    # Reuse the exact normalized scalar vector fixed by the admitted interface.
    from check_pentachoron_spin_interfaces import ZERO,ONE,S2
    scalar_vector=((ONE/S2,),(ZERO,),(ZERO,),(ONE/S2,))
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    parameter_ok=contract['frozen_comparison']['candidate_parameters']=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'}
    assert {(r['chirality'],r['doublet_option']) for r in native['adapter_reports']}=={(1,0),(1,1),(-1,0),(-1,1)}
    for row in native['adapter_reports']:
        label=f"{row['chirality']}_{row['doublet_option']}"
        W=matrix(row['cell_encoding']);J=kron(W,conjugate_matrix(W));Pi=mm(mm(J,Ps),adj(J));I=eye(100);c=I;rival_projection=add(c,scale(A(-1),Pi))
        check('native_carrier_same_'+label,len(J)==100 and mm(adj(J),J)==eye(4))
        check('rival_defect_projection_'+label,mm(rival_projection,rival_projection)==rival_projection and adj(rival_projection)==rival_projection and trace(rival_projection)==99)
        check('rival_orthogonal_to_scalar_'+label,mm(rival_projection,Pi)==tuple(tuple(A(0) for _ in range(100)) for _ in range(100)) and add(rival_projection,Pi)==c)
        # Paired signs have R+= (I-Q)⊗I+Q⊗X, R-=Q⊗X-(I-Q)⊗I.
        S=add(I,scale(A(-1),rival_projection));zero=tuple(tuple(A(0) for _ in range(100)) for _ in range(100))
        check('rival_control_square_'+label,add(mm(S,S),mm(rival_projection,rival_projection))==I and add(mm(S,rival_projection),mm(rival_projection,S))==zero)
        check('rival_control_self_adjoint_'+label,adj(S)==S and adj(rival_projection)==rival_projection)
        # The control projection (not the signed involutions) vanishes on vacuum.
        extended=add(vacuum_extend(c),scale(A(-1),vacuum_extend(Pi)))
        vacuum=tuple((A(int(k==100)),) for k in range(101))
        check('rival_control_zero_on_vacuum_'+label,extended==vacuum_extend(rival_projection) and mm(extended,vacuum)==tuple((A(0),) for _ in range(101)))
        # Same normalized native scalar pair and |0> record: Pi v=v; Qv=0.
        v=mm(J,scalar_vector);ready=((A(1),),(A(0),));N=((A(0),A(0)),(A(0),A(1)))
        check('same_ready_pair_and_record_'+label,mm(adj(v),v)==eye(1) and mm(Pi,v)==v and mm(rival_projection,v)==tuple((A(0),) for _ in range(100)) and mm(N,ready)==((A(0),),(A(0),)))
        # Both control projectors share I-PiX resource identity and common empty
        # reference; only the active subspace changes from Pi to Q.
        check('same_native_carrier_'+label,len(rival_projection)==len(Pi)==100)
        check('same_record_pool_'+label,contract['frozen_comparison']['records'].startswith('one neutral two-level record'))
        check('same_preparation_'+label,contract['frozen_comparison']['preparation'].startswith('normalized native scalar pair') and mm(Pi,v)==v)
        check('same_candidate_parameters_'+label,parameter_ok)
        empty00,empty01,empty11=generator_blocks(((A(0),),),g)
        check('same_empty_reference_'+label,empty00==((g,),) and empty01==((A(0),),) and empty11==((1+g,),))
        # Q is a projection, so the same two signed controls sum to I-Q⊗X.
        # Adding N=|1><1| gives bare blocks [[gI,-gQ],[-gQ,(1+g)I]];
        # subtracting the shared empty energy g leaves [[0,-gQ],[-gQ,I]].
        bare_diag0,bare_off,bare_diag1=generator_blocks(rival_projection,g)
        primary00,primary01,primary11=generator_blocks(Pi,g)
        sub_diag0=add(bare_diag0,scale(-g,I));sub_diag1=add(bare_diag1,scale(-g,I))
        check('same_complete_generator_diagonal_'+label,bare_diag0==primary00==scale(g,I) and bare_diag1==primary11==scale(1+g,I) and bare_off==scale(-g,rival_projection) and primary01==scale(-g,Pi) and sub_diag0==zero and sub_diag1==I)
        check('complementary_records_retained_'+label,trace(I)==100 and trace(rival_projection)+trace(Pi)==100)
    expected={c for r in refinements['refinements'] if r['parent']=='rival-defect-record-rule' for c in r['required_checks']}
    # Aggregate per native choice into the two explicitly named refinement checks.
    checks['rival_control_square']=all(checks['rival_control_square_'+f"{r['chirality']}_{r['doublet_option']}"] for r in native['adapter_reports'])
    checks['rival_control_self_adjoint']=all(checks['rival_control_self_adjoint_'+f"{r['chirality']}_{r['doublet_option']}"] for r in native['adapter_reports'])
    checks['rival_control_zero_on_vacuum']=all(checks['rival_control_zero_on_vacuum_'+f"{r['chirality']}_{r['doublet_option']}"] for r in native['adapter_reports'])
    checks['same_ready_pair_and_record']=all(checks['same_ready_pair_and_record_'+f"{r['chirality']}_{r['doublet_option']}"] for r in native['adapter_reports'])
    for name in ('same_native_carrier','same_record_pool','same_preparation','same_candidate_parameters','same_empty_reference','same_complete_generator_diagonal','complementary_records_retained'): 
        checks[name]=all(checks[name+'_'+f"{r['chirality']}_{r['doublet_option']}"] for r in native['adapter_reports'])
    # Keep detail checks as audit data; only the exact required refinement set is
    # consumed as the theorem admission surface.
    required_checks=sorted(expected)
    sources={str(Path(__file__).resolve().relative_to(ROOT)).replace('\\','/'):sha256(Path(__file__).read_bytes()).hexdigest(),CONTRACT:sha256((ROOT/CONTRACT).read_bytes()).hexdigest(),REFINEMENTS:sha256((ROOT/REFINEMENTS).read_bytes()).hexdigest(),NATIVE:sha256((ROOT/NATIVE).read_bytes()).hexdigest()}
    for path in ('research/voevodsky/results/typed_spin_channels.json','research/voevodsky/checkers/check_native_spinor_pair_adapter.py','research/voevodsky/checkers/check_typed_spin_channels.py','research/voevodsky/checkers/check_pentachoron_spin_interfaces.py'):
        sources[path]=sha256((ROOT/path).read_bytes()).hexdigest()
    return {'schema':'marici.voevodsky.rival-defect-record-receipt.v1','status':'pass','node_id':'rival-defect-record-rule','outcome':'++','intent':'prove','attempt_nonce':nonce,'fresh_execution':True,'checks':{k:checks[k] for k in required_checks},'detail_checks':checks,'required_checks':required_checks,'proof_kind':'exact finite carrier projection and vacuum-extension identities; same-input/resource contract checks in four native choices','physical_admission':False,'native_carrier_dimension':100,'separate_vacuum_dimension':1,'record_dimension':2,'rival_projector_rank':99,'candidate_parameters':contract['frozen_comparison']['candidate_parameters'],'control':'Q=c-Pi on carrier; Q=0 on separate vacuum; H_rival=N-g Q⊗X after common empty-reference subtraction.','source_hashes':sources}

if __name__=='__main__':Path(sys.argv[2]).write_text(json.dumps(prove(sys.argv[1]),indent=2)+'\n')
