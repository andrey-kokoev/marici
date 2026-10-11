"""Single-clock seam dressing and reversible source-interface recording.

The three admitted record involutions all receive H_R=(I-R)/2 in common
pi*hbar/tau units. Their admission is model input, not a physical electron ID.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_seam_occupation_energy import matrix, local_certificate
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint
from check_coupled_six_piece_belt import ONE
from check_pentachoron_spin_interfaces import A, S5, I, add, scale, mm

BASE = Path(__file__).resolve().parents[1]


def tensor(a,b,width):
    from check_coupled_six_piece_belt import mul
    return {(width*i+k,width*j+l):mul(v,w) for (i,j),v in a.items() for (k,l),w in b.items()}


def main():
    path = BASE/'results/native_operation_energy_lift_store.json'
    raw = path.read_bytes()
    belt = json.loads(raw)['carriers']['belt']
    d = tuple(map(F,belt['metric_denominators']))
    N = matrix(belt['return_entries'])
    projectors = [matrix(e['entries']) for e in belt['seam_projectors']]
    carrier_I = identity(36)
    bit_I = identity(2)
    bit_X = {(0,1):ONE,(1,0):ONE}
    bit_Z = plus({(0,0):ONE},times(-1,{(1,1):ONE}))
    whole_I = identity(72)
    metric = tuple(v for v in d for _ in range(2))
    R_occ = tensor(carrier_I,bit_Z,2)
    R_mix = tensor(carrier_I,bit_X,2)
    for P in projectors:
        # S=I-P in the occupied-carrier sector. Its parity consistency
        # reflection is (I-2S) tensor Z = (2P-I) tensor Z.
        R_cons = tensor(plus(times(2,P),times(-1,carrier_I)),bit_Z,2)
        for R in (R_occ,R_mix,R_cons):
            assert compose(R,R)==whole_I and adjoint(R,metric)==R
        H = times(F(1,2),plus(times(3,whole_I),times(-1,R_occ),times(-1,R_mix),times(-1,R_cons)))
        # On N, occupation and consistency sum to I. The remaining
        # elementary flip selects |+>, not a classical occupied bit.
        matched = times(F(1,2),plus(times(3,bit_I),times(-1,bit_X)))
        assert compose(H,tensor(N,bit_I,2))==tensor(N,matched,2)
        # Reversible QND recording of success: ready 0 -> success 1.
        U = plus(tensor(P,bit_I,2),tensor(plus(carrier_I,times(-1,P)),bit_X,2))
        assert compose(U,U)==whole_I and adjoint(U,metric)==U
        assert compose(U,tensor(N,bit_I,2))==tensor(N,bit_X,2)
    # Two addressed records retain ordering for general inputs. The inverse
    # uses the reverse schedule; neither carrier nor record is discarded.
    flip0 = {(i,i^2):ONE for i in range(4)}
    flip1 = {(i,i^1):ONE for i in range(4)}
    gates = [plus(tensor(P,identity(4),4),tensor(plus(carrier_I,times(-1,P)),flip,4))
             for P,flip in zip(projectors[:2],(flip0,flip1))]
    forward = compose(gates[1],gates[0])
    reverse = compose(gates[0],gates[1])
    assert forward != reverse
    assert compose(reverse,forward)==identity(144)

    # No fitted record parameters: each of occupation, consistency and flip
    # has coefficient one under the common involution rule. Thus epsilon=J=1,
    # g=1/2 and the flip contributes a common +1/2 energy constant.
    cert = local_certificate(F(1),F(1),F(1,2),S5,A(1))
    ev = cert['inactive_ground']+A(F(1,2))
    eb = cert['matched_ground']+A(F(1,2))
    delta = cert['relative_seam_energy']
    assert ev==(3-S5)/2 and eb==A(1) and delta==(S5-1)/2
    assert cert['matched_occupation']==A(F(1,2))
    assert cert['matched_occupation']-cert['inactive_occupation']==S5/5
    # Positive roots 1<sqrt(5)<3 imply 0<delta<kappa=1. Hence the preceding
    # noncommuting many-register bound applies despite epsilon=J=kappa.
    assert F(1)**2<F(5)<F(3)**2
    # Elementary isolated involution gap is 1; the actual inactive record's
    # dressed excitation gap is sqrt(5). They are distinct reference choices.
    ratio = 21*delta/S5
    assert ratio == F(21,2)*(A(1)-S5/5)
    # A consistent bit relabelling conjugates the whole model. It cannot
    # create a gap by merely renaming success and failure.
    X = ((A(0),A(1)),(A(1),A(0)))
    hv = ((A(F(1,2)),A(F(-1,2))),(A(F(-1,2)),A(F(5,2))))
    Pv = scale(S5.inverse(),add(scale(ev+S5,I),scale(A(-1),hv)))
    Pb = scale(A(F(1,2)),add(I,X))
    n = ((A(0),A(0)),(A(0),A(1)))
    mixing = scale(A(F(1,2)),add(I,scale(A(-1),X)))
    def expectation(H,P):
        product = mm(H,P)
        return product[0][0]+product[1][1]
    term_energies = {}
    for label,P,consistency,total in (
        ('inactive',Pv,n,ev),('matched',Pb,add(I,scale(A(-1),n)),eb)):
        values = [expectation(term,P) for term in (n,consistency,mixing)]
        assert sum(values,A(0))==total
        term_energies[label] = {key:value.record() for key,value in zip(('occupation','consistency','mixing'),values)}
    assert expectation(mm(X,mm(hv,X)),mm(X,mm(Pv,X)))==ev
    report = {
        'verification_passed':True,
        'source_seams':len(projectors),
        'common_rule':'H_R=(I-R)/2 in pi*hbar/tau units for each admitted involution',
        'admitted_record_operations':['occupation phase reflection I-2n','consistency parity reflection I-2(n-S)^2','record flip X'],
        'fixed_parameters':{'epsilon':'1','J':'1','g':'1/2','kappa':'1','flip_constant':'1/2'},
        'actual_seam_recording_reversible':True,
        'two_seam_order_matters_and_reverse_schedule_recovers_all_inputs':True,
        'carrier_return_preserved':True,
        'strict_stability':'0<(sqrt(5)-1)/2<1',
        'inactive_record_energy':ev.record(),
        'matched_record_energy':eb.record(),
        'extra_energy_per_seam':delta.record(),
        'belt_increment':(21*delta).record(),
        'matched_record_occupation':cert['matched_occupation'].record(),
        'inactive_record_occupation':cert['inactive_occupation'].record(),
        'excess_occupation_per_seam':(S5/5).record(),
        'term_energy_expectations':term_energies,
        'isolated_involution_gap':'1',
        'inactive_dressed_record_gap':'sqrt(5)',
        'belt_increment_in_inactive_record_gap_units':ratio.record(),
        'radical_basis':'mask 4 denotes sqrt(5); mask 0 denotes rational coefficient',
        'interpretation':'Single-clock candidate interaction fixes a spectrum and a response; source geometry does not by itself admit the three record operations or identify the reference excitation with an electron.',
        'physical_electron_or_neutron_mass_identified':False,
        'source_sha256':sha256(raw).hexdigest()
    }
    (BASE/'results/single_clock_seam_record.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
