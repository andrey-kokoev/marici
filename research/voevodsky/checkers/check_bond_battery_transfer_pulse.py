"""Continuous matched-sector transfer energy and a mid-pulse fault control.

The direct spectral pulse and previous SWAP/Pauli circuit have the same ideal
endpoint but different fault propagation. No autonomous switch or physical
availability of the high-weight encoded interaction is assumed.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import importlib.util
from check_encoded_history_memory import ZERO,ONE,add,mul,conj,scale,inner
from check_history_code_circuit import apply
from check_pairwise_bond_battery_storage import tensor,pauli_state
from check_phase_occupation_necessity import matrix
from check_constraint_energy_accounting import compose

BASE=Path(__file__).resolve().parents[1]


def main():
    previous_raw=(BASE/'results/pairwise_bond_battery_storage.json').read_bytes()
    previous=json.loads(previous_raw)
    circuit_raw=(BASE/'results/history_code_circuit.json').read_bytes()
    assert sha256(circuit_raw).hexdigest()==previous['encoder_receipt_sha256']
    circuit=json.loads(circuit_raw)
    source=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    assert sha256(source.read_bytes()).hexdigest()==previous['owning_code_sha256']
    spec=importlib.util.spec_from_file_location('prior_code',source)
    owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    xrow,zrow=cert['logical_x'],cert['logical_z']
    memory=json.loads((BASE/'results/native_phase_seam_memory.json').read_bytes())
    snapshot=BASE.parent.parent/memory['source_snapshot']
    raw=snapshot.read_bytes()
    assert sha256(raw).hexdigest()==previous['source_snapshot_sha256']
    native=json.loads(raw)['records']['native']['carriers']['belt']
    N=matrix(native['return_entries'])
    assert all(compose(matrix(row['entries']),N)=={} for row in native['seam_projectors'])
    code=[]
    for bit in (0,1):
        v=[ZERO]*32;v[bit<<4]=ONE
        code.append(apply(circuit['component_encoder_gates'],v))
    def word(v,row,offset):
        for i in range(5):
            if row[i] or row[5+i]: v=pauli_state(v,i+offset,row[i],row[5+i])
        return v
    def X(v,offset): return word(v,xrow,offset)
    def Z(v,offset): return word(v,zrow,offset)
    def Y(v,offset): return [mul((F(0),F(1)),a) for a in X(Z(v,offset),offset)]
    def Q(v):
        zz,xx,yy=Z(Z(v,0),5),X(X(v,0),5),Y(Y(v,0),5)
        return [scale(F(1,4),add(add(a,b),add(scale(-1,c),d))) for a,b,c,d in zip(v,zz,xx,yy)]
    def pulse(v,phase):
        coefficient=add(phase,scale(-1,ONE))
        return [add(a,mul(coefficient,b)) for a,b in zip(v,Q(v))]
    J,delta=F(1,2),F(1,4)
    def H(v):
        return [add(scale(J,a),scale(delta/2,add(b,scale(-1,c)))) for a,b,c in zip(v,Z(v,0),Z(v,5))]
    def expectation(v):
        return inner(v,H(v))
    half_phase=(F(0),F(-1))
    for a in (0,1):
        for b in (0,1):
            v=tensor(code[a],code[b])
            assert Q(Q(v))==Q(v)
            assert H(Q(v))==Q(H(v))
            half=pulse(v,half_phase)
            final=pulse(half,half_phase)
            assert final==tensor(code[1-b],code[1-a])
            assert inner(half,half)==inner(final,final)==ONE
            assert expectation(half)==expectation(final)==expectation(v)
    # Actual one-physical-qubit error after half the encoded pulse.
    # This site anticommutes with both owning logical X and logical Z.
    site=next(i for i in range(5) if xrow[i] and zrow[i])
    initial=tensor(code[0],code[0])
    target=tensor(code[1],code[1])
    mid=pulse(initial,half_phase)
    noisy=pauli_state(mid,site,0,1)
    final_noisy=pulse(noisy,half_phase)
    recovered=pauli_state(final_noisy,site,0,1)
    overlap=inner(target,recovered)
    fidelity=mul(conj(overlap),overlap)
    assert fidelity==(F(1,2),F(0))
    # The same syndrome correction is correct: the pulse commutes with all
    # stabilizers, so the fault's syndrome has not changed in the second half.
    for row in owner.QUBIT:
        assert word(recovered,row,0)==recovered
        assert word(recovered,row,5)==recovered
    assert expectation(recovered)==expectation(target)==(J,F(0))
    xweight=owner.weight(tuple(xrow));zweight=owner.weight(tuple(zrow))
    yweight=owner.weight(tuple((a+b)%2 for a,b in zip(xrow,zrow)))
    report={'status':'continuous_transfer_energy_and_midpulse_fault_checked',
            'pair_projector':'Q=(I+Z_n Z_b-X_n X_b+Y_n Y_b)/4=(I-F)/2',
            'matched_hold_H':'J*I+(J-epsilon)*(Z_n-Z_b)/2',
            'direct_pulse':'U(t)=I+(exp(-i*theta(t))-1)*Q; theta(T)=pi',
            'all_time_matched_sector_bare_energy_conservation':'[Q,H_hold]=0, hence every pulse angle preserves bare hold energy',
            'code_pair_basis_cases':4,'half_and_full_pulse_exact':True,
            'interaction_pauli_weights':{'X_X':2*xweight,'Z_Z':2*zweight,'Y_Y':2*yweight},
            'midpulse_fault':{'physical_Z_site_in_first_block':site,
                'time_fraction':'1/2','correct_syndrome_recovery_applied':True,
                'recovered_state_in_code':True,'target_fidelity':'1/2',
                'bare_energy_unchanged':True,
                'conclusion':'The direct high-weight pulse is not single-fault tolerant, despite the fault being one physical Pauli and the syndrome correction being correct.'},
            'implementation_distinction':'The earlier physical SWAP/Pauli circuit had bounded single-fault propagation but only endpoint bare-energy matching. Its fault guarantee does not transfer to this direct simultaneous Hamiltonian.',
            'control_account':'For a pulse Hamiltonian H_hold+lambda(t)*Q, external control power is lambda_dot*<Q>. Since <Q> is constant for the ideal pulse, a pulse beginning and ending at lambda=0 has zero net ideal switching work; this is not a free clock, controller or autonomous latch.',
            'limitations':['The interaction is a declared encoded many-body Hamiltonian, with terms of weights 6,6,10 for this owning code; no two-body physical implementation is supplied.',
                'Bare-energy conservation is asserted in the prepared native coherent sector. Carrier mismatch remains outside this guarantee.',
                'No noise rate, threshold, microscopic bath, autonomous storage lifetime or particle mass follows.'],
            'next_gate':'Recover prior error-transparent or fault-tolerant energy-conserving gate constructions; require both continuous energy accounting and a declared fault guarantee in the SAME implementation.',
            'previous_pair_receipt_sha256':sha256(previous_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/bond_battery_transfer_pulse.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
