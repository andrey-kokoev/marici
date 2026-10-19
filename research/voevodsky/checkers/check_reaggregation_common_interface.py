"""Theorem-specific first gate; executed only inside a charged live attempt."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json,sys,subprocess
from check_native_spinor_pair_adapter import matrix
from check_typed_spin_channels import eye,kron,conjugate_matrix
from check_pentachoron_spin_interfaces import A,S2,mm,adj

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json'

def prove(root,nonce):
    # Fresh source-bound closure, not consumption of a saved success alone.
    subprocess.run([sys.executable,str(root/'research/voevodsky/checkers/check_native_spinor_pair_adapter.py')],check=True,stdout=subprocess.DEVNULL,timeout=300)
    path=root/'research/voevodsky/results/native_spinor_pair_adapter.json'
    native=json.loads(path.read_text());assert native['verification_passed'] and len(native['checks'])==99
    contract=json.loads((root/CONTRACT).read_text());checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    Ps=((A(Q(1,2)),A(),A(),A(Q(1,2))), (A(),A(),A(),A()),(A(),A(),A(),A()),(A(Q(1,2)),A(),A(),A(Q(1,2))))
    omega=((A(1)/S2,),(A(),),(A(),),(A(1)/S2,))
    check('scalar_preparation_normalized',mm(adj(omega),omega)==((A(1),),) and mm(omega,adj(omega))==Ps)
    for row in native['adapter_reports']:
        key=str(row['chirality'])+'_'+str(row['doublet_option']);W=matrix(row['cell_encoding']);J=kron(W,conjugate_matrix(W));v=mm(J,omega)
        check('native_metric_'+key,mm(adj(J),J)==eye(4) and mm(adj(v),v)==((A(1),),))
        # Pi=vvdag; c=I on the 100-state occupied block, zero on separate vacuum.
        # Exact rank-one identities prove projection, orthogonality and rival
        # ready-state annihilation without allocating a 202-square matrix.
        primary_on_v=mm(v,mm(adj(v),v));rival_on_v=tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(v,primary_on_v))
        check('same_preparation_controls_'+key,primary_on_v==v and all(x==0 for r in rival_on_v for x in r))
        check('complement_retained_'+key,len(v)==100 and row['retained_space_dimensions']['full_pair_complement']==96)
        D=matrix(row['effective_cycle_D']);pair=kron(D,conjugate_matrix(D))
        check('scalar_cycle_fixed_'+key,mm(pair,omega)==omega)
    check('vacuum_and_record_contract',contract['frozen_comparison']['rival_control'].startswith('c-Pi') and contract['frozen_comparison']['candidate_parameters']=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'})
    sources={str(Path(__file__).resolve().relative_to(root)).replace('\\','/'):sha256(Path(__file__).read_bytes()).hexdigest(),CONTRACT:sha256((root/CONTRACT).read_bytes()).hexdigest(),str(path.relative_to(root)).replace('\\','/'):sha256(path.read_bytes()).hexdigest()}
    for name,digest in native['source_hashes'].items():sources['research/voevodsky/'+name]=digest
    return {'schema':'marici.voevodsky.reaggregation-gate-receipt.v1','status':'pass','node_id':'freeze-common-interface','outcome':'++','intent':'prove','attempt_nonce':nonce,'checks':checks,'fresh_execution':True,'proof_kind':'exact native metric/projection/covariance checks plus rank-one vacuum-extension identities','kernel_verified_analytic_theorem':False,'physical_admission':False,'dimensions':{'native_pair':100,'matter_with_vacuum':101,'matter_and_one_neutral_record':202},'source_hashes':sources}

if __name__=='__main__':
    out=Path(sys.argv[2]);out.write_text(json.dumps(prove(ROOT,sys.argv[1]),indent=2)+'\n')
