"""Hostile relative-orientation test for the open P/E protocol conjecture.
Exact rational arithmetic, source operators, no fitted correction or particle labels.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from check_shared_seam_observability import identity, power, mm, mv, add, sub, scale, rank, transpose

ROOT = Path(__file__).resolve().parents[3]


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    I3, I5 = identity(3), identity(5)
    C = (I3[1], I3[2], I3[0])
    Q = scale(add(add(I3, C), mm(C, C)), F(1, 3))
    S = add(add(Q, scale(sub(I3, Q), F(1, 2))), scale(sub(C, transpose(C)), F(1, 2)))
    R1 = (I5[0], I5[1], I5[2])
    R2 = (tuple(-v for v in I5[0]), I5[3], I5[4])
    P = (I3[0], I3[2], I3[1])
    Kplus = (I3[0], I3[1], I3[2], tuple(-v for v in I3[1]), tuple(-v for v in I3[2]))
    Kminus = (I3[0], I3[1], I3[2], tuple(-v for v in I3[2]), tuple(-v for v in I3[1]))
    J = (tuple(-v for v in I5[0]), I5[3], I5[4], I5[1], I5[2])
    M = add(R1, R2)
    metric = add(mm(transpose(R1), R1), mm(transpose(R2), R2))
    left, right = ((1, 1, 1, 0, 0),), ((-1, 0, 0, 1, 1),)
    outer = add(left, right)
    check('declared local periods', power(C, 3) == I3 and power(S, 6) == I3)
    check('mirror fixes observed slot and is involutive', P[0] == I3[0] and mm(P, P) == I3)
    check('counteroriented restrictions', mm(R1, Kminus) == I3 and mm(R2, Kminus) == scale(P, -1))
    check('counteroriented reference action', mm(J, Kminus) == mm(Kminus, scale(P, -1)))
    check('counteroriented outer circulation zero', mm(outer, Kminus) == ((0, 0, 0),))
    check('same paired-occurrence metric', mm(mm(transpose(Kminus), metric), Kminus) == scale(I3, 2))
    check('intersection of two compatible carriers has dimension two', 5-rank(sub(R2, scale(mm(P, R1), -1)) + M) == 2)
    records = {}
    for name, T, inverse in [('C', C, power(C, 2)), ('S', S, power(S, 5))]:
        check(name + ' inverse is existing positive power', mm(T, inverse) == I3)
        check(name + ' mirror conjugates to inverse', mm(mm(P, T), P) == inverse)
        check(name + ' left intertwining', mm(R1, mm(Kminus, T)) == mm(T, mm(R1, Kminus)))
        check(name + ' right inverse intertwining', mm(R2, mm(Kminus, T)) == mm(inverse, mm(R2, Kminus)))
        rows = tuple(tuple(a+b for a,b in zip(mm(power(T,n), R1)[0], mm(power(inverse,n), R2)[0])) for n in range(6))
        check(name + ' counteroriented maximal carrier dimension three', rank(rows) == 2 and mm(rows, Kminus) == scale(mm(rows, Kminus), 0))
        check(name + ' local circulation preserved', mm(left, mm(Kminus,T)) == mm(left,Kminus) and mm(right,mm(Kminus,T)) == mm(right,Kminus))
        check(name + ' reference reverses schedule rather than commuting', mm(J,mm(Kminus,T)) == mm(Kminus,mm(inverse,scale(P,-1))))
        check(name + ' fixed orientation exchange commutator nonzero', mm(J,mm(Kminus,T)) != mm(Kminus,mm(T,scale(P,-1))))
        witness = mv(Kminus, I3[1])
        check(name + ' rival admissible input outside proposed K', mv(M,witness) != (0,0,0))
        common = I5[0]
        same_output = mv(Kplus, mv(T, mv(R1, common)))
        rival_output = mv(Kminus, mv(T, mv(R1, common)))
        check(name + ' same initially synchronized input separates protocols', same_output != rival_output and mv(M,rival_output) != (0,0,0))
        records[name] = {'counteroriented_seam_rows': rows, 'same_input': common,
                         'synchronized_output': same_output, 'counteroriented_output': rival_output,
                         'outside_K_witness': witness, 'reference_law': 'J F_T J = F_(T^-1) on Kminus, not J F_T J = F_T'}
    # Complete six-phase power census: each pair has period dividing six.
    dimensions = []
    for p in range(6):
        row = []
        for q in range(6):
            seam = tuple(tuple(a+b for a,b in zip(mm(power(S,p*n),R1)[0], mm(power(S,q*n),R2)[0])) for n in range(6))
            row.append(5-rank(seam))
        dimensions.append(row)
    check('identity control dimension five', dimensions[0][0] == 5)
    check('same nondegenerate local phase dimension three', all(dimensions[p][p] == 3 for p in (1,2,4,5)))
    check('inverse nondegenerate local phase dimension three', all(dimensions[p][(-p)%6] == 3 for p in (1,2,4,5)))
    check('half-return is not fully observable', dimensions[3][3] == 4)
    check('different frequency example leaves common fixed line', dimensions[1][2] == 1)
    paths = ['research/nima/triangle-half-phase-primitive.md',
             'research/nima/two-triangles-shared-edge-half-phase.md',
             'research/strominger/contracts/persistent-seam-pe-conjecture-net.v1.json',
             'research/strominger/checkers/check_persistent_seam_pe_falsification.py']
    report = {'status':'passed', 'check_count':len(checks), 'checks':checks, 'counteroriented_protocols':records,
              'six_phase_power_compatible_dimensions':dimensions,
              'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
              'disposition':{'seam_balance_and_transported_reference_select_same_orientation':'refuted',
                             'fixed_same_operator_observability_theorem':'unchanged',
                             'intended_PE_source_protocol':'not_decided',
                             'opposite_leg_orientation_source_selected':False},
              'scope':'Counterprotocol built from existing local powers with retained fixed port labels. It changes relative leg orientation/schedule and is not asserted to be selected by the intended source. Powers are operator identities, not erased retained execution records.'}
    dest = ROOT/'research/strominger/results/persistent-seam-pe-falsification.json'
    dest.write_text(json.dumps(report, indent=2, default=str)+'\n', encoding='utf-8')
    print(json.dumps({'status':'passed', 'checks':len(checks), 'dimensions':dimensions, 'result':str(dest)}))


if __name__ == '__main__':
    main()
