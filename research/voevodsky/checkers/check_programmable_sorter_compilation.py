# /// script
# dependencies = ["sympy"]
# ///
"""Source-specific exact Givens compile, exhaustive Gray-path lowering."""
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
from check_native_spinor_pair_adapter import matrix
from check_pentachoron_spin_interfaces import A,S2,mm
from check_typed_spin_channels import kron,conjugate_matrix
ROOT=Path(__file__).resolve().parents[3]
NOTE='research/voevodsky/programmable-sorter-compilation-v1.md'
OUT='research/voevodsky/results/programmable-sorter-compilation-v1.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'

def require(ok,msg):
    if not ok:raise ValueError(msg)
def swap(k,pair):
    a,b=pair
    return b if k==a else a if k==b else k
def edge(pair,kind,entries=None):
    a,b=pair;bit=(a^b).bit_length()-1
    require(a^b==1<<bit,'non-adjacent primitive')
    require(a&(1<<bit)==0,'target orientation')
    result=dict(kind=kind,target_bit=bit,controls={str(i):(a>>i)&1 for i in range(7) if i!=bit},indices=[a,b])
    if entries is not None:result['matrix']=entries
    return result

def main():
    native=json.loads((ROOT/NATIVE).read_text());require(native['verification_passed'],'native')
    for p,h in native['source_hashes'].items():require(sha256((ROOT/'research/voevodsky'/p).read_bytes()).hexdigest()==h,'native drift')
    row=next(r for r in native['adapter_reports'] if r['chirality']==1 and r['doublet_option']==0)
    W=matrix(row['cell_encoding']);raw=mm(kron(W,conjugate_matrix(W)),((A(1)/S2,),(A(),),(A(),),(A(1)/S2,)))
    support=[i for i,r in enumerate(raw) if r[0]!=0]
    require(len(support)==50 and all(raw[i][0]==S2/10 for i in support),'actual real uniform scalar')
    w0=1-S.sqrt(2)/10;alpha=w0;pivot=w0;normsq=w0**2
    gates=[];rotations=[];lowering_checks=0
    for j in support:
        if j==0:continue
        b=-S.sqrt(2)/10;r=S.sqrt(S.simplify(normsq+b*b))
        a=pivot;G=S.Matrix([[a/r,b/r],[-b/r,a/r]])
        require(S.simplify(G.T*G-S.eye(2))==S.zeros(2),'rotation unitary')
        require(S.simplify(G*S.Matrix([a,b])-S.Matrix([r,0]))==S.zeros(2,1),'elimination')
        entries=[[str(x) for x in G.row(i)] for i in range(2)]
        path=[0]
        for bit in range(7):
            if j&(1<<bit):path.append(path[-1]^(1<<bit))
        swaps=list(zip(path[:-2],path[1:-1]));pair=(path[-2],path[-1])
        # Verify complete two-level conjugation support and orientation.
        for k in range(128):
            moved=k
            for ab in swaps:moved=swap(moved,ab)
            require((moved==pair[0])==(k==0) and (moved==pair[1])==(k==j),'Gray conjugation support')
            restored=moved
            for ab in reversed(swaps):restored=swap(restored,ab)
            require(restored==k,'Gray spectator restoration')
            lowering_checks+=1
        lowered=[edge(ab,'MCX') for ab in swaps]+[edge(pair,'MC-real-rotation',entries)]+[edge(ab,'MCX') for ab in reversed(swaps)]
        gates.extend(lowered);rotations.append(dict(pair=[0,j],matrix=entries,gray_path=path,lowered_gate_count=len(lowered)))
        normsq=S.simplify(normsq+b*b);pivot=r
    require(S.simplify(normsq-2*alpha)==0,'full reflection norm')
    # Inverse each primitive in reverse chronological order, preserving labels.
    inverse=[]
    for g in reversed(gates):
        item=dict(g)
        if g['kind']=='MC-real-rotation':item['matrix']=[list(r) for r in zip(*g['matrix'])]
        inverse.append(item)
    circuit=gates+[dict(kind='basis-phase-flip',index=0,phase='-1')]+inverse
    require(len(rotations)==49,'elimination count')
    paths=[NOTE,NATIVE,'research/voevodsky/checkers/check_native_spinor_pair_adapter.py',
           'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',
           'research/voevodsky/checkers/check_typed_spin_channels.py',
           'research/conjecture_net/contracts/programmable-matter-projector-control.v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.programmable-sorter-compilation.v1',passed=True,
                source_case=dict(chirality=1,doublet_option=0),matter_qubits=7,
                nonzero_scalar_amplitudes=50,elimination_rotations=len(rotations),
                lowered_gate_count=len(circuit),gray_basis_checks=lowering_checks,
                gate_set='six-controlled X and arbitrary real rotations, plus basis-state phase flip',
                chronological_circuit=circuit,elimination_certificate=rotations,
                norm_error_bound='L*delta for unitary per-gate approximants',
                hardware_execution=False,finite_alphabet_synthesis=False,physical_admission=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','chronological_circuit','elimination_certificate')},indent=2))
if __name__=='__main__':main()
