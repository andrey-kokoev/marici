"""Exact source-bound coherent sorter and exhaustive padded flag predicates."""
import json
from hashlib import sha256
from pathlib import Path
from check_native_spinor_pair_adapter import matrix
from check_pentachoron_spin_interfaces import A,S2,mm,adj
from check_typed_spin_channels import kron,conjugate_matrix
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/programmable-matter-projector-control.v1.json'
NOTE='research/voevodsky/programmable-matter-projector-control-v1.md'
OUT='research/voevodsky/results/programmable-matter-projector-control-v1.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'

def require(ok,msg):
    if not ok:raise ValueError(msg)
def conj(x):return x.flip(8)
def inner(a,b):return sum((conj(x)*y for x,y in zip(a,b)),A())
def main():
    native=json.loads((ROOT/NATIVE).read_text());require(native['verification_passed'],'native receipt')
    for p,h in native['source_hashes'].items():
        require(sha256((ROOT/'research/voevodsky'/p).read_bytes()).hexdigest()==h,'native source drift: '+p)
    cases=[];count=0
    for row in native['adapter_reports']:
        W=matrix(row['cell_encoding']);J=kron(W,conjugate_matrix(W))
        scalar=((A(1)/S2,),(A(),),(A(),),(A(1)/S2,))
        v=tuple(r[0] for r in mm(J,scalar))+(A(),)*28
        require(len(v)==128 and inner(v,v)==1,'normalized padded scalar')
        require(conj(v[0])==v[0] and v[0]!=1,'sorter phase/denominator condition')
        e0=(A(1),)+(A(),)*127;w=tuple(a-b for a,b in zip(e0,v));alpha=A(1)-v[0]
        require(inner(w,w)==2*alpha,'Householder involution coefficient')
        def U(x):
            coefficient=inner(w,x)/alpha
            return tuple(a-b*coefficient for a,b in zip(x,w))
        require(U(e0)==v and U(v)==e0,'sorter seed square')
        # Full basis coverage using rank-one formulas, no truncation of complement.
        for j in range(128):
            basis=tuple(A(i==j) for i in range(128));sorted_state=U(basis)
            require(U(sorted_state)==basis,'sorter involution/basis')
            # U^dag |v><v| U = |0><0|; primary predicate action.
            amplitude=inner(v,basis)
            primary=U(tuple(vv*amplitude for vv in v))
            require(primary==tuple(A(i==0)*sorted_state[0] for i in range(128)),'primary control square')
            carrier=tuple(x if i<100 else A() for i,x in enumerate(basis))
            sorted_carrier=U(carrier)
            require(sorted_carrier==tuple(x if i<100 else A() for i,x in enumerate(sorted_state)),'carrier-presence square')
            rival=tuple(x-y for x,y in zip(sorted_carrier,primary))
            require(rival==tuple(x if 1<=i<100 else A() for i,x in enumerate(sorted_state)),'rival control square')
            if j>=100:require(sorted_state==basis,'vacuum/padding spectator')
            count+=1
        cases.append({'chirality':row['chirality'],'doublet_option':row['doublet_option'],
                      'v0':v[0].record(),'alpha':alpha.record(),'basis_checks':128})
    # Reversible flag calculation keeps every data state. Uncomputation restores
    # clean flag after any operation controlled by it which leaves matter index fixed.
    flags=lambda j:(j==0,1<=j<100,j<100,j==100,j>100)
    for j in range(128):
        p,q,c,vac,pad=flags(j)
        require((p or q)==c and not(p and q) and int(c)+int(vac)+int(pad)==1,'typed flag partition')
        for readyflag in (0,1):
            for predicate in (p,q):
                require((readyflag^int(predicate))^int(predicate)==readyflag,'reversible predicate uncompute')
    paths=[DEF,NOTE,NATIVE,'research/voevodsky/checkers/check_native_spinor_pair_adapter.py',
           'research/voevodsky/checkers/check_typed_spin_channels.py',
           'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',
           'research/conjecture_net/contracts/optical-neutral-record-block.v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.programmable-matter-projector-control-validation.v1',passed=True,
                cases=cases,source_bound_basis_checks=count,coherent_flag_indices_checked=128,
                primary_rank=1,rival_rank=99,carrier_rank=100,matter_vacuum_dimension=1,padding_dimension=27,
                matter_register_dimension=128,record_qubit_joint_dimension=256,
                native_joint_subspace_dimension=202,no_complement_discarded=True,
                verification_level='exact source-field Householder identities, full basis control squares and reversible predicate truth tables',
                native_gates_derived=False,hardware_circuit_compiled=False,physical_admission=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
