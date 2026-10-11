"""Reuse Kitaev's frozen five-qubit code for the 22-label history.

Five logical bits embed the 22 labels into 32 states; five component codes use
25 physical qubits. Exact block isometries and error overlaps avoid enumerating
2^25 amplitudes. A logical history-phase fault is deliberately NOT relabelled
as a single physical-qubit error.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json

BASE=Path(__file__).resolve().parents[1]
OWNER=BASE.parent/'kitaev'
ZERO=(F(0),F(0))
ONE=(F(1),F(0))


def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0],-a[1]
def scale(q,a): return q*a[0],q*a[1]
def inner(a,b):
    result=ZERO
    for x,y in zip(a,b): result=add(result,mul(conj(x),y))
    return result


def pauli(row,v):
    x=sum(row[i]<<i for i in range(5))
    z=sum(row[5+i]<<i for i in range(5))
    phase=(ONE,(F(0),F(1)),(-F(1),F(0)),(F(0),-F(1)))[sum(row[i]*row[5+i] for i in range(5))%4]
    out=[ZERO]*32
    for j,a in enumerate(v):
        out[j^x]=scale((-1)**((j&z).bit_count()),mul(phase,a))
    return out


def project_plus(row,v):
    return [scale(F(1,2),add(a,b)) for a,b in zip(v,pauli(row,v))]


def main():
    source_path=OWNER/'checkers/check_s3_five_rail_code_freeze.py'
    spec=importlib.util.spec_from_file_location('prior_five_rail_code',source_path)
    prior=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)
    certificate=prior.certify('five_qubit_perfect_code',2,prior.QUBIT)
    rows=prior.QUBIT
    logical_x,logical_z=certificate['logical_x'],certificate['logical_z']
    for basis in range(32):
        v=[ZERO]*32
        v[basis]=ONE
        for row in rows+[logical_z]: v=project_plus(row,v)
        if inner(v,v)!=ZERO: break
    zero=v
    one=pauli(logical_x,zero)
    length=inner(zero,zero)
    assert length[1]==0 and length[0]>0
    assert inner(one,one)==length and inner(zero,one)==ZERO
    for v in (zero,one):
        assert all(pauli(row,v)==v for row in rows)
    assert pauli(logical_z,zero)==zero
    assert pauli(logical_z,one)==[scale(-1,z) for z in one]
    errors=[(0,)*10]+prior.single_rail_errors(2)
    encoded_errors=[[pauli(e,v) for v in (zero,one)] for e in errors]
    overlaps=0
    for i in range(16):
        for j in range(16):
            for a in range(2):
                for b in range(2):
                    expected=length if i==j and a==b else ZERO
                    assert inner(encoded_errors[i][a],encoded_errors[j][b])==expected
                    overlaps+=1
        for a in range(2):
            assert pauli(errors[i],encoded_errors[i][a])==(zero,one)[a]
    # V_bit=(zero,one)/sqrt(length) is an isometry. Tensor products supply
    # a genuine five-logical-qubit encoding; no list of 2^25 entries is needed.
    labels=range(22)
    gram_checks=0
    for j in labels:
        for k in labels:
            product=ONE
            for b in range(5):
                product=mul(product,inner((zero,one)[(j>>b)&1],(zero,one)[(k>>b)&1]))
            expected=(length[0]**5,F(0)) if j==k else ZERO
            assert product==expected
            gram_checks+=1
    global_syndromes=set()
    recoveries=[]
    for block in range(5):
        for error in errors[1:]:
            syndrome=[0]*20
            syndrome[4*block:4*block+4]=[prior.symplectic(error,s,2) for s in rows]
            assert any(syndrome)
            assert tuple(syndrome) not in global_syndromes
            global_syndromes.add(tuple(syndrome))
            recoveries.append({'block':block,'error':list(error),'syndrome':syndrome})
    assert len(global_syndromes)==75
    # Syndrome record is retained. On the correctable span, the unitary
    # recovery E_a V|psi>|ready> -> V|psi>|a> preserves every inner product
    # by the exact block Gram identities. It does not erase noise provenance.
    audit_path=BASE/'results/seam_addressed_history_storage.json'
    audit_raw=audit_path.read_bytes()
    audit=json.loads(audit_raw)
    assert audit['history_dimension']==22
    assert audit['history_phase_error']['fidelity_strictly_below_one']
    # The original selective logical phase remains inside the encoded space.
    # Each |j>_L is stabilized, as are all signed superpositions of them.
    phases=[-1 if j==1 else 1 for j in labels]
    assert phases[1]!=phases[2]
    for j in labels:
        for block in range(5):
            component=(zero,one)[(j>>block)&1]
            signed=[scale(phases[j],z) for z in component]
            assert all(pauli(s,signed)==signed for s in rows)
    # Concrete out-of-model control: two data faults within one block have
    # a syndrome that aliases a single fault and induces a logical error.
    first,second=errors[1],errors[4]  # Z on distinct physical qubits
    combined=tuple((a+b)%2 for a,b in zip(first,second))
    syndrome=tuple(prior.symplectic(combined,s,2) for s in rows)
    correction=next(e for e in errors if tuple(prior.symplectic(e,s,2) for s in rows)==syndrome)
    recovered=[pauli(correction,pauli(first,pauli(second,v))) for v in (zero,one)]
    logical_effect=[[scale(1/length[0],inner(a,b)) for b in recovered] for a in (zero,one)]
    assert logical_effect[0][1]!=ZERO or logical_effect[1][0]!=ZERO or logical_effect[0][0]!=logical_effect[1][1]
    # Optional stabilizer penalty detects physical errors but not logical
    # phases. Its scale is NOT supplied by the occupation law.
    minimum_syndrome_weight=min(sum(s) for s in global_syndromes)
    assert minimum_syndrome_weight==1
    report={'status':'history_code_adapter_and_noise_boundary_checked',
            'history_labels':22,'logical_qubits':5,'logical_capacity':32,
            'unused_logical_labels':10,'physical_data_qubits':25,
            'component_code':'five copies of prior [[5,1,3]]_2 code',
            'raw_block_gram_norm':str(length[0]),'history_isometry_gram_checks':gram_checks,
            'exact_block_error_overlap_checks':overlaps,
            'distinct_nonzero_physical_error_syndromes':75,
            'declared_correctable_noise':'Identity and the linear span of X,Y,Z on any one of the 25 physical data qubits per fault-free recovery interval.',
            'syndrome_retention':'One of 76 correctable error labels is retained; a direct stabilizer readout uses 20 syndrome bits. Fresh/reset resources are not free.',
            'all_history_amplitudes_preserved_under_declared_recovery':True,
            'existing_shor_schedule_resources_for_five_blocks':{'cat_data_contacts':240,'cat_verification_checks':180,'fresh_cat_qubits':240,'syndrome_rounds':3,
                'scope':'Imported prior separated 1-EC bound: one input error with fault-free recovery, or clean input with one recovery fault. An input error plus a recovery fault is not certified here.'},
            'original_logical_history_phase_fault':{'zero_stabilizer_syndrome':True,'corrected_by_this_recovery':False,
                'old_fidelity_loss_survives_logical_encoding':True},
            'two_fault_control':{'first_error':list(first),'second_error':list(second),
                'aliased_single_error_correction':list(correction),
                'logical_error_remains_after_recovery':True,
                'logical_matrix':[[[str(z[0]),str(z[1])] for z in row] for row in logical_effect]},
            'energy':'The existing hold Hamiltonian acts as identity on degenerate history, so the isometric storage encoding changes no bond/battery energy. It supplies no recovery Hamiltonian or resource normalization.',
            'optional_penalty_boundary':'eta*sum (I-S_a)/2 detects each single physical Pauli with energy at least eta, but eta is new input and every logical history phase still has zero penalty.',
            'unimplemented_interfaces':['Physical noise identification: the source-level history phase cannot be assumed to be a single physical-qubit fault.',
                'A gate-level history encoder/decoder and fault-tolerant modular-address controls tied to the storage device.',
                'Recovery work, ready ancillas, retained syndrome disposal and microscopic local implementation.',
                'A combined input-error-plus-recovery-fault threshold, autonomous latch and physical lifetime.'],
            'source_code_sha256':sha256(source_path.read_bytes()).hexdigest(),
            'prior_recovery_packet_sha256':sha256((OWNER/'s3-five-rail-shor-recovery.md').read_bytes()).hexdigest(),
            'history_audit_receipt_sha256':sha256(audit_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'recovery_table':recoveries}
    (BASE/'results/encoded_history_memory.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='recovery_table'},indent=2))


if __name__=='__main__':
    main()
