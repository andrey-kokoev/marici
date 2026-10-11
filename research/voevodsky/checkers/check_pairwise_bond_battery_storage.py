"""Address-free bond/battery storage and an existing-code gate realization.

New declared record architecture: one battery bit per bond. Inherited gap
J-epsilon; no separate history lookup. The battery stores the old pattern.
Energy preservation is on the actual coherent carrier, not all carrier states.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import importlib.util
from check_encoded_history_memory import ZERO,ONE,mul,scale
from check_history_code_circuit import apply
from check_constraint_energy_accounting import compose
from check_phase_occupation_necessity import matrix

BASE=Path(__file__).resolve().parents[1]


def tensor(a,b): return [mul(a[i],b[j]) for j in range(32) for i in range(32)]


def swap_state(v,a,b):
    out=[ZERO]*len(v)
    for i,z in enumerate(v):
        j=i^((1<<a)|(1<<b)) if ((i>>a)&1)!=((i>>b)&1) else i
        out[j]=z
    return out


def pauli_state(v,site,x,z):
    phase=(F(0),F(1)) if x and z else ONE
    out=[ZERO]*len(v)
    for i,a in enumerate(v):
        out[i^(x<<site)]=scale((-1)**(z*((i>>site)&1)),mul(phase,a))
    return out


def permute_error(e,a,b):
    result=list(e)
    result[a],result[b]=result[b],result[a]
    return result


def main():
    circuit_path=BASE/'results/history_code_circuit.json'
    circuit_raw=circuit_path.read_bytes()
    circuit=json.loads(circuit_raw)
    owning_path=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    assert circuit['source_code_sha256']==sha256(owning_path.read_bytes()).hexdigest()
    spec=importlib.util.spec_from_file_location('owning_code',owning_path)
    owner=importlib.util.module_from_spec(spec); spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    logical_x=cert['logical_x']
    memory_raw=(BASE/'results/native_phase_seam_memory.json').read_bytes()
    memory=json.loads(memory_raw)
    snapshot=BASE.parent.parent/memory['source_snapshot']
    snapshot_raw=snapshot.read_bytes()
    assert sha256(snapshot_raw).hexdigest()==memory['source_snapshot_sha256']
    native=json.loads(snapshot_raw)['records']['native']['carriers']['belt']
    N=matrix(native['return_entries'])
    seams=[matrix(item['entries']) for item in native['seam_projectors']]
    assert len(seams)==21 and all(compose(P,N)=={} for P in seams)
    epsilon,J=F(1,4),F(1,2)
    delta=J-epsilon
    # F = (X tensor X) SWAP: (n,b)->(1-b,1-n).
    # Complete four-state test, including non-ready batteries.
    for p in (0,1):
        for n in (0,1):
            for b in (0,1):
                nn,bb=1-b,1-n
                assert (1-bb,1-nn)==(n,b)
                before=epsilon*n+J*(n-(1-p))**2+delta*b
                after=epsilon*nn+J*(nn-(1-p))**2+delta*bb
                assert after-before==2*J*p*(nn-n)
    m=21; full=(1<<m)-1
    def transfer(n,b): return full^b,full^n
    def total_energy(n,b):
        return epsilon*n.bit_count()+J*(m-n.bit_count())+delta*b.bit_count()
    # Formula applies to every bit pattern, not only one-hot states.
    fixtures=[0,full]+[1<<j for j in range(m)]+[full^(1<<j) for j in range(m)]
    for n in fixtures:
        nn,bb=transfer(n,0)
        assert nn==full and bb==full^n
        assert transfer(nn,bb)==(n,0)
        assert total_energy(n,0)==total_energy(nn,bb)
    source=[(1<<j,0) for j in range(m)]
    targets=[transfer(*s) for s in source]
    assert len(set(targets))==m
    assert all(n==full and b.bit_count()==20 for n,b in targets)
    assert all(total_energy(*s)==F(41,4) for s in source+targets)
    # Clifford circuit: whole-codeblock SWAP via five pairwise physical
    # SWAPs, then the owning logical-X Pauli word on each block.
    code=[]
    for bit in (0,1):
        v=[ZERO]*32; v[bit<<4]=ONE
        code.append(apply(circuit['component_encoder_gates'],v))
    gates=[('SWAP',i,i+5) for i in range(5)]
    for offset in (0,5):
        for i in range(5):
            if logical_x[i] or logical_x[5+i]:
                gates.append(('P',offset+i,logical_x[i],logical_x[5+i]))
    assert len(gates)==11
    for n in (0,1):
        for b in (0,1):
            v=tensor(code[n],code[b])
            for gate in gates:
                v=swap_state(v,gate[1],gate[2]) if gate[0]=='SWAP' else pauli_state(v,*gate[1:])
            assert v==tensor(code[1-b],code[1-n])
    # Support propagation; phases do not affect correctability. Faults are
    # arbitrary Pauli products on the qubits of a single physical gate.
    paulis=[(0,0),(1,0),(0,1),(1,1)]
    def propagate(e,tail):
        for gate in tail:
            if gate[0]=='SWAP': e=permute_error(e,gate[1],gate[2])
        return e
    def weights(e): return [sum(v!=(0,0) for v in e[:5]),sum(v!=(0,0) for v in e[5:])]
    input_cases=0
    for i in range(10):
        for p in paulis[1:]:
            e=[(0,0)]*10; e[i]=p
            assert sum(weights(propagate(e,gates)))==1
            input_cases+=1
    gate_fault_cases=0
    for k,gate in enumerate(gates):
        sites=gate[1:3] if gate[0]=='SWAP' else (gate[1],)
        errors=[(a,b) for a in paulis for b in paulis if (a,b)!=((0,0),(0,0))] if len(sites)==2 else [(a,) for a in paulis[1:]]
        for values in errors:
            e=[(0,0)]*10
            for site,value in zip(sites,values): e[site]=value
            assert max(weights(propagate(e,gates[k+1:])))<=1
            gate_fault_cases+=1
    assert gate_fault_cases==93
    # A data error AND a gate fault can already make two errors in one block.
    e=[(0,0)]*10; e[0]=(0,1)
    e=propagate(e,gates[:2])
    e[6]=(e[6][0],e[6][1]^1)  # extra fault at the second SWAP's battery rail
    combined_weights=weights(propagate(e,gates[2:]))
    assert combined_weights==[0,2]
    report={'status':'pairwise_bond_battery_storage_and_encoded_gate_checked',
            'architecture_change':'21 independently addressable battery bits replace the nondegenerate ladder plus explicit history; their occupation pattern retains the input.',
            'battery_gap':str(delta),'pair_map':'(n,b)->(1-b,1-n)',
            'ready_battery_map':'|n>|0...0> -> |1...1>|complement(n)>',
            'explicit_modular_history_addressing_required':False,
            'all_patterns_identity':'Each pair is an involution; tensoring proves exact recovery for arbitrary coherent superpositions and populated batteries.',
            'pattern_fixtures_checked':len(fixtures),
            'onehot_sector':{'input_occupied_bonds':1,'output_occupied_bonds':21,'charged_battery_bits':20,
                'output_bond_energy':'21/4','battery_energy':'5','conserved_total':'41/4'},
            'empty_occupied_carrier_control':'Unlike the previous history-disabled gate, a present coherent carrier with all bonds empty fills them and charges all 21 battery bits. Initial penalty energy 21*J supplies it; this is not the absent-carrier vacuum.',
            'coherent_carrier_energy_conserved':True,
            'off_sector_energy_change':'2*J*P_e*(n_e_after-n_e_before); zero on N, not a global conservation theorem.',
            'component_physical_gates':gates,
            'per_pair_physical_swaps':5,'per_pair_single_qubit_paulis':6,
            'all_pairs_physical_swaps':105,'all_pairs_single_qubit_paulis':126,
            'encoded_data_qubits':210,
            'encoding_resource':'42 logical bits (21 bonds plus 21 battery bits), each in the prior five-qubit code; excludes preparation, recovery ancillas and the native carrier.',
            'logical_pair_basis_cases_checked':4,
            'input_error_support_cases':input_cases,'single_gate_fault_support_cases':gate_fault_cases,
            'fault_guarantee':'One input physical-qubit error with ideal gates remains one error; with clean input one gate fault leaves at most one error in each affected code block. Subsequent fault-free component recovery corrects these. A simultaneous input error and gate fault is not certified.',
            'combined_input_and_gate_fault_control':{'remaining_error_weights_by_block':combined_weights,'outside_one_error_per_block_guarantee':True},
            'not_transversal_SUM':'Whole-block SWAP exchanges identical codes; it does not assume the refuted railwise logical CNOT.',
            'limitations':['This is an explicit different battery/history architecture, not a coordinate change of the earlier simple ladder.',
                'The gate lists implement endpoint transfers. Energy conservation of the matched-sector endpoint does not prove that every elementary physical SWAP/Pauli conserves the bare hold energy during execution.',
                'Encoded preparations, recovery energy, physical noise coupling and spatial routing are supplied or open; the mathematical gate fault model is not a derived bath.',
                'A logical phase acting on an entire battery pattern still evades single-physical-qubit recovery.',
                'There is no autonomous latch, physical lifetime, mass calibration or isotope stability prediction.'],
            'source_snapshot_sha256':snapshot.stem,'encoder_receipt_sha256':sha256(circuit_raw).hexdigest(),
            'owning_code_sha256':sha256(owning_path.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/pairwise_bond_battery_storage.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__': main()
