"""Source-bound counterexamples to a frozen whole-class compiler conjecture."""
import json
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
from check_native_spinor_pair_adapter import matrix
from check_pentachoron_spin_interfaces import A,S2,mm
from check_typed_spin_channels import kron,conjugate_matrix
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/routing-only-projector-control-conjecture.v1.json'
NOTE='research/voevodsky/routing-only-projector-control-obstruction-v1.md'
OUT='research/voevodsky/results/routing-only-projector-control-obstruction-v1.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'
def require(ok,msg):
    if not ok:raise ValueError(msg)
def conj(x):return x.flip(8)
def norm(v):return sum((conj(x)*x for x in v),A())
def main():
    native=json.loads((ROOT/NATIVE).read_text());require(native['verification_passed'],'native receipt')
    for p,h in native['source_hashes'].items():require(sha256((ROOT/'research/voevodsky'/p).read_bytes()).hexdigest()==h,'native source drift')
    reports=[]
    for row in native['adapter_reports']:
        W=matrix(row['cell_encoding']);J=kron(W,conjugate_matrix(W))
        v=tuple(r[0] for r in mm(J,((A(1)/S2,),(A(),),(A(),),(A(1)/S2,))))+(A(),)*28
        require(norm(v)==1 and v[0]==S2/10,'source normalized scalar')
        # Pi^2=Pi is equivalent to norm(v)=1. Target X is Hermitian involution;
        # the orthogonal Pi/complement block decomposition proves unitarity.
        active=tuple(x*conj(v[0]) for x in v)
        inactive=tuple(A(i==0)-x for i,x in enumerate(active))
        probs=tuple(conj(x)*x+conj(y)*y for x,y in zip(active,inactive))
        require(sum(probs,A())==1,'target normalized output')
        require(active[0]==F(1,50) and inactive[0]==F(49,50),'input-label branches')
        require(probs[0]==F(1201,1250),'retained input-label probability')
        require(sum(probs[1:],A())==F(49,1250),'outside-label probability')
        # Each outside probability <= their sum < input-label probability,
        # since each is a sum of absolute squares. This gives max-label bound.
        j=next(i for i in range(1,100) if active[i]!=0)
        require(active[j]!=0 and inactive[0]!=0,'two output labels')
        require(all(probs[i]==0 for i in range(100,128)),'vacuum/padding retained dark')
        reports.append(dict(chirality=row['chirality'],doublet_option=row['doublet_option'],
                            witness_input=[0,0],second_output_label=j,
                            second_label_record_one_amplitude=active[j].record(),
                            max_single_label_probability='1201/1250',outside_input_label_probability='49/1250'))
    # Positive control: diagonal coordinate projector has no off-label output.
    for source in range(128):
        for record in (0,1):
            target_record=record^(source==0)
            require(target_record in (0,1),'coordinate-projector positive control')
    paths=[DEF,NOTE,NATIVE,'research/voevodsky/checkers/check_native_spinor_pair_adapter.py',
           'research/voevodsky/checkers/check_typed_spin_channels.py',
           'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.routing-only-projector-control-obstruction-validation.v1',passed=True,
                conjecture='routing-and-phase-suffice-for-native-scalar-controlled-flip',
                proposed_attempt_outcome='-+',independent_admission=False,
                cases=reports,positive_control_coordinate_projector=True,
                universal_invariant='block-monomial closure by written finite-word induction',
                counterexample_level='exact native-source arithmetic in all four cases',
                squared_overlap_upper_bound='1201/1250',pure_state_trace_distance_lower_bound='sqrt(49/1250)',
                physical_experiment=False,physical_admission=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
