"""Attack the inverse-leg rival against fixed source primitives and prefix gluing."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_shared_seam_observability import (
    identity, power, mm, mv, add, sub, scale, rank, transpose,
    TwoPacket, cycle_from_packets,
)

ROOT = Path(__file__).resolve().parents[3]


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    left = tuple(TwoPacket(*p) for p in [('AB','A','B'), ('BC','B','C'), ('CA','C','A')])
    right = tuple(TwoPacket(*p) for p in [('BA','B','A'), ('AD','A','D'), ('DB','D','B')])
    C = cycle_from_packets(left)
    check('both retained packet words select the same forward C', cycle_from_packets(right) == C)
    I = identity(3)
    Q = scale(add(add(I,C),power(C,2)),F(1,3))
    S = add(add(Q,scale(sub(I,Q),F(1,2))),scale(sub(C,transpose(C)),F(1,2)))
    inv = power(S,5)
    P = (I[0], I[2], I[1])
    check('native half phase squares to native successor', mm(S,S) == C)
    check('inverse half phase squares to inverse successor', mm(inv,inv) == power(C,2))
    defect = sub(mm(inv,inv),C)
    check('inverse half phase is not a native root except common line', rank(defect) == 2 and mv(defect,(1,1,1)) == (0,0,0))
    check('rival algebra remains correct', mm(mm(P,S),P) == inv)
    try:
        cycle_from_packets((right[0],right[2],right[1]))
    except ValueError:
        rejected = True
    else:
        rejected = False
    check('slot swap alone breaks source composability', rejected)
    reversed_right = tuple(TwoPacket(*p) for p in [('AB','A','B'), ('BD','B','D'), ('DA','D','A')])
    check('actual reversed directed word is composable', cycle_from_packets(reversed_right) == C)
    check('reversed word changes retained directed occurrences', {p.label for p in right}.isdisjoint({p.label for p in reversed_right}))
    check('reverse-word coordinate transport realizes inverse', mm(mm(scale(P,-1), C), scale(P,-1)) == power(C,2))
    # On Kminus(v), independent forward prefixes have seam defect
    # [h S^i - h S^(-j)]v. Six phases exhaust these operator readings.
    rows = {(i,j): tuple(a-b for a,b in zip(power(S,i)[0],power(S,(-j)%6)[0]))
            for i in range(6) for j in range(6)}
    check('all-state prefix gluing iff i+j is zero mod six',
          all((row == (0,0,0)) == ((i+j)%6 == 0) for (i,j),row in rows.items()))
    moves = [(i,j) for i in (0,1,2) for j in (0,1,2) if (i,j) != (0,0)]
    check('no nonidle first native I/S/C tick glues entire rival carrier', all(rows[m] != (0,0,0) for m in moves))
    v = (1,2,4)
    mismatches = {str(m): sum(a*b for a,b in zip(rows[m],v)) for m in moves}
    check('one explicit state defeats every nonidle native first tick', all(value != 0 for value in mismatches.values()))
    I5 = identity(5)
    R1 = (I5[0], I5[1], I5[2])
    R2 = (tuple(-a for a in I5[0]), I5[3], I5[4])
    Kplus = (I[0], I[1], I[2], tuple(-a for a in I[1]), tuple(-a for a in I[2]))
    check('same-orientation carrier positive control', all(
        mm((add(mm(power(S,i),R1),mm(power(S,i),R2))[0],),Kplus) == ((0,0,0),)
        for i in (1,2)))
    check('atomic inverse macro still glues', rows[(1,5)] == (0,0,0) and rows[(2,4)] == (0,0,0))
    check('even both legs forward once can immediately disagree', sum(a*b for a,b in zip(rows[(1,1)],v)) == -2)
    # Native right S instead of inverse S cannot realize Kminus(v)->Kminus(Sv).
    intertwining_defect = sub(mm(S,scale(P,-1)), mm(scale(P,-1),S))
    check('native intertwining survives only on common line', rank(intertwining_defect) == 2 and mv(intertwining_defect,(1,1,1)) == (0,0,0))
    paths = ['research/nima/triangle-half-phase-primitive.md',
             'research/nima/two-triangles-shared-edge-half-phase.md',
             'research/nima/checkers/check_triangle_half_phase.py',
             'research/nima/checkers/check_two_triangle_half_phase.py',
             'research/strominger/checkers/check_shared_seam_observability.py',
             'research/strominger/checkers/check_counteroriented_rival_source.py']
    report = {'status':'passed', 'check_count':len(checks), 'checks':checks,
              'native_root_defect':defect,
              'hostile_local_state':v, 'hostile_global_state':(1,2,4,-4,-2),
              'first_tick_seam_defects':mismatches,
              'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
              'disposition':{'inverse_leg_as_native_forward_half_phase':'refuted',
                             'forward_native_prefix_glued_compilation_on_full_Kminus':'refuted',
                             'atomic_inverse_leg_algebra':'survives',
                             'intended_PE_protocol':'not_selected'},
              'scope':'Prefix claim allows independent I,S,C per leg per tick, no arbitration, resets, extra state or hidden unglued prefixes. Atomic inverse operations or changed orientation are outside this execution model. No retained histories are equated by equal endpoint matrices.'}
    dest = ROOT/'research/strominger/results/counteroriented-rival-source.json'
    dest.write_text(json.dumps(report,indent=2,default=str)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'result':str(dest)}))


if __name__ == '__main__':
    main()
