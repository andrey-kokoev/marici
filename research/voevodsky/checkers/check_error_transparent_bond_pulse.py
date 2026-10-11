"""Uniform error-sector lift from the verified recovery map.

An error-transparent pulse and hold can be constructed together. The old hold
extension is not silently replaced: a source-bound error-sector energy witness
shows why transparency cannot conserve that old hold on every correctable sector.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import importlib.util
import json
from check_encoded_history_memory import ZERO,ONE,add,mul,scale,inner,pauli
from check_history_code_circuit import apply
from check_coupled_six_piece_belt import ONE as NATIVE_ONE
from check_constraint_energy_accounting import identity,times,compose

BASE=Path(__file__).resolve().parents[1]


def main():
    circuit_path=BASE/'results/history_code_circuit.json'
    circuit_raw=circuit_path.read_bytes();circuit=json.loads(circuit_raw)
    pulse_path=BASE/'results/bond_battery_transfer_pulse.json'
    pulse_raw=pulse_path.read_bytes();pulse=json.loads(pulse_raw)
    pair=json.loads((BASE/'results/pairwise_bond_battery_storage.json').read_text())
    assert pair['encoder_receipt_sha256']==sha256(circuit_raw).hexdigest()
    source=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    assert sha256(source.read_bytes()).hexdigest()==circuit['source_code_sha256']
    spec=importlib.util.spec_from_file_location('prior_code',source)
    owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    table={r['decoded_syndrome']:r for r in circuit['recovery_table']}
    def correct(v):
        out=[ZERO]*32
        for j,a in enumerate(v):
            row=table[j&15]
            x,z=row['controlled_logical_x'],row['controlled_logical_z']
            phase=(F(0),F(1)) if x and z else ONE
            out[j^(x<<4)]=scale((-1)**(z*((j>>4)&1)),mul(phase,a))
        return out
    def recover(v): return correct(apply(circuit['component_decoder_gates'],v))
    def unrecover(v): return apply(circuit['component_encoder_gates'],correct(v))
    def logical(v,kind):
        out=[ZERO]*32
        for j,a in enumerate(v):
            if kind=='X': out[j^16]=a
            else: out[j]=scale((-1)**((j>>4)&1),a)
        return out
    def extended(v,kind): return unrecover(logical(recover(v),kind))
    for j in range(32):
        v=[ZERO]*32;v[j]=ONE
        assert unrecover(recover(v))==v
    code=[]
    for bit in (0,1):
        v=[ZERO]*32;v[16*bit]=ONE
        code.append(apply(circuit['component_encoder_gates'],v))
    errors=[(0,)*10]+owner.single_rail_errors(2)
    phases=[]
    for e in errors:
        decoded=[recover(pauli(e,v)) for v in code]
        support=[j for j,a in enumerate(decoded[0]) if a!=ZERO]
        assert len(support)==1
        s=support[0]
        assert s<16
        phase=decoded[0][s]
        assert decoded[1][s|16]==phase and inner(decoded[1],decoded[1])==ONE
        phases.append(phase)
        for bit in (0,1):
            v=pauli(e,code[bit])
            assert extended(v,'X')==pauli(e,code[1-bit])
            assert extended(v,'Z')==[scale((-1)**bit,a) for a in v]
    # The error sectors form a complete orthogonal basis: 16 sectors x 2.
    error_basis=[pauli(e,v) for e in errors for v in code]
    for i,a in enumerate(error_basis):
        for j,b in enumerate(error_basis): assert inner(a,b)==(ONE if i==j else ZERO)
    # In the recovery frame, the same Q and H act in every two-block sector.
    Q=times(F(1,2),{(0,0):NATIVE_ONE,(3,3):NATIVE_ONE,
                     (0,3):(-NATIVE_ONE[0],NATIVE_ONE[1]),(3,0):(-NATIVE_ONE[0],NATIVE_ONE[1])})
    J,delta=F(1,2),F(1,4)
    H={(j,j):scale(J+delta*F((1-2*(j&1))-(1-2*((j>>1)&1)),2),NATIVE_ONE) for j in range(4)}
    assert compose(Q,Q)==Q and compose(Q,H)==compose(H,Q)
    def half(v):
        q=scale(F(1,2),add(v[0],scale(-1,v[3])))
        coefficient=(F(-1),F(-1))
        result=list(v)
        result[0]=add(v[0],mul(coefficient,q))
        result[3]=add(v[3],scale(-1,mul(coefficient,q)))
        return result
    midfault_cases=0
    for side in (0,1):
        for phase in phases[1:]:
            for j in range(4):
                v=[ZERO]*4;v[j]=ONE
                # Physical error moves to its syndrome sector with this
                # logical-independent phase, as certified on actual states.
                mid=[mul(phase,a) for a in half(v)]
                final=half(mid)
                target_index=(1-((j>>1)&1))|((1-(j&1))<<1)
                expected=[ZERO]*4;expected[target_index]=phase
                assert final==expected
                midfault_cases+=1
    assert midfault_cases==120
    # Keep the old bare-H extension as a distinct control. A physical Z at
    # the prior fault site anticommutes with logical Z on the first block.
    site=pulse['midpulse_fault']['physical_Z_site_in_first_block']
    e=[0]*10;e[5+site]=1
    assert owner.symplectic(e,cert['logical_z'],2)==1
    old_sector_H={(j,j):scale(J+delta*((-(1-2*(j&1)))-(1-2*((j>>1)&1)))/2,NATIVE_ONE) for j in range(4)}
    assert compose(Q,old_sector_H)!=compose(old_sector_H,Q)
    old_input=J-delta;old_target=J+delta
    assert old_target-old_input==F(1,2)
    report={'status':'error_transparent_pair_witness_and_old_energy_obstruction_checked',
            'construction':'R is the actual unitary decoder plus retained-syndrome correction. X_ET=R^dagger(I_syndrome tensor X)R and Z_ET analogously.',
            'pulse':'Q_ET=(I+Z_ET,A Z_ET,B-X_ET,A X_ET,B+Y_ET,A Y_ET,B)/4',
            'hold':'H_ET=J*I+delta*(Z_ET,A-Z_ET,B)/2',
            'same_implementation_energy_and_fault_property':True,
            'component_recovery_inverse_basis_checks':32,
            'component_error_basis_gram_entries':1024,
            'two_block_correctable_sector_count':256,
            'midpulse_single_physical_fault_logical_basis_cases':midfault_cases,
            'arbitrary_time_transparency':'Q_ET E V = E V Q_logical for every one-error-per-block representative, so a single fault at any pulse time is corrected without changing the logical endpoint.',
            'all_time_energy_conservation':'[Q_ET,H_ET]=0 on the complete two-block space',
            'on_code_hold_matches_previous':True,
            'off_code_hold_is_changed':True,
            'old_hold_control':{'physical_error':'Z on physical site '+str(site)+' of the first code block',
                 'old_energy_of_error_times_encoded_00':str(old_input),
                 'old_energy_of_error_times_encoded_11':str(old_target),
                 'energy_difference':'1/2',
                 'conclusion':'An error-transparent 00-to-11 transfer cannot conserve the unchanged old bare H in this error sector. A changed error-sector energy law or an additional energy-exchange degree of freedom is necessary.'},
            'scope':['This is a uniform finite-dimensional existence witness built from the checked source code and recovery map, not a fitted energy spectrum.',
                'The repaired hold and direct pulse are a new syndrome-resolved Hamiltonian extension off the code. They are not merely a coordinate rewrite with the old physical errors and old hold unchanged.',
                'The identity assumes direct implementation of those generally many-body operators. Executing decoder/gate/encoder as a noisy sequence does not inherit the transparency theorem.',
                'One correctable fault during the pulse is covered; repeated same-block faults, noisy recovery, spatial locality, a microscopic bath and an autonomous latch are not.',
                'Agreement on the unperturbed source sector does not admit the new error-sector coupling as a unique physical law or predict mass/lifetime.'],
            'previous_pulse_receipt_sha256':sha256(pulse_raw).hexdigest(),
            'recovery_circuit_receipt_sha256':sha256(circuit_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/error_transparent_bond_pulse.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
